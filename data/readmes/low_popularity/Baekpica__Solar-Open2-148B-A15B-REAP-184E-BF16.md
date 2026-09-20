---
base_model: upstage/Solar-Open2-250B
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
---
<!-- solar-reap-hub-card:v1 -->

# Solar-Open2-148B-A15B-REAP-184E-BF16

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## English

## Built with Solar

This is a community derivative of [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B), created by pruning routed experts with [REAP](https://github.com/CerebrasResearch/reap). It is not an official Upstage release and is not sponsored, endorsed, or certified by Upstage.

## Overview

The model retains **184 routed experts and 1 shared expert in every MoE layer**. It removes 136 of the original 320 routed experts per layer, which is exactly **42.5% routed-expert pruning**. The configured top-k remains 8 routed experts per token, and the shared expert is always retained.

| Item | Value |
|---|---:|
| Total parameters | 147,584,494,336 (147.584B) |
| Active parameters per token | 14,708,943,616 (14.709B) |
| Transformer layers | 48 |
| Routed experts | 184 per layer |
| Shared experts | 1 per layer |
| Active experts | top-8 routed + 1 shared |
| Hidden size | 4,096 |
| Routed expert intermediate size | 1,280 |
| Weight storage | BF16; router correction bias remains FP32 |
| Raw tensor payload | 295,169,024,000 bytes (295.169 GB / 274.898 GiB) |

The 148B-A15B name is rounded; the exact total and active counts are above. Active parameters are a compute characteristic, not checkpoint memory: all retained weights still need storage or loading.

## Personal Motivation

This is a hobby project driven by technical curiosity. Solar Open 2 is a new model, so this release is not based on a claim that it is being overlooked. The practical question was whether pruning, together with the W4A16 sibling release, could move a 250B-class model a little closer to direct download, serving, and evaluation by open-source users, independent developers, small labs, and owners of high-end non-datacenter hardware.

The calibration mixture deliberately contains substantial Korean instruction, reasoning, tool-use, and long-context material as a counterweight to the predominantly English data that is readily available. The intent is to give those Korean signals a chance to influence expert selection. REAP does not identify language-labelled experts, so this does **not** establish that “Korean experts” were found or guarantee preservation of Korean capability.

I am also interested in independently operable, Korea-developed foundation-model options for isolated networks and environments with data-governance, provenance, supply-chain, or licensing constraints. That does not make a domestic model inherently superior: performance, cost, reliability, licensing, and maintainability still require objective evaluation. I hope this release encourages more community experimentation, derivative work, and public evaluation around Korea-developed open models. The result remains large and experimental; it is an attempt to narrow an accessibility gap, not a hype or benchmark claim.

## Pruning Setup

REAP saliency was accumulated independently for each routed expert in each of the 48 layers:

    mean(actual_topk_router_weight × expert_output_L2_norm)

The 136 lowest-saliency routed experts were removed independently per layer. Retained source expert IDs were sorted in ascending order before reindexing and are recorded in <code>reap_metadata.json</code>.

Solar Open 2 stores routed experts as fused tensors rather than a ModuleList. Each layer therefore applied the **same ordered 184 keep indices** to all four expert/router tensors:

| Tensor | Source shape |
|---|---:|
| experts.gate_up_proj | [320, 2560, 4096] |
| experts.down_proj | [320, 4096, 1280] |
| gate.weight | [320, 4096] |
| gate.e_score_correction_bias | [320] |

The final configuration sets <code>n_routed_experts = 184</code>. Slicing <code>e_score_correction_bias</code> in the same order is essential because stale correction-bias indexing would misalign router choices after expert reindexing. The shared expert was not sliced or pruned.

The implementation follows and acknowledges the official [Cerebras REAP repository](https://github.com/CerebrasResearch/reap) and the [REAP paper](https://arxiv.org/abs/2510.13999). Solar-specific fused-tensor handling and validation were added for this derivative.

## Calibration Mixture

Pruning saliency used K-EXAONE-236B-REAP-calibration-mix, which I used for the K-EXAONE-REAP series. The mixture contains **16,780 samples**, measured as exactly **106,795,574 tokens** by the pinned Solar tokenizer, with a maximum measured sample length of **269,944 tokens**. It was used only for saliency measurement; the model was not fine-tuned on it.

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
| REAP implementation | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

The publication audit performs full bit-exact source comparison of all **26,496 retained routed-expert projection weights**, every router weight and correction-bias tensor, and all **144 shared-expert weights**. It also checks all 48 keep-index maps, the 184E configuration, tensor shapes, parameter counts, and a finite-logit smoke inference before the checkpoint is accepted.

Use the Upstage Transformers Solar Open 2 branch, <code>v5.14.1-solar-open2</code>:

    uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_id = "Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

For serving, use the Upstage vLLM Solar fork/revision <code>v0.22.0-solar-open2</code> as the architecture reference. Solar reasoning and tool calls use <code>--reasoning-parser solar_open2</code>, <code>--tool-call-parser solar_open2</code>, and <code>--enable-auto-tool-choice</code>. Verify the target build supports Solar Open 2 hybrid KDA/GQA before loading this derivative.

## Limitations

The 274.898 GiB raw BF16 tensor payload does **not** fit in 128 GB GB10 unified memory without substantial offload. Use a multi-accelerator host or consider the W4A16 sibling. No downstream benchmark suite is claimed here, and the original 250B model's reported scores must not be attributed to this derivative without evaluation.

Expert pruning can change routing balance, specialist coverage, factuality, multilingual behavior, tool use, and long-context behavior. The configured context length is inherited from the source, but long-context quality and throughput after pruning have not been independently revalidated. Evaluate safety, accuracy, latency, memory use, and licensing fit for the intended deployment.

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

이 모델은 [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)의 routed expert를 [REAP](https://github.com/CerebrasResearch/reap)으로 프루닝한 커뮤니티 파생 모델입니다. Upstage의 공식 릴리스가 아니며 Upstage의 후원, 보증 또는 인증을 받은 모델이 아닙니다.

## 모델 개요

각 MoE 레이어에서 **184개 routed expert와 1개 shared expert**를 유지합니다. 원본의 routed expert 320개 중 레이어마다 136개를 제거했으며, 이는 정확히 **42.5% routed-expert pruning**입니다. 토큰당 top-k는 routed expert 8개로 유지되고 shared expert도 그대로 사용됩니다.

| 항목 | 값 |
|---|---:|
| 전체 파라미터 | 147,584,494,336 (147.584B) |
| 토큰당 활성 파라미터 | 14,708,943,616 (14.709B) |
| Transformer 레이어 | 48 |
| Routed expert | 레이어당 184 |
| Shared expert | 레이어당 1 |
| 활성 expert | routed top-8 + shared 1 |
| Hidden size | 4,096 |
| Routed expert intermediate size | 1,280 |
| 가중치 저장 | BF16, router correction bias는 FP32 유지 |
| Raw tensor payload | 295,169,024,000 bytes (295.169 GB / 274.898 GiB) |

148B-A15B는 반올림한 이름이며 정확한 전체 및 활성 파라미터 수는 위 표와 같습니다. 활성 파라미터 수는 연산 특성이지 체크포인트 메모리 크기가 아니므로, 저장하거나 로드할 때는 유지된 전체 가중치가 필요합니다.

## 개인적인 동기

이 작업은 기술적 호기심에서 시작한 취미 프로젝트입니다. Solar Open 2는 새로 공개된 모델이므로 관심을 덜 받고 있다는 서사를 전제로 하지 않습니다. 현실적인 관심사는 프루닝과 함께 공개하는 W4A16 버전을 통해 250B급 모델을 오픈소스 사용자, 독립 개발자, 소규모 연구실, 고성능 비데이터센터 장비 사용자가 직접 다운로드하고 서빙하며 평가할 수 있는 범위에 조금 더 가깝게 가져올 수 있는지였습니다.

Calibration mixture에는 쉽게 구할 수 있는 데이터가 영어에 편중된 현실에 대한 작은 counterweight로 한국어 instruction, reasoning, tool-use, long-context 데이터를 충분히 포함했습니다. 한국어 신호가 expert 선택에 영향을 줄 기회를 주려는 의도입니다. 그러나 REAP는 언어 label이 붙은 expert를 식별하지 않으므로 “한국어 expert를 찾았다”고 말할 수 없고, 한국어 능력 보존도 보장하지 않습니다.

폐쇄망과 data governance, provenance, supply chain, licensing 제약이 있는 환경에서 독립적으로 운용 가능한 한국 개발 foundation model 선택지에도 실용적인 관심이 있습니다. 그렇다고 국내 모델이 본질적으로 우월하다는 뜻은 아닙니다. 성능, 비용, 신뢰성, 라이선스, 유지보수성을 객관적으로 평가해야 합니다. 이 공개가 한국 개발 open model을 둘러싼 더 많은 커뮤니티 실험, 파생 작업, 공개 평가로 이어지기를 바랍니다. 결과물은 여전히 크고 실험적이며, 접근성 격차를 조금 줄이려는 시도이지 과장이나 benchmark 주장이 아닙니다.

## Pruning 설정

48개 레이어의 각 routed expert에 대해 다음 REAP saliency를 독립적으로 누적했습니다.

    mean(actual_topk_router_weight × expert_output_L2_norm)

레이어마다 saliency가 가장 낮은 routed expert 136개를 제거했습니다. 유지할 원본 expert ID는 오름차순으로 정렬한 뒤 재인덱싱했으며, 전체 목록은 <code>reap_metadata.json</code>에 기록되어 있습니다.

Solar Open 2의 routed expert는 ModuleList가 아니라 fused tensor로 저장됩니다. 따라서 각 레이어에서 **동일한 순서의 184개 keep index**를 아래 네 텐서에 모두 적용했습니다.

| 텐서 | 원본 shape |
|---|---:|
| experts.gate_up_proj | [320, 2560, 4096] |
| experts.down_proj | [320, 4096, 1280] |
| gate.weight | [320, 4096] |
| gate.e_score_correction_bias | [320] |

최종 설정은 <code>n_routed_experts = 184</code>입니다. <code>e_score_correction_bias</code>도 같은 순서로 slice해야 expert 재인덱싱 뒤 router 선택이 어긋나지 않습니다. Shared expert는 slice하거나 프루닝하지 않았습니다.

구현은 공식 [Cerebras REAP 저장소](https://github.com/CerebrasResearch/reap)와 [REAP 논문](https://arxiv.org/abs/2510.13999)을 따르고 이를 명시적으로 acknowledge합니다. 이 파생 모델을 위해 Solar 전용 fused-tensor 처리와 검증을 추가했습니다.

## Calibration 데이터 구성

Pruning saliency 계산에는 지난번 K-EXAONE-REAP 작업에 활용된 K-EXAONE-236B-REAP-calibration-mix를 사용했습니다. 전체 **16,780개 샘플**이며, 고정된 Solar tokenizer로 측정한 정확한 토큰 수는 **106,795,574개**, 측정된 샘플 최대 길이는 **269,944 tokens**입니다. 이 데이터는 saliency 측정에만 사용했으며 fine-tuning에는 사용하지 않았습니다.

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
| REAP 구현 | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

공개 전 audit은 유지된 routed-expert projection 가중치 **26,496개 전부**, 모든 router weight와 correction-bias tensor, shared-expert 가중치 **144개 전부**를 원본과 bit-exact하게 비교합니다. 또한 48개 keep-index map, 184E 설정, tensor shape, parameter count, 저장 전 finite-logit smoke inference를 확인합니다.

Upstage Transformers의 Solar Open 2 branch인 <code>v5.14.1-solar-open2</code>를 사용하십시오.

    uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_id = "Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

서빙 시에는 Upstage vLLM Solar fork/revision <code>v0.22.0-solar-open2</code>를 architecture reference로 사용하십시오. Solar reasoning 및 tool call에는 <code>--reasoning-parser solar_open2</code>, <code>--tool-call-parser solar_open2</code>, <code>--enable-auto-tool-choice</code>가 필요합니다. 이 파생 모델을 로드하기 전에 대상 build가 Solar Open 2 hybrid KDA/GQA를 지원하는지 확인해야 합니다.

## 제한사항

BF16 raw tensor payload는 274.898 GiB이므로 상당한 offload 없이는 128 GB GB10 unified memory에 들어가지 않습니다. Multi-accelerator 장비를 사용하거나 W4A16 버전을 고려하십시오. 이 카드에서는 downstream benchmark 결과를 주장하지 않으며, 별도 평가 없이 원본 250B 모델의 공개 성능을 이 파생 모델에 귀속해서는 안 됩니다.

Expert pruning은 routing balance, specialist coverage, factuality, 다국어 동작, tool use, long-context 동작을 바꿀 수 있습니다. 설정된 context length는 원본에서 상속했지만 pruning 후 장문 품질과 처리 성능은 독립적으로 재검증하지 않았습니다. 실제 배포 목적에 맞춰 안전성, 정확도, 지연시간, 메모리 사용량, 라이선스 적합성을 평가하십시오.

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
