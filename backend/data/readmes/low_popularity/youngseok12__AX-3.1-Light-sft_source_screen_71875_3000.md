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
- medical-qa
---

# A.X-3.1-Light SFT Source Screen 71875 (Essential Medical 3K)

이 모델은 `skt/A.X-3.1-Light`를 기반으로 AI Hub 71875 필수의료 의학지식
데이터만 사용해 한국어 질의응답을 LoRA 방식으로 1 epoch 지도학습한
모델입니다. 학습이 끝난 뒤 LoRA adapter를 base model에 병합한 BF16
standalone 전체 가중치 모델이므로 추론 시 별도의 adapter가 필요하지
않습니다. 연구 및 통제된 평가용 모델이며, 의료 관련 답변을 포함한 모든
생성 결과는 오류가 있을 수 있어 전문적인 판단을 대체할 수 없습니다.

## Model details

- Model name: `A.X-3.1-Light SFT Source Screen 71875 (Essential Medical 3K)`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning: LoRA supervised fine-tuning, merged into base weights
- Weight format: BF16 `safetensors`
- Architecture: unchanged Llama causal language model architecture
- Chat template: bundled A.X tokenizer chat template
- Custom model code: none; standard Transformers/vLLM loading is intended

## Training data

Training used only AI Hub dataset **71875, 필수의료 의학지식 데이터**. The
training split contains 3,000 selected examples and the separate development
split contains 300 examples. No v0.21 mixture, other AI Hub dataset, public
benchmark question, benchmark answer, or evaluation artifact was used as SFT
data or included in this repository.

| Source | Training examples |
|---|---:|
| Category 14 | 895 |
| Category 15 | 895 |
| Category 16 | 315 |
| Category 17 | 895 |
| **Total** | **3,000** |

The output contract is answer-first (`정답: ...`). Depending on the source
question, the target is a label, number, short answer, or concise explanation.
Examples over 2,048 chat-template tokens were excluded rather than truncated;
the training summary reports zero runtime truncation. The applicable AI Hub
terms of use remain in force. [AI Hub dataset 71875](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875)

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
- Mean target length: 10.23 tokens; median: 5 tokens
- Total supervised target tokens: 30,703
- Final training loss: `0.5942968483`

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_source_screen_71875_3000"
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
answers. It has not been validated as a medical device or professional medical
advice system and must not be used as the sole basis for clinical decisions.
