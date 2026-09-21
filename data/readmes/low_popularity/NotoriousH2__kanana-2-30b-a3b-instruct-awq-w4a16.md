---
license: apache-2.0
base_model: kakaocorp/kanana-2-30b-a3b-instruct
tags:
  - awq
  - quantized
  - 4bit
  - korean
  - moe
  - medical
library_name: transformers
language:
  - ko
  - en
---

# Kanana-2-30B-A3B-Instruct AWQ (W4A16)

[kakaocorp/kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct) 모델을 AWQ 방식으로 4비트 양자화한 버전입니다.
`compressed-tensors==0.13.0` 버전에서 제작되었습니다.

## Model Details

| Attribute | Value |
|-----------|-------|
| Base Model | kakaocorp/kanana-2-30b-a3b-instruct |
| Quantization | AWQ (W4A16) |
| Bits | 4-bit weights, 16-bit activations |
| Calibration Dataset | [ChuGyouk/Asan-AMC-Healthinfo](https://huggingface.co/datasets/ChuGyouk/Asan-AMC-Healthinfo) |
| Quantization Tool | [llmcompressor](https://github.com/vllm-project/llm-compressor) |

## Quantization Config

```python
AWQModifier(
    ignore=["lm_head", "re:.*mlp.gate$", "re:.*mlp.shared_expert_gate$"],
    scheme="W4A16",
    targets=["Linear"],
)
```

- `lm_head`: 출력 레이어는 양자화 제외
- `mlp.gate`: MoE 라우터 게이트는 양자화 제외
- `shared_expert_gate`: 공유 전문가 게이트는 양자화 제외

## Installation

```bash
pip install compressed-tensors==0.13.0
```

호환성을 위해 위 버전 설치를 권장합니다.

## Usage

### With vLLM (Recommended)

```python
from vllm import LLM, SamplingParams

model = LLM(model="NotoriousH2/kanana-awq-w4a16")
sampling_params = SamplingParams(temperature=0.7, max_tokens=512)

prompt = "고혈압 환자의 식이요법에 대해 설명해주세요."
output = model.generate([prompt], sampling_params)
print(output[0].outputs[0].text)
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "NotoriousH2/kanana-awq-w4a16",
    torch_dtype="auto",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("NotoriousH2/kanana-awq-w4a16")

messages = [{"role": "user", "content": "고혈압 환자의 식이요법에 대해 설명해주세요."}]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
output = model.generate(input_ids, max_new_tokens=512)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## License

This model inherits the license from the base model. Please refer to [kakaocorp/kanana-2-30b-a3b-instruct](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct) for license details.
