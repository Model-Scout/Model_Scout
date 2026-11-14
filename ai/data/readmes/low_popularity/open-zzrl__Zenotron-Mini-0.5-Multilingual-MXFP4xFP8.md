---
language:
- ru
- en
- fr
- ko
license: apache-2.0
base_model: open-zzrl/Zenotron-Mini-0.5-Multilingual
tags:
- mxfp4
- fp8
- quantized
- compressed-tensors
- llm-compressor
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

# 🧠 Zenotron-Mini-v0.5-Multilingual (MXFP4xFP8)

![](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/LKJBKn02BwueQQK4xseIk.png)

**Zenotron-Mini-v0.5-Multilingual (MXFP4xFP8)** is a highly optimized, mixed-precision quantized checkpoint developed by **[Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)**. 

This release is designed for extreme memory efficiency and high-throughput inference on modern data center GPUs (such as NVIDIA Blackwell). It leverages **LLM Compressor** and the **compressed-tensors** format to selectively quantize MoE experts while preserving critical routing and embedding layers in original precision.

## 📌 Model Details
*   **Base Model:** Qwen3.6-35B-A3B
*   **Active Parameters:** ~3B
*   **Total Parameters:** 35B
*   **Base Post-training:** Full LoRA (BF16)
*   **Quantization Backend:** LLM Compressor / compressed-tensors
*   **Context Length:** 16,384 tokens

## ⚡ Mixed-Precision Quantization Details
Unlike standard uniform quantization, this checkpoint uses a targeted, mixed-precision approach to balance memory footprint and model accuracy, specifically tailored for the MoE architecture.

| Component | Format | Rationale |
| :--- | :--- | :--- |
| **Routed MoE Experts** | **MXFP4xFP8** | Extremely low footprint (4-bit weights) for the bulk of the parameters, with dynamic FP8 activation scaling. |
| **Dense Projections** (Self-Attn, Linear-Attn, Shared Experts) | **FP8_BLOCK** | Maintains 8-bit precision to ensure high fidelity in attention and shared processing. |
| **Router / Gating** | **BF16** (Preserved) | Quantizing the router can break MoE routing. Kept in original precision. |
| **Embeddings & Norms** | **BF16** (Preserved) | Critical for text representation and stability. |
| **Vision Encoder & MTP** | **BF16** (Preserved) | Kept unquantized to preserve multimodal and speculative capabilities. |

### 🖥️ Hardware Requirements
*   **Recommended:** NVIDIA Blackwell (SM100+) for native MXFP4 acceleration.
*   **Compatibility:** Modern NVIDIA GPUs (Ada Lovelace, Hopper) support the FP8_BLOCK components natively and will run the MXFP4 experts via software emulation.
*   **Storage:** SafeTensors (not GGUF). Requires `compressed-tensors` runtime for inference.

## 📊 Evaluation Results
*Extensive testing confirms that our mixed-precision quantization preserves the performance of the original BF16 model.*

![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/NmaMURWpyB5Pr4e-lRwwE.png)

| Benchmark | Qwen3.6-35B-A3B | Zenotron-Mini v0.5 (BF16) | Delta |
| :--- | :--- | :--- | :--- |
| **Belebele** (Reading Comp.) | 92.56% | **93.44%** | +0.89 p.p. |
| **Global-MGSM** (Math/Logic) | 75.50% | **89.20%** | **+13.70 p.p.** |

### Cross-Lingual Performance (Global-MGSM)
![image](https://cdn-uploads.huggingface.co/production/uploads/6a535822f7c1c2b44a684b39/ThDKCL5Yqta36FVpBVA0y.png)

| Language | Qwen3.6-35B-A3B | Zenotron-Mini v0.5 | Delta |
| :--- | :--- | :--- | :--- |
| **RU** (Russian) | 84.0% | **91.2%** | +7.2% |
| **EN** (English) | 87.6% | **97.2%** | +9.6% |
| **FR** (French) | 62.0% | **83.2%** | +21.2% |
| **KO** (Korean) | 68.4% | **85.2%** | +16.8% |

## 💻 How to Use

### Option 1: vLLM (Highly Recommended)
Because this model uses `compressed-tensors` mixed-precision, **vLLM** is the most performant engine to run it.

```bash
# Ensure you have a recent version of vLLM installed
pip install vllm

# Serve the model (vLLM automatically detects the compressed-tensors format)
vllm serve open-zzrl/Zenotron-Mini-0.5-Multilingual-MXFP4xFP8
```

### Option 2: Hugging Face Transformers
You can also run it via `transformers`, but ensure you are using the latest version (`>= 4.45`) and have `compressed-tensors` installed.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "open-zzrl/Zenotron-Mini-0.5-Multilingual-MXFP4xFP8"

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

# Apply chat template, disabling internal reasoning for fast responses
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
    enable_thinking=False 
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
*   **Hardware Bound:** While it will run on older GPUs via emulation, the MXFP4 format is specifically designed for Blackwell architecture to achieve optimal throughput.
*   **Preview Version:** As a `v0.5` release, this is an experimental iteration based on the 4-language model. 
*   **Next Steps:** The upcoming **Zenotron-Mini v1.0** will focus exclusively on RU and EN.

---
**Quantized and developed by [Open Zeno-Zero Research Lab](https://huggingface.co/open-zzrl)** ❤️