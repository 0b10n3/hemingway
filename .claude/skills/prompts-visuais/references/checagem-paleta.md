# Checagem de paleta na imagem gerada (não só no prompt)

`graf-NN` e `diag-NN` são estruturalmente seguros porque o código lê
`../../../../../brand/tokens/syntaxis.tokens.json` em runtime — a cor é determinística. `ilu-NN` e a
capa dependem de um gerador de imagem externo (Nano Banana Pro), e geradores são conhecidos por
não aderir 100% ao hex pedido no prompt. O item 10 de `revisao-editorial/SKILL.md` audita hoje
só o **texto** do prompt (grep de hex em `capa.md`/`ilustracoes.md`/`infograficos.md`) — isso
confirma que o prompt só cita cor autorizada, não que a imagem final saiu com essa cor. Esta
checagem fecha essa lacuna, **só quando a imagem já foi de fato gerada** (PNG salvo em
`posts/<slug>/figuras/`) — se a peça ainda é só prompt, não há o que checar.

Decisão registrada em `pesquisa/epico-rascunhos-e-colagem/01-proposta.md`, Frente 3.2.
`Pillow` já está instalado no ambiente (confirmado nesta sessão, versão 12.1.1) — não é
dependência nova.

## Quando rodar

Etapa 9 (`revisao-editorial`), como parte do item 10, **só para peças com PNG existente** em
`posts/<slug>/figuras/`. Peças ainda em estágio de prompt seguem só com a checagem de texto já
existente.

## Método

1. Ler o PNG com Pillow, converter para RGB.
2. Quantizar para uma paleta de 32 cores e medir **a fração da área da imagem** que cada cor
   ocupa — não basta pegar "as N cores mais comuns" de um clustering pequeno: a primeira
   versão deste método (testada abaixo) fazia isso e forçava blend de borda/antialiasing em
   clusters que não correspondem a nenhuma região sólida real.
3. Descartar cores cuja área for menor que `MIN_SHARE` (ruído de borda, texto, artefato de
   compressão) — só cores que de fato cobrem uma fatia visível da peça entram na checagem.
4. Para cada cor que sobrar, achar o token mais próximo por distância euclidiana simples em RGB
   e reportar a distância.
5. Cor cuja distância ao token mais próximo passar da tolerância vira pendência para o gate
   humano — não é bloqueio automático, é sinalização, no mesmo espírito do item 10 atual.

**Validação real, feita nesta sessão:** a primeira versão do método (quantização direta para 6
cores, sem filtro de área) rodada contra `posts/2026-09-01-quando-os-modelos-se-rebelam/figuras/graf-01.png`
— uma peça comprovadamente on-brand, porque o código de `graf-01` lê os tokens direto em
runtime — acusou duas cores fora da tolerância. Falso positivo: o clustering pequeno forçava a
mistura de pixels de borda/gradiente em clusters que não existem como região sólida na peça.
A versão com quantização maior (32 cores) e filtro de área mínima (`MIN_SHARE = 0.02`, ou seja
2% da imagem) rodada contra a mesma peça deu **distância 0 nas três cores dominantes** (chalk,
`errorText`, `grove-500`, cobrindo juntas 96,7% da imagem) — é a versão registrada abaixo.

**Tolerância:** `RGB_DIST_MAX = 20` (escala de 0 a ~441, distância euclidiana em RGB de 8 bits)
— mais apertada que a primeira tentativa porque o filtro de área já eliminou o ruído que
exigia folga. Ainda é provisória: nenhuma imagem de `ilu-NN`/capa (gerada por IA, não por
código) passou por este script até agora — arte gerada por Nano Banana Pro pode ter gradiente
sutil mesmo em áreas "chapadas" que o Plotly nunca produz, e só um caso real revela se 20 é
apertado demais. Pergunta 1 de `01-proposta.md` continua aberta para o autor decidir o valor
definitivo depois da primeira geração.

## Script

```python
import sys
import json
from pathlib import Path
from PIL import Image

RGB_DIST_MAX = 20  # provisório — ver "Tolerância" acima
N_CLUSTERS = 32
MIN_SHARE = 0.02  # ignora cor que cobre menos de 2% da imagem (ruído de borda/antialiasing)

def carregar_tokens(caminho_tokens):
    dados = json.loads(Path(caminho_tokens).read_text())
    # percorre o DTCG procurando folhas com $value em formato hex
    tokens = {}
    def visitar(no, prefixo=""):
        if isinstance(no, dict):
            if "$value" in no and isinstance(no["$value"], str) and no["$value"].startswith("#"):
                tokens[prefixo.strip(".")] = no["$value"]
            else:
                for chave, valor in no.items():
                    if not chave.startswith("$"):
                        visitar(valor, f"{prefixo}.{chave}")
    visitar(dados)
    return tokens

def hex_para_rgb(hex_cor):
    hex_cor = hex_cor.lstrip("#")
    return tuple(int(hex_cor[i:i+2], 16) for i in (0, 2, 4))

def distancia(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def cores_dominantes_por_area(caminho_png, n_clusters=N_CLUSTERS, min_share=MIN_SHARE):
    img = Image.open(caminho_png).convert("RGB")
    total_pixels = img.width * img.height
    quantizada = img.quantize(colors=n_clusters, method=Image.MEDIANCUT)
    paleta = quantizada.getpalette()[: n_clusters * 3]
    contagem = quantizada.getcolors()
    contagem.sort(reverse=True)
    resultado = []
    for pixels, idx in contagem:
        fatia = pixels / total_pixels
        if fatia >= min_share:
            resultado.append((tuple(paleta[idx * 3: idx * 3 + 3]), fatia))
    return resultado

def checar(caminho_png, caminho_tokens):
    tokens = carregar_tokens(caminho_tokens)
    tokens_rgb = {nome: hex_para_rgb(hexv) for nome, hexv in tokens.items()}
    problemas = []
    for cor, fatia in cores_dominantes_por_area(caminho_png):
        nome_mais_perto, dist_minima = min(
            ((nome, distancia(cor, rgb)) for nome, rgb in tokens_rgb.items()),
            key=lambda par: par[1],
        )
        if dist_minima > RGB_DIST_MAX:
            problemas.append((cor, fatia, nome_mais_perto, round(dist_minima, 1)))
    return problemas

if __name__ == "__main__":
    caminho_png, caminho_tokens = sys.argv[1], sys.argv[2]
    problemas = checar(caminho_png, caminho_tokens)
    if not problemas:
        print(f"OK — todas as cores dominantes de {caminho_png} ficam dentro da tolerância.")
    else:
        print(f"Cores fora da tolerância em {caminho_png}:")
        for cor, fatia, token_perto, dist in problemas:
            print(f"  RGB{cor} ({fatia:.1%} da imagem) — mais próximo de {token_perto}, distância {dist} (limite {RGB_DIST_MAX})")
```

Uso: `python3 checagem-paleta.py posts/<slug>/figuras/capa.png ../../brand/tokens/syntaxis.tokens.json`
(ajuste os caminhos relativos ao diretório de execução).

## Saída

Cor fora da tolerância vira item na lista de pendências do gate humano (etapa 10), com a peça,
a cor encontrada e o token mais próximo — não corrija a imagem nem o token sozinho; quem decide
se é erro do gerador ou tolerância apertada demais é o autor.
