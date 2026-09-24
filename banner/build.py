"""Build the profile banners in assets/.

    python banner/build.py

Header: a kNN-retrieval constellation. About 40 embedding points sit in three
clusters; every 8 s a query point appears, draws hairlines to its 5 nearest
neighbours, holds, and fades (one retrieval step). Footer: same layout and
palette; a hairline draws token by token through the constellation until it
reaches an <|eos|> node (one generation step).

Each banner is written in a dark and a light variant, switched in the README
with <picture>. Design rules:
- the first frame already reads as finished, even if nothing animates
- one primary motion (retrieval) plus one ambient motion (aurora drift)
- SMIL only, so it animates inside GitHub's <img> sandbox
"""
import math
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

PALETTES = {
    "dark": dict(name="#E6EDF3", muted="#8B949E", accent="#D97757", highlight="#E8A15A", teal="#5EB1BF",
                 edge="#30363D", edge_op=0.9, point="#8B949E", point_op=0.4,
                 aurora=("#D97757", "#5EB1BF"), aurora_op=(0.18, 0.28)),
    "light": dict(name="#1F2328", muted="#59636E", accent="#B4532F", highlight="#B4532F", teal="#2B7A87",
                  edge="#D0D7DE", edge_op=1.0, point="#8C959F", point_op=0.5,
                  aurora=("#E8A15A", "#5EB1BF"), aurora_op=(0.10, 0.16)),
}
SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
EASE_OUT = "0.16 1 0.3 1"


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


# --------------------------------------------------------------- geometry
def make_points(seed=7):
    """Three loose clusters inside the constellation box (x 560-912, y 36-244)."""
    rng = random.Random(seed)
    clusters = [((650, 92), "agents"), ((832, 104), "retrieval"), ((742, 196), "fine-tuning")]
    pts = []
    for (cx, cy), _ in clusters:
        placed = 0
        while placed < 13:
            x, y = rng.gauss(cx, 40), rng.gauss(cy, 30)
            if not (566 <= x <= 906 and 42 <= y <= 238):
                continue
            if any(math.dist((x, y), p) < 15 for p in pts):
                continue
            pts.append((x, y))
            placed += 1
    return pts, clusters


def knn(q, pts, k):
    return sorted(range(len(pts)), key=lambda i: math.dist(q, pts[i]))[:k]


def idle_edges(pts, k=2):
    edges = set()
    for i, p in enumerate(pts):
        for j in knn(p, pts, k + 1)[1:]:
            edges.add(tuple(sorted((i, j))))
    return sorted(edges)


# ------------------------------------------------------------------ header
PERIOD = 24.0          # three queries, one every 8 s
SLOT = 8.0
FIRST = 1.8            # first retrieval starts after the intro
QUERIES = [(748, 140), (700, 62), (872, 176)]


def kt(*times):
    """keyTimes string for seconds within the 24 s period."""
    return ";".join(f"{t / PERIOD:.4f}".rstrip("0").rstrip(".") or "0" for t in times)


