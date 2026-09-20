---
base_model: Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16
base_model_relation: finetune
datasets:
- Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix
language:
- en
- ko
- ja
library_name: transformers
license: other
license_name: upstage-solar-license
license_link: LICENSE
pipeline_tag: text-generation
tags:
- solar
- solar-open2
- moe
- reap
- ream
- expert-merging
- expert-pruning
- healing
- conversational
---

<!-- solar-ream-hub-card:v2 -->

# Solar-Open2-120B-A15B-REAM-148E-BF16-v2

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

> ## Built with Solar
>
> This is a **Derivative AI Model** of [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B),
> distributed under the **Upstage Solar License**. A copy of the license is
> included in this repository as `LICENSE`.
>
> 이 모델은 [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) 의
> **파생 AI 모델**이며 **Upstage Solar License** 로 배포됩니다. 라이선스 사본은
> 이 저장소의 `LICENSE` 에 포함돼 있습니다.

## English

## Built with Solar — Model Lineage

| Role | Model |
|---|---|
| Original / Hub `base_model` | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent (184E) | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM result (148E, before healing) | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16) |
| **Healing result (this repository)** | Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2 |
| Healing result, NVFP4A16 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2) |

## Overview

This is `Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16` after **supervised healing** of the damage introduced by REAM
expert merging. The healing adapters are merged into the weights, so the
checkpoint layout and the serving procedure are **identical to v1** — no PEFT
adapter has to be attached at runtime.

The architecture is unchanged from v1.

| Item | Value |
|---|---:|
| Total parameters | 120,398,326,528 (120.398B) |
| Active parameters per token | 14,701,865,728 (14.702B) |
| Transformer layers | 48 |
| Routed experts | 148 per layer |
| Shared experts | 1 per layer |
| Active experts | top-8 routed + 1 shared |
| Hidden size | 4,096 |
| Routed expert intermediate size | 1,280 |
| Weight storage | BF16; router correction bias remains FP32 |
| Raw tensor payload | 240,796,681,472 bytes (240.797 GB) |
| Checkpoint shards | 49, unpacked per-expert tensors (same as v1) |

## Why Healing Was Needed

REAM absorbs 36 routed experts per layer into salient centroid experts,
reducing the 184-expert REAP parent to 148 experts. The damage concentrates in
two places:

1. **The router.** The router weight and the FP32 correction bias are sliced to
   the sorted centroid order, which distorts the competition between experts.
2. **The merged expert weights.** Neuron alignment and saliency-weighted
   merging leave an approximation error in every surviving expert.

Attention is untouched by REAM.

On a fixed prompt set served through the same vLLM engine, v1 showed
**repetition collapse on 5 of 16 prompts**, and — more seriously — it failed to
close `<|think:end|>` on **all 16**, so every generation ran to the token limit
without ever producing a final answer. Every collapse was on a **Korean**
prompt; none of the English prompts collapsed.

## Healing Method

Solar Open 2 stores routed experts as packed 3D `nn.Parameter` tensors
(`gate_up_proj [148, 2560, 4096]`, `down_proj [148, 4096, 1280]`), not as
`nn.Linear` modules. Standard PEFT cannot target them. This release uses a
**batched LoRA that keeps the expert axis**, applied inside the per-expert GEMM.
Merging is exact and per-expert: `W += (alpha/r) · B @ A`. The output difference
between the adapted and the merged model was measured at **2.05e-8**.

| Target | Method | Parameters |
|---|---|---:|
| `mlp.experts.gate_up_proj`, `down_proj` | batched 3D LoRA, r=16, alpha=32 | 1,367.6M |
| `mlp.gate.weight`, `mlp.gate.e_score_correction_bias` | full fine-tuning | 29.1M |
| `mlp.shared_experts.{gate,up,down}_proj` | full fine-tuning | 755.0M |
| All RMSNorm weights | full fine-tuning | 0.4M |
| | **Total trainable** | **2.152B (1.79%)** |

`e_score_correction_bias` is declared as a `register_buffer` with
`dtype=torch.float32`. Loading with `dtype=bfloat16` casts it and it never
appears in `named_parameters()`. It was restored to the original FP32 values and
promoted to `nn.Parameter` before training, because it is added to the sigmoid
scores and therefore controls expert **selection** directly — exactly the
quantity REAM sliced.

