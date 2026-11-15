---
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
base_model_relation: finetune
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
tags:
- lg-ai
- exaone
- exaone-deep
pipeline_tag: text-generation
library_name: transformers
---

# <span style="color: #7FFF7F;">EXAONE-Deep-7.8B GGUF Models</span>

## <span style="color: #7FFF7F;">Ultra-Low-Bit Quantization with IQ-DynamicGate (1-2 bit)</span>

Our latest quantization method introduces **precision-adaptive quantization** for ultra-low-bit models (1-2 bit), with benchmark-proven improvements on **Llama-3-8B**. This approach uses layer-specific strategies to preserve accuracy while maintaining extreme memory efficiency.

### **Benchmark Context**
All tests conducted on **Llama-3-8B-Instruct** using:
- Standard perplexity evaluation pipeline
- 2048-token context window
- Same prompt set across all quantizations

### **Method**
- **Dynamic Precision Allocation**:  
  - First/Last 25% of layers → IQ4_XS (selected layers)  
  - Middle 50% → IQ2_XXS/IQ3_S (increase efficiency)  
- **Critical Component Protection**:  
  - Embeddings/output layers use Q5_K  
  - Reduces error propagation by 38% vs standard 1-2bit  

### **Quantization Performance Comparison (Llama-3-8B)**

| Quantization | Standard PPL | DynamicGate PPL | Δ PPL   | Std Size | DG Size | Δ Size | Std Speed | DG Speed |
|--------------|--------------|------------------|---------|----------|---------|--------|-----------|----------|
| IQ2_XXS      | 11.30        | 9.84             | -12.9%  | 2.5G     | 2.6G    | +0.1G  | 234s      | 246s     |
| IQ2_XS       | 11.72        | 11.63            | -0.8%   | 2.7G     | 2.8G    | +0.1G  | 242s      | 246s     |
| IQ2_S        | 14.31        | 9.02             | -36.9%  | 2.7G     | 2.9G    | +0.2G  | 238s      | 244s     |
| IQ1_M        | 27.46        | 15.41            | -43.9%  | 2.2G     | 2.5G    | +0.3G  | 206s      | 212s     |
| IQ1_S        | 53.07        | 32.00            | -39.7%  | 2.1G     | 2.4G    | +0.3G  | 184s      | 209s     |

**Key**:
- PPL = Perplexity (lower is better)
- Δ PPL = Percentage change from standard to DynamicGate
- Speed = Inference time (CPU avx2, 2048 token context)
- Size differences reflect mixed quantization overhead

**Key Improvements:**
- 🔥 **IQ1_M** shows massive 43.9% perplexity reduction (27.46 → 15.41)
- 🚀 **IQ2_S** cuts perplexity by 36.9% while adding only 0.2GB
- ⚡ **IQ1_S** maintains 39.7% better accuracy despite 1-bit quantization

**Tradeoffs:**
- All variants have modest size increases (0.1-0.3GB)
- Inference speeds remain comparable (<5% difference)


### **When to Use These Models**
📌 **Fitting models into GPU VRAM**

✔ **Memory-constrained deployments**

✔ **Cpu and Edge Devices** where 1-2bit errors can be tolerated 
 
✔ **Research** into ultra-low-bit quantization


## **Choosing the Right Model Format**  

Selecting the correct model format depends on your **hardware capabilities** and **memory constraints**.  

