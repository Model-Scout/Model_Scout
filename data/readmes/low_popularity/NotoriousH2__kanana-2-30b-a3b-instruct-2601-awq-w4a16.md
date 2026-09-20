---
license: apache-2.0
base_model: kakaocorp/kanana-2-30b-a3b-instruct-2601
tags:
  - awq
  - quantized
  - 4-bit
  - vllm
  - moe
  - korean
library_name: transformers
pipeline_tag: text-generation
language:
  - ko
  - en
---

# Kanana-2-30B-A3B-Instruct AWQ (W4A16)

This is the AWQ quantized version of [kakaocorp/kanana-2-30b-a3b-instruct-2601](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601).

## Model Description

- **Base Model**: kakaocorp/kanana-2-30b-a3b-instruct-2601
- **Quantization Method**: AWQ (Activation-aware Weight Quantization)
- **Quantization Scheme**: W4A16 (4-bit weights, 16-bit activations)
- **Calibration Dataset**: [ChuGyouk/Asan-AMC-Healthinfo](https://huggingface.co/datasets/ChuGyouk/Asan-AMC-Healthinfo)
- **Calibration Samples**: 64
- **Max Sequence Length**: 512

## Quantization Details

This model was quantized using [LLM Compressor](https://github.com/vllm-project/llm-compressor) with the following configuration:

- **Ignored Layers** (not quantized):
  - `lm_head`: Output layer
  - `mlp.gate`: MoE router gates
  - `mlp.shared_expert_gate`: Shared expert gates

```python
from llmcompressor.modifiers.awq import AWQModifier

recipe = [
    AWQModifier(
        ignore=["lm_head", "re:.*mlp.gate$", "re:.*mlp.shared_expert_gate$"],
        scheme="W4A16",
        targets=["Linear"],
    ),
]
```

## Usage

### With vLLM (Recommended)

```python
from vllm import LLM, SamplingParams

model = LLM(
    model="NotoriousH2/kanana-2-30b-a3b-instruct-2601-awq-w4a16",
    trust_remote_code=True,
)

sampling_params = SamplingParams(temperature=0.7, max_tokens=512)
output = model.generate("고혈압 환자의 식이요법에 대해 설명해주세요.", sampling_params)
print(output[0].outputs[0].text)
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "NotoriousH2/kanana-2-30b-a3b-instruct-2601-awq-w4a16",
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "NotoriousH2/kanana-2-30b-a3b-instruct-2601-awq-w4a16",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "고혈압 환자의 식이요법에 대해 설명해주세요."}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    return_tensors="pt",
    add_generation_prompt=True,
).to(model.device)

output = model.generate(input_ids, max_new_tokens=512)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Acknowledgements

- Original model by [Kakao Corp](https://huggingface.co/kakaocorp)
- Quantization powered by [LLM Compressor](https://github.com/vllm-project/llm-compressor)
