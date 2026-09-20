---
license: apache-2.0
base_model: mistralai/Mixtral-8x22B-Instruct-v0.1
inference: false
model_creator: MaziyarPanahi
model_name: Mixtral-8x22B-Instruct-v0.1-GGUF
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
tags:
- quantized
- 2-bit
- 3-bit
- 4-bit
- 5-bit
- 6-bit
- 8-bit
- 16-bit
- GGUF
- mixtral
- moe
language:
- fr
- en
- es
- it
- de
---

# Mixtral-8x22B-Instruct-v0.1-GGUF

The GGUF and quantized models here are based on [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) model

## How to download
You can download only the quants you need instead of cloning the entire repository as follows:

```
huggingface-cli download MaziyarPanahi/Mixtral-8x22B-Instruct-v0.1-GGUF --local-dir . --include '*Q2_K*gguf'
```

## Load sharded model

`llama_load_model_from_file` will detect the number of files and will load additional tensors from the rest of files.

```sh
llama.cpp/main -m Mixtral-8x22B-Instruct-v0.1.Q2_K-00001-of-00005.gguf -p "Building a website can be done in 10 simple steps:\nStep 1:" -n 1024 -e
```


Original README
--- 

# Model Card for Mixtral-8x22B-Instruct-v0.1
The Mixtral-8x22B-Instruct-v0.1 Large Language Model (LLM) is an instruct fine-tuned version of the [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1).

## Run the model 
```python
from transformers import AutoModelForCausalLM
from mistral_common.protocol.instruct.messages import (
    AssistantMessage,
    UserMessage,
)
from mistral_common.protocol.instruct.tool_calls import (
    Tool,
    Function,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.tokens.instruct.normalize import ChatCompletionRequest

device = "cuda" # the device to load the model onto

tokenizer_v3 = MistralTokenizer.v3()

mistral_query = ChatCompletionRequest(
    tools=[
        Tool(
            function=Function(
                name="get_current_weather",
                description="Get the current weather",
                parameters={
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location", "format"],
                },
            )
        )
    ],
    messages=[
        UserMessage(content="What's the weather like today in Paris"),
    ],
    model="test",
)

encodeds = tokenizer_v3.encode_chat_completion(mistral_query).tokens
model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x22B-Instruct-v0.1")
model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
sp_tokenizer = tokenizer_v3.instruct_tokenizer.tokenizer
decoded = sp_tokenizer.decode(generated_ids[0])
print(decoded)
```

# Instruct tokenizer
The HuggingFace tokenizer included in this release should match our own. To compare: 
`pip install mistral-common`

```py
from mistral_common.protocol.instruct.messages import (
    AssistantMessage,
    UserMessage,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.tokens.instruct.normalize import ChatCompletionRequest

from transformers import AutoTokenizer

tokenizer_v3 = MistralTokenizer.v3()

mistral_query = ChatCompletionRequest(
    messages=[
        UserMessage(content="How many experts ?"),
        AssistantMessage(content="8"),
        UserMessage(content="How big ?"),
        AssistantMessage(content="22B"),
        UserMessage(content="Noice 🎉 !"),
    ],
    model="test",
)
hf_messages = mistral_query.model_dump()['messages']

tokenized_mistral = tokenizer_v3.encode_chat_completion(mistral_query).tokens

tokenizer_hf = AutoTokenizer.from_pretrained('mistralai/Mixtral-8x22B-Instruct-v0.1')
tokenized_hf = tokenizer_hf.apply_chat_template(hf_messages, tokenize=True)

assert tokenized_hf == tokenized_mistral
```

# Function calling and special tokens
This tokenizer includes more special tokens, related to function calling : 
- [TOOL_CALLS]
- [AVAILABLE_TOOLS]
- [/AVAILABLE_TOOLS]
- [TOOL_RESULT]
- [/TOOL_RESULTS]

If you want to use this model with function calling, please be sure to apply it similarly to what is done in our [SentencePieceTokenizerV3](https://github.com/mistralai/mistral-common/blob/main/src/mistral_common/tokens/tokenizers/sentencepiece.py#L299).

# The Mistral AI Team
Albert Jiang, Alexandre Sablayrolles, Alexis Tacnet, Antoine Roux,
Arthur Mensch, Audrey Herblin-Stoop, Baptiste Bout, Baudouin de Monicault,
Blanche Savary, Bam4d, Caroline Feldman, Devendra Singh Chaplot,
Diego de las Casas, Eleonore Arcelin, Emma Bou Hanna, Etienne Metzger,
Gianna Lengyel, Guillaume Bour, Guillaume Lample, Harizo Rajaona,
Jean-Malo Delignon, Jia Li, Justus Murke, Louis Martin, Louis Ternon,
Lucile Saulnier, Lélio Renard Lavaud, Margaret Jennings, Marie Pellat,
Marie Torelli, Marie-Anne Lachaux, Nicolas Schuhl, Patrick von Platen,
Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao,
Thibaut Lavril, Timothée Lacroix, Théophile Gervet, Thomas Wang,
Valera Nemychnikova, William El Sayed, William Marshall

---