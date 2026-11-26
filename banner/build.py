"""Build the unified dark/light animated SVG design system in assets/.

    python banner/build.py

Generates 22 paired dark/light SVGs (11 visual components), switched in
README.md via <picture> and prefers-color-scheme:
- header-{dark,light}.svg         : Live-Telemetry Bento Hero with glassmorphic
                                    AI Systems Topology (MCP/RAG/EVAL/vLLM) +
                                    live-cycling SMIL telemetry bar & sparkline.
- card-{1..6}-{dark,light}.svg    : 6 borderless rounded (410x176) Flagship
                                    System bento product cards with micro-icons,
                                    tech pills, breathing accent dot & metric pill.
- stack-{dark,light}.svg          : 4-Layer Architectural Engineering Stack
                                    Blueprint with vertical signal bus pulses.
- architecture-{dark,light}.svg   : End-to-end Production AI Systems pipeline.
- kpi-{dark,light}.svg            : 3 executive impact cards with shimmer sweep.
- footer-{dark,light}.svg         : Minimal rounded signal-wave footer bar.

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
        glass_bg="#161B22",
        glass_op="0.72",
        pill_bg="#21262D",
        card_op="0.94",
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
        glass_bg="#FFFFFF",
        glass_op="0.78",
        pill_bg="#F5F5F4",
        card_op="0.97",
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


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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


# ---------------------------------------------------------- 1. LIVE-TELEMETRY HERO
def make_satellites(hubs, seed=11):
    """Faint satellite embedding points inside the right glassmorphic topology panel."""
    rng = random.Random(seed)
    pts = []
    hub_coords = [(x, y) for _, x, y, _ in hubs]
    while len(pts) < 18:
        x, y = rng.uniform(524, 916), rng.uniform(44, 198)
        if any(math.dist((x, y), h) < 32 for h in hub_coords):
            continue
        if any(math.dist((x, y), p) < 20 for p in pts):
            continue
        pts.append((x, y))
    return pts


def header(p):
    W, H = 960, 296
    # 4 architectural hub nodes inside the glassmorphic topology panel (x 512..934, y 22..210)
    hubs = [
        ("MCP", 574, 86, p["accent"]),
        ("RAG", 734, 62, p["cyan"]),
        ("EVAL", 872, 122, p["emerald"]),
        ("vLLM", 686, 168, p["cyan"]),
    ]
    satellites = make_satellites(hubs)

    sat_edges = []
    for sx, sy in satellites:
        nh = min(hubs, key=lambda h: math.dist((sx, sy), (h[1], h[2])))
        if math.dist((sx, sy), (nh[1], nh[2])) < 110:
            sat_edges.append(f'      <line x1="{f(sx)}" y1="{f(sy)}" x2="{nh[1]}" y2="{nh[2]}"/>')
    sat_dots = "\n".join(f'      <circle cx="{f(x)}" cy="{f(y)}" r="1.9"/>' for x, y in satellites)

    routes = [
        ("M 574,86 C 636,52 686,52 734,62", p["accent"], 3.4, 0.0),
        ("M 734,62 C 804,70 842,88 872,122", p["cyan"], 3.6, 0.8),
        ("M 574,86 C 594,136 628,158 686,168", p["cyan"], 3.8, 1.3),
        ("M 686,168 C 762,174 824,154 872,122", p["emerald"], 3.5, 2.0),
        ("M 734,62 C 724,112 708,138 686,168", p["accent"], 4.2, 0.4),
        ("M 574,86 C 686,102 782,110 872,122", p["highlight"], 4.8, 2.6),
    ]

    route_svg = []
    for d, color, dur, begin in routes:
        route_svg.append(
            f'      <path d="{d}" fill="none" stroke="{p["edge"]}" stroke-width="1.1" opacity="0.62"/>'
        )
        route_svg.append(
            f'      <path d="{d}" fill="none" stroke="{color}" stroke-width="1.3" stroke-linecap="round" '
            f'stroke-dasharray="16 140" opacity="0.58">'
            f'<animate attributeName="stroke-dashoffset" from="156" to="0" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>'
            f'</path>'
        )
        route_svg.append(
            f'      <g opacity="0.95">'
            f'<circle r="6" fill="{color}" opacity="0.22"/>'
            f'<circle r="2.4" fill="{color}"/>'
            f'<circle r="1" fill="#FFFFFF" opacity="0.9"/>'
            f'<animateMotion dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite" path="{d}"/>'
            f'</g>'
        )

    hub_svg = []
    for idx, (label, hx, hy, color) in enumerate(hubs):
        b = idx * 1.15
        hub_svg.append(
            f'      <g>\n'
            f'        <circle cx="{hx}" cy="{hy}" r="16" fill="none" stroke="{color}" stroke-width="1.2" opacity="0">\n'
            f'          <animate attributeName="r" values="16;28;28" keyTimes="0;0.45;1" dur="4.6s" begin="{b:.2f}s" repeatCount="indefinite"/>\n'
            f'          <animate attributeName="opacity" values="0.55;0;0" keyTimes="0;0.45;1" dur="4.6s" begin="{b:.2f}s" repeatCount="indefinite"/>\n'
            f'        </circle>\n'
            f'        <circle cx="{hx}" cy="{hy}" r="20" fill="{color}" opacity="0.10"/>\n'
            f'        <circle cx="{hx}" cy="{hy}" r="16" fill="{p["node_bg"]}" stroke="{color}" stroke-width="1.35"/>\n'
            f'        <text x="{hx}" y="{hy + 3.6}" text-anchor="middle" font-family="{MONO}" font-size="9.8" font-weight="600" letter-spacing="0.4" fill="{p["name"]}">{label}</text>\n'
            f'      </g>'
        )

    # Live-cycling 12s SMIL telemetry signals (each visible for 4s with smooth cross-fade)
    telemetry = [
        ("eval-gate", "1.00 faithfulness · 10/10 PASS", p["emerald"], "1;1;0;0;0;0;1", "0;0.29;0.34;0.63;0.68;0.95;1"),
        ("mcp-sql", "89/89 attacks blocked · 0 leaks", p["accent"], "0;0;1;1;0;0;0", "0;0.31;0.36;0.62;0.67;0.95;1"),
        ("fsdp2-a100", "52% MFU · −38% ONNX latency", p["cyan"], "0;0;0;0;1;1;0", "0;0.33;0.64;0.69;0.71;0.95;1"),
    ]
    tele_svg = []
    for tag, msg, color, vals, kt in telemetry:
        tele_svg.append(
            f'      <g opacity="0">\n'
            f'        <animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="12s" repeatCount="indefinite"/>\n'
            f'        <circle cx="534" cy="242" r="2.8" fill="{color}"/>\n'
            f'        <text x="544" y="245.5" font-family="{MONO}" font-size="10" font-weight="600" fill="{color}">{esc(tag)}</text>\n'
            f'        <text x="614" y="245.5" font-family="{MONO}" font-size="10" fill="{p["name"]}">·  {esc(msg)}</text>\n'
            f'      </g>'
        )

    spark_path = "M 852,248 L 860,244 L 868,246 L 876,238 L 884,242 L 892,235 L 900,239 L 910,233"
    a0, a1 = p["aurora_op"]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Kishor Hange — Forward Deployed, ML and AI Engineer at E2open, Bengaluru (~4 YOE). Live AI Systems Topology and Production Telemetry.</title>
  <style>
    @media (max-width: 520px) {{ .topics {{ display: none; }} .satellites {{ opacity: 0.35; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="heroClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
    <clipPath id="panelClip">
      <rect x="506" y="20" width="430" height="256" rx="14"/>
    </clipPath>
    <clipPath id="barClip">
      <rect x="44" y="198" width="144" height="2.5" rx="1.25"/>
    </clipPath>
    <pattern id="dotGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="{p["grid"]}" opacity="{p["grid_op"]}"/>
    </pattern>
    <radialGradient id="auroraCyan">
      <stop offset="0" stop-color="{p["aurora_a"]}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{p["aurora_a"]}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{p["aurora_a"]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraWarm">
      <stop offset="0" stop-color="{p["aurora_b"]}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{p["aurora_c"]}" stop-opacity="0.24"/>
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

  <!-- outer obsidian/alabaster card -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#heroClip)">
    <!-- left editorial identity -->
    <g>
      <circle cx="49" cy="50" r="3.2" fill="{p["emerald"]}"/>
      <circle cx="49" cy="50" r="3.2" fill="none" stroke="{p["emerald"]}" stroke-width="1.2" opacity="0.8">
        <animate attributeName="r" values="3.2;9.5;9.5" keyTimes="0;0.55;1" dur="2.8s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.75;0;0" keyTimes="0;0.55;1" dur="2.8s" repeatCount="indefinite"/>
      </circle>
      <text x="62" y="53.8" font-family="{MONO}" font-size="11" letter-spacing="1.1" fill="{p["muted"]}" font-weight="500">Production AI &amp; ML Systems</text>
    </g>

    <text x="44" y="118" font-family="{SANS}" font-size="62" font-weight="600" letter-spacing="-1.6" fill="{p["name"]}">Kishor Hange{intro(0.1, 0.8, 7)}</text>
    <text x="44" y="153" font-family="{SANS}" font-size="20" font-weight="500" fill="{p["muted"]}">Forward Deployed · ML &amp; AI Engineer{intro(0.22, 0.8, 5)}</text>
    <text x="44" y="180" font-family="{SANS}" font-size="15" fill="{p["dim"]}">E2open · Bengaluru · ~4 YOE{intro(0.32, 0.7, 3)}</text>

    <!-- smooth animated gradient accent underline sweep -->
    <rect x="44" y="198" width="144" height="2.5" rx="1.25" fill="url(#accentBase)"/>
    <g clip-path="url(#barClip)">
      <rect x="-12" y="198" width="56" height="2.5" fill="url(#sweepGlow)">
        <animate attributeName="x" values="-12;196;196" keyTimes="0;0.45;1" dur="5.2s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};0 0 1 1"/>
      </rect>
    </g>

    <text class="topics" x="44" y="246" font-family="{MONO}" font-size="10.5" letter-spacing="0.3" fill="{p["muted"]}">Enterprise Agents (MCP) · Hybrid RAG</text>
    <text class="topics" x="44" y="264" font-family="{MONO}" font-size="10.5" letter-spacing="0.3" fill="{p["dim"]}">LLM Evals · Inference &amp; Distributed Training</text>

    <!-- right glassmorphic AI Systems Topology + Live Telemetry panel -->
    <rect x="506" y="20" width="430" height="256" rx="14" fill="{p["glass_bg"]}" fill-opacity="{p["glass_op"]}"/>
    <g clip-path="url(#panelClip)">
      <rect x="506" y="20" width="430" height="200" fill="url(#dotGrid)"/>

      <!-- breathing radial depth glows inside panel -->
      <ellipse cx="776" cy="82" rx="175" ry="104" fill="url(#auroraCyan)" opacity="{a0}">
        <animate attributeName="opacity" values="{a0};{a1};{a0}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
        <animateTransform attributeName="transform" type="translate" values="-10 0;10 0;-10 0" dur="22s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
      </ellipse>
      <ellipse cx="670" cy="162" rx="165" ry="92" fill="url(#auroraWarm)" opacity="{a0}">
        <animate attributeName="opacity" values="{a1};{a0};{a1}" dur="16s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
      </ellipse>

      <!-- faint satellite field -->
      <g class="satellites">
        <g stroke="{p["edge"]}" stroke-width="0.85" opacity="0.42">
{chr(10).join(sat_edges)}
        </g>
        <g fill="{p["muted"]}" opacity="0.36">
{sat_dots}
        </g>
      </g>

      <!-- fluid Bezier routes & data packets -->
      <g>
{chr(10).join(route_svg)}
      </g>

      <!-- 4 architectural hub nodes -->
      <g>
{chr(10).join(hub_svg)}
      </g>

      <!-- panel top-left micro label -->
      <text x="522" y="38" font-family="{MONO}" font-size="9.2" letter-spacing="1.2" fill="{p["dim"]}">AI SYSTEMS TOPOLOGY</text>
      <text x="920" y="38" text-anchor="end" font-family="{MONO}" font-size="9.2" fill="{p["emerald"]}" opacity="0.9">● LIVE</text>

      <!-- docked live-cycling telemetry bar -->
      <rect x="518" y="220" width="406" height="44" rx="10" fill="{p["card_bg"]}" fill-opacity="0.88" stroke="{p["border_subtle"]}" stroke-width="1"/>
      <!-- static first frame fallback + 3 smooth cycling signals -->
{chr(10).join(tele_svg)}

      <!-- subtle animated sparkline -->
      <path d="{spark_path}" fill="none" stroke="{p["cyan"]}" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round" opacity="0.82" stroke-dasharray="90" stroke-dashoffset="0">
        <animate attributeName="stroke-dashoffset" values="90;0;0" keyTimes="0;0.35;1" dur="4s" repeatCount="indefinite"/>
      </path>
      <circle cx="910" cy="233" r="2.2" fill="{p["emerald"]}">
        <animate attributeName="opacity" values="0.35;1;0.35" dur="2s" repeatCount="indefinite"/>
      </circle>
    </g>
    <rect x="506" y="20" width="430" height="256" rx="14" fill="none" stroke="{p["border"]}" stroke-width="1"/>
  </g>

  <!-- crisp outer hairline border -->
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------ 2. BORDERLESS 2x3 BENTO CARDS
CARDS_SPEC = [
    dict(
        idx=1,
        kicker="FDE · MCP PLATFORM",
        title="enterprise-mcp-agent-platform",
        line1="Multi-tenant RBAC/RLS, PII & injection guardrails,",
        line2="SQL/REST/doc connectors, DAG runtime, HITL & K8s.",
        tags=["MCP", "FastAPI", "OTel", "Helm / K8s"],
        metric="RBAC/RLS · HITL · Red-Team Suite",
        color_key="accent",
        icon="grid",
    ),
    dict(
        idx=2,
        kicker="PRODUCTION HYBRID RAG",
        title="production-rag-service",
        line1="Multi-format CDC ingestion, BM25 + dense RRF,",
        line2="calibrated reranker, fail-closed ACLs & SSE API.",
        tags=["FastAPI", "BM25 + FAISS", "Reranker", "CI Gate"],
        metric="1.00 Faithfulness · 10/10 Eval Gate",
        color_key="cyan",
        icon="search",
    ),
    dict(
        idx=3,
        kicker="LLM EVALUATION",
        title="llm-evaluation-harness",
        line1="Reproducible MMLU/ARC/GSM8K/HumanEval suite,",
        line2="calibrated LLM judge, BCa bootstrap CIs & tests.",
        tags=["PyTorch", "Bootstrap CIs", "Sandboxed Exec"],
        metric="Matches lm-eval within 0.5 pts",
        color_key="emerald",
        icon="chart",
    ),
    dict(
        idx=4,
        kicker="INFERENCE OPTIMIZATION",
        title="llm-inference-optimization",
        line1="INT8/NF4/AWQ quantization, PagedAttention KV,",
        line2="continuous batching, prefix cache & speculative.",
        tags=["vLLM", "PyTorch", "Quantization", "FastAPI"],
        metric="TTFT/TPOT · OpenAI Router · K8s HPA",
        color_key="accent",
        icon="bolt",
    ),
    dict(
        idx=5,
        kicker="DISTRIBUTED TRAINING",
        title="distributed-llm-training",
        line1="Plain-PyTorch GPT-2 pre-training & alignment:",
        line2="DDP, FSDP2, ZeRO-2/3, LoRA/SFT/DPO/GRPO.",
        tags=["PyTorch", "DDP", "FSDP2", "PyTorchJob"],
        metric="52% MFU Pre-Training on A100",
        color_key="cyan",
        icon="layers",
    ),
    dict(
        idx=6,
        kicker="MCP · SQL SECURITY",
        title="mcp-sql-agent",
        line1="LangGraph text-to-SQL behind MCP with layered",
        line2="sqlglot AST validation, RLS, masking & audit logs.",
        tags=["MCP", "LangGraph", "sqlglot", "RLS"],
        metric="89/89 Attacks Blocked · 0 Leaks",
        color_key="emerald",
        icon="shield",
    ),
]


def micro_icon(kind, x, y, color):
    """Minimalist 18x18 geometric micro-icon anchored at (x, y)."""
    if kind == "grid":
        return (
            f'    <g stroke="{color}" stroke-width="1.35" fill="none" opacity="0.88">\n'
            f'      <rect x="{x}" y="{y}" width="6" height="6" rx="1.5"/>\n'
            f'      <rect x="{x + 9}" y="{y}" width="6" height="6" rx="1.5"/>\n'
            f'      <rect x="{x}" y="{y + 9}" width="6" height="6" rx="1.5"/>\n'
            f'      <rect x="{x + 9}" y="{y + 9}" width="6" height="6" rx="1.5"/>\n'
            f'    </g>'
        )
    if kind == "search":
        return (
            f'    <g stroke="{color}" stroke-width="1.4" fill="none" stroke-linecap="round" opacity="0.88">\n'
            f'      <circle cx="{x + 6.5}" cy="{y + 6.5}" r="5.5"/>\n'
            f'      <line x1="{x + 10.8}" y1="{y + 10.8}" x2="{x + 15}" y2="{y + 15}"/>\n'
            f'    </g>'
        )
    if kind == "chart":
        return (
            f'    <g stroke="{color}" stroke-width="1.5" stroke-linecap="round" opacity="0.88">\n'
            f'      <line x1="{x + 2}" y1="{y + 14}" x2="{x + 2}" y2="{y + 8}"/>\n'
            f'      <line x1="{x + 7.5}" y1="{y + 14}" x2="{x + 7.5}" y2="{y + 3}"/>\n'
            f'      <line x1="{x + 13}" y1="{y + 14}" x2="{x + 13}" y2="{y + 6}"/>\n'
            f'    </g>'
        )
    if kind == "bolt":
        return (
            f'    <path d="M {x + 9},{y + 1} L {x + 3},{y + 9} L {x + 8},{y + 9} L {x + 6.5},{y + 15} L {x + 13},{y + 7} L {x + 8},{y + 7} Z" '
            f'fill="none" stroke="{color}" stroke-width="1.3" stroke-linejoin="round" opacity="0.88"/>'
        )
    if kind == "layers":
        return (
            f'    <g stroke="{color}" stroke-width="1.35" fill="none" stroke-linejoin="round" opacity="0.88">\n'
            f'      <polygon points="{x + 7.5},{y + 1} {x + 15},{y + 5} {x + 7.5},{y + 9} {x},{y + 5}"/>\n'
            f'      <polyline points="{x},{y + 9.5} {x + 7.5},{y + 13.5} {x + 15},{y + 9.5}"/>\n'
            f'    </g>'
        )
    return (
        f'    <path d="M {x + 7.5},{y + 1} L {x + 14},{y + 3.5} L {x + 14},{y + 8.5} C {x + 14},{y + 12} {x + 11},{y + 14.5} {x + 7.5},{y + 15.5} '
        f'C {x + 4},{y + 14.5} {x + 1},{y + 12} {x + 1},{y + 8.5} L {x + 1},{y + 3.5} Z" '
        f'fill="none" stroke="{color}" stroke-width="1.35" stroke-linejoin="round" opacity="0.88"/>'
    )


def flagship_card(spec, p):
    W, H = 410, 176
    color = p[spec["color_key"]]
    idx = spec["idx"]
    b = (idx - 1) * 0.9

    # Render clean rounded tech pills
    px = 20
    pills = []
    for tag in spec["tags"]:
        tw = max(36, int(len(tag) * 6.2 + 16))
        pills.append(
            f'    <rect x="{px}" y="106" width="{tw}" height="20" rx="6" fill="{p["pill_bg"]}" stroke="{p["border_subtle"]}" stroke-width="0.9"/>\n'
            f'    <text x="{px + tw / 2:.1f}" y="119.2" text-anchor="middle" font-family="{MONO}" font-size="9.3" fill="{p["muted"]}">{esc(tag)}</text>'
        )
        px += tw + 7

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">{esc(spec["title"])} — {esc(spec["kicker"])}: {esc(spec["metric"])}</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="cClip{idx}">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14"/>
    </clipPath>
    <radialGradient id="cGlow{idx}">
      <stop offset="0" stop-color="{color}" stop-opacity="0.24"/>
      <stop offset="1" stop-color="{color}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#cClip{idx})">
    <!-- top accent stripe -->
    <rect x="0" y="0" width="{W}" height="3" fill="{color}" opacity="0.88"/>
    <!-- subtle breathing corner glow -->
    <circle cx="{W - 24}" cy="24" r="76" fill="url(#cGlow{idx})" opacity="0.38">
      <animate attributeName="opacity" values="0.22;0.58;0.22" dur="7.5s" begin="{b:.1f}s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>
    </circle>

    <!-- kicker + micro icon -->
    <circle cx="24" cy="24" r="2.6" fill="{color}">
      <animate attributeName="opacity" values="0.45;1;0.45" dur="3.6s" begin="{b:.1f}s" repeatCount="indefinite"/>
    </circle>
    <text x="34" y="27.5" font-family="{MONO}" font-size="9.5" font-weight="600" letter-spacing="1.2" fill="{color}">{esc(spec["kicker"])}</text>
{micro_icon(spec["icon"], W - 36, 16, color)}

    <!-- repo title & 2-line architecture summary -->
    <text x="20" y="53" font-family="{SANS}" font-size="16" font-weight="600" letter-spacing="-0.3" fill="{p["name"]}">{esc(spec["title"])}</text>
    <text x="20" y="75" font-family="{SANS}" font-size="11.6" fill="{p["muted"]}">{esc(spec["line1"])}</text>
    <text x="20" y="92" font-family="{SANS}" font-size="11.6" fill="{p["muted"]}">{esc(spec["line2"])}</text>

    <!-- tech pills -->
{chr(10).join(pills)}

    <!-- highlighted bottom metric pill -->
    <rect x="20" y="138" width="{W - 40}" height="24" rx="7" fill="{color}" fill-opacity="0.11" stroke="{color}" stroke-opacity="0.32" stroke-width="0.9"/>
    <text x="32" y="153.5" font-family="{MONO}" font-size="10.2" font-weight="600" fill="{p["name"]}">{esc(spec["metric"])}</text>
    <text x="{W - 30}" y="153.5" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{color}">↗</text>
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ----------------------------------------------- 3. 4-LAYER STACK BLUEPRINT SVG
def stack_blueprint(p):
    W, H = 960, 274
    layers = [
        ("01", "AGENTS, RAG & EVALS", "MCP · LangGraph · LangChain · CrewAI · FAISS · Chroma · OpenSearch · Ragas · DeepEval · sqlglot · xgrammar", p["accent"]),
        ("02", "MODELS, TRAINING & INFERENCE", "PyTorch (DDP, FSDP2) · Transformers · PEFT (LoRA/QLoRA) · TRL (SFT/DPO/GRPO) · vLLM · ONNX Runtime · Optimum · TVM", p["cyan"]),
        ("03", "SERVING, INFRA & OBSERVABILITY", "FastAPI · Docker · Kubernetes · Helm · Terraform · GitHub Actions · MLflow · Airflow · OpenTelemetry · Prometheus · Grafana", p["emerald"]),
        ("04", "LANGUAGES, DATA & CLOUD", "Python · TypeScript · SQL · Java · C++ · Go · Spark · Kafka · Snowflake · AWS (Bedrock, ECS, SageMaker, S3) · GCP (Vertex AI)", p["cyan"]),
    ]

    row_h, gap, start_y = 46, 10, 46
    bus_x = 34
    bus_top = start_y + row_h // 2
    bus_bot = start_y + 3 * (row_h + gap) + row_h // 2
    bus_path = f"M {bus_x},{bus_top} L {bus_x},{bus_bot}"

    rows_svg = []
    cycle = 5.6
    for i, (num, label, techs, color) in enumerate(layers):
        y = start_y + i * (row_h + gap)
        cy = y + row_h // 2
        t_hit = i * 1.15
        k1 = f"{t_hit / cycle:.3f}"
        k2 = f"{(t_hit + 0.35) / cycle:.3f}"
        k3 = f"{(t_hit + 1.0) / cycle:.3f}"
        rows_svg.append(
            f'    <g>\n'
            f'      <line x1="{bus_x}" y1="{cy}" x2="54" y2="{cy}" stroke="{p["border"]}" stroke-width="1.2"/>\n'
            f'      <circle cx="{bus_x}" cy="{cy}" r="4.2" fill="{p["card_bg"]}" stroke="{color}" stroke-width="1.5"/>\n'
            f'      <rect x="54" y="{y}" width="882" height="{row_h}" rx="10" fill="{p["card_surface"]}" stroke="{p["border"]}" stroke-width="1"/>\n'
            f'      <rect x="54" y="{y}" width="882" height="{row_h}" rx="10" fill="none" stroke="{color}" stroke-width="1.35" opacity="0.14">\n'
            f'        <animate attributeName="opacity" values="0.14;0.14;0.82;0.14;0.14" keyTimes="0;{k1};{k2};{k3};1" dur="{cycle:.1f}s" repeatCount="indefinite"/>\n'
            f'      </rect>\n'
            f'      <rect x="54" y="{y}" width="3.5" height="{row_h}" rx="1.75" fill="{color}" opacity="0.88"/>\n'
            f'      <text x="72" y="{y + 18}" font-family="{MONO}" font-size="9.5" font-weight="600" letter-spacing="1.2" fill="{color}">{num} · {esc(label)}</text>\n'
            f'      <text x="72" y="{y + 35}" font-family="{SANS}" font-size="11.5" fill="{p["name"]}" opacity="0.92">{esc(techs)}</text>\n'
            f'    </g>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Core Engineering Stack — 4-Layer Architecture Blueprint covering Agents/RAG/Evals, Models/Training/Inference, Serving/Infra/Observability, and Languages/Data/Cloud.</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="stackClip">
      <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/>
    </clipPath>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["card_bg"]}" fill-opacity="{p["card_op"]}"/>

  <g clip-path="url(#stackClip)">
    <text x="24" y="29" font-family="{MONO}" font-size="10.2" font-weight="600" letter-spacing="1.4" fill="{p["muted"]}">CORE ENGINEERING STACK · 4-LAYER BLUEPRINT</text>
    <text x="936" y="29" text-anchor="end" font-family="{MONO}" font-size="10" fill="{p["dim"]}">application → models → runtime → infrastructure</text>

    <!-- vertical architectural bus spine -->
    <line x1="{bus_x}" y1="{bus_top}" x2="{bus_x}" y2="{bus_bot}" stroke="{p["border"]}" stroke-width="1.4"/>

    <!-- 4 architectural stack layers -->
{chr(10).join(rows_svg)}

    <!-- vertical signal pulse gliding through all 4 layers -->
    <g opacity="0.95">
      <circle r="6" fill="{p["cyan"]}" opacity="0.25"/>
      <circle r="2.6" fill="{p["cyan"]}"/>
      <animateMotion dur="{cycle:.1f}s" repeatCount="indefinite" path="{bus_path}"/>
    </g>
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------ 4. ARCHITECTURE
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
    start_x = 24
    cy = 96
    top_y = cy - ch // 2
    cycle = 6.0

    nodes_svg = []
    arrows_svg = []

    for i, (num, l1, l2, sub, color) in enumerate(stages):
        x = start_x + i * (cw + gap)
        cx = x + cw / 2
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

{chr(10).join(arrows_svg)}
{chr(10).join(nodes_svg)}
  </g>

  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" stroke="{p["border"]}" stroke-width="1"/>
</svg>
"""