Model parameters stay in BF16 while the optimizer keeps FP32 master copies.
Applying Adam directly to BF16 parameters loses updates whose magnitude falls
below BF16 relative precision.

### Training Setup

| Item | Value |
|---|---|
| Data | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix](https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix) |
| Stage A | 4,096-token mix · 395 steps · 25.8M tokens · LoRA LR 1e-4 · cosine, warmup 20 |
| Stage B | long context 4,097–16,384 · 100 steps · 3.7M tokens · LoRA LR 3e-5, resumed from Stage A |
| Total | 495 steps · 29.5M tokens (assistant 22.0M) · 10.19h |
| Loss | assistant tokens only (`-100` masking), including the think block, tool calls and `<\|im:end\|>` |
| LR ratio | LoRA : router : shared : norm = 10 : 1 : 1 : 1 |
| Optimizer | AdamW (0.9, 0.95), weight decay 0, grad clip 1.0, FP32 master weights |
| Parallelism | 4-GPU pipeline model parallel per rank × 2-rank data parallel |
| Hardware | 8 × NVIDIA RTX PRO 6000 Blackwell 96GB (no NVLink) |

Without NVLink, the per-layer all-gather that FSDP/ZeRO-3 requires (4.7GB per
MoE layer) costs seconds per step. Weights were pinned to their GPUs and only
the gradients of the trainable 1.8% were synchronised.

## Data

All supervised fine-tuning. RL and GenRM style corpora were deliberately
excluded: they belong after SFT in the pipeline and risk changing style without
restoring the capability lost to merging.

| Bucket | Source | Tokens | Share |
|---|---|---:|---:|
| `if_chat` | Nemotron-SFT-Instruction-Following-Chat-v2 | 15.40M | 22.0% |
| `cascade1_reasoning` | Nemotron-Cascade-SFT-Stage-1 | 11.20M | 16.0% |
| `cascade2_reasoning` | Nemotron-Cascade-SFT-Stage-2 | 11.20M | 16.0% |
| `ko` | Nemotron-SFT-Multilingual-v2 (Korean) | 11.20M | 16.0% |
| `multilingual_other` | Nemotron-SFT-Multilingual-v2 (ja/pt/hi) | 8.40M | 12.0% |
| `finance` | Nemotron-SpecializedDomains-Finance-v1 | 4.20M | 6.0% |
| `swe_agentic` | Nemotron-SFT-SWE-v2 | 4.20M | 6.0% |
| `code_algo` | Nemotron-SFT-Competitive-Programming-v2 | 4.20M | 6.0% |

Korean comes entirely from `nvidia/Nemotron-SFT-Multilingual-v2`;
`Multilingual-v1` contains no Korean.

## Evaluation

This is not a benchmark run. It is a qualitative comparison over **16 prompts
frozen before training started** — 10 Korean, 6 English, covering factual recall,
proofreading, arithmetic, concept explanation, business writing, code, summary,
logical reasoning, long-form writing and structured output, with response
budgets from 160 to 640 tokens.

All three models were served by the **same engine** — vLLM
`v0.22.0-solar-open2`, tensor parallel 4 — with identical sampling
(`temperature=0`, `top_p=1.0`, `repetition_penalty=1.0`, `seed=42`, per-prompt
fixed `max_tokens`).

| Metric | v1 (before healing) | v2 BF16 | v2 NVFP4A16 |
|---|---:|---:|---:|
| distinct-1 &uarr; | 0.3225 | **0.4633** | 0.4357 |
| distinct-3 &uarr; | 0.5954 | **0.827** | 0.8183 |
| top 3-gram ratio &darr; | 0.2612 | **0.018** | 0.0164 |
| distinct word ratio &uarr; | 0.4441 | **0.621** | 0.5956 |
| Repetition collapse / 16 | 5 | **0** | **0** |
| Closed `<\|think:end\|>` / 16 | 0 | **8** | 9 |
| Stopped on its own / 16 | 0 | **4** | 4 |

"Closed `<|think:end|>`" counts generations that finished the reasoning block
and began emitting the response. v1 closed it on **0 of 16** — every generation
exhausted its token budget still inside the think block. v2 closes it on
**8 of 16** and terminates on its own on 4.
The remainder are prompts where the reasoning legitimately exceeded the fixed
token budget (160–640), not collapses.

