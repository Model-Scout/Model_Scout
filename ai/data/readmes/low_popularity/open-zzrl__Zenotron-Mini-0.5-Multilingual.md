---
language:
- ru
- en
- fr
- ko
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
tags:
- text-generation
- conversational
- moe
- zenotron
- ko
- ru
- en
- fr
pipeline_tag: text-generation
---

# 🧠 Zenotron-Mini-v0.5-Multilingual

![](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/LKJBKn02BwueQQK4xseIk.png)

**Zenotron-Mini-v0.5-Multilingual** is a compact, highly efficient multilingual language model developed by **[Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)**. 

This is a preview release (v0.5) post-trained on 4 languages (Russian, English, French, and Korean). It demonstrates strong cross-lingual transfer capabilities and improved logical reasoning without catastrophic forgetting.

## 📌 Model Details
*   **Base Model:** Qwen3.6-35B-A3B
*   **Active Parameters:** ~3B (efficient inference)
*   **Total Parameters:** 35B
*   **Post-train Method:** Full LoRA (BF16). 
*   **Context Length:** 16,384 tokens
*   **Training Data:** 30,000 perfectly shuffled instruction-following examples (25% RU, 25% EN, 25% FR, 25% KO).

## 📊 Evaluation Results

Our fine-tuning demonstrated significant improvements, particularly in mathematical and logical reasoning (Global-MGSM), while simultaneously improving performance across all four languages.

### General Benchmarks

![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/NmaMURWpyB5Pr4e-lRwwE.png)

| Benchmark | Qwen3.6-35B-A3B | Zenotron-Mini v0.5 | Delta |
| :--- | :--- | :--- | :--- |
| **Belebele** (Reading Comp.) | 92.56% | **93.44%** | +0.89 p.p. |
| **Global-MGSM** (Math/Logic) | 75.50% | **89.20%** | **+13.70 p.p.** |

### Cross-Lingual Performance (Global-MGSM)
*Post-training on a multilingual mixture improved logical reasoning even on non-dominant languages, preventing catastrophic forgetting.*

![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/ThDKCL5Yqta36FVpBVA0y.png)

| Language | Qwen3.6-35B-A3B | Zenotron-Mini v0.5 | Delta |
| :--- | :--- | :--- | :--- |
| **RU** (Russian) | 84.0% | **91.2%** | +7.2% |
| **EN** (English) | 87.6% | **97.2%** | +9.6% |
| **FR** (French) | 62.0% | **83.2%** | +21.2% |
| **KO** (Korean) | 68.4% | **85.2%** | +16.8% |


![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/SCGfImIctqEw-GAHkSgHS.png)

*(For detailed per-language Belebele scores, please refer to the evaluation logs in the repository).*

## 💻 How to Use

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Model
MODEL_ID = "open-zzrl/Zenotron-Mini-0.5-Multilingual"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
)

# Load model in BF16
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

model.eval()

# Example prompt
messages = [
    {
        "role": "user",
        "content": (
            "Solve the following problem step by step and provide the final answer at the end.\n\n"
            "A store has 24 boxes. Each box contains 12 items. "
            "The store sells 87 items and receives another 35.\n\n"
            "How many items are left?"
        ),
    }
]

# Apply chat template
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
)

inputs = inputs.to(model.device)

# Generate response
input_length = inputs["input_ids"].shape[-1]
max_new_tokens = 4096

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_length=input_length + max_new_tokens,
        do_sample=False,
        use_cache=True,
        pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

# Decode generated tokens
generated_tokens = outputs[0, input_length:]

response = tokenizer.decode(
    generated_tokens,
    skip_special_tokens=True,
)

print(response)
```

## 🚧 Limitations & Future Work
*   **Preview Version:** As a `v0.5` release, this model is an experimental iteration. 
*   **Next Steps:** Based on our analysis, adding KO and FR diluted the quality of the target languages. The upcoming **Zenotron-Mini v1.0** will focus exclusively on RU and EN to achieve state-of-the-art performance on these languages.
*   **Quantization:** Weights in BF16, FP8, FP4, and GGUF (including i-quants for llama.cpp/Ollama).

---
**Developed with ❤️ by [Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)**