---
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
library_name: transformers
tags:
- mlx
---

# mlx-community/c4ai-command-r-v01-4bit
This model was converted to MLX format from [`CohereForAI/c4ai-command-r-v01`]().
Refer to the [original model card](https://huggingface.co/CohereForAI/c4ai-command-r-v01) for more details on the model.
## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-r-v01-4bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```


## Tool use 🛠️

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-r-v01-4bit")

# Format message with the command-r tool use template
conversation = [
    {"role": "user", "content": "Whats the biggest penguin in the world?"}
]
# Define tools available for the model to use:
tools = [
  {
    "name": "internet_search",
    "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
    "parameter_definitions": {
      "query": {
        "description": "Query to search the internet with",
        "type": 'str',
        "required": True
      }
    }
  },
  {
    'name': "directly_answer",
    "description": "Calls a standard (un-augmented) AI chatbot to generate a response given the conversation history",
    'parameter_definitions': {}
  }
]

formatted_input = tokenizer.apply_tool_use_template(conversation, tools=tools, tokenize=False, add_generation_prompt=True)
response = generate(model, tokenizer, prompt=formatted_input, verbose=True)
```

<details>
<summary><b> Prompt [CLICK TO EXPAND]</b></summary>

````
<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># Safety Preamble
The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral.

# System Preamble
## Basic Rules
You are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what kind of response to generate. When you answer the user's requests, you cite your sources in your answers, according to those instructions.

# User Preamble
## Task and Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.

## Available Tools
Here is a list of tools that you have available to you:

```python
def internet_search(query: str) -> List[Dict]:
    """Returns a list of relevant document snippets for a textual query retrieved from the internet

    Args:
        query (str): Query to search the internet with
    """
    pass
```

```python
def directly_answer() -> List[Dict]:
    """Calls a standard (un-augmented) AI chatbot to generate a response given the conversation history
    """
    pass
```<|START_OF_TURN_TOKEN|><|USER_TOKEN|>Whats the biggest penguin in the world?<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Write 'Action:' followed by a json-formatted list of actions that you want to perform in order to produce a good response to the user's last input. You can use any of the supplied tools any number of times, but you should aim to execute the minimum number of necessary actions for the input. You should use the `directly-answer` tool if calling the other tools is unnecessary. The list of actions you want to call should be formatted as a list of json objects, for example:
```json
[
    {
        "tool_name": title of the tool in the specification,
        "parameters": a dict of parameters to input into the tool as they are defined in the specs, or {} if it takes no parameters
    }
]```<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
````
</details>

<summary><b> Output </b></summary>

````
Action:```json
[
    {
        "tool_name": "internet_search",
        "parameters": {
            "query": "biggest penguin in the world"
        }
    }
]
```
````


## RAG use 📚

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-r-v01-4bit")

# Format message with the command-r tool use template
conversation = [
  {"role": "user", "content": "Whats the biggest penguin in the world?"}
]
# define documents to ground on:
documents = [
  { "title": "Tall penguins", "text": "Emperor penguins are the tallest growing up to 122 cm in height." }, 
  { "title": "Penguin habitats", "text": "Emperor penguins only live in Antarctica."}
]


formatted_input = tokenizer.apply_grounded_generation_template(
  conversation,
  documents=documents,
  citation_mode="accurate", # or "fast"
  tokenize=False,
  add_generation_prompt=True,
)

response = generate(model, tokenizer, prompt=formatted_input, verbose=True)
```

<details>
<summary><b> Prompt [CLICK TO EXPAND]</b></summary>

````
<BOS_TOKEN><BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># Safety Preamble
The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral.

# System Preamble
## Basic Rules
You are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what kind of response to generate. When you answer the user's requests, you cite your sources in your answers, according to those instructions.

# User Preamble
## Task and Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Whats the biggest penguin in the world?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|><results>
Document: 0
title: Tall penguins
text: Emperor penguins are the tallest growing up to 122 cm in height.

Document: 1
title: Penguin habitats
text: Emperor penguins only live in Antarctica.
</results><|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Carefully perform the following instructions, in order, starting each with a new line.
Firstly, Decide which of the retrieved documents are relevant to the user's last input by writing 'Relevant Documents:' followed by comma-separated list of document numbers. If none are relevant, you should instead write 'None'.
Secondly, Decide which of the retrieved documents contain facts that should be cited in a good answer to the user's last input by writing 'Cited Documents:' followed a comma-separated list of document numbers. If you dont want to cite any of them, you should instead write 'None'.
Thirdly, Write 'Answer:' followed by a response to the user's last input in high quality natural english. Use the retrieved documents to help you. Do not insert any citations or grounding markup.
Finally, Write 'Grounded answer:' followed by a response to the user's last input in high quality natural english. Use the symbols <co: doc> and </co: doc> to indicate when a fact comes from a document in the search result, e.g <co: 0>my fact</co: 0> for a fact from document 0.<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
````
</details>

<summary><b> Output </b></summary>

````

Relevant Documents: 0,1
Cited Documents: 0
Answer: The tallest species of penguin in the world is the emperor penguin (Aptenodytes forsteri), which can reach heights of up to 122 cm.
Grounded answer: The tallest species of penguin in the world is the <co: 0>emperor penguin</co: 0> <co: 0>(Aptenodytes forsteri)</co: 0>, which can reach <co: 0>heights of up to 122 cm.</co: 0>
````
