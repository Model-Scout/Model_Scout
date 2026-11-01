---
license:
- apache-2.0
- cc-by-nc-2.0
pretty_name: Step-3.5-Flash-SFT
language:
- multilingual
task_categories:
- text-generation
tags:
- chat
- sft
- instruction-tuning
- reasoning
- code
- agent
---

# Step-3.5-Flash-SFT

`Step-3.5-Flash-SFT` is a general-domain supervised fine-tuning release for chat models.

This repository keeps the full training interface in one place:

- `json/`: canonical raw training data
- `tokenizers/`: tokenizer snapshots for Step-3.5-Flash and Qwen3, released to preserve chat-template alignment
- `compiled/`: tokenizer-specific compiled shards for StepTronOSS training

## Data Format

Each raw shard is a JSON file whose top level is a list of examples. Each example currently contains a `conversations` field with ordered message turns.

```json
{
  "conversations": [
    {
      "role": "user",
      "content": "...",
      "loss_mask": 1,
      "name": "",
      "meta": {}
    },
    {
      "role": "assistant",
      "content": "...",
      "loss_mask": 1,
      "name": "",
      "meta": {},
      "reasoning_content": "..."
    }
  ]
}
```

Observed fields:

- `role`: speaker role such as `user` or `assistant`
- `content`: visible message text
- `loss_mask`: turn-level supervision flag
- `name`: optional speaker name
- `meta`: per-turn metadata
- `reasoning_content`: optional assistant-side field present in some examples

## Recommended Training Framework

The official recommended training framework for this release is [StepTronOSS](https://github.com/stepfun-ai/SteptronOss).

Reproduce our experiment: [step3p5_flash_sft_step3_data_muon.py](https://github.com/stepfun-ai/SteptronOss/blob/dev/playground/sft/step3/step3p5_flash_sft_step3_data_muon.py)

Important compatibility rules:

- Train this dataset with `Sequential sampler`. Do not shuffle when reproducing the StepTronOSS recipe.
- Do not mix tokenizer variants and compiled variants.
- Use `transformers<5.0` for `apply_chat_template(...)`.
- Raw JSON is the origin. Compiled shards are tokenizer-specific acceleration artifacts for StepTronOSS.

## StepTronOSS Training Semantics

In the StepTronOSS reference SFT path, dialogs are tokenized with the selected Hugging Face chat template and then packed sequentially. Training loss is applied only to assistant tokens after the last user turn when that turn has `loss_mask = 1`.

This means tokenizer snapshots are part of the effective training definition, not optional metadata.

## Using With StepTronOSS

Reference recipes:

- Step-3.5-Flash uses `Recipe0311CompiledSFTDataConfig`
- Qwen3 uses `Recipe0311QwenCompiledSFTDataConfig`

Representative StepTronOSS files:

- `playground/sft/step3/step3_flash_sft_step3_data_muon.py`
- `playground/sft/qwen3/qwen3_30a3b_sft_step3_data.py`

Minimal local pattern for Step-3.5-Flash compiled data:

```python
from pathlib import Path

from playground.data.sft.oss260312.step_sft_data_config0311 import Recipe0311SFTDataConfig
from playground.tools.compile_recipe import CompiledDataRecipe, CompiledDatasetsConfig
from playground.pretrain.step3p5.step3p5_flash import Step3p5FlashModelConfig
from playground.sft.qwen3.qwen3_sft_base import Exp as BaseExp

DATA_ROOT = Path("/path/to/Step-3.5-Flash-SFT")


class PublicStep3p5CompiledDatasetsConfig(CompiledDatasetsConfig):
    compiled_recipe = CompiledDataRecipe(
        domains={"general": str(DATA_ROOT / "compiled/step3p5_flash/general")},
        epochs={"general": 1},
    )


class PublicStep3p5CompiledSFTDataConfig(Recipe0311SFTDataConfig):
    dataset_cfg = PublicStep3p5CompiledDatasetsConfig


class Exp(BaseExp):
    model_cfg = Step3p5FlashModelConfig
    data_cfg = PublicStep3p5CompiledSFTDataConfig
```

Run with the matching tokenizer:

```bash
torchrun --standalone --nproc-per-node=8 your_exp.py \
  tokenizer_cfg.tokenizer_path=/path/to/Step-3.5-Flash-SFT/tokenizers/step3p5_flash
```

For Qwen3, point the compiled data root to `compiled/qwen3/general` and the tokenizer path to `tokenizers/qwen3`.

## How To Compile

StepTronOSS provides tokenizer-specific compile entrypoints:

- `playground/data/sft/oss260312/step_sft_data_config0311_step3p5_tokenizer.py`
- `playground/data/sft/oss260312/step_sft_data_config0311_qwen_tokenizer.py`

Compile Step-3.5-Flash:

```bash
cd /path/to/SteptronOss
python3 playground/data/sft/oss260312/step_sft_data_config0311_step3p5_tokenizer.py \
  --tokenizer-path /path/to/Step-3.5-Flash-SFT/tokenizers/step3p5_flash
```

Compile Qwen3:

```bash
cd /path/to/SteptronOss
python3 playground/data/sft/oss260312/step_sft_data_config0311_qwen_tokenizer.py \
  --tokenizer-path /path/to/Step-3.5-Flash-SFT/tokenizers/qwen3
```

Notes:

- Use the tokenizer snapshot that matches the compiled variant you want to generate.
- Keep `transformers<5.0` in the compile environment.
- The reference scripts write to tokenizer-specific `COMPILED_ROOT_...` paths defined in the scripts.

## Raw JSON Loading

Raw JSON shards can also be inspected with `datasets`:

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files={"train": "json/general/chunk_*.json"})
print(dataset["train"][0]["conversations"])
```

## Notes

- This is a training corpus, not a benchmark.
- Some assistant turns include `reasoning_content` in addition to final `content`; downstream users may keep, remove, or transform that field depending on their training recipe.
- Compiled datasets are StepTronOSS-specific derived artifacts and are not intended as a framework-agnostic exchange format.

## Responsible Data Disclosure: Advancing Open Source While Safeguarding Commercial Sustainability

We are committed to open data and research, and strive to strike a balance between maximal transparency and the protection of legitimate commercial interests.


## License

This dataset is made available under both Apache-2.0 and CC-BY-NC-2.0.

For the avoidance of doubt, use of this dataset requires compliance with both licenses simultaneously. This is not an alternative-license grant, and users may not choose to comply with only one of the two licenses.
