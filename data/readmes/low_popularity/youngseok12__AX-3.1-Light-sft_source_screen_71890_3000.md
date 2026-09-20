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
- law
- mathematics
- science
---

# A.X-3.1-Light SFT Source Screen 71890 (Law, Science, Mathematics 3K)

이 모델은 `skt/A.X-3.1-Light`를 기반으로 AI Hub 71890의 법·세무·행정,
과학·기술, 수학 문제 및 풀이 데이터를 사용해 한국어 질의응답과 지시
수행을 LoRA 방식으로 1 epoch 지도학습한 모델입니다. 학습 후 LoRA
adapter를 base model에 병합한 BF16 standalone 전체 가중치 모델이므로
추론 시 별도의 adapter가 필요하지 않습니다. 긴 설명형 응답이 포함된
학습 데이터의 특성상 답변의 사실성·간결성·형식이 항상 보장되지 않으며,
연구 및 평가 목적으로만 사용해야 합니다.

## Model details

- Model name: `A.X-3.1-Light SFT Source Screen 71890 (Law, Science, Mathematics 3K)`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning: LoRA supervised fine-tuning, merged into base weights
- Weight format: BF16 `safetensors`
- Architecture: unchanged Llama causal language model architecture
- Chat template: bundled A.X tokenizer chat template
- Custom model code: none; standard Transformers/vLLM loading is intended

## Training data

Training used only AI Hub dataset **71890, AI 파운데이션 모델 LLM/LAM
사후학습용 데이터**. The training split contains 3,000 selected examples and
the separate development split contains 300 examples. No v0.21 mixture, other
AI Hub dataset, public benchmark question, benchmark answer, or evaluation
artifact was used as SFT data or included in this repository.

| Domain | Training examples | Main subjects |
|---|---:|---|
| 법·세무·행정 관련 질의/지시 응답 | 1,000 | 세법 394, 행정법 384, 일반법 222 |
| 과학·기술 관련 질의/지시 응답 | 1,000 | 생명과학·화학·제조공학·물리·지구과학 각 200 |
| 수학 문제 및 풀이 | 1,000 | 미적분·수론·대수·조합론 각 250 |
| **Total** | **3,000** |  |

The output contract is answer-first: the core answer is presented first and a
short rationale may follow. New examples were selected and filtered for a
2,048-token maximum without runtime target truncation. The applicable AI Hub
terms of use remain in force. [AI Hub dataset 71890](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71890)

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
- Mean target length: 373.24 tokens; median: 369 tokens
- Total supervised target tokens: 1,119,712
- Final training loss: `1.2575108846`

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_source_screen_71890_3000"
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
answers. It must not be used as the sole basis for legal, tax, administrative,
scientific, mathematical, financial, or other high-impact decisions.
