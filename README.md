<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg?v=4">
  <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg?v=4">
  <img alt="Kishor Hange — AI / ML & Forward Deployed Engineer at E2open, Bengaluru. Enterprise MCP agents, production RAG, LLM evals, inference optimization, and distributed training." src="./assets/header-light.svg?v=4" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/kishorhange/"><img src="https://img.shields.io/badge/LinkedIn-kishorhange-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://kishorhange.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-kishorhange.vercel.app-111827?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
  <a href="mailto:kishorhange46@gmail.com"><img src="https://img.shields.io/badge/Email-kishorhange46%40gmail.com-D97757?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

## About

**Forward Deployed, ML & AI Engineer** at **E2open** (Bengaluru) with **~4 years of experience** taking machine learning and LLM systems from prototype to production. I specialize in the engineering around the model — secure MCP tool layers, hybrid RAG with automated eval gates, low-latency inference, distributed training, and observable MLOps — so AI systems stay fast, measurable, and reliable once real customers depend on them.

---

## Core Engineering Pillars

| Pillar | Focus Areas |
|---|---|
| **FDE & Agentic Systems** | Multi-tenant MCP servers, RBAC/ACL policy enforcement, stateful DAG/LangGraph runtimes, HITL approval workflows, PII & prompt-injection guardrails, immutable audit trails |
| **Production RAG & Evals** | Hybrid BM25 + dense retrieval (RRF), cross-encoder reranking, citation grounding, abstention, Ragas/DeepEval CI regression gates, statistical eval harnesses with bootstrap CIs |
| **ML Systems & Inference** | Quantization (int8, NF4, AWQ), pruning, ONNX Runtime / Optimum, `torch.compile`, speculative decoding, KV-cache capacity planning, vLLM concurrency & TTFT/TPOT benchmarking |
| **Distributed Training & MLOps** | PyTorch DDP & FSDP2, SFT / DPO / GRPO / QLoRA post-training, sharded checkpointing, gated MLflow registries, drift-triggered retraining, OpenTelemetry / Prometheus / Grafana |

---

## Production Impact at E2open

> **Software Engineer** (Sep 2025 – Present) · **Associate Software Engineer** (Jul 2023 – Sep 2025)

- **38% lower inference latency** via quantization and pruning (ONNX Runtime, Hugging Face Optimum), saving a full delivery sprint.
- **+9.5% classification accuracy** by replacing a legacy business-document classifier with a Random Forest on custom Word2Vec embeddings and fine-tuned BERT.
- **Enterprise MCP & Agentic Workflows:** Built agentic LLM workflows (LangChain, CrewAI, n8n) and **Model Context Protocol (MCP)** integrations for secure LLM access to enterprise databases.
- **Production RAG & Support Automation:** Shipped an LLM customer-support ticket resolution chatbot and RAG pipelines (LangChain, FAISS, Chroma) evaluated with **Ragas** and **DeepEval** for faithfulness and relevance.
- **Domain Fine-Tuning & Semantic Matching:** Fine-tuned multilingual/domain LLMs with PEFT (LoRA, QLoRA) tracked in MLflow & Comet ML, and built semantic document matching on GCP Vertex AI.
- **Observability & Data Pipelines:** Built real-time model monitoring and feedback loops (FastAPI, Airflow, Prometheus, Grafana) alongside Spark, Hadoop, Kafka, and Snowflake pipelines.

---

## Flagship Portfolio

### 1. Enterprise FDE & Agentic Systems