### **BF16 (Brain Float 16) – Use if BF16 acceleration is available**  
- A 16-bit floating-point format designed for **faster computation** while retaining good precision.  
- Provides **similar dynamic range** as FP32 but with **lower memory usage**.  
- Recommended if your hardware supports **BF16 acceleration** (check your device's specs).  
- Ideal for **high-performance inference** with **reduced memory footprint** compared to FP32.  

📌 **Use BF16 if:**  
✔ Your hardware has native **BF16 support** (e.g., newer GPUs, TPUs).  
✔ You want **higher precision** while saving memory.  
✔ You plan to **requantize** the model into another format.  

📌 **Avoid BF16 if:**  
❌ Your hardware does **not** support BF16 (it may fall back to FP32 and run slower).  
❌ You need compatibility with older devices that lack BF16 optimization.  

---

### **F16 (Float 16) – More widely supported than BF16**  
- A 16-bit floating-point **high precision** but with less of range of values than BF16. 
- Works on most devices with **FP16 acceleration support** (including many GPUs and some CPUs).  
- Slightly lower numerical precision than BF16 but generally sufficient for inference.  

📌 **Use F16 if:**  
✔ Your hardware supports **FP16** but **not BF16**.  
✔ You need a **balance between speed, memory usage, and accuracy**.  
✔ You are running on a **GPU** or another device optimized for FP16 computations.  

📌 **Avoid F16 if:**  
❌ Your device lacks **native FP16 support** (it may run slower than expected).  
❌ You have memory limitations.  

---

### **Quantized Models (Q4_K, Q6_K, Q8, etc.) – For CPU & Low-VRAM Inference**  
Quantization reduces model size and memory usage while maintaining as much accuracy as possible.  
- **Lower-bit models (Q4_K)** → **Best for minimal memory usage**, may have lower precision.  
- **Higher-bit models (Q6_K, Q8_0)** → **Better accuracy**, requires more memory.  

📌 **Use Quantized Models if:**  
✔ You are running inference on a **CPU** and need an optimized model.  
✔ Your device has **low VRAM** and cannot load full-precision models.  
✔ You want to reduce **memory footprint** while keeping reasonable accuracy.  

📌 **Avoid Quantized Models if:**  
❌ You need **maximum accuracy** (full-precision models are better for this).  
❌ Your hardware has enough VRAM for higher-precision formats (BF16/F16).  

---

### **Very Low-Bit Quantization (IQ3_XS, IQ3_S, IQ3_M, Q4_K, Q4_0)**  
These models are optimized for **extreme memory efficiency**, making them ideal for **low-power devices** or **large-scale deployments** where memory is a critical constraint.  

- **IQ3_XS**: Ultra-low-bit quantization (3-bit) with **extreme memory efficiency**.  
  - **Use case**: Best for **ultra-low-memory devices** where even Q4_K is too large.  
  - **Trade-off**: Lower accuracy compared to higher-bit quantizations.  

- **IQ3_S**: Small block size for **maximum memory efficiency**.  
  - **Use case**: Best for **low-memory devices** where **IQ3_XS** is too aggressive.  

- **IQ3_M**: Medium block size for better accuracy than **IQ3_S**.  
  - **Use case**: Suitable for **low-memory devices** where **IQ3_S** is too limiting.  

- **Q4_K**: 4-bit quantization with **block-wise optimization** for better accuracy.  
  - **Use case**: Best for **low-memory devices** where **Q6_K** is too large.  

- **Q4_0**: Pure 4-bit quantization, optimized for **ARM devices**.  
  - **Use case**: Best for **ARM-based devices** or **low-memory environments**.  

---

### **Summary Table: Model Format Selection**  

| Model Format  | Precision  | Memory Usage  | Device Requirements  | Best Use Case  |  
|--------------|------------|---------------|----------------------|---------------|  
| **BF16**     | Highest    | High          | BF16-supported GPU/CPUs  | High-speed inference with reduced memory |  
| **F16**      | High       | High          | FP16-supported devices | GPU inference when BF16 isn't available |  
| **Q4_K**     | Medium Low | Low           | CPU or Low-VRAM devices | Best for memory-constrained environments |  
| **Q6_K**     | Medium     | Moderate      | CPU with more memory | Better accuracy while still being quantized |  
| **Q8_0**     | High       | Moderate      | CPU or GPU with enough VRAM | Best accuracy among quantized models |  
| **IQ3_XS**   | Very Low   | Very Low      | Ultra-low-memory devices | Extreme memory efficiency and low accuracy |  
| **Q4_0**     | Low        | Low           | ARM or low-memory devices | llama.cpp can optimize for ARM devices |  

---

## **Included Files & Details**  

### `EXAONE-Deep-7.8B-bf16.gguf`  
- Model weights preserved in **BF16**.  
- Use this if you want to **requantize** the model into a different format.  
- Best if your device supports **BF16 acceleration**.  

### `EXAONE-Deep-7.8B-f16.gguf`  
- Model weights stored in **F16**.  
- Use if your device supports **FP16**, especially if BF16 is not available.  

### `EXAONE-Deep-7.8B-bf16-q8_0.gguf`  
- **Output & embeddings** remain in **BF16**.  
- All other layers quantized to **Q8_0**.  
- Use if your device supports **BF16** and you want a quantized version.  

### `EXAONE-Deep-7.8B-f16-q8_0.gguf`  
- **Output & embeddings** remain in **F16**.  
- All other layers quantized to **Q8_0**.    

### `EXAONE-Deep-7.8B-q4_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q4_K**.  
- Good for **CPU inference** with limited memory.  

### `EXAONE-Deep-7.8B-q4_k_s.gguf`  
- Smallest **Q4_K** variant, using less memory at the cost of accuracy.  
- Best for **very low-memory setups**.  

### `EXAONE-Deep-7.8B-q6_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q6_K** .  

### `EXAONE-Deep-7.8B-q8_0.gguf`  
- Fully **Q8** quantized model for better accuracy.  
- Requires **more memory** but offers higher precision.  

### `EXAONE-Deep-7.8B-iq3_xs.gguf`  
- **IQ3_XS** quantization, optimized for **extreme memory efficiency**.  
- Best for **ultra-low-memory devices**.  

### `EXAONE-Deep-7.8B-iq3_m.gguf`  
- **IQ3_M** quantization, offering a **medium block size** for better accuracy.  
- Suitable for **low-memory devices**.  

### `EXAONE-Deep-7.8B-q4_0.gguf`  
- Pure **Q4_0** quantization, optimized for **ARM devices**.  
- Best for **low-memory environments**.
- Prefer IQ4_NL for better accuracy.

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>
❤ **Please click "Like" if you find this useful!**  
Help me test my **AI-Powered Network Monitor Assistant** with **quantum-ready security checks**:  
👉 [Quantum Network Monitor](https://readyforquantum.com)  

💬 **How to test**:  
1. Click the **chat icon** (bottom right on any page)  
2. Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4-mini)  
   - `FreeLLM` (Open-source)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap scans**  
  - **Quantum-readiness checks**  
  - **Metasploit integration**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 6 CPU threads):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**)  
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4-mini** for:  
- **Real-time network diagnostics**  
- **Automated penetration testing** (Nmap/Metasploit)  
- 🔑 Get more tokens by [downloading our Quantum Network Monitor Agent](https://readyforquantum.com/download/?utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  

🔵 **HugLLM** – Open-source models (≈8B params):  
- **2x more tokens** than TurboLLM  
- **AI-powered log analysis**  
- 🌐 Runs on Hugging Face Inference API  

### 💡 **Example AI Commands to Test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a quick Nmap vulnerability test"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a Quantum Network Monitor Agent to run the .net code from. This is a very flexible and powerful feature. Use with caution!

### Final word
I fund the servers to create the models files, run the Quantum Network Monitor Service and Pay for Inference from Novita and OpenAI all from my own pocket. All of the code for creating the models and the work I have done with Quantum Network Monitor is [open source](https://github.com/Mungert69). Feel free to use what you find useful. Please support my work and consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) .
This will help me pay for the services and increase the token limits for everyone.

Thank you :)  




# EXAONE-Deep-7.8B

## Introduction

We introduce EXAONE Deep, which exhibits superior capabilities in various reasoning tasks including math and coding benchmarks, ranging from 2.4B to 32B parameters developed and released by LG AI Research. Evaluation results show that 1) EXAONE Deep **2.4B** outperforms other models of comparable size, 2) EXAONE Deep **7.8B** outperforms not only open-weight models of comparable scale but also a proprietary reasoning model OpenAI o1-mini, and 3) EXAONE Deep **32B** demonstrates competitive performance against leading open-weight models.

