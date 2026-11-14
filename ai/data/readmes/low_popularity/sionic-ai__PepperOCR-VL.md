---
license: agpl-3.0
base_model: Qwen/Qwen3.5-4B
base_model_relation: finetune
pipeline_tag: image-text-to-text
library_name: transformers
tags:
  - ocr
  - document-parsing
  - document-understanding
  - markdown
  - latex
  - table-recognition
  - multilingual
  - vllm
  - qwen3_5
language:
  - en
  - de
  - es
  - fr
  - id
  - it
  - nl
  - pt
  - vi
  - ar
  - hi
  - ja
  - ko
  - ru
  - th
  - zh
---

# PepperOCR-VL

<div align="center">
  <img src="assets/sionic_ai_logo.webp" alt="Sionic AI" width="40%"/>
  <p>
    <a href="https://sionic.ai"><img src="https://img.shields.io/badge/Website-sionic.ai-0f766e?style=for-the-badge" alt="Website"/></a>
    <a href="https://huggingface.co/sionic-ai"><img src="https://img.shields.io/badge/Hugging_Face-sionic--ai-f59e0b?style=for-the-badge" alt="Hugging Face"/></a>
  </p>
</div>

PepperOCR-VL turns a page image into clean Markdown. Point it at a scanned or
photographed document, an invoice, a paper, a textbook page or a slide, and it
returns the text in reading order with headings, lists, tables and formulas
preserved. It is a 4.5B-parameter vision-language model fine-tuned from
[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) for 17 languages across
Latin and non-Latin scripts. On [MDPBench](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/MDPBench)
it holds the **state-of-the-art Korean (92.6) and Thai (83.3) scores** across
all listed models, including large general-purpose VLMs, as of the
September 2026 leaderboard.

## About Sionic AI

