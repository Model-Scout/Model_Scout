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
- document-level-translation
- multilingual
- mistral
- supervised-fine-tuning
---

# Tower-7B-d2d

This model is released as part of our paper **Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking**. The code and paper-specific inference scripts are available in the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

Tower-7B-d2d is a full-parameter fine-tuned version of [Unbabel/TowerInstruct-Mistral-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2) for multilingual document-level machine translation. It was fine-tuned on [sardinelab/DocBlocks](https://huggingface.co/datasets/sardinelab/DocBlocks).

This model is trained directly on the document-to-document (d2d) translation task.

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

The example below demonstrates general model usage. For the exact inference scripts, prompting setup, and evaluation procedure used in the paper, please refer to the [Doc2FRC GitHub repository](https://github.com/ynklab/Doc2FRC).

### Recommended prompt format

The model was fine-tuned with the following raw ChatML-style translation prompt:

```text
<|im_start|>user
Translate the following source text from {SOURCE_LANGUAGE} into {TARGET_LANGUAGE}.
{SOURCE_LANGUAGE}: {SOURCE_TEXT}.
{TARGET_LANGUAGE}: <|im_end|>
<|im_start|>assistant
```

Use full English language names such as `English`, `Chinese`, `German`, or `Russian`.

### Transformers example

Install a PyTorch build appropriate for your hardware, together with Transformers and Accelerate. PyTorch 2.6 or later is recommended for loading the current PyTorch `.bin` checkpoint files.

```bash
pip install "transformers>=4.56.2" accelerate
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "ynklab/Tower-7B-d2d"

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

# The Tower tokenizer adds the beginning-of-sequence token used during training.
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {name: tensor.to(model.device) for name, tensor in inputs.items()}

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=16384,
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

For best results, keep the combined prompt and generated translation within 32,768 tokens.

## Training

- Base model: TowerInstruct-Mistral-7B-v0.2
- Training method: full-parameter supervised fine-tuning
- Training data: DocBlocks document-level parallel data
- Epochs: 2
- Learning rate: 7e-6
- Learning-rate scheduler: cosine
- Warmup steps: 125
- Maximum sequence length: 32,768 tokens
- Training precision: bfloat16
- Optimizer: AdamW
- Weight decay: 0.01

## License

This model preserves the CC BY-NC-SA 4.0 License distributed with its base model, [TowerInstruct-Mistral-7B-v0.2](https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2). See the [LICENSE](https://huggingface.co/ynklab/Tower-7B-d2d/blob/main/LICENSE) file and the upstream model card for the applicable terms.

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