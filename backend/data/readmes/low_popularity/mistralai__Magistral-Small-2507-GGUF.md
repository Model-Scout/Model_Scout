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
library_name: llama.cpp
inference: false
base_model:
- mistralai/Magistral-Small-2507
extra_gated_description: >-
  If you want to learn more about how we process your personal data, please read
  our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
---

> [!Note]
> At Mistral, we don't yet have too much experience with providing GGUF-quantized checkpoints
> to the community, but want to help improving the ecosystem going forward.
> If you encounter any problems with the provided checkpoints here, please open a discussion or pull request


# Magistral Small 1.1 (GGUF)

Building upon Mistral Small 3.1 (2503), **with added reasoning capabilities**, undergoing SFT from Magistral Medium traces and RL on top, it's a small, efficient reasoning model with 24B parameters.

Magistral Small can be deployed locally, fitting within a single RTX 4090 or a 32GB RAM MacBook once quantized.

This is the GGUF version of the [Magistral-Small-2507](https://huggingface.co/mistralai/Magistral-Small-2507) model. We released the BF16 weights as well as the following quantized format:
- Q8_0
- Q5_K_M
- Q4_K_M
Our format **does not have a chat template** and instead we recommend to use [`mistral-common`](#usage).

## Updates compared with [Magistral Small 1.0](https://huggingface.co/mistralai/Magistral-Small-2506)

Magistral Small 1.1 should give you about the same performance as Magistral Small 1.0 as seen in the [benchmark results](#benchmark-results).

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

## Usage

We recommend to use Magistral with [llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master) along with [mistral-common >= 1.8.3](https://mistralai.github.io/mistral-common/) server. See [here](https://mistralai.github.io/mistral-common/usage/experimental/) for the documentation of `mistral-common` server.

### Install

1. Install `llama.cpp` following their [guidelines](https://github.com/ggml-org/llama.cpp/blob/master/README.md#quick-start).

2. Install `mistral-common` with its dependencies.

```sh
pip install mistral-common[server]
```

3. Download the weights from huggingface.

```sh
pip install -U "huggingface_hub[cli]"

huggingface-cli download \
"mistralai/Magistral-Small-2507-GGUF" \
--include "Magistral-Small-2507-Q4_K_M.gguf" \
--local-dir "mistralai/Magistral-Small-2507-GGUF/"
```

### Launch the servers

1. Launch the `llama.cpp` server

```sh
llama-server -m mistralai/Magistral-Small-2507-GGUF/Magistral-Small-2507-Q4_K_M.gguf -c 0
```

2. Launch the `mistral-common` server and pass the url of the `llama.cpp` server.

This is the server that will handle tokenization and detokenization and call the `llama.cpp` server for generations.

```sh
mistral_common serve mistralai/Magistral-Small-2507 \
--host localhost --port 6000 \
--engine-url http://localhost:8080 --engine-backend llama_cpp \
--timeout 300
```

### Use the model

1. let's define the function to call the servers:

**generate**: call `mistral-common` that will tokenizer, call the `llama.cpp` server to generate new tokens and detokenize the output to an [`AssistantMessage`](https://mistralai.github.io/mistral-common/code_reference/mistral_common/protocol/instruct/messages/#mistral_common.protocol.instruct.messages.AssistantMessage) with think chunk and tool calls parsed.

```python
from mistral_common.protocol.instruct.messages import AssistantMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.experimental.app.models import OpenAIChatCompletionRequest
from fastapi.encoders import jsonable_encoder
import requests

mistral_common_url = "http://127.0.0.1:6000"

def generate(
    request: dict | ChatCompletionRequest | OpenAIChatCompletionRequest, url: str
) -> AssistantMessage:
    response = requests.post(
        f"{url}/v1/chat/completions", json=jsonable_encoder(request)
    )
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code} - {response.text}")
    return AssistantMessage(**response.json())
```

2. Tokenize the input, call the model and detokenize

```python
from typing import Any
from huggingface_hub import hf_hub_download


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

SYSTEM_PROMPT = load_system_prompt("mistralai/Magistral-Small-2507", "SYSTEM_PROMPT.txt")

query = "Write 4 sentences, each with at least 8 words. Now make absolutely sure that every sentence has exactly one word less than the previous sentence."
# or try out other queries
# query = "Exactly how many days ago did the French Revolution start? Today is June 4th, 2025."
# query = "Think about 5 random numbers. Verify if you can combine them with addition, multiplication, subtraction or division to 133"
# query = "If it takes 30 minutes to dry 12 T-shirts in the sun, how long does it take to dry 33 T-shirts?"
messages = [SYSTEM_PROMPT, {"role": "user", "content": [{"type": "text", "text": query}]}]

request = {"messages": messages, "temperature": TEMP, "top_p": TOP_P, "max_tokens": MAX_TOK}

generated_message = generate(request, mistral_common_url)
print(generated_message)
```