### Concrete examples

**Korean proofreading (`ko_edit_01`)** — v1 collapsed with a top 3-gram ratio of
0.919 and never reached the answer; v2 identifies both errors.

```
v1: Thinking Process: The user wants me to correct the spelling and spacing in a
    given Korean Korean Korean Korean Korean Korean Korean Korean Korean Korean
    Korean Korean Korean Korean Korean Korean Korean Korean ...        (200 tok, no answer)

v2: ... "보내드리겠읍니다" should be "보내드리겠습니다". Also "말슴해" should be
    "말씀해". ...
```

**Korean concept explanation (`ko_explain_01`)** — top 3-gram ratio 0.830 → 0.009.

```
v1: - **Language:** Korean (Korean Korean Korean Korean ...          (448 tok, no answer)

v2: ### Part 1: Role of the Router in Mixture-of-Experts (MoE)
    In a Mixture-of-Experts model, the architecture consists of: ...
```

**English instruction following (`en_format_01`)** — "exactly 5 tips, one
sentence each, starting with a verb, no preamble".

```
v1: 384 tokens of planning, hit the token limit, never emitted the list.

v2: 103 tokens, stopped on its own:
    1. Optimize model selection by choosing smaller, efficient architectures ...
    2. Implement caching to reuse responses for identical or similar queries ...
```

The full 16-prompt, three-way transcript is in `healing_comparison.md`.

## Usage

Identical to v1. The Upstage Transformers Solar Open 2 branch is required.

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

For serving, use a Solar Open 2-compatible runtime. This release was verified
with the Upstage vLLM Solar branch `v0.22.0-solar-open2` at tensor parallel 4.
Solar reasoning and tool calls require the Solar Open 2 reasoning and tool-call
parsers. **No PEFT adapter is needed** — the checkpoint is 49 unpacked
per-expert BF16 shards with the same file list as v1.

## Limitations

- No downstream benchmark was run. Neither the original model's scores nor the
  REAP parent's behaviour should be attributed to this derivative.
- The healing budget is 22M assistant tokens.
  Clear failure modes such as repetition collapse improve substantially, but the
  specialist knowledge lost to merging is not fully restored.
- Training sequences were capped at 4,096 (Stage A) and 16,384 (Stage B). The
  configured context length of 1,048,576 is inherited, not revalidated.
- `Nemotron-SFT-SWE-v2/swe.jsonl` has a median of 44,710 tokens and its
  system+tools block alone exceeds 8,192, so no sample fit the budget even after
  turn-level truncation. That bucket was filled from `agentless.jsonl` only, and
  long agentic trajectories were not trained.
- Evaluate safety, accuracy, memory, latency, throughput, runtime compatibility
  and licensing for the intended deployment.

## Citation

```bibtex
@article{jha2026ream,
  title={REAM: Merging Improves Pruning of Experts in LLMs},
  author={Jha, Saurav and Hashemzadeh, Maryam and Pasand, Ali Saheb and Parviz, Ali and Lee, Min-Joong and Knyazev, Boris},
  journal={arXiv preprint arXiv:2604.04356},
  year={2026}
}
```

```bibtex
@misc{solar-open-2-2026,
  title={Solar Open 2 Technical Report},
  author={Upstage AI},
  year={2026},
  url={https://huggingface.co/upstage/Solar-Open2-250B}
}
```

## License

This derivative is distributed under the **Upstage Solar License**. The
repository includes an exact copy of the source model's `LICENSE`.
Redistribution and use must satisfy that license, including its Solar naming
and attribution requirements.

---

## 한국어

## Built with Solar — 모델 계보

| 역할 | 모델 |
|---|---|
| 원본 / Hub `base_model` | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent (184E) | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM 결과 (148E, 힐링 전) | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16) |
| **힐링 결과 (이 저장소)** | Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2 |
| 힐링 결과 NVFP4A16 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2) |

## 모델 개요

`Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16` 의 REAM expert 병합 손상을 **지도학습으로 복구**한 체크포인트입니다.
힐링 어댑터는 가중치에 흡수돼 있어 체크포인트 구성과 서빙 절차가 **v1과
동일**합니다. 런타임에 PEFT 어댑터를 붙일 필요가 없습니다.

