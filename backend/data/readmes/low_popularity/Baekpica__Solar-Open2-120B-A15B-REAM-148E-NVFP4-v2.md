---
base_model: Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2
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
- compressed-tensors
- nvfp4
- w4a16
- quantized
- conversational
---

<!-- solar-ream-hub-card:v2 -->

# Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2

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
| Healing result, BF16 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2) |
| **This repository** | Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2 |
| Same quantization applied to v1 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4) |

## Overview

Weight-only **NVFP4A16 (W4A16)** compressed-tensors quantization of
[Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2). Only the routed expert projections are
quantized; every path that all tokens traverse stays in BF16.

| Item | Value |
|---|---|
| Scheme | `NVFP4A16` (compressed-tensors `nvfp4-pack-quantized`) |
| Weights | NVIDIA FP4 E2M1, group size 16 |
| Group scales | `float8_e4m3fn`, plus a per-tensor FP32 global scale |
| Activations | **not quantized (16-bit)** |
| Algorithm | llm-compressor `model_free_ptq` — data-free RTN, no calibration set |
| Quantized modules | 21,312 routed expert projections (48 × 148 × 3) |
| gate/up shared global-scale pairs | 7,104 |
| PTQ wall clock | 82s on 6 GPUs |
| Payload | 80,175,895,040 bytes (80.18 GB) |
| Shards / tensor keys | 9 / 64,875 |

240.80 GB → 80.18 GB, a 3.0× reduction.

### Paths kept in BF16

```
re:^model\.layers\.\d+\.self_attn\..*$            # attention (KDA linear + full)
re:^model\.layers\.\d+\.mlp\.shared_experts\..*$   # shared expert
re:^model\.layers\.\d+\.mlp\.gate.*$              # router weight + correction bias
model.embed_tokens
lm_head
```

Because the router is not quantized, quantization cannot change routing
decisions. Because attention, the shared expert, the embedding and the LM head
are not quantized, no token passes through FP4 on its dense path — only the
8 of 148 routed experts selected per token.

### gate/up global-scale sharing

The runtime loads `gate_proj` and `up_proj` fused into a single
`gate_up_proj [148, 2560, 4096]` tensor, so the pair must share one NVFP4 global
scale. llm-compressor's default fused pattern only matches `.mlp.gate_proj` and
misses Solar's `.mlp.experts.N.gate_proj`. A Solar-specific fused mapping was
registered so that all 7,104 pairs share
a global scale.

### Tensor composition

| dtype | Keys | Purpose |
|---|---:|---|
| `U8` | 21,312 | packed FP4 E2M1 weights (2 values per byte) |
| `F8_E4M3` | 21,312 | per-group scales (group size 16) |
| `F32` | 21,360 | per-tensor global scales + router correction bias |
| `BF16` | 891 | unquantized paths kept at full precision |

## Quality

Measured with the **same fixed prompts, same engine and same sampling** as the
BF16 parent: vLLM `v0.22.0-solar-open2`, tensor parallel 4, `temperature=0`,
`top_p=1.0`, `repetition_penalty=1.0`, `seed=42`.

| Metric | v1 (before healing) | v2 BF16 | v2 NVFP4A16 |
|---|---:|---:|---:|
| distinct-1 &uarr; | 0.3225 | **0.4633** | 0.4357 |
| distinct-3 &uarr; | 0.5954 | **0.827** | 0.8183 |
| top 3-gram ratio &darr; | 0.2612 | **0.018** | 0.0164 |
| distinct word ratio &uarr; | 0.4441 | **0.621** | 0.5956 |
| Repetition collapse / 16 | 5 | **0** | **0** |
| Closed `<\|think:end\|>` / 16 | 0 | **8** | 9 |
| Stopped on its own / 16 | 0 | **4** | 4 |

NVFP4A16 is effectively on par with the BF16 parent — repetition collapse stays
at 0 of 16 and the top 3-gram ratio is marginally lower. The full transcript is
in `healing_comparison.md`.