For more details, please refer to our [documentation](https://arxiv.org/abs/2503.12524), [blog](https://www.lgresearch.ai/news/view?seq=543) and [GitHub](https://github.com/LG-AI-EXAONE/EXAONE-Deep).

<p align="center">
<img src="assets/exaone_deep_overall_performance.png", width="100%", style="margin: 40 auto;">

This repository contains the reasoning 7.8B language model with the following features:

- Number of Parameters (without embeddings): 6.98B
- Number of Layers: 32
- Number of Attention Heads: GQA with 32 Q-heads and 8 KV-heads
- Vocab Size: 102,400
- Context Length: 32,768 tokens

## Quickstart

We recommend to use `transformers` v4.43.1 or later.

Here is the code snippet to run conversational inference with the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model_name = "LGAI-EXAONE/EXAONE-Deep-7.8B"
streaming = True    # choose the streaming option

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Choose your prompt:
#   Math example (AIME 2024)
prompt = r"""Let $x,y$ and $z$ be positive real numbers that satisfy the following system of equations:
\[\log_2\left({x \over yz}\right) = {1 \over 2}\]\[\log_2\left({y \over xz}\right) = {1 \over 3}\]\[\log_2\left({z \over xy}\right) = {1 \over 4}\]
Then the value of $\left|\log_2(x^4y^3z^2)\right|$ is $\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

Please reason step by step, and put your final answer within \boxed{}."""
#   Korean MCQA example (CSAT Math 2025)
prompt = r"""Question : $a_1 = 2$인 수열 $\{a_n\}$과 $b_1 = 2$인 등차수열 $\{b_n\}$이 모든 자연수 $n$에 대하여\[\sum_{k=1}^{n} \frac{a_k}{b_{k+1}} = \frac{1}{2} n^2\]을 만족시킬 때, $\sum_{k=1}^{5} a_k$의 값을 구하여라.

Options :
A) 120
B) 125
C) 130
D) 135
E) 140
 
Please reason step by step, and you should write the correct option alphabet (A, B, C, D or E) within \\boxed{}."""

messages = [
    {"role": "user", "content": prompt}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
)

if streaming:
    streamer = TextIteratorStreamer(tokenizer)
    thread = Thread(target=model.generate, kwargs=dict(
        input_ids=input_ids.to("cuda"),
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=32768,
        do_sample=True,
        temperature=0.6,
        top_p=0.95,
        streamer=streamer
    ))
    thread.start()

    for text in streamer:
        print(text, end="", flush=True)
else:
    output = model.generate(
        input_ids.to("cuda"),
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=32768,
        do_sample=True,
        temperature=0.6,
        top_p=0.95,
    )
    print(tokenizer.decode(output[0]))
```

> ### Note
> The EXAONE Deep models are trained with an optimized configuration,
> so we recommend following the [Usage Guideline](#usage-guideline) section to achieve optimal performance.

## Evaluation

The following table shows the evaluation results of reasoning tasks such as math and coding. The full evaluation results can be found in the [documentation](https://arxiv.org/abs/2503.12524).

<table>
    <tr>
        <th>Models</th>
        <th>MATH-500 (pass@1)</th>
        <th>AIME 2024 (pass@1 / cons@64)</th>
        <th>AIME 2025 (pass@1 / cons@64)</th>
        <th>CSAT Math 2025 (pass@1)</th>
        <th>GPQA Diamond (pass@1)</th>
        <th>Live Code Bench (pass@1)</th>
    </tr>
    <tr>
        <td>EXAONE Deep 32B</td>
        <td>95.7</td>
        <td>72.1 / <strong>90.0</strong></td>
        <td>65.8 / <strong>80.0</strong></td>
        <td><strong>94.5</strong></td>
        <td>66.1</td>
        <td>59.5</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-32B</td>
        <td>94.3</td>
        <td>72.6 / 83.3</td>
        <td>55.2 / 73.3</td>
        <td>84.1</td>
        <td>62.1</td>
        <td>57.2</td>
    </tr>
    <tr>
        <td>QwQ-32B</td>
        <td>95.5</td>
        <td>79.5 / 86.7</td>
        <td><strong>67.1</strong> / 76.7</td>
        <td>94.4</td>
        <td>63.3</td>
        <td>63.4</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Llama-70B</td>
        <td>94.5</td>
        <td>70.0 / 86.7</td>
        <td>53.9 / 66.7</td>
        <td>88.8</td>
        <td>65.2</td>
        <td>57.5</td>
    </tr>
    <tr>
        <td>DeepSeek-R1 (671B)</td>
        <td><strong>97.3</strong></td>
        <td><strong>79.8</strong> / 86.7</td>
        <td>66.8 / <strong>80.0</strong></td>
        <td>89.9</td>
        <td><strong>71.5</strong></td>
        <td><strong>65.9</strong></td>
    </tr>
    <tr>
        <th colspan="7" height="30px"></th>
    </tr>
    <tr>
        <td>EXAONE Deep 7.8B</td>
        <td><strong>94.8</strong></td>
        <td><strong>70.0</strong> / <strong>83.3</strong></td>
        <td><strong>59.6</strong> / <strong>76.7</strong></td>
        <td><strong>89.9</strong></td>
        <td><strong>62.6</strong></td>
        <td><strong>55.2</strong></td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-7B</td>
        <td>92.8</td>
        <td>55.5 / <strong>83.3</strong></td>
        <td>38.5 / 56.7</td>
        <td>79.7</td>
        <td>49.1</td>
        <td>37.6</td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Llama-8B</td>
        <td>89.1</td>
        <td>50.4 / 80.0</td>
        <td>33.6 / 53.3</td>
        <td>74.1</td>
        <td>49.0</td>
        <td>39.6</td>
    </tr>
    <tr>
        <td>OpenAI o1-mini</td>
        <td>90.0</td>
        <td>63.6 / 80.0</td>
        <td>54.8 / 66.7</td>
        <td>84.4</td>
        <td>60.0</td>
        <td>53.8</td>
    </tr>
    <tr>
        <th colspan="7" height="30px"></th>
    </tr>
    <tr>
        <td>EXAONE Deep 2.4B</td>
        <td><strong>92.3</strong></td>
        <td><strong>52.5</strong> / <strong>76.7</strong></td>
        <td><strong>47.9</strong> / <strong>73.3</strong></td>
        <td><strong>79.2</strong></td>
        <td><strong>54.3</strong></td>
        <td><strong>46.6</strong></td>
    </tr>
    <tr>
        <td>DeepSeek-R1-Distill-Qwen-1.5B</td>
        <td>83.9</td>
        <td>28.9 / 52.7</td>
        <td>23.9 / 36.7</td>
        <td>65.6</td>
        <td>33.8</td>
        <td>16.9</td>
    </tr>
</table>

## Deployment

EXAONE Deep models can be inferred in the various frameworks, such as:
- `TensorRT-LLM`
- `vLLM`
- `SGLang`
- `llama.cpp`
- `Ollama`
- `LM-Studio`

Please refer to our [EXAONE Deep GitHub](https://github.com/LG-AI-EXAONE/EXAONE-Deep) for more details about the inference frameworks.

## Quantization

We provide the pre-quantized EXAONE Deep models with **AWQ** and several quantization types in **GGUF** format. Please refer to our [EXAONE Deep collection](https://huggingface.co/collections/LGAI-EXAONE/exaone-deep-67d119918816ec6efa79a4aa) to find corresponding quantized models.

## Usage Guideline

To achieve the expected performance, we recommend using the following configurations:

1. Ensure the model starts with `<thought>\n` for reasoning steps. The model's output quality may be degraded when you omit it. You can easily apply this feature by using `tokenizer.apply_chat_template()` with `add_generation_prompt=True`. Please check the example code on [Quickstart](#quickstart) section.
2. The reasoning steps of EXAONE Deep models enclosed by `<thought>\n...\n</thought>` usually have lots of tokens, so previous reasoning steps may be necessary to be removed in multi-turn situation. The provided tokenizer handles this automatically.
3. Avoid using system prompt, and build the instruction on the user prompt. 
4. Additional instructions help the models reason more deeply, so that the models generate better output.
    - For math problems, the instructions **"Please reason step by step, and put your final answer within \boxed{}."** are helpful.
    - For more information on our evaluation setting including prompts, please refer to our [Documentation](https://arxiv.org/abs/2503.12524).
5. In our evaluation, we use `temperature=0.6` and `top_p=0.95` for generation. 
6. When evaluating the models, it is recommended to test multiple times to assess the expected performance accurately.

## Limitation

The EXAONE language model has certain limitations and may occasionally generate inappropriate responses. The language model generates responses based on the output probability of tokens, and it is determined during learning from training data. While we have made every effort to exclude personal, harmful, and biased information from the training data, some problematic content may still be included, potentially leading to undesirable responses. Please note that the text generated by EXAONE language model does not reflects the views of LG AI Research.

- Inappropriate answers may be generated, which contain personal, harmful or other inappropriate information.
- Biased responses may be generated, which are associated with age, gender, race, and so on.
- The generated responses rely heavily on statistics from the training data, which can result in the generation of
semantically or syntactically incorrect sentences.
- Since the model does not reflect the latest information, the responses may be false or contradictory.

LG AI Research strives to reduce potential risks that may arise from EXAONE language models. Users are not allowed
to engage in any malicious activities (e.g., keying in illegal information) that may induce the creation of inappropriate
outputs violating LG AI’s ethical principles when using EXAONE language models.

## License

The model is licensed under [EXAONE AI Model License Agreement 1.1 - NC](./LICENSE)

## Citation
 
```
@article{exaone-deep,
  title={EXAONE Deep: Reasoning Enhanced Language Models},
  author={{LG AI Research}},
  journal={arXiv preprint arXiv:2503.12524},
  year={2025}
}
```

## Contact
LG AI Research Technical Support: contact_us@lgresearch.ai