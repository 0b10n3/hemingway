# Checagem de sobrevivência do grão à recompressão de plataforma

`estilos-ilustracao.md` ("A escada") já trava um teto numérico para a granulação de fundo —
`illustration.grainMaxLuminanceAmplitude`, abaixo de 0,028 — mas esse teto nunca foi testado
contra o que de fato acontece à imagem depois que ela sai daqui: LinkedIn, Instagram e YouTube
recomprimem e redimensionam toda imagem enviada. Lacuna registrada três vezes
(`brand/DESIGN.md` §11 item 9, `brand/revisao-2026/_arquivo/.../03-proposta.md` B9/L2,
`brand/_arquivo/DECISOES-HERDADAS.md` P4) e nunca fechada.

Esta checagem fecha a lacuna com uma peça real, gerada especificamente para o teste
(`pesquisa/epico-sobrevivencia-graos/raw/teste-grao-v1.png`) — as peças reais mais antigas do
repositório (`ilu-01` de agosto) são anteriores à regra de degrau de tom/grão e não serviriam
de baseline válido.

**Pillow já está instalado no ambiente** (12.1.1, mesmo confirmado em `checagem-paleta.md`) —
sem dependência nova. Este script **não usa scipy** — o Laplaciano e a erosão de máscara são
implementados com fatiamento de array puro em `numpy` (também já disponível), pela mesma regra.

## Quando rodar

Uma vez por mudança de regra de granulação (não por peça publicada) — é uma checagem de
especificação, não um gate de PR por imagem. Rodar de novo se `illustration.grainMax*` mudar
de valor, ou se um novo perfil de entrega (nova plataforma, novo tamanho) entrar em uso.

## Método

1. Achar a cor de fundo dominante por quantização de área (mesmo método de
   `checagem-paleta.md`: 32 cores, ordenado por cobertura).
2. Construir uma máscara de "pixel de fundo puro" — distância euclidiana RGB até a cor
   dominante abaixo de um limiar (`BG_DIST_MAX = 18`) — e erodir essa máscara em 1px para
   descartar qualquer pixel cuja vizinhança 3×3 toque uma borda de recorte (evita que a aresta
   de uma forma de papel seja lida como grão).
3. Medir o grão como o desvio-padrão de um Laplaciano 4-vizinhos da luminância, calculado só
   nos pixels interiores da máscara — um proxy de alta frequência que isola ruído fino de
   qualquer gradiente suave ou vinheta de grande escala (testado: medir amplitude bruta
   min–max num recorte manual do canto capturava vinheta, não grão; o Laplaciano não).
4. Recomprimir a peça original em três perfis de entrega e remedir o mesmo Laplaciano na
   imagem recomprimida.
5. Reportar a razão `std_depois / std_antes` por perfil — sobrevivência do grão, não valor
   absoluto comparável byte a byte com o teto de 0,028 (métrica diferente da usada para medir
   o degrau entre camadas da pilha; ver nota de escala abaixo).

**Nota de escala.** `illustration.grainMaxLuminanceAmplitude` (0,028) foi medido como diferença
simples entre duas regiões chapadas (a mesma metodologia dos degraus da pilha, `01-referencias.md`
§1.2). O desvio-padrão do Laplaciano aqui é uma métrica distinta — não dá para comparar os dois
números diretamente como "acima/abaixo do teto". O que este script mede de novo, que nenhum
documento media antes, é a **razão de sobrevivência** através da recompressão real — essa razão
é a resposta à lacuna, independente da escala absoluta do teto.

## Perfis de recompressão testados

| Perfil | Redimensionamento | Formato | Qualidade JPEG |
| --- | --- | --- | --- |
| LinkedIn (post) | maior lado a 1200px | JPEG | 80 |
| YouTube (thumbnail) | recorte central 16:9, depois 1280×720 | JPEG | 90 |
| Instagram (feed) | 1080×1080 | JPEG | 80 |

Valores de qualidade/tamanho são a prática comum documentada para cada plataforma no momento
desta checagem (09/2026) — não são garantidos pela plataforma e podem mudar sem aviso. Se um
perfil mudar, rode de novo com o valor atualizado.

## Script