## Usage

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
uv pip install compressed-tensors
```

Load through a Solar Open 2-compatible runtime with the compressed-tensors
NVFP4 path. This release was verified on the Upstage vLLM Solar branch
`v0.22.0-solar-open2` at tensor parallel 4. Tensor naming follows the same
unpacked per-expert convention as v1.

## Limitations

- W4A16 keeps activations at 16-bit. The goal is memory and bandwidth
  reduction, not FP4 compute throughput.
- FP4 is lossy. Even though quantization error is confined to the routed
  experts, outputs are not bit-identical to the BF16 parent.
- All limitations of the BF16 parent carry over.

## Citation

See [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2).

## License

**Upstage Solar License**, identical to the BF16 parent. Redistribution and use
must satisfy that license, including its Solar naming and attribution
requirements.

---

## 한국어

## Built with Solar — 모델 계보

| 역할 | 모델 |
|---|---|
| 원본 / Hub `base_model` | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent (184E) | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM 결과 (148E, 힐링 전) | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16) |
| 힐링 결과 BF16 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2) |
| **이 저장소** | Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2 |
| v1에 동일 양자화를 적용한 모델 | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4) |

## 모델 개요

[Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2) 의 weight-only **NVFP4A16 (W4A16)**
compressed-tensors 양자화 버전입니다. routed expert 투영만 양자화하고 모든
토큰이 지나는 경로는 BF16으로 남겼습니다.

| 항목 | 값 |
|---|---|
| 스킴 | `NVFP4A16` (compressed-tensors `nvfp4-pack-quantized`) |
| 가중치 | NVIDIA FP4 E2M1, group size 16 |
| 그룹 스케일 | `float8_e4m3fn` + 텐서별 FP32 global scale |
| 활성값 | **양자화하지 않음 (16-bit)** |
| 알고리즘 | llm-compressor `model_free_ptq` — 데이터 무관 RTN, calibration 불필요 |
| 양자화 모듈 | routed expert 투영 21,312개 (48 × 148 × 3) |
| gate/up global scale 공유 페어 | 7,104 |
| PTQ 소요 | 6 GPU에서 82초 |
| Payload | 80,175,895,040 bytes (80.18 GB) |
| 샤드 / 텐서 키 | 9 / 64,875 |

240.80 GB → 80.18 GB, 3.0배 축소입니다.

### BF16으로 남긴 경로

```
re:^model\.layers\.\d+\.self_attn\..*$            # attention (KDA linear + full)
re:^model\.layers\.\d+\.mlp\.shared_experts\..*$   # shared expert
re:^model\.layers\.\d+\.mlp\.gate.*$              # router weight + correction bias
model.embed_tokens
lm_head
```

라우터를 양자화하지 않았으므로 양자화가 라우팅 결정 자체를 바꾸지 못합니다.
attention·shared expert·embedding·LM head도 양자화하지 않았으므로 dense 경로에
FP4가 개입하지 않고, 토큰당 선택되는 148개 중 8개 routed expert에만 적용됩니다.

### gate/up global scale 공유

런타임은 `gate_proj` 와 `up_proj` 를 `gate_up_proj [148, 2560, 4096]` 하나로
합쳐 로드하므로 두 텐서가 동일한 NVFP4 global scale을 가져야 합니다.
llm-compressor의 기본 fused 패턴은 `.mlp.gate_proj` 만 인식해 Solar의
`.mlp.experts.N.gate_proj` 를 놓치므로, Solar 전용 fused 매핑을 등록해
7,104개 페어가 모두 global scale을
공유하도록 했습니다.

### 텐서 구성

| dtype | 키 수 | 용도 |
|---|---:|---|
| `U8` | 21,312 | packed FP4 E2M1 가중치 (바이트당 2값) |
| `F8_E4M3` | 21,312 | 그룹 스케일 (group size 16) |
| `F32` | 21,360 | 텐서별 global scale + router correction bias |
| `BF16` | 891 | 양자화하지 않은 경로 |

## 품질

BF16 부모와 **동일한 고정 프롬프트·동일 엔진·동일 샘플링**으로 측정했습니다.
vLLM `v0.22.0-solar-open2`, tensor parallel 4, `temperature=0`, `top_p=1.0`,
`repetition_penalty=1.0`, `seed=42`.

| 지표 | v1 (힐링 전) | v2 BF16 | v2 NVFP4A16 |
|---|---:|---:|---:|
| distinct-1 &uarr; | 0.3225 | **0.4633** | 0.4357 |
| distinct-3 &uarr; | 0.5954 | **0.827** | 0.8183 |
| top 3-gram ratio &darr; | 0.2612 | **0.018** | 0.0164 |
| distinct word ratio &uarr; | 0.4441 | **0.621** | 0.5956 |
| Repetition collapse / 16 | 5 | **0** | **0** |
| Closed `<\|think:end\|>` / 16 | 0 | **8** | 9 |
| Stopped on its own / 16 | 0 | **4** | 4 |

NVFP4A16은 BF16 부모와 사실상 동등합니다 — 반복 붕괴가 16개 중 0개로 동일하고
최빈 3-gram 비율은 오히려 근소하게 낮습니다. 생성 결과 전문은
`healing_comparison.md` 에 있습니다.

## 사용

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
uv pip install compressed-tensors
```

Solar Open 2 호환 런타임에서 compressed-tensors NVFP4 경로로 로드합니다.
이 릴리스는 Upstage vLLM Solar 브랜치 `v0.22.0-solar-open2`, tensor parallel 4
에서 검증했습니다. 텐서 이름 규약은 v1과 같은 unpacked per-expert 형식입니다.

## 한계

- W4A16이므로 활성값은 16비트입니다. 목적은 메모리·대역폭 절감이지 FP4 연산
  처리량이 아닙니다.
- FP4는 손실 압축입니다. 양자화 오차가 routed expert에 국한되더라도 출력이 BF16
  부모와 비트 단위로 같지는 않습니다.
- BF16 부모의 모든 한계가 그대로 이어집니다.

## 인용

[Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2) 를 참조하십시오.

## 라이선스

**Upstage Solar License**, BF16 부모와 동일합니다. 재배포와 사용은 Solar 명명·
귀속 요구를 포함한 해당 라이선스를 따라야 합니다.
