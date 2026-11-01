---
base_model: Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16
base_model_relation: quantized
datasets:
- Baekpica/K-EXAONE-236B-REAP-calibration-mix
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
- text-generation
- compressed-tensors
- nvfp4
- w4a16
- quantized
---
<!-- solar-ream-hub-card:v1 -->

# Solar-Open2-120B-A15B-REAM-148E-NVFP4

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## English

## Built with Solar

This is the routed-experts-only **NVFP4A16 (W4A16)** derivative of
[Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16).
The BF16 parent was created by applying
[REAM](https://github.com/SamsungSAILMontreal/ream) to a REAP-pruned
[upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)
derivative. This is not an official Upstage or Samsung SAIL Montréal release.

## [Update] Verified vLLM Serving

This exact checkpoint was successfully served from a local model directory on
an NVIDIA GB10 with a **262,144-token context window**. The working runtime is
a custom source build based on **vLLM v0.25.1**, with Solar Open 2 support
ported from
[UpstageAI/vllm `v0.22.0-solar-open2`](https://github.com/UpstageAI/vllm/tree/v0.22.0-solar-open2).
Stock vLLM v0.25.1 does not include this port.

| Component | Verified version / setting |
|---|---|
| vLLM | 0.25.1 + custom Solar Open 2 port |
| PyTorch / CUDA | 2.11.0+cu130 / CUDA 13.0 |
| Transformers | 5.14.1+solaropen2 |
| FlashInfer | 0.6.13, JIT cache 0.6.13+cu130 |
| Device | NVIDIA GB10, TP 1 |
| Context / concurrency | 262,144 tokens, max sequences 2 |

Install the CUDA 13.0 JIT cache explicitly:

```bash
uv pip install "flashinfer-jit-cache==0.6.13+cu130" \
  --index https://flashinfer.ai/whl/cu130
```

Core settings from the confirmed 256K-context launch:

```bash
MODEL_DIR=/path/to/Solar-Open2-120B-A15B-REAM-148E-NVFP4

CUDA_HOME=/usr/local/cuda-13.0 vllm serve "$MODEL_DIR" \
  --optimization-level 3 \
  --max-model-len 262144 \
  --max-num-seqs 2 \
  --max-num-batched-tokens 8192 \
  --gpu-memory-utilization 0.90 \
  --tensor-parallel-size 1 \
  --moe-backend flashinfer_b12x \
  --attention-backend flashinfer \
  --kv-cache-dtype fp8 \
  --quantization compressed-tensors \
  --enable-chunked-prefill \
  --enable-prefix-caching \
  --reasoning-parser solar_open2 \
  --tool-call-parser solar_open2 \
  --logits-processors vllm.v1.sample.logits_processor.solar_open2:SolarOpen2TemplateLogitsProcessor \
  --default-chat-template-kwargs '{"think_render_option":"preserved"}' \
  --enable-auto-tool-choice \
  --language-model-only
```

| Agent conversation | Tool-aware response | Served model selected |
|:---:|:---:|:---:|
| [![Agent conversation](assets/solar-open2-120b-ream-nvfp4-256k-01.jpg)](assets/solar-open2-120b-ream-nvfp4-256k-01.jpg) | [![Tool-aware response](assets/solar-open2-120b-ream-nvfp4-256k-02.jpg)](assets/solar-open2-120b-ream-nvfp4-256k-02.jpg) | [![Served model selected](assets/solar-open2-120b-ream-nvfp4-256k-03.jpg)](assets/solar-open2-120b-ream-nvfp4-256k-03.jpg) |

## Overview

The architecture retains **148 routed experts and 1 shared expert per layer**.
Before storage quantization it has exactly **120,398,326,528 total parameters**
and **14,701,865,728 active parameters per token**.

| Item | Value |
|---|---:|
| Quantization | NVFP4A16, weight-only W4A16 |
| Format | compressed-tensors `nvfp4-pack-quantized` |
| Quantized coverage | all 21,312 routed-expert projections in 48 layers |
| Quantized modules | routed `gate_proj`, `up_proj`, and `down_proj` weights |
| Group size | 16 |
| Per-group scale dtype | FP8 E4M3 |
| Activation quantization | none |
| Raw tensor payload | 80,175,895,040 bytes (80.176 GB / 74.670 GiB) |

This is **W4A16**, not the NVFP4 W4A4 preset. There are no activation
quantizers, `input_global_scale` tensors, or weight zero points.

### Quantized versus preserved components

Only routed-expert projection weights are quantized. The following remain
bit-identical to the audited BF16 parent:

- all softmax/GQA and KDA attention weights;
- the shared expert in every layer;
- router weights and FP32 `e_score_correction_bias` buffers;
- token embeddings and `lm_head`;
- normalization and every other non-routed tensor.

Quantization uses data-free RTN through
`llmcompressor.model_free_ptq`, `llmcompressor==0.12.0`, and
`compressed-tensors==0.17.1`. A Solar-specific fused mapping makes each
expert's `gate_proj` and `up_proj` share one microscale global scale. The audit
checks all **7,104 gate/up pairs** bitwise, validates every local and global
scale, and compares all **939 preserved tensors** to the BF16 parent.

The final checkpoint is repacked into shards below 10,000,000,000 physical
bytes. Repacking copies raw safetensors payloads without decoding or changing
them; the audit compares every one of the **64,875 logical tensor payloads**
before atomic publication.

## REAM Parent

The BF16 parent merges 36 of 184 routed experts per layer into 148 centroids.
It combines router-logit and actually routed weighted-output similarity,
aligns intermediate neurons with activation plus rank-64 weight-PCA features
and Hungarian matching, then performs saliency-weighted FP32 merging. Router
weights and correction biases are sliced to the same centroid order.

REAM used 3,072 deterministic 512-token windows (1,572,864 tokens) from
K-EXAONE-236B-REAP-calibration-mix for layerwise statistics. NVFP4 conversion
itself is data-free and does not use calibration data or fine-tuning.

The Solar implementation is available at
[Baekpica/solar-ream](https://github.com/Baekpica/solar-ream) and acknowledges
the official [SamsungSAILMontreal/ream](https://github.com/SamsungSAILMontreal/ream)
and [CerebrasResearch/reap](https://github.com/CerebrasResearch/reap)
repositories.

## Provenance and Usage

| Component | Pinned revision |
|---|---|
| Original model upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| Official REAM implementation | 84a3030716a0059589e9d10e2ea049e32b76cfa6 |
| Official REAP implementation | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| llmcompressor | 0.12.0 |
| compressed-tensors | 0.17.1 |

Install the Solar architecture support and compressed-tensors stack:

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
uv pip install "llmcompressor==0.12.0" "compressed-tensors==0.17.1"
```

For serving, use the verified stack and launch command in the update above.
The Upstage v0.22 branch is the architecture source for the custom v0.25.1
port; stock vLLM v0.25.1 is not drop-in compatible.

## Limitations

The 74.670 GiB raw tensor payload is not an end-to-end serving-memory
guarantee. Runtime state, CUDA context, kernels, graph capture, KDA state, KV
cache, and temporary buffers require additional memory. Unsupported runtimes
may expand weights.

Publication checks establish structure, quantization coverage, finite positive
scales, shared gate/up scales, BF16-parent preservation, and payload integrity.
They are not a quality benchmark. REAM and quantization can affect reasoning,
factuality, multilingual behavior, tools, routing, and long context. Evaluate
quality, safety, peak memory, throughput, and compatibility for the intended
use.

## Citation

```bibtex
@article{jha2026ream,
  title={REAM: Merging Improves Pruning of Experts in LLMs},
  author={Jha, Saurav and Hashemzadeh, Maryam and Pasand, Ali Saheb and Parviz, Ali and Lee, Min-Joong and Knyazev, Boris},
  journal={arXiv preprint arXiv:2604.04356},
  year={2026}
}
```

## License

This derivative is distributed under the **Upstage Solar License**. The
repository includes an exact copy of the source model's `LICENSE`.

---

## 한국어

## Built with Solar

이 모델은
[Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16)의
routed-expert weight만 **NVFP4A16 (W4A16)**으로 양자화한 커뮤니티 파생
모델입니다. BF16 parent는 REAP-pruned Solar Open 2 파생 모델에
[REAM](https://github.com/SamsungSAILMontreal/ream)을 적용해 만들었습니다.
Upstage 또는 Samsung SAIL Montréal의 공식 릴리스가 아닙니다.

## 모델 개요

각 레이어에 **148개 routed expert와 1개 shared expert**가 있습니다. 저장
양자화 전 전체 파라미터는 정확히 **120,398,326,528개**, 토큰당 활성
파라미터는 **14,701,865,728개**입니다.

| 항목 | 값 |
|---|---:|
| 양자화 | NVFP4A16, weight-only W4A16 |
| 포맷 | compressed-tensors `nvfp4-pack-quantized` |
| 양자화 범위 | 48개 레이어의 routed-expert projection 21,312개 전부 |
| 양자화 모듈 | routed `gate_proj`, `up_proj`, `down_proj` weight |
| Group size | 16 |
| Group scale dtype | FP8 E4M3 |
| Activation 양자화 | 없음 |
| Raw tensor payload | 80,175,895,040 bytes (80.176 GB / 74.670 GiB) |

비슷한 이름의 W4A4 preset이 아니라 **W4A16**입니다. Activation
quantizer, `input_global_scale`, weight zero point가 없습니다.

### 양자화 범위와 보존 범위

Routed-expert projection weight만 양자화했습니다. Attention 전체, shared
expert, router weight와 FP32 correction bias, embedding, `lm_head`,
normalization, 그 밖의 non-routed tensor는 audit된 BF16 parent와
bit-identical하게 유지합니다.

`llmcompressor==0.12.0`, `compressed-tensors==0.17.1`의 data-free RTN
`model_free_ptq`를 사용했습니다. Solar 전용 fused mapping으로 각 expert의
`gate_proj`와 `up_proj`가 같은 microscale global scale을 공유합니다.
Audit은 **7,104 gate/up pair**를 bitwise 검사하고, 모든 local/global scale과
BF16 parent에서 보존한 **939개 tensor**를 검증합니다.

최종 checkpoint는 physical shard당 10,000,000,000 bytes 미만으로
repack합니다. Repack은 raw safetensors payload를 변경하지 않는 layout
작업이며 atomic publish 전에 **64,875개 tensor payload 전부**를 비교합니다.

## REAM Parent

BF16 parent는 레이어마다 184개 routed expert 중 36개를 148개 centroid에
흡수·병합합니다. Router-logit과 실제 routed weighted-output similarity를
결합하고, activation 및 rank-64 weight-PCA feature와 Hungarian matching으로
neuron을 정렬한 뒤 saliency-weighted FP32 merge를 수행합니다. Router와
correction bias는 같은 centroid 순서로 slice합니다.

REAM 통계에는 K-EXAONE-236B-REAP-calibration-mix에서 추출한 512-token
window 3,072개, 정확히 1,572,864 tokens를 사용했습니다. NVFP4 변환 자체는
data-free이며 calibration이나 fine-tuning을 하지 않습니다.

Solar 구현은
[Baekpica/solar-ream](https://github.com/Baekpica/solar-ream)에 공개하며,
공식 [SamsungSAILMontreal/ream](https://github.com/SamsungSAILMontreal/ream)과
[CerebrasResearch/reap](https://github.com/CerebrasResearch/reap)을
명시적으로 acknowledge합니다.

## 출처 및 사용법

| 구성요소 | 고정 revision |
|---|---|
| 원본 모델 upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| 공식 REAM 구현 | 84a3030716a0059589e9d10e2ea049e32b76cfa6 |
| 공식 REAP 구현 | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| llmcompressor | 0.12.0 |
| compressed-tensors | 0.17.1 |

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
uv pip install "llmcompressor==0.12.0" "compressed-tensors==0.17.1"
```

서빙에는 English 섹션의 update에 기재된 stack과 실행 명령을 사용하십시오.
Upstage v0.22 브랜치는 v0.25.1 커스텀 포트의 architecture source이며,
순정 vLLM v0.25.1과 drop-in compatible하지 않습니다.

## 제한사항

74.670 GiB raw tensor payload는 end-to-end serving-memory 보장이 아닙니다.
Runtime state, CUDA context, kernel, graph capture, KDA state, KV cache,
temporary buffer가 추가 메모리를 사용하며 미지원 runtime은 weight를
펼칠 수 있습니다.

공개 전 검증은 구조, 양자화 범위, finite positive scale, gate/up shared
scale, BF16-parent 보존, payload 무결성을 확인하지만 품질 benchmark는
아닙니다. REAM과 양자화는 reasoning, factuality, 다국어, tool use,
routing, long-context 동작에 영향을 줄 수 있습니다. 실제 용도에 맞춰
품질, 안전성, peak memory, throughput, 호환성을 평가하십시오.

## 인용

```bibtex
@article{jha2026ream,
  title={REAM: Merging Improves Pruning of Experts in LLMs},
  author={Jha, Saurav and Hashemzadeh, Maryam and Pasand, Ali Saheb and Parviz, Ali and Lee, Min-Joong and Knyazev, Boris},
  journal={arXiv preprint arXiv:2604.04356},
  year={2026}
}
```

## 라이선스

이 파생 모델은 **Upstage Solar License**에 따라 배포됩니다. 저장소의
`LICENSE`는 원본 모델 라이선스의 정확한 사본입니다.