PepperOCR-VL is built by [Sionic AI](https://sionic.ai), a Seoul-based AI
company building document and language models for enterprise use. If you are
building agentic document parsing, large-scale document processing pipelines,
or want to use PepperOCR in a commercial product, we would like to hear from
you: contact us through the website. Commercial licensing, larger deployments
and hosted inference are available.

## What it outputs

One page image in, one Markdown document out:

- **Text and layout**: headings (`#`), paragraphs, bullet and numbered lists,
  in the original language and reading order. No translation, no summarizing,
  no spelling correction.
- **Tables**: HTML `<table>` blocks with `rowspan`/`colspan`, which survive
  merged cells better than Markdown pipe tables.
- **Mathematics**: LaTeX, `$x$` for inline formulas and `$$x$$` for display
  formulas.
- Nothing else: no preamble, no explanation, just the transcription.

## Prompt format

The model is trained to respond to a single user turn that contains the page
image followed by this instruction. Use it verbatim (also in
`prompt.txt`):

```text
You are an advanced hybrid OCR engine capable of processing multilingual text mixed with mathematical notation. Your goal is to transcribe the content with high fidelity.Strict Rules: 1. Multilingual Precision: Transcribe text exactly as it appears in the original language. Do not translate, summarize, or correct original spelling errors. 2. Math Formatting: Identify all mathematical expressions and convert them into LaTeX. 3. Use single dollar signs ($x$) for inline math (formulas within a sentence). 4. Use double dollar signs ($$x$$) for display math (standalone formulas on their own lines). 5. Layout & Structure: Use Markdown to preserve the visual structure (headers, paragraphs, lists). 6. Output Only: Output the transcribed text directly without any conversational filler.
```

Message layout:

```json
{"role": "user", "content": [
  {"type": "image", "image": "<page image>"},
  {"type": "text",  "text": "<the prompt above>"}
]}
```

Keep thinking mode off (`enable_thinking: false`); the model was tuned and
evaluated without it. The decoding settings are in the next section.

## Inference settings

The decoding defaults that produced the reported scores are built into
`generation_config.json` (greedy decoding, `repetition_penalty` 1.05,
`no_repeat_ngram_size` 30, up to 8192 new tokens), so `transformers` and vLLM
apply them automatically. Keep thinking mode off.

The complete configuration behind the benchmark numbers, including the vLLM
serving arguments, image preprocessing, the orientation threshold, the
runaway-output retry policy and the exact software versions, is in
[`inference_config.yaml`](inference_config.yaml). Start from that file if you
want to reproduce the scores or tune the setup.

## Quickstart

### vLLM

```bash
vllm serve sionic-ai/PepperOCR-VL \
  --served-model-name pepperocr-vl \
  --max-model-len 32768 \
  --max-num-seqs 64 \
  --gpu-memory-utilization 0.85 \
  --gdn-prefill-backend triton     # vLLM 0.24; drop if your version does not have it
```

```python
import base64, pathlib
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")
prompt = pathlib.Path("prompt.txt").read_text()
image = base64.b64encode(pathlib.Path("page.jpg").read_bytes()).decode()

response = client.chat.completions.create(
    model="pepperocr-vl",
    messages=[{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image}"}},
        {"type": "text", "text": prompt},
    ]}],
    temperature=0.0,
    top_p=1.0,
    max_tokens=8192,
    seed=42,
    presence_penalty=0.0,
    extra_body={
        "top_k": -1,
        "repetition_penalty": 1.05,
        "no_repeat_ngram_size": 30,
        "chat_template_kwargs": {"enable_thinking": False},
    },
)
print(response.choices[0].message.content)
```

### Transformers

```python
import torch
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor

model_id = "sionic-ai/PepperOCR-VL"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="cuda"
)

prompt = open("prompt.txt").read()
messages = [{"role": "user", "content": [
    {"type": "image", "image": Image.open("page.jpg")},
    {"type": "text", "text": prompt},
]}]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt", enable_thinking=False,
).to(model.device)

out = model.generate(
    **inputs, max_new_tokens=8192, do_sample=False,
    repetition_penalty=1.05, no_repeat_ngram_size=30,
)
print(processor.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Requirements: `transformers >= 5.10` or `vllm >= 0.24`, a GPU with 24 GB or
more for bf16. PDFs must be rasterized to page images first (around 150 to
200 DPI works well).

## Tips

- **Rotated photos.** The model expects upright pages. If your inputs may be
  rotated, run an orientation check first. `orientation/` contains the small
  CPU classifier (PP-LCNet_x1_0_doc_ori, 6.6 MB) and the script we use: rotate
  only when the predicted angle has confidence 0.85 or higher.
- **Runaway output.** On rare pages with dense repeated structure the model can
  keep generating until the token limit. If the output hits `max_tokens`,
  regenerate with a slightly higher temperature (0.1 to 0.8) and keep the
  shorter result.
- **Throughput.** One vLLM server per GPU with `--max-num-seqs 64` and 64
  concurrent requests processes about 1.3 pages per second per GPU on
  80 GB-class hardware.

## Model details

| | |
|---|---|
| Architecture | `Qwen3_5ForConditionalGeneration` |
| Parameters | 4.54 B |
| Weights | bf16 safetensors, 2 shards, 9.08 GB |
| Text decoder | 32 layers, hidden size 2560, vocabulary 248,320, context 262,144 |
| Vision encoder | 24 layers, patch 16, spatial merge 2 |
| Languages | de, en, es, fr, id, it, nl, pt, vi, ar, hi, ja, ko, ru, th, zh (Simplified and Traditional) |
| License | AGPL-3.0 (see `LICENSE`, `NOTICE`) |

## Benchmark

Official [MDPBench](https://github.com/Yuliang-Liu/MultimodalOCR/tree/main/MDPBench)
re-evaluation by the benchmark team (public set 2,720 pages, 17 languages,
digital-born and photographed):

| | Score |
|---|---|
| Public set, overall | 82.3 |
| Digital-born / Photographed | 87.3 / 80.7 |
| Private set, overall | 85.7 |
| Korean / Thai | **92.6 / 83.3** (highest on the leaderboard, September 2026) |

Per-language scores and the evaluation conditions are in
`eval_results/mdpbench.md`.

## Limitations

- Arabic, Japanese and French are the weakest of the supported languages.
- Tables come out as HTML, not Markdown pipe tables.
- One page per request; no multi-page or PDF input.
- Handwriting, very low-resolution scans and non-document photographs were not
  part of training or evaluation targets.

## License

The weights and the files in this repository are released under the GNU Affero
General Public License v3.0 (`LICENSE`). You may use, modify and redistribute
them, including in networked services, provided the complete corresponding
source of your service is made available under the same license. For use under
different terms, including closed commercial deployment, contact Sionic AI.

PepperOCR-VL is a fine-tune of Qwen3.5-4B (Apache-2.0, Alibaba Cloud); the
optional orientation classifier is PP-LCNet_x1_0_doc_ori from PaddleOCR
(Apache-2.0). Their notices are preserved in `NOTICE`.

## Citation

```bibtex
@misc{pepperocr-vl-2026,
  title        = {PepperOCR-VL: Multilingual End-to-End Document Parsing},
  author       = {Sionic AI},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/sionic-ai/PepperOCR-VL}}
}
```
