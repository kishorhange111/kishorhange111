<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg?v=9">
  <source media="(prefers-color-scheme: light)" srcset="./assets/header-light.svg?v=9">
  <img alt="Kishor Hange — Forward Deployed, ML & AI Engineer at E2open, Bengaluru (~4 YOE). Live AI Systems Topology and Production Telemetry." src="./assets/header-light.svg?v=9" width="100%">
</picture>

<p align="center">
  <a href="https://kishorhange.vercel.app/">Portfolio</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/kishorhange/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="./PORTFOLIO_MAP.md">Portfolio Map</a> &nbsp;·&nbsp;
  <a href="https://github.com/python/cpython/pull/148978">CPython PR #148978</a> &nbsp;·&nbsp;
  <a href="mailto:kishorhange46@gmail.com">Email</a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/kpi-dark.svg?v=3">
  <source media="(prefers-color-scheme: light)" srcset="./assets/kpi-light.svg?v=3">
  <img alt="Key Impact: -38% Inference Latency at E2open, +9.5% Classifier Accuracy at E2open, and CPython Open-Source Contributor (merged python/cpython#148978)." src="./assets/kpi-light.svg?v=3" width="100%">
</picture>

**Forward Deployed, ML & AI Engineer** at **E2open** (Bengaluru, **~4 YOE**) taking LLM and ML systems from prototype to production — specializing in secure MCP agent platforms, hybrid RAG with automated eval gates, low-latency inference, distributed training, and observable MLOps. Outside production systems, I run controlled multi-seed deep learning experiments (RLVR/GRPO, mechanistic interpretability, grokking, scaling laws, GPU kernels) and report null results as carefully as wins.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/architecture-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./assets/architecture-light.svg?v=1">
  <img alt="End-to-End Production AI Architecture: Enterprise Data and MCP to RBAC and Guardrails to Hybrid RAG and Agents to vLLM/ONNX Serving to Evals and OpenTelemetry." src="./assets/architecture-light.svg?v=1" width="100%">
</picture>

---

## Flagship Systems

> Hiring manager or recruiter? Open the [**Portfolio Competency Map**](./PORTFOLIO_MAP.md) for a 60-second role-based guide across **FDE**, **AI Engineer**, **ML Systems**, **Research**, and **MLOps**.

<p align="center">
  <a href="https://github.com/kishorhange111/enterprise-mcp-agent-platform"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-1-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-1-light.svg?v=1"><img alt="enterprise-mcp-agent-platform — FDE MCP Platform" src="./assets/card-1-light.svg?v=1" width="48.5%"></picture></a>&nbsp;&nbsp;<a href="https://github.com/kishorhange111/production-rag-service"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-2-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-2-light.svg?v=1"><img alt="production-rag-service — Production Hybrid RAG" src="./assets/card-2-light.svg?v=1" width="48.5%"></picture></a>
</p>
<p align="center">
  <a href="https://github.com/kishorhange111/llm-evaluation-harness"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-3-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-3-light.svg?v=1"><img alt="llm-evaluation-harness — LLM Evaluation" src="./assets/card-3-light.svg?v=1" width="48.5%"></picture></a>&nbsp;&nbsp;<a href="https://github.com/kishorhange111/llm-inference-optimization"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-4-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-4-light.svg?v=1"><img alt="llm-inference-optimization — Inference Optimization" src="./assets/card-4-light.svg?v=1" width="48.5%"></picture></a>
</p>
<p align="center">
  <a href="https://github.com/kishorhange111/distributed-llm-training"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-5-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-5-light.svg?v=1"><img alt="distributed-llm-training — Distributed Training" src="./assets/card-5-light.svg?v=1" width="48.5%"></picture></a>&nbsp;&nbsp;<a href="https://github.com/kishorhange111/mcp-sql-agent"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-6-dark.svg?v=1"><source media="(prefers-color-scheme: light)" srcset="./assets/card-6-light.svg?v=1"><img alt="mcp-sql-agent — MCP SQL Security" src="./assets/card-6-light.svg?v=1" width="48.5%"></picture></a>
