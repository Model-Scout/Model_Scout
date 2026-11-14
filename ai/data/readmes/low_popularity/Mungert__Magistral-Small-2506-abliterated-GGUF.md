---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: vllm
inference: false
base_model:
- mistralai/Magistral-Small-2506
extra_gated_description: >-
  If you want to learn more about how we process your personal data, please read
  our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text2text-generation
tags:
- chat
- abliterated
- uncensored
extra_gated_prompt: >-
    **Usage Warnings**


    “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

    “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

    “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

    “**Research and Experimental Use**“: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

    “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

    “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.


---

# <span style="color: #7FFF7F;">Magistral-Small-2506-abliterated GGUF Models</span>


## <span style="color: #7F7FFF;">Model Generation Details</span>

This model was generated using [llama.cpp](https://github.com/ggerganov/llama.cpp) at commit [`7f4fbe51`](https://github.com/ggerganov/llama.cpp/commit/7f4fbe5183b23b6b2e25fd1ccc5d1fa8bb010cb7).





---

## <span style="color: #7FFF7F;">Quantization Beyond the IMatrix</span>

I've been experimenting with a new quantization approach that selectively elevates the precision of key layers beyond what the default IMatrix configuration provides.

In my testing, standard IMatrix quantization underperforms at lower bit depths, especially with Mixture of Experts (MoE) models. To address this, I'm using the `--tensor-type` option in `llama.cpp` to manually "bump" important layers to higher precision. You can see the implementation here:  
👉 [Layer bumping with llama.cpp](https://github.com/Mungert69/GGUFModelBuilder/blob/main/model-converter/tensor_list_builder.py)

While this does increase model file size, it significantly improves precision for a given quantization level.

### **I'd love your feedback—have you tried this? How does it perform for you?**




---

<a href="https://readyforquantum.com/huggingface_gguf_selection_guide.html" style="color: #7FFF7F;">
  Click here to get info on choosing the right GGUF model format
</a>

---



<!--Begin Original Model Card-->


# huihui-ai/Magistral-Small-2506-abliterated

This is an uncensored version of [mistralai/Magistral-Small-2506](https://huggingface.co/mistralai/Magistral-Small-2506) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 

## ollama

You can use [huihui_ai/magistral-abliterated](https://ollama.com/huihui_ai/magistral-abliterated) directly, 
Switch the thinking toggle using /set think and /set nothink
```
ollama run huihui_ai/magistral-abliterated
```

## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TextStreamer
import torch
import os
import signal
import time
import numpy as np
import random

cpu_count = os.cpu_count()
print(f"Number of CPU cores in the system: {cpu_count}")
half_cpu_count = cpu_count // 2
os.environ["MKL_NUM_THREADS"] = str(half_cpu_count)
os.environ["OMP_NUM_THREADS"] = str(half_cpu_count)
torch.set_num_threads(half_cpu_count)

print(f"PyTorch threads: {torch.get_num_threads()}")
print(f"MKL threads: {os.getenv('MKL_NUM_THREADS')}")
print(f"OMP threads: {os.getenv('OMP_NUM_THREADS')}")

# Load the model and tokenizer
NEW_MODEL_ID = "huihui-ai/Magistral-Small-2506-abliterated"
print(f"Load Model {NEW_MODEL_ID} ... ")

tokenizer = AutoTokenizer.from_pretrained(NEW_MODEL_ID, trust_remote_code=True)
#if tokenizer.pad_token is None:
#    tokenizer.pad_token = tokenizer.eos_token
#tokenizer.pad_token_id = tokenizer.eos_token_id

quant_config_4 = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    llm_int14_enable_fp32_cpu_offload=True,
)

model = AutoModelForCausalLM.from_pretrained(
    NEW_MODEL_ID,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=quant_config_4,
    torch_dtype=torch.bfloat16
)

def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = f"{repo_id}/{filename}"
    with open(file_path, "r") as file:
        system_prompt = file.read()
    return system_prompt

SYSTEM_PROMPT = load_system_prompt(NEW_MODEL_ID, "SYSTEM_PROMPT.txt")


initial_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
messages = initial_messages.copy()
nothink = False
same_seed = False
skip_prompt=True
skip_special_tokens=True
do_sample = True

def set_random_seed(seed=None):
    """Set random seed for reproducibility. If seed is None, use int(time.time())."""
    if seed is None:
        seed = int(time.time())  # Convert float to int
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # If using CUDA
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    return seed  # Return seed for logging if needed
    
def apply_chat_template(tokenizer, messages, nothink, add_generation_prompt=True):
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
    )
    if nothink:
        input_ids += "\n<think>\n\n</think>\n"
    return input_ids

class CustomTextStreamer(TextStreamer):
    def __init__(self, tokenizer, skip_prompt=True, skip_special_tokens=True):
        super().__init__(tokenizer, skip_prompt=skip_prompt, skip_special_tokens=skip_special_tokens)
        self.generated_text = ""
        self.stop_flag = False
        self.init_time = time.time()  # Record initialization time
        self.end_time = None  # To store end time
        self.first_token_time = None  # To store first token generation time
        self.token_count = 0  # To track total tokens

    def on_finalized_text(self, text: str, stream_end: bool = False):
        if self.first_token_time is None and text.strip():  # Set first token time on first non-empty text
            self.first_token_time = time.time()
        self.generated_text += text
        # Count tokens in the generated text
        tokens = self.tokenizer.encode(text, add_special_tokens=False)
        self.token_count += len(tokens)
        print(text, end="", flush=True)
        if stream_end:
            self.end_time = time.time()  # Record end time when streaming ends
        if self.stop_flag:
            raise StopIteration

    def stop_generation(self):
        self.stop_flag = True
        self.end_time = time.time()  # Record end time when generation is stopped

    def get_metrics(self):
        """Returns initialization time, first token time, first token latency, end time, total time, total tokens, and tokens per second."""
        if self.end_time is None:
            self.end_time = time.time()  # Set end time if not already set
        total_time = self.end_time - self.init_time  # Total time from init to end
        tokens_per_second = self.token_count / total_time if total_time > 0 else 0
        first_token_latency = (self.first_token_time - self.init_time) if self.first_token_time is not None else None
        metrics = {
            "init_time": self.init_time,
            "first_token_time": self.first_token_time,
            "first_token_latency": first_token_latency,
            "end_time": self.end_time,
            "total_time": total_time,  # Total time in seconds
            "total_tokens": self.token_count,
            "tokens_per_second": tokens_per_second
        }
        return metrics
        
def generate_stream(model, tokenizer, messages, nothink, skip_prompt, skip_special_tokens, do_sample, max_new_tokens):
    formatted_prompt = apply_chat_template(tokenizer, messages, nothink)
    input_ids = tokenizer(
        formatted_prompt,
        return_tensors="pt",
        return_attention_mask=True,
        padding=False
    )
    
    tokens = input_ids['input_ids'].to(model.device)
    attention_mask = input_ids['attention_mask'].to(model.device)

    streamer = CustomTextStreamer(tokenizer, skip_prompt=skip_prompt, skip_special_tokens=skip_special_tokens)

    def signal_handler(sig, frame):
        streamer.stop_generation()
        print("\n[Generation stopped by user with Ctrl+C]")

    signal.signal(signal.SIGINT, signal_handler)

    if do_sample:
        generate_kwargs = {
              "do_sample": do_sample,
              "max_length": max_new_tokens,
              "temperature": 0.6,
              "top_k": 20,
              "top_p": 0.95,
              "repetition_penalty": 1.2,
              "no_repeat_ngram_size": 2
        }
    else:
        generate_kwargs = {
              "do_sample": do_sample,
              "max_length": max_new_tokens,
              "repetition_penalty": 1.2,
              "no_repeat_ngram_size": 2
        }
            
    print("Response: ", end="", flush=True)
    try:
        generated_ids = model.generate(
            tokens,
            attention_mask=attention_mask,
            #use_cache=False,
            pad_token_id=tokenizer.pad_token_id,
            streamer=streamer,
            **generate_kwargs
        )
        del generated_ids
    except StopIteration:
        print("\n[Stopped by user]")

    del input_ids, attention_mask
    torch.cuda.empty_cache()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    return streamer.generated_text, streamer.stop_flag, streamer.get_metrics()

init_seed = set_random_seed()

while True:
    if same_seed:
        set_random_seed(init_seed)
    else:
        init_seed = set_random_seed()
        
    print(f"\nnothink: {nothink}")
    print(f"skip_prompt: {skip_prompt}")
    print(f"skip_special_tokens: {skip_special_tokens}")
    print(f"do_sample: {do_sample}")
    print(f"same_seed: {same_seed}, {init_seed}\n")
    
    user_input = input("User: ").strip()
    if user_input.lower() == "/exit":
        print("Exiting chat.")
        break
    if user_input.lower() == "/clear":
        messages = initial_messages.copy()
        print("Chat history cleared. Starting a new conversation.")
        continue
    if user_input.lower() == "/nothink":
        nothink = not nothink
        continue
    if user_input.lower() == "/skip_prompt":
        skip_prompt = not skip_prompt
        continue
    if user_input.lower() == "/skip_special_tokens":
        skip_special_tokens = not skip_special_tokens
        continue
    if user_input.lower().startswith("/same_seed"):
        parts = user_input.split()
        if len(parts) == 1:  # /same_seed (no number)
            same_seed = not same_seed  # Toggle switch
        elif len(parts) == 2:  # /same_seed <number>
            try:
                init_seed = int(parts[1])  # Extract and convert number to int
                same_seed = True
            except ValueError:
                print("Error: Please provide a valid integer after /same_seed")       
        continue
    if user_input.lower() == "/do_sample":
        do_sample = not do_sample
        continue
    if not user_input:
        print("Input cannot be empty. Please enter something.")
        continue
    
    messages.append({"role": "user", "content": user_input})
    response, stop_flag, metrics = generate_stream(model, tokenizer, messages, nothink, skip_prompt, skip_special_tokens, do_sample, 40960)
    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    print("", flush=True)
    if stop_flag:
        continue
    messages.append({"role": "assistant", "content": response})

```


### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

If you have any questions, insights, or specific ablation models you want to request, please send an email to support@huihui.ai

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```


<!--End Original Model Card-->

---

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>

Help me test my **AI-Powered Free Network Monitor Assistant** with **quantum-ready security checks**:  

👉 [Free Network Monitor](https://readyforquantum.com/?assistant=open&utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  


The full Open Source Code for the Free Network Monitor Service available at my github repos ( repos with NetworkMonitor in the name) : [Source Code Free Network Monitor](https://github.com/Mungert69). You will also find the code I use to quantize the models if you want to do it yourself [GGUFModelBuilder](https://github.com/Mungert69/GGUFModelBuilder)

💬 **How to test**:  
 Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4.1-mini)  
   - `HugLLM` (Hugginface Open-source models)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap security scans**  
  - **Quantum-readiness checks**  
  - **Network Monitoring tasks**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 2 CPU threads on huggingface docker space):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**) . No token limited as the cost is low.
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4.1-mini** :
- **It performs very well but unfortunatly OpenAI charges per token. For this reason tokens usage is limited. 
- **Create custom cmd processors to run .net code on Free Network Monitor Agents**
- **Real-time network diagnostics and monitoring**
- **Security Audits**
- **Penetration testing** (Nmap/Metasploit)  

🔵 **HugLLM** – Latest Open-source models:  
- 🌐 Runs on Hugging Face Inference API. Performs pretty well using the lastest models hosted on Novita.

### 💡 **Example commands you could test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a comprehensive security audit on my server"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a Free Network Monitor Agent to run the .net code from. This is a very flexible and powerful feature. Use with caution!

### Final Word

I fund the servers used to create these model files, run the Free Network Monitor service, and pay for inference from Novita and OpenAI—all out of my own pocket. All the code behind the model creation and the Free Network Monitor project is [open source](https://github.com/Mungert69). Feel free to use whatever you find helpful.

If you appreciate the work, please consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) ☕. Your support helps cover service costs and allows me to raise token limits for everyone.

I'm also open to job opportunities or sponsorship.

Thank you! 😊
