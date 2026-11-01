---
thumbnail: >-
  https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b/resolve/main/resources/pe.png
license: apache-2.0
tags:
- general-purpose
- roleplay
- storywriting
- chemistry
- biology
- code
- climate
- axolotl
- text-generation-inference
- finetune
- legal
- medical
- finance
datasets:
- PocketDoc/Dans-Prosemaxx-RP
- PocketDoc/Dans-Personamaxx-Logs-2
- PocketDoc/Dans-Personamaxx-VN
- PocketDoc/Dans-Kinomaxx-VanillaBackrooms
- PocketDoc/Dans-Prosemaxx-Gutenberg
- PocketDoc/Dans-Prosemaxx-Cowriter-3-XL
- PocketDoc/Dans-Prosemaxx-Adventure
- PocketDoc/Dans-Failuremaxx-Adventure-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-2
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-Continue-2
- PocketDoc/Dans-Prosemaxx-Instructwriter-Long
- PocketDoc/Dans-Prosemaxx-RepRemover-1
- PocketDoc/Dans-MemoryCore-CoreCurriculum-Small
- AquaV/US-Army-Survival-Sharegpt
- AquaV/Multi-Environment-Operations-Sharegpt
- AquaV/Resistance-Sharegpt
- AquaV/Interrogation-Sharegpt
- AquaV/Chemical-Biological-Safety-Applications-Sharegpt
- AquaV/Energetic-Materials-Sharegpt
- PocketDoc/Dans-Mathmaxx
- PJMixers/Math-Multiturn-1K-ShareGPT
- PocketDoc/Dans-Taskmaxx
- PocketDoc/Dans-Taskmaxx-DataPrepper
- PocketDoc/Dans-Taskmaxx-ConcurrentQA-Reworked
- PocketDoc/Dans-Taskmaxx-TableGPT
- PocketDoc/Dans-Taskmaxx-SciRIFF
- PocketDoc/Dans-Taskmaxx-Edit
- PocketDoc/Dans-Toolmaxx-Agent
- PocketDoc/Dans-Toolmaxx-ShellCommands
- PocketDoc/Dans-Toolmaxx-Functions-Toolbench
- PocketDoc/Dans-Toolmaxx-Functions-ToolACE
- PocketDoc/Dans-Toolmaxx-Functions-apigen-subset
- PocketDoc/Dans-Assistantmaxx-OpenAssistant2
- PocketDoc/Dans-Assistantmaxx-Opus-Merge-2
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset-2
- PocketDoc/Dans-Assistantmaxx-Synthia
- PocketDoc/Dans-Assistantmaxx-ASL
- PocketDoc/Dans-Assistantmaxx-PersonaLLM-Opus
- PocketDoc/Dans-Assistantmaxx-LongAlign
- PocketDoc/Dans-Assistantmaxx-OpenLeecher-Instruct
- PocketDoc/Dans-Assistantmaxx-Tulu3-IF
- PocketDoc/Dans-Systemmaxx
- PocketDoc/Dans-Logicmaxx-SAT-AP
- PJMixers/grimulkan_theory-of-mind-ShareGPT
- PJMixers/grimulkan_physical-reasoning-ShareGPT
- PocketDoc/Dans-Reasoningmaxx-NaturalReasoning
- PocketDoc/Dans-Reasoningmaxx-WebInstruct
- PocketDoc/Dans-Reasoningmaxx-GeneralReasoning
- PocketDoc/Dans-Assistantmaxx-ClosedInstruct
language:
- en
- ar
- de
- fr
- es
- hi
- pt
- ja
- ko
base_model:
- mistralai/Mistral-Small-3.1-24B-Base-2503
pipeline_tag: text-generation
library_name: transformers
---

# <span style="color: #7FFF7F;">Dans-PersonalityEngine-V1.3.0-24b GGUF Models</span>


## <span style="color: #7F7FFF;">Model Generation Details</span>

