---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- ar
- es
- pt
metrics:
- accuracy
base_model:
- BlinkDL/rwkv-7-world
pipeline_tag: text-generation
---

# <span style="color: #7FFF7F;">RWKV7-Goose-World3-2.9B-HF GGUF Models</span>

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

### `RWKV7-Goose-World3-2.9B-HF-bf16.gguf`  
- Model weights preserved in **BF16**.  
- Use this if you want to **requantize** the model into a different format.  
- Best if your device supports **BF16 acceleration**.  

### `RWKV7-Goose-World3-2.9B-HF-f16.gguf`  
- Model weights stored in **F16**.  
- Use if your device supports **FP16**, especially if BF16 is not available.  

### `RWKV7-Goose-World3-2.9B-HF-bf16-q8_0.gguf`  
- **Output & embeddings** remain in **BF16**.  
- All other layers quantized to **Q8_0**.  
- Use if your device supports **BF16** and you want a quantized version.  

### `RWKV7-Goose-World3-2.9B-HF-f16-q8_0.gguf`  
- **Output & embeddings** remain in **F16**.  
- All other layers quantized to **Q8_0**.    

### `RWKV7-Goose-World3-2.9B-HF-q4_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q4_K**.  
- Good for **CPU inference** with limited memory.  

### `RWKV7-Goose-World3-2.9B-HF-q4_k_s.gguf`  
- Smallest **Q4_K** variant, using less memory at the cost of accuracy.  
- Best for **very low-memory setups**.  

### `RWKV7-Goose-World3-2.9B-HF-q6_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q6_K** .  

### `RWKV7-Goose-World3-2.9B-HF-q8_0.gguf`  
- Fully **Q8** quantized model for better accuracy.  
- Requires **more memory** but offers higher precision.  

### `RWKV7-Goose-World3-2.9B-HF-iq3_xs.gguf`  
- **IQ3_XS** quantization, optimized for **extreme memory efficiency**.  
- Best for **ultra-low-memory devices**.  

### `RWKV7-Goose-World3-2.9B-HF-iq3_m.gguf`  
- **IQ3_M** quantization, offering a **medium block size** for better accuracy.  
- Suitable for **low-memory devices**.  

### `RWKV7-Goose-World3-2.9B-HF-q4_0.gguf`  
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



# rwkv7-2.9B-world 

<!-- Provide a quick summary of what the model is/does. -->

This is RWKV-7 model under flash-linear attention format.

## Model Details


### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Bo Peng, Yu Zhang, Songlin Yang, Ruichong Zhang
- **Funded by:** RWKV Project (Under LF AI & Data Foundation)
- **Model type:** RWKV7
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Parameter count:** 2.9B
- **Tokenizer:** RWKV World tokenizer
- **Vocabulary size:** 65,536

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/fla-org/flash-linear-attention ; https://github.com/BlinkDL/RWKV-LM
- **Paper:** With in Progress

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Install `flash-linear-attention` and the latest version of `transformers` before using this model:

```bash
pip install git+https://github.com/fla-org/flash-linear-attention
pip install 'transformers>=4.48.0'
```

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
You can use this model just as any other HuggingFace models:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('fla-hub/rwkv7-2.9B-world', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('fla-hub/rwkv7-2.9B-world', trust_remote_code=True)
model = model.cuda()
prompt = "What is a large language model?"
messages = [
    {"role": "user", "content": "Who are you?"},
    {"role": "assistant", "content": "I am a GPT-3 based model."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]
print(response)
```

### Training Data

This model is trained on the World v3 with a total of 3.119 trillion tokens.

#### Training Hyperparameters

- **Training regime:** bfloat16, lr 4e-4 to 1e-5 "delayed" cosine decay, wd 0.1 (with increasing batch sizes during the middle)
- **Final Loss:** 1.8745
- **Token Count:** 3.119 trillion

## FAQ
Q: safetensors metadata is none.

A: upgrade transformers to >=4.48.0: `pip install 'transformers>=4.48.0'`