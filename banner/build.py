"""Build the profile banners in assets/.

    python banner/build.py

Header: editorial rounded-card hero with a kNN-retrieval constellation. About 39
embedding points sit in three clusters; every 8 s a query point appears, draws
hairlines to its 5 nearest neighbours, holds, and fades (one retrieval step).
Footer: matching rounded card with a token-by-token generation path ending in
an <|eos|> node.

Each banner is written in a dark and a light variant, switched in the README
with <picture>. Design rules:
- the first frame already reads as finished, even if nothing animates
- one primary motion (retrieval / generation) plus one ambient motion (aurora drift)
- SMIL only, so it animates reliably inside GitHub's <img> sandbox
"""
import math
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

PALETTES = {
    "dark": dict(
        card_bg="#161B22",
        card_op="0.62",
        border="#30363D",
        pill_bg="#21262D",
        pill_border="#30363D",
        pill_text="#C9D1D9",
        grid="#8B949E",
        grid_op="0.10",
        name="#F0F6FC",
        muted="#8B949E",
        accent="#D97757",
        highlight="#E8A15A",
        teal="#5EB1BF",
        edge="#30363D",
        edge_op=0.85,
        point="#8B949E",
        point_op=0.45,
        aurora=("#D97757", "#5EB1BF"),
        aurora_op=(0.20, 0.30),
    ),
    "light": dict(
        card_bg="#F6F8FA",
        card_op="0.82",
        border="#D0D7DE",
        pill_bg="#FFFFFF",
        pill_border="#D0D7DE",
        pill_text="#24292F",
        grid="#6E7781",
        grid_op="0.14",
        name="#1F2328",
        muted="#57606A",
        accent="#B4532F",
        highlight="#B4532F",
        teal="#2B7A87",
        edge="#D0D7DE",
        edge_op=1.0,
        point="#8C959F",
        point_op=0.52,
        aurora=("#E8A15A", "#5EB1BF"),
        aurora_op=(0.12, 0.18),
    ),
}
SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
EASE_OUT = "0.16 1 0.3 1"


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


# --------------------------------------------------------------- geometry
def make_points(seed=7):
    """Three loose clusters inside the constellation box (x 566-908, y 44-246)."""
    rng = random.Random(seed)
    clusters = [((650, 96), "mcp / agents"), ((834, 108), "hybrid rag"), ((744, 202), "ml systems")]
    pts = []
    for (cx, cy), _ in clusters:
        placed = 0
        while placed < 13:
            x, y = rng.gauss(cx, 40), rng.gauss(cy, 30)
            if not (566 <= x <= 908 and 44 <= y <= 246):
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


def pill(x, y, w, text, p, accent_dot=False):
    dot = (
        f'<circle cx="{x + 12}" cy="{y + 12}" r="2.6" fill="{p["accent"]}"/>'
        if accent_dot
        else f'<circle cx="{x + 12}" cy="{y + 12}" r="2.6" fill="{p["teal"]}"/>'
    )
    tx = x + 22
    return (
        f'    <g>'
        f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="12" fill="{p["pill_bg"]}" stroke="{p["pill_border"]}" stroke-width="1"/>'
        f'{dot}'
        f'<text x="{tx}" y="{y + 15.8}" font-family="{MONO}" font-size="11" fill="{p["pill_text"]}">{text}</text>'
        f'</g>'
    )


# ------------------------------------------------------------------ header
PERIOD = 24.0          # three queries, one every 8 s
SLOT = 8.0
FIRST = 1.8            # first retrieval starts after the intro
QUERIES = [(748, 146), (700, 68), (874, 182)]


def kt(*times):
    """keyTimes string for seconds within the 24 s period."""
    return ";".join(f"{t / PERIOD:.4f}".rstrip("0").rstrip(".") or "0" for t in times)