# ------------------------------------------------------------------ 5. KPI
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
            f'      <circle cx="{x + cw - 20}" cy="18" r="64" fill="url(#kpiGlow{i})" opacity="0.35">\n'
            f'        <animate attributeName="opacity" values="0.22;0.65;0.22" dur="7s" begin="{b:.1f}s" repeatCount="indefinite" calcMode="spline" keySplines="{EASE_SINE};{EASE_SINE}"/>\n'
            f'      </circle>\n'
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


# --------------------------------------------------------------- 6. FOOTER
def footer(p):
    W, H = 960, 74
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
    <path d="{wave}" fill="none" stroke="{p["border_subtle"]}" stroke-width="1.2"/>
    <path d="{wave}" fill="none" stroke="url(#waveGrad)" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="120 820">
      <animate attributeName="stroke-dashoffset" from="940" to="0" dur="8s" repeatCount="indefinite"/>
    </path>
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
        for name, build in (
            ("header", header),
            ("architecture", architecture),
            ("kpi", kpi),
            ("stack", stack_blueprint),
            ("footer", footer),
        ):
            out = ASSETS / f"{name}-{mode}.svg"
            out.write_text(build(pal), encoding="utf-8", newline="\n")
            print(f"{out.name}: {out.stat().st_size / 1024:.1f} KB")
        for spec in CARDS_SPEC:
            out = ASSETS / f"card-{spec['idx']}-{mode}.svg"
            out.write_text(flagship_card(spec, pal), encoding="utf-8", newline="\n")
            print(f"{out.name}: {out.stat().st_size / 1024:.1f} KB")
