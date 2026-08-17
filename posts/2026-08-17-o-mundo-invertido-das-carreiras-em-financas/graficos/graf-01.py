"""
graf-01 — Duas trilhas: a ordem de referência e a ordem que eu segui.
Versão enxuta: só os marcadores numerados e a seta de direção por trilha —
descrição completa vive só no hover, não poluindo o gráfico estático.
Autocontido: lê o CSV ao lado (dados/graf-01.csv) e os tokens de marca/tokens.json,
exporta para ../figuras/graf-01.svg e .png. Rodar com: python3 graf-01.py
"""
import csv
import json
from pathlib import Path

import plotly.graph_objects as go

SCRIPT_DIR = Path(__file__).resolve().parent          # posts/<slug>/graficos
SLUG_DIR = SCRIPT_DIR.parent                           # posts/<slug>
REPO_ROOT = SLUG_DIR.parent.parent                     # raiz do repo
TOKENS_PATH = REPO_ROOT / "marca" / "tokens.json"
CSV_PATH = SCRIPT_DIR / "dados" / "graf-01.csv"
OUT_DIR = SLUG_DIR / "figuras"

# --- tokens: fonte única de cor (marca/tokens.json) ---
tokens = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))

COLOR_REFERENCIA = tokens["functional"]["success"]["hex"]  # volt-500, caminho recomendado
COLOR_AUTOR = tokens["functional"]["error"]["hex"]          # caminho que o autor seguiu

# --- dados (posts/<slug>/graficos/dados/graf-01.csv, versionado junto) ---
with CSV_PATH.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

trilhas = {}
for r in rows:
    trilhas.setdefault(r["trilha"], []).append(r)
for t in trilhas:
    trilhas[t].sort(key=lambda r: int(r["ordem"]))

X_REFERENCIA, X_AUTOR = 0, 2
X_LABELS = ["Ordem de referência", "A ordem que eu segui"]

fig = go.Figure()

for trilha, x_pos, color, nome in (
    ("referencia", X_REFERENCIA, COLOR_REFERENCIA, "Ordem de referência"),
    ("autor", X_AUTOR, COLOR_AUTOR, "A ordem que eu segui"),
):
    pontos = trilhas[trilha]
    ys = [int(p["nivel_y"]) for p in pontos]
    fig.add_trace(
        go.Scatter(
            x=[x_pos] * len(pontos),
            y=ys,
            mode="markers+text",
            marker=dict(size=26, color=color, line=dict(color=tokens["neutrals"]["obsidian"]["hex"], width=2)),
            text=[p["ordem"] for p in pontos],
            textposition="middle center",
            textfont=dict(color=tokens["neutrals"]["obsidian"]["hex"], size=14, family="JetBrains Mono, monospace"),
            name=nome,
            hovertext=[p["rotulo_completo"] for p in pontos],
            hoverinfo="text",
            showlegend=False,
        )
    )
    # seta de direção conectando o primeiro ao segundo ponto da trilha (ordem 1 -> 2)
    p_ini, p_fim = pontos[0], pontos[1]
    fig.add_annotation(
        x=x_pos,
        y=int(p_fim["nivel_y"]),
        ax=x_pos,
        ay=int(p_ini["nivel_y"]),
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.4,
        arrowwidth=4,
        arrowcolor=color,
        text="",
    )

fig.update_layout(
    title=dict(
        text="A ordem de referência — e a ordem que eu segui",
        font=dict(family="Space Grotesk, sans-serif", size=20, color=tokens["text"]["high"]["hex"]),
        x=0.5,
        xanchor="center",
        y=0.95,
    ),
    paper_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    plot_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    font=dict(family="Inter, sans-serif", color=tokens["text"]["medium"]["hex"]),
    margin=dict(l=60, r=60, t=110, b=70),
    xaxis=dict(
        tickmode="array",
        tickvals=[X_REFERENCIA, X_AUTOR],
        ticktext=X_LABELS,
        tickfont=dict(size=15, color=tokens["text"]["high"]["hex"]),
        range=[-1.0, 3.0],
        showgrid=False,
        zeroline=False,
    ),
    yaxis=dict(
        tickmode="array",
        tickvals=[1, 2],
        ticktext=["Base", "Topo"],
        tickfont=dict(size=15),
        range=[0.5, 2.5],
        gridcolor=tokens["dataviz"]["grid_line"],
        color=tokens["dataviz"]["axis_text"],
        zeroline=False,
    ),
    showlegend=False,
    width=1100,
    height=750,
)

OUT_DIR.mkdir(parents=True, exist_ok=True)
fig.write_image(str(OUT_DIR / "graf-01.svg"))
fig.write_image(str(OUT_DIR / "graf-01.png"), scale=2)
print("OK — figuras exportadas em", OUT_DIR)
