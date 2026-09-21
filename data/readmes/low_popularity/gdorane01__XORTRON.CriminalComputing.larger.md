---
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: wtfpl
tags:
- heretic
- uncensored
- decensored
- abliterated
- transformers
base_model:
- mistralai/Mistral-Large-Instruct-2411
pipeline_tag: text-generation
library_name: transformers
---

![newGenerated Image February 27, 2026 - 6_06AM-topaz-sharpen-wonder](https://cdn-uploads.huggingface.co/production/uploads/6540a02d1389943fef4d2640/a4DcZkriSOFBWdu437a0f.jpeg)

---
# This is a decensored version of [mistralai/Mistral-Large-Instruct-2411](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0

## Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 37.86 |
| **attn.o_proj.max_weight** | 1.27 |
| **attn.o_proj.max_weight_position** | 64.44 |
| **attn.o_proj.min_weight** | 1.26 |
| **attn.o_proj.min_weight_distance** | 47.53 |
| **mlp.down_proj.max_weight** | 1.44 |
| **mlp.down_proj.max_weight_position** | 61.73 |
| **mlp.down_proj.min_weight** | 1.38 |
| **mlp.down_proj.min_weight_distance** | 46.10 |

## Performance

| Metric | This model | Original model ([mistralai/Mistral-Large-Instruct-2411](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0578 | 0 *(by definition)* |
| **Refusals** | 2/100 | 87/100 |

-----


# Model Card for Mistral-Large-Instruct-2411

Mistral-Large-Instruct-2411 is an advanced dense Large Language Model (LLM) of 123B parameters with state-of-the-art reasoning, knowledge and coding capabilities extending [Mistral-Large-Instruct-2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) with better Long Context, Function Calling and System Prompt.

## Key features
- **Multi-lingual by design:** Dozens of languages supported, including English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, Dutch and Polish.
- **Proficient in coding:** Trained on 80+ coding languages such as Python, Java, C, C++, Javacsript, and Bash. Also trained on more specific languages such as Swift and Fortran.
- **Agent-centric:** Best-in-class agentic capabilities with native function calling and JSON outputting.
- **Advanced Reasoning:** State-of-the-art mathematical and reasoning capabilities.
- **Mistral Research License:** Allows usage and modification for non-commercial usages.
- **Large Context:** A large 128k context window.
- **Robust Context Adherence:** Ensures strong adherence for RAG and large context applications.
- **System Prompt:** Maintains strong adherence and support for more reliable system prompts.

### System Prompt
We appreciate the feedback received from our community regarding our system prompt handling.  
In response, we have implemented stronger support for system prompts.  
To achieve optimal results, we recommend always including a system prompt that clearly outlines the bot's purpose, even if it is minimal.

### Basic Instruct Template (V7)

```
<s>[SYSTEM_PROMPT] <system prompt>[/SYSTEM_PROMPT][INST] <user message>[/INST] <assistant response></s>[INST] <user message>[/INST]
```

**Be careful with subtle missing or trailing white spaces!**

*Please make sure to use [mistral-common](https://github.com/mistralai/mistral-common) as the source of truth*

## Usage

The model can be used with the following frameworks

- [`vllm`](https://github.com/vllm-project/vllm): See [here](#vLLM)

### vLLM

We recommend using this model with the [vLLM library](https://github.com/vllm-project/vllm)
to implement production-ready inference pipelines.

**_Installation_**

Make sure you install [`vLLM >= v0.6.4.post1`](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1):

```
pip install --upgrade vllm
```

Also make sure you have [`mistral_common >= 1.5.0`](https://github.com/mistralai/mistral-common/releases/tag/v1.5.0) installed:

```
pip install --upgrade mistral_common
```

You can also make use of a ready-to-go [docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile) or on the [docker hub](https://hub.docker.com/layers/vllm/vllm-openai/latest/images/sha256-55a88146a4da0b6e193431b5b1d3492dfd7bebdc16919df4d031273e85a6157c?context=explore).

### Server

We recommand that you use Mistral-Large-Instruct-2411 in a server/client setting. 

1. Spin up a server:


```
vllm serve mistralai/Mistral-Large-Instruct-2411 --tokenizer_mode mistral --config_format mistral --load_format mistral --tensor_parallel_size 8
```

**Note:** Running Mistral-Large-Instruct-2411 on GPU requires over 300 GB of GPU RAM. 


2. To ping the client you can use a simple Python snippet.

```py
import requests
import json
from huggingface_hub import hf_hub_download
from datetime import datetime, timedelta

url = "http://<your-server>:8000/v1/chat/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}

model = "mistralai/Mistral-Large-Instruct-2411"


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
    {"role": "system", "content": SYSTEM_PROMPT + "\n\nThink step by step. You're a math genius."},
    {
        "role": "user",
        "content": "Think of four random numbers. Then add, substract or multiply them so that the solution is 10. If it's not possible, say it."
    },
]

data = {"model": model, "messages": messages}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()["choices"][0]["message"]["content"])
#  Sure, let's start by thinking of four random numbers. For example, let's take 3, 5, 2, and 1.
#
#  Now, we need to find a combination of addition, subtraction, or multiplication that results in 10.

#  Let's try:

#  \[ 3 + 5 + 2 - 1 = 9 \]

#  This doesn't work. Let's try another combination:

#  \[ 3 \times 2 + 5 - 1 = 6 + 5 - 1 = 10 \]

#  This works! So, with the numbers 3, 5, 2, and 1, we can achieve the result 10 by performing the operations \( 3 \times 2 + 5 - 1 \).
```

### Offline

```py
from vllm import LLM
from vllm.sampling_params import SamplingParams
from huggingface_hub import hf_hub_download
from datetime import datetime, timedelta

model_name = "mistralai/Mistral-Large-Instruct-2411"

def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, 'r') as file:
        system_prompt = file.read()
    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    model_name = repo_id.split("/")[-1]
    return system_prompt.format(name=model_name, today=today, yesterday=yesterday)


SYSTEM_PROMPT = load_system_prompt(model_name, "SYSTEM_PROMPT.txt") + "\n\nThink step by step. You're a math genius."

user_prompt = "Without browsing the web, how many days ago was Mistral founded?"

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": user_prompt
    },
]

# note that running this model on GPU requires over 300 GB of GPU RAM
llm = LLM(model=model_name, tokenizer_mode="mistral", tensor_parallel_size=8)

sampling_params = SamplingParams(max_tokens=512)

outputs = llm.chat(messages, sampling_params=sampling_params)

print(outputs[0].outputs[0].text)
# I don't have real-time web browsing capabilities or access to current data, but I can help you calculate the number of days based on the information I have.
#
#Mistral AI was founded in April 2023. To determine how many days ago that was from today's date, November 18, 2024, we need to calculate the total number of days between April 2023 and November 2024.
#
#Here's the step-by-step calculation:
#
#1. **Days from April 2023 to December 2023:**
#   - April 2023: 30 days (April has 30 days)
#   - May 2023: 31 days
#   - June 2023: 30 days
#   - July 2023: 31 days
#   - August 2023: 31 days
#   - September 2023: 30 days
#   - October 2023: 31 days
#   - November 2023: 30 days
#   - December 2023: 31 days
#
#   Total days in 2023 from April to December = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 = 275 days
#
#2. **Days from January 2024 to November 18, 2024:**
#   - January 2024: 31 days
#   - February 2024: 29 days (2024 is a leap year)
#   - March 2024: 31 days
#   - April 2024: 30 days
#   - May 2024: 31 days
#   - June 2024: 30 days
#   - July 2024: 31 days
#   - August 2024: 31 days
#   - September 2024: 30 days
#   - October 2024: 31 days
#   - November 2024 (up to the 18th): 18 days
#
#   Total days in 2024 from January to November 18 = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 18 = 323 days
#
#3. **Total days from April 2023 to November 18, 2024:**
#   Total days = 275 days (2023) + 323 days (2024) = 598 days
#
#Therefore, Mistral AI was founded 598 days ago from today's date, November 18, 2024.
```

### Improved Function Calling

Mistral-Large-2411 has much improved function calling capabilities that are fully supported 
using [`mistral_common >= 1.5.0`](https://github.com/mistralai/mistral-common/releases/tag/v1.5.0) and [`vLLM >= v0.6.4.post1`](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1).

Make sure to serve the model with the following flags in vLLM:

```
vllm serve mistralai/Pixtral-Large-Instruct-2411 --tokenizer_mode mistral --config_format mistral --load_format mistral --tensor-parallel-size 8 --tool-call-parser mistral --enable-auto-tool-choice
```

<details>
  <summary>Example</summary>

```py
import requests
import json
from huggingface_hub import hf_hub_download
from datetime import datetime, timedelta

url = "http://<your-server>:8000/v1/chat/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}

model = "mistralai/Mistral-Large-Instruct-2411"


def load_system_prompt(repo_id: str, filename: str) -> str:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    model_name = repo_id.split("/")[-1]
    return system_prompt.format(name=model_name, today=today, yesterday=yesterday)


SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "The state abbreviation, e.g. 'CA' for California",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit for temperature",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
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
        "content": "Could you please make the below article more concise?\n\nOpenAI is an artificial intelligence research laboratory consisting of the non-profit OpenAI Incorporated and its for-profit subsidiary corporation OpenAI Limited Partnership.",
    },
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "id": "bbc5b7ede",
                "type": "function",
                "function": {
                    "name": "rewrite",
                    "arguments": '{"text": "OpenAI is an artificial intelligence research laboratory consisting of the non-profit OpenAI Incorporated and its for-profit subsidiary corporation OpenAI Limited Partnership."}',
                },
            }
        ],
    },
    {
        "role": "tool",
        "content": '{"action":"rewrite","outcome":"OpenAI is a FOR-profit company."}',
        "tool_call_id": "bbc5b7ede",
        "name": "rewrite",
    },
    {
        "role": "assistant",
        "content": "---\n\nOpenAI is a FOR-profit company.",
    },
    {
        "role": "user",
        "content": "Can you tell me what the temperature will be in Dallas, in Fahrenheit?",
    },
]

data = {"model": model, "messages": messages, "tools": tools}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()["choices"][0]["message"]["tool_calls"])
# [{'id': '8PdihwL6d', 'type': 'function', 'function': {'name': 'get_current_weather', 'arguments': '{"city": "Dallas", "state": "TX", "unit": "fahrenheit"}'}}]
```

</details>

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Alok Kothari, Antoine Roux, Arthur Mensch, Audrey Herblin-Stoop, Augustin Garreau, Austin Birky, Bam4d, Baptiste Bout, Baudouin de Monicault, Blanche Savary, Carole Rambaud, Caroline Feldman, Devendra Singh Chaplot, Diego de las Casas, Diogo Costa, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger, Gaspard Blanchet, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona, Henri Roussez, Hichem Sattouf, Ian Mack, Jean-Malo Delignon, Jessica Chudnovsky, Justus Murke, Kartik Khandelwal, Lawrence Stewart, Louis Martin, Louis Ternon, Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat, Marie Torelli, Marie-Anne Lachaux, Marjorie Janiewicz, Mickaël Seznec, Nicolas Schuhl, Niklas Muhs, Olivier de Garrigues, Patrick von Platen, Paul Jacob, Pauline Buche, Pavan Kumar Reddy, Perry Savas, Pierre Stock, Romain Sauvestre, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Sophia Yang, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Wang, Théophile Gervet, Timothée Lacroix, Valera Nemychnikova, Wendy Shang, William El Sayed, William Marshall