This model was generated using [llama.cpp](https://github.com/ggerganov/llama.cpp) at commit [`f5cd27b7`](https://github.com/ggerganov/llama.cpp/commit/f5cd27b71da3ac375a04a41643d14fc779a8057b).




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

### `Dans-PersonalityEngine-V1.3.0-24b-bf16.gguf`  
- Model weights preserved in **BF16**.  
- Use this if you want to **requantize** the model into a different format.  
- Best if your device supports **BF16 acceleration**.  

### `Dans-PersonalityEngine-V1.3.0-24b-f16.gguf`  
- Model weights stored in **F16**.  
- Use if your device supports **FP16**, especially if BF16 is not available.  

### `Dans-PersonalityEngine-V1.3.0-24b-bf16-q8_0.gguf`  
- **Output & embeddings** remain in **BF16**.  
- All other layers quantized to **Q8_0**.  
- Use if your device supports **BF16** and you want a quantized version.  

### `Dans-PersonalityEngine-V1.3.0-24b-f16-q8_0.gguf`  
- **Output & embeddings** remain in **F16**.  
- All other layers quantized to **Q8_0**.    

### `Dans-PersonalityEngine-V1.3.0-24b-q4_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q4_K**.  
- Good for **CPU inference** with limited memory.  

### `Dans-PersonalityEngine-V1.3.0-24b-q4_k_s.gguf`  
- Smallest **Q4_K** variant, using less memory at the cost of accuracy.  
- Best for **very low-memory setups**.  

### `Dans-PersonalityEngine-V1.3.0-24b-q6_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q6_K** .  

### `Dans-PersonalityEngine-V1.3.0-24b-q8_0.gguf`  
- Fully **Q8** quantized model for better accuracy.  
- Requires **more memory** but offers higher precision.  

### `Dans-PersonalityEngine-V1.3.0-24b-iq3_xs.gguf`  
- **IQ3_XS** quantization, optimized for **extreme memory efficiency**.  
- Best for **ultra-low-memory devices**.  

### `Dans-PersonalityEngine-V1.3.0-24b-iq3_m.gguf`  
- **IQ3_M** quantization, offering a **medium block size** for better accuracy.  
- Suitable for **low-memory devices**.  

### `Dans-PersonalityEngine-V1.3.0-24b-q4_0.gguf`  
- Pure **Q4_0** quantization, optimized for **ARM devices**.  
- Best for **low-memory environments**.
- Prefer IQ4_NL for better accuracy.

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>
❤ **Please click "Like" if you find this useful!**  
Help me test my **AI-Powered Network Monitor Assistant** with **quantum-ready security checks**:  
👉 [Quantum Network Monitor](https://readyforquantum.com/dashboard/?assistant=open&utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  

💬 **How to test**:  
 Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4o-mini)  
   - `HugLLM` (Hugginface Open-source)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap scans**  
  - **Quantum-readiness checks**  
  - **Network Monitoring tasks**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 2 CPU threads):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**)  
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4o-mini** for: 
- **Create custom cmd processors to run .net code on Quantum Network Monitor Agents**
- **Real-time network diagnostics and monitoring**
- **Security Audits**
- **Penetration testing** (Nmap/Metasploit)  
  

🔵 **HugLLM** – Latest Open-source models:  
- 🌐 Runs on Hugging Face Inference API  

### 💡 **Example commands to you could test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a comprehensive security audit on my server"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a Quantum Network Monitor Agent to run the .net code from. This is a very flexible and powerful feature. Use with caution!

### Final Word

I fund the servers used to create these model files, run the Quantum Network Monitor service, and pay for inference from Novita and OpenAI—all out of my own pocket. All the code behind the model creation and the Quantum Network Monitor project is [open source](https://github.com/Mungert69). Feel free to use whatever you find helpful.

If you appreciate the work, please consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) ☕. Your support helps cover service costs and allows me to raise token limits for everyone.

I'm also open to job opportunities or sponsorship.

Thank you! 😊



