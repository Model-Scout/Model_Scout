---
base_model:
- mistralai/Magistral-Small-2507
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
library_name: vllm
license: apache-2.0
inference: false
extra_gated_description: >-
  If you want to learn more about how we process your personal data, please read
  our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
---
# Magistral Small 1.1

Building upon Mistral Small 3.1 (2503), **with added reasoning capabilities**, undergoing SFT from Magistral Medium traces and RL on top, it's a small, efficient reasoning model with 24B parameters.

Magistral Small can be deployed locally, fitting within a single RTX 4090 or a 32GB RAM MacBook once quantized.

Learn more about Magistral in our [blog post](https://mistral.ai/news/magistral/).

The model was presented in the paper [Magistral](https://huggingface.co/papers/2506.10910).

## Updates compared with [Magistral Small 1.0](https://huggingface.co/mistralai/Magistral-Small-2506)

Magistral Small 1.1 should give you about the same performance as Mistral Small 1.0 as seen in the [benchmark results](#benchmark-results).

The update involves the following features:
- Better tone and model behaviour. You should experiment better LaTeX and Markdown formatting, and shorter answers on easy general prompts.
- The model is less likely to enter infinite generation loops.
- `[THINK]` and `[/THINK]` special tokens encapsulate the reasoning content in a thinking chunk. This makes it easier to parse the reasoning trace and prevents confusion when the '[THINK]' token is given as a string in the prompt.
- The reasoning prompt is now given in the system prompt.

## Key Features
- **Reasoning:** Capable of long chains of reasoning traces before providing an answer.
- **Multilingual:** Supports dozens of languages, including English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Malay, Nepali, Polish, Portuguese, Romanian, Russian, Serbian, Spanish, Turkish, Ukrainian, Vietnamese, Arabic, Bengali, Chinese, and Farsi.
- **Apache 2.0 License:** Open license allowing usage and modification for both commercial and non-commercial purposes.
- **Context Window:** A 128k context window, **but** performance might degrade past **40k**. Hence we recommend setting the maximum model length to 40k.

## Benchmark Results

| Model                    | AIME24 pass@1 | AIME25 pass@1 | GPQA Diamond | Livecodebench (v5) |
|---------------------------|---------------|---------------|--------------|--------------------|
| **Magistral Medium 1.1**  | 72.03%        | 60.99%        | 71.46%       | 59.35%             |
| Magistral Medium 1.0      | 73.59%        | 64.95%        | 70.83%       | 59.36%             |
| **Magistral Small 1.1**   | 70.52%        | 62.03%        | 65.78%       | 59.17%             |
| Magistral Small 1.0       | 70.68%        | 62.76%        | 68.18%       | 55.84%             |

## Sampling parameters

Please make sure to use: 
- `top_p`: 0.95
- `temperature`: 0.7
- `max_tokens`: 40960

## Basic Chat Template

We highly recommend including the following system prompt for the best results, you can edit and customise it if needed for your specific use case.

> First draft your thinking process (inner monologue) until you arrive at a response. Format your response using Markdown, and use LaTeX for any mathematical equations. Write both your thoughts and the response in the same language as the input.
>
> Your thinking process must follow the template below:[THINK]Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate the response. Use the same language as the input.[/THINK]Here, provide a self-contained response.


The `[THINK]` and `[/THINK]` are special tokens that **must** be encoded as such.

***Please make sure to use [mistral-common](https://github.com/mistralai/mistral-common) as the source of truth***. Find [below](#usage) examples from libraries supporting `mistral-common`.

We invite you to choose, depending on your use case and requirements, between keeping reasoning traces during multi-turn interactions or keeping only the final assistant response.


## Usage

The model can be used with the following frameworks;
- [`vllm (recommended)`](https://github.com/vllm-project/vllm): See [below](#vllm-recommended)
- [`transformers`](https://github.com/huggingface/transformers): See [below](#transformers)


### vLLM (recommended)

We recommend using this model with the [vLLM library](https://github.com/vllm-project/vllm)
to implement production-ready inference pipelines.

**_Installation_**

Make sure you install the latest [`vLLM`](https://github.com/vllm-project/vllm/) code:

```
pip install -U vllm \
    --pre \
    --extra-index-url https://wheels.vllm.ai/nightly
```

Doing so should automatically install [`mistral_common >= 1.8.2`](https://github.com/mistralai/mistral-common/releases/tag/v1.8.2).

To check:
```
python -c "import mistral_common; print(mistral_common.__version__)"
```

You can also make use of a ready-to-go [docker image](https://github.com/vllm-project/vllm/blob/main/Dockerfile) or on the [docker hub](https://hub.docker.com/layers/vllm/vllm-openai/latest/images/sha256-de9032a92ffea7b5c007dad80b38fd44aac11eddc31c435f8e52f3b7404bbf39).


Serve model as follows:

```
vllm serve mistralai/Magistral-Small-2507 --reasoning-parser mistral --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --tensor-parallel-size 2
```

Ping model as follows:

<details>
<summary>Python snippet</summary>

```python
from typing import Any
from openai import OpenAI
from huggingface_hub import hf_hub_download
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
TEMP = 0.7
TOP_P = 0.95
MAX_TOK = 40_960
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
def load_system_prompt(repo_id: str, filename: str) -> dict[str, Any]:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    index_begin_think = system_prompt.find("[THINK]")
    index_end_think = system_prompt.find("[/THINK]")
    return {
        "role": "system",
        "content": [
            {"type": "text", "text": system_prompt[:index_begin_think]},
            {
                "type": "thinking",
                "thinking": system_prompt[
                    index_begin_think + len("[THINK]") : index_end_think
                ],
                "closed": True,
            },
            {
                "type": "text",
                "text": system_prompt[index_end_think + len("[/THINK]") :],
            },
        ],
    }
SYSTEM_PROMPT = load_system_prompt(model, "SYSTEM_PROMPT.txt")
query = "Write 4 sentences, each with at least 8 words. Now make absolutely sure that every sentence has exactly one word less than the previous sentence."
# or try out other queries
# query = "Exactly how many days ago did the French Revolution start? Today is June 4th, 2025."
# query = "Think about 5 random numbers. Verify if you can combine them with addition, multiplication, subtraction or division to 133"
# query = "If it takes 30 minutes to dry 12 T-shirts in the sun, how long does it take to dry 33 T-shirts?"
messages = [
    SYSTEM_PROMPT,
    {"role": "user", "content": query}
]
stream = client.chat.completions.create(
  model=model,
  messages=messages,
  stream=True,
  temperature=TEMP,
  top_p=TOP_P,
  max_tokens=MAX_TOK,
)
print("client: Start streaming chat completions...:\n")
printed_reasoning_content = False
answer = []
for chunk in stream:
    reasoning_content = None
    content = None
    # Check the content is reasoning_content or content
    if hasattr(chunk.choices[0].delta, "reasoning_content"):
        reasoning_content = chunk.choices[0].delta.reasoning_content
    elif hasattr(chunk.choices[0].delta, "content"):
        content = chunk.choices[0].delta.content
    if reasoning_content is not None:
        if not printed_reasoning_content:
            printed_reasoning_content = True
            print("Start reasoning:\n", end="", flush=True)
        print(reasoning_content, end="", flush=True)
    elif content is not None:
        # Extract and print the content
        if not reasoning_content and printed_reasoning_content:
            answer.extend(content)
        print(content, end="", flush=True)
if answer:
    print("\n\n=============\nAnswer\n=============\n")
    print("".join(answer))
else:
    print("\n\n=============\nNo Answer\n=============\n")
    print("No answer was generated by the model, probably because the maximum number of tokens was reached.")
# client: Start streaming chat completions...:
#
# Start reasoning:
# First, I need to write ...
# ...
#
#
# =============
# Answer
# =============
# 
# Here are four sentences where each has at least 8 words, and each subsequent sentence has exactly one word less than the previous one:
# 1. The quick brown fox jumps over the lazy dog and rests.
# 2. The lazy dog rests under the big shady tree peacefully.
# 3. The big shady tree provides ample shade during summer.
# 4. The tree's leaves are very lush and green.
```

</details>

### Transformers

Make sure you install the latest [`Transformers`](https://github.com/huggingface/transformers/) code:

```sh
pip install git+https://github.com/huggingface/transformers
```

Also make sure to install [`mistral_common >= 1.8.2`](https://github.com/mistralai/mistral-common/releases/tag/v1.8.2):
```sh
pip install --upgrade mistral-common
```

To check:
```sh
python -c "import mistral_common; print(mistral_common.__version__)"
```

Now you can use Transformers with Magistral:

<details>
<summary>Python snippet</summary>

```python
from typing import Any
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoTokenizer
TEMP = 0.7
TOP_P = 0.95
MAX_TOK = 40_960
def load_system_prompt(repo_id: str, filename: str) -> dict[str, Any]:
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    with open(file_path, "r") as file:
        system_prompt = file.read()
    index_begin_think = system_prompt.find("[THINK]")
    index_end_think = system_prompt.find("[/THINK]")
    return {
        "role": "system",
        "content": [
            {"type": "text", "text": system_prompt[:index_begin_think]},
            {
                "type": "thinking",
                "thinking": system_prompt[
                    index_begin_think + len("[THINK]") : index_end_think
                ],
                "closed": True,
            },
            {
                "type": "text",
                "text": system_prompt[index_end_think + len("[/THINK]") :],
            },
        ],
    }
model_id = "mistralai/Magistral-Small-2507"
SYSTEM_PROMPT = load_system_prompt(model_id, "SYSTEM_PROMPT.txt")
query = "Think about 5 random numbers. Verify if you can combine them with addition, multiplication, subtraction or division to 133."
# or try out other queries
# query = "Exactly how many days ago did the French Revolution start? Today is June 4th, 2025."
# query = "Write 4 sentences, each with at least 8 words. Now make absolutely sure that every sentence has exactly one word less than the previous sentence."
# query = "If it takes 30 minutes to dry 12 T-shirts in the sun, how long does it take to dry 33 T-shirts?"
tokenizer = AutoTokenizer.from_pretrained(model_id, tokenizer_type="mistral", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)
input_ids = tokenizer.apply_chat_template(
    [
        SYSTEM_PROMPT,
        {"role": "user", "content": query},
    ],
)
output = model.generate(
    input_ids=torch.tensor([input_ids], device=model.device),
    pad_token_id=tokenizer.pad_token_id,
    eos_token_id=tokenizer.eos_token_id,
    temperature=TEMP,
    top_p=TOP_P,
    do_sample=True,
    max_new_tokens=MAX_TOK,
)[0]
decoded_output = tokenizer.decode(output[len(input_ids) :])
print(decoded_output)
# [THINK]Alright, I need to think of 5 random numbers first. Let's say I pick the numbers 5, 10, 2, 7, and 3.
# 
# Now, I need to see if I can combine these numbers using addition, multiplication, subtraction, or division to get 133.
# ...
# ...
# ...
# But if we're to find any five numbers that can be combined to make 133, then yes, such sets exist, like the one demonstrated above.[/THINK]Yes, it is possible to combine some sets of five random numbers to make 133 using basic arithmetic operations. For example, the numbers 13, 10, 1, 2, and 3 can be combined as follows to make 133:
# 
# \[ (13 \times 10) + (3 \times (2 - 1)) = 130 + 3 = 133 \]
# 
# However, not all sets of five random numbers can be combined in this way to make 133. For instance, with the numbers 5, 10, 2, 7, and 3, it is not possible to combine them using the allowed operations to get exactly 133.
# 
# Therefore, the ability to combine five random numbers to make 133 depends on the specific numbers chosen.
# 
# $133 = (13 \times 10) + (3 \times (2 - 1))$</s>
```

</details>