구조는 v1과 같습니다.

| 항목 | 값 |
|---|---:|
| 전체 파라미터 | 120,398,326,528 (120.398B) |
| 토큰당 활성 파라미터 | 14,701,865,728 (14.702B) |
| Transformer 레이어 | 48 |
| Routed expert | 레이어당 148 |
| Shared expert | 레이어당 1 |
| 활성 expert | routed top-8 + shared 1 |
| Hidden size | 4,096 |
| Routed expert intermediate size | 1,280 |
| 가중치 저장 | BF16, router correction bias는 FP32 유지 |
| Raw tensor payload | 240,796,681,472 bytes (240.797 GB) |
| 체크포인트 샤드 | 49개, unpacked per-expert 텐서 (v1과 동일) |

## 왜 힐링이 필요했나

REAM은 184E REAP parent에서 레이어마다 routed expert 36개를 saliency가 높은
centroid에 흡수시켜 148E로 줄입니다. 손상은 두 곳에 집중됩니다.

1. **라우터** — router weight와 FP32 correction bias를 정렬된 centroid 순서로
   slice하면서 expert 간 경쟁 분포가 왜곡됩니다.
2. **병합된 expert 가중치** — neuron 정렬과 saliency 가중 병합 과정의 근사
   오차가 살아남은 모든 expert에 남습니다.

Attention은 REAM이 건드리지 않습니다.

동일한 vLLM 엔진으로 고정 프롬프트를 돌린 결과 v1은 **16개 중 5개에서 반복
붕괴**했고, 더 심각하게는 **16개 전부에서 `<|think:end|>` 를 닫지 못해** 최종
답변에 도달하지 못한 채 토큰 한도까지 생성했습니다. 붕괴한 5개는 **전부
한국어** 프롬프트였고 영어는 한 건도 붕괴하지 않았습니다.

## 힐링 방법

Solar Open 2는 routed expert를 `nn.Linear` 가 아니라 packed 3D `nn.Parameter`
(`gate_up_proj [148, 2560, 4096]`, `down_proj [148, 4096, 1280]`)로 저장합니다.
표준 PEFT로는 타겟할 수 없어 **expert 축을 유지하는 배치 LoRA**를 expert별 GEMM
안에 직접 넣었습니다. 머지는 expert 단위로 `W += (alpha/r) · B @ A` 로 자명하며,
어댑터 적용 상태와 머지 후의 출력 차이는 **2.05e-8** 로 측정했습니다.

| 대상 | 방식 | 파라미터 |
|---|---|---:|
| `mlp.experts.gate_up_proj`, `down_proj` | 배치 3D LoRA, r=16, alpha=32 | 1,367.6M |
| `mlp.gate.weight`, `mlp.gate.e_score_correction_bias` | full fine-tuning | 29.1M |
| `mlp.shared_experts.{gate,up,down}_proj` | full fine-tuning | 755.0M |
| 전체 RMSNorm | full fine-tuning | 0.4M |
| | **학습 대상 합계** | **2.152B (1.79%)** |

`e_score_correction_bias` 는 `dtype=torch.float32` 인 `register_buffer` 로
선언돼 있습니다. `dtype=bfloat16` 으로 로드하면 캐스트되고 buffer라
`named_parameters()` 에도 잡히지 않습니다. 이 값은 sigmoid 점수에 더해져 expert
**선택**을 직접 좌우하는, 정확히 REAM이 slice한 대상이므로 학습 전에 원본 FP32
값으로 복원하고 `nn.Parameter` 로 승격했습니다.

모델 파라미터는 BF16으로 두고 옵티마이저가 FP32 master 사본을 유지합니다.
BF16 파라미터에 Adam을 직접 걸면 BF16 상대 정밀도보다 작은 업데이트가
유실됩니다.

### 학습 설정