| Repository | Architecture & Measured Highlights |
|---|---|
| [**enterprise-mcp-agent-platform**](https://github.com/kishorhange111/enterprise-mcp-agent-platform) | Multi-tenant enterprise FDE platform: MCP server with read-only SQL/REST/doc connectors, RBAC & row-level policies, PII/prompt-injection guardrails, stateful checkpointed DAG runtime, HITL approval queue, immutable audit logs, OTel/Prometheus/Grafana, Helm/K8s & red-team security suite |
| [**mcp-sql-agent**](https://github.com/kishorhange111/mcp-sql-agent) | LangGraph text-to-SQL agent behind an MCP server with layered AST (`sqlglot`) + SQLite authorizer guardrails — **89/89 attack queries blocked**, 0 protected values leaked, 39/60 (65%) execution accuracy with a local 1.5B model |

### 2. Production RAG, Retrieval & Evaluation

| Repository | Architecture & Measured Highlights |
|---|---|
| [**production-rag-service**](https://github.com/kishorhange111/production-rag-service) | Production FastAPI RAG service: multi-format ingestion, hybrid BM25 + dense retrieval (RRF), cross-encoder reranking, ACL filtering, citation verification, abstention, SSE streaming, Prometheus metrics, Docker, and SQuAD 2.0 / faithfulness eval suite |
| [**llm-evaluation-harness**](https://github.com/kishorhange111/llm-evaluation-harness) | Reproducible LLM benchmark harness (MMLU, ARC, HellaSwag, GSM8K, sandboxed HumanEval) with position-bias-controlled LLM-as-judge, bootstrap CIs, and paired significance tests — matches EleutherAI `lm-eval` within 0.5 pts |
| [**embedding-finetuning-retrieval**](https://github.com/kishorhange111/embedding-finetuning-retrieval) | Domain embedding fine-tuning on BEIR FiQA: hard-negative mining, Matryoshka representation learning, int8 & binary vector compression, benchmarked against BM25 and the base bi-encoder |
| [**llm-structured-extraction**](https://github.com/kishorhange111/llm-structured-extraction) | Receipt field extraction on CORD with a small local LLM: real OCR (`rapidocr`), free vs schema-constrained decoding (`xgrammar`), arithmetic/grounding checks, and a repair loop benchmarked against rule-based baselines |

### 3. LLM Inference, Post-Training & Distributed Systems

| Repository | Architecture & Measured Highlights |
|---|---|
| [**llm-inference-optimization**](https://github.com/kishorhange111/llm-inference-optimization) | Single-GPU & serving inference benchmarks: int8/NF4/AWQ quantization vs perplexity, SDPA, `torch.compile` + static KV cache, speculative decoding, KV-cache capacity planning, and vLLM concurrency sweeps (TTFT/TPOT percentiles) |
| [**distributed-llm-training**](https://github.com/kishorhange111/distributed-llm-training) | GPT-2 pre-training stack in plain PyTorch: single GPU, DDP, and FSDP2 with bf16, `torch.compile`, activation checkpointing, and exact-resume sharded checkpoints — **52% MFU** on an A100 |
| [**mini-chatgpt**](https://github.com/kishorhange111/mini-chatgpt) | End-to-end post-training from a base LLM (`Qwen2.5-0.5B`): 160k-conversation SFT (127M tokens) + DPO written from scratch (12k pairs) — matches Qwen Instruct on IFEval (**36.7 vs 36.3**) and beats it on ARC-Easy (**+5 pts**) in ~3 GPU-hours |
| [**generative-ai-engineering**](https://github.com/kishorhange111/generative-ai-engineering) | 8 benchmarked LLM systems: QLoRA text-to-SQL (**60.0% → 66.2%**), 7B→0.5B distillation, function-calling agent (**16.7% → 94.8%** exact calls), GRPO on GSM8K, RAG eval, Qwen2-VL, Whisper Marathi (CER **53.6% → 14.7%**), and prompt-injection guardrails |

### 4. Applied ML, Causal Inference & MLOps

| Repository | Architecture & Measured Highlights |
|---|---|
| [**demand-forecasting-mlops**](https://github.com/kishorhange111/demand-forecasting-mlops) | M5 retail forecasting (30,490 series, **WRMSSE 0.5536**, 35% below seasonal naive) with rolling-origin backtests, conformal prediction intervals, gated MLflow registry, drift-triggered retraining, and a monitored FastAPI service |
| [**two-tower-recommender**](https://github.com/kishorhange111/two-tower-recommender) | Two-stage MovieLens 1M recommender: two-tower retrieval (in-batch softmax, logQ correction, item bias), FAISS index, LightGBM re-ranker, and FastAPI service — rigorously benchmarked against EASE and ItemKNN on a global temporal split |
| [**uplift-targeting**](https://github.com/kishorhange111/uplift-targeting) | Causal uplift modeling on the Hillstrom randomized experiment: S, T, X, and DR learners vs response-model targeting, Qini curves with bootstrap CIs, budget constraints, and off-policy policy evaluation |

<details>
<summary><strong>More Projects (Deep Learning, Edge Compilation &amp; Observability)</strong></summary>

| Repository | Highlights |
|---|---|
| [**deep-learning-portfolio**](https://github.com/kishorhange111/deep-learning-portfolio) | 14 CV, NLP & generative projects: BERT distillation + ONNX + int8 (**4.8× faster, 85% smaller**), GPT-2 LoRA (-69% GPU mem), ViT, U-Net, AdaIN, Music Transformer, molecule GPT |
| [**cnn-edge-optimization-tflite-onnx-tvm**](https://github.com/kishorhange111/cnn-edge-optimization-tflite-onnx-tvm) | Edge compilation of a Keras CNN through TFLite, ONNX, and Apache TVM pipelines (**~12× smaller** models) |
| [**vm-energy-agent**](https://github.com/kishorhange111/vm-energy-agent) | Go monitoring agent estimating VM power consumption and exporting Prometheus / OpenTelemetry metrics |
| [**llm-token-visualizer**](https://github.com/kishorhange111/llm-token-visualizer) | Interactive Streamlit app comparing tokenization across BERT, GPT-2, GPT-4, Phi-3, and DeepSeek |

</details>

---

## Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,fastapi,docker,kubernetes,gcp,aws,linux,git,postgres&perline=12" alt="Tech stack icons" />
</p>

- **GenAI & Agents:** LangChain · LangGraph · CrewAI · MCP · Hugging Face Transformers · PEFT (LoRA/QLoRA) · TRL (SFT/DPO/GRPO) · FAISS · Chroma · Ragas · DeepEval
- **ML & Optimization:** PyTorch (DDP/FSDP2) · TensorFlow/Keras · scikit-learn · LightGBM · XGBoost · vLLM · ONNX Runtime · Hugging Face Optimum · TFLite · Apache TVM
- **MLOps, Observability & Data:** FastAPI · Docker · Kubernetes · Helm · GitHub Actions · MLflow · Airflow · OpenTelemetry · Prometheus · Grafana · Spark · Kafka · Snowflake
- **Cloud & Languages:** Python · SQL · Java · C++ · Go · GCP (Vertex AI) · AWS (Bedrock, SageMaker, S3)

---

## GitHub Activity

<p align="center">
  <img width="100%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=kishorhange111&theme=tokyonight" alt="Contribution overview" />
</p>
<p align="center">
  <img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=kishorhange111&theme=tokyonight" alt="GitHub stats" />
  <img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=kishorhange111&theme=tokyonight" alt="Top languages by commit" />
</p>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake.svg" />
    <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/kishorhange111/kishorhange111/output/github-snake.svg" />
  </picture>
</p>

<p align="center"><sub>B.Tech in Computer Science &amp; Engineering · DKTE Society's Textile and Engineering Institute, Ichalkaranji (2019–2023) · CGPA 8.31</sub></p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg?v=3">
  <source media="(prefers-color-scheme: light)" srcset="./assets/footer-light.svg?v=3">
  <img alt="Thanks for visiting. Kishor Hange, Bengaluru, IN — FDE, ML & AI Systems" src="./assets/footer-light.svg?v=3" width="100%">
</picture>
