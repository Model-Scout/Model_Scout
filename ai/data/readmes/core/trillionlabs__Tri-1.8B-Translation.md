---
library_name: transformers
tags:
- translation
- multilingual
- trillionlabs
- preview
license: apache-2.0
language:
- ko
- en
- zh
- ja
---

# Tri-1.8B Translation

We release **Tri-1.8B Translation**, a lightweight multilingual translation model from **Trillion Labs**.  

Tri-1.8B Translate is trained through pretraining and supervised fine-tuning (SFT), and was distilled from our larger Tri-21B model to preserve strong translation quality in a much smaller, deployment-friendly 1.8B parameter model. It supports all translation directions among English, Korean, Japanese, and Chinese.



## ✨ Highlights

* **Compact & efficient:** \~1.8B params, easy to serve on a single GPU.
* **Multilingual:** Fully bidirectional **EN ↔ KO ↔ JA ↔ ZH**.
* **Simple prompts:** Works with a short **task instruction + `<lang>` tag**.
* **Research-ready:** Suitable for domain SFT or lightweight adapters.

---

## 🧾 Prompt format

```
Translate the following {SRC_NAME} text into {TGT_NAME}:
{TEXT} <{lang_tag}>
```

Where `{lang_tag} ∈ { en, ko, ja, zh }`.

---

## 🔧 Usage

### 1) 🤗 Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "trillionlabs/Tri-1.8B-Translation"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

text = "안녕하세요"
messages = [
    {"role": "user", "content": f"Translate the following Korean text into English:\n{text} <en>"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=256,
    do_sample=False,
    pad_token_id=tokenizer.eos_token_id
)

full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
translation = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

print(f"Korean: {text}")
print(f"English: {translation}")
```

---

### 2) Local vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="trillionlabs/Tri-1.8B-Translation")
sp = SamplingParams(temperature=0.3, max_tokens=512)

def translate(text, target="en"):
    prompt = f"Translate into {target}:\n{text} <{target}>"
    out = llm.chat([{"role": "user", "content": prompt}], sampling_params=sp)
    return out[0].outputs[0].text.strip()

print(translate("안녕하세요", "en"))
```

---

### 3) API client (OpenAI-compatible)

```python
import openai

client = openai.OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

def translate(text, target="en"):
    prompt = f"Translate into {target}:\n{text} <{target}>"
    resp = client.chat.completions.create(
        model="trillionlabs/Tri-1.8B-Translation",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=512,
    )
    return resp.choices[0].message.content.strip()

print(translate("안녕하세요", "en"))
```


## 📜 License

Apache-2.0 (for model weights & code). Please verify data licenses for your use.


## 🙏 Acknowledgments

* Thanks to the **ByteDance Seed team** for releasing **Seed-X**; our prompt template and some training design were adapted from their paper.


## 📚 Citation

If you use **Tri-1.8B Translation**, please cite:

```bibtex
@misc{suk2025tri18b,
  title   = {Tri-1.8B Translation: A Lightweight Multilingual Translation Model},
  author  = {Juyoung Suk and Trillion Labs},
  year    = {2025},
  howpublished = {\url{https://huggingface.co/trillionlabs/Tri-1.8B-Translation}}
}
```