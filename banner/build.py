"""Build the studio-grade animated profile SVGs in assets/.

    python banner/build.py

Generates 4 paired dark/light SVGs (8 files total), switched in README.md with
<picture> and prefers-color-scheme:
- header-{dark,light}.svg       : Editorial hero + fluid neural/agentic retrieval
                                  constellation (MCP, RAG, EVAL, vLLM) with cubic
                                  Bezier data packets, signal streams & ripples.
- architecture-{dark,light}.svg : End-to-end Production AI Systems pipeline with
                                  left-to-right light pulses & sequential node glow.
- kpi-{dark,light}.svg          : 3 executive impact cards with subtle top-edge
                                  gradient shimmer sweep & soft corner glow.
- footer-{dark,light}.svg       : Minimal rounded signal-wave bar with clean
                                  typographic education & location line.

Design rules:
- 100% native GitHub-safe SMIL animations (zero external JS/fonts/images)
- Finished static first frame + prefers-reduced-motion media query
- Obsidian dark (#0D1117) and warm alabaster light (#FAFAF9) palettes
"""
import math
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

PALETTES = {
    "dark": dict(
        card_bg="#0D1117",
        card_surface="#161B22",
        card_op="0.92",
        border="#30363D",
        border_subtle="#21262D",
        grid="#8B949E",
        grid_op="0.11",
        name="#F0F6FC",
        muted="#8B949E",
        dim="#6E7681",
        accent="#D97757",      # warm terracotta
        highlight="#F2A679",   # warm highlight
        cyan="#38BDF8",        # obsidian cyan
        emerald="#34D399",     # live status emerald
        edge="#30363D",
        edge_op="0.80",
        node_bg="#161B22",
        aurora_a="#38BDF8",
        aurora_b="#D97757",
        aurora_c="#34D399",
        aurora_op=("0.16", "0.26"),
    ),
    "light": dict(
        card_bg="#FAFAF9",
        card_surface="#FFFFFF",
        card_op="0.96",
        border="#D6D3D1",
        border_subtle="#E7E5E4",
        grid="#78716C",
        grid_op="0.13",
        name="#1C1917",
        muted="#57534E",
        dim="#78716C",
        accent="#B4532F",      # deep terracotta
        highlight="#D97757",   # warm highlight
        cyan="#0F766E",        # deep teal
        emerald="#059669",     # live status emerald
        edge="#D6D3D1",
        edge_op="0.92",
        node_bg="#FFFFFF",
        aurora_a="#0F766E",
        aurora_b="#D97757",
        aurora_c="#059669",
        aurora_op=("0.09", "0.15"),
    ),
}

SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
EASE_OUT = "0.16 1 0.3 1"
EASE_SINE = "0.45 0 0.55 1"


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def intro(delay, dur, dy=0):
    t0 = f"{delay / (delay + dur):.3f}"
    out = (
        f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{t0};1" '
        f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT}" dur="{delay + dur:.2f}s" fill="freeze"/>'
    )
    if dy:
        out += (
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 {dy};0 {dy};0 0" keyTimes="0;{t0};1" '
            f'calcMode="spline" keySplines="0 0 1 1;{EASE_OUT}" dur="{delay + dur:.2f}s" fill="freeze"/>'
        )
    return out


# ------------------------------------------------------------------ 1. HEADER
def make_satellites(hubs, seed=11):
    """Faint satellite embedding points surrounding the 4 primary architectural hubs."""
    rng = random.Random(seed)
    pts = []
    hub_coords = [(x, y) for _, x, y, _ in hubs]
    while len(pts) < 24:
        x, y = rng.uniform(544, 922), rng.uniform(36, 232)
        if any(math.dist((x, y), h) < 34 for h in hub_coords):
            continue
        if any(math.dist((x, y), p) < 20 for p in pts):
            continue
        pts.append((x, y))
    return pts


