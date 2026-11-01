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
- ream
- expert-merging
- expert-pruning
- text-generation
---
<!-- solar-ream-hub-card:v1 -->

# Solar-Open2-120B-A15B-REAM-148E-BF16

## Support my work

I work on making large language models practical on hardware they were never really designed to fit on — through mixed quantization, inference optimization, custom kernels, and serving experiments.

While much of the development happens on local hardware, calibration, profiling, and large-scale validation often require expensive on-demand GPUs.

Contributions help pay for that compute, storage, and testing infrastructure, so I can keep experimenting and publishing the results openly.

<a href="https://www.buymeacoffee.com/baekpica" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;"></a> <a href="https://github.com/sponsors/Baekpica" target="_blank"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Baekpica on GitHub" style="height: 60px !important;width: 217px !important;"></a>

## English

## Built with Solar

| Role | Model |
|---|---|
| Original / Hub `base_model` | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent / conversion input | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM result | Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16 |

## Overview

The model retains **148 routed experts and 1 shared expert in every MoE
layer**. Starting from the 184-expert REAP parent, REAM absorbs 36 routed
experts per layer into salient, similar centroid experts. The configured
top-k remains 8 routed experts per token, and the shared expert is unchanged.

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
| Raw tensor payload | 240,796,681,472 bytes (240.797 GB / 224.259 GiB) |

The 120B-A15B name is rounded; the exact total and active counts are above.
Active parameters are a compute characteristic, not checkpoint memory.

## REAM Method

The implementation adapts the official REAM method to Solar Open 2's packed
expert tensors and executes it sequentially over all 48 layers:

1. Select the 148 most salient centroid experts from the parent's audited
   per-layer REAP saliency.
2. Measure expert similarity as the mean of normalized raw-router-logit
   similarity and actually routed, real-top-k-weighted expert-output
   similarity.
3. Assign each non-centroid expert to a similar centroid using REAM's bounded
   pseudo-grouping rule, with at most 16 experts in a group.
4. Align intermediate neurons to the centroid with activation and weight
   features, rank-64 weight PCA, and Hungarian matching.
5. Merge aligned expert projections in FP32 using normalized REAP saliency,
   then cast once to BF16.
6. Slice the router weight and FP32 correction bias to the same sorted centroid
   order; keep the shared expert unchanged.

Solar stores routed experts as packed tensors:

| Tensor | Parent shape | Result shape |
|---|---:|---:|
| experts.gate_up_proj | [184, 2560, 4096] | [148, 2560, 4096] |
| experts.down_proj | [184, 4096, 1280] | [148, 4096, 1280] |
| gate.weight | [184, 4096] | [148, 4096] |
| gate.e_score_correction_bias | [184] | [148] |

The implementation uses exact sufficient statistics for the two similarity
families instead of retaining every token's logits and expert outputs. All
groups, centroid IDs, source IDs, normalized merge weights, and 1,280-element
neuron permutations are recorded in `ream_metadata.json`.

