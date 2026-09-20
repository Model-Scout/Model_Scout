---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
base_model: skt/A.X-3.1-Light
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- instruction-tuning
- merged-model
---

# A.X-3.1-Light SFT A1 (Paper-guided 4K)

This is a full BF16 model obtained by merging a LoRA SFT adapter into
[`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light). No separate
adapter is required for inference.

## Training

- Method: LoRA supervised fine-tuning with assistant-only loss
- Data: 4,000 selected examples from five AI Hub sources
- Selection: A1 paper-guided selection with source/context/document balancing
- Base model: `skt/A.X-3.1-Light`
- Precision: BF16
- Epochs: 1
- Learning rate: `5e-5`
- Maximum sequence length: 2,048
- Effective batch size: 8
- Seed: 42
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`

### AI Hub sources

The source data are referenced by dataset ID only; no benchmark data or
training examples are included in this repository. Users must follow the
applicable AI Hub terms of use.

- 569 — 행정 문서 대상 기계독해: [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=569)
- 71610 — 금융·법률 문서 기계독해: [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71610)
- 71857 — 국어 교과 지문형 문제: [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71857)
- 71874 — 전문 의학지식: [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71874)
- 71949 — 인과 관계 기반 추론: [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949)

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_A1_paperguided4k"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

## Local evaluation

These are local proxy results on the KDS canonical suite, not official K-AI
leaderboard scores. The evaluation used the text-only HLE subset and reported
Original MuSR separately in the suite.

| Probe | Parsed accuracy | Strict accuracy | Format error | Parse fail | Generation errors |
|---|---:|---:|---:|---:|---:|
| B1 constrained | 42.01% | 42.01% | 0.42% | 0.05% | 0 |
| Free generation | 35.60% | 20.66% | 57.48% | 13.44% | 0 |

The model is derived from the Apache-2.0 licensed base model. See the
[`LICENSE`](LICENSE) file and the base model's license for terms and notices.

## Limitations

This model was fine-tuned for Korean text-generation and benchmark-style
question answering. It may produce incorrect or poorly formatted answers and
should not be used as the sole basis for medical, legal, financial, or other
high-impact decisions.
