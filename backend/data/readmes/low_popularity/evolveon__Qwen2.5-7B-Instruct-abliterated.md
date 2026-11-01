---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/evolveon/Qwen2.5-7B-Instruct-abliterated/blob/main/LICENSE
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
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
- chat
- abliterated
- uncensored
- unrestricted
---

# evolveon/Qwen2.5-7B-Instruct-abliterated


This is an uncensored version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) created with abliteration (see [this article](https://huggingface.co/blog/mlabonne/abliteration) to know more about it).

Special thanks to [@FailSpy](https://huggingface.co/failspy) for the original code and technique.


## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "evolveon/Qwen2.5-7B-Instruct-abliterated"
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