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
- mistralai/Devstral-Small-2505
extra_gated_description: >-
  If you want to learn more about how we process your personal data, please read
  our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text2text-generation
---

# <span style="color: #7FFF7F;">Devstral-Small-2505 GGUF Models</span>


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

### `Devstral-Small-2505-bf16.gguf`  
- Model weights preserved in **BF16**.  
- Use this if you want to **requantize** the model into a different format.  
- Best if your device supports **BF16 acceleration**.  

### `Devstral-Small-2505-f16.gguf`  
- Model weights stored in **F16**.  
- Use if your device supports **FP16**, especially if BF16 is not available.  

### `Devstral-Small-2505-bf16-q8_0.gguf`  
- **Output & embeddings** remain in **BF16**.  
- All other layers quantized to **Q8_0**.  
- Use if your device supports **BF16** and you want a quantized version.  

### `Devstral-Small-2505-f16-q8_0.gguf`  
- **Output & embeddings** remain in **F16**.  
- All other layers quantized to **Q8_0**.    

### `Devstral-Small-2505-q4_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q4_K**.  
- Good for **CPU inference** with limited memory.  

### `Devstral-Small-2505-q4_k_s.gguf`  
- Smallest **Q4_K** variant, using less memory at the cost of accuracy.  
- Best for **very low-memory setups**.  

### `Devstral-Small-2505-q6_k.gguf`  
- **Output & embeddings** quantized to **Q8_0**.  
- All other layers quantized to **Q6_K** .  

### `Devstral-Small-2505-q8_0.gguf`  
- Fully **Q8** quantized model for better accuracy.  
- Requires **more memory** but offers higher precision.  

### `Devstral-Small-2505-iq3_xs.gguf`  
- **IQ3_XS** quantization, optimized for **extreme memory efficiency**.  
- Best for **ultra-low-memory devices**.  

### `Devstral-Small-2505-iq3_m.gguf`  
- **IQ3_M** quantization, offering a **medium block size** for better accuracy.  
- Suitable for **low-memory devices**.  

### `Devstral-Small-2505-q4_0.gguf`  
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




# Model Card for mistralai/Devstrall-Small-2505

