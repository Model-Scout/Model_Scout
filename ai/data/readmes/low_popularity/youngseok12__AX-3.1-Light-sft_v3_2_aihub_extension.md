---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
base_model: skt/A.X-3.1-Light
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- instruction-tuning
- supervised-fine-tuning
- merged-model
- answer-first
---

# A.X-3.1-Light SFT v3.2 AI Hub Extension

이 모델은 `skt/A.X-3.1-Light`를 기반으로 한국어 질의응답 및 지시 수행
데이터를 1 epoch LoRA SFT한 뒤 adapter를 base model에 병합한 BF16 전체
가중치 모델입니다. 답변형·객관식 문제에서 첫 문장 또는 첫 부분에 핵심
답을 제시하고, 필요한 경우 짧은 근거를 덧붙이도록 학습했습니다. 연구 및
평가용 모델이며, 생성 결과가 부정확할 수 있으므로 의료·법률·재정 등
고위험 의사결정의 유일한 근거로 사용해서는 안 됩니다.

## Model information

- Model name: `A.X-3.1-Light SFT v3.2 AI Hub Extension`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning method: LoRA supervised fine-tuning, merged for inference
- Model format: standalone BF16 `safetensors`; no separate adapter is required
- Intended use: Korean text generation, instruction following, and research evaluation

## Training

- Training data file: `format_sft_answer_first_extension_13801.jsonl`
- Selected rows: 13,801
- Serialized training examples: 13,793 (8 rows skipped during example construction)
- Epochs: 1
- Maximum sequence length: 2,048
- Precision: BF16
- Learning rate: `5e-5`
- Effective batch size: 8
- Scheduler: linear; warmup steps: 0
- Weight decay: 0
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Objective: assistant-token causal language-model cross entropy
- Training loss: `1.0445830774`
- Training runtime: 4,646.3862 seconds

The target contract is answer-first: a compact answer is given first, followed
by at most one short rationale when a rationale is available. New AI Hub
candidates were filtered to fit the base model with a 2,048-token maximum.

## Training data

The final training mixture contains 5,801 examples inherited from the v0.21
answer-first core and 8,000 newly selected examples from three AI Hub sources.
The source dataset IDs and selected counts are listed below. The source data,
benchmark questions, answers, and evaluation artifacts are not included in this
repository. Users must follow the applicable AI Hub terms of use.

| AI Hub dataset | Description | Selected examples |
|---|---|---:|
| 569 | 행정 문서 대상 기계독해 데이터 / VL_multiple_choice | 2,787 |
| 71610 | 금융·법률 문서 기계독해 데이터 / VL_4 다지선다 | 644 |
| 71857 | 국어 교과 지문형 문제 데이터 | 597 |
| 71874 | 전문 의학지식 데이터 | 823 |
| 71890 | AI 파운데이션 모델 LLM/LAM 사후학습용 데이터 | 3,000 |
| 71894 | 지식·지능 데이터 | 3,000 |
| 71904 | 생각과정 씨앗 학습·검증 데이터 | 2,000 |
| 71949 | 인과관계 기반 추론 데이터(업사이클링) / label_json | 950 |
| **Total** |  | **13,801** |

The new-data selection was deterministic with seed `20260831`. It covered law,
science/technology, mathematics, general knowledge, Korean culture/history,
math, science, and social studies categories according to the selection
manifest used for this run. Prompt-level duplicate checking found no duplicate
prompts or replacements; inherited duplicate SFT IDs may remain as recorded in
the manifest.

AI Hub references:

- [Dataset 569](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=569)
- [Dataset 71610](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71610)
- [Dataset 71857](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71857)
- [Dataset 71874](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71874)
- [Dataset 71890](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71890)
- [Dataset 71894](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71894)
- [Dataset 71904](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71904)
- [Dataset 71949](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949)

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_v3_2_aihub_extension"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

The bundled tokenizer includes the chat template used by the base model. For
chat-style inference, use `tokenizer.apply_chat_template` and keep the prompt
format consistent with the intended conversational interface.

## Reproducibility

- Local adapter checkpoint: `/home/youngseok3/KDS/checkpoints/aihub_extension_20260831_gpu3`
- Local merged output: `/home/youngseok3/KDS/submission/AX-3.1-Light-sft_v3_2_aihub_extension-merged`
- Dataset selection manifest: `data/processed/aihub_extension_20260831/selection_manifest.json`
- Base model revision and merge details are recorded in `kds_merge_info.json`.

## Limitations and license

This model is derived from the Apache-2.0 licensed `skt/A.X-3.1-Light` model.
The base model's notices and SK Telecom trademark terms also apply. AI Hub
dataset terms apply to the source data. See [`LICENSE`](LICENSE) and the base
model repository for the applicable terms.

The model may produce incorrect, incomplete, biased, or poorly formatted
answers. It has not been validated as a professional medical, legal, financial,
or safety-critical system.