| 항목 | 값 |
|---|---|
| 데이터 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix](https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix) |
| 단계 A | 4,096 토큰 믹스 · 395스텝 · 25.8M 토큰 · LoRA LR 1e-4 · cosine, warmup 20 |
| 단계 B | 장문맥 4,097–16,384 · 100스텝 · 3.7M 토큰 · LoRA LR 3e-5, 단계 A에서 이어학습 |
| 합계 | 495스텝 · 29.5M 토큰 (assistant 22.0M) · 10.19h |
| Loss | assistant 토큰만 (`-100` 마스킹), think 블록·tool call·`<\|im:end\|>` 포함 |
| LR 비율 | LoRA : router : shared : norm = 10 : 1 : 1 : 1 |
| 옵티마이저 | AdamW (0.9, 0.95), weight decay 0, grad clip 1.0, FP32 master |
| 병렬화 | 랭크당 4 GPU 파이프라인 모델 병렬 × 2랭크 데이터 병렬 |
| 하드웨어 | NVIDIA RTX PRO 6000 Blackwell 96GB × 8 (NVLink 없음) |

NVLink가 없으면 FSDP/ZeRO-3의 레이어별 all-gather(MoE 레이어당 4.7GB)가 스텝당
수 초를 소모합니다. 가중치를 GPU에 고정하고 학습 대상 1.8%의 그래디언트만
동기화했습니다.

## 데이터

전량 지도학습 데이터입니다. RL·GenRM 계열은 의도적으로 제외했습니다 — 파이프라인
상 SFT 이후 단계이고, style만 바꾸면서 병합으로 잃은 capability는 복구하지 못할
위험이 있습니다.

| 버킷 | 소스 | 토큰 | 비중 |
|---|---|---:|---:|
| `if_chat` | Nemotron-SFT-Instruction-Following-Chat-v2 | 15.40M | 22.0% |
| `cascade1_reasoning` | Nemotron-Cascade-SFT-Stage-1 | 11.20M | 16.0% |
| `cascade2_reasoning` | Nemotron-Cascade-SFT-Stage-2 | 11.20M | 16.0% |
| `ko` | Nemotron-SFT-Multilingual-v2 (Korean) | 11.20M | 16.0% |
| `multilingual_other` | Nemotron-SFT-Multilingual-v2 (ja/pt/hi) | 8.40M | 12.0% |
| `finance` | Nemotron-SpecializedDomains-Finance-v1 | 4.20M | 6.0% |
| `swe_agentic` | Nemotron-SFT-SWE-v2 | 4.20M | 6.0% |
| `code_algo` | Nemotron-SFT-Competitive-Programming-v2 | 4.20M | 6.0% |

한국어는 전량 `nvidia/Nemotron-SFT-Multilingual-v2` 에서 가져왔습니다.
`Multilingual-v1` 에는 한국어가 없습니다.

## 평가

벤치마크가 아니라 **학습 시작 전에 동결한 16개 프롬프트**의 정성 비교입니다.
한국어 10개, 영어 6개이며 상식·교정·산술·개념 설명·비즈니스 작문·코드·요약·
논리 추론·장문 작성·구조화 출력을 다루고 응답 예산은 160~640 토큰입니다.

세 모델 모두 **동일한 엔진**(vLLM `v0.22.0-solar-open2`, tensor parallel 4)과
동일한 샘플링(`temperature=0`, `top_p=1.0`, `repetition_penalty=1.0`,
`seed=42`, 프롬프트별 고정 `max_tokens`)으로 측정했습니다.

| 지표 | v1 (힐링 전) | v2 BF16 | v2 NVFP4A16 |
|---|---:|---:|---:|
| distinct-1 &uarr; | 0.3225 | **0.4633** | 0.4357 |
| distinct-3 &uarr; | 0.5954 | **0.827** | 0.8183 |
| top 3-gram ratio &darr; | 0.2612 | **0.018** | 0.0164 |
| distinct word ratio &uarr; | 0.4441 | **0.621** | 0.5956 |
| Repetition collapse / 16 | 5 | **0** | **0** |
| Closed `<\|think:end\|>` / 16 | 0 | **8** | 9 |
| Stopped on its own / 16 | 0 | **4** | 4 |

"`<|think:end|>` 닫음"은 추론 블록을 끝내고 응답 본문을 내기 시작한 생성의
수입니다. v1은 **16개 중 0개** — 전부 think 블록 안에서 토큰 예산을 소진했습니다.
v2는 **8개**에서 닫고 4개는 스스로 종료합니다.
나머지는 붕괴가 아니라 고정 토큰 예산(160~640) 안에 추론이 안 끝난 경우입니다.