Devstral is an agentic LLM for software engineering tasks built under a collaboration between [Mistral AI](https://mistral.ai/) and [All Hands AI](https://www.all-hands.dev/) 🙌. Devstral excels at using tools to explore codebases, editing multiple files and power software engineering agents. The model achieves remarkable performance on SWE-bench which positionates it as the #1 open source model on this [benchmark](#benchmark-results). 

It is finetuned from [Mistral-Small-3.1](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Base-2503), therefore it has a long context window of up to 128k tokens. As a coding agent, Devstral is text-only and before fine-tuning from `Mistral-Small-3.1` the vision encoder was removed.

For enterprises requiring specialized capabilities (increased context, domain-specific knowledge, etc.), we will release commercial models beyond what Mistral AI contributes to the community.

Learn more about Devstral in our [blog post](https://mistral.ai/news/devstral).


## Key Features:
- **Agentic coding**: Devstral is designed to excel at agentic coding tasks, making it a great choice for software engineering agents.
- **lightweight**: with its compact size of just 24 billion parameters, Devstral is light enough to run on a single RTX 4090 or a Mac with 32GB RAM, making it an appropriate model for local deployment and on-device use.
- **Apache 2.0 License**: Open license allowing usage and modification for both commercial and non-commercial purposes.
- **Context Window**: A 128k context window.
- **Tokenizer**: Utilizes a Tekken tokenizer with a 131k vocabulary size.



## Benchmark Results

### SWE-Bench

Devstral achieves a score of 46.8% on SWE-Bench Verified, outperforming prior open-source SoTA by 6%.

| Model            | Scaffold           | SWE-Bench Verified (%) |
|------------------|--------------------|------------------------|
| Devstral         | OpenHands Scaffold | **46.8**               |
| GPT-4.1-mini     | OpenAI Scaffold    | 23.6                   |
| Claude 3.5 Haiku | Anthropic Scaffold | 40.6                   |
| SWE-smith-LM 32B | SWE-agent Scaffold | 40.2                   |


 When evaluated under the same test scaffold (OpenHands, provided by All Hands AI 🙌), Devstral exceeds far larger models such as Deepseek-V3-0324 and Qwen3 232B-A22B.

![SWE Benchmark](assets/swe_bench.png)

## Usage

We recommend to use Devstral with the [OpenHands](https://github.com/All-Hands-AI/OpenHands/tree/main) scaffold.
You can use it either through our API or by running locally. 

### API 
Follow these [instructions](https://docs.mistral.ai/getting-started/quickstart/#account-setup) to create a Mistral account and get an API key.

Then run these commands to start the OpenHands docker container.
```bash
export MISTRAL_API_KEY=<MY_KEY>

docker pull docker.all-hands.dev/all-hands-ai/runtime:0.39-nikolaik

mkdir -p ~/.openhands-state && echo '{"language":"en","agent":"CodeActAgent","max_iterations":null,"security_analyzer":null,"confirmation_mode":false,"llm_model":"mistral/devstral-small-2505","llm_api_key":"'$MISTRAL_API_KEY'","remote_runtime_resource_factor":null,"github_token":null,"enable_default_condenser":true}' > ~/.openhands-state/settings.json

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.39-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.39
```

### Local inference 

You can also run the model locally. It can be done with LMStudio or other providers listed below.

Launch Openhands
You can now interact with the model served from LM Studio with openhands. Start the openhands server with the docker

```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik
docker run -it --rm --pull=always \
	-e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik \
	-e LOG_ALL_EVENTS=true \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v ~/.openhands-state:/.openhands-state \
	-p 3000:3000 \
	--add-host host.docker.internal:host-gateway \
	--name openhands-app \
	docker.all-hands.dev/all-hands-ai/openhands:0.38
```

The server will start at http://0.0.0.0:3000. Open it in your browser and you will see a tab AI Provider Configuration. 
Now you can start a new conversation with the agent by clicking on the plus sign on the left bar.


The model can also be deployed with the following libraries:
- [`LMStudio (recommended for quantized model)`](https://lmstudio.ai/): See [here](#lmstudio-recommended-for-quantized-model)
- [`vllm (recommended)`](https://github.com/vllm-project/vllm): See [here](#vllm-recommended)
- [`mistral-inference`](https://github.com/mistralai/mistral-inference): See [here](#mistral-inference)
- [`transformers`](https://github.com/huggingface/transformers): See [here](#transformers)
- [`ollama`](https://github.com/ollama/ollama): See [here](#ollama)


### OpenHands (recommended)

#### Launch a server to deploy Devstral-Small-2505

Make sure you launched an OpenAI-compatible server such as vLLM or Ollama as described above. Then, you can use OpenHands to interact with `Devstral-Small-2505`.

In the case of the tutorial we spineed up a vLLM server running the command:
```bash
vllm serve mistralai/Devstral-Small-2505 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --tensor-parallel-size 2
```

The server address should be in the following format: `http://<your-server-url>:8000/v1`

#### Launch OpenHands

You can follow installation of OpenHands [here](https://docs.all-hands.dev/modules/usage/installation).

The easiest way to launch OpenHands is to use the Docker image:
```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.38
```


Then, you can access the OpenHands UI at `http://localhost:3000`.

#### Connect to the server

When accessing the OpenHands UI, you will be prompted to connect to a server. You can use the advanced mode to connect to the server you launched earlier.

Fill the following fields:
- **Custom Model**: `openai/mistralai/Devstral-Small-2505`
- **Base URL**: `http://<your-server-url>:8000/v1`
- **API Key**: `token` (or any other token you used to launch the server if any)

#### Use OpenHands powered by Devstral

Now you're good to use Devstral Small inside OpenHands by **starting a new conversation**. Let's build a To-Do list app.

<details>
  <summary>To-Do list app</summary

1. Let's ask Devstral to generate the app with the following prompt:

```txt
Build a To-Do list app with the following requirements:
- Built using FastAPI and React.
- Make it a one page app that:
   - Allows to add a task.
   - Allows to delete a task.
   - Allows to mark a task as done.
   - Displays the list of tasks.
- Store the tasks in a SQLite database.
```

![Agent prompting](assets/tuto_open_hands/agent_prompting.png)


2. Let's see the result

You should see the agent construct the app and be able to explore the code it generated.

If it doesn't do it automatically, ask Devstral to deploy the app or do it manually, and then go the front URL deployment to see the app.

![Agent working](assets/tuto_open_hands/agent_working.png)
![App UI](assets/tuto_open_hands/app_ui.png)


3. Iterate

Now that you have a first result you can iterate on it by asking your agent to improve it. For example, in the app generated we could click on a task to mark it checked but having a checkbox would improve UX. You could also ask it to add a feature to edit a task, or to add a feature to filter the tasks by status.

Enjoy building with Devstral Small and OpenHands!

</details>


### LMStudio (recommended for quantized model)
Download the weights from huggingface:

```
pip install -U "huggingface_hub[cli]"
huggingface-cli download \
"mistralai/Devstral-Small-2505_gguf" \
--include "devstralQ4_K_M.gguf" \
--local-dir "mistralai/Devstral-Small-2505_gguf/"
```

You can serve the model locally with [LMStudio](https://lmstudio.ai/).
* Download [LM Studio](https://lmstudio.ai/) and install it
* Install `lms cli ~/.lmstudio/bin/lms bootstrap`
* In a bash terminal, run `lms import devstralQ4_K_M.ggu` in the directory where you've downloaded the model checkpoint (e.g. `mistralai/Devstral-Small-2505_gguf`)
* Open the LMStudio application, click the terminal icon to get into the developer tab. Click select a model to load and select Devstral Q4 K M. Toggle the status button to start the model, in setting oggle Serve on Local Network to be on.
* On the right tab, you will see an API identifier which should be devstralq4_k_m and an api address under API Usage. Keep note of this address, we will use it in the next step.

Launch Openhands
You can now interact with the model served from LM Studio with openhands. Start the openhands server with the docker

```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik
docker run -it --rm --pull=always \
	-e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.38-nikolaik \
	-e LOG_ALL_EVENTS=true \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v ~/.openhands-state:/.openhands-state \
	-p 3000:3000 \
	--add-host host.docker.internal:host-gateway \
	--name openhands-app \
	docker.all-hands.dev/all-hands-ai/openhands:0.38
```

Click “see advanced setting” on the second line. 
In the new tab, toggle advanced to on. Set the custom model to be mistral/devstralq4_k_m and Base URL the api address we get from the last step in LM Studio. Set API Key to dummy. Click save changes.

### vLLM (recommended)

We recommend using this model with the [vLLM library](https://github.com/vllm-project/vllm)
to implement production-ready inference pipelines.

**_Installation_**

Make sure you install [`vLLM >= 0.8.5`](https://github.com/vllm-project/vllm/releases/tag/v0.8.5):

```
pip install vllm --upgrade
```

Doing so should automatically install [`mistral_common >= 1.5.5`](https://github.com/mistralai/mistral-common/releases/tag/v1.5.5).

To check:
```
python -c "import mistral_common; print(mistral_common.__version__)"
```

You can also make use of a ready-to-go [docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile) or on the [docker hub](https://hub.docker.com/layers/vllm/vllm-openai/latest/images/sha256-de9032a92ffea7b5c007dad80b38fd44aac11eddc31c435f8e52f3b7404bbf39).

#### Server

We recommand that you use Devstral in a server/client setting. 

1. Spin up a server:

```
vllm serve mistralai/Devstral-Small-2505 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --tensor-parallel-size 2
```


2. To ping the client you can use a simple Python snippet.

```py
import requests
import json
from huggingface_hub import hf_hub_download


url = "http://<your-server-url>:8000/v1/chat/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}

model = "mistralai/Devstral-Small-2505"

def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    return system_prompt

SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "<your-command>",
            },
        ],
    },
]

data = {"model": model, "messages": messages, "temperature": 0.15}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()["choices"][0]["message"]["content"])
```


### Mistral-inference

We recommend using mistral-inference to quickly try out / "vibe-check" Devstral.

#### Install

Make sure to have mistral_inference >= 1.6.0 installed.

```bash
pip install mistral_inference --upgrade
```

#### Download

```python
from huggingface_hub import snapshot_download
from pathlib import Path

mistral_models_path = Path.home().joinpath('mistral_models', 'Devstral')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Devstral-Small-2505", allow_patterns=["params.json", "consolidated.safetensors", "tekken.json"], local_dir=mistral_models_path)
```

#### Python

You can run the model using the following command:

```bash
mistral-chat $HOME/mistral_models/Devstral --instruct --max_tokens 300
```

You can then prompt it with anything you'd like.

### Ollama

You can run Devstral using the [Ollama](https://ollama.ai/) CLI.

```bash
ollama run devstral
```

### Transformers

To make the best use of our model with transformers make sure to have [installed](https://github.com/mistralai/mistral-common) `    mistral-common >= 1.5.5` to use our tokenizer.

```bash
pip install mistral-common --upgrade
```

Then load our tokenizer along with the model and generate:

```python
import torch

from mistral_common.protocol.instruct.messages import (
    SystemMessage, UserMessage
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.tokens.tokenizers.tekken import SpecialTokenPolicy
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM

def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    return system_prompt

model_id = "mistralai/Devstral-Small-2505"
tekken_file = hf_hub_download(repo_id=model_id, filename="tekken.json")
SYSTEM_PROMPT = load_system_prompt(model_id, "SYSTEM_PROMPT.txt")

tokenizer = MistralTokenizer.from_file(tekken_file)

model = AutoModelForCausalLM.from_pretrained(model_id)

tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        messages=[
            SystemMessage(content=SYSTEM_PROMPT),
            UserMessage(content="<your-command>"),
        ],
    )
)

output = model.generate(
    input_ids=torch.tensor([tokenized.tokens]),
    max_new_tokens=1000,
)[0]

decoded_output = tokenizer.decode(output[len(tokenized.tokens):])
print(decoded_output)
```