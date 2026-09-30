---
license: mit
base_model: baidu/Unlimited-OCR
library_name: transformers
pipeline_tag: image-text-to-text
language:
- ko
tags:
- ocr
- document-parsing
- vision-language
- moe
- korean
- custom_code
---

# schift-ocr-1-beta

Beta open-weights release. A better version is served only through the Schift API.

schift-ocr-1-beta is a Korean document OCR model fine-tuned from [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR). It reads a page image and writes the page as text in reading order, with HTML tables and a layout box for every block.

## Architecture

| Part | Details |
|---|---|
| Vision encoder | Same as the base model: a SAM ViT-B branch (12 layers) and a CLIP ViT-L/14 branch (24 layers). A linear projector maps them into the decoder. |
| Decoder | DeepSeek-V2-style mixture-of-experts (MoE) decoder: 12 layers, hidden size 1280, 10 attention heads. The first layer is dense. |
| Experts | 72 routed experts per MoE layer: the base model's 64 plus 8 added experts. Each token uses the top 6, plus 2 shared experts. |
| Attention window | While writing, each token sees the whole image and prompt, plus the last 128 generated tokens. Memory does not grow with output length. |
| Size | About 3.6B parameters, BF16. Vocabulary 129,280 tokens. |

Fine-tuning on Korean documents focused on the expert feed-forward layers that table content is routed to. The router stays as in the base model.

## Results

We report the character error rate (CER). It is the edit distance divided by the reference length, capped at 1.0 per page, averaged over pages. Lower is better. All models were run at temperature 0 on the same page images.

- **Printed forms**: 60 scanned Korean bank and finance forms.
- **Slides**: 100 Korean lecture slides.
- **General**: 100 pages of Korean reports and publications.

| Model | Printed forms | Slides | General |
|---|---|---|---|
| **schift-ocr-1-beta** | **0.067** | 0.217 | 0.191 |
| baidu/Unlimited-OCR (base) | 0.135 | 0.228 | 0.219 |
| MinerU2.5-Pro-2605-1.2B | 0.091 | 0.222 | 0.164 |
| PaddleOCR-VL-1.6 | 0.155 | 0.258 | 0.161 |
| Gemini 3.1 flash-lite | 0.152 | 0.391 | 0.178 |
| Meta Muse Spark 1.3 | 0.159 | 0.410 | 0.132 |

Compared with the base model, errors drop by 50% on printed forms, 5% on slides and 13% on general documents.

The Slides and General scores depend on how Markdown markup in each model's output is normalized, and several slide references are incomplete, so we do not claim a lead on those two sets.

## Usage

### vLLM

Use a vLLM build that includes the Unlimited-OCR model. See the base model card for Docker images. We checked this command with vLLM's `unlimited_ocr.py` from commit `7aaf016a1`.

```bash
vllm serve schift-io/schift-ocr-1-beta --trust-remote-code --max-model-len 32768
```

Send the page image with the text prompt `<image>document parsing.` to the OpenAI-compatible chat endpoint. Use `temperature=0`, `repetition_penalty=1.0` and `max_tokens` up to 16384.

### Transformers

```python
import torch
from transformers import AutoModel, AutoTokenizer

name = "schift-io/schift-ocr-1-beta"
tokenizer = AutoTokenizer.from_pretrained(name, trust_remote_code=True)
model = AutoModel.from_pretrained(
    name, trust_remote_code=True, use_safetensors=True, dtype=torch.bfloat16
).eval().cuda()

text = model.infer(
    tokenizer,
    prompt="<image>document parsing.",
    image_file="page.png",
    output_path="out",
    base_size=1024, image_size=640, crop_mode=True,
    max_length=16384,
    eval_mode=True,  # return the raw output
)
print(text)
```

## Output format

Each block starts with its type and a box in 0–1000 page coordinates, then the content:

```
<|det|>title [132, 68, 310, 86]<|/det|>3. 조회에 관한 사항
<|det|>table [80, 94, 938, 382]<|/det|><table><tr><td>조회 대상 기관</td>...</tr></table>
```

## Limitations (beta)

- Very long pages can end in repeated text.
- Large tables with many merged cells can come out with rows that have the wrong number of cells.

## License

MIT, inherited from [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR). The base model's `LICENSE` is included.
