---
inference: false
library_name: transformers
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
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
extra_gated_prompt: "By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll receive email updates about C4AI and Cohere research, events, products and services. You can unsubscribe at any time." 
extra_gated_fields:
 Name: text
 Affiliation: text
 Country: country
 I agree to use this model for non-commercial use ONLY: checkbox
---

# **Model Card for C4AI Command R7B**

## **Model Summary**

C4AI Command R7B is an open weights research release of a 7B billion parameter model with advanced capabilities optimized for a variety of use cases including reasoning, summarization, question answering, and code. The model is trained to perform sophisticated tasks including Retrieval Augmented Generation (RAG) and tool use. The model also has powerful agentic capabilities with the ability to use and combine multiple tools over multiple steps to accomplish more difficult tasks. It obtains top performance on enterprise relevant code use cases. C4AI Command R7B is a multilingual model trained on 23 languages. 

Developed by: [Cohere](https://cohere.com/) and [Cohere For AI](https://cohere.for.ai/)

* Point of Contact: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)  
* License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)  
* Model: c4ai-command-r7b-12-2024  
* Model Size: 7 billion parameters  
* Context length: 128K


**Try C4AI Command R7B**

You can try out C4AI Command R7B before downloading the weights in our hosted [Hugging Face Space](https://cohereforai-c4ai-command.hf.space/models/command-r7b-12-2024).


**Usage**

Please install transformers from the source repository that includes the necessary changes for this model.

```py
# pip install 'git+https://github.com/huggingface/transformers.git'
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/c4ai-command-r7b-12-2024"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the c4ai-command-r7b-12-2024 chat template
messages = [{"role": "user", "content": "Hello, how are you?"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
)

gen_text = tokenizer.decode(gen_tokens[0], skip_special_tokens=True)
print(gen_text)
```

## **Model Details**

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: This is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety. The model features three layers with **sliding window attention** (window size 4096\) and **ROPE** for efficient local context modeling and relative positional encoding. A fourth layer uses **global attention** without positional embeddings, enabling unrestricted token interactions across the entire sequence.

**Languages covered**: The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.

Context length: Command R7B supports a context length of 128K.

### A well-rounded model 

Command R7B excels on standardized and externally verifiable benchmarks such as the [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/). Compared to other similarly sized open-weights models, Command R7B ranks first with strong performance across all tasks.

|  | Command R7B | Gemma 2 IT 9B | Ministral 8B | Llama 3.1 8B |
| :---- | :---- | :---- | :---- | :---- |
| Average | **31.4** | 28.9 | 22 | 28.2 |
| IFEval | 77.9 | 74.4 | 58.96 | **78.6** |
| BBH | 36.1 | **42.1** | 25.82 | 29.9 |
| MATH hard | **26.4** | 0.2 | 6.5 | 19.3 |
| GPQA | 7.7 | **14.8** | 4.5 | 2.4 |
| MUSR | **11.6** | 9.74 | 10.7 | 8.41 |
| MMLU-Pro | 28.5 | **32** | 25.5 | 30.7 |

*HuggingFace Leaderboard evaluation results. Competitor numbers are taken from the official leaderboard. Command R7B results are calculated by us using the official HuggingFace prompts and evaluation code.*


### **Chat Capabilities:**

Command R7B can be configured as both a conversational model and an instruct model. The [conversational mode](https://docs.cohere.com/docs/command-r7b-hf) conditions the model on interactive behaviour, meaning it is expected to reply in a conversational fashion, provides introductory statements and follow-up questions, and uses Markdown as well as LaTeX where appropriate. It is optimized for interactive experiences, such as chatbots, where the model engages in dialogue.

The [instruct mode](https://docs.cohere.com/docs/command-r7b-hf), in contrast, conditions the model to provide concise yet comprehensive responses, and does not use Markdown / LaTeX by default. It is designed for non-interactive, task-focused use cases like extracting information, summarizing text, translation, and categorization.

**Note:** by default, Command R7B is delivered without a system preamble. We recommend to add the conversational or instruct preambles as [described in our docs](https://docs.cohere.com/docs/command-r7b-hf).


### **RAG Capabilities:**

Command R7B has been trained specifically for tasks like the final step of Retrieval Augmented Generation (RAG).

RAG with Command R7B is supported through [chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-retrieval-augmented-generation) in Transformers. The model takes a conversation as input (with an optional user-supplied system preamble), along with a list of document snippets.


<details>
<summary><b>RAG Example [CLICK TO EXPAND]</b></summary>
  
```py
# Define conversation input
conversation = [{"role": "user", "content": "What has Man always dreamed of?"}]

# Define documents for retrieval-based generation
documents = [
  {"heading": "The Moon: Our Age-Old Foe", "body": "Man has always dreamed of destroying the moon. In this essay, I shall..."},
  {"heading": "Love is all you need", "body": "Man's dream has always been to find love. This profound lesson..."}
]

# Get the RAG prompt
input_prompt = tokenizer.apply_chat_template(conversation=conversation, documents=documents, tokenize=False, add_generation_prompt=True, return_tensors="pt")
# Tokenize the prompt
input_ids = tokenizer.encode_plus(input_prompt, return_tensors="pt")
```

You can then generate text from this input as normal.

Document snippets should be short chunks, rather than long documents, typically around 100-400 words per chunk, formatted as key-value pairs. The keys should be short descriptive strings, the values can be text or semi-structured.

You may find that simply including relevant documents directly in a user message works just as well, or better than using the documents parameter to render the special RAG template. The RAG template is generally a strong default. We encourage users to play with both, and to evaluate which mode works best for their specific use case.
</details>

Note that this was a very brief introduction to RAG \- for more information, see the Command R7B [prompt format docs](https://docs.cohere.com/docs/command-r7b-hf) and the Transformers [RAG documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-retrieval-augmented-generation).

### **Tool Use Capabilities:**
Command R7B has been specifically trained with conversational tool use capabilities. This allows the model to interact with external tools like APIs, databases, or search engines.
Instructions on how to leverage these capabilities in Hugging Face are coming soon.
<!--
Command R7B has been specifically trained with conversational tool use capabilities. This allows the model to interact with external tools like APIs, databases, or search engines.

Tool use with Command R7B is supported through [chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-tool-use--function-calling) in Transformers. We recommend providing tool descriptions using JSON schema.

<details>
<summary><b>Tool Use Example [CLICK TO EXPAND]</b></summary>

```py
tools = [
    {
    "type": "function",
    "function": {
        "name": "query_daily_sales_report",
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
        "parameters": {
            "type": "object",
            "properties": {
                "day": {
                    "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                    "type": "string",
                    }
                },
                "required": ["day"]
            },
        }
    }
]

# Define conversation input
conversation = [{"role": "user", "content": "Can you provide a sales summary for 29th September 2023?"}]

# Get the Tool Use prompt
input_prompt = tokenizer.apply_chat_template(conversation=conversation, tools=tools, tokenize=False, add_generation_prompt=True, return_tensors="pt")

# Tokenize the prompt
input_ids = tokenizer.encode_plus(input_prompt, return_tensors="pt")
```

You can then generate text from this input as normal.

If the model generates a plan and tool calls, you should add them to the chat history like so:

```py
tool_call = {"name": "query_daily_sales_report", "arguments": {"day": "2023-09-29"}}
tool_plan = "I will use the query_daily_sales_report tool to find the sales summary for 29th September 2023. I will then use the query_product_catalog tool to find the details about the products in the 'Electronics' category."
conversation.append({"role": "assistant", "tool_calls": [{ "id": "0", "type": "function", "function": tool_call},], "tool_plan": tool_plan})
```

and then call the tool and append the result, with the tool role, like so:

```py
api_response_for_query_daily_sales_report = SOME JSON RESPONSE
# Append tool results from tool call 0
conversation.append({"role": "tool", "tool_call_id": "0", "content": json.dumps(api_response_for_query_daily_sales_report)})
```

After that, you can generate() again to let the model use the tool result in the chat.
</details>

Note that this was a very brief introduction to tool calling \- for more information, see the Command R7B [prompt format docs](https://docs.cohere.com/docs/command-r7b-hf) and the Transformers [tool use documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling).
-->

### **Code Capabilities:**

Command R7B has meaningfully improved on code capabilities.  In addition to academic code benchmarks, we have evaluated it on enterprise-relevant scenarios, including SQL and code translation, where it outperforms other models of similar size. Try these out by requesting code snippets, code explanations, or code rewrites. For better performance, we also recommend using a low temperature (and even greedy decoding) for code-generation related instructions.

## **Model Card Contact**

For errors or additional questions about details in this model card, contact info@for.ai.

## **Terms of Use:**

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 7 billion parameter model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).

## **Try Chat:**

You can try Command R7B chat in the playground [here](https://dashboard.cohere.com/playground/chat). You can also use it in our dedicated Hugging Face Space [here](https://cohereforai-c4ai-command.hf.space/models/command-r7b-12-2024).