def header(p):
    pts, clusters = make_points()
    W, H = 960, 292

    edges = "\n".join(
        f'    <line x1="{f(pts[i][0])}" y1="{f(pts[i][1])}" x2="{f(pts[j][0])}" y2="{f(pts[j][1])}"/>'
        for i, j in idle_edges(pts))
    points = [f'    <circle cx="{f(x)}" cy="{f(y)}" r="2.8"/>' for x, y in pts]
    labels = "\n".join(
        f'    <text x="{cx}" y="{cy - 44 if name != "ml systems" else cy + 52}" text-anchor="middle">{name}</text>'
        for (cx, cy), name in clusters)

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
                f'    <line x1="{q[0]}" y1="{q[1]}" x2="{f(x)}" y2="{f(y)}" stroke="{p["accent"]}" stroke-width="1.35" '
                f'stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0.9">'
                f'<animate attributeName="stroke-dashoffset" values="1;1;0;0" keyTimes="{kt(0, s, e, PERIOD)}" '
                f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT};0 0 1 1" {begin}/>'
                f'<animate attributeName="opacity" values="0.9;0.9;0;0" keyTimes="{kt(0, 5.6, 6.6, PERIOD)}" {begin}/></line>')
        for j in nbrs:
            x, y = pts[j]
            tint = f'keyTimes="{kt(0, 1.8, 2.4, 5.6, 6.6, PERIOD)}" {begin}'
            g.append(
                f'    <circle cx="{f(x)}" cy="{f(y)}" r="8.5" fill="{p["teal"]}" opacity="0">'
                f'<animate attributeName="opacity" values="0;0;0.24;0.24;0;0" {tint}/></circle>'
                f'<circle cx="{f(x)}" cy="{f(y)}" r="3.5" fill="{p["teal"]}" opacity="0">'
                f'<animate attributeName="opacity" values="0;0;1;1;0;0" {tint}/></circle>')
        show = f'values="0;1;1;0;0" keyTimes="{kt(0, 0.6, 5.6, 6.6, PERIOD)}" {begin}'
        g.append(
            f'    <circle cx="{q[0]}" cy="{q[1]}" r="4.5" fill="none" stroke="{p["highlight"]}" stroke-width="1.4" opacity="0">'
            f'<animate attributeName="r" values="4.5;10.5;10.5" keyTimes="{kt(0, 0.6, PERIOD)}" {begin}/>'
            f'<animate attributeName="opacity" values="0.55;0;0" keyTimes="{kt(0, 0.6, PERIOD)}" {begin}/></circle>')
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

    pills_svg = "\n".join([
        pill(44, 186, 148, "E2open · ~4 YOE", p, accent_dot=True),
        pill(200, 186, 174, "CPython Contributor", p, accent_dot=False),
        pill(44, 218, 152, "100+ Merged PRs", p, accent_dot=False),
        pill(204, 218, 182, "588+ Automated Tests", p, accent_dot=True),
    ])

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Kishor Hange: Forward Deployed, ML and AI Engineer at E2open, Bengaluru (~4 YOE). Enterprise MCP agents, production RAG, LLM evals, inference optimization, and distributed training.</title>
  <style>
    @media (max-width: 520px) {{ .topics {{ display: none; }} .idle {{ opacity: 0.45; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="cardClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
    <pattern id="dotGrid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="{p["grid"]}" opacity="{p["grid_op"]}"/>
    </pattern>
    <radialGradient id="aurora">
      <stop offset="0" stop-color="{p["aurora"][0]}" stop-opacity="0.95"/>
      <stop offset="0.52" stop-color="{p["aurora"][1]}" stop-opacity="0.48"/>
      <stop offset="1" stop-color="{p["aurora"][1]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="depthGlow">
      <stop offset="0" stop-color="{p["aurora"][1]}" stop-opacity="0.32"/>
      <stop offset="1" stop-color="{p["aurora"][1]}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- rounded editorial card surface -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#cardClip)">
    <!-- subtle architectural dot grid on right canvas -->
    <rect x="520" y="0" width="440" height="{H}" fill="url(#dotGrid)"/>

    <!-- ambient: layered radial depth glow behind constellation (never behind name), 36 s drift -->
    <ellipse cx="810" cy="88" rx="190" ry="120" fill="url(#depthGlow)" opacity="{a0}"/>
    <ellipse cx="748" cy="146" rx="215" ry="132" fill="url(#aurora)" opacity="{a0}">
      <animate attributeName="opacity" values="{a0};{a1};{a0}" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
      <animateTransform attributeName="transform" type="translate" values="-16 0;16 0;-16 0" dur="36s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>
    </ellipse>

    <!-- idle embedding space -->
    <g class="idle">
    <g stroke="{p["edge"]}" stroke-width="1" opacity="{p["edge_op"]}">
{edges}
    </g>
    <g fill="{p["point"]}" opacity="{p["point_op"]}">
{chr(10).join(points)}
    </g>
    <g font-family="{MONO}" font-size="11" letter-spacing="1" fill="{p["muted"]}" opacity="0.88">
{labels}
    </g>
    </g>

    <!-- primary: retrieval, query -> top-5 neighbours -->
{chr(10).join(loops)}
    <text x="920" y="272" text-anchor="end" font-family="{MONO}" font-size="11" fill="{p["muted"]}" opacity="0.85">retrieve(q, k=5)</text>

    <!-- left editorial identity -->
    <g>
      <circle cx="49" cy="48" r="3" fill="{p["accent"]}"/>
      <text x="60" y="52" font-family="{MONO}" font-size="11" letter-spacing="1.6" fill="{p["accent"]}" font-weight="600">PRODUCTION AI SYSTEMS · BENGALURU, IN</text>
    </g>
    <text x="44" y="114" font-family="{SANS}" font-size="64" font-weight="600" letter-spacing="-1.6" fill="{p["name"]}">Kishor Hange{intro(0.12, 0.85, 8)}</text>
    <text x="44" y="148" font-family="{SANS}" font-size="20.5" font-weight="500" fill="{p["muted"]}">Forward Deployed · ML &amp; AI Engineer{intro(0.25, 0.85, 6)}</text>
    <rect x="44" y="166" width="44" height="2.5" rx="1.25" fill="{p["accent"]}" opacity="0.95">{intro(0.4, 0.6, 0)}</rect>

    <!-- proof pills -->
    <g class="pills">
{pills_svg}
    </g>

    <text class="topics" x="44" y="272" font-family="{MONO}" font-size="11.5" letter-spacing="0.9" fill="{p["muted"]}" opacity="0.88">MCP AGENTS · HYBRID RAG · LLM EVALS · INFERENCE · FSDP2{intro(0.65, 0.6, 0)}</text>
  </g>

  <!-- crisp hairline card border -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------------ footer
CHAIN = [(612, 108), (660, 74), (708, 100), (756, 62), (804, 92), (852, 58), (896, 84)]
F_PERIOD = 8.0
F_BEGIN = 1.2


def footer(p):
    W, H = 960, 156
    rng = random.Random(3)

    pts = []
    while len(pts) < 22:
        x, y = rng.uniform(596, 916), rng.uniform(22, 138)
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
    for i, ((x1, y1), (x2, y2)) in enumerate(zip(CHAIN, CHAIN[1:])):
        s, e = 0.2 + 0.3 * i, 0.5 + 0.3 * i
        anim.append(
            f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{p["accent"]}" stroke-width="1.35" stroke-linecap="round" '
            f'pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0.9">'
            f'<animate attributeName="stroke-dashoffset" values="1;1;0;0" keyTimes="{kt8(0, s, e, F_PERIOD)}" '
            f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT};0 0 1 1" {begin}/>'
            f'<animate attributeName="opacity" values="0.9;0.9;0;0" {fade}/></line>')
    for i, (x, y) in enumerate(CHAIN[:-1]):
        t = 0.2 + 0.3 * i
        tint = f'keyTimes="{kt8(0, t, t + 0.3, 5.6, 6.6, F_PERIOD)}" {begin}'
        anim.append(
            f'  <circle cx="{x}" cy="{y}" r="8" fill="{p["teal"]}" opacity="0"><animate attributeName="opacity" values="0;0;0.22;0.22;0;0" {tint}/></circle>'
            f'<circle cx="{x}" cy="{y}" r="3.4" fill="{p["teal"]}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" {tint}/></circle>')
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
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="footerClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
    <radialGradient id="aurora">
      <stop offset="0" stop-color="{p["aurora"][0]}" stop-opacity="0.9"/>
      <stop offset="0.55" stop-color="{p["aurora"][1]}" stop-opacity="0.45"/>
      <stop offset="1" stop-color="{p["aurora"][1]}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#footerClip)">
    <!-- ambient: aurora wash behind the constellation, 36 s drift -->
    <ellipse cx="756" cy="78" rx="185" ry="72" fill="url(#aurora)" opacity="{a0}">
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
    <text x="44" y="68" font-family="{SANS}" font-size="36" font-weight="600" letter-spacing="-0.8" fill="{p["name"]}">Thanks for visiting</text>
    <text class="sub" x="44" y="100" font-family="{SANS}" font-size="17" fill="{p["muted"]}">Building fast, measurable, and reliable AI systems.</text>
    <text x="44" y="132" font-family="{MONO}" font-size="12" letter-spacing="1.2" fill="{p["muted"]}">BENGALURU, IN · FDE · ML · AI SYSTEMS <tspan fill="{p["highlight"]}">▍<animate attributeName="fill-opacity" values="1;0" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/></tspan></text>
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------------ kpi strip
def kpi(p):
    W, H = 960, 112
    cards = [
        ("−38%", "Inference Latency", "ONNX Runtime &amp; Optimum · E2open", p["accent"]),
        ("+9.5%", "Classifier Accuracy", "Custom Word2Vec + RF &amp; BERT · E2open", p["teal"]),
        ("588+ Tests · 100+ PRs", "Verified Engineering", "9 Production Repos + CPython PR", p["accent"]),
    ]
    cw, ch, gap = 308, 108, 16
    xs = [2, 2 + cw + gap, 2 + 2 * (cw + gap)]
    blocks = []
    for x, (metric, label, sub, color) in zip(xs, cards):
        cx = x + cw / 2
        fs = "22" if len(metric) > 10 else "27"
        blocks.append(
            f'  <g>\n'
            f'    <rect x="{x}" y="2" width="{cw}" height="{ch}" rx="14" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}" stroke="{p["border"]}" stroke-width="1"/>\n'
            f'    <rect x="{cx - 16:.0f}" y="14" width="32" height="2.5" rx="1.25" fill="{color}" opacity="0.9"/>\n'
            f'    <text x="{cx:.0f}" y="52" text-anchor="middle" font-family="{SANS}" font-size="{fs}" font-weight="600" letter-spacing="-0.6" fill="{color}">{metric}</text>\n'
            f'    <text x="{cx:.0f}" y="76" text-anchor="middle" font-family="{SANS}" font-size="13.5" font-weight="500" fill="{p["name"]}">{label}</text>\n'
            f'    <text x="{cx:.0f}" y="95" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{p["muted"]}">{sub}</text>\n'
            f'  </g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Key Impact Metrics: -38% Inference Latency at E2open, +9.5% Classifier Accuracy at E2open, 588+ Tests and 100+ PRs across 9 production repos plus a merged CPython PR.</title>
{chr(10).join(blocks)}
</svg>
"""


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for mode, pal in PALETTES.items():
        for name, build in (("header", header), ("kpi", kpi), ("footer", footer)):
            out = ASSETS / f"{name}-{mode}.svg"
            out.write_text(build(pal), encoding="utf-8", newline="\n")
            print(f"{out.name}: {out.stat().st_size / 1024:.1f} KB")