</p>

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
<summary><strong>Retrieval, Similarity Search, Data Dedup &amp; Structured Extraction (5 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**llm-data-dedup**](https://github.com/kishorhange111/llm-data-dedup) | Pretraining-data dedup from scratch — MinHash, one-permutation hashing with optimal densification, LSH banding and suffix-array exact-substring dedup — scored against an **exact prefix-filter Jaccard join** on 22k real Python files: tuned banding recovers **99.1%+** of the exact removals, unverified LSH clustering over-removes by up to **84%**, and per-cluster averaging recovers the S-curve (**0.793 vs 0.795** predicted) where correlated pairs break the per-pair check |
| [**ann-search-from-scratch**](https://github.com/kishorhange111/ann-search-from-scratch) | The index structures inside FAISS and vector databases in NumPy — k-means IVF, **PQ with ADC lookup tables, IVF-PQ with exact re-ranking, OPQ** (alternating k-means + Procrustes) and **HNSW** with the paper's neighbour-selection heuristic. On SIFT, recall matches FAISS within **0.007** at every nprobe; HNSW reaches **0.983 recall evaluating 1.5% of distances**; PQ16 plateaus at 0.64 recall until re-ranking lifts it to **0.994**; the heuristic adds +0.05 to +0.13 recall |
| [**embedding-finetuning-retrieval**](https://github.com/kishorhange111/embedding-finetuning-retrieval) | Domain embedding fine-tuning on BEIR FiQA: hard-negative mining, Matryoshka representation learning, int8 & binary vector compression + FastAPI serving |
| [**graphrag-entity-linking**](https://github.com/kishorhange111/graphrag-entity-linking) | Multi-hop QA benchmark (single-shot vs iterative RAG vs entity-linked knowledge graph) — entity-ID graph hops hit **100%** vs **88%** name-based iterative RAG and **~1%** single-shot |
| [**llm-structured-extraction**](https://github.com/kishorhange111/llm-structured-extraction) | Receipt field extraction on CORD with a small local LLM: RapidOCR, free vs schema-constrained decoding (xgrammar), arithmetic/grounding checks, repair loop & FastAPI service |

</details>

<details>
<summary><strong>LLM Post-Training, Capacity Planning &amp; Deep Learning Research (8 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**llm-capacity-planner**](https://github.com/kishorhange111/llm-capacity-planner) | Roofline cost model + continuous-batching simulator + SLO planner, **calibrated against real vLLM on a T4**: replaying the closed-loop schedule and separating attention efficiency cut model error **76% → 12%**, and showed T4 attention (TRITON_ATTN) runs at ~1% of peak vs 27% for GEMMs; per-GPU chunked-prefill tuning finds **up to 24% more SLO-compliant throughput** than a fixed 2,048-token budget |
| [**mini-chatgpt**](https://github.com/kishorhange111/mini-chatgpt) | Base LLM (`Qwen2.5-0.5B`) → 160k SFT (127M tokens) → from-scratch DPO (12k pairs) — matches Qwen Instruct on IFEval (**36.7 vs 36.3**) and beats it on ARC-Easy (**+5 pts**) in ~3 GPU-hours |
| [**generative-ai-engineering**](https://github.com/kishorhange111/generative-ai-engineering) | 8 benchmarked LLM systems: QLoRA text-to-SQL (**60.0% → 66.2%**), 7B→0.5B distillation, function-calling (**16.7% → 94.8%**), GRPO, Qwen2-VL, Whisper Marathi (CER **53.6% → 14.7%**), guardrails |
| [**rl-from-scratch**](https://github.com/kishorhange111/rl-from-scratch) | Double/Dueling DQN, PPO (GAE, clipping, vectorized envs) & REINFORCE in PyTorch — 45-run 5-seed IQM benchmark (PPO **5/5** CartPole, Double DQN **5/5** Acrobot) |
| [**rlvr-grpo-from-scratch**](https://github.com/kishorhange111/rlvr-grpo-from-scratch) | GRPO / Dr. GRPO / RLOO / online DPO with matched-compute controls — RL **doubles pass@1 (18% → 34–38%)** while leaving pass@16 flat |
| [**arithmetic-transformer-interp**](https://github.com/kishorhange111/arithmetic-transformer-interp) | Activation patching & TopK SAEs (**99.97%** CE recovered) on addition transformers — shows **probe-decodable ≠ causally used** (88.5% probe acc vs 2% patching effect) |
| [**grokking-progress-measures**](https://github.com/kishorhange111/grokking-progress-measures) | Modular-addition grokking with Fourier-sparsity progress measures — sparsity rises **0.32 → 0.61** while test accuracy is still near chance |
| [**scaling-laws-from-scratch**](https://github.com/kishorhange111/scaling-laws-from-scratch) | Chinchilla-style IsoFLOP sweeps & parametric L(N, D) fits on byte-level GPTs — demonstrates batch-size step-starvation vs interior compute optimum |

</details>

<details>
<summary><strong>GPU Kernels &amp; Model Architectures from Scratch (27 repos)</strong></summary>

| Repository | Highlights |
|---|---|
| [**triton-kernels-from-scratch**](https://github.com/kishorhange111/triton-kernels-from-scratch) | FlashAttention-2 forward + two-kernel backward, fused softmax & RMSNorm in **Triton** — values and gradients verified vs PyTorch (CI runs the real kernels in Triton's interpreter); on a T4 the fused RMSNorm hits **~230 GB/s (9× eager)** and a PTX diagnosis shows why attention lags (no `mma` emitted on sm75); plus a vLLM-style **paged-attention decode** kernel with flash-decoding split-K |
| [**moe-from-scratch**](https://github.com/kishorhange111/moe-from-scratch) | Mixture-of-Experts: top-k & expert-choice routing, capacity/token dropping (GShard priority), Switch balance + z-loss, shared experts, batched `(E, C, d)` experts — dense vs MoE at equal active params |
| [**sparse-autoencoders-interp**](https://github.com/kishorhange111/sparse-autoencoders-interp) | TopK / BatchTopK / L1 sparse autoencoders with AuxK — on a superposition toy model TopK recovers **100%** of ground-truth features while L1 recovers ~0% despite lower FVU; on GPT-2 layer 6, **TopK recovers 98.6% of CE loss at L0 = 32**, while L1 leaves 75% of latents dead |
| [**ssm-from-scratch**](https://github.com/kishorhange111/ssm-from-scratch) | Mamba-2 from scratch: sequential, parallel-scan and chunked **SSD** algorithms (verified identical, incl. the attention duality), O(1) recurrent decoding — on a T4 the decode step stays **flat at 3.7 ms while attention grows to 65 ms at 65k tokens** (271 KiB state vs 256 MiB KV cache); MQAR recall gap vs attention |
| [**long-context-rope-scaling**](https://github.com/kishorhange111/long-context-rope-scaling) | RoPE context extension from scratch — Position Interpolation, NTK-aware, dynamic NTK and **YaRN**, each pinned by a property test. Measured on a T4: zero-shot at 16× length YaRN holds **1.97 bits/byte vs 4.89** for plain RoPE; fine-tuning finds scaled RoPE loses short-range passkey retrieval |
| [**optimizers-from-scratch**](https://github.com/kishorhange111/optimizers-from-scratch) | AdamW, Lion, Adafactor and **Muon** (Newton–Schulz orthogonalisation) from their papers — verified against defining properties, then compared on a GPT: on a T4, **Muon beats AdamW at every lr tried (1.25 vs 1.50 bits/byte) with half the optimizer state** |
| [**kv-cache-compression**](https://github.com/kishorhange111/kv-cache-compression) | KV-cache eviction (sliding window, StreamingLLM sinks, **H2O**, TOVA) and **KIVI**-style 2/4/8-bit KV on a hand-written GPT-2 decode loop — on a T4, eviction at 50% memory matches full-cache perplexity yet **loses long-range copying (≤10% vs 97.6%)**, while 4-bit KV with per-channel keys keeps **97.2% at 31% memory** |
| [**llm-quantization-from-scratch**](https://github.com/kishorhange111/llm-quantization-from-scratch) | **GPTQ** (Cholesky H⁻¹, lazy batch updates, act-order), **AWQ** and **SmoothQuant** W8A8 from their papers on GPT-2 — on a T4, GPTQ w4 costs **+1.2 ppl vs +3.4 for RTN**, holds w3 at +9 where RTN collapses (+35); diagnoses why smoothing every linear layer gives ppl 2325 (a GELU channel 155× outside its calibration range) |
| [**mup-from-scratch**](https://github.com/kishorhange111/mup-from-scratch) | **μP** (Tensor Programs V) by hand — on a T4 the best lr is **2⁻⁸ at every width 128→1024 under μP** while SP's drifts 8× (2⁻⁸→2⁻¹¹); coordinate check flat (×1.0 vs SP ×4.1); found and ablated two common variants that broke the first run (a zero-init readout alone cost 0.6 nats/byte) |
| [**masked-diffusion-lm**](https://github.com/kishorhange111/masked-diffusion-lm) | Absorbing-state **discrete diffusion LM** (MDLM / LLaDA) vs an equal-size autoregressive model — 1/t-weighted NELBO, ancestral & confidence-ordered samplers, steps-vs-quality and infilling |
| [**test-time-compute-scaling**](https://github.com/kishorhange111/test-time-compute-scaling) | Test-time compute on GSM8K with vLLM — unbiased pass@k oracle vs self-consistency, confidence-weighted voting and best-of-N, plus confidence calibration |
| [**attention-variants-mla**](https://github.com/kishorhange111/attention-variants-mla) | MHA / GQA / MQA and DeepSeek-V2 **Multi-head Latent Attention** with decoupled RoPE — the **absorbed-matrix decode path** (no per-head K/V ever materialised) is verified equal to the naive forward to 1e-10. On a T4, **GQA-2 matches MHA at a third of the cache**, while a d_c sweep shows MLA needs a latent of about 192 to reach MQA's quality, an honest negative at 10M parameters |
| [**speculative-decoding**](https://github.com/kishorhange111/speculative-decoding) | Speculative decoding on a hand-written GPT-2 with a roll-back KV cache — exact accept/reject rule (Monte Carlo test that output matches the target distribution, with a power control), prompt-lookup drafting; on a T4 **prompt lookup gives 1.95–2.12×** over gpt2-xl greedy and a gpt2 draft 1.73× (γ=4), while the higher-acceptance gpt2-medium draft is slower |
| [**medusa-heads-from-scratch**](https://github.com/kishorhange111/medusa-heads-from-scratch) | **Medusa-1** on Qwen2.5-0.5B with its own attention and a **compacting KV cache** — tree-attention verification proven equal to greedy decoding in float64, candidate trees chosen from measured head accuracy (prediction within 3% of measurement); on a T4 a 64-node tree gives **2.00 tokens/step and 1.53× wall clock**. A float16/float32 agreement check caught Qwen's default repetition penalty corrupting the self-distilled data |
| [**grpo-from-scratch**](https://github.com/kishorhange111/grpo-from-scratch) | **GRPO vs Dr. GRPO** on Qwen2.5-0.5B-Instruct through hand-written LoRA (adapters-off = KL reference, no second model copy) — RL with verifiable arithmetic rewards, resumable across 40-minute GPU sessions. On a T4, **held-out accuracy goes from 0% to 85% in 50 steps**, mostly from learning the answer format, as the README spells out; tests pin the REINFORCE limit, clipping, k3 unbiasedness and each aggregation's length bias |
| [**sequence-parallel-attention**](https://github.com/kishorhange111/sequence-parallel-attention) | Context parallelism — **ring attention with a hand-written backward** (dK/dV travel with their shard), **zigzag** causal load balancing (1.82× shorter critical path at P = 8) and **DeepSpeed-Ulysses** all-to-all; forward and all gradients exact to 1e-10 on a 4-process group; a measured benchmark matches the **closed-form bytes on the wire** for both methods and shows zigzag cutting the slowest rank's time **1.36×** |
| [**model-parallelism-from-scratch**](https://github.com/kishorhange111/model-parallelism-from-scratch) | **Megatron tensor parallelism** (f/g conjugate ops, column/row-parallel, head-sharded attention, vocab-parallel cross-entropy), **sequence parallelism**, and **GPipe vs 1F1B** pipelines with a bubble simulator — every gradient shard matches single-device training to 1e-10; on real processes the measured bubble tracks (p − 1)/(m + p − 1), and the step time is best at m = 4 because micro-batch compute grows **3.5×** at m = 32 |
| [**fp8-training-from-scratch**](https://github.com/kishorhange111/fp8-training-from-scratch) | FP8 / MXFP8 / MXFP4 / **NVFP4** training recipes from scratch, **bit-exact against PyTorch's float8 casts** — per-tensor, delayed, DeepSeek-V3 1×128 block and OCP MX microscaling, each GEMM quantised along its own reduction axis. On real GPT tensors gradients reach amax/rms **164**; block-scaled E4M3 beats per-tensor E5M2 by **4.7 dB on weight gradients**, NVFP4 beats MXFP4 by 3.5–4.6 dB, and a random Hadamard transform adds **3.0 dB** to MXFP4 wgrad |
| [**collectives-from-scratch**](https://github.com/kishorhange111/collectives-from-scratch) | **All-reduce on point-to-point sends only** — naive, binomial tree, recursive doubling, **ring** (reduce-scatter + all-gather) and **Rabenseifner**, with rounds and bytes tested against the closed forms (ring hits the 2n(p−1)/p bound exactly). Measured on real processes: ring is **2.8–5.3× slower below 256 KB** (rounds) and **1.5–2.0× faster at 16–64 MB**; on one host a tree matches ring because total traffic, not per-rank bytes, is what costs — a shared-bus term **halves the α-β fit error** |
| [**mini-vllm**](https://github.com/kishorhange111/mini-vllm) | An LLM **serving engine** from scratch — paged KV block allocator with **prefix caching** (chained block hashes, LRU eviction), **continuous batching** with chunked prefill and preemption-by-recompute, ragged batched GPT-2 forward; output token-for-token identical to sequential decoding even under forced preemption; on a T4 **continuous batching is 4.1× static batching**, and prefix caching cuts computed tokens 45% |
| [**linear-attention-deltanet**](https://github.com/kishorhange111/linear-attention-deltanet) | Linear, gated and **DeltaNet** attention — DeltaNet's chunkwise **WY / triangular-solve** algorithm proven equal to the delta-rule recurrence; on a T4, with a short conv, **DeltaNet holds 99.8% recall at 64 pairs while linear attention falls to 57%**; without the conv every mixer, softmax included, stalls near 10% |
| [**flash-attention-wmma**](https://github.com/kishorhange111/flash-attention-wmma) | FlashAttention-2 forward in **CUDA C++ on Turing tensor cores (WMMA)** — 128 `HMMA` in the SASS; padding shared-memory rows to break 16-way bank conflicts is worth **4.0–4.3× (1.6 → 6.7 TFLOP/s)** with identical instruction counts, 5× the best Triton tile on the same T4 |
| [**preference-optimization-from-scratch**](https://github.com/kishorhange111/preference-optimization-from-scratch) | **DPO, cDPO, IPO and SimPO** from their papers on the DPO paper's IMDb controlled-sentiment task (known classifier reward) — reward vs sampled KL(π‖π_ref) frontier over a 13-config β/τ sweep on a T4; finds SimPO drifts to KL≈22 and held-out preference accuracy does not track reward |
| [**multi-lora-serving**](https://github.com/kishorhange111/multi-lora-serving) | **Punica/S-LoRA-style multi-adapter serving** — a different LoRA per request in one batch: per-adapter loop, gather-BGMV, segment-SGMV and a hand-written **Triton BGMV** shrink/expand pair, wired into GPT-2; a mixed batch provably equals each request with its adapter merged; on a T4 the Triton kernel stays at 0.10–0.13 ms from 1 to 64 adapters, and serving 32 adapters in one batch is **15.7× faster** than merging per adapter |
| [**fused-linear-cross-entropy**](https://github.com/kishorhange111/fused-linear-cross-entropy) | Liger-style **chunked fused LM head + cross-entropy** with a closed-form backward (ignore_index, label smoothing, z-loss, tied embeddings) — the (tokens × 152k-vocab) logits tensor is never materialised; gradcheck-verified; on a T4 extra memory stays at 1.16 GiB up to 16k tokens (the naive loss OOMs) and the max Qwen2.5-0.5B batch doubles |
| [**constrained-decoding-from-scratch**](https://github.com/kishorhange111/constrained-decoding-from-scratch) | Outlines/XGrammar internals by hand — **byte-level regex → Thompson NFA → pruned minimal DFA**, JSON Schema → regex (exact UTF-8), a vectorized **token index** over Qwen's 151k vocab (~1 s per schema), masked decoding that always yields valid JSON; measures the state blowup of `maxLength` and shows compact-only grammars degrade content, fixed with a whitespace-tolerant grammar |
| [**bpe-tokenizer-from-scratch**](https://github.com/kishorhange111/bpe-tokenizer-from-scratch) | **Byte-level BPE** (GPT-2/cl100k pre-tokenization) — an incremental **lazy-heap trainer** proven merge-for-merge identical to the naive one, an **O(n log n) linked-list + heap encoder**, and GPT-2's merge table recovered from tiktoken's ranks with **byte-for-byte identical encodings** |

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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/stack-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./assets/stack-light.svg?v=1">
  <img alt="Core Engineering Stack — 4-Layer Architecture Blueprint covering Agents/RAG/Evals, Models/Training/Inference, Serving/Infra/Observability, and Languages/Data/Cloud." src="./assets/stack-light.svg?v=1" width="100%">
</picture>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg?v=5">
  <source media="(prefers-color-scheme: light)" srcset="./assets/footer-light.svg?v=5">
  <img alt="B.Tech CSE · DKTE Ichalkaranji (2019–2023) · CGPA 8.31 · Bengaluru, India" src="./assets/footer-light.svg?v=5" width="100%">
</picture>
