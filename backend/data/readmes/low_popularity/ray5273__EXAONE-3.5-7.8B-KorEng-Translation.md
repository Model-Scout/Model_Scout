---
license: other
license_name: exaone
license_link: LICENSE
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
tags:
  - exaone
  - korean
  - english
  - translation
  - fine-tuned
  - merged
language:
  - ko
  - en
library_name: transformers
---

# EXAONE 3.5 7.8B Korean-English Translation

This model is [LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct) fine-tuned with LoRA and merged for Korean-English translation tasks.

## Model Details

- **Base Model**: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **LoRA Config**:
  - Rank (r): 64
  - Alpha: 128
  - Dropout: 0.05
  - Target Modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "ray5273/EXAONE-3.5-7.8B-KorEng-Translation",
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "ray5273/EXAONE-3.5-7.8B-KorEng-Translation",
    trust_remote_code=True
)

messages = [
    {"role": "system", "content": "You are a helpful translator."},
    {"role": "user", "content": "Translate the following to English: 안녕하세요, 만나서 반갑습니다."}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

output = model.generate(input_ids, max_new_tokens=256)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## License

This model follows the EXAONE AI Model License Agreement 1.1 - NC.
See the [EXAONE License](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct/blob/main/LICENSE) for details.
