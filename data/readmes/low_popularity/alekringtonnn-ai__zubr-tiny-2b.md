---
license: apache-2.0
language:
- zh
- en
- ru
- fr
- es
- pt
- de
- be
- it
- ja
- ko
- vi
- th
- ar
- id
- ms
- tl
- nl
- pl
- uk
- be
- tr
- hi
- fa
- uz
- kk
- ur
- bn
- ta
- te
base_model:
- Qwen/Qwen3.5-2B
pipeline_tag: text-generation
---
# zubr-tiny-2b

## Model Overview
**zubr-tiny-2b** is a lightweight, fine-tuned conversational language model based on the state-of-the-art **Qwen 3.5** (and Qwen 2.5 architecture ecosystem) developed by **alekringtonnn-ai**. 

By leveraging the powerful foundations of the Qwen series, this **2-billion parameter model** offers exceptional multi-lingual capabilities, reasoning, and instruction-following proficiency while maintaining an incredibly small hardware footprint. It is highly optimized for fast local inference, low RAM/VRAM consumption, and efficient deployment on consumer-grade hardware such as laptops and edge devices.

## How to Download via Terminal

You can easily download the model weights and configuration files directly from Hugging Face using your terminal. Choose one of the methods below:

### Method 1: Using Hugging Face CLI (Recommended)
This is the most efficient method to download the repository or specific model shards.

1. **Install or update the Hugging Face Hub CLI:**
   ```bash
   pip install -U huggingface_hub
   ```

2. **Download the complete repository:**
   ```bash
   huggingface-cli download alekringtonnn-ai/zubr-tiny-2b
   ```

3. **Download to a specific local directory:**
   ```bash
   huggingface-cli download alekringtonnn-ai/zubr-tiny-2b --local-dir ./zubr-tiny-2b
   ```

### Method 2: Using Git LFS
If you prefer working with standard Git workflows, make sure Git Large File Storage is installed.

1. **Initialize Git LFS:**
   ```bash
   git lfs install
   ```

2. **Clone the repository:**
   ```bash
   git clone https://huggingface.co
   ```

### Method 3: Direct Download via cURL
To pull specific configurations or single files without Python dependencies:

```bash
curl -L -O https://huggingface.co/resolve/main/config.json
```

## Quick Start (Python)

Since the model is based on **Qwen**, it is fully compatible with the standard `transformers` library. You can run it locally using the following snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "alekringtonnn-ai/zubr-tiny-2b"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", 
    torch_dtype="auto"
)

# Format your prompt
prompt = "Привет! Расскажи о себе."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Generate response
inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=512)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

## Features & Limitations
* **Base Architecture:** Qwen 3.5 / Qwen 2.5 2B.
* **Context Length:** Inherits the extended context window support from the base Qwen architecture.
* **Target Use Case:** Perfect for private local chatbots, text summarization, and embedded tasks where resources are highly constrained.