```python
import sys
import io
from pathlib import Path
from PIL import Image
import numpy as np

BG_DIST_MAX = 18  # distância RGB para um pixel contar como "fundo puro"
N_CLUSTERS = 32

PROFILES = {
    "linkedin_1200_q80": dict(size=(1200, 1200), quality=80, crop_16x9=False),
    "youtube_thumb_1280x720_q90": dict(size=(1280, 720), quality=90, crop_16x9=True),
    "instagram_1080_q80": dict(size=(1080, 1080), quality=80, crop_16x9=False),
}


def bg_mask(img, dist_max=BG_DIST_MAX):
    arr = np.asarray(img.convert("RGB")).astype(float)
    q = img.convert("RGB").quantize(colors=N_CLUSTERS, method=Image.MEDIANCUT)
    palette = q.getpalette()[: N_CLUSTERS * 3]
    counts = q.getcolors()
    counts.sort(reverse=True)
    dominant_idx = counts[0][1]
    dominant = np.array(palette[dominant_idx * 3 : dominant_idx * 3 + 3], dtype=float)
    dist = np.sqrt(((arr - dominant) ** 2).sum(axis=2))
    return dist < dist_max


def laplacian(lum):
    p = np.pad(lum, 1, mode="edge")
    return p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:] - 4 * lum


def erode(mask):
    p = np.pad(mask, 1, mode="constant", constant_values=False)
    out = mask.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            out &= p[1 + dy : 1 + dy + mask.shape[0], 1 + dx : 1 + dx + mask.shape[1]]
    return out


def grain_std(img):
    arr = np.asarray(img.convert("RGB")).astype(float)
    lum = (0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2]) / 255.0
    interior = erode(bg_mask(img))
    vals = laplacian(lum)[interior]
    return vals.std(), int(interior.sum())


def recomprimir(img, cfg):
    im = img.copy()
    if cfg.get("crop_16x9"):
        w, h = im.size
        new_h = int(w / (16 / 9))
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    im = im.resize(cfg["size"], Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=cfg["quality"])
    buf.seek(0)
    return Image.open(buf).convert("RGB"), len(buf.getvalue())


def checar(caminho_png):
    img = Image.open(caminho_png).convert("RGB")
    base_std, base_n = grain_std(img)
    print(f"ORIGINAL  grain_std={base_std:.5f}  pixels_interiores={base_n}  tamanho={img.size}")
    resultados = {}
    for nome, cfg in PROFILES.items():
        recompressa, n_bytes = recomprimir(img, cfg)
        std, n = grain_std(recompressa)
        sobrevivencia = std / base_std
        resultados[nome] = (std, n, sobrevivencia, n_bytes)
        print(
            f"{nome:30s} grain_std={std:.5f}  pixels={n:7d}  sobrevivência={sobrevivencia:.1%}  jpeg={n_bytes}B"
        )
    return base_std, resultados


if __name__ == "__main__":
    checar(sys.argv[1])
```

Uso: `python3 checagem-graos.py pesquisa/epico-sobrevivencia-graos/raw/teste-grao-v1.png`

## Resultado medido (09/2026, peça de teste desta checagem)

Peça: `pesquisa/epico-sobrevivencia-graos/raw/teste-grao-v1.png` (1024×1024, gerada via Nano
Banana Pro seguindo `_bloco-marca.md` à risca — fundo Deep Forest com grão fino uniforme, pilha
`nodeBranch` em forest.700/forest.500/grove.500, acento lime).

| Perfil | `grain_std` | Sobrevivência |
| --- | --- | --- |
| Original | 0,03633 | — (baseline) |
| LinkedIn (1200px, JPEG 80) | 0,02019 | **55,6%** |
| YouTube thumbnail (1280×720, JPEG 90) | 0,02157 | **59,4%** |
| Instagram feed (1080×1080, JPEG 80) | 0,01719 | **47,3%** |

**Achado real, não estimativa:** o grão perde entre 40% e 53% da sua amplitude de alta
frequência nos três perfis testados — nenhum perfil zera o grão, mas nenhum o preserva
integralmente. Instagram é o mais destrutivo dos três (recomprime mais perto do tamanho
original, o que deveria preservar mais detalhe, mas a qualidade JPEG 80 dominou o efeito).

**Consequência prática para o prompt-kit:** uma peça gerada com grão no **limite inferior** da
faixa aceitável arrisca ficar visualmente lisa depois de publicada — metade da amplitude de um
grão já sutil pode cair abaixo do que o olho percebe. Recomendação: ao escrever o prompt, mirar
a **metade superior** da faixa de granulação aceitável (mais perto do teto de 0,028 de
`illustration.grainMaxLuminanceAmplitude`, não do meio ou do piso), sabendo que a distribuição
social corta a amplitude quase pela metade. Isto não muda o teto — muda a instrução de "quanto
grão pedir" dentro dele.
