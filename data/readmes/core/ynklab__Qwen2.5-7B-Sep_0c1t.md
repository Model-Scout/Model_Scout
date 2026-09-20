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

# Qwen2.5-7B-Sep_0c1t

This model is released as part of our paper **Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking**. The code and paper-specific inference scripts are available in the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

Qwen2.5-7B-Sep_0c1t is a full-parameter fine-tuned version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) for multilingual chunk-level machine translation. It is the `Sep_0c1t` variant: each call translates one source chunk into one target chunk without preceding context chunks. The training examples were derived from [sardinelab/DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks) using fixed-range chunking.

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

The example below demonstrates general model usage for translating a single chunk. For the exact document chunking, inference scripts, prompting setup, and evaluation procedure used in the paper, please refer to the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

### Recommended prompt format

The model was fine-tuned with the following raw ChatML-style translation prompt:

```text
<|im_start|>user
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

Use full English language names such as `English`, `Chinese`, `German`, or `Russian`. The model was trained on source and target chunks in the 256–512 token range.

### Transformers example

Install a PyTorch build appropriate for your hardware, together with Transformers and Accelerate. PyTorch 2.6 or later is recommended for loading the current PyTorch `.bin` checkpoint files.

```bash
pip install "transformers>=4.56.2" accelerate
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "ynklab/Qwen2.5-7B-Sep_0c1t"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()

source_language = "English"
target_language = "Chinese"
source_text = "The weather is nice today"

prompt = (
    "<|im_start|>user\n"
    f"Translate the following source text from {source_language} "
    f"into {target_language}.\n"
    f"{source_language}: {source_text}.\n"
    f"{target_language}: <|im_end|>\n"
    "<|im_start|>assistant\n"
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

- Base model: Qwen2.5-7B-Instruct
- Training method: full-parameter supervised fine-tuning
- Training variant: `Sep_0c1t` (zero preceding context chunks and one target chunk)
- Chunk range: 256–512 tokens
- Epochs: 2
- Learning rate: 7e-6
- Learning-rate scheduler: cosine
- Warmup steps: 125
- Maximum sequence length: 32,768 tokens
- Training precision: bfloat16
- Optimizer: AdamW
- Weight decay: 0.01

## License

This model is released under the **Apache License 2.0**. See the [LICENSE](https://huggingface.co/ynklab/Qwen2.5-7B-Sep_0c1t/blob/main/LICENSE) file for details.

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