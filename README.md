<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg?v=7">
  <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg?v=7">
  <img alt="Kishor Hange — Forward Deployed, ML & AI Engineer at E2open, Bengaluru (~4 YOE). Enterprise Agents (MCP), Hybrid RAG, LLM Evals, Inference and Distributed Training." src="./assets/header-light.svg?v=7" width="100%">
</picture>

<p align="center">
  <a href="https://kishorhange.vercel.app/">Portfolio</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/kishorhange/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="./PORTFOLIO_MAP.md">Portfolio Map</a> &nbsp;·&nbsp;
  <a href="https://github.com/python/cpython/pull/148978">CPython PR #148978</a> &nbsp;·&nbsp;
  <a href="mailto:kishorhange46@gmail.com">Email</a>
</p>

**Forward Deployed, ML & AI Engineer** at **E2open** (Bengaluru, **~4 YOE**) taking LLM and ML systems from prototype to production — specializing in secure MCP agent platforms, hybrid RAG with automated eval gates, low-latency inference, distributed training, and observable MLOps. Outside production systems, I run controlled multi-seed deep learning experiments (RLVR/GRPO, mechanistic interpretability, grokking, scaling laws) and report null results as carefully as wins.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/kpi-dark.svg?v=2">
  <source media="(prefers-color-scheme: light)" srcset="./assets/kpi-light.svg?v=2">
  <img alt="Key Impact: -38% Inference Latency at E2open, +9.5% Classifier Accuracy at E2open, and CPython Open-Source Contributor (merged python/cpython#148978)." src="./assets/kpi-light.svg?v=2" width="100%">
</picture>

---

## Flagship Systems

> Hiring manager or recruiter? Open the [**Portfolio Competency Map**](./PORTFOLIO_MAP.md) for a 60-second role-based guide across **FDE**, **AI Engineer**, **ML Systems**, **Research**, and **MLOps**.

