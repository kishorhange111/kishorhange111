<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg?v=6">
  <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg?v=6">
  <img alt="Kishor Hange — Forward Deployed, ML & AI Engineer at E2open, Bengaluru (~4 YOE). Enterprise MCP agents, production RAG, LLM evals, inference optimization, and distributed training." src="./assets/header-light.svg?v=6" width="100%">
</picture>

<p align="center">
  <a href="https://kishorhange.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-1F2328?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/kishorhange/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="./PORTFOLIO_MAP.md"><img src="https://img.shields.io/badge/Portfolio_Map-2B7A87?style=flat-square&logo=readthedocs&logoColor=white" alt="Portfolio Map" /></a>
  <a href="https://github.com/python/cpython/pull/148978"><img src="https://img.shields.io/badge/CPython_PR-3776AB?style=flat-square&logo=python&logoColor=white" alt="CPython PR" /></a>
  <a href="mailto:kishorhange46@gmail.com"><img src="https://img.shields.io/badge/Email-D97757?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

**Forward Deployed, ML & AI Engineer** at **E2open** (Bengaluru, **~4 YOE**) taking LLM and ML systems from prototype to production — specializing in secure MCP agent platforms, hybrid RAG with automated eval gates, low-latency inference, distributed training, and observable MLOps. Outside production systems, I run controlled multi-seed deep learning experiments (RLVR/GRPO, mechanistic interpretability, grokking, scaling laws) and report null results as carefully as wins.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/kpi-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./assets/kpi-light.svg?v=1">
  <img alt="Impact Highlights: -38% Inference Latency at E2open, +9.5% Classifier Accuracy at E2open, 588+ Tests and 100+ PRs across 9 production repos plus a merged CPython PR." src="./assets/kpi-light.svg?v=1" width="100%">
</picture>

---

## Flagship Systems

> Hiring manager or recruiter? Open the [**Portfolio Competency Map**](./PORTFOLIO_MAP.md) for a 60-second role-based guide across **FDE**, **AI Engineer**, **ML Systems**, **Research**, and **MLOps**.

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/FDE_%C2%B7_MCP_PLATFORM-D97757?style=flat-square" alt="FDE MCP Platform" /><br/>
      <a href="https://github.com/kishorhange111/enterprise-mcp-agent-platform"><strong>enterprise-mcp-agent-platform</strong></a><br/>
      <sub>Multi-tenant MCP platform with RBAC, PII/injection guardrails, SQL/REST/doc connectors, HITL approvals &amp; Helm/K8s.</sub><br/><br/>
      <code>MCP</code> <code>FastAPI</code> <code>OTel</code> <code>Helm</code><br/>
      <strong>113 tests · 20 PRs · Red-team suite</strong>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/PRODUCTION_HYBRID_RAG-2B7A87?style=flat-square" alt="Production Hybrid RAG" /><br/>
      <a href="https://github.com/kishorhange111/production-rag-service"><strong>production-rag-service</strong></a><br/>
      <sub>FastAPI hybrid RAG with CDC ingestion, BM25 + dense RRF, calibrated reranking, fail-closed ACLs &amp; citation checks.</sub><br/><br/>
      <code>FastAPI</code> <code>FAISS</code> <code>Reranker</code> <code>K8s</code><br/>
      <strong>80 tests · 10/10 eval gate (1.00 faithful)</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/LLM_EVALUATION-57606A?style=flat-square" alt="LLM Evaluation" /><br/>
      <a href="https://github.com/kishorhange111/llm-evaluation-harness"><strong>llm-evaluation-harness</strong></a><br/>
      <sub>Reproducible eval suite (MMLU, ARC, HellaSwag, GSM8K, HumanEval) with bias-controlled LLM judge &amp; bootstrap CIs.</sub><br/><br/>
      <code>PyTorch</code> <code>Stats</code> <code>Sandboxed Exec</code> <code>CI</code><br/>
      <strong>93 tests · Within 0.5 pts of lm-eval</strong>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/INFERENCE_OPTIMIZATION-B4532F?style=flat-square" alt="Inference Optimization" /><br/>
      <a href="https://github.com/kishorhange111/llm-inference-optimization"><strong>llm-inference-optimization</strong></a><br/>
      <sub>Serving &amp; GPU optimization: int8/NF4/AWQ quantization, KV paging, continuous batching, speculative decoding &amp; vLLM.</sub><br/><br/>
      <code>vLLM</code> <code>PyTorch</code> <code>Quantization</code> <code>FastAPI</code><br/>
      <strong>55 tests · TTFT/TPOT latency sweeps</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/DISTRIBUTED_TRAINING-2B7A87?style=flat-square" alt="Distributed Training" /><br/>
      <a href="https://github.com/kishorhange111/distributed-llm-training"><strong>distributed-llm-training</strong></a><br/>
      <sub>Plain-PyTorch GPT-2 training &amp; alignment: DDP, FSDP2, ZeRO-2/3 configs, bf16, LoRA/SFT/DPO/GRPO &amp; atomic checkpoints.</sub><br/><br/>
      <code>PyTorch</code> <code>DDP</code> <code>FSDP2</code> <code>MLflow</code><br/>
      <strong>57 tests · 52% MFU on A100</strong>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/MCP_%C2%B7_SQL_SECURITY-D97757?style=flat-square" alt="MCP SQL Security" /><br/>
      <a href="https://github.com/kishorhange111/mcp-sql-agent"><strong>mcp-sql-agent</strong></a><br/>
      <sub>LangGraph text-to-SQL agent behind an MCP server with sqlglot AST guards, SQLite authorizer, RLS &amp; audit logs.</sub><br/><br/>
      <code>MCP</code> <code>LangGraph</code> <code>sqlglot</code> <code>RLS</code><br/>
      <strong>89 tests · 89/89 attacks blocked</strong>
    </td>
  </tr>