The Solar-specific implementation is published at
[Baekpica/solar-ream](https://github.com/Baekpica/solar-ream). It follows and
acknowledges the official
[SamsungSAILMontreal/ream](https://github.com/SamsungSAILMontreal/ream)
repository and paper. The parent pruning follows
[CerebrasResearch/reap](https://github.com/CerebrasResearch/reap).

## REAM Calibration

REAM used **3,072 deterministic windows of 512 tokens**, exactly **1,572,864
tokens**. The windows were sampled from the parent's audited
K-EXAONE-236B-REAP-calibration-mix with the pinned Solar tokenizer. They were
used only to measure layerwise routing, output, and activation statistics; the
model was not fine-tuned.

| Bucket | Windows |
|---|---:|
| code_en | 384 |
| mot_code | 384 |
| mot_math | 384 |
| mot_science | 288 |
| tool_en | 384 |
| agentic_swe | 192 |
| ko_instr | 576 |
| ko_tool | 288 |
| long_ctx | 144 |
| stress_256k | 48 |

The parent REAP saliency was measured over its full 16,780-sample,
106,795,574-token calibration mixture. REAM reuses that externally audited
saliency for centroid selection and merge weights, while the 3,072-window
subset supplies REAM similarity and neuron-alignment statistics.

## Provenance and Validation

| Component | Pinned revision |
|---|---|
| Original model upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| BF16 REAP parent | dea73266ec31a2453d115f6efc622e35d216ef81 |
| Official REAM implementation | 84a3030716a0059589e9d10e2ea049e32b76cfa6 |
| Official REAP implementation | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

The publication audit checks all 48 grouping results and similarity archives,
all neuron-permutation bijections and hashes, all checkpoint shapes and dtypes,
the exact parameter counts, every unchanged tensor against the parent, every
router/correction-bias centroid row, and a bit-exact GPU replay of every merged
projection. It also reloads the saved checkpoint and requires finite logits.

Use the Upstage Transformers Solar Open 2 branch:

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

For serving, use a Solar Open 2-compatible runtime. The Upstage vLLM Solar
branch `v0.22.0-solar-open2` is the architecture reference. Solar reasoning
and tool calls require the Solar Open 2 reasoning and tool-call parsers.

## Limitations

This release has not been downstream-benchmarked. Neither the original model's
scores nor the REAP parent's behavior should be attributed to this derivative
without evaluation. Expert merging can change routing balance, specialist
coverage, factuality, reasoning, multilingual behavior, tool use, and
long-context behavior. The configured context length is inherited, not
revalidated. Evaluate safety, accuracy, memory, latency, throughput, runtime
compatibility, and licensing for the intended deployment.

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

## Built with Solar

| 역할 | 모델 |
|---|---|
| 원본 / Hub `base_model` | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent / 변환 입력 | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM 결과 | Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16 |

## 모델 개요

각 MoE 레이어에서 **148개 routed expert와 1개 shared expert**를 유지합니다.
184E REAP parent에서 레이어마다 routed expert 36개를 saliency가 높고 유사한
centroid expert에 흡수·병합했습니다. 토큰당 top-k는 routed expert 8개로
유지하며 shared expert는 변경하지 않았습니다.

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
| 가중치 저장 | BF16, router correction bias는 FP32 |
| Raw tensor payload | 240,796,681,472 bytes (240.797 GB / 224.259 GiB) |

120B-A15B는 반올림한 이름이며 정확한 전체 및 활성 파라미터 수는 위 표와
같습니다. 활성 파라미터는 연산 특성이지 체크포인트 메모리 크기가 아닙니다.

## REAM 방법

공식 REAM 방법을 Solar Open 2의 packed expert tensor에 맞게 적용하고 48개
레이어를 순차 처리했습니다.

1. Parent의 audit된 레이어별 REAP saliency에서 상위 148개 expert를
   centroid로 선택합니다.
2. Raw router-logit similarity와 실제 선택된 real top-k 가중 expert-output
   similarity를 정규화해 평균합니다.
3. REAM bounded pseudo-grouping으로 non-centroid expert를 유사한 centroid에
   할당하며 group 크기는 최대 16입니다.
4. Activation feature, rank-64 weight PCA feature, Hungarian matching으로
   intermediate neuron을 centroid에 정렬합니다.
5. 정렬한 projection을 정규화한 REAP saliency로 FP32 누적한 뒤 한 번만
   BF16으로 변환합니다.
6. Router weight와 FP32 correction bias를 동일한 centroid 순서로 slice하고
   shared expert는 유지합니다.

Solar의 packed tensor는 184E에서 148E로 다음과 같이 바뀝니다.

| 텐서 | Parent shape | 결과 shape |
|---|---:|---:|
| experts.gate_up_proj | [184, 2560, 4096] | [148, 2560, 4096] |
| experts.down_proj | [184, 4096, 1280] | [148, 4096, 1280] |
| gate.weight | [184, 4096] | [148, 4096] |
| gate.e_score_correction_bias | [184] | [148] |

모든 token의 logit과 expert output을 보관하는 대신 두 similarity를 정확히
보존하는 sufficient statistics를 사용했습니다. 전체 group, centroid ID,
source ID, merge weight, 1,280개 neuron permutation은
`ream_metadata.json`에 기록했습니다.

Solar 전용 구현은
[Baekpica/solar-ream](https://github.com/Baekpica/solar-ream)에 공개합니다.
공식 [SamsungSAILMontreal/ream](https://github.com/SamsungSAILMontreal/ream)
저장소와 논문을 따르고 명시적으로 acknowledge하며, parent pruning은
[CerebrasResearch/reap](https://github.com/CerebrasResearch/reap)을 따릅니다.

## REAM Calibration

REAM에는 **512-token window 3,072개**, 정확히 **1,572,864 tokens**를
사용했습니다. Parent의 audit된 K-EXAONE-236B-REAP-calibration-mix에서
고정된 Solar tokenizer와 seed로 추출했습니다. Layerwise routing, output,
activation 통계 측정에만 사용했으며 fine-tuning은 하지 않았습니다.

| 버킷 | Window 수 |
|---|---:|
| code_en | 384 |
| mot_code | 384 |
| mot_math | 384 |
| mot_science | 288 |
| tool_en | 384 |
| agentic_swe | 192 |
| ko_instr | 576 |
| ko_tool | 288 |
| long_ctx | 144 |
| stress_256k | 48 |

Parent REAP saliency는 전체 16,780 samples, 106,795,574 tokens에서
측정됐습니다. REAM은 centroid 선택과 merge weight에 이 외부 audit
saliency를 재사용하고, 3,072-window subset은 similarity와 neuron alignment
통계를 제공합니다.

## 출처 및 검증

| 구성요소 | 고정 revision |
|---|---|
| 원본 모델 upstage/Solar-Open2-250B | 8d1dda5ad2af58207c65348d825772d2f4d72481 |
| BF16 REAP parent | dea73266ec31a2453d115f6efc622e35d216ef81 |
| 공식 REAM 구현 | 84a3030716a0059589e9d10e2ea049e32b76cfa6 |
| 공식 REAP 구현 | 1970473c51ca3caeb98c10392f15b3a08a672974 |
| Upstage Transformers Solar branch | ef5c37485091057070b36dd0620798f74988eb01 |
| Calibration dataset | 94e90afc261634a30384d3037d9021f1c997b286 |

공개 전 audit은 48개 grouping 결과와 similarity archive, 모든 neuron
permutation의 bijection과 hash, checkpoint shape/dtype, 정확한 파라미터 수,
parent와 같아야 하는 모든 tensor, router/correction-bias centroid row,
병합된 모든 projection의 bit-exact GPU replay를 검사합니다. 저장된
checkpoint를 다시 로드한 finite-logit 추론도 통과해야 합니다.

Upstage Transformers Solar Open 2 branch를 사용하십시오.

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

서빙에는 Solar Open 2 호환 runtime을 사용해야 합니다. Upstage vLLM Solar
branch `v0.22.0-solar-open2`가 architecture reference이며 Solar reasoning과
tool call에는 Solar Open 2 parser가 필요합니다.

## 제한사항

아직 downstream benchmark를 수행하지 않았습니다. 별도 평가 없이 원본
또는 REAP parent의 성능을 이 파생 모델에 귀속하면 안 됩니다. Expert
merging은 routing balance, specialist coverage, factuality, reasoning,
다국어 동작, tool use, long-context 동작을 바꿀 수 있습니다. 설정된
context length는 상속된 값이며 재검증 결과가 아닙니다. 실제 용도에 맞춰
안전성, 정확도, 메모리, 지연시간, 처리량, runtime 호환성, 라이선스를
평가하십시오.

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
`LICENSE`는 원본 모델의 라이선스를 정확히 복사한 파일입니다. 재배포와
사용은 Solar 명칭 및 attribution 요구사항을 포함한 해당 라이선스를
준수해야 합니다.
