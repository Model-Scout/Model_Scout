---
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - ja
  - ko
  - zh
  - ar
  - el
  - fa
  - pl
  - id
  - cs
  - he
  - hi
  - nl
  - ro
  - ru
  - tr
  - uk
  - vi
license: cc-by-nc-4.0
library_name: transformers
tags:
- cohere
- pytorch
- gptq
model_name: aya-expanse-32b-gptq-4bit
base_model: CohereForAI/aya-expanse-32b
inference: false
model_creator: Cohere For AI
pipeline_tag: text-generation
quantized_by: kevinbazira
---

# aya-expanse-32b-gptq-4bit

This repository contains a quantized version of the `CohereForAI/aya-expanse-32b` model using the [GPTQ](https://huggingface.co/docs/transformers/en/quantization/gptq) method in 4-bit precision.

## Model Summary

- **Quantized Model**: [kevinbazira/aya-expanse-32b-gptq-4bit](https://huggingface.co/kevinbazira/aya-expanse-32b-gptq-4bit)
- **Quantization Method**: [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/pdf/2210.17323)
- **Dataset**: [c4](https://huggingface.co/datasets/legacy-datasets/c4)
- **Precision**: 4-bit
- **Original Model**: [CohereForAI/aya-expanse-32b](https://huggingface.co/CohereForAI/aya-expanse-32b)

## How to Use the Quantized Model

### 1. Install the necessary packages

Before using the quantized model, please ensure your environment has:
- [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ)

### 2. Run inference
Load and use the quantized model as shown below in Python:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set up device
device = torch.device('cuda:1') # Remember to use the correct device here

# Load model and tokenizer
model_name = "kevinbazira/aya-expanse-32b-gptq-4bit"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map={"": device.index}
)

# Prepare input
# https://huggingface.co/docs/transformers/en/pad_truncation
input_text = "Add your prompt here."
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding="max_length", max_length=64)
inputs = {key: value.to(device) for key, value in inputs.items()}

# Perform text generation 
# https://huggingface.co/docs/transformers/en/main_classes/text_generation
outputs = model.generate(
    **inputs,
    num_return_sequences=1,
    min_new_tokens=64,
    max_new_tokens=64,
    do_sample=False,
    use_cache=True,
    num_beams=1
)

# Decode and print the output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## More Information

- **Original Model**: For details about the original model's architecture, training dataset, and performance, please visit the CohereForAI [aya-expanse-32b model card](https://huggingface.co/CohereForAI/aya-expanse-32b).
- **Support or inquiries**: If you run into any issues or have questions about the quantized model, feel free to reach me via email: `contact@kevinbazira.com`. I'll be happy to help!