<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Dans-PersonalityEngine-V1.3.0-24b</title>
    </head>
    <div class="crt-container">
        <div class="crt-case">
            <div class="crt-inner-case">
                <div class="crt-bezel">
                    <div class="terminal-screen">
                        <div style="text-align: center">
                            <h2>Dans-PersonalityEngine-V1.3.0-24b</h2>
                            <pre class="code-block" style="display: inline-block; text-align: left; font-size: clamp(2px, 0.8vw, 14px); line-height: 1.2; max-width: 100%; overflow: hidden; white-space: pre;">
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠄⠀⡂⠀⠁⡄⢀⠁⢀⣈⡄⠌⠐⠠⠤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡄⠆⠀⢠⠀⠛⣸⣄⣶⣾⡷⡾⠘⠃⢀⠀⣴⠀⡄⠰⢆⣠⠘⠰⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⡋⢀⣤⡿⠟⠋⠁⠀⡠⠤⢇⠋⠀⠈⠃⢀⠀⠈⡡⠤⠀⠀⠁⢄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⡂⠀⠀⣀⣔⣧⠟⠋⠀⢀⡄⠀⠪⣀⡂⢁⠛⢆⠀⠀⠀⢎⢀⠄⢡⠢⠛⠠⡀⠀⠄⠀⠀
⠀⠀⡀⠡⢑⠌⠈⣧⣮⢾⢏⠁⠀⠀⡀⠠⠦⠈⠀⠞⠑⠁⠀⠀⢧⡄⠈⡜⠷⠒⢸⡇⠐⠇⠿⠈⣖⠂⠀
⠀⢌⠀⠤⠀⢠⣞⣾⡗⠁⠀⠈⠁⢨⡼⠀⠀⠀⢀⠀⣀⡤⣄⠄⠈⢻⡇⠀⠐⣠⠜⠑⠁⠀⣀⡔⡿⠨⡄
⠈⠂⠀⠆⠀⣼⣾⠟⠀⠑⠀⡐⠗⠉⠀⠐⠶⣤⡵⠋⠀⠠⠹⡌⡀⠘⠇⢠⣾⡣⣀⡴⠋⠅⠈⢊⠠⡱⡀
⠪⠑⢌⠂⣼⣿⡟⠀⠀⠙⠀⠀⠀⡀⠀⠀⠐⡞⡐⠀⠀⡧⠀⢀⠠⠀⣁⠾⡇⠀⠙⡁⠀⠀⢀⣨⣄⡠⢱
⣸⠈⠊⠙⣛⣿⡧⠔⠚⠛⠳⣄⣀⡬⠤⠬⠼⡣⠃⠀⢀⡗⠀⡤⠞⠙⠄⠂⠃⢀⣠⣤⠶⠙⠅⠁⠃⠋⠈
⢋⠼⣀⠰⢯⢿⠁⠀⢢⠀⠀⢐⠋⡀⠀⠈⠁⠀⣀⣰⠏⠒⠙⠈⠀⣀⡤⠞⢁⣼⠏⠘⢀⣀⢤⢤⡐⢈⠂
⠀⠢⠀⠀⠸⣿⡄⠲⠚⠘⠚⠃⢀⠀⠈⢋⠶⠛⠉⠉⢃⣀⢤⢾⠋⣁⡤⡚⠁⢹⠁⠠⢛⠠⠬⠁⢬⠀⠀
⠀⠈⢳⣒⠋⠉⣿⢐⠠⣀⣃⠀⠀⠉⠂⢁⣀⣀⡤⢞⠩⢑⡨⠰⡞⠁⠁⢀⡠⠾⠎⡈⡌⡈⡓⡀⠄⠀⠀
⠀⠀⠀⠉⠘⠃⢻⡒⠦⢼⣿⣛⣻⣿⡷⢄⣀⣀⣠⣴⢾⣿⣆⣡⡄⣠⣪⡿⣷⣾⣷⣧⡡⠅⣇⠍⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠛⠛⠓⠉⢹⠀⣷⠴⣻⣽⡻⢧⢻⡿⡏⣼⢿⣻⢾⣿⣿⣿⡿⢠ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠻⠨⠰⢋⡅⠉⣑⡇⡗⣿⢂⣸⡿⣿⣛⠿⠃⠁ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣌⣙⣸⢧⣿⣕⣼⣇⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣸⢧⢟⢟⡟⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠙⣾⡟⣻⡕⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⢰⡏⢠⡿⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠸⡇⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
</pre>
                        </div>
                        <p>
                            Dans-PersonalityEngine is a versatile model series
                            fine-tuned on 50+ specialized datasets, designed to
                            excel at both creative tasks (like roleplay and
                            co-writing) and technical challenges (such as code
                            generation, tool use, and complex reasoning).
                        </p>
                        <p>
                            V1.3.0 introduces multilingual capabilities with
                            support for 10 languages and enhanced domain
                            expertise across multiple fields. The primary
                            language is still English and that is where peak
                            performance can be expected.
                        </p>
                        <h3>Multilingual Support</h3>
                        <pre class="code-block">
Arabic  Chinese   English  French      German
Hindi   Japanese  Korean   Portuguese  Spanish</pre>
                        <h3>Key Details</h3>
                        <pre class="code-block">
BASE MODEL: mistralai/Mistral-Small-3.1-24B-Base-2503
LICENSE: apache-2.0
LANGUAGE: Multilingual with 10 supported languages
CONTEXT LENGTH: 32768 tokens, 131072 with degraded recall</pre>
                        <h3>Recommended Settings</h3>
                        <pre class="code-block">
