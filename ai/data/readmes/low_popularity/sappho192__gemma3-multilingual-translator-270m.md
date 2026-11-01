---
license: apache-2.0
language:
- ko
- en
- ja
base_model:
- google/gemma-3-270m
base_model_relation: finetune
pipeline_tag: translation
tags:
- gemma3
- multilingual
- translation
- korean
- japanese
- english
- lora
- ema
- onnx
---

# Gemma3 Multilingual Translator (270M)

A multilingual translation model based on Gemma3-270m, fine-tuned with LoRA and Bias-corrected EMA on 7.4M translation pairs.

## Features

- **6-way translation**: Korean, English, Japanese (all directions)
- **High quality**: 60% loss reduction (4.03 → 1.59) with EMA smoothing
- **Easy to use**: Simple prompt format with language tags
- **ONNX included**: Pre-converted ONNX models for PyTorch-free deployment
- **Multiple precisions**: fp32 and q4 quantized ONNX models included

## Quick Start

### Using Transformers (PyTorch)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "sappho192/gemma3-multilingual-translator-270m",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("sappho192/gemma3-multilingual-translator-270m")

# Translate Korean to English
prompt = "<src:ko><tgt:en>\n안녕하세요, 만나서 반갑습니다.\n###\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        do_sample=False,
        pad_token_id=tokenizer.pad_token_id
    )

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
translation = result.split("###")[-1].strip()
print(translation)  # "Hello, nice to meet you."
```

### Using ONNX (No PyTorch Required)

```python
from torch_free.inference import TranslatorInferencer

# Load ONNX model (q4 recommended for speed/size)
translator = TranslatorInferencer(
    "sappho192/gemma3-multilingual-translator-270m",
    precision="q4"
)

# Translate
result = translator.translate(
    "안녕하세요, 만나서 반갑습니다.",
    src_lang="ko",
    tgt_lang="en"
)
print(result)  # "Hello, nice to meet you."
```

## Translation Format

```
<src:SOURCE_LANG><tgt:TARGET_LANG>
SOURCE_TEXT
###
```

**Language codes**: `ko` (Korean), `en` (English), `ja` (Japanese)

## Examples

| Direction | Input | Output |
|-----------|-------|--------|
| KO→EN | 안녕하세요, 만나서 반갑습니다. | Hello, nice to meet you. |
| EN→KO | Hello, nice to meet you. | 안녕하세요, 만나서 반갑습니다. |
| JA→KO | こんにちは、お元気ですか？ | 안녕하세요, 건강하세요? |
| KO→JA | 오늘 날씨가 정말 좋네요. | 今日の天気は本当にいいですね。 |

## Model Details

### Training Specifications

| Parameter | Value |
|-----------|-------|
| Base Model | google/gemma-3-270m |
| Training Data | 7.4M translation pairs |
| LoRA Rank | 16 |
| LoRA Alpha | 32 |
| EMA Decay | 0.999 |
| Final Loss | 1.59 |

### Model Architecture

| Parameter | Value |
|-----------|-------|
| Hidden Size | 640 |
| Intermediate Size | 2048 |
| Num Layers | 18 |
| Num Attention Heads | 4 |
| Num KV Heads | 1 |
| Head Dim | 256 |
| Vocab Size | 262,144 |
| Max Position Embeddings | 32,768 |

### Included Files

| File | Description |
|------|-------------|
| `model.safetensors` | Merged model weights (LoRA + base) |
| `onnx/model.onnx` | ONNX model (fp32) |
| `onnx/model_q4.onnx` | ONNX model (int4 quantized) |
| `torch_free/` | PyTorch-free inference code |

### ONNX Model Sizes

| Precision | Model Size | Avg. Latency |
|-----------|------------|--------------|
| fp32 | 1.1 GB | 0.26s |
| q4 | 764 MB | 0.17s |

## Requirements

### For PyTorch Inference
- Python 3.11+
- PyTorch 2.0+
- transformers >= 4.55.0

### For ONNX Inference (No PyTorch)
- Python 3.11+
- numpy >= 1.24.0
- onnxruntime >= 1.16.0
- tokenizers >= 0.15.0

## License

Apache License 2.0

## Citation

If you use this model, please cite:

```bibtex
@misc{gemma3-multilingual-translator,
  author = {Taein Kim},
  title = {Gemma3 Multilingual Translator},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/sappho192/gemma3-multilingual-translator-270m}
}
```