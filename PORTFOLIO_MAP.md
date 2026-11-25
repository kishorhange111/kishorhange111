# Portfolio Map — Competency Guide for Hiring Managers & Recruiters

> **Kishor Hange** · Software Engineer (AI / ML & Forward Deployed Systems) @ **E2open** (~4 YOE, Bengaluru)  
> Back to [Profile README](./README.md) · [LinkedIn](https://www.linkedin.com/in/kishorhange/) · [Portfolio](https://kishorhange.vercel.app/)

This guide maps **Forward Deployed Engineer (FDE)**, **AI Engineer**, **ML Systems / MLOps Engineer**, and **Research Engineer** competencies directly to public repositories, architectural patterns, and verified engineering artifacts.

---

## 60-Second Reviewer Guide (Start Here by Role)

| Target Role | Start-Here Repositories | What to Look For |
|---|---|---|
| **Forward Deployed Engineer (FDE)** | [`enterprise-mcp-agent-platform`](https://github.com/kishorhange111/enterprise-mcp-agent-platform), [`agent-reliability-bench`](https://github.com/kishorhange111/agent-reliability-bench), [`llm-reliability-gateway`](https://github.com/kishorhange111/llm-reliability-gateway) | Agent reliability (pass^k, fault injection, policy violations), gateway fallback/circuit breakers under failure injection, multi-tenant RBAC/ACL scoping, customer config-as-code, MCP connectors, HITL approvals, PII/SQLi red-team suites, Helm/K8s, ADRs |
| **AI / LLM Engineer** | [`production-rag-service`](https://github.com/kishorhange111/production-rag-service), [`agent-memory-bench`](https://github.com/kishorhange111/agent-memory-bench), [`agent-runtime-ts`](https://github.com/kishorhange111/agent-runtime-ts), [`llm-evaluation-harness`](https://github.com/kishorhange111/llm-evaluation-harness), [`embedding-finetuning-retrieval`](https://github.com/kishorhange111/embedding-finetuning-retrieval), [`llm-structured-extraction`](https://github.com/kishorhange111/llm-structured-extraction) | Hybrid BM25+dense retrieval, cross-encoder reranking, citation verification, statistical evals (bootstrap CIs, paired tests), Matryoshka embeddings, schema-constrained decoding, long-term agent memory (fact stores vs retrieval), TypeScript agent runtime |
| **ML Systems / Inference / Training Engineer** | [`llm-inference-optimization`](https://github.com/kishorhange111/llm-inference-optimization), [`llm-capacity-planner`](https://github.com/kishorhange111/llm-capacity-planner), [`distributed-llm-training`](https://github.com/kishorhange111/distributed-llm-training), [`mini-chatgpt`](https://github.com/kishorhange111/mini-chatgpt) | int8/NF4/AWQ quantization, `torch.compile`, speculative decoding, vLLM TTFT/TPOT sweeps, roofline + continuous-batching GPU sizing under SLOs, DDP/FSDP2 (52% MFU on A100), SFT + from-scratch DPO |
| **Research Engineer / RL & Post-Training** | [`rlvr-grpo-from-scratch`](https://github.com/kishorhange111/rlvr-grpo-from-scratch), [`arithmetic-transformer-interp`](https://github.com/kishorhange111/arithmetic-transformer-interp), [`grokking-progress-measures`](https://github.com/kishorhange111/grokking-progress-measures), [`scaling-laws-from-scratch`](https://github.com/kishorhange111/scaling-laws-from-scratch) | Controlled multi-seed experiments with matched compute, GRPO/Dr. GRPO/RLOO/DPO from scratch, probes + activation patching + sparse autoencoders, grokking progress measures, IsoFLOP scaling-law fits (batch-size pilot), honest reporting of null and negative results |
| **Applied ML / MLOps Engineer** | [`demand-forecasting-mlops`](https://github.com/kishorhange111/demand-forecasting-mlops), [`two-tower-recommender`](https://github.com/kishorhange111/two-tower-recommender), [`uplift-targeting`](https://github.com/kishorhange111/uplift-targeting) | Rolling-origin backtests, conformal intervals, gated MLflow registry, drift retraining, two-stage FAISS + LightGBM ranking, causal uplift (S/T/X/DR learners) |

---

## Competency Matrix

### 1. Forward Deployed Engineering & Enterprise Agentic Systems

| Competency | Public Proof (Repo) | Concrete Artifacts & Signals |
|---|---|---|
| **MCP Tool Layer & Enterprise Connectors** | [`enterprise-mcp-agent-platform`](https://github.com/kishorhange111/enterprise-mcp-agent-platform), [`mcp-sql-agent`](https://github.com/kishorhange111/mcp-sql-agent) | MCP server & tool registry, read-only SQL connector with AST (`sqlglot`) validation, idempotent REST/ticketing connector, ACL-filtered doc store |
| **Multi-Tenant Security, RBAC & Guardrails** | [`enterprise-mcp-agent-platform`](https://github.com/kishorhange111/enterprise-mcp-agent-platform), [`mcp-sql-agent`](https://github.com/kishorhange111/mcp-sql-agent) | Row-level tenant policies, PII redaction, prompt-injection screening, SQLi red-team tests (**89/89** attack queries blocked, 0 leaks) |
| **Stateful Agent Runtimes & HITL** | [`enterprise-mcp-agent-platform`](https://github.com/kishorhange111/enterprise-mcp-agent-platform), [`generative-ai-engineering`](https://github.com/kishorhange111/generative-ai-engineering) | Checkpointed DAG runtime, structured output validation with retries/fallbacks, human-in-the-loop escalation queue, function-calling accuracy (**16.7% → 94.8%**) |
| **Compliance, Auditability & Deployment** | [`enterprise-mcp-agent-platform`](https://github.com/kishorhange111/enterprise-mcp-agent-platform) | Immutable audit logs, customer YAML config-as-code profiles, OpenTelemetry + Prometheus + Grafana dashboards, Docker Compose, Helm/K8s manifests, ADRs |
| **LLM Gateway & Resilience Engineering** | [`llm-reliability-gateway`](https://github.com/kishorhange111/llm-reliability-gateway) | Multi-provider fallback, sliding-window failure-rate circuit breakers, full-jitter retries, per-tenant rate limits/budgets, exact & semantic caching, Prometheus; open-loop failure-injection sim (100% availability through a hanging outage, 64% fewer wasted calls, p95 halved; diagnosed a count-based breaker cascade) |
| **Agent Runtime in TypeScript** | [`agent-runtime-ts`](https://github.com/kishorhange111/agent-runtime-ts) | zod-typed tools, approval hook for write tools, idempotent-only retries, timeouts, loop guard, step/cost budgets, all stop reasons handled, OTel-shaped JSONL traces; guard eval: unsafe actions 16.3% → 0, runaway loops 16.3% → 0, cost −83% |
| **Agent Memory & Context Engineering** | [`agent-memory-bench`](https://github.com/kishorhange111/agent-memory-bench) | Recency vs BM25 vs embeddings vs fact store with supersession vs hybrid; oracle/gullible reader bounds; budget, history-length and extractor-noise sweeps (confusion ≈ 2× as costly as misses; hybrid recovers misses) |

### 2. Production RAG, Retrieval & Evaluation

| Competency | Public Proof (Repo) | Concrete Artifacts & Signals |
|---|---|---|
| **Enterprise Hybrid RAG** | [`production-rag-service`](https://github.com/kishorhange111/production-rag-service) | Multi-format/table ingestion, BM25 + dense retrieval (RRF), cross-encoder reranking, ACL filtering, citation verifier, abstention, FastAPI SSE streaming |
| **Serverless Multi-Tenant RAG (AWS)** | [`bedrock-serverless-rag`](https://github.com/kishorhange111/bedrock-serverless-rag) | Terraform AWS design (S3→SQS→Lambda idempotent ingestion, OpenSearch k-NN tenant pre-filter, Bedrock Claude, Cognito JWT, Step Functions backfill); 99.3% answerable accuracy, 100% abstention, 0 cross-tenant citations |
| **Domain Retrieval & Compression** | [`embedding-finetuning-retrieval`](https://github.com/kishorhange111/embedding-finetuning-retrieval) | BEIR FiQA hard-negative mining, Matryoshka representation learning, int8 & binary vector quantization benchmarked vs BM25 & base encoder |
| **Knowledge Graphs, Entity Linking & Multi-Hop QA** | [`graphrag-entity-linking`](https://github.com/kishorhange111/graphrag-entity-linking) | Mention detection, entity linking ablations (naive / context / coherence / oracle) with ambiguity-bucket error analysis, relation extraction with coreference + type checks, GraphRAG-style entity-index hops vs single-shot & iterative RAG, nDCG and support recall over 3 seeds |
| **Structured Extraction & Constrained Decoding** | [`llm-structured-extraction`](https://github.com/kishorhange111/llm-structured-extraction) | CORD receipt OCR (`rapidocr`), free vs schema-constrained decoding (`xgrammar`), arithmetic/grounding checks, automated repair loop |
| **Statistical LLM Evaluation** | [`llm-evaluation-harness`](https://github.com/kishorhange111/llm-evaluation-harness) | MMLU, ARC, HellaSwag, GSM8K, sandboxed HumanEval, position-bias-controlled LLM judge, bootstrap CIs & paired significance tests (within 0.5 pts of `lm-eval`) |

### 3. ML Systems, Inference Optimization & Distributed Training

| Competency | Public Proof (Repo) | Concrete Artifacts & Signals |
|---|---|---|
| **Inference Optimization & Serving** | [`llm-inference-optimization`](https://github.com/kishorhange111/llm-inference-optimization), [`cnn-edge-optimization-tflite-onnx-tvm`](https://github.com/kishorhange111/cnn-edge-optimization-tflite-onnx-tvm) | int8/NF4/AWQ quantization vs perplexity, SDPA, `torch.compile` + static KV cache, speculative decoding, KV-cache sizing, vLLM TTFT/TPOT concurrency sweeps, edge compilation (~12× smaller) |
| **GPU Capacity Planning & SLO Sizing** | [`llm-capacity-planner`](https://github.com/kishorhange111/llm-capacity-planner) | Roofline cost model (FLOPs, HBM, KV-cache, TP all-reduce) + continuous-batching simulator + SLO planner (kv8 decode throughput, 4× GQA concurrency, TP2 vs TP1 trade-offs) |
| **Distributed Pre-Training** | [`distributed-llm-training`](https://github.com/kishorhange111/distributed-llm-training) | Plain-PyTorch GPT-2 stack across single GPU, DDP, and FSDP2 with bf16, activation checkpointing, and exact-resume sharded checkpoints (**52% MFU** on A100) |
| **Post-Training (SFT, DPO, GRPO, QLoRA)** | [`mini-chatgpt`](https://github.com/kishorhange111/mini-chatgpt), [`generative-ai-engineering`](https://github.com/kishorhange111/generative-ai-engineering) | Qwen2.5-0.5B SFT (127M tokens) + from-scratch DPO (IFEval **36.7 vs 36.3**, ARC-Easy **+5 pts**); QLoRA text-to-SQL (**60.0% → 66.2%**); 7B→0.5B distillation; GRPO on GSM8K |

### 4. Reinforcement Learning, Research & Agent Reliability

| Competency | Public Proof (Repo) | Concrete Artifacts & Signals |
|---|---|---|
| **Deep RL Algorithms** | [`rl-from-scratch`](https://github.com/kishorhange111/rl-from-scratch) | DQN (Double/Dueling/Polyak), PPO (GAE, clipping, truncation bootstrap), REINFORCE; 5-seed IQM + steps-to-solve (PPO **5/5** CartPole, Double DQN **5/5** Acrobot in 20.8k steps) |
| **RL for LLMs (RLVR)** | [`rlvr-grpo-from-scratch`](https://github.com/kishorhange111/rlvr-grpo-from-scratch) | GRPO / Dr. GRPO / RLOO advantage and loss-aggregation variants, k3-KL, online DPO with verifier-built pairs, unbiased pass@k, continued-SFT control at matched optimizer steps |
| **Mechanistic Interpretability & Science of DL** | [`arithmetic-transformer-interp`](https://github.com/kishorhange111/arithmetic-transformer-interp), [`grokking-progress-measures`](https://github.com/kishorhange111/grokking-progress-measures), [`scaling-laws-from-scratch`](https://github.com/kishorhange111/scaling-laws-from-scratch) | Probes vs causal activation patching (carry localised to `b0` → `=`; 88.5% probe acc but 2% causal effect), TopK SAEs (99.97% spliced CE recovered), grokking Fourier progress measures, Chinchilla-style IsoFLOP & parametric L(N, D) scaling-law fits |
| **Agent Evaluation & Reliability** | [`agent-reliability-bench`](https://github.com/kishorhange111/agent-reliability-bench) | Final-state grading, policy monitor, pass^k (pass^1 0.77 → pass^8 0.32 at 10% faults), fault-to-violation cascades, Claude tool-use adapter |

### 5. Applied ML, Causal Modeling & MLOps

| Competency | Public Proof (Repo) | Concrete Artifacts & Signals |
|---|---|---|
| **Forecasting & MLOps Lifecycle** | [`demand-forecasting-mlops`](https://github.com/kishorhange111/demand-forecasting-mlops) | M5 global LightGBM (**WRMSSE 0.5536**, 35% below seasonal naive), conformal intervals, gated MLflow registry, drift-triggered retraining, monitored FastAPI service |
| **Retrieval & Ranking Systems** | [`two-tower-recommender`](https://github.com/kishorhange111/two-tower-recommender) | MovieLens 1M two-tower retrieval (logQ, item bias) + FAISS + LightGBM re-ranker rigorously measured against EASE and ItemKNN on a global temporal split |
| **Causal Inference & Policy Evaluation** | [`uplift-targeting`](https://github.com/kishorhange111/uplift-targeting) | Hillstrom randomized experiment: S, T, X, and DR learners vs response modeling, Qini curves with bootstrap CIs, budgeted targeting, off-policy evaluation |

---

## Production Experience Summary (E2open · Jul 2023 – Present)

- **Role progression:** Associate Software Engineer (Jul 2023 – Sep 2025) → Software Engineer (Sep 2025 – Present)
- **Measured production wins:** **-38% inference latency** (quantization/pruning via ONNX Runtime & HF Optimum), **+9.5% classifier accuracy** (RF + custom Word2Vec + fine-tuned BERT)
- **Systems shipped:** Automated LLM customer-support chatbot, RAG pipelines evaluated with Ragas & DeepEval, LangChain/CrewAI/n8n agentic workflows with MCP enterprise DB access, PEFT (LoRA/QLoRA) fine-tuning, Vertex AI semantic document matching, FastAPI/Airflow/Prometheus/Grafana monitoring, Spark/Hadoop/Kafka/Snowflake data pipelines.

---

## Open Source Contributions

- **python/cpython** — [PR #148978](https://github.com/python/cpython/pull/148978) (**Merged**): `gh-148849: Deprecate http.cookies.BaseCookie.js_output()`
- **sphinx-doc/sphinx** — [PR #14421](https://github.com/sphinx-doc/sphinx/pull/14421) (**Open**): `Fix #2835: Trigger rebuild when theme files change`
