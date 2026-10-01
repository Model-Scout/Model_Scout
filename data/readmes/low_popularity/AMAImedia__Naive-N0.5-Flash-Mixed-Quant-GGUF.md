---
license: mit
base_model:
- NaiveAI/Naive-N0.5-Flash
- Baekpica/Naive-N0.5-Flash-Mixed-Quant-GGUF
pipeline_tag: text-generation
library_name: gguf
tags:
- gguf
- mixed-quant
- imatrix
- moe
- long-context
- ds4
- dgx-spark
language:
- en
- ru
- kk
- zh
- ja
- vi
- af
- am
- ar
- as
- ast
- az
- be
- bg
- bn
- bs
- ca
- ceb
- ckb
- cs
- cy
- da
- de
- el
- es
- et
- eu
- fa
- ff
- fi
- fil
- fr
- ga
- gl
- gn
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- is
- it
- jv
- ka
- kam
- kea
- km
- kmr
- kn
- ko
- ky
- lb
- lg
- ln
- lo
- lt
- luo
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- mvy
- my
- ne
- nl
- "no"
- nso
- ny
- oc
- om
- "or"
- pa
- pl
- ps
- pt
- qxp
- ro
- rw
- sd
- sk
- skr
- sl
- sn
- so
- sr
- sv
- sw
- ta
- te
- tg
- th
- ti
- tk
- tr
- ug
- uk
- umb
- ur
- uz
- wo
- xh
- yo
- yue
- zu
---

<!-- apex-banner -->
<div style="background-color: #f59e0b; color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<h2 style="color: white; margin: 0 0 10px 0;">⚡ Each donation funds the next large quant.</h2>
<p style="font-size: 16px; margin: 0 0 15px 0;">I host free GGUF or MoE quants as independent research.<br>
Local hardware: <b>Mechrevo Kuangshi GM7AG0M</b> — RTX 3060 Laptop 6GB GDDR6, 64GB DDR5, i7-12700H (14C/20T, 4.7GHz), Windows 11, Samsung 990 Pro.<br>
Good for imatrix and 0.6–35B-class work in RAM. <b>9B+ and searches need rented H200/Blackwell</b>, typically $100 per quant.</p>
<p style="font-size: 20px; margin: 0;">
<a href="https://boosty.to/amaimediacom" style="color: white; text-decoration: underline;">🎉 Boosty🦄</a>  | 
<a href="https://donatex.gg/widgets/donation-goal/89bc59e8-b69c-467a-9aa0-5e1c3f8842d6" style="color: white; text-decoration: underline;">☕ Buy Me a Coffee🦄</a>  | 
<a href="https://www.donationalerts.com/r/djbionicl" style="color: white; text-decoration: underline;">⭐ DonationAlerts🦄</a>
</p>
<p style="font-size: 14px; margin: 10px 0 0 0; opacity: 0.9;">💚 Thanks to Hugging Face for extra storage.🦄</p>
</div>

---

## NOESIS / AMAImedia

Released as part of the NOESIS Professional Multilingual Dubbing Automation Platform 
(framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators)

