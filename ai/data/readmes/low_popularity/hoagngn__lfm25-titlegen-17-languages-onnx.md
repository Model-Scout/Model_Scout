---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-230M
pipeline_tag: text-generation
language: [en, vi, zh, ja, ko, th, fr, de, es, pt, ru, id, tl, ms, my, lo, ta]
tags: [onnx, lfm2.5, title-generation, multilingual]
---

# LFM2.5 TitleGen — ONNX

**Complete 230M conversation-title model**, fine-tuned from
[LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M), merged and
exported to ONNX q8. No separate base model or adapter download is required.
Download both `onnx/model_q8.onnx` and `onnx/model_q8.onnx_data` (about 490 MB together).

17 languages; two modes: **descriptive** names the main concern, **discreet**
uses a general title without exposing sensitive details.
Checkpoint: `balance_lora32_20261007/final`; LoRA r32, Qwen teacher distillation
and language balancing. Weights were modified through fine-tuning, merging
and ONNX conversion; original model/tokenizer attribution: Liquid AI.

Local Benchmark167 (en/id/th/vi/zh), ONNX q8 greedy: **98.2% constraint pass**,
**29.25 chrF++**, **100% automated red-team pass** on 96 cases.
These are small, automated research evaluations, not safety guarantees.
Quality varies by language; some neutral labels still need native review.
Not for medical advice. No chat data is included.

## Run

Requires `huggingface_hub`, `transformers>=5`, and an **LFM2-compatible
onnxruntime-genai build** (tested locally with version 0.17.1).
Not an Ollama/GGUF model.

```python
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer
import onnxruntime_genai as og

folder = snapshot_download("hoagngn/lfm25-titlegen-17-languages-onnx")
tokenizer = AutoTokenizer.from_pretrained(folder)
model = og.Model(folder)
message = "Tôi đau đầu ba ngày nay và muốn biết cần theo dõi dấu hiệu nào."
user = (
    "Generate a conversation title in Vietnamese for the following message.\n"
    "Mode: descriptive. Explicitly name the main symptom or concern stated in the message. "
    "Do not invent a diagnosis, treatment, or facts. Output only one short title.\n\n"
    + message.strip()[:1600]
)
prompt = tokenizer.apply_chat_template(
    [{"role": "system", "content": "You generate conversation titles."},
     {"role": "user", "content": user}],
    tokenize=False, add_generation_prompt=True,
)
ids = tokenizer.encode(prompt, add_special_tokens=False)
params = og.GeneratorParams(model)
params.set_search_options(do_sample=False, num_beams=1, max_length=len(ids) + 160)
generator = og.Generator(model, params)
generator.append_tokens(ids)
while not generator.is_done():
    generator.generate_next_token()
title = og.Tokenizer(model).decode(generator.get_sequence(0)[len(ids):])
print(title.strip())
```

For another language, replace `Vietnamese` with its English name.
For discreet mode, replace the mode instruction with:
`Mode: discreet. Use a neutral, general conversation title. Do not reveal symptoms, diagnoses, sensitive topics, medicines, or personal details. Output only one short title.`
