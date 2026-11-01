---
inference: false
library_name: transformers
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
extra_gated_prompt: "By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license) and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s [Privacy Policy](https://cohere.com/privacy). You’ll receive email updates about C4AI and Cohere research, events, products and services. You can unsubscribe at any time."
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
tags:
  - quantized
  - 4bit
  - 8bit
  - multi-gpu
  - nlp
  - conversational-ai
  - rag
  - tool-use
  - code-generation
  - enterprise
model_name: C4AI Command A - Quantized
base_model: CohereForAI/c4ai-command-a-03-2025
model_size: 111B
context_length: 256K
developers:
  - Cohere
  - Cohere For AI
contact: info@for.ai
---

# C4AI Command A - Quantized Models

This repository contains quantized versions of the **C4AI Command A** model, an open weights research release by [Cohere](https://cohere.com/) and [Cohere For AI](https://cohere.for.ai/). The original model is a 111 billion parameter language model optimized for enterprise use cases, excelling in agentic, multilingual, and retrieval-augmented generation (RAG) tasks while being deployable on minimal hardware (e.g., two GPUs). Here, we provide multiple quantized variants to further reduce memory footprint and enhance deployment flexibility across various hardware setups, including multi-GPU environments.

For details on the original model, refer to the [official model card](#model-card-for-c4ai-command-a) below.

---

## Quantized Models

We have quantized the original `CohereForAI/c4ai-command-a-03-2025` model using the `bitsandbytes` library with various configurations to balance performance, memory efficiency, and accuracy. Below are the available quantized versions:

| Quantization Type         | Description                                                                 | Compute Dtype | Double Quantization | Notes                                      |
|---------------------------|-----------------------------------------------------------------------------|---------------|---------------------|--------------------------------------------|
| `4bit_nf4_double`         | 4-bit quantization with `nf4` (Normal Float 4)                              | `bfloat16`    | Yes                 | High precision with reduced memory usage  |
| `4bit_fp4`               | 4-bit quantization with `fp4` (Float Point 4)                              | `bfloat16`    | No                  | Lightweight, slightly less precise        |
| `8bit_standard`          | Standard 8-bit quantization                                                | `bfloat16`    | N/A                 | Balanced memory and accuracy              |
| `8bit_mixed`             | 8-bit quantization with mixed precision and CPU offloading capability      | `float16`     | N/A                 | Flexible for constrained environments     |
| `4bit_nf4_no_double`     | 4-bit quantization with `nf4`, no double quantization                      | `bfloat16`    | No                  | Minimal memory footprint                  |

These models are optimized for multi-GPU deployment using the `accelerate` library, ensuring efficient distribution across available GPUs. Each variant is hosted in its own sub-repository:

- `Tonic/c4ai-command-a-03-2025-4bit_nf4_double`
- `Tonic/c4ai-command-a-03-2025-4bit_fp4`
- `Tonic/c4ai-command-a-03-2025-8bit_standard`
- `Tonic/c4ai-command-a-03-2025-8bit_mixed`
- `Tonic/c4ai-command-a-03-2025-4bit_nf4_no_double`

---

## Usage

To use a quantized model, install the required dependencies and load the desired variant as shown below. Multi-GPU support is enabled via `accelerate`.

### Installation

```bash
pip install transformers bitsandbytes accelerate torch huggingface_hub
```

### Example: Loading and Generating Text

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator

# Initialize Accelerator for multi-GPU support
accelerator = Accelerator()

# Specify the quantized model ID
model_id = "Tonic/c4ai-command-a-03-2025-4bit_nf4_double"  # Replace with desired variant
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.bfloat16)

# Prepare model for multi-GPU
model = accelerator.prepare(model)

# Format message with chat template
messages = [{"role": "user", "content": "Hello, how are you?"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(accelerator.device)

# Generate text
gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
)
gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

### Notes
- **Device Mapping**: `device_map="auto"` ensures the model is distributed across all available GPUs.
- **Compute Dtype**: Adjust `torch_dtype` (e.g., `torch.bfloat16` or `torch.float16`) based on your hardware and the quantization type.
- **Memory**: Quantized models significantly reduce VRAM requirements compared to the original 111B parameter model, making them suitable for deployment on consumer-grade GPUs.

---

## Quantization Details

The quantization process leverages `bitsandbytes` with the following configurations:
- **4-bit Variants**: Use `nf4` or `fp4` quantization types, with optional double quantization for improved precision.
- **8-bit Variants**: Offer standard or mixed precision options, with the latter supporting CPU offloading for additional flexibility.
- **Multi-GPU Optimization**: The `accelerate` library handles model sharding and distribution, allowing deployment on systems with multiple GPUs.

For the exact quantization script, see [this Gist](#) (replace with a link to your script if hosted).

---

## Model Card for C4AI Command A

Below is the original model card for `C4AI Command A`, adapted for this repository.

---

### Model Summary

C4AI Command A is an open weights research release of a 111 billion parameter model optimized for demanding enterprises that require fast, secure, and high-quality AI. Compared to other leading proprietary and open-weights models, Command A delivers maximum performance with minimum hardware costs, excelling on business-critical agentic and multilingual tasks while being deployable on just two GPUs.

- **Developed by**: [Cohere](https://cohere.com/) and [Cohere For AI](https://cohere.for.ai/)
- **Point of Contact**: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)
- **License**: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- **Model**: `c4ai-command-a-03-2025`
- **Model Size**: 111 billion parameters
- **Context Length**: 256K

**Try C4AI Command A**

You can try the original model before downloading weights in the hosted [Hugging Face Space](https://cohereforai-c4ai-command.hf.space/models/command-a-03-2025).

---

### Model Details

- **Input**: Text only
- **Output**: Text only
- **Model Architecture**: Auto-regressive language model with an optimized transformer architecture, featuring sliding window attention (window size 4096) with RoPE, and a global attention layer without positional embeddings.
- **Languages**: Supports 23 languages including English, French, Spanish, German, Japanese, Chinese, Arabic, and more (see full list in the original model card).
- **Context Length**: 256K

---

### Chat Capabilities

Command A is configured as a conversational model by default with two safety modes: **contextual** (default, fewer constraints) and **strict** (avoids sensitive topics). See [Command A prompt format docs](https://docs.cohere.com/docs/command-a-hf) for details.

---

### RAG Capabilities

Command A excels in Retrieval Augmented Generation (RAG) tasks. Use the `apply_chat_template` method with document snippets for RAG functionality. Example:

```python
conversation = [{"role": "user", "content": "What has Man always dreamed of?"}]
documents = [
    {"heading": "The Moon", "body": "Man has always dreamed of destroying the moon..."},
    {"heading": "Love", "body": "Man's dream has always been to find love..."}
]
input_ids = tokenizer.apply_chat_template(conversation, documents=documents, tokenize=True, add_generation_prompt=True, return_tensors="pt")
```

---

### Tool Use Capabilities

Command A supports conversational tool use with JSON schema-based tool descriptions. See the [tool use example](#tool-use-example-click-to-expand) in the original model card for implementation details.

---

### Code Capabilities

The model performs well on enterprise-relevant code tasks (e.g., SQL generation, code translation). Use low temperature or greedy decoding for optimal code generation.

---

## Terms of Use

This model is released under a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) license for non-commercial use only, adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy). For commercial inquiries, contact [Cohere’s Sales team](https://cohere.com/contact-sales).

---

## Contact

For issues or questions, reach out to `info@for.ai`.

---