- **Founder:** Ilia Bolotnikov
- **Organization:** AMAImedia.com
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@djbionicl](https://t.me/djbionicl)
- **Release date:** 2026-09-27

## AMAImedia

- **Original repository:** [NaiveAI/Naive-N0.5-Flash](https://huggingface.co/NaiveAI/Naive-N0.5-Flash)

- **GGUF:** [Mixed-Quant-GGUF](https://huggingface.co/Baekpica/Naive-N0.5-Flash-Mixed-Quant-GGUF/tree/main)

---

<div align="center">
  <img class="dark:hidden" src="assets/naive-n0.5-flash-logo.svg" width="440" alt="Naive-N0.5-Flash">
  <img class="hidden dark:block" src="assets/naive-n0.5-flash-logo-dark.svg" width="440" alt="Naive-N0.5-Flash">
</div>

<p align="center"><strong>Building Frontier AI with AI</strong></p>

<div align="center">

[🏠 Homepage][website] · [📰 Technical Blog][blog] · [💻 GitHub][github]

</div>

> Upstream model description, architecture and benchmark results reproduced from
> [NaiveAI/Naive-N0.5-Flash-FP8-Draft](https://huggingface.co/NaiveAI/Naive-N0.5-Flash-FP8-Draft)
> and [NaiveAI/Naive-N0.5-Flash](https://huggingface.co/NaiveAI/Naive-N0.5-Flash).
> Everything below this note describes the **upstream BF16/FP8 checkpoint**, not this
> mixed-quant GGUF. For the quant recipe, tensor audit and memory budget of *this*
> repository, see the sections further down.

## Introduction

Naive-N0.5-Flash is an open-weight **309B MoE model with 15.5B active parameters**, built for **coding and AI R&D**. It supports a **native 1M-token context window** through a hybrid of Sliding-Window Attention (SWA) and lightweight DeepSeek Sparse Attention (DSA), with no full-attention layers.

### Key Features

- **Native 1M context, without full attention.** Naive-N0.5-Flash combines Sliding-Window Attention (SWA) and lightweight DeepSeek Sparse Attention (DSA) with GQA4 at a predominantly 5:1 SWA–DSA layout. The entire network remains local or sparse, with no full-attention layers.
- **AI-optimized inference up to 2,000 tokens/s.** NaiveRT, our inference system for Naive-N0.5-Flash, was built and optimized through AI-centered R&D. It combines mega-kernel fusion, Programmatic Dependent Launch (PDL), and speculative decoding, delivering 50 tokens/s per user in Standard mode and up to 2,000 tokens/s in Ultrafast mode. See the NaiveRT case study in the [technical blog][blog] for the implementation and optimization process.
- **Open weights and API.** Model weights and inference code are released under the MIT license. API access will also be provided, with pricing set at $0.10 / $0.40 / $0.01 per million tokens for input, output, and cache reads, respectively.

## Model Architecture

| Property | Specification |
| --- | --- |
| Architecture | Mixture-of-Experts (MoE) |
| Total parameters | 309B |
| Active parameters | 15.5B |
| Context length | Native 1M tokens |
| Transformer layers | 48 |
| Attention-layer composition | 39 SWA layers + 9 DSA layers |
| Attention mechanism | Hybrid SWA–DSA |
| SWA window | 128 tokens |
| DSA token selection | Top 2,048 tokens for backbone attention |
| DSA KV groups | 4 (GQA4) |
| Indexer query heads | 16 |
### Hybrid SWA–DSA Attention

Naive-N0.5-Flash builds on the open-weight MiMo-V2.5 base model, which has a simple architecture with strong foundational capabilities in world knowledge and deep research. Most layers use Sliding-Window Attention (SWA), whose per-token decoding cost does not grow with context length, while a small number of global-attention layers preserve long-range information. At million-token context lengths, however, these global-attention layers account for much of the decoding overhead.

Naive-N0.5-Flash replaces the global-attention layers with DeepSeek Sparse Attention (DSA). A lightweight indexer scores the full history, while the backbone computes attention only over a selected subset of tokens. Although the indexer still scans the full history and the full KV cache is retained, sparse attention substantially reduces attention computation and memory access. Adapting the model to this new attention structure was one objective of continued pretraining.

![Hybrid SWA–DSA architecture showing the network stack and the DSA attention module, including the 16-head indexer and top-2,048 token selection.][architecture-figure]

<p align="center"><em>Figure 1. The hybrid attention stack and DSA module.</em></p>

The network consists of **eight six-layer modules**. A standard module contains five SWA layers followed by one DSA layer, with the first layer of the first module also replaced by DSA. SWA uses a **128-token window**, while DSA selects the **top 2,048 tokens** for backbone attention. Both attention types incorporate sink bias.

Unlike the original MLA-based DSA implementation, Naive-N0.5-Flash replaces MLA with grouped-query attention (GQA) using **four KV groups**. For the architecture design process and indexer efficiency comparison, see model architecture in the [technical blog][blog].
### Training Overview

Following the architectural changes, Naive-N0.5-Flash completed 3.25T tokens of multi-stage training with a native 1M-token context window: 50B tokens of Indexer Warmup, 3T tokens of Sparse Attention Training, and 200B tokens of Learning Rate Decay. This process adapted the model to its new sparse attention architecture while substantially improving its AI R&D and coding capabilities. See the [technical blog][blog] for training details.
## Evaluation Results

[![Coding benchmarks comparing Naive-N0.5-Flash with other models across seven software engineering and agentic tasks.][coding-figure]][coding-pdf]

<p align="center"><em>Figure 2. Coding and agentic task results. Naive-N0.5-Flash is highlighted in yellow.</em></p>

[![AI R&D benchmarks covering PostTrainBench, MLE-bench-30, PaperBench, SOL-ExecBench, NanoChat AutoResearch, and NanoGPT SpeedRun.][ai-rd-figure]][ai-rd-pdf]

<p align="center"><em>Figure 3. AI research and systems optimization results. Metric directions are indicated in the figure.</em></p>
<a id="evaluation-notes"></a>

<details>
<summary>Evaluation setup and metric notes</summary>

**Evaluation setup.** Unless otherwise noted, our evaluations of Naive-N0.5-Flash use Claude Code 2.1.207 with a 1M-token context window, temperature 1.0, and top-p 0.95. The harness exposes only basic file I/O and Bash tools.

**Sources for reported benchmark scores are as follows:**

- **GLM-5.3 and GLM-5.3-Flash:** [GLM-5.3 blog](https://z.ai/blog/glm-5.3) and [GLM-5.3-Flash blog](https://z.ai/blog/glm-5.3-flash), respectively.
- **Kimi-K3:** [Kimi-K3 model page](https://huggingface.co/moonshotai/Kimi-K3).
- **Qwen-3.8-Max:** [Qwen-3.8-Max blog](https://qwen.ai/blog?id=qwen3.8).
- **Hy4-preview:** [Hy4-preview model page](https://huggingface.co/tencent/Hy4-preview).
- **DeepSeek-V4.1-Flash:** [DeepSeek-V4.1-Flash model page](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).
- **Step-5-preview:** [Step-5-Preview-BF16 model page](https://huggingface.co/TypeSafeAI/Step-5-Preview-BF16).
- **Fable-5 (w/ fallback):** [GLM-5.3 blog](https://z.ai/blog/glm-5.3).
- **SWE-Bench Pro:** GPT-5.6-Sol, Opus-5, and Opus-5.5 scores are drawn from the [GPT-5.6 blog](https://openai.com/index/gpt-5-6/) and the [Claude Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf).
- **DeepSWE v1.1:** The Muse-Spark-1.3 score comes from its [Muse-Spark-1.3 blog](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology). GPT-5.6-Sol and Opus-5 scores come from the [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/). The Opus-5.5 score comes from the [Claude Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf).
- **Terminal-Bench 2.1:** Muse-Spark-1.3, GPT-5.6-Sol, and Opus-5 scores come from the [Muse-Spark-1.3 blog](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology). The GPT-6-Astra score comes from the [Terminal-Bench 2.1 leaderboard](https://www.tbench.ai/?version=2.1).
- **ALE-CLI:** GPT-5.6-Sol, GPT-6-Astra, Muse-Spark-1.3, Opus-5, and Opus-5.5 scores come from the [ALE-CLI leaderboard](https://agents-last-exam.org/leaderboard).
- **FrontierSWE v1:** We calculate the Dominance score using the competing systems’ results as of August 23, 2026.
- **ProgramBench:** We report the Almost@1 score. GPT-5.6-Sol and Opus-5 scores come from the [ProgramBench leaderboard](https://programbench.com/).
- **MLE-bench-30:** Gemini-3.5-Flash, Gemini-3.6-Flash, Grok-4.5, and GPT-5.6-Luna scores come from the [Gemini 3.6 Flash model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/). Following its evaluation protocol, we report the average position score of Naive-N0.5-Flash.
- **PaperBench:** MiniMax M3, Opus-4.7, GPT-5.5, and Gemini-3.1-Pro scores come from the [MiniMax M3 model page](https://huggingface.co/MiniMaxAI/MiniMax-M3).
- **SOL-ExecBench, NanoChat AutoResearch, and NanoGPT SpeedRun:** Naive-N0.5-Flash scores were obtained using our in-house AutoResearch harness. Recursive Superintelligence Inc. scores come from its [research article](https://www.recursive.com/articles/first-steps-toward-automated-ai-research). Following the SOL-ExecBench update, we use its updated score from the [leaderboard](https://research.nvidia.com/benchmarks/sol-execbench).

</details>
## Citation

If you find Naive-N0.5-Flash useful in your research or work, please cite:

```bibtex
@misc{naiveai2026naiven05flash,
  title  = {Naive-N0.5-Flash: Building Frontier AI with AI},
  author = {{NaiveAI Team}},
  year   = {2026},
  url    = {https://naive.ai/en/research/}
}
```
## Acknowledgments

Naive-N0.5-Flash builds on the work of the open-source community and gives back to it. 
We thank the Xiaomi MiMo team for making their MiMo-V2.5 base model publicly available, 
the DeepSeek team for their work on DeepSeek Sparse Attention (DSA), and 
the SGLang team and community for their open-source inference infrastructure.
## Contact

For questions, feedback, or collaboration, please contact us at contact@naive.ai or 
follow us on X at @naiveailab. You can also find our open-source projects and model 
releases on [GitHub](https://github.com/naiveai-labs) and [Hugging Face](https://huggingface.co/NaiveAI).

---

# Naive-N0.5-Flash — Mixed Quant for DGX Spark

**Status: all four main GGUF shards and the companion Q8_0 DSpark draft are
available. Independent tensor checks and the post-upload BF16/converted-weight
numerical comparison are complete; measured results are below.**

revision `0235b3b5ff27422b1f57cdc2acddfaf643e08356`.
All 49 safetensors headers contain **308,859,589,056 parameters** in 36,568
source tensors. Routed experts account for 302,795,194,368 parameters.

The target is a resident mixed GGUF around the Qwen Q5 backbone budget of
83.275 decimal GB reference budget, with memory left for native 1M context.
The selected precision-first target is 86.908 GB, 3.633 GB above that reference. All 48 layers,
47 MoE layers, 256 experts per MoE layer and top-8 routing are retained.
All original experts, layers and parameters are retained.

## Target tensor recipe

Variant: `MQ87-IQ2XXS-IQ2XS-Q6Q8-BF16`.
Layer indices below are zero-based. [Machine-readable recipe](quant-recipe.json).

| Tensor group | Target | Purpose |
|---|---|---|
| Routed expert gate, all MoE layers | IQ2_XXS, 2.0625 BPW | Preserve the selected higher gate tier |
| Routed expert up, all MoE layers | IQ2_XXS, 2.0625 BPW | Match the selected gate precision |
| Routed expert down, all MoE layers | IQ2_XS, 2.3125 BPW | Protect return to the residual stream |
| Attention Q and O | Q6_K, 6.5625 BPW | Balance shared precision and resident capacity |
| Attention K and V | Q8_0, 8.5 BPW | Protect cached attention representations |
| Token embedding, output head, L0 dense FFN | Q8_0 | Protect token ingress and logits |
| DSA indexer projection matrices | BF16 | Preserve native token-selection computation |
| Router weights/correction bias, norms, indexer LayerNorm, sinks | F32 | Preserve routing and numerical controls |

The measured **tensor payload is 86,908,487,424 bytes =
86.908487 GB = 80.939836 GiB**, or
**2.251081 effective BPW**. The four complete GGUF files total
**86,960,547,072 bytes = 86.960547 GB / 80.988321 GiB**, including metadata,
tokenizer and alignment.

The selected layout promotes every gate to IQ2_XXS. Compared with the
83.301386 GB IQ1_M-interior target, this costs **3.607101 GB / 3.359375 GiB
(4.33%)**. Up and down precision and all shared-tensor formats are unchanged.

This recipe records the precision and storage layout used in the completed
conversion. The numerical comparison below was measured after the public upload.

## Model files

Download all four main shards into the same directory.

| Main GGUF shard | Bytes | GB |
|---|---:|---:|
| [Naive-N0.5-Flash-MQ87-00001-of-00004.gguf](Naive-N0.5-Flash-MQ87-00001-of-00004.gguf) | 20,942,674,048 | 20.942674 |
| [Naive-N0.5-Flash-MQ87-00002-of-00004.gguf](Naive-N0.5-Flash-MQ87-00002-of-00004.gguf) | 21,784,615,264 | 21.784615 |
| [Naive-N0.5-Flash-MQ87-00003-of-00004.gguf](Naive-N0.5-Flash-MQ87-00003-of-00004.gguf) | 21,784,615,264 | 21.784615 |
| [Naive-N0.5-Flash-MQ87-00004-of-00004.gguf](Naive-N0.5-Flash-MQ87-00004-of-00004.gguf) | 22,448,642,496 | 22.448642 |

[File manifest](main-file-manifest.json), [SHA256 checksums](SHA256SUMS),
[conversion provenance](conversion-provenance.json).

## Native 1M context and memory budget

The source has 39 sliding-window layers with a 128-token window and 9 DSA
layers selecting up to 2,048 history positions. DSA uses four GQA KV heads,
192-dimensional keys and 128-dimensional values. The source retains full
DSA K/V history; sparse attention reduces selected computation, not that
cache allocation. See the [official architecture](https://github.com/NaiveAI-Labs/Naive-N0.5-Flash).

Analytical one-sequence budget at 1,048,576 tokens and a 2,048-token prefill chunk:

| Component | GiB |
|---|---:|
| Main weight payload | 80.940 |
| Companion draft payload | 0.646 |
| All 9 DSA K/V histories, BF16 | 22.500 |
| 39 SWA caches, window plus prefill chunk | 0.404 |
| Indexer history stored as FP32 | 4.500 |
| Alternative native FP8 codes plus original F32 row scales | 1.160 |
| Main and draft payloads plus cache, depending on indexer storage | 105.650–108.990 |

The FP8 alternative is a proposed lossless storage representation of the
source's FP8-rounded indexer activations, not extra quantization. It needs
numerical validation. Resident repacks, CUDA scratch, staging and OS/services
are additional. Available unified memory must be measured on the actual GB10.
One 1M bank is the initial memory target.

The planned runtime uses bounded query/history tiles and incremental top-k: materializing
all 16-head index scores for a full prefill chunk at 1M would exceed the budget.
No SSD weight/embedding sidecar is planned. The Qwen SSD-PLE design does not
remove Naive's attention-cache requirement.

## Calibration

Calibration ran on eight A100 SXM 80GB GPUs with the pinned original BF16
checkpoint and original F32 router. Routed-input and post-SwiGLU second moments
were collected separately for every expert, with valid lengths and no padding.

The first **2,367,654 tokens** were processed through all 48 layers. A further
**1,581,699 tokens** broadened the language/domain mix through the first nine
layers. Inputs came from
[Solar Healing Mix](https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix),
[Inkling Calibration](https://huggingface.co/datasets/Baekpica/Inkling-Small-Multimodal-Calibration),
[Nemotron Cascade tools](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-SFT-Stage-2),
and [Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia), retokenized
with the original Naive tokenizer and chat template.

**12,015 / 12,032 layer/expert pairs** were naturally routed, with
**991,466,640 recorded selections**. The remaining **17** were measured
separately using **56,639 actual BF16 source-layer input states per expert**.
Their zero natural-route counts are retained; directly measured input and
SwiGLU moments provide their quantization importance. All other experts use
routed moments. All original experts and parameters are retained.

The final **48-document / 95,244-token** comparison set was checked against all
2,498 training records for exact content and truncation-prefix overlap,
including sequences of different lengths. Raw natural and direct moments were
independently recomputed before production conversion. Source BF16 layer
checks were bit-identical to the released eager graph, including a 2,304-token
DSA probe.

The original BF16 generation checks were completed before conversion finished.
The main GGUF files were then uploaded, followed by the numerical comparison
below.

## Measured checks

[Independent tensor audit](verification/main-tensor-audit.json) verified all
36,568 source payload hashes and their mapping into 613 GGUF tensors. All 248
F32 control tensors and 27 BF16 indexer matrices preserve their source values
exactly. One deterministic row from each of the 36,293 quantized source matrices
was independently re-encoded and compared with the actual GGUF bytes.

[Post-upload numerical comparison](verification/main-quality-summary.json)
processed all 48 layers on 48 clean documents totaling 95,244 tokens. Scores use
32 sampled next-token positions per document, totaling 1,536 positions.

| Measurement | Value |
|---|---:|
| BF16 sampled-position target NLL | 3.463912 |
| Mixed GGUF sampled-position target NLL | 3.385064 |
| Mean KL, BF16 → mixed GGUF | 0.597300 |
| Top-1 prediction agreement | 73.6979% |
| Mean logit cosine similarity | 0.967016 |

All scores were recomputed from the saved full-vocabulary logits. These sampled
observations do not establish a general quality ranking. Actual GGUF weights
were decoded with canonical ggml and evaluated in the original BF16/F32 eager
graph; the measurement does not exercise native quantized serving kernels.
The 108 sampled query positions at or beyond 2,048 had 75% top-1 agreement and
mean KL 0.439294. The longest evaluated documents were 4,096 tokens.

## Runtime

Target runtime: [Baekpica/ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs).
The inspected commit is `4b1d22fc7b0d6ef5b489a6f85750d1b97191804e`.
It already has MiMo GQA/SWA and DeepSeek-family sparse-attention primitives,
but does not yet implement this Naive family. The GGUF preserves its Naive architecture identity and original indexer tensors.

The source configuration fixes 64 rotary dimensions, split-half RoPE,
different SWA/DSA theta values, value scale 0.707, sigmoid/noaux_tc routing
with correction bias, and per-row FP8 E4M3 indexer rounding. These are the source semantics used for the reference comparisons, including
the stable tie behavior of index selection.
The main checkpoint has no embedded MTP. The newly added external DSpark draft
package is described below and shares the target's embedding/output tensors.

## Companion DSpark draft

[`NaiveAI/Naive-N0.5-Flash-FP8-Draft`](https://huggingface.co/NaiveAI/Naive-N0.5-Flash-FP8-Draft),
revision `b2b8ee9f5d6b3fd1dfba113d3a363138e37c83b0`, is included in
[draft/](draft/README.md). Despite FP8 in the source name, the downloaded
checkpoint contains **652,797,441 BF16 parameters in 63 tensors**.

| Draft group | Final format |
|---|---|
| Five-layer attention/FFN and eight-tap `fc` projection matrices | Q8_0 |
| Vanilla rank-256 Markov embedding and vocabulary projection | Q8_0 |
| Norms, trained mask embedding and confidence weight/bias | F32 |

The measured draft file is **693,777,632 bytes = 0.693778 GB / 0.646131 GiB**;
the payload is **693,770,244 bytes**. The main selected payload plus draft
payload is **87,602,257,668 bytes = 87.602258 GB / 81.585960 GiB**, before
GGUF metadata and alignment. The measured main and draft files together total
**87,654,324,704 bytes = 87.654325 GB / 81.634451 GiB**.
The target's token embedding and output head are shared and not duplicated. [Complete draft precision map](draft-recipe.json).

The source uses five SWA/1024 layers, seven-position blocks (one anchor plus
six proposals), target hidden taps `[1,7,14,20,26,32,39,45]`, a learned mask
vector, Markov correction and confidence tensors. Those mechanics and the
exact target/source revisions are preserved in the draft GGUF metadata and
original configuration. Hidden-tap capture, draft caches, activation scratch,
logits and resident repacks add to the weight-storage figure.

[Independent draft tensor checks](draft/verification/tensor-audit.json)
cover all 63 tensors and all 652,797,441 elements, including exact independent
Q8_0 scale/code reconstruction and F32 controls. A
[CPU source-graph probe](draft/verification/source-graph-probe.json)
exercises the packaged source with synthetic context and real target
anchor/output tensors. Native Naive draft integration, natural acceptance,
throughput and GB10 serving are pending; existing DeepSeek DSpark and MiMo
DFlash primitives provide integration references.

Actual BF16 target-prefix comparisons cover **182 cases / 1,092 proposals**.
Source-versus-Q8 draft top-1 agreement is **96.7033%** for the base path and
**98.3516%** with identical gold previous-token Markov input.
[Detailed natural-input measurements](draft/verification/natural-graph-probe.json).
These are teacher-forced draft-fidelity measurements; native speculative
acceptance and throughput remain unmeasured.

## References and license

Recipe precedents: [DS4 Mixed Quant collection](https://huggingface.co/collections/Baekpica/ds4-mixed-quant-for-spark),
[MiMo RL](https://huggingface.co/Baekpica/MiMo-V2.6-Flash-RL-Mixed-Quant-GGUF),
[Qwen Q5](https://huggingface.co/Baekpica/Qwen3.8-Flash-Next-Mixed-Quant-SSD-PLE-GGUF)
and [Motif-3](https://huggingface.co/Baekpica/Motif-3-GGUF).
DSA implementation reference: [antirez/ds4](https://github.com/antirez/ds4).

Model weights retain the upstream MIT license. Upstream implementation files
and calibration sources retain their respective licenses; they are recorded
in the reproduction package.

[website]: https://naive.ai/
[blog]: https://naive.ai/en/research/
[github]: https://github.com/naiveai-labs/Naive-N0.5-Flash
[weights]: https://huggingface.co/NaiveAI/Naive-N0.5-Flash
[discussions]: https://huggingface.co/NaiveAI/Naive-N0.5-Flash/discussions
[base-model]: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Base

[architecture-figure]: assets/hybrid-swa-dsa-architecture.svg
[coding-figure]: assets/coding-benchmarks.png
[coding-pdf]: assets/coding-benchmarks.pdf
[ai-rd-figure]: assets/ai-rd-benchmarks.png
[ai-rd-pdf]: assets/ai-rd-benchmarks.pdf
