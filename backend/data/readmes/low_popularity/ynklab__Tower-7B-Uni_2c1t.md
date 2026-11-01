---
license: cc-by-nc-sa-4.0
library_name: transformers
pipeline_tag: text-generation
base_model: Unbabel/TowerInstruct-Mistral-7B-v0.2
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
- mistral
- fixed-range-chunking
- supervised-fine-tuning
---

# Tower-7B-Uni_2c1t

This model is released as part of our paper **Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking**. The code and paper-specific inference scripts are available in the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

Tower-7B-Uni_2c1t is a full-parameter fine-tuned version of [Unbabel/TowerInstruct-Mistral-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2) for multilingual chunk-level machine translation. It is the `Uni_2c1t` variant, jointly trained on three prompt forms for translating a current source chunk: no context (`0c1t`), one preceding source-language context chunk (`1c1t`), or two preceding source-language context chunks (`2c1t`). The data are derived from [sardinelab/DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks) and segmented using fixed-range chunking with a 256–512-token range. When two contexts are used, they are supplied separately and in chronological order through the `Context1` and `Context2` sections.

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

The example below demonstrates general model usage for translating a current source chunk with zero, one, or two preceding source-language context chunks. For the exact document chunking, inference scripts, prompting setup, and evaluation procedure used in the paper, please refer to the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

### Recommended prompt formats

The model was fine-tuned with the following three raw ChatML-style translation prompt formats.

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

Use full English language names such as `English`, `Chinese`, `German`, or `Russian`. Supply up to the two immediately preceding source chunks as context. When using two chunks, pass them separately in chronological order: the earlier chunk as `Context1` and the more recent chunk as `Context2`.

### Transformers example

Install a PyTorch build appropriate for your hardware, together with Transformers and Accelerate. PyTorch 2.6 or later is recommended for loading the current PyTorch `.bin` checkpoint files.

```bash
pip install "transformers>=4.56.2" accelerate
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "ynklab/Tower-7B-Uni_2c1t"

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
    if len(context_texts) > 2:
        raise ValueError("Uni_2c1t accepts at most two context chunks.")

    lines = ["<|im_start|>user"]

    if len(context_texts) == 1:
        lines.extend([
            "Context",
            f"{source_language}: {context_texts[0]}",
        ])
    elif len(context_texts) == 2:
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
    return "\n".join(lines)


source_language = "English"
target_language = "Chinese"
source_text = "The weather is nice today"

# Context is optional. Use zero, one, or two immediately preceding source
# chunks. With two chunks, order them from the earlier to the more recent.
context_texts = [
    "We planned a picnic for this afternoon.",
    "We checked the forecast before leaving.",
]
prompt = build_prompt(
    source_language,
    target_language,
    source_text,
    context_texts,
)

# The Tower tokenizer adds the beginning-of-sequence token used during training.
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {name: tensor.to(model.device) for name, tensor in inputs.items()}

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
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

- Base model: TowerInstruct-Mistral-7B-v0.2
- Training method: full-parameter supervised fine-tuning
- Training variant: `Uni_2c1t` (joint 0c1t, 1c1t, and 2c1t prompt forms)
- Fixed-range segmentation: 256–512 tokens
- Epochs: 2
- Learning rate: 7e-6
- Learning-rate scheduler: cosine
- Warmup steps: 125
- Maximum sequence length: 32,768 tokens
- Training precision: bfloat16
- Optimizer: AdamW
- Weight decay: 0.01

## License

This model preserves the CC BY-NC-SA 4.0 License distributed with its base model, [TowerInstruct-Mistral-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2). See the [LICENSE](https://huggingface.co/ynklab/Tower-7B-Uni_2c1t/blob/main/LICENSE) file and the upstream model card for the applicable terms.

DocBlocks contains material derived from multiple sources. Users should also consult the [DocBlocks dataset](https://huggingface.co/datasets/sardinelab/DocBlocks) and the original data sources for their applicable licensing conditions.

## Acknowledgements

This model is based on [TowerInstruct-Mistral-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2) and was fine-tuned using [DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks). Please cite our paper when using this model in academic work.

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