</table>

---

## Production Impact @ E2open

> **Software Engineer** (Sep 2025 – Present) · **Associate SE** (Jul 2023 – Sep 2025)

- **38% lower inference latency** via quantization and pruning (ONNX Runtime, Hugging Face Optimum), saving a full delivery sprint.
- **+9.5% classification accuracy** replacing a legacy business-document classifier with Random Forest on custom Word2Vec embeddings and fine-tuned BERT.
- **Enterprise MCP & Agentic Workflows:** Built agentic LLM workflows (LangChain, CrewAI, n8n) and **Model Context Protocol (MCP)** integrations for secure LLM access to enterprise databases.
- **Production RAG, Fine-Tuning & Monitoring:** Shipped an automated customer-support LLM chatbot, RAG pipelines evaluated with **Ragas** & **DeepEval**, PEFT (LoRA/QLoRA) domain fine-tuning, Vertex AI semantic matching, and FastAPI / Airflow / Prometheus / Grafana monitoring alongside Spark, Kafka & Snowflake pipelines.

---

## Explore More by Engineering Pillar

<details>
<summary><strong>Agent Runtimes, Gateways &amp; Cloud RAG (5 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**llm-reliability-gateway**](https://github.com/kishorhange111/llm-reliability-gateway) | Multi-provider LLM gateway (fallback, failure-rate circuit breakers, jitter retries, per-tenant budgets, semantic cache, Docker/K8s/Terraform AWS ECS Fargate) — holds **100% availability** through hanging outages, **−64%** wasted calls, **0.5×** p95 |
| [**agent-runtime-ts**](https://github.com/kishorhange111/agent-runtime-ts) | **TypeScript** Claude agent runtime with zod-typed tools, MCP client adapter, write-approval hooks, loop guards, budgets & OTel traces — unsafe refunds **16.3% → 0%**, cost/episode **−83%** |
| [**agent-memory-bench**](https://github.com/kishorhange111/agent-memory-bench) | Multi-session agent memory benchmark (recency vs BM25 vs embeddings vs fact store with supersession vs hybrid) — fact store hits **100% at 17 tokens**; hybrid recovers **+14 pts** from extraction misses |
| [**agent-reliability-bench**](https://github.com/kishorhange111/agent-reliability-bench) | τ-bench-style stateful tool-use benchmark with policy monitor, final-state grading & fault injection — exposes pass^1 **0.77 → pass^8 0.32** under 10% tool faults |
| [**bedrock-serverless-rag**](https://github.com/kishorhange111/bedrock-serverless-rag) | Multi-tenant AWS serverless RAG design (Terraform: S3→SQS→Lambda, OpenSearch k-NN tenant pre-filter, Bedrock Claude, Cognito JWT, Step Functions) — **99.3%** accuracy, **100%** abstention, **0** cross-tenant leaks |

</details>

<details>
<summary><strong>Retrieval, GraphRAG &amp; Structured Extraction (3 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**embedding-finetuning-retrieval**](https://github.com/kishorhange111/embedding-finetuning-retrieval) | Domain embedding fine-tuning on BEIR FiQA: hard-negative mining, Matryoshka representation learning, int8 & binary vector compression + FastAPI serving (**33 tests**) |
| [**graphrag-entity-linking**](https://github.com/kishorhange111/graphrag-entity-linking) | Multi-hop QA benchmark (single-shot vs iterative RAG vs entity-linked knowledge graph) — entity-ID graph hops hit **100%** vs **88%** name-based iterative RAG and **~1%** single-shot |
| [**llm-structured-extraction**](https://github.com/kishorhange111/llm-structured-extraction) | Receipt field extraction on CORD with a small local LLM: RapidOCR, free vs schema-constrained decoding (`xgrammar`), arithmetic/grounding checks, repair loop & FastAPI service (**45 tests**) |

</details>

<details>
<summary><strong>LLM Post-Training, Capacity Planning &amp; Deep Learning Research (8 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**llm-capacity-planner**](https://github.com/kishorhange111/llm-capacity-planner) | Roofline cost model (FLOPs, HBM, KV cache, TP all-reduce) + continuous-batching simulator + SLO planner — kv8 doubles decode throughput, GQA gives **4×** concurrency |
| [**mini-chatgpt**](https://github.com/kishorhange111/mini-chatgpt) | Base LLM (`Qwen2.5-0.5B`) → 160k SFT (127M tokens) → from-scratch DPO (12k pairs) — matches Qwen Instruct on IFEval (**36.7 vs 36.3**) and beats it on ARC-Easy (**+5 pts**) in ~3 GPU-hours |
| [**generative-ai-engineering**](https://github.com/kishorhange111/generative-ai-engineering) | 8 benchmarked LLM systems: QLoRA text-to-SQL (**60.0% → 66.2%**), 7B→0.5B distillation, function-calling (**16.7% → 94.8%**), GRPO, Qwen2-VL, Whisper Marathi (CER **53.6% → 14.7%**), guardrails |
| [**rl-from-scratch**](https://github.com/kishorhange111/rl-from-scratch) | Double/Dueling DQN, PPO (GAE, clipping, vectorized envs) & REINFORCE in PyTorch — 45-run 5-seed IQM benchmark (PPO **5/5** CartPole, Double DQN **5/5** Acrobot) |
| [**rlvr-grpo-from-scratch**](https://github.com/kishorhange111/rlvr-grpo-from-scratch) | GRPO / Dr. GRPO / RLOO / online DPO with matched-compute controls — RL **doubles pass@1 (18% → 34–38%)** while leaving pass@16 flat |
| [**arithmetic-transformer-interp**](https://github.com/kishorhange111/arithmetic-transformer-interp) | Activation patching & TopK SAEs (**99.97%** CE recovered) on addition transformers — shows **probe-decodable ≠ causally used** (88.5% probe acc vs 2% patching effect) |
| [**grokking-progress-measures**](https://github.com/kishorhange111/grokking-progress-measures) | Modular-addition grokking with Fourier-sparsity progress measures — sparsity rises **0.32 → 0.61** while test accuracy is still near chance |
| [**scaling-laws-from-scratch**](https://github.com/kishorhange111/scaling-laws-from-scratch) | Chinchilla-style IsoFLOP sweeps & parametric L(N, D) fits on byte-level GPTs — demonstrates batch-size step-starvation vs interior compute optimum |

</details>

<details>
<summary><strong>Applied ML, Causal Inference, MLOps &amp; Edge Systems (7 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**demand-forecasting-mlops**](https://github.com/kishorhange111/demand-forecasting-mlops) | M5 retail forecasting (30,490 series, **WRMSSE 0.5536**, 35% below seasonal naive) with conformal intervals, drift retraining, gated MLflow registry & FastAPI |
| [**two-tower-recommender**](https://github.com/kishorhange111/two-tower-recommender) | MovieLens 1M two-tower retrieval (logQ, item bias) + FAISS + LightGBM re-ranker & FastAPI benchmarked honestly against EASE & ItemKNN on a global temporal split |
| [**uplift-targeting**](https://github.com/kishorhange111/uplift-targeting) | Causal uplift modeling on Hillstrom (S, T, X, DR learners vs response modeling), Qini bootstrap CIs, budgeted targeting & off-policy evaluation (**23 tests**) |
| [**deep-learning-portfolio**](https://github.com/kishorhange111/deep-learning-portfolio) | 14 CV, NLP & generative projects: BERT distillation + ONNX + int8 (**4.8× faster, 85% smaller**), GPT-2 LoRA (−69% GPU mem), ViT, U-Net, Music Transformer |
| [**cnn-edge-optimization-tflite-onnx-tvm**](https://github.com/kishorhange111/cnn-edge-optimization-tflite-onnx-tvm) | Edge compilation of a Keras CNN through TFLite, ONNX & Apache TVM (**~12× smaller** models) |
| [**vm-energy-agent**](https://github.com/kishorhange111/vm-energy-agent) | Go monitoring agent estimating VM power consumption and exporting Prometheus / OpenTelemetry metrics |
| [**llm-token-visualizer**](https://github.com/kishorhange111/llm-token-visualizer) | Interactive Streamlit app comparing tokenization across BERT, GPT-2, GPT-4, Phi-3 & DeepSeek |

</details>

<details>
<summary><strong>Open Source Contributions (CPython, Sphinx)</strong></summary>

| Project | PR | Status & Summary |
|---|---|---|
| **python/cpython** | [**#148978**](https://github.com/python/cpython/pull/148978) | **Merged** — `gh-148849: Deprecate http.cookies.BaseCookie.js_output()` |
| **sphinx-doc/sphinx** | [**#14421**](https://github.com/sphinx-doc/sphinx/pull/14421) | **Open** — `Fix #2835: Trigger rebuild when theme files change` |

</details>

---

## Core Engineering Stack

| Layer | Technologies |
|---|---|
| **Agents, RAG & Evals** | MCP · LangGraph · LangChain · CrewAI · FAISS · Chroma · OpenSearch · Ragas · DeepEval · sqlglot · xgrammar |
| **Models, Training & Inference** | PyTorch (DDP, FSDP2) · Hugging Face Transformers · PEFT (LoRA, QLoRA) · TRL (SFT, DPO, GRPO) · vLLM · ONNX Runtime · Optimum · TFLite · Apache TVM · LightGBM · scikit-learn |
| **Serving, Infra & Observability** | FastAPI · Docker · Kubernetes · Helm · Terraform · GitHub Actions · MLflow · Airflow · OpenTelemetry · Prometheus · Grafana |
| **Languages, Data & Cloud** | Python · TypeScript · SQL · Java · C++ · Go · Spark · Kafka · Snowflake · AWS (Bedrock, ECS, SageMaker, S3) · GCP (Vertex AI) |

---

## GitHub Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake.svg" />
    <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake.svg" />
  </picture>
</p>

<p align="center"><sub>B.Tech CSE · DKTE Ichalkaranji (2019–2023) · CGPA 8.31</sub></p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg?v=4">
  <source media="(prefers-color-scheme: light)" srcset="./assets/footer-light.svg?v=4">
  <img alt="Thanks for visiting. Kishor Hange, Bengaluru, IN — FDE, ML & AI Systems" src="./assets/footer-light.svg?v=4" width="100%">
</picture>
