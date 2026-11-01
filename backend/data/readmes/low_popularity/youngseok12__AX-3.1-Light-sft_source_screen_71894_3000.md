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
- source-screening
- general-knowledge
- mathematics
- korean-culture
---

# A.X-3.1-Light SFT Source Screen 71894 (General, Mathematics, Korean Culture 3K)

이 모델은 `skt/A.X-3.1-Light`를 기반으로 AI Hub 71894 지식·지능 데이터의
일반지식, 수학, 한국문화·역사 영역만 사용해 한국어 질의응답 및 지시
수행을 LoRA 방식으로 1 epoch 지도학습한 모델입니다. 학습 후 LoRA
adapter를 base model에 병합한 BF16 standalone 전체 가중치 모델이므로
추론 시 별도의 adapter가 필요하지 않습니다. 다양한 길이의 설명형 답변을
포함한 연구용 모델이며, 생성 결과가 항상 정확하거나 완전하지 않을 수
있습니다.

## Model details

- Model name: `A.X-3.1-Light SFT Source Screen 71894 (General, Mathematics, Korean Culture 3K)`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning: LoRA supervised fine-tuning, merged into base weights
- Weight format: BF16 `safetensors`
- Architecture: unchanged Llama causal language model architecture
- Chat template: bundled A.X tokenizer chat template
- Custom model code: none; standard Transformers/vLLM loading is intended

## Training data

Training used only AI Hub dataset **71894, 지식·지능 데이터**. The training
split contains 3,000 selected examples and the separate development split
contains 300 examples. No v0.21 mixture, other AI Hub dataset, public benchmark
question, benchmark answer, or evaluation artifact was used as SFT data or
included in this repository.

| Domain | Training examples |
|---|---:|
| General knowledge | 1,000 |
| Mathematics | 1,000 |
| Korean culture and history | 1,000 |
| **Total** | **3,000** |

The output contract is answer-first: the key answer is presented first and a
short rationale may follow. The data were serialized with a 2,048-token maximum
and the training summary reports zero runtime target truncation. The applicable
AI Hub terms of use remain in force. [AI Hub dataset 71894](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71894)

## Training configuration

- Epochs: 1
- Optimizer steps: 375
- Maximum sequence length: 2,048
- Precision: BF16
- Per-device batch size: 1
- Gradient accumulation: 8 (effective batch size 8)
- Learning rate: `5e-5`
- Scheduler: cosine; warmup ratio `0.03` (11 steps)
- Weight decay: `0.01`
- Random seed: 42
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Objective: assistant-token causal language-model cross entropy
- Mean target length: 352.38 tokens; median: 255 tokens
- Total supervised target tokens: 1,057,132
- Final training loss: `1.0957567635`

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_source_screen_71894_3000"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

Use the bundled tokenizer chat template for conversational inference. The
repository is a merged full model and does not require PEFT adapter loading.

## Limitations and license

This model is derived from the Apache-2.0 licensed `skt/A.X-3.1-Light` model;
the base model notices and SK Telecom trademark terms also apply. AI Hub terms
apply to the source dataset. See [`LICENSE`](LICENSE) and the base model
repository for the applicable terms.

The model can produce incorrect, incomplete, biased, or poorly formatted
answers. It should not be used as the sole basis for legal, educational,
financial, cultural, or other high-impact decisions.