def header(p):
    W, H = 960, 296
    # 4 primary architectural hubs in right canvas (x 540..926, y 36..234)
    hubs = [
        ("MCP", 594, 92, p["accent"]),
        ("RAG", 756, 66, p["cyan"]),
        ("EVAL", 872, 148, p["emerald"]),
        ("vLLM", 686, 198, p["cyan"]),
    ]
    satellites = make_satellites(hubs)

    # Faint satellite mesh (connect each satellite to its nearest hub + nearest neighbour)
    sat_edges = []
    for sx, sy in satellites:
        nh = min(hubs, key=lambda h: math.dist((sx, sy), (h[1], h[2])))
        if math.dist((sx, sy), (nh[1], nh[2])) < 115:
            sat_edges.append(f'    <line x1="{f(sx)}" y1="{f(sy)}" x2="{nh[1]}" y2="{nh[2]}"/>')
    sat_dots = "\n".join(f'    <circle cx="{f(x)}" cy="{f(y)}" r="2.1"/>' for x, y in satellites)

    # Smooth cubic Bezier routes between MCP, RAG, EVAL, vLLM
    routes = [
        ("M 594,92 C 654,54 704,54 756,66", p["accent"], 3.6, 0.0),
        ("M 756,66 C 824,78 854,104 872,148", p["cyan"], 3.8, 0.9),
        ("M 594,92 C 606,154 636,184 686,198", p["cyan"], 4.0, 1.4),
        ("M 686,198 C 762,208 824,186 872,148", p["emerald"], 3.7, 2.2),
        ("M 756,66 C 746,126 722,158 686,198", p["accent"], 4.4, 0.5),
        ("M 594,92 C 696,118 784,132 872,148", p["highlight"], 5.0, 2.8),
    ]

    route_svg = []
    for idx, (d, color, dur, begin) in enumerate(routes):
        # Base subtle Bezier track
        route_svg.append(
            f'    <path d="{d}" fill="none" stroke="{p["edge"]}" stroke-width="1.15" opacity="0.65"/>'
        )
        # Animated dashed signal stream along the curve
        route_svg.append(
            f'    <path d="{d}" fill="none" stroke="{color}" stroke-width="1.35" stroke-linecap="round" '
            f'stroke-dasharray="18 140" opacity="0.55">'
            f'<animate attributeName="stroke-dashoffset" from="158" to="0" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>'
            f'</path>'
        )
        # Glowing data packet traveling along cubic Bezier via inline animateMotion
        route_svg.append(
            f'    <g opacity="0.95">'
            f'<circle r="6.5" fill="{color}" opacity="0.22"/>'
            f'<circle r="2.6" fill="{color}"/>'
            f'<circle r="1.1" fill="#FFFFFF" opacity="0.9"/>'
            f'<animateMotion dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite" path="{d}"/>'
            f'</g>'
        )

    # Architectural hub nodes with staggered expanding ring ripples
    hub_svg = []
    for idx, (label, hx, hy, color) in enumerate(hubs):
        b = idx * 1.15
        hub_svg.append(
            f'    <g>\n'
            f'      <circle cx="{hx}" cy="{hy}" r="18" fill="none" stroke="{color}" stroke-width="1.2" opacity="0">\n'
            f'        <animate attributeName="r" values="17;31;31" keyTimes="0;0.45;1" dur="4.6s" begin="{b:.2f}s" repeatCount="indefinite"/>\n'
            f'        <animate attributeName="opacity" values="0.55;0;0" keyTimes="0;0.45;1" dur="4.6s" begin="{b:.2f}s" repeatCount="indefinite"/>\n'
            f'      </circle>\n'
            f'      <circle cx="{hx}" cy="{hy}" r="22" fill="{color}" opacity="0.10"/>\n'
            f'      <circle cx="{hx}" cy="{hy}" r="17" fill="{p["node_bg"]}" stroke="{color}" stroke-width="1.4"/>\n'
            f'      <text x="{hx}" y="{hy + 3.8}" text-anchor="middle" font-family="{MONO}" font-size="10.2" font-weight="600" letter-spacing="0.4" fill="{p["name"]}">{label}</text>\n'
            f'    </g>'
        )

    a0, a1 = p["aurora_op"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Kishor Hange — Forward Deployed, ML and AI Engineer at E2open, Bengaluru (~4 YOE). Enterprise Agents (MCP), Hybrid RAG, LLM Evals, Inference and Distributed Training.</title>
  <style>
    @media (max-width: 520px) {{ .topics {{ display: none; }} .satellites {{ opacity: 0.35; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="heroClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
    <clipPath id="barClip">
      <rect x="44" y="198" width="144" height="2.5" rx="1.25"/>
    </clipPath>
    <pattern id="dotGrid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="{p["grid"]}" opacity="{p["grid_op"]}"/>
    </pattern>
    <radialGradient id="auroraCyan">
      <stop offset="0" stop-color="{p["aurora_a"]}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{p["aurora_a"]}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{p["aurora_a"]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraWarm">
      <stop offset="0" stop-color="{p["aurora_b"]}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{p["aurora_c"]}" stop-opacity="0.25"/>
      <stop offset="1" stop-color="{p["aurora_c"]}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="accentBase" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{p["accent"]}"/>
      <stop offset="0.55" stop-color="{p["cyan"]}"/>
      <stop offset="1" stop-color="{p["emerald"]}" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="sweepGlow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- card surface -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#heroClip)">
    <!-- architectural dot grid on right canvas -->
    <rect x="512" y="0" width="448" height="{H}" fill="url(#dotGrid)"/>

    <!-- ambient breathing radial depth glows behind constellation -->
    <ellipse cx="786" cy="92" rx="195" ry="118" fill="url(#auroraCyan)" opacity="{a0}">
      <animate attributeName="opacity" values="{a0};{a1};{a0}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
      <animateTransform attributeName="transform" type="translate" values="-12 0;12 0;-12 0" dur="22s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
    </ellipse>
    <ellipse cx="690" cy="186" rx="180" ry="104" fill="url(#auroraWarm)" opacity="{a0}">
      <animate attributeName="opacity" values="{a1};{a0};{a1}" dur="16s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
    </ellipse>

    <!-- faint satellite embedding field -->
    <g class="satellites">
      <g stroke="{p["edge"]}" stroke-width="0.9" opacity="0.45">
{chr(10).join(sat_edges)}
      </g>
      <g fill="{p["muted"]}" opacity="0.38">
{sat_dots}
      </g>
    </g>

    <!-- fluid Bezier routes & glowing data packets -->
    <g>
{chr(10).join(route_svg)}
    </g>

    <!-- 4 architectural hub nodes -->
    <g>
{chr(10).join(hub_svg)}
    </g>

    <text x="920" y="272" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{p["dim"]}">agentic_graph · live_flow</text>

    <!-- left editorial identity -->
    <g>
      <circle cx="49" cy="50" r="3.2" fill="{p["emerald"]}"/>
      <circle cx="49" cy="50" r="3.2" fill="none" stroke="{p["emerald"]}" stroke-width="1.2" opacity="0.8">
        <animate attributeName="r" values="3.2;9.5;9.5" keyTimes="0;0.55;1" dur="2.8s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.75;0;0" keyTimes="0;0.55;1" dur="2.8s" repeatCount="indefinite"/>
      </circle>
      <text x="62" y="53.8" font-family="{MONO}" font-size="11" letter-spacing="1.1" fill="{p["muted"]}" font-weight="500">Production AI &amp; ML Systems</text>
    </g>

    <text x="44" y="118" font-family="{SANS}" font-size="64" font-weight="600" letter-spacing="-1.6" fill="{p["name"]}">Kishor Hange{intro(0.1, 0.8, 7)}</text>
    <text x="44" y="153" font-family="{SANS}" font-size="20.5" font-weight="500" fill="{p["muted"]}">Forward Deployed · ML &amp; AI Engineer{intro(0.22, 0.8, 5)}</text>
    <text x="44" y="180" font-family="{SANS}" font-size="15" fill="{p["dim"]}">E2open · Bengaluru · ~4 YOE{intro(0.32, 0.7, 3)}</text>

    <!-- smooth animated gradient accent underline sweep -->
    <rect x="44" y="198" width="144" height="2.5" rx="1.25" fill="url(#accentBase)"/>
    <g clip-path="url(#barClip)">
      <rect x="-12" y="198" width="56" height="2.5" fill="url(#sweepGlow)">
        <animate attributeName="x" values="-12;196;196" keyTimes="0;0.45;1" dur="5.2s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};0 0 1 1"/>
      </rect>
    </g>

    <!-- understated domain line -->
    <text class="topics" x="44" y="272" font-family="{MONO}" font-size="11" letter-spacing="0.35" fill="{p["muted"]}" opacity="0.9">Enterprise Agents (MCP) · Hybrid RAG · LLM Evals · Inference &amp; Distributed Training{intro(0.55, 0.6, 0)}</text>
  </g>

  <!-- crisp hairline border -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------ 2. ARCHITECTURE
def architecture(p):
    W, H = 960, 162
    stages = [
        ("01", "Enterprise Data", "&amp; MCP", "SQL · REST · Docs", p["accent"]),
        ("02", "RBAC &amp;", "Guardrails", "RLS · PII · Injection", p["cyan"]),
        ("03", "Hybrid RAG", "&amp; Agents", "BM25 · FAISS · DAG", p["emerald"]),
        ("04", "vLLM / ONNX", "Serving", "Quant · KV · Batch", p["cyan"]),
        ("05", "Evals &amp;", "OTel", "CI Gates · Metrics", p["accent"]),
    ]
    cw, ch, gap = 158, 86, 30
    start_x = 24  # 24 + 5*158 + 4*30 = 934, symmetric 24..936
    cy = 96       # vertical center of stage cards
    top_y = cy - ch // 2
    cycle = 6.0

    nodes_svg = []
    arrows_svg = []

    for i, (num, l1, l2, sub, color) in enumerate(stages):
        x = start_x + i * (cw + gap)
        cx = x + cw / 2
        # Sequential node border highlight timed to pulse arrival
        t_on = i * 0.95
        k1 = f"{t_on / cycle:.3f}"
        k2 = f"{(t_on + 0.35) / cycle:.3f}"
        k3 = f"{(t_on + 1.05) / cycle:.3f}"
        nodes_svg.append(
            f'    <g>\n'
            f'      <rect x="{x}" y="{top_y}" width="{cw}" height="{ch}" rx="12" fill="{p["card_surface"]}" stroke="{p["border"]}" stroke-width="1"/>\n'
            f'      <rect x="{x}" y="{top_y}" width="{cw}" height="{ch}" rx="12" fill="none" stroke="{color}" stroke-width="1.6" opacity="0.18">\n'
            f'        <animate attributeName="opacity" values="0.18;0.18;0.95;0.18;0.18" keyTimes="0;{k1};{k2};{k3};1" dur="{cycle:.1f}s" repeatCount="indefinite"/>\n'
            f'      </rect>\n'
            f'      <text x="{x + 12}" y="{top_y + 18}" font-family="{MONO}" font-size="9.5" font-weight="600" fill="{color}" opacity="0.9">{num}</text>\n'
            f'      <circle cx="{x + cw - 14}" cy="{top_y + 15}" r="2.5" fill="{color}" opacity="0.35">\n'
            f'        <animate attributeName="opacity" values="0.3;0.3;1;0.3;0.3" keyTimes="0;{k1};{k2};{k3};1" dur="{cycle:.1f}s" repeatCount="indefinite"/>\n'
            f'      </circle>\n'
            f'      <text x="{cx:.0f}" y="{top_y + 39}" text-anchor="middle" font-family="{SANS}" font-size="12.8" font-weight="600" fill="{p["name"]}">{l1}</text>\n'
            f'      <text x="{cx:.0f}" y="{top_y + 55}" text-anchor="middle" font-family="{SANS}" font-size="12.8" font-weight="600" fill="{p["name"]}">{l2}</text>\n'
            f'      <text x="{cx:.0f}" y="{top_y + 74}" text-anchor="middle" font-family="{MONO}" font-size="9.4" fill="{p["muted"]}">{sub}</text>\n'
            f'    </g>'
        )

        if i < len(stages) - 1:
            ax1 = x + cw + 2
            ax2 = x + cw + gap - 4
            path_d = f"M {ax1},{cy} L {ax2},{cy}"
            t_start = i * 0.95 + 0.35
            t_end = t_start + 0.65
            arrows_svg.append(
                f'    <g>\n'
                f'      <line x1="{ax1}" y1="{cy}" x2="{ax2 - 2}" y2="{cy}" stroke="{p["border"]}" stroke-width="1.3"/>\n'
                f'      <polygon points="{ax2},{cy} {ax2 - 6},{cy - 3.5} {ax2 - 6},{cy + 3.5}" fill="{p["muted"]}" opacity="0.8"/>\n'
                f'      <g opacity="0">\n'
                f'        <circle r="5.5" fill="{color}" opacity="0.28"/>\n'
                f'        <circle r="2.4" fill="{color}"/>\n'
                f'        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t_start / cycle:.3f};{(t_start + 0.08) / cycle:.3f};{(t_end - 0.08) / cycle:.3f};{t_end / cycle:.3f};1" dur="{cycle:.1f}s" repeatCount="indefinite"/>\n'
                f'        <animateMotion dur="{cycle:.1f}s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="0;{t_start / cycle:.3f};{t_end / cycle:.3f};1" calcMode="linear" path="{path_d}"/>\n'
                f'      </g>\n'
                f'    </g>'
            )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">End-to-End Production AI Architecture: Enterprise Data and MCP to RBAC and Guardrails to Hybrid RAG and Agents to vLLM/ONNX Serving to Evals and OpenTelemetry.</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="archClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#archClip)">
    <text x="24" y="31" font-family="{MONO}" font-size="10.2" font-weight="600" letter-spacing="1.4" fill="{p["muted"]}">END-TO-END PRODUCTION AI ARCHITECTURE</text>
    <text x="936" y="31" text-anchor="end" font-family="{MONO}" font-size="10" fill="{p["dim"]}">request → policy → retrieval → inference → telemetry</text>

    <!-- connecting arrows with sequential light pulses -->
{chr(10).join(arrows_svg)}

    <!-- 5 pipeline stage cards -->
{chr(10).join(nodes_svg)}
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------------ 3. KPI
def kpi(p):
    W, H = 960, 116
    cards = [
        ("−38%", "Inference Latency", "ONNX Runtime &amp; Optimum · E2open", p["accent"]),
        ("+9.5%", "Classifier Accuracy", "Word2Vec + RF &amp; Fine-Tuned BERT · E2open", p["cyan"]),
        ("CPython", "Open-Source Contributor", "Merged python/cpython#148978 · Production AI/ML", p["emerald"]),
    ]
    cw, ch, gap = 308, 112, 16
    xs = [2, 2 + cw + gap, 2 + 2 * (cw + gap)]
    defs = []
    blocks = []

    for i, (x, (metric, label, sub, color)) in enumerate(zip(xs, cards)):
        cx = x + cw / 2
        b = i * 2.0
        defs.append(
            f'    <clipPath id="kpiClip{i}"><rect x="{x}" y="2" width="{cw}" height="{ch}" rx="14"/></clipPath>\n'
            f'    <radialGradient id="kpiGlow{i}">\n'
            f'      <stop offset="0" stop-color="{color}" stop-opacity="0.28"/>\n'
            f'      <stop offset="1" stop-color="{color}" stop-opacity="0"/>\n'
            f'    </radialGradient>\n'
            f'    <linearGradient id="kpiSweep{i}" x1="0" y1="0" x2="1" y2="0">\n'
            f'      <stop offset="0" stop-color="{color}" stop-opacity="0"/>\n'
            f'      <stop offset="0.5" stop-color="{color}" stop-opacity="0.95"/>\n'
            f'      <stop offset="1" stop-color="{color}" stop-opacity="0"/>\n'
            f'    </linearGradient>'
        )
        blocks.append(
            f'  <g>\n'
            f'    <rect x="{x}" y="2" width="{cw}" height="{ch}" rx="14" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>\n'
            f'    <g clip-path="url(#kpiClip{i})">\n'
            f'      <!-- soft corner glow pulse -->\n'
            f'      <circle cx="{x + cw - 20}" cy="18" r="64" fill="url(#kpiGlow{i})" opacity="0.35">\n'
            f'        <animate attributeName="opacity" values="0.22;0.65;0.22" dur="7s" begin="{b:.1f}s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>\n'
            f'      </circle>\n'
            f'      <!-- subtle top-edge gradient shimmer sweep -->\n'
            f'      <rect x="{x - 90}" y="2" width="90" height="2" fill="url(#kpiSweep{i})">\n'
            f'        <animate attributeName="x" values="{x - 90};{x + cw + 20};{x + cw + 20}" keyTimes="0;0.42;1" dur="6.5s" begin="{b:.1f}s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};0 0 1 1"/>\n'
            f'      </rect>\n'
            f'      <rect x="{cx - 18:.0f}" y="15" width="36" height="2.2" rx="1.1" fill="{color}" opacity="0.85"/>\n'
            f'      <text x="{cx:.0f}" y="54" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="600" letter-spacing="-0.6" fill="{color}">{metric}</text>\n'
            f'      <text x="{cx:.0f}" y="78" text-anchor="middle" font-family="{SANS}" font-size="13.5" font-weight="500" fill="{p["name"]}">{label}</text>\n'
            f'      <text x="{cx:.0f}" y="98" text-anchor="middle" font-family="{MONO}" font-size="9.7" fill="{p["muted"]}">{sub}</text>\n'
            f'    </g>\n'
            f'    <rect x="{x}" y="2" width="{cw}" height="{ch}" rx="14" fill="none" stroke="{p["border"]}" stroke-width="1"/>\n'
            f'  </g>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Key Impact: -38% Inference Latency at E2open, +9.5% Classifier Accuracy at E2open, and CPython Open-Source Contributor (merged python/cpython#148978).</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
{chr(10).join(defs)}
  </defs>
{chr(10).join(blocks)}
</svg>
"""


# --------------------------------------------------------------- 4. FOOTER
def footer(p):
    W, H = 960, 74
    # Smooth subtle sine-wave signal line across the top third of the footer bar
    wave = (
        "M 24,22 C 110,12 190,32 280,22 C 370,12 450,32 540,22 "
        "C 630,12 710,32 800,22 C 855,16 900,26 936,22"
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">B.Tech CSE · DKTE Ichalkaranji (2019–2023) · CGPA 8.31 · Bengaluru, India</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="footClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14"/>
    </clipPath>
    <linearGradient id="waveGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{p["accent"]}" stop-opacity="0.15"/>
      <stop offset="0.35" stop-color="{p["cyan"]}" stop-opacity="0.75"/>
      <stop offset="0.7" stop-color="{p["emerald"]}" stop-opacity="0.75"/>
      <stop offset="1" stop-color="{p["accent"]}" stop-opacity="0.15"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#footClip)">
    <!-- subtle base signal wave -->
    <path d="{wave}" fill="none" stroke="{p["border_subtle"]}" stroke-width="1.2"/>
    <!-- animated flowing highlight wave -->
    <path d="{wave}" fill="none" stroke="url(#waveGrad)" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="120 820">
      <animate attributeName="stroke-dashoffset" from="940" to="0" dur="8s" repeatCount="indefinite"/>
    </path>
    <!-- soft traveling signal dot -->
    <g opacity="0.85">
      <circle r="4.5" fill="{p["cyan"]}" opacity="0.22"/>
      <circle r="2" fill="{p["cyan"]}"/>
      <animateMotion dur="8s" repeatCount="indefinite" path="{wave}"/>
    </g>

    <text x="480" y="52" text-anchor="middle" font-family="{MONO}" font-size="11.5" letter-spacing="0.4" fill="{p["muted"]}">B.Tech CSE · DKTE Ichalkaranji (2019–2023) · CGPA 8.31 · Bengaluru, India</text>
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for mode, pal in PALETTES.items():
        for name, build in (("header", header), ("architecture", architecture), ("kpi", kpi), ("footer", footer)):
            out = ASSETS / f"{name}-{mode}.svg"
            out.write_text(build(pal), encoding="utf-8", newline="\n")
            print(f"{out.name}: {out.stat().st_size / 1024:.1f} KB")
