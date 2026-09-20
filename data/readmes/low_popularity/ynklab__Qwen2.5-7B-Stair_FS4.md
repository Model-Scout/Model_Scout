---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-7B-Instruct
base_model_relation: finetune
datasets:
- sardinelab/DocBlocks
language:
- en
- de
- es
- fr
- it
- ko
- nl
- pt
- ru
- zh
tags:
- translation
- chunk-level-translation
- document-level-translation
- multilingual
- qwen2.5
- fixed-range-chunking
- supervised-fine-tuning
---

# Qwen2.5-7B-Stair_FS4

This model is released as part of our paper **Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking**. The code and paper-specific inference scripts are available in the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

Qwen2.5-7B-Stair_FS4 is a full-parameter fine-tuned version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) for multilingual chunk-level machine translation. It is the `Stair_FS4` variant. Documents derived from [sardinelab/DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks) were first segmented using fixed-range chunking with a 256–512-token range. The segments in each document were then merged into four chunks for training. The four chunks follow a stair-step context scheme: the first chunk uses no preceding context, the second uses the first chunk, the third uses the first two chunks, and the fourth uses the first three chunks. Multiple context chunks are supplied separately and in chronological order through the `Context1`, `Context2`, and `Context3` sections.

## Supported translation directions

The model supports translation between English and the following languages in both directions:

- German
- Spanish
- French
- Italian
- Korean
- Dutch
- Portuguese
- Russian
- Chinese

## General usage

The example below demonstrates general model usage for translating a current source chunk with zero, one, two, or three preceding source-language context chunks. For the exact document chunking, inference scripts, prompting setup, and evaluation procedure used in the paper, please refer to the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

### Recommended prompt formats

The model was fine-tuned with four raw ChatML-style translation prompt formats, one for each position in a four-chunk training document.

#### 0c1t: no context

```text
<|im_start|>user
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

#### 1c1t: one context chunk

```text
<|im_start|>user
Context
{SOURCE_LANGUAGE}: {CONTEXT_TEXT}
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

#### 2c1t: two context chunks

```text
<|im_start|>user
Context1
{SOURCE_LANGUAGE}: {CONTEXT_TEXT_1}
Context2
{SOURCE_LANGUAGE}: {CONTEXT_TEXT_2}
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

#### 3c1t: three context chunks

```text
<|im_start|>user
Context1
{SOURCE_LANGUAGE}: {CONTEXT_TEXT_1}
Context2
{SOURCE_LANGUAGE}: {CONTEXT_TEXT_2}
Context3
{SOURCE_LANGUAGE}: {CONTEXT_TEXT_3}
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

Use full English language names such as `English`, `Chinese`, `German`, or `Russian`. Apply fixed-range segmentation with a 256–512-token range and merge each document into four chunks. Use 0c1t for the first chunk, 1c1t for the second, 2c1t for the third, and 3c1t for the fourth. Supply multiple context chunks separately and in chronological order.

### Transformers example

Install a PyTorch build appropriate for your hardware, together with Transformers and Accelerate. PyTorch 2.6 or later is recommended for loading the current PyTorch `.bin` checkpoint files.

```bash
pip install "transformers>=4.56.2" accelerate
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "ynklab/Qwen2.5-7B-Stair_FS4"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()


def build_prompt(
    source_language,
    target_language,
    source_text,
    context_texts=None,
):
    context_texts = context_texts or []
    if len(context_texts) > 3:
        raise ValueError("Stair_FS4 accepts at most three context chunks.")

    lines = ["<|im_start|>user"]

    if len(context_texts) == 1:
        lines.extend([
            "Context",
            f"{source_language}: {context_texts[0]}",
        ])
    elif len(context_texts) >= 2:
        for index, context_text in enumerate(context_texts, start=1):
            lines.extend([
                f"Context{index}",
                f"{source_language}: {context_text}",
            ])

    lines.extend([
        f"Translate the following source text from {source_language} "
        f"into {target_language}.",
        f"{source_language}: {source_text}.",
        f"{target_language}: <|im_end|>",
        "<|im_start|>assistant",
        "",
    ])
    return "
".join(lines)


source_language = "English"
target_language = "Chinese"
source_text = "The weather is nice today"

# Use up to the three immediately preceding source chunks,
# ordered from the earliest to the most recent.
context_texts = [
    "We planned a picnic for this afternoon.",
    "We packed some food and drinks.",
    "We checked the forecast before leaving.",
]
prompt = build_prompt(
    source_language,
    target_language,
    source_text,
    context_texts,
)

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    add_special_tokens=False,
)
inputs = {name: tensor.to(model.device) for name, tensor in inputs.items()}

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=8192,
        do_sample=False,
        repetition_penalty=1.05,
    )

generated_tokens = outputs[0, inputs["input_ids"].shape[1]:]
translation = tokenizer.decode(
    generated_tokens,
    skip_special_tokens=True,
).strip()

print(translation)
```

For paper-level document translation, split the document into fixed-range chunks and reconstruct the translated chunks using the procedures provided in the [Doc2FRC repository](https://github.com/ynklab/Doc2FRC).

## Training

- Base model: Qwen2.5-7B-Instruct
- Training method: full-parameter supervised fine-tuning
- Training variant: `Stair_FS4` (four-chunk staircase: 0c1t, 1c1t, 2c1t, and 3c1t)
- Document construction: fixed-range segmentation followed by merging each document into four chunks
- Fixed-range segmentation: 256–512 tokens
- Chunks per training document: 4
- Epochs: 2
- Learning rate: 7e-6
- Learning-rate scheduler: cosine
- Warmup steps: 125
- Maximum sequence length: 32,768 tokens
- Training precision: bfloat16
- Optimizer: AdamW
- Weight decay: 0.01

## License

This model is released under the **Apache License 2.0**. See the [LICENSE](https://huggingface.co/ynklab/Qwen2.5-7B-Stair_FS4/blob/main/LICENSE) file for details.

DocBlocks contains material derived from multiple sources. Users should also consult the [DocBlocks dataset](https://huggingface.co/datasets/sardinelab/DocBlocks) and the original data sources for their applicable licensing conditions.

## Acknowledgements

This model is based on [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) and was fine-tuned using [DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks). Please cite our paper when using this model in academic work.

## Citation

```bibtex
@misc{wang2026doc2frclengthconsistentdocumentlevelmachine,
      title={Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking}, 
      author={Xiaotian Wang and Youyuan Lin and Zhan Shen and Hitomi Yanaka},
      year={2026},
      eprint={2609.12674},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2609.12674}, 
}
```