def header(p):
    pts, clusters = make_points()
    W, H = 960, 280

    # idle constellation: faint kNN graph + points (static, so the first frame is complete)
    edges = "\n".join(
        f'    <line x1="{f(pts[i][0])}" y1="{f(pts[i][1])}" x2="{f(pts[j][0])}" y2="{f(pts[j][1])}"/>'
        for i, j in idle_edges(pts))
    points = [f'    <circle cx="{f(x)}" cy="{f(y)}" r="2.8"/>' for x, y in pts]
    labels = "\n".join(
        f'    <text x="{cx}" y="{cy - 44 if name != "fine-tuning" else cy + 52}" text-anchor="middle">{name}</text>'
        for (cx, cy), name in clusters)

    # retrieval loop: each query gets one 8 s slot inside the 24 s period
    loops = []
    for qi, q in enumerate(QUERIES):
        begin = f'begin="{FIRST + qi * SLOT:.1f}s" dur="{PERIOD:.0f}s" repeatCount="indefinite"'
        nbrs = knn(q, pts, 5)
        g = [f'  <g><!-- query {qi + 1} -->']
        for n_i, j in enumerate(nbrs):
            x, y = pts[j]
            s = 0.6 + 0.12 * n_i
            e = s + 0.72
            g.append(
                f'    <line x1="{q[0]}" y1="{q[1]}" x2="{f(x)}" y2="{f(y)}" stroke="{p["accent"]}" stroke-width="1.3" '
                f'stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0.9">'
                f'<animate attributeName="stroke-dashoffset" values="1;1;0;0" keyTimes="{kt(0, s, e, PERIOD)}" '
                f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT};0 0 1 1" {begin}/>'
                f'<animate attributeName="opacity" values="0.9;0.9;0;0" keyTimes="{kt(0, 5.6, 6.6, PERIOD)}" {begin}/></line>')
        for j in nbrs:
            x, y = pts[j]
            tint = f'keyTimes="{kt(0, 1.8, 2.4, 5.6, 6.6, PERIOD)}" {begin}'
            g.append(
                f'    <circle cx="{f(x)}" cy="{f(y)}" r="8" fill="{p["teal"]}" opacity="0">'
                f'<animate attributeName="opacity" values="0;0;0.22;0.22;0;0" {tint}/></circle>'
                f'<circle cx="{f(x)}" cy="{f(y)}" r="3.4" fill="{p["teal"]}" opacity="0">'
                f'<animate attributeName="opacity" values="0;0;1;1;0;0" {tint}/></circle>')
        show = f'values="0;1;1;0;0" keyTimes="{kt(0, 0.6, 5.6, 6.6, PERIOD)}" {begin}'
        g.append(
            f'    <circle cx="{q[0]}" cy="{q[1]}" r="4.5" fill="none" stroke="{p["highlight"]}" stroke-width="1.4" opacity="0">'
            f'<animate attributeName="r" values="4.5;10;10" keyTimes="{kt(0, 0.6, PERIOD)}" {begin}/>'
            f'<animate attributeName="opacity" values="0.5;0;0" keyTimes="{kt(0, 0.6, PERIOD)}" {begin}/></circle>')
        g.append(f'    <circle cx="{q[0]}" cy="{q[1]}" r="5" fill="{p["accent"]}" opacity="0"><animate attributeName="opacity" {show}/></circle>')
        g.append(f'    <circle cx="{q[0]}" cy="{q[1]}" r="2" fill="{p["highlight"]}" opacity="0"><animate attributeName="opacity" {show}/></circle>')
        g.append("  </g>")
        loops.append("\n".join(g))

    a0, a1 = p["aurora_op"]
    intro = lambda delay, dur, dy: (
        f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{delay / (delay + dur):.3f};1" '
        f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT}" dur="{delay + dur:.2f}s" fill="freeze"/>'
        + (f'<animateTransform attributeName="transform" type="translate" values="0 {dy};0 {dy};0 0" '
           f'keyTimes="0;{delay / (delay + dur):.3f};1" calcMode="spline" keySplines="0 0 1 1;{EASE_OUT}" '
           f'dur="{delay + dur:.2f}s" fill="freeze"/>' if dy else ""))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Kishor Hange: Software Engineer at E2open, Bengaluru. LLM apps, RAG, fine-tuning, AI agents.</title>
  <style>
    @media (max-width: 520px) {{ .topics {{ display: none; }} .idle {{ opacity: 0.5; }} }}
  </style>
  <defs>
    <radialGradient id="aurora">
      <stop offset="0" stop-color="{p["aurora"][0]}" stop-opacity="0.9"/>
      <stop offset="0.55" stop-color="{p["aurora"][1]}" stop-opacity="0.45"/>
      <stop offset="1" stop-color="{p["aurora"][1]}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- ambient: one aurora wash behind the constellation (never behind the name), 36 s drift -->
  <ellipse cx="748" cy="140" rx="200" ry="122" fill="url(#aurora)" opacity="{a0}">
    <animate attributeName="opacity" values="{a0};{a1};{a0}" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
    <animateTransform attributeName="transform" type="translate" values="-18 0;18 0;-18 0" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
  </ellipse>

  <!-- idle embedding space -->
  <g class="idle">
  <g stroke="{p["edge"]}" stroke-width="1" opacity="{p["edge_op"]}">
{edges}
  </g>
  <g fill="{p["point"]}" opacity="{p["point_op"]}">
{chr(10).join(points)}
  </g>
  <g font-family="{MONO}" font-size="11" letter-spacing="1" fill="{p["muted"]}" opacity="0.85">
{labels}
  </g>
  </g>

  <!-- primary: retrieval, query -> top-5 neighbours -->
{chr(10).join(loops)}
  <text x="912" y="268" text-anchor="end" font-family="{MONO}" font-size="11" fill="{p["muted"]}" opacity="0.85">retrieve(q, k=5)</text>

  <!-- type -->
  <text x="48" y="118" font-family="{SANS}" font-size="72" font-weight="600" letter-spacing="-1.5" fill="{p["name"]}">Kishor Hange{intro(0.15, 0.9, 8)}</text>
  <text x="48" y="158" font-family="{SANS}" font-size="24" fill="{p["muted"]}">Software Engineer · E2open · Bengaluru{intro(0.3, 0.9, 8)}</text>
  <g class="topics" font-family="{MONO}" font-size="14.5" letter-spacing="1.2" fill="{p["muted"]}">
    <text x="48" y="202">LLM APPS · RAG · AI AGENTS{intro(0.65, 0.6, 0)}</text>
    <text x="48" y="226">FINE-TUNING: LoRA · QLoRA · DPO · GRPO{intro(0.75, 0.6, 0)}</text>
  </g>