<table>
  <tr>
    <td width="50%" valign="top">
      <sub>FDE · MCP PLATFORM</sub><br/>
      <a href="https://github.com/kishorhange111/enterprise-mcp-agent-platform"><strong>enterprise-mcp-agent-platform</strong></a><br/>
      <sub>Multi-tenant MCP platform with RBAC/RLS policy enforcement, PII &amp; injection guardrails, SQL/REST/doc connectors, HITL approvals, and audit logging.</sub><br/><br/>
      <sub>MCP · FastAPI · OpenTelemetry · Helm / K8s</sub><br/>
      <strong>RBAC/RLS · HITL approvals · Red-team security suite</strong>
    </td>
    <td width="50%" valign="top">
      <sub>PRODUCTION HYBRID RAG</sub><br/>
      <a href="https://github.com/kishorhange111/production-rag-service"><strong>production-rag-service</strong></a><br/>
      <sub>FastAPI hybrid RAG with multi-format CDC ingestion, BM25 + dense RRF, calibrated reranking, fail-closed ACL filtering, and SSE streaming.</sub><br/><br/>
      <sub>FastAPI · BM25 + FAISS · Reranker · Prometheus</sub><br/>
      <strong>1.00 faithfulness &amp; recall@3 golden eval gate</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub>LLM EVALUATION</sub><br/>
      <a href="https://github.com/kishorhange111/llm-evaluation-harness"><strong>llm-evaluation-harness</strong></a><br/>
      <sub>Reproducible benchmark harness covering MMLU, ARC, HellaSwag, GSM8K, and sandboxed HumanEval with position-bias-controlled LLM judging.</sub><br/><br/>
      <sub>PyTorch · Bootstrap CIs · Paired Tests · Sandboxed Exec</sub><br/>
      <strong>Matches EleutherAI lm-eval within 0.5 pts</strong>
    </td>
    <td width="50%" valign="top">
      <sub>INFERENCE OPTIMIZATION</sub><br/>
      <a href="https://github.com/kishorhange111/llm-inference-optimization"><strong>llm-inference-optimization</strong></a><br/>
      <sub>Single-GPU &amp; serving stack: int8/NF4/AWQ quantization, KV-cache paging, continuous batching, radix prefix caching, and speculative decoding.</sub><br/><br/>
      <sub>vLLM · PyTorch · Quantization · FastAPI</sub><br/>
      <strong>vLLM TTFT/TPOT sweeps · OpenAI-compatible router</strong>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub>DISTRIBUTED TRAINING</sub><br/>
      <a href="https://github.com/kishorhange111/distributed-llm-training"><strong>distributed-llm-training</strong></a><br/>
      <sub>Plain-PyTorch GPT-2 pre-training and alignment stack supporting DDP, FSDP2, ZeRO-2/3 configs, bf16, LoRA/SFT/DPO/GRPO, and K8s PyTorchJob.</sub><br/><br/>
      <sub>PyTorch · DDP · FSDP2 · MLflow</sub><br/>
      <strong>52% MFU pre-training on A100 · Exact-resume shards</strong>
    </td>
    <td width="50%" valign="top">
      <sub>MCP · SQL SECURITY</sub><br/>
      <a href="https://github.com/kishorhange111/mcp-sql-agent"><strong>mcp-sql-agent</strong></a><br/>
      <sub>LangGraph text-to-SQL agent behind an MCP server with layered sqlglot AST policy guards, SQLite authorizer, multi-tenant RLS, and audit logs.</sub><br/><br/>
      <sub>MCP · LangGraph · sqlglot · Row-Level Security</sub><br/>
      <strong>89/89 SQL attacks blocked · 0 protected leaks</strong>
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
| [**embedding-finetuning-retrieval**](https://github.com/kishorhange111/embedding-finetuning-retrieval) | Domain embedding fine-tuning on BEIR FiQA: hard-negative mining, Matryoshka representation learning, int8 & binary vector compression + FastAPI serving |
| [**graphrag-entity-linking**](https://github.com/kishorhange111/graphrag-entity-linking) | Multi-hop QA benchmark (single-shot vs iterative RAG vs entity-linked knowledge graph) — entity-ID graph hops hit **100%** vs **88%** name-based iterative RAG and **~1%** single-shot |
| [**llm-structured-extraction**](https://github.com/kishorhange111/llm-structured-extraction) | Receipt field extraction on CORD with a small local LLM: RapidOCR, free vs schema-constrained decoding (xgrammar), arithmetic/grounding checks, repair loop & FastAPI service |

</details>

<details>
<summary><strong>LLM Post-Training, Capacity Planning &amp; Deep Learning Research (8 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**llm-capacity-planner**](https://github.com/kishorhange111/llm-capacity-planner) | Roofline cost model + continuous-batching simulator + SLO planner, **calibrated against real vLLM on a T4**: replaying the closed-loop schedule and separating attention efficiency cut model error **76% → 12%**, and showed T4 attention (TRITON_ATTN) runs at ~1% of peak vs 27% for GEMMs |
| [**mini-chatgpt**](https://github.com/kishorhange111/mini-chatgpt) | Base LLM (`Qwen2.5-0.5B`) → 160k SFT (127M tokens) → from-scratch DPO (12k pairs) — matches Qwen Instruct on IFEval (**36.7 vs 36.3**) and beats it on ARC-Easy (**+5 pts**) in ~3 GPU-hours |
| [**generative-ai-engineering**](https://github.com/kishorhange111/generative-ai-engineering) | 8 benchmarked LLM systems: QLoRA text-to-SQL (**60.0% → 66.2%**), 7B→0.5B distillation, function-calling (**16.7% → 94.8%**), GRPO, Qwen2-VL, Whisper Marathi (CER **53.6% → 14.7%**), guardrails |
| [**rl-from-scratch**](https://github.com/kishorhange111/rl-from-scratch) | Double/Dueling DQN, PPO (GAE, clipping, vectorized envs) & REINFORCE in PyTorch — 45-run 5-seed IQM benchmark (PPO **5/5** CartPole, Double DQN **5/5** Acrobot) |
| [**rlvr-grpo-from-scratch**](https://github.com/kishorhange111/rlvr-grpo-from-scratch) | GRPO / Dr. GRPO / RLOO / online DPO with matched-compute controls — RL **doubles pass@1 (18% → 34–38%)** while leaving pass@16 flat |
| [**arithmetic-transformer-interp**](https://github.com/kishorhange111/arithmetic-transformer-interp) | Activation patching & TopK SAEs (**99.97%** CE recovered) on addition transformers — shows **probe-decodable ≠ causally used** (88.5% probe acc vs 2% patching effect) |
| [**grokking-progress-measures**](https://github.com/kishorhange111/grokking-progress-measures) | Modular-addition grokking with Fourier-sparsity progress measures — sparsity rises **0.32 → 0.61** while test accuracy is still near chance |
| [**scaling-laws-from-scratch**](https://github.com/kishorhange111/scaling-laws-from-scratch) | Chinchilla-style IsoFLOP sweeps & parametric L(N, D) fits on byte-level GPTs — demonstrates batch-size step-starvation vs interior compute optimum |

</details>

<details>
<summary><strong>GPU Kernels &amp; Model Architectures from Scratch (4 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**triton-kernels-from-scratch**](https://github.com/kishorhange111/triton-kernels-from-scratch) | FlashAttention-2 forward + two-kernel backward, fused softmax & RMSNorm in **Triton** — values and gradients verified vs PyTorch (CI runs the real kernels in Triton's interpreter), benchmarked on GPU |
| [**moe-from-scratch**](https://github.com/kishorhange111/moe-from-scratch) | Mixture-of-Experts: top-k & expert-choice routing, capacity/token dropping (GShard priority), Switch balance + z-loss, shared experts, batched `(E, C, d)` experts — dense vs MoE at equal active params |
| [**sparse-autoencoders-interp**](https://github.com/kishorhange111/sparse-autoencoders-interp) | TopK / BatchTopK / L1 sparse autoencoders with AuxK — ground-truth feature recovery on a superposition toy model and CE-loss-recovered splicing on GPT-2 |
| [**ssm-from-scratch**](https://github.com/kishorhange111/ssm-from-scratch) | Mamba-2 from scratch: sequential, parallel-scan and chunked **SSD** algorithms (verified identical, incl. the attention duality), O(1) recurrent decoding — vs attention on associative recall, LM and decode cost |

</details>

<details>
<summary><strong>Applied ML, Causal Inference, MLOps &amp; Edge Systems (7 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**demand-forecasting-mlops**](https://github.com/kishorhange111/demand-forecasting-mlops) | M5 retail forecasting (30,490 series, **WRMSSE 0.5536**, 35% below seasonal naive) with conformal intervals, drift retraining, gated MLflow registry & FastAPI |
| [**two-tower-recommender**](https://github.com/kishorhange111/two-tower-recommender) | MovieLens 1M two-tower retrieval (logQ, item bias) + FAISS + LightGBM re-ranker & FastAPI benchmarked honestly against EASE & ItemKNN on a global temporal split |
| [**uplift-targeting**](https://github.com/kishorhange111/uplift-targeting) | Causal uplift modeling on Hillstrom (S, T, X, DR learners vs response modeling), Qini bootstrap CIs, budgeted targeting & off-policy evaluation |
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

<p align="center"><sub>B.Tech in Computer Science &amp; Engineering · DKTE Ichalkaranji (2019–2023) · CGPA 8.31 · Bengaluru, India</sub></p>
