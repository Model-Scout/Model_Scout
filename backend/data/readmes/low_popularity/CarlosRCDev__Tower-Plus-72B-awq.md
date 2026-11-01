---
license: cc-by-nc-sa-4.0
language:
  - de
  - nl
  - is
  - es
  - fr
  - pt
  - uk
  - hi
  - zh
  - ru
  - cs
  - ko
  - ja
  - it
  - en
  - da
  - pl
  - hu
  - sv
  - 'no'
  - ro
  - fi
base_model: Unbabel/Tower-Plus-72B
library_name: transformers
tags:
  - awq
  - quantized
  - multilingual
  - instruct
  - compressed-tensors
pipeline_tag: text-generation
model_creator: Unbabel
---

# Tower-Plus-72B AWQ (W4A16)

This is a W4A16 AWQ quantized version of [Unbabel/Tower-Plus-72B](https://huggingface.co/Unbabel/Tower-Plus-72B).

## Quantization Model Details

| Attribute | Value |
|-----------|-------|
| Original Model | Unbabel/Tower-Plus-72B |
| Quantization | W4A16_ASYM (4-bit weights, 16-bit activations) |
| Calibration Samples | 128 |
| Sequence Length | 2048 |
| Calibration Dataset | neuralmagic/LLM_compression_calibration |

## Quantization Script

### Dependencies
```toml
dependencies = [
    "llmcompressor>=0.10.0.1",
    "protobuf>=7.34.0",
    "sentencepiece>=0.2.1",
    "compressed-tensors>=0.12.2"
]
```
### Code

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor.modifiers.awq import AWQModifier, AWQMapping
from llmcompressor import oneshot

from datasets import load_dataset

# envs
MODEL_PATH = "Tower-Plus-72B"
OUTPUT_PATH = "Tower-Plus-72B-awq"
DATASET_ID = "neuralmagic/LLM_compression_calibration"
NUM_CALIBRATION_SAMPLES = 128
MAX_SEQUENCE_LENGTH = 2048

# Load model and tokenizer
"""
The model is first loaded onto the cpu, as indicated through the use of None for the device_map argument in the from_pretrained method when loading the model.
uring oneshot, only one gpu is required which will be used to onload each layer for calibration in a sequential manner.
"""
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="cpu",
    dtype="auto",
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

# Load and preprocess calibration dataset
calib_dataset = load_dataset(DATASET_ID, split=f"train[:{NUM_CALIBRATION_SAMPLES}]")
calib_dataset = calib_dataset.shuffle(seed=42)

def preprocess(example):
    return {
        "text": tokenizer.apply_chat_template(
            [{"role": "user", "content": example["text"]}],
            tokenize=False,
        )
    }

calib_dataset = calib_dataset.map(preprocess)

# Tokenize calibration dataset
def tokenize(example):
    return tokenizer(
        example["text"],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        add_special_tokens=False,
    )

calib_dataset = calib_dataset.map(tokenize, remove_columns=calib_dataset.column_names)

# Define AWQ quantization recipe
recipe = [
    AWQModifier(
        ignore=["lm_head"],
        scheme="W4A16_ASYM",
        targets=["Linear"],
    ),
]

# Run quantization with calibration
oneshot(
    model=model,
    tokenizer=tokenizer,
    dataset=calib_dataset,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    output_dir=OUTPUT_PATH,
    pipeline="sequential",
)
```

This repository contains the Tower+ 72B model, as presented in the paper [Tower+: Bridging Generality and Translation Specialization in Multilingual LLMs](https://huggingface.co/papers/2506.17080).

Project Page: [https://huggingface.co/collections/Unbabel/tower-plus-6846ca452a10c0905dc03c0f](https://huggingface.co/collections/Unbabel/tower-plus-6846ca452a10c0905dc03c0f)

![Tower Plus Pareto](./Tower-plus-pareto.png)

# Model Description:

**Tower+ 72B** is build on top of Qwen 2.5 72B. The model goes through the Continuous Pretraining (CPT), Instruction Tuning (IT) and Weighted Preference Optimization (WPO). During all these stages we include parallel and multilingual data (covering 22 languages).

-   **Developed by:** Unbabel
-   **Model type:** A 72B parameter model fine-tuned on a mix of _translation-related tasks_ as well as _general instruction-following_ datasets that include reasoning, code instructions, etc.
-   **Languages:** German, Spanish, French, Italian, Korean, Dutch, Russian, English, Portuguese (Portugal), Portuguese (Brazilian), Spanish (Latin America), Chinese (Simplified), Chinese (Traditional), Czech, Ukrainian, Hindi, Icelandic, Japanese, Polish, Swedish, Hungarian, Romanian, Danish, Norwegian (Nynorsk), Norwegian (Bokmål), Finnish
-   **License:** CC-BY-NC-4.0
-   **Context Size:**: 131,072 tokens (recommended generation tokens 8192)

# Intended uses & limitations

Tower is intended for multilingual tasks and its specially strong on translation related tasks.

Another usecase Tower works well is for creating multilingual synthethic data (for the languages it covers). You can do this either by translating instructions and the respective answers or by asking the model to create an instruction given a document as seed data.

# Usage:

When using the model, make sure your prompt is formated correctly!

Also, we recommend using VLLM rather than Hugging Face.

### Using on VLLM:

```python
# pip install vllm
from vllm import LLM, SamplingParams
sampling_params = SamplingParams(
  best_of=1,
  temperature=0,
  max_tokens=8192,
)
llm = LLM(model="Unbabel/Tower-Plus-72B", tensor_parallel_size=4)
messages = [{"role": "user", "content": "Translate the following English source text to Portuguese (Portugal):\nEnglish: Hello world!\nPortuguese (Portugal): "}]
outputs = llm.chat(messages, sampling_params)
# Make sure your prompt_token_ids look like this
print (outputs[0].outputs[0].text)
# > Olá, mundo!
```

### Using on Transformers:

```python
# pip install transformers
# pip install accelerate
import torch
from transformers import pipeline
pipe = pipeline("text-generation", model="Unbabel/Tower-Plus-72B", device_map="auto")
# We use the tokenizer’s chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [{"role": "user", "content": "Translate the following English source text to Portuguese (Portugal):\nEnglish: Hello world!\nPortuguese (Portugal): "}]
input_ids = pipe.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
outputs = pipe(messages, max_new_tokens=256, do_sample=False)
print(outputs[0]["generated_text"])
```

# Citation
If you use this model please cite our paper:
```
@misc{rei2025towerplus,
      title={Tower+: Bridging Generality and Translation Specialization in Multilingual LLMs}, 
      author={Ricardo Rei and Nuno M. Guerreiro and José Pombal and João Alves and Pedro Teixeirinha and Amin Farajian and André F. T. Martins},
      year={2025},
      eprint={2506.17080},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.17080}, 
}
```