### 실제 사례

**한국어 맞춤법 교정 (`ko_edit_01`)** — v1은 최빈 3-gram 비율 0.919로 붕괴해
답변에 도달하지 못했고, v2는 두 오류를 모두 잡아냅니다.

```
v1: Thinking Process: The user wants me to correct the spelling and spacing in a
    given Korean Korean Korean Korean Korean Korean Korean Korean Korean Korean
    Korean Korean Korean Korean Korean Korean Korean Korean ...        (200토큰, 답변 없음)

v2: ... "보내드리겠읍니다" should be "보내드리겠습니다". Also "말슴해" should be
    "말씀해". ...
```

**한국어 개념 설명 (`ko_explain_01`)** — 최빈 3-gram 비율 0.830 → 0.009.

```
v1: - **Language:** Korean (Korean Korean Korean Korean ...          (448토큰, 답변 없음)

v2: ### Part 1: Role of the Router in Mixture-of-Experts (MoE)
    In a Mixture-of-Experts model, the architecture consists of: ...
```

**영어 지시 준수 (`en_format_01`)** — "정확히 5개, 각 한 문장, 동사로 시작,
서론·결론 없이".

```
v1: 384토큰을 계획 수립에 쓰고 토큰 한도에 도달, 목록을 내지 못함.

v2: 103토큰, 스스로 종료:
    1. Optimize model selection by choosing smaller, efficient architectures ...
    2. Implement caching to reuse responses for identical or similar queries ...
```

16개 프롬프트 3-way 생성 결과 전문은 `healing_comparison.md` 에 있습니다.

## 사용

v1과 동일합니다. Upstage Transformers Solar Open 2 브랜치가 필요합니다.

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

서빙은 Solar Open 2 호환 런타임을 사용하십시오. 이 릴리스는 Upstage vLLM Solar
브랜치 `v0.22.0-solar-open2`, tensor parallel 4에서 검증했습니다. Solar의 추론과
tool call에는 Solar Open 2 reasoning·tool-call 파서가 필요합니다. **PEFT 어댑터는
필요 없습니다** — 체크포인트는 v1과 같은 파일 목록의 unpacked per-expert BF16
49샤드입니다.

## 한계

- 다운스트림 벤치마크를 돌리지 않았습니다. 원본이나 REAP parent의 점수를 이 파생
  모델에 귀속시키면 안 됩니다.
- 힐링 예산은 assistant 토큰 기준 22M 수준입니다.
  반복 붕괴 같은 명확한 열화는 크게 개선되지만 병합으로 잃은 전문 지식이 전부
  복원되지는 않습니다.
- 학습 시퀀스 상한은 단계 A 4,096, 단계 B 16,384입니다. 설정된 컨텍스트 길이
  1,048,576은 상속된 값이며 재검증되지 않았습니다.
- `Nemotron-SFT-SWE-v2/swe.jsonl` 은 median 44,710 토큰이고 system+tools 블록만
  으로도 8,192를 넘겨 turn 단위 절단으로도 예산에 맞출 수 없었습니다. 해당 버킷은
  `agentless.jsonl` 로만 채웠고 장문 에이전틱 궤적은 학습되지 않았습니다.
- 배포 목적에 맞게 안전성·정확도·메모리·지연·처리량·런타임 호환성·라이선스를
  직접 평가해야 합니다.

## 인용

```bibtex
@article{jha2026ream,
  title={REAM: Merging Improves Pruning of Experts in LLMs},
  author={Jha, Saurav and Hashemzadeh, Maryam and Pasand, Ali Saheb and Parviz, Ali and Lee, Min-Joong and Knyazev, Boris},
  journal={arXiv preprint arXiv:2604.04356},
  year={2026}
}
```

```bibtex
@misc{solar-open-2-2026,
  title={Solar Open 2 Technical Report},
  author={Upstage AI},
  year={2026},
  url={https://huggingface.co/upstage/Solar-Open2-250B}
}
```

## 라이선스

이 파생 모델은 **Upstage Solar License** 로 배포됩니다. 저장소에 원본 모델의
`LICENSE` 사본이 포함돼 있습니다. 재배포와 사용은 Solar 명명·귀속 요구를 포함한
해당 라이선스를 따라야 합니다.
