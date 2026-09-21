---
base_model: Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16
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
- expert-pruning
- text-generation
- compressed-tensors
- nvfp4
- w4a16
- quantized
---
<!-- solar-reap-hub-card:v1 -->

# Solar-Open2-148B-A15B-REAP-184E-NVFP4

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## English

## Built with Solar

This is the routed-experts-only **NVFP4A16 (W4A16)** derivative of [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16), which was REAP-pruned from [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B). It is not an official Upstage release and is not sponsored, endorsed, or certified by Upstage.

## [Update] Verified vLLM Serving

This exact checkpoint was successfully served from a local model directory on
an NVIDIA GB10. The working runtime is a custom source build based on
**vLLM v0.25.1**, with Solar Open 2 support ported from
[UpstageAI/vllm `v0.22.0-solar-open2`](https://github.com/UpstageAI/vllm/tree/v0.22.0-solar-open2).
Stock vLLM v0.25.1 does not include this port.

| Component | Verified version / setting |
|---|---|
| vLLM | 0.25.1 + custom Solar Open 2 port |
| PyTorch / CUDA | 2.11.0+cu130 / CUDA 13.0 |
| Transformers | 5.14.1+solaropen2 |
| FlashInfer | 0.6.13, JIT cache 0.6.13+cu130 |
| Device | NVIDIA GB10, TP 1, max sequences 1 |

Install the CUDA 13.0 JIT cache explicitly:

```bash
uv pip install "flashinfer-jit-cache==0.6.13+cu130" \
  --index https://flashinfer.ai/whl/cu130
```

Core settings from the confirmed 65K-context launch:

```bash
MODEL_DIR=/path/to/Solar-Open2-148B-A15B-REAP-184E-NVFP4

CUDA_HOME=/usr/local/cuda-13.0 vllm serve "$MODEL_DIR" \
  --optimization-level 3 \
  --max-model-len 65536 \
  --max-num-seqs 1 \
  --max-num-batched-tokens 4096 \
  --gpu-memory-utilization 0.94 \
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

![Solar Open 2 148B NVFP4 serving on NVIDIA GB10](assets/solar-open2-148b-nvfp4-gb10.jpg)

## Overview

The architecture retains **184 routed experts and 1 shared expert per MoE layer**, after removing 136 of 320 routed experts per layer (**42.5% routed-expert pruning**). Before storage quantization, it has exactly **147,584,494,336 total parameters (147.584B)** and **14,708,943,616 active parameters per token (14.709B)**.

| Item | Value |
|---|---:|
| Quantization | NVFP4A16, weight-only W4A16 |
| Format | compressed-tensors nvfp4-pack-quantized |
| Quantized coverage | all 26,496 routed-expert projections in all 48 layers |
| Quantized modules | routed gate_proj, up_proj, and down_proj weights |
| Group size | 16 |
| Per-group scale dtype | FP8 E4M3 |
| Activation quantization | none |
| Raw tensor payload | 95,478,316,544 bytes (95.478 GB / 88.921 GiB) |

This is **W4A16**, not the similarly named NVFP4 W4A4 preset. There are no activation quantizers and the <code>input_global_scale</code> tensor count is exactly **0**.

### Quantized versus preserved components

Only routed-expert projection weights are quantized. The following remain bit-identical to the audited BF16 parent:

- all softmax/GQA and KDA attention weights;
- the shared expert in every layer;
- router weights and FP32 <code>e_score_correction_bias</code> buffers;
- token embeddings and <code>lm_head</code>;
- normalization and every other non-routed tensor.

Quantization uses data-free RTN through <code>llmcompressor.model_free_ptq</code> with <code>llmcompressor==0.12.0</code> and <code>compressed-tensors==0.17.1</code>. A Solar-specific fused mapping makes each expert's <code>gate_proj</code> and <code>up_proj</code> share one microscale global scale. The audit checks bitwise equality for all **8,832 gate/up pairs**. The final repack is a byte-preserving layout operation; its audit hashes all tensor payloads and separately verifies every preserved BF16/FP32 tensor against the parent.

## Personal Motivation

This is a hobby project driven by technical curiosity. Solar Open 2 is a new model, so this release is not based on a claim that it is being overlooked. The practical question was whether expert pruning plus W4A16 could move a 250B-class model a little closer to direct download, serving, and evaluation by open-source users, independent developers, small labs, and owners of high-end non-datacenter hardware.

The pruning calibration mixture deliberately contains substantial Korean instruction, reasoning, tool-use, and long-context material as a counterweight to the predominantly English data that is readily available. The intent is to give those Korean signals a chance to influence expert selection. REAP does not identify language-labelled experts, so this does **not** establish that “Korean experts” were found or guarantee preservation of Korean capability.

I am also interested in independently operable, Korea-developed foundation-model options for isolated networks and environments with data-governance, provenance, supply-chain, or licensing constraints. That does not make a domestic model inherently superior: performance, cost, reliability, licensing, and maintainability still require objective evaluation. I hope this release encourages more community experimentation, derivative work, and public evaluation around Korea-developed open models. The result remains large and experimental; it is an attempt to narrow an accessibility gap, not a hype or benchmark claim.

## Pruning Setup

The BF16 parent used per-layer REAP saliency:

    mean(actual_topk_router_weight × expert_output_L2_norm)

The 136 lowest-saliency routed experts were removed independently from each of 48 layers. Retained source expert IDs were sorted in ascending order and recorded in <code>reap_metadata.json</code>.

Because Solar Open 2 uses fused expert tensors, the same ordered 184 keep indices were applied to <code>experts.gate_up_proj</code> [320, 2560, 4096], <code>experts.down_proj</code> [320, 4096, 1280], <code>gate.weight</code> [320, 4096], and <code>gate.e_score_correction_bias</code> [320]. The final configuration is <code>n_routed_experts = 184</code>. The correction bias must be sliced in lockstep to preserve router indexing, and the shared expert remains unchanged.

The implementation follows and acknowledges the official [Cerebras REAP repository](https://github.com/CerebrasResearch/reap) and the [REAP paper](https://arxiv.org/abs/2510.13999). Solar-specific fused-tensor pruning and quantization mappings were added for this derivative.

## Calibration Mixture

REAP saliency used K-EXAONE-236B-REAP-calibration-mix that I used for the K-EXAONE-REAP series. The mixture contains **16,780 samples**, measured as exactly **106,795,574 tokens** by the pinned Solar tokenizer, with a maximum measured sample length of **269,944 tokens**. It was used for pruning saliency, not for activation calibration or fine-tuning.

At layer 0, 23 routed experts received no route in this calibration mixture and consequently had exact zero observed saliency; all 23 were included among the 136 removed experts. Every routed expert in layers 1–47 was observed. The published calibration audit verifies the zero-valued accumulators, exact route totals, reconstructed saliency, and the final keep map rather than treating missing observations as measured evidence.

| Bucket | Samples | Solar tokens | Max Solar length | Purpose |
|---|---:|---:|---:|---|
| code_en | 2,048 | 1,166,925 | 6,430 | Code generation |
| mot_code | 2,048 | 11,641,280 | 16,147 | Code reasoning |
| mot_math | 2,048 | 10,710,847 | 15,697 | Mathematical reasoning |
| mot_science | 2,048 | 8,904,796 | 9,947 | Scientific reasoning |
| tool_en | 2,048 | 901,608 | 2,220 | Single-turn tool calling |
| agentic_swe | 2,048 | 44,337,438 | 35,398 | Multi-turn agentic coding |
| ko_instr | 3,072 | 6,880,271 | 18,792 | Korean instruction and reasoning |
| ko_tool | 1,024 | 2,366,960 | 5,927 | Korean tool and function calling |
| long_ctx | 384 | 17,011,558 | 136,514 | Korean/English long-context QA and summarization |
| stress_256k | 12 | 2,873,891 | 269,944 | Late-position needle and routing stress |

## Provenance and Usage

| Component | Pinned revision |
|---|---|
| Source model upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| BF16 parent | Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16 |
| REAP implementation | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

Use the Upstage Transformers Solar Open 2 branch <code>v5.14.1-solar-open2</code> for architecture support and install the pinned compressed-tensors stack when inspecting or loading the packed checkpoint:

    uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
    uv pip install "llmcompressor==0.12.0" "compressed-tensors==0.17.1"

For serving, use the verified stack and launch command in the update above.
The Upstage v0.22 branch is the architecture source for the custom v0.25.1
port; stock vLLM v0.25.1 is not drop-in compatible.

## Limitations

The 88.921 GiB raw tensor payload was selected with 128 GB GB10-class unified memory in mind, but it is **not an end-to-end serving-memory guarantee**. The operating system, CUDA context, engine metadata, conversion buffers, kernels, graph capture, recurrent KDA state, and KV cache all consume additional memory. Actual free unified memory is lower than the nominal capacity, and unsupported runtimes may expand weights and fail to load.

Publication checks establish structure, quantization coverage, finite positive scales, bitwise shared gate/up scales, and payload integrity. They are not a downstream quality evaluation. No benchmark result is claimed for the pruned or quantized model. Pruning and quantization can affect reasoning, factuality, Korean/Japanese/English behavior, tool use, routing balance, and long context. Evaluate quality, peak memory, throughput, runtime compatibility, and licensing for the intended use.

## Citation

<pre>
@misc{solar-open-2-2026,
  title={Solar Open 2 Technical Report},
  author={Upstage AI},
  year={2026},
  url={https://huggingface.co/upstage/Solar-Open2-250B}
}
</pre>

## License

This derivative is distributed under the **Upstage Solar License**. The repository includes an exact copy of the source model's <code>LICENSE</code>. Redistribution and use must satisfy that license, including its Solar naming and attribution requirements.

---

## 한국어

## Built with Solar

이 모델은 [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)를 REAP 프루닝한 [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16)에서 routed-expert 가중치만 **NVFP4A16 (W4A16)**으로 양자화한 커뮤니티 파생 모델입니다. Upstage의 공식 릴리스가 아니며 Upstage의 후원, 보증 또는 인증을 받은 모델이 아닙니다.

## 모델 개요

각 MoE 레이어에서 **184개 routed expert와 1개 shared expert**를 유지하며, 원본 320개 중 136개를 제거한 정확히 **42.5% routed-expert pruning** 모델입니다. 저장 양자화 전 파라미터 수는 정확히 **147,584,494,336개(147.584B)**이고 토큰당 활성 파라미터는 **14,708,943,616개(14.709B)**입니다.

| 항목 | 값 |
|---|---:|
| 양자화 | NVFP4A16, weight-only W4A16 |
| 포맷 | compressed-tensors nvfp4-pack-quantized |
| 양자화 범위 | 48개 레이어의 routed-expert projection 26,496개 전부 |
| 양자화 모듈 | routed gate_proj, up_proj, down_proj weight |
| Group size | 16 |
| Group scale dtype | FP8 E4M3 |
| Activation 양자화 | 없음 |
| Raw tensor payload | 95,478,316,544 bytes (95.478 GB / 88.921 GiB) |

이 모델은 비슷한 이름의 NVFP4 W4A4 preset이 아니라 **W4A16**입니다. Activation quantizer가 없으며 <code>input_global_scale</code> tensor 수는 정확히 **0개**입니다.

### 양자화 모듈과 보존 모듈

Routed-expert projection weight만 양자화했습니다. 다음 구성요소는 audit된 BF16 parent와 bit-identical하게 유지됩니다.

- softmax/GQA 및 KDA attention weight 전체
- 모든 레이어의 shared expert
- router weight와 FP32 <code>e_score_correction_bias</code> buffer
- token embedding과 <code>lm_head</code>
- normalization 및 그 밖의 모든 non-routed tensor

양자화에는 <code>llmcompressor==0.12.0</code>과 <code>compressed-tensors==0.17.1</code>의 data-free RTN, <code>llmcompressor.model_free_ptq</code>를 사용합니다. Solar 전용 fused mapping으로 각 expert의 <code>gate_proj</code>와 <code>up_proj</code>가 하나의 microscale global scale을 공유하도록 했고, audit은 **8,832개 gate/up pair 전부**의 scale을 bitwise 비교합니다. 최종 repack은 tensor payload를 바꾸지 않는 byte-preserving layout 작업이며, 모든 tensor payload hash와 보존된 BF16/FP32 tensor를 parent와 별도로 검증합니다.

## 개인적인 동기

이 작업은 기술적 호기심에서 시작한 취미 프로젝트입니다. Solar Open 2는 새로 공개된 모델이므로 관심을 덜 받고 있다는 서사를 전제로 하지 않습니다. 현실적인 관심사는 expert pruning과 W4A16을 결합해 250B급 모델을 오픈소스 사용자, 독립 개발자, 소규모 연구실, 고성능 비데이터센터 장비 사용자가 직접 다운로드하고 서빙하며 평가할 수 있는 범위에 조금 더 가깝게 가져올 수 있는지였습니다.

Pruning calibration mixture에는 쉽게 구할 수 있는 데이터가 영어에 편중된 현실에 대한 작은 counterweight로 한국어 instruction, reasoning, tool-use, long-context 데이터를 충분히 포함했습니다. 한국어 신호가 expert 선택에 영향을 줄 기회를 주려는 의도입니다. 그러나 REAP는 언어 label이 붙은 expert를 식별하지 않으므로 “한국어 expert를 찾았다”고 말할 수 없고, 한국어 능력 보존도 보장하지 않습니다.

폐쇄망과 data governance, provenance, supply chain, licensing 제약이 있는 환경에서 독립적으로 운용 가능한 한국 개발 foundation model 선택지에도 실용적인 관심이 있습니다. 그렇다고 국내 모델이 본질적으로 우월하다는 뜻은 아닙니다. 성능, 비용, 신뢰성, 라이선스, 유지보수성을 객관적으로 평가해야 합니다. 이 공개가 한국 개발 open model을 둘러싼 더 많은 커뮤니티 실험, 파생 작업, 공개 평가로 이어지기를 바랍니다. 결과물은 여전히 크고 실험적이며, 접근성 격차를 조금 줄이려는 시도이지 과장이나 benchmark 주장이 아닙니다.

## Pruning 설정

BF16 parent는 48개 레이어에서 다음 REAP saliency를 expert별로 계산했습니다.

    mean(actual_topk_router_weight × expert_output_L2_norm)

각 레이어에서 saliency가 가장 낮은 routed expert 136개를 독립적으로 제거했고, 유지한 원본 expert ID는 오름차순으로 정렬하여 <code>reap_metadata.json</code>에 기록했습니다.

Solar Open 2는 fused expert tensor를 사용하므로 동일한 순서의 184개 keep index를 <code>experts.gate_up_proj</code> [320, 2560, 4096], <code>experts.down_proj</code> [320, 4096, 1280], <code>gate.weight</code> [320, 4096], <code>gate.e_score_correction_bias</code> [320]에 모두 적용했습니다. 최종 설정은 <code>n_routed_experts = 184</code>입니다. Router index를 보존하려면 correction bias도 반드시 같은 순서로 slice해야 하며 shared expert는 그대로 유지합니다.

구현은 공식 [Cerebras REAP 저장소](https://github.com/CerebrasResearch/reap)와 [REAP 논문](https://arxiv.org/abs/2510.13999)을 따르고 이를 명시적으로 acknowledge합니다. 이 파생 모델을 위해 Solar 전용 fused-tensor pruning 및 quantization mapping을 추가했습니다.

## Calibration 데이터 구성

REAP saliency 계산에는 지난번 K-EXAONE-REAP 시리즈에 활용된 K-EXAONE-236B-REAP-calibration-mix를 사용했습니다. 전체 **16,780개 샘플**이며, 고정된 Solar tokenizer로 측정한 정확한 토큰 수는 **106,795,574개**, 측정된 샘플 최대 길이는 **269,944 tokens**입니다. 이 데이터는 pruning saliency에만 사용했고 activation calibration이나 fine-tuning에는 사용하지 않았습니다.

0번 레이어에서는 routed expert 23개가 이 calibration mixture에서 한 번도 선택되지 않아 관측 saliency가 정확히 0이었고, 23개 모두 제거된 136개에 포함됐습니다. 1–47번 레이어에서는 모든 routed expert가 관측됐습니다. 공개 calibration audit은 미관측 항목의 accumulator가 정확히 0인지, 전체 route 수와 재구성한 saliency가 일치하는지, 최종 keep map에서 해당 expert들이 실제로 제거됐는지를 함께 검증합니다.

| 버킷 | 샘플 수 | Solar 토큰 수 | Solar 최대 길이 | 목적 |
|---|---:|---:|---:|---|
| code_en | 2,048 | 1,166,925 | 6,430 | 코드 생성 |
| mot_code | 2,048 | 11,641,280 | 16,147 | 코드 추론 |
| mot_math | 2,048 | 10,710,847 | 15,697 | 수학 추론 |
| mot_science | 2,048 | 8,904,796 | 9,947 | 과학 추론 |
| tool_en | 2,048 | 901,608 | 2,220 | 단일 턴 도구 호출 |
| agentic_swe | 2,048 | 44,337,438 | 35,398 | 멀티턴 agentic coding |
| ko_instr | 3,072 | 6,880,271 | 18,792 | 한국어 instruction 및 reasoning |
| ko_tool | 1,024 | 2,366,960 | 5,927 | 한국어 tool 및 function calling |
| long_ctx | 384 | 17,011,558 | 136,514 | 한영 long-context QA 및 summarization |
| stress_256k | 12 | 2,873,891 | 269,944 | 후반부 needle 및 routing stress |

## 출처 및 사용법

| 구성요소 | 고정 revision |
|---|---|
| 원본 모델 upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| BF16 parent | Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16 |
| REAP 구현 | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

Architecture 지원에는 Upstage Transformers Solar Open 2 branch <code>v5.14.1-solar-open2</code>를 사용하고 packed checkpoint 확인 및 로드에는 고정된 compressed-tensors stack을 설치하십시오.

    uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
    uv pip install "llmcompressor==0.12.0" "compressed-tensors==0.17.1"

서빙에는 English 섹션의 update에 기재된 stack과 실행 명령을 사용하십시오. Upstage v0.22
브랜치는 v0.25.1 커스텀 포트의 architecture source이며, 순정 vLLM v0.25.1과
drop-in compatible하지 않습니다.

## 제한사항

Raw tensor payload 88.921 GiB는 128 GB GB10급 unified memory를 염두에 둔 크기이지만 **end-to-end serving memory를 보장하지 않습니다**. OS, CUDA context, engine metadata, 변환 buffer, kernel workspace, graph capture, KDA recurrent state, KV cache가 추가 메모리를 사용합니다. 실제 free unified memory는 nominal capacity보다 작으며 지원하지 않는 runtime이 weight를 펼치면 로드에 실패할 수 있습니다.

공개 전 검증은 구조, 양자화 범위, finite positive scale, gate/up shared scale의 bitwise 일치, payload 무결성을 확인하지만 downstream 품질 평가는 아닙니다. Pruned 또는 quantized 모델의 benchmark 결과를 주장하지 않습니다. Pruning과 양자화는 reasoning, factuality, 한국어·일본어·영어 동작, tool use, routing balance, long context에 영향을 줄 수 있습니다. 사용 목적에 맞춰 품질, peak memory, throughput, runtime 호환성, 라이선스를 평가하십시오.

## 인용

<pre>
@misc{solar-open-2-2026,
  title={Solar Open 2 Technical Report},
  author={Upstage AI},
  year={2026},
  url={https://huggingface.co/upstage/Solar-Open2-250B}
}
</pre>

## 라이선스

이 파생 모델은 **Upstage Solar License**에 따라 배포됩니다. 저장소의 <code>LICENSE</code>는 원본 모델의 라이선스를 정확히 복사한 파일입니다. 재배포와 사용은 Solar 명칭 및 attribution 요구사항을 포함한 해당 라이선스를 준수해야 합니다.
