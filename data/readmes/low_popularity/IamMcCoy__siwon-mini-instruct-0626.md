---
language:
- ko
- en
library_name: transformers
tags:
- instruction-tuning
- korean
- phi-4
- causal-lm
model_creator: microsoft
base_model: microsoft/Phi-4-mini-instruct
model_name: siwon-mini-instruct-0626
pipeline_tag: text-generation
---

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/665818433a098887a5b95015/IlaWEzz4UrH7d14DkXGgQ.png" width="300" height="300">
</p>

# siwon-mini-instruct-0626

This model is a fine-tuned version of [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct), adapted for Korean instruction-based tasks. The tuning was focused on enhancing Korean performance through supervised fine-tuning with Korean instruction datasets.

---

## 🔧 Token Adjustments

The original model used the same token ID (199999) for multiple special tokens such as BOS, EOS, PAD, and UNK. This caused confusion in instruction-following tasks. We fixed this by remapping the token IDs as follows:

| Token Type | Original ID | Fixed ID | 
|------------|-------------|----------|
| BOS        | 199999      | 199999   | 
| EOS        | 199999      | 200020   |
| PAD        | 199999      | 200029   |
| UNK        | 199999      | 200030   | 

These changes ensure proper differentiation and functioning of special tokens during generation and training.

---

## 🗨️ Chat Template

The chat template was updated accordingly to support multi-turn conversation formatting in the Korean context:

```jinja2
{% for message in messages %}
{% if message['role'] == 'system' and 'tools' in message and message['tools'] is not none %}
{{ '<|' + message['role'] + '|>' + message['content'] + '<|tool|>' + message['tools'] + '<|/tool|>' + '<|end|>' }}
{% else %}
{{ '<|' + message['role'] + '|>' + message['content'] + '<|end|>' }}
{% endif %}
{% endfor %}
{% if add_generation_prompt %}{{ '<|assistant|>' }}{% endif %}
```

## 🧪 Inference with Transformers
Below is an example of how to load and use the model with the adjusted tokenizer, token IDs, and custom prompt template. 

> **Note**: This model uses a custom `chat_template` and updated special token IDs:
> - `<|end|>` → 200020 (EOS)
> - `<|dummy_85|>` → 200029 (PAD)
> - `ï¿½` → 200030 (UNK)
>

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "IamMcCoy/siwon-mini-instruct-0626"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True,
)

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "안녕하세요."},
    ]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=2048,
    # do_sample=True, # Optional
    # top_p=0.95, # Optional
    # temperature=0.6, # Optional
    # repetition_penalty=1.1, # Optional
)

response = tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
print(response)
```

## 📊 Model Performance Comparison
Performance scores across three Korean language benchmarks (KMMLU, ko_best, pawsx_ko).

| Model                          | KMMLU (0-shot) | ko_best (5-shot) | pawsx_ko |
|-------------------------------|----------------|------------------|----------|
| Phi-4-mini-instruct           | 0.3161         | 0.6341           | 0.5300   |
| kanana-1.5-2.1b-instruct-2505 | 0.1577         | 0.7165           | 0.5070   |
| EXAONE-3.5-2.4B-Instruct       | 0.3071         | 0.6496           | 0.5655   |
| siwon-mini-instruct-0626      | 0.3387         | 0.5576           | 0.5485   |


## 📌 Caution
* Commercial use is strictly prohibited.

* This model is intended for research and educational use only.

* Redistribution or use in commercial products or services is not allowed.


## ✍️ Acknowledgments
* Base model: microsoft/Phi-4-mini-instruct
* Special thanks to the open-source community for instruction-tuning resources and Korean language corpora.


## 🙏 Feedback & Contributions
We welcome any feedback to improve the model’s performance, usability, and alignment with Korean instruction tasks.
If you encounter any issues or have suggestions, please feel free to open an issue on the Hugging Face model page.

Your input is greatly appreciated and will help us enhance the model further.
