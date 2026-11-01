---
license: other
license_name: hyperclovax-seed
license_link: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B/blob/main/LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-32B
tags:
  - awq
  - quantized
  - 4bit
  - korean
  - vlm
  - medical
library_name: transformers
language:
  - ko
  - en
---

# HyperCLOVAX-SEED-Think-32B AWQ (W4A16)

[naver-hyperclovax/HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B) 모델을 AWQ 방식으로 4비트 양자화한 버전입니다.
`compressed-tensors==0.13.0` 버전에서 제작되었습니다.

## Model Details

| Attribute | Value |
|-----------|-------|
| Base Model | naver-hyperclovax/HyperCLOVAX-SEED-Think-32B |
| Architecture | HCXVisionForCausalLM (VLM) |
| Quantization | AWQ (W4A16) |
| Bits | 4-bit weights, 16-bit activations |
| Calibration Dataset | [ChuGyouk/Asan-AMC-Healthinfo](https://huggingface.co/datasets/ChuGyouk/Asan-AMC-Healthinfo) |
| Quantization Tool | [llmcompressor](https://github.com/vllm-project/llm-compressor) |

## Quantization Config

```python
# HyperCLOVAX VLM 모델에 맞는 커스텀 AWQ 매핑
hyperclovax_mappings = [
    AWQMapping(
        smooth_layer="re:.*language_model.*layers\\.\\d+\\.input_layernorm$",
        balance_layers=[
            "re:.*language_model.*layers\\.\\d+\\.self_attn\\.q_proj$",
            "re:.*language_model.*layers\\.\\d+\\.self_attn\\.k_proj$",
            "re:.*language_model.*layers\\.\\d+\\.self_attn\\.v_proj$",
        ],
    ),
    AWQMapping(
        smooth_layer="re:.*language_model.*layers\\.\\d+\\.post_attention_layernorm$",
        balance_layers=[
            "re:.*language_model.*layers\\.\\d+\\.mlp\\.gate_proj$",
            "re:.*language_model.*layers\\.\\d+\\.mlp\\.up_proj$",
        ],
    ),
    AWQMapping(
        smooth_layer="re:.*language_model.*layers\\.\\d+\\.mlp\\.up_proj$",
        balance_layers=["re:.*language_model.*layers\\.\\d+\\.mlp\\.down_proj$"],
    ),
]

AWQModifier(
    ignore=["lm_head", "re:.*vision_model.*", "re:.*visual.*"],
    scheme="W4A16",
    targets=["Linear"],
    mappings=hyperclovax_mappings,
)
```

- `lm_head`: 출력 레이어는 양자화 제외
- `vision_model`, `visual`: 비전 모델 부분은 양자화 제외

## Installation

```bash
pip install compressed-tensors==0.13.0
```

호환성을 위해 위 버전 설치를 권장합니다.

## Usage

### With vLLM (Recommended)

```python
from vllm import LLM, SamplingParams

model = LLM(
    model="NotoriousH2/HyperCLOVAX-SEED-Think-32B-awq-w4a16",
    trust_remote_code=True,
)
sampling_params = SamplingParams(temperature=0.7, max_tokens=512)

prompt = "고혈압 환자의 식이요법에 대해 설명해주세요."
output = model.generate([prompt], sampling_params)
print(output[0].outputs[0].text)
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "NotoriousH2/HyperCLOVAX-SEED-Think-32B-awq-w4a16",
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "NotoriousH2/HyperCLOVAX-SEED-Think-32B-awq-w4a16",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "고혈압 환자의 식이요법에 대해 설명해주세요."}]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
output = model.generate(input_ids, max_new_tokens=512)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## License

This model inherits the license from the base model. Please refer to [naver-hyperclovax/HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B) for license details.
