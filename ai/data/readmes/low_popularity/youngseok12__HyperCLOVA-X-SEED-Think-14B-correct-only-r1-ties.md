---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- sft
- lora
- model-merging
- ties
- answer-first
---

# HyperCLOVA X SEED Think-14B Correct-Only TIES

`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B` pristine Base에서 세 AI Hub source를
각각 독립적으로 LoRA SFT한 뒤 TIES로 병합한 standalone BF16 모델입니다. 각 source의
1,000개 Base probe 중 Base가 정답을 맞힌 sample만 사용하여, source별 correct-only
학습 효과와 세 specialist의 병합 효과를 확인하기 위한 연구·평가용 모델입니다.

## Model information

- Base model: [`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B)
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Format: standalone BF16 `safetensors`; 별도 adapter가 필요하지 않습니다.
- Merge: TIES, weights `[1.0, 1.0, 1.0]`, density `0.5`
- Chat template: Base 원본 그대로 사용했으며 수정하지 않았습니다.

## Training data

세 adapter는 모두 pristine Base에서 독립적으로 학습했으며, 서로의 학습 데이터나
기존 mixture를 섞지 않았습니다. 아래 수는 각 1,000개 probe에서 correct로 판정된
실제 학습 sample 수입니다.

| Specialist | AI Hub dataset | Correct-only samples | Dataset URL |
|---|---|---:|---|
| K | 71875 필수의료 의학지식 QA | 557 | [AI Hub 71875](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875) |
| R | 71568 경제·스포츠 숫자 연산/수치 MRC | 131 | [AI Hub 71568](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568) |
| C | 71949 인과관계 기반 추론 | 535 | [AI Hub 71949](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949) |

총 1,223개 sample에 해당하는 세 correct-only adapter를 병합했습니다. 학습에는
public benchmark test 데이터, v0.21 mixture, 다른 fine-tuned checkpoint를 사용하지
않았습니다. 각 target은 기존 answer-first 형식을 유지했습니다.

## Training configuration

| | |
|---|---|
| Method | independent LoRA SFT, then TIES merge |
| Rank / alpha / dropout | `16 / 32 / 0.05` |
| Target modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |
| Learning rate | `5e-5`, cosine scheduler, warmup ratio `0.03` |
| Epochs | `1` |
| Batch | per-device `4`, gradient accumulation `4`, effective `16` |
| Sequence length | `4096`, packing disabled |
| Precision | BF16 |
| Objective | assistant-token-only causal LM cross entropy |
| Seeds | training/data `42/42` |
| Weight decay | `0` |

## Validation

The merged weights passed a full NaN/Inf sweep over 421 parameters. The model was loaded
and generated responses for 24 canonical smoke samples with zero empty outputs. This is a
load/generation smoke check; no benchmark score is reported in this repository.

## License and use

This derivative model is distributed under the Base model's HyperCLOVA X SEED 14B Think
Model License Agreement included in `LICENSE`. Please review that agreement and the
applicable AI Hub dataset terms before use or redistribution. The model is for research