TEMPERATURE: 1.0
TOP_P: 0.9</pre>
                        <h3>Prompting Format</h3>
                        <p>
                            The model uses the following format I'll refer to as
                            "DanChat-2":
                        </p>
                        <pre class="code-block">
<|system|>system prompt<|endoftext|><|user|>Hi there!<|endoftext|><|assistant|>Hey, how can I help?<|endoftext|></pre>
                        <h3>Why not ChatML?</h3>
                        <p>
                            While ChatML is a standard format for LLMs, it has
                            limitations. DanChat-2 uses special tokens
                            for each role, this reduces biases and helps the model adapt to different tasks more readily.
                        </p>
                        <h3>SillyTavern Template</h3>
                        <p>
                            <a
                                href="https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b/resolve/main/resources/DanChat-2.json?download=true"
                                download
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                Download Master JSON
                            </a>
                        </p>
                        <h3>Inference Provider</h3>
                        <p>
                            This model and others are available from ⚡Mancer AI for
                            those interested in high quality inference without
                            owning or renting expensive hardware.
                        </p>
                        <p class="mancer-button-container">
                            <a
                                href="https://mancer.tech/"
                                target="_blank"
                                rel="noopener noreferrer"
                                class="mancer-button"
                            >
                                <span class="mancer-text">mancer</span>
                            </a>
                        </p>
                        <h3>Training Process</h3>
                        <p>
                            The model was trained using Axolotl on 8x H100 GPUs
                            for 50 hours. The resources to train this model were provided by Prime Intellect and Kalomaze.
                        </p>
                        <h3>Support Development</h3>
                        <p>
                            Development is limited by funding and resources. To
                            help support:
                        </p>
                        <p>- Contact on HF</p>
                        <p>- Email: visuallyadequate@gmail.com</p>
                        <p class="coffee-container">
                            <a
                                href="https://www.buymeacoffee.com/visually"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <img
                                    src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
                                    alt="Buy Me A Coffee"
                                    height="45"
                                    width="162"
                                />
                            </a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Consolas&display=swap");
        .crt-container {
            padding: 10px;
            max-width: 1000px;
            margin: 0 auto;
            width: 95%;
        }
        .crt-case {
            background: #e8d7c3;
            border-radius: 10px;
            padding: 15px;
            box-shadow:
                inset -2px -2px 5px rgba(0, 0, 0, 0.3),
                2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .crt-inner-case {
            background: #e8d7c3;
            border-radius: 8px;
            padding: 3px;
            box-shadow:
                inset -1px -1px 4px rgba(0, 0, 0, 0.3),
                1px 1px 4px rgba(0, 0, 0, 0.2);
        }
        .crt-bezel {
            background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
            padding: 15px;
            border-radius: 5px;
            border: 3px solid #0a0a0a;
            position: relative;
            box-shadow:
                inset 0 0 20px rgba(0, 0, 0, 0.5),
                inset 0 0 4px rgba(0, 0, 0, 0.4),
                inset 2px 2px 4px rgba(255, 255, 255, 0.05),
                inset -2px -2px 4px rgba(0, 0, 0, 0.8),
                0 0 2px rgba(0, 0, 0, 0.6),
                -1px -1px 4px rgba(255, 255, 255, 0.1),
                1px 1px 4px rgba(0, 0, 0, 0.3);
        }
        .crt-bezel::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                45deg,
                rgba(255, 255, 255, 0.03) 0%,
                rgba(255, 255, 255, 0) 40%,
                rgba(0, 0, 0, 0.1) 60%,
                rgba(0, 0, 0, 0.2) 100%
            );
            border-radius: 3px;
            pointer-events: none;
        }
        .terminal-screen {
            background: #111112;
            padding: 20px;
            border-radius: 15px;
            position: relative;
            overflow: hidden;
            font-family: "Consolas", monospace;
            font-size: clamp(12px, 1.5vw, 16px);
            color: #e49b3e;
            line-height: 1.4;
            text-shadow: 0 0 2px #e49b3e;
            /* Removed animation: flicker 0.15s infinite; */
            filter: brightness(1.1) contrast(1.1);
            box-shadow:
                inset 0 0 30px rgba(0, 0, 0, 0.9),
                inset 0 0 8px rgba(0, 0, 0, 0.8),
                0 0 5px rgba(0, 0, 0, 0.6);
            max-width: 80ch;
            margin: 0 auto;
        }
        .terminal-screen h2,
        .terminal-screen h3 {
            font-size: clamp(16px, 2vw, 20px);
            margin-bottom: 1em;
            color: #e49b3e;
        }
        .terminal-screen pre.code-block {
            font-size: clamp(10px, 1.3vw, 14px);
            white-space: pre; /* Changed from pre-wrap to pre */
            margin: 1em 0;
            background-color: #1a1a1a;
            padding: 1em;
            border-radius: 4px;
            color: #e49b3e;
            overflow-x: auto; /* Added to enable horizontal scrolling */
        }
        .terminal-screen::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                linear-gradient(
                    rgba(18, 16, 16, 0) 50%,
                    rgba(0, 0, 0, 0.25) 50%
                ),
                url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyBAMAAADsEZWCAAAAGFBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4o8JoAAAAB3RSTlMAGwQIEQMYADcPzwAAACJJREFUKM9jYBgFo2AU0Beg+A8YMCLxGYZCbNQEo4BaAAD5TQiR5wU9vAAAAABJRU5ErkJggg==");
            background-size: 100% 2.5px;
            /* Removed animation: scan 1s linear infinite; */
            pointer-events: none;
            z-index: 2;
        }
        .terminal-screen::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(
                circle at center,
                rgba(17, 17, 18, 0) 0%,
                rgba(17, 17, 18, 0.2) 50%,
                rgba(17, 17, 18, 0.15) 100%
            );
            border-radius: 20px;
            /* Removed animation: vignette-pulse 3s infinite; */
            pointer-events: none;
            z-index: 1;
        }
        .terminal-screen details {
            margin: 1em 0;
            padding: 0.5em;
            border: 1px solid #e49b3e;
            border-radius: 4px;
        }
        .terminal-screen summary {
            cursor: pointer;
            font-weight: bold;
            margin: -0.5em;
            padding: 0.5em;
            border-bottom: 1px solid #e49b3e;
            color: #e49b3e;
        }
        .terminal-screen details[open] summary {
            margin-bottom: 0.5em;
        }
        .badge-container,
        .coffee-container {
            text-align: center;
            margin: 1em 0;
        }
        .badge-container img,
        .coffee-container img {
            max-width: 100%;
            height: auto;
        }
        .terminal-screen a {
            color: #e49b3e;
            text-decoration: underline;
            transition: opacity 0.2s;
        }
        .terminal-screen a:hover {
            opacity: 0.8;
        }
        .terminal-screen strong,
        .terminal-screen em {
            color: #f0f0f0; /* off-white color for user/system messages */
        }
        .terminal-screen p {
            color: #f0f0f0; /* off-white color for assistant responses */
        }
        .terminal-screen p,
        .terminal-screen li {
            color: #e49b3e;
        }
        .terminal-screen code,
        .terminal-screen kbd,
        .terminal-screen samp {
            color: #e49b3e;
            font-family: "Consolas", monospace;
            text-shadow: 0 0 2px #e49b3e;
            background-color: #1a1a1a;
            padding: 0.2em 0.4em;
            border-radius: 4px;
        }
        .terminal-screen pre.code-block,
        .terminal-screen pre {
            font-size: clamp(10px, 1.3vw, 14px);
            white-space: pre; /* Changed from pre-wrap to pre */
            margin: 1em 0;
            background-color: #1a1a1a;
            padding: 1em;
            border-radius: 4px;
            color: #e49b3e;
            overflow-x: auto; /* Added to enable horizontal scrolling */
        }
        .mancer-button-container {
            text-align: left;
            margin: 1em 0;
        }
        .mancer-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #1a1a1a;
            color: #e49b3e;
            padding: 15px 15px;
            border: 2px solid #e49b3e;
            border-radius: 5px;
            text-decoration: none !important;
            box-shadow: 0 0 10px rgba(228, 155, 62, 0.3);
            transition: all 0.3s ease;
            position: relative;
        }
        .mancer-text {
            font-family: "Consolas", monospace;
            font-weight: bold;
            font-size: 20px;
            text-shadow: 0 0 2px #e49b3e;
            line-height: 1;
            display: inline-block;
            margin-left: -4px;
            margin-top: -2px;
        }
        .mancer-button::before {
            content: "⚡";
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            line-height: 1;
        }
        .mancer-button:hover {
            background: #2a2a2a;
            box-shadow: 0 0 15px rgba(228, 155, 62, 0.5);
            text-shadow: 0 0 4px #e49b3e;
            text-decoration: none !important;
        }
    </style>
</html>