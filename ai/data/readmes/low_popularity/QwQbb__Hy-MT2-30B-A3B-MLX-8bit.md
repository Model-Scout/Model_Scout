---
license: other
base_model: tencent/Hy-MT2-30B-A3B
base_model_relation: quantized
library_name: mlx
pipeline_tag: translation
tags:
- mlx
- mlx-lm
- apple-silicon
- translation
- multilingual-translation
- hy-v3
- tencent-hy
- quantized
- 8-bit
- moe
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
- yue
language_bcp47:
- zh-Hant
---

# Hy-MT2-30B-A3B-MLX-8bit

This repository contains a community-created **MLX 8-bit conversion** of [tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B), optimized for Apple Silicon Macs through [MLX-LM](https://github.com/ml-explore/mlx-lm).

It exists for Mac users who want to run the 30B-A3B Hy-MT2 translation model locally without repeating the conversion and HYV3 architecture-adapter work.

## Important Notice

This is **not an official Tencent release**. It is a community conversion.

Tencent is not affiliated with, associated with, sponsoring, endorsing, or maintaining this repository, this conversion, or any service that uses it.

The original model is licensed under the **Tencent HY Community License Agreement**. A copy is included as `LICENSE.txt`, and the required redistribution notice is included as `NOTICE`.

The Tencent HY license states that the agreement **does not apply in the European Union** and defines its Territory as worldwide excluding the EU. Do not use, reproduce, modify, distribute, or display Tencent HY Works outside the permitted Territory. You are responsible for reading and complying with the full license and Acceptable Use Policy before using this model.

## What Was Converted

- Base model: [tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)
- Architecture: `hy_v3`
- Model family: Hy-MT2 multilingual translation
- Parameters: 30B total, about 3B active per token
- Source precision: BF16
- Target format: MLX safetensors
- Quantization: MLX affine 8-bit, group size 64
- Reported bits per weight: 8.500
- Output size: about 30 GB
- Conversion date: 2026-05-22

The converted repository includes a custom `hy_v3.py` adapter because `mlx-lm 0.31.3` did not include built-in `hy_v3` model support at conversion time. Loading this repository executes that local adapter file through MLX-LM's `model_file` mechanism. Please inspect the file before running it if you have any concern about custom model code.

## Tested Hardware

Tested on:

- MacBook Pro M5 Max
- 128 GB unified memory
- macOS with Apple Silicon Metal acceleration
- `mlx==0.31.2`
- `mlx-lm==0.31.3`
- Python 3.13

Short smoke test:

```text
Input:
오늘 날씨가 정말 좋네요.

Output:
The weather is really nice today.

Generation speed:
88.095 tokens/sec

Peak memory:
32.015 GB
```

This is a short smoke test, not a full benchmark. Throughput and memory use will vary by Mac model, macOS version, prompt length, output length, batch size, and KV-cache size.

## Installation

Install MLX-LM:

```bash
python3 -m pip install -U mlx-lm
```

For best results, use a recent macOS release and a Mac with enough unified memory. The model files are about 30 GB, and real memory use increases with prompt length and generated output length.

## Quick Start: Python

```python
from mlx_lm import load, stream_generate
from mlx_lm.sample_utils import make_sampler

model_id = "QwQbb/Hy-MT2-30B-A3B-MLX-8bit"

model, tokenizer = load(model_id)

source_text = "오늘 날씨가 정말 좋네요."
prompt = (
    "Translate the following text into English. "
    "Note that you should only output the translated result without any additional explanation:\n\n"
    f"{source_text}"
)

messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_dict=False,
)

sampler = make_sampler(temp=0.7, top_p=1.0, top_k=0)

parts = []
for response in stream_generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=4096,
    sampler=sampler,
):
    print(response.text, end="", flush=True)
    parts.append(response.text)

print("\n\nFinal:", "".join(parts).strip())
```

## Quick Start: MLX-LM Server

Start an OpenAI-compatible local server:

```bash
mlx_lm.server \
  --model QwQbb/Hy-MT2-30B-A3B-MLX-8bit \
  --host 127.0.0.1 \
  --port 8080 \
  --temp 0.7 \
  --top-p 1.0 \
  --max-tokens 4096 \
  --trust-remote-code
```

Call it with `curl`:

```bash
curl -X POST "http://127.0.0.1:8080/v1/chat/completions" \
  -H "Content-Type: application/json" \
  --data '{
    "model": "QwQbb/Hy-MT2-30B-A3B-MLX-8bit",
    "messages": [
      {
        "role": "user",
        "content": "Translate the following text into English. Note that you should only output the translated result without any additional explanation:\n\n오늘 날씨가 정말 좋네요."
      }
    ],
    "temperature": 0.7,
    "top_p": 1.0,
    "max_tokens": 4096,
    "stream": true
  }'
```

## Recommended Generation Settings

Tencent recommends the following parameters for Hy-MT2-30B-A3B:

```json
{
  "temperature": 0.7,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_tokens": 4096
}
```

In MLX-LM, `top_k=0` disables top-k filtering, which corresponds to the intent of Tencent's `top_k=-1` setting.

## Prompt Templates

Use full language names in prompts, for example `English`, `Korean`, `Japanese`, `Traditional Chinese`, or `French`.

### Default Translation

```text
Translate the following text into {target_lang}. Note that you should only output the translated result without any additional explanation:

{source_text}
```

### Terminology Control

```text
Reference the following translations:
{term_1} translates to {translation_1}
{term_2} translates to {translation_2}
{term_3} translates to {translation_3}

Translate the following text into {target_lang}. Note that you must ONLY output the translated result without any additional explanation:

{source_text}
```

### Style Control

```text
Please translate the following text into {target_lang}. Note that the translation style must strictly conform to [{target_style}]:

{source_text}
```

### Structured Data Translation

```text
### Task
Translate the user-facing text within the following {format_type} data into {target_lang}.

### Strict Rules
1. Structure Preservation: You MUST preserve the original {format_type} data structure, nesting, hierarchy, and indentation exactly as they are.
2. Selective Translation: Translate ONLY the visible, user-facing text content/values.
3. Strict Non-Translation: NEVER translate or alter code tags, keys, properties, object names, or variable placeholders. Leave them exactly in their original English/code form.

### Source Data
{source_text}
```

## Supported Languages

Hy-MT2 supports translation among the following languages:

| Language | Code |
|---|---|
| Chinese | zh |
| English | en |
| French | fr |
| Portuguese | pt |
| Spanish | es |
| Japanese | ja |
| Turkish | tr |
| Russian | ru |
| Arabic | ar |
| Korean | ko |
| Thai | th |
| Italian | it |
| German | de |
| Vietnamese | vi |
| Malay | ms |
| Indonesian | id |
| Filipino | tl |
| Hindi | hi |
| Traditional Chinese | zh-Hant |
| Polish | pl |
| Czech | cs |
| Dutch | nl |
| Khmer | km |
| Burmese | my |
| Persian | fa |
| Gujarati | gu |
| Urdu | ur |
| Telugu | te |
| Marathi | mr |
| Hebrew | he |
| Bengali | bn |
| Tamil | ta |
| Ukrainian | uk |
| Tibetan | bo |
| Kazakh | kk |
| Mongolian | mn |
| Uyghur | ug |
| Cantonese | yue |

## Files

- `model-00001-of-00006.safetensors` through `model-00006-of-00006.safetensors`: MLX 8-bit quantized weights
- `model.safetensors.index.json`: weight index
- `config.json`: HyV3 model configuration plus MLX quantization metadata
- `hy_v3.py`: custom MLX-LM model adapter for HYV3
- `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`: tokenizer and chat template files from the base model
- `LICENSE.txt`: Tencent HY Community License Agreement from the base model
- `NOTICE`: required redistribution notice and conversion notice
- `conversion_info.json`: conversion metadata and smoke-test result

## Limitations

- This is an experimental community conversion, not an official Tencent artifact.
- It is intended for MLX-LM on Apple Silicon. It is not a Transformers checkpoint.
- The custom `hy_v3.py` adapter was tested with a short translation smoke test, but it has not been exhaustively validated on every long-context, batching, or edge-case workload.
- The benchmark number above is a short generation test and should not be treated as a universal throughput guarantee.
- Users are responsible for license compliance, applicable law compliance, and Acceptable Use Policy compliance.

## Attribution

Base model:

```text
tencent/Hy-MT2-30B-A3B
https://huggingface.co/tencent/Hy-MT2-30B-A3B
```

Hy-MT2 paper:

```bibtex
@misc{zheng2026hymt2familyfastefficient,
      title={Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild},
      author={Mao Zheng and Zheng Li and Tao Chen and Bo Lv and Mingrui Sun and Mingyang Song and Jinlong Song and Hong Huang and Decheng Wu and Hai Wang and Yifan Song and Yanfeng Chen and Guanwei Zhang},
      year={2026},
      eprint={2605.22064},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.22064},
}
```

## Required Notice

Tencent HY is licensed under the Tencent HY Community License Agreement, Copyright © 2026 Tencent. All Rights Reserved. The trademark rights of "Tencent HY" are owned by Tencent or its affiliate.
