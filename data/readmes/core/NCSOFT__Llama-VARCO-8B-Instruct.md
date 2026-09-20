---
language:
- en
- ko
license: llama3.1
tags:
- llama-3.1
- ncsoft
- varco
base_model:
- meta-llama/Meta-Llama-3.1-8B
library_name: transformers
---

## Llama-VARCO-8B-Instruct

### About the Model

**Llama-VARCO-8B-Instruct** is a *generative model* built with Llama, specifically designed to excel in Korean through additional training. The model uses continual pre-training with both Korean and English datasets to enhance its understanding and generation capabilites in Korean, while also maintaining its proficiency in English. It performs supervised fine-tuning (SFT) and direct preference optimization (DPO) in Korean to align with human preferences.

- **Developed by:** NC Research, Language Model Team
- **Languages (NLP):** Korean, English
- **License:** LLAMA 3.1 COMMUNITY LICENSE AGREEMENT
- **Base model:** [meta-llama/Meta-Llama-3.1-8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B)

## Uses

### Direct Use

We recommend to use transformers v4.43.0 or later, as advised for Llama-3.1.

```python
  from transformers import AutoTokenizer, AutoModelForCausalLM
  import torch

  model = AutoModelForCausalLM.from_pretrained(
      "NCSOFT/Llama-VARCO-8B-Instruct",
      torch_dtype=torch.bfloat16,
      device_map="auto"
  )
  tokenizer = AutoTokenizer.from_pretrained("NCSOFT/Llama-VARCO-8B-Instruct")

  messages = [
      {"role": "system", "content": "You are a helpful assistant Varco. Respond accurately and diligently according to the user's instructions."},
      {"role": "user", "content": "안녕하세요."}
  ]

  inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)

  eos_token_id = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
  ]
  
  outputs = model.generate(
      inputs,
      eos_token_id=eos_token_id,
      max_length=8192
  )

  print(tokenizer.decode(outputs[0]))
```

## Evaluation

### LogicKor

We used the [LogicKor](https://github.com/instructkr/LogicKor) code to measure performance. For the judge model, we used the officially recommended gpt-4-1106-preview. The score includes only the 0-shot evaluation provided in the default.

| Model        |  Math  |  Reasoning  |  Writing  |  Coding  |  Understanding  |  Grammer  |  Single turn  |  Multi turn  |  Overall  |
|--------------|--------|-------------|-----------|----------|-----------------|-----------|---------------|--------------|-----------|
| [Llama-VARCO-8B-Instruct](https://huggingface.co/NCSOFT/Llama-VARCO-8B-Instruct)| 6.71 / 8.57 | 8.86 / 8.29 | 9.86 / 9.71 | 8.86 / 9.29 | 9.29 / 10.0 | 8.57 / 7.86 | 8.69 | 8.95 | 8.82 |
| [EXAONE-3.0-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct)| 6.86 / 7.71 | 8.57 / 6.71 | 10.0 / 9.29 | 9.43 / 10.0 | 10.0 / 10.0 | 9.57 / 5.14 | 9.07 | 8.14 | 8.61 |
| [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)| 4.29 / 4.86  | 6.43 / 6.57 | 6.71 / 5.14 | 6.57 / 6.00 | 4.29 / 4.14 | 6.00 / 4.00 | 5.71 | 5.12 | 5.42 |
| [Gemma-2-9B-Instruct](https://huggingface.co/google/gemma-2-9b-it)| 6.14 / 5.86 | 9.29 / 9.0 | 9.29 / 8.57 | 9.29 / 9.14 | 8.43 / 8.43 | 7.86 / 4.43 | 8.38 | 7.57 | 7.98
| [Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct)| 5.57 / 4.86 | 7.71 / 6.43 | 7.43 / 7.00 | 7.43 / 8.00 | 7.86 / 8.71 | 6.29 / 3.29 | 7.05 | 6.38 | 6.71 |