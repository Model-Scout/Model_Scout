---
license: other
license_name: modified-mit
license_link: https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE
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
base_model: mistralai/Mistral-Medium-3.5-128B
tags:
- vllm
- nvfp4
- quantized
- compressed-tensors
- llm-compressor
- blackwell
library_name: transformers
pipeline_tag: text-generation
---

# Mistral-Medium-3.5-128B-NVFP4

> **2026-05-03 Config Fix:** `rope_scaling.mscale_all_dim` in `config.json` has been corrected from `1.0` to `0.0`, matching the [upstream Mistral fix](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B). This parameter only affects YaRN attention scaling at inference time and has no impact on the quantized weights (this model uses data-free NVFP4A16 weight-only quantization — no recalibration needed). **If you have already downloaded this model, simply update this field in `config.json`. No need to re-download the weight files.**

NVFP4 (W4A16) quantization of [mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B), created with [llm-compressor](https://github.com/vllm-project/llm-compressor) in `compressed-tensors` `nvfp4-pack-quantized` format.

Designed for **vLLM** inference on **Blackwell-class GPUs** (compute capability 10.0+, e.g. RTX 5090 / B200).

## Quantization Details

- **Scheme:** NVFP4A16 (weights quantized to NVIDIA FP4, activations unquantized / weight-only)
- **Algorithm:** RTN (Round-To-Nearest) via `QuantizationModifier` with `scheme="NVFP4A16"`
- **Calibration data:** None. Fully **data-free** quantization, no calibration samples used.
- **Source model:** [mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) (FP8, per-tensor, `activation_scheme: static`)
- **Conversion:** FP8 weights dequantized to BF16 (`weight * weight_scale_inv`), then quantized to NVFP4A16
- **Tools:**
  - `llm-compressor` 0.10.1.dev125
  - `compressed-tensors` 0.15.1a20260428
  - `transformers` 5.7.0

### Model Size

| Component | Tensors | Format | Size |
|-----------|---------|--------|------|
| Language model (88 layers) | 1,848 | NVFP4 packed | 63.81 GiB |
| Vision tower (Pixtral) | 434 | BF16 (not quantized) | 4.65 GiB |
| Multi-modal projector | 4 | BF16 (not quantized) | 0.34 GiB |
| embed_tokens | 1 | BF16 (not quantized) | 3.00 GiB |
| lm_head | 1 | BF16 (not quantized) | 3.00 GiB |
| norm layers | 177 | BF16 | < 0.01 GiB |
| **Total** | **2,465** | **mixed** | **74.80 GiB** |

Source FP8 model: 124.43 GiB (tensor data). **Compression ratio: ~1.66x vs FP8, ~3.3x vs BF16**

### Serving with vLLM

Tested on a single NVIDIA RTX 6000 Pro (96 GiB VRAM), max context length 98,304 tokens:

```bash
vllm serve Mistral-Medium-3.5-128B-NVFP4 \
    --tokenizer-mode mistral \
    --max-model-len 98304 \
    --tool-call-parser mistral \
    --enable-auto-tool-choice \
    --max_num_batched_tokens 16384 \
    --max_num_seqs 1 \
    --gpu_memory_utilization 0.99 \
    --language-model-only \
    --kv-cache-dtype fp8_e4m3 \
    --kv-offloading-size 32 \
    --disable-hybrid-kv-cache-manager
```

> **Important:** `--tokenizer-mode mistral` is **required**. Without it, vLLM may not detect the Mistral tokenizer (since weight files use HuggingFace naming `model-*.safetensors` instead of Mistral-native `consolidated*.safetensors`), causing: `The tokenizer must be an instance of MistralTokenizer`.

> **Note:** 131K context requires ~22 GiB KV cache, which is tight on a single 96 GiB GPU. Use multi-GPU or increase `--kv-offloading-size` for longer contexts.

### Tested Environment

| Package | Version |
|---------|---------|
| vllm | 0.19.1 |
| mistral_common | 1.11.0 |
| transformers | 5.6.2 |
| torch | 2.10.0 |
| triton | 3.6.0 |
| tokenizers | 0.22.2 |

### Quantization Recipe

```python
from llmcompressor.modifiers.quantization import QuantizationModifier

recipe = QuantizationModifier(
    targets="Linear",
    scheme="NVFP4A16",
    ignore=[
        "lm_head",
        "re:.*embed_tokens$",
        "re:.*vision_tower.*",
        "re:.*multi_modal_projector.*",
    ],
)
```

---

# Original Model Card: Mistral Medium 3.5 128B

Mistral Medium 3.5 is our first flagship merged model. It is a dense 128B model with a 256k context window, handling instruction-following, reasoning,
and coding in a single set of weights. Mistral Medium 3.5 replaces its predecessor Mistral Medium 3.1 and Magistral in Le Chat. It also replaces Devstral 2 in our
coding agent Vibe. Concretely, expect better performance for instruct, reasoning and coding tasks in a new unified model in comparison with our previous released models.

Reasoning effort is configurable per request, so the same model can answer a quick chat reply or work through a complex agentic run. We trained the vision encoder from
scratch to handle variable image sizes and aspect ratios.

Find more information on our [blog](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5).

> [!Note]
> To speed up local inference using vLLM or SGLang, check out our released [EAGLE model](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B-EAGLE).

## Key Features

Mistral Medium 3.5 includes the following architectural choices:

- **Dense 128B parameters**.
- **256k context length**.
- **Multimodal input**: Accepts both text and image input, with text output.
- **Instruct and Reasoning functionalities** with function calls (reasoning effort configurable per request).

Mistral Medium 3.5 offers the following capabilities:

- **Reasoning Mode**: Toggle between fast instant reply mode and reasoning mode, boosting performance with test-time compute when requested.
- **Vision**: Analyzes images and provides insights based on visual content, in addition to text.
- **Multilingual**: Supports dozens of languages, including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, and Arabic.
- **System Prompt**: Strong adherence and support for system prompts.
- **Agentic**: Best-in-class agentic capabilities with native function calling and JSON output.
- **Large Context Window**: Supports a 256k context window.

We release this model under a **[Modified MIT License]((https://huggingface.co/mistralai/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE))**: Open-source license for both commercial and non-commercial use with exceptions for companies with large revenue.

## Recommended Settings

- **Reasoning Effort**:
  - `'none'` → Do not use reasoning
  - `'high'` → Use reasoning (recommended for complex prompts and agentic usage)
  Use `reasoning_effort="high"` for complex tasks and agentic coding.
- **Temperature**: 0.7 for `reasoning_effort="high"`. Temp between 0.0 and 0.7 for `reasoning_effort="none"` depending on the task.
  Generally, lower means answer that are more to the point and higher allows the model to be more creative. It is a good practice to try different values in order to
  improve the model performance to meet your demands. 

## Benchmarks

### Agentic Benchmarks

Mistral Medium 3.5 supersedes all our previous coding models, namely Devstral, across all benchmarks. It scores **91.4%** on τ³-Telecom and **77.6%** on SWE-Bench Verified. Due to its stronger agentic capabilities, Mistral Medium 3.5 replaces Devstral 2 in our coding agent, Vibe CLI.

![Mistral agentic benchmark](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/resolve/main/images/image2.png)
![Mistral agentic benchmark SWE-bench](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/resolve/main/images/image3.png)
![Mistral agentic vs competiting models benchmark](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/resolve/main/images/image4.png)

### Instruction Following, Reasoning, and Coding Benchmarks

We compared Mistral Medium 3.5 with competing models on instruction following, reasoning (math), and coding benchmarks. Thanks to its unified capabilities, it achieves strong results across all these tasks and Mistral Medium 3.5 is now powering Le Chat.

![instruct reasoning and agentic benchmark](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/resolve/main/images/image1.png)

## Usage

You can find Mistral Medium 3.5 support on multiple libraries for inference and fine-tuning.

We here **thank** every contributors and maintainers that helped us making it happen.

### Mistral-Vibe

Use `Mistral Medium 3.5` with [Mistral Vibe](https://github.com/mistralai/mistral-vibe). 

#### Install

Install the latest version:

```sh
uv pip install mistral-vibe --upgrade
```

#### API Usage

Mistral Medium 3.5 can be selected by starting `vibe`. If it is the first time you launch `vibe`, it will:

- Create a default configuration file at ~/.vibe/config.toml.
- Prompt you to enter your API key if it's not already configured.
- Save your API key to ~/.vibe/.env for future use.

Now select `mistral-medium-3.5` and start building !

#### Local server

If instead of pinging the Mistral API, you want to use a local vLLM server, you can do the following:
- 1. Spin up a vllm server as explained in [`Usage - vllm`](#vllm-recommended)
- 2. Add the model configuration in `~/.vibe/config.toml`:
 

```toml
display_name = "Mistral Medium 3.5 (local vLLM)"
description = "Mistral Medium 3.5 mode using local vLLM"
safety = "neutral"

active_model = "mistral-medium-3.5" # Make sure this is the only active_model entry
[[providers]]
name = "vllm"
api_base = "http://<your-host-url>:8000/v1"
api_key_env_var = ""
backend = "generic"
api_style = "reasoning"

[[models]]
name = "mistralai/Mistral-Medium-3.5-128B"
provider = "vllm"
alias = "mistral-medium-3.5"
thinking = "high"
temperature = 0.7
auto_compact_threshold = 168000

[tools.bash]
default_timeout = 1200
```

**Notes**:
- Make sure to overwrite `<your-host-url>` with your server's url.
- Other inference backends are also supported. Please look at [Mistral Vibe repo](https://github.com/mistralai/mistral-vibe) for more info.

Then restart `vibe` and "tab-shift" to "mistral-medium-3.5" mode.

Give it a try on some coding agentic tasks and start building some cool stuff !

### Inference

The model can be deployed with:
- [`vllm (recommended)`](https://github.com/vllm-project/vllm): See [here](#vllm-recommended).
- [`llama.cpp`](https://github.com/ggml-org/llama.cpp): WIP stay tuned !
- [`LM studio`](https://lmstudio.ai/): WIP stay tuned !
- [`Ollama`](https://ollama.com//): See [here](https://ollama.com/library/mistral-medium-3.5).
- [`SGLang`](https://github.com/sgl-project/sglang): See [here](#sglang).
- [`transformers`](https://github.com/huggingface/transformers): See [here](#transformers).

For optimal performance, we recommend using the Mistral AI API if local serving is subpar.

### Fine-Tuning

Fine-tune the model via:
- [`Axolotl`](https://github.com/axolotl-ai-cloud/axolotl): See [here](https://docs.axolotl.ai/docs/models/mistral-medium-3_5.html).
- [`Unsloth`](https://unsloth.ai/): See [here](https://unsloth.ai/docs/models/mistral-3.5).

## vLLM (Recommended)

We recommend using Mistral Medium 3.5 with the [vLLM library](https://github.com/vllm-project/vllm) for production-ready inference.

> [!Note]
> To speed up local inference using vLLM, check out our released [EAGLE model](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B-EAGLE)

### Installation

Make sure to install **vllm nightly**:

```
uv pip install -U vllm \
   --torch-backend=auto \
   --extra-index-url https://wheels.vllm.ai/nightly
```

Doing so should automatically install [`mistral_common >= 1.11.1`](https://github.com/mistralai/mistral-common/releases/tag/v1.11.0) and `transformers >= 5.4.0`.
  
To check:
```
python -c "import mistral_common; print(mistral_common.__version__)"
python -c "import transformers; print(transformers.__version__)"
```
  
You can also make use of a ready-to-go [docker image](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) or on the [docker hub](https://hub.docker.com/layers/vllm/vllm-openai/nightly).

### Serve the Model

We recommend a server/client setup:

```bash
vllm serve mistralai/Mistral-Medium-3.5-128B --tensor-parallel-size 8 \
  --tool-call-parser mistral --enable-auto-tool-choice --reasoning-parser mistral --max_num_batched_tokens 16384 --max_num_seqs 128 \
  --gpu_memory_utilization 0.8
```

### Ping the Server

<details>
  <summary>Instruction Following</summary>

Mistral Medium 3.5 can follow your instructions to the letter.


```python
from datetime import datetime, timedelta

from openai import OpenAI
from huggingface_hub import hf_hub_download

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

TEMP = 0.1
# use TEMP = 0.7 for reasoning="high"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id


def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    model_name = repo_id.split("/")[-1]
    return system_prompt.format(name=model_name, today=today, yesterday=yesterday)


SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": "Write me a sentence where every word starts with the next letter in the alphabet - start with 'a' and end with 'z'.",
    },
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=TEMP,
    reasoning_effort="none",
)

assistant_message = response.choices[0].message.content
print(assistant_message)
```

</details>

<details>
  <summary>Tool Call</summary>

Let's solve some equations thanks to our simple Python calculator tool.


```python
import json
from datetime import datetime, timedelta

from openai import OpenAI
from huggingface_hub import hf_hub_download

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

TEMP = 0.1

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id


def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    model_name = repo_id.split("/")[-1]
    return system_prompt.format(name=model_name, today=today, yesterday=yesterday)


SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")

image_url = "https://math-coaching.com/img/fiche/46/expressions-mathematiques.jpg"


def my_calculator(expression: str) -> str:
    return str(eval(expression))


tools = [
    {
        "type": "function",
        "function": {
            "name": "my_calculator",
            "description": "A calculator that can evaluate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate.",
                    },
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "rewrite",
            "description": "Rewrite a given text for improved clarity",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The input text to rewrite",
                    }
                },
            },
        },
    },
]

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Thanks to your calculator, compute the results for the equations that involve numbers displayed in the image.",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
            },
        ],
    },
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=TEMP,
    tools=tools,
    tool_choice="auto",
    reasoning_effort="none",
)

tool_calls = response.choices[0].message.tool_calls

results = []
for tool_call in tool_calls:
    function_name = tool_call.function.name
    function_args = tool_call.function.arguments
    if function_name == "my_calculator":
        result = my_calculator(**json.loads(function_args))
        results.append(result)

messages.append({"role": "assistant", "tool_calls": tool_calls})
for tool_call, result in zip(tool_calls, results):
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": result,
        }
    )


response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=TEMP,
    reasoning_effort="none",
)

print(response.choices[0].message.content)
```

</details>

<details>
  <summary>Vision Reasoning</summary>

Let's see if the Mistral Medium 3.5 knows when to pick a fight !

```python
from datetime import datetime, timedelta

from openai import OpenAI
from huggingface_hub import hf_hub_download

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

TEMP = 0.7

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id


def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    model_name = repo_id.split("/")[-1]
    return system_prompt.format(name=model_name, today=today, yesterday=yesterday)


SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")
image_url = "https://static.wikia.nocookie.net/essentialsdocs/images/7/70/Battle.png/revision/latest?cb=20220523172438"

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What action do you think I should take in this situation? List all the possible actions and explain why you think they are good or bad.",
            },
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    },
]


response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=TEMP,
    reasoning_effort="high",
)

print(response.choices[0].message.content)
```

</details>

## SGLang

Serve Mistral Medium 3.5 with the [SGLang library](https://github.com/sgl-project/sglang) for production-ready inference.

> [!Note]
> To speed up local inference using SGLang, check out our released [EAGLE model](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B-EAGLE).

### Installation

Day-zero support ships in dedicated docker tags:

```
docker pull lmsysorg/sglang:dev-mistral-medium-3.5         # H100 / H200 (Hopper, CUDA 12.9)
docker pull lmsysorg/sglang:dev-cu13-mistral-medium-3.5    # B200 / B300 (Blackwell, CUDA 13.0)
```

Or follow the [SGLang installation guide](https://docs.sglang.io/docs/get-started/install). Requires `transformers >= 5.4.0`.

### Serve the Model

```bash
python -m sglang.launch_server --model-path mistralai/Mistral-Medium-3.5-128B \
  --tp 8 --tool-call-parser mistral --reasoning-parser mistral
```

For the full deployment guide, benchmarks, and per-request examples (reasoning effort, tool calls, vision, streaming), see the [SGLang cookbook entry for Mistral Medium 3.5](https://docs.sglang.io/cookbook/autoregressive/Mistral/Mistral-Medium-3.5).

## Transformers

### Installation

First install the [Transformers framework](https://github.com/huggingface/transformers/) to use Mistral Medium 3.5:

```bash
uv pip install transformers
```

### Inference

<details>
<summary>Python Inference Snippet</summary>

```python
import torch
from transformers import AutoProcessor, Mistral3ForConditionalGeneration


model_id = "mistralai/Mistral-Medium-3.5-128B"

processor = AutoProcessor.from_pretrained(model_id)
model = Mistral3ForConditionalGeneration.from_pretrained(
    model_id, device_map="auto"
)

image_url = "https://static.wikia.nocookie.net/essentialsdocs/images/7/70/Battle.png/revision/latest?cb=20220523172438"

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What action do you think I should take in this situation? List all the possible actions and explain why you think they are good or bad.",
            },
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    },
]

inputs = processor.apply_chat_template(messages, return_tensors="pt", tokenize=True, return_dict=True, reasoning_effort="high")
inputs = inputs.to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=1024,
    do_sample=True,
    temperature=0.7,
)[0]

# Setting `skip_special_tokens=False` to visualize reasoning trace between [THINK] [/THINK] tags.
decoded_output = processor.decode(output[len(inputs["input_ids"][0]):], skip_special_tokens=False) 
print(decoded_output)
```
</details>


## License

This model is licensed under a [Modified MIT License](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE).

*You must not use this model in a manner that infringes, misappropriates, or otherwise violates any third party’s rights, including intellectual property rights.*