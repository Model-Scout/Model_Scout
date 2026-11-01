---
license: apache-2.0
license_link: https://huggingface.co/huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3/blob/main/LICENSE
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-0.5B-Instruct
tags:
- chat
- abliterated
- uncensored
---

# huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3


This is an uncensored version of [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 

Ablation was performed using a new and faster method, which yields better results.

This ablation version used a more precise dataset.  
The pass rate for the 320 harmful instructions test is **100%**.

## ollama

huihui_ai/qwen2.5-abliterate:0.5b-v3 is **less than 400MB** in size and performs very well.


You can use [huihui_ai/qwen2.5-abliterate:0.5b-v3](https://ollama.com/huihui_ai/qwen2.5-abliterate:0.5b-v3) directly, 
```
ollama run huihui_ai/qwen2.5-abliterate:0.5b-v3
```

## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation context
initial_messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}
]
messages = initial_messages.copy()  # Copy the initial conversation context

# Enter conversation loop
while True:
    # Get user input
    user_input = input("User: ").strip()  # Strip leading and trailing spaces

    # If the user types '/exit', end the conversation
    if user_input.lower() == "/exit":
        print("Exiting chat.")
        break

    # If the user types '/clean', reset the conversation context
    if user_input.lower() == "/clean":
        messages = initial_messages.copy()  # Reset conversation context
        print("Chat history cleared. Starting a new conversation.")
        continue

    # If input is empty, prompt the user and continue
    if not user_input:
        print("Input cannot be empty. Please enter something.")
        continue

    # Add user input to the conversation
    messages.append({"role": "user", "content": user_input})

    # Build the chat template
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # Tokenize input and prepare it for the model
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # Generate a response from the model
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=8192
    )

    # Extract model output, removing special tokens
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # Add the model's response to the conversation
    messages.append({"role": "assistant", "content": response})

    # Print the model's response
    print(f"Qwen: {response}")

```

## Pass Rate Description

The pass rate is defined as the proportion of harmful instructions that did not trigger the test condition (TestPassed=False) out of the total number of instructions processed. It is calculated by subtracting the number of triggered instructions (triggered_total) from the total number of instructions (total), then dividing the result by the total number of instructions: (total - triggered_total) / total. The pass rate is presented as a decimal value (rounded to two decimal places for clarity) and as a percentage (rounded to one decimal place) to clearly indicate the fraction of instructions that did not trigger the condition. 

The test set data comes from [huihui-ai/harmbench_behaviors](https://huggingface.co/datasets/huihui-ai/harmbench_behaviors), the test code, [TestPassed.py](https://huggingface.co/huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3/blob/main/TestPassed.py).

The test result is [100.00%](https://huggingface.co/huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3/blob/main/TestPassed.jsonl).
```
python TestPassed.py
Load Model huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3 ...
Processing harmful instructions: 100%|███████████████████████████████████████████████████████████████████████████████████| 320/320 [01:04<00:00,  4.99it/s]
Passed total: 320/320, Passed ratio: 1.00 (100.00%)
```

Below is the comparison of pass rates.

| Model                                | Passed total | Passed ratio |
|--------------------------------------|--------------|--------------|
| Qwen2.5-0.5B-Instruct                | 201/320      | 62.8%        |
| Qwen2.5-0.5B-Instruct-abliterated    | 310/320      | 96.9%        |
| Qwen2.5-0.5B-Instruct-abliterated-v2 | 317/320      | 99.1%        |
| Qwen2.5-0.5B-Instruct-abliterated-v3 | **320/320**  | **100.00%**  |


### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