</svg>
"""


# ------------------------------------------------------------------ footer
# A generation step: tokens are produced one by one along this chain,
# ending in the <|eos|> node (last point).
CHAIN = [(612, 112), (660, 78), (708, 104), (756, 66), (804, 96), (852, 62), (896, 88)]
F_PERIOD = 8.0
F_BEGIN = 1.2


def footer(p):
    W, H = 960, 160
    rng = random.Random(3)

    # idle constellation around the chain, same style as the header
    pts = []
    while len(pts) < 22:
        x, y = rng.uniform(596, 916), rng.uniform(24, 146)
        if any(math.dist((x, y), q) < 16 for q in pts) or any(math.dist((x, y), c) < 14 for c in CHAIN):
            continue
        pts.append((x, y))
    edges = "\n".join(
        f'    <line x1="{f(pts[i][0])}" y1="{f(pts[i][1])}" x2="{f(pts[j][0])}" y2="{f(pts[j][1])}"/>'
        for i, j in idle_edges(pts))
    points = "\n".join(f'    <circle cx="{f(x)}" cy="{f(y)}" r="2.6"/>' for x, y in pts + CHAIN[:-1])
    chain_d = "M" + " L".join(f"{x},{y}" for x, y in CHAIN)

    kt8 = lambda *ts: ";".join(f"{t / F_PERIOD:.4f}".rstrip("0").rstrip(".") or "0" for t in ts)
    begin = f'begin="{F_BEGIN}s" dur="{F_PERIOD:.0f}s" repeatCount="indefinite"'
    fade = f'keyTimes="{kt8(0, 5.6, 6.6, F_PERIOD)}" {begin}'

    anim = []
    # the hairline draws token to token (accent), like the header's retrieval lines
    for i, ((x1, y1), (x2, y2)) in enumerate(zip(CHAIN, CHAIN[1:])):
        s, e = 0.2 + 0.3 * i, 0.5 + 0.3 * i
        anim.append(
            f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{p["accent"]}" stroke-width="1.3" stroke-linecap="round" '
            f'pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0.9">'
            f'<animate attributeName="stroke-dashoffset" values="1;1;0;0" keyTimes="{kt8(0, s, e, F_PERIOD)}" '
            f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT};0 0 1 1" {begin}/>'
            f'<animate attributeName="opacity" values="0.9;0.9;0;0" {fade}/></line>')
    # each generated token tints teal as the line reaches it
    for i, (x, y) in enumerate(CHAIN[:-1]):
        t = 0.2 + 0.3 * i
        tint = f'keyTimes="{kt8(0, t, t + 0.3, 5.6, 6.6, F_PERIOD)}" {begin}'
        anim.append(
            f'  <circle cx="{x}" cy="{y}" r="8" fill="{p["teal"]}" opacity="0"><animate attributeName="opacity" values="0;0;0.22;0.22;0;0" {tint}/></circle>'
            f'<circle cx="{x}" cy="{y}" r="3.4" fill="{p["teal"]}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" {tint}/></circle>')
    # <|eos|>: always visible (finished first frame), pulses when generation reaches it
    ex, ey = CHAIN[-1]
    t_eos = 0.2 + 0.3 * (len(CHAIN) - 1)
    anim.append(
        f'  <circle cx="{ex}" cy="{ey}" r="5" fill="none" stroke="{p["highlight"]}" stroke-width="1.4" opacity="0">'
        f'<animate attributeName="r" values="5;5;11;11" keyTimes="{kt8(0, t_eos, t_eos + 0.6, F_PERIOD)}" {begin}/>'
        f'<animate attributeName="opacity" values="0;0.6;0;0" keyTimes="{kt8(0, t_eos, t_eos + 0.6, F_PERIOD)}" {begin}/></circle>')
    anim.append(f'  <circle cx="{ex}" cy="{ey}" r="5" fill="{p["accent"]}"/>'
                f'<circle cx="{ex}" cy="{ey}" r="2" fill="{p["highlight"]}"/>')

    a0, a1 = p["aurora_op"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Thanks for visiting. Kishor Hange, Bengaluru, IN</title>
  <style>
    @media (max-width: 520px) {{ .sub {{ display: none; }} }}
  </style>
  <defs>
    <radialGradient id="aurora">
      <stop offset="0" stop-color="{p["aurora"][0]}" stop-opacity="0.9"/>
      <stop offset="0.55" stop-color="{p["aurora"][1]}" stop-opacity="0.45"/>
      <stop offset="1" stop-color="{p["aurora"][1]}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- ambient: aurora wash behind the constellation, 36 s drift -->
  <ellipse cx="756" cy="82" rx="180" ry="72" fill="url(#aurora)" opacity="{a0}">
    <animate attributeName="opacity" values="{a0};{a1};{a0}" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
    <animateTransform attributeName="transform" type="translate" values="-14 0;14 0;-14 0" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
  </ellipse>

  <!-- idle embedding space + the path the next generation will take -->
  <g stroke="{p["edge"]}" stroke-width="1" opacity="{p["edge_op"]}">
{edges}
  </g>
  <path d="{chain_d}" fill="none" stroke="{p["edge"]}" stroke-width="1" opacity="{p["edge_op"]}"/>
  <g fill="{p["point"]}" opacity="{p["point_op"]}">
{points}
  </g>
  <text x="{ex}" y="{ey + 26}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="600" fill="{p["accent"]}">&lt;|eos|&gt;</text>

  <!-- primary: generation, token by token until <|eos|> -->
{chr(10).join(anim)}

  <!-- type -->
  <text x="48" y="74" font-family="{SANS}" font-size="40" font-weight="600" letter-spacing="-0.8" fill="{p["name"]}">Thanks for visiting</text>
  <text class="sub" x="48" y="106" font-family="{SANS}" font-size="18" fill="{p["muted"]}">Let's build something intelligent together.</text>
  <text x="48" y="136" font-family="{MONO}" font-size="13" letter-spacing="1.2" fill="{p["muted"]}">BENGALURU, IN <tspan fill="{p["highlight"]}">▍<animate attributeName="fill-opacity" values="1;0" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/></tspan></text>
</svg>
"""


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for mode, pal in PALETTES.items():
        for name, build in (("header", header), ("footer", footer)):
            out = ASSETS / f"{name}-{mode}.svg"
            out.write_text(build(pal), encoding="utf-8", newline="\n")
            print(f"{out.name}: {out.stat().st_size / 1024:.1f} KB")
