---
language:
- ko
- en
license: apache-2.0
tags:
- text-generation
- qwen2.5
- korean
- instruct
- mlx
pipeline_tag: text-generation
---

## Qwen2.5-7B-Instruct-kowiki-qa mlx convert model
- Original model is [beomi/Qwen2.5-7B-Instruct-kowiki-qa](https://huggingface.co/beomi/Qwen2.5-7B-Instruct-kowiki-qa)


## Requirement
- `pip install mlx-lm`

## Usage
- [Generate with CLI](https://github.com/ml-explore/mlx-examples/blob/main/llms/README.md#command-line)
    ```bash
    mlx_lm.generate --model mlx-community/Qwen2.5-7B-Instruct-kowiki-qa --prompt "하늘이 파란 이유가 뭐야?"
    ```

- [In Python](https://github.com/ml-explore/mlx-examples/blob/main/llms/README.md#python-api)
    ```python
    from mlx_lm import load, generate
    
    model, tokenizer = load(
        "mlx-community/Qwen2.5-7B-Instruct-kowiki-qa",
        tokenizer_config={"trust_remote_code": True},
    )

    prompt = "하늘이 파란 이유가 뭐야?"
    
    messages = [
        {"role": "system", "content": "당신은 친철한 챗봇입니다."},
        {"role": "user", "content": prompt},
    ]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    
    text = generate(
        model,
        tokenizer,
        prompt=prompt,
        # verbose=True,
        # max_tokens=8196,
        # temp=0.0,
    )
    ```

- [OpenAI Compitable HTTP Server](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/SERVER.md)
    ```bash
    mlx_lm.server --model mlx-community/Qwen2.5-7B-Instruct-kowiki-qa --host 0.0.0.0
    ```

    ```python
    import openai


    client = openai.OpenAI(
        base_url="http://localhost:8080/v1",
    )

    prompt = "하늘이 파란 이유가 뭐야?"

    messages = [
        {"role": "system", "content": "당신은 친절한 챗봇입니다.",},
        {"role": "user", "content": prompt},
    ]
    res = client.chat.completions.create(
        model='mlx-community/Qwen2.5-7B-Instruct-kowiki-qa',
        messages=messages,
        temperature=0.2,
    )
    
    print(res.choices[0].message.content)
    ```