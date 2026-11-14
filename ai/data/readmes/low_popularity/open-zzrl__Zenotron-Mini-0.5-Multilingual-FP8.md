---
language:
- ru
- en
- fr
- ko
license: apache-2.0
base_model: open-zzrl/Zenotron-Mini-0.5-Multilingual
tags:
- fp8
- quantized
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

# 🧠 Zenotron-Mini-v0.5-Multilingual (FP8)

![](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/LKJBKn02BwueQQK4xseIk.png)

**Zenotron-Mini-v0.5-Multilingual (FP8)** is a highly efficient, quantized version of the preview model developed by **[Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)**. 

This release features **FP8 (E4M3)** quantization to drastically reduce memory footprint and accelerate inference on modern GPU architectures, while maintaining the strong cross-lingual transfer and reasoning capabilities of the original BF16 model.

## 📌 Model Details
*   **Base Model:** Qwen3.6-35B-A3B
*   **Active Parameters:** ~3B (efficient inference)
*   **Total Parameters:** 35B
*   **Post-train Method:** Full LoRA (BF16)
*   **Quantization:** FP8 (E4M3) dynamic quantization
*   **Context Length:** 16,384 tokens
*   **Training Data:** 30,000 perfectly shuffled instruction-following examples (25% RU, 25% EN, 25% FR, 25% KO).

## ⚡ Quantization Details
This repository contains the FP8 quantized weights, optimized for production-level inference.

*   **Hardware Requirements:** Requires an NVIDIA GPU with **Compute Capability ≥ 8.9** (Ada Lovelace, Hopper, or Blackwell architecture — e.g., RTX 40-series, L4/L40S, H100/H200, B100/B200, or RTX PRO 6000). 
*   **Backward Compatibility:** On older GPUs (Ampere and below), the model will be dequantized to BF16 on the fly. This maintains compatibility but loses the speed/memory benefits of FP8.
*   **Quality:** FP8 quantization preserves the original BF16 evaluation metrics while significantly improving throughput.

## 📊 Evaluation Results

*(The FP8 quantization does not degrade the performance of the original model. Below are the results achieved by the base v0.5 Multilingual model.)*

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

## 💻 How to Use

### Option 1: vLLM (Recommended for FP8)
The best way to serve this model is using **vLLM**, which natively supports FP8 execution for maximum speed.

```bash
pip install vllm
vllm serve open-zzrl/Zenotron-Mini-0.5-Multilingual-FP8
```

### Option 2: Hugging Face Transformers
If you are using `transformers`, ensure you have a recent version (>= 4.40). Using `dtype="auto"` will automatically load the model in FP8 (if your hardware supports it) or dequantize it to BF16.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "open-zzrl/Zenotron-Mini-0.5-Multilingual-FP8"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

# Using dtype="auto" is crucial for quantized models
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype="auto", 
    device_map="auto",
    trust_remote_code=True,
)

model.eval()

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

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
    enable_thinking=False # Disables internal reasoning for faster, direct answers
)

inputs = inputs.to(model.device)
input_length = inputs["input_ids"].shape[-1]

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_length=input_length + 512,
        do_sample=False,
        use_cache=True,
        pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

generated_tokens = outputs[0, input_length:]
response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
print(response)
```

## 🚧 Limitations & Future Work
*   **Preview Version:** As a `v0.5` release, this model is an experimental iteration. 
*   **Next Steps:** Based on our analysis, adding KO and FR diluted the quality of the target languages. The upcoming **Zenotron-Mini v1.0** will focus exclusively on RU and EN to achieve state-of-the-art performance on these languages.
*   **Quantization Note:** This is the **FP8 variant**. For maximum compatibility with older hardware (like standard RTX 30-series or Apple Silicon) or CPU inference, please refer to the standard BF16 version or the upcoming GGUF release.

---
**Developed by [Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)** ❤️