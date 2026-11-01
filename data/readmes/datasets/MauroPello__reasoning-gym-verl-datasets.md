---
configs:
- config_name: default
  data_files:
  - split: train
    path: train.parquet
  - split: train_interleaved
    path: train_interleaved.parquet
  - split: validation
    path: val.parquet
  - split: validation_mini
    path: val_mini.parquet
  - split: held_out_languages
    path: held_out_languages_validation.parquet
  - split: held_out_tasks
    path: held_out_tasks.parquet
license: apache-2.0
task_categories:
- text-generation
language:
- en
- de
- es
- fr
- hi
- it
- ja
- ko
- pt
- ru
- uk
- zh
- nl
- tr
tags:
- reasoning-gym
- verl
- grpo
- alignment
---

# reasoning-gym-verl-datasets

This dataset contains procedurally generated reasoning tasks from the [Reasoning Gym (r-gym)](https://github.com/open-thought/reasoning-gym) framework, structured and pre-processed in parquet format for training models with [veRL](https://github.com/volcengine/verl).

These datasets were used to train **[MauroPello/Qwen3-1.7B-RL-final](https://huggingface.co/MauroPello/Qwen3-1.7B-RL-final)** using GRPO (Group Relative Policy Optimization).

## Dataset Splits & Structure

| Split Name | Path | Size (Examples) | Description |
|------------|------|-----------------|-------------|
| `train` | `train.parquet` | 100,000 | Raw training set containing randomly sampled tasks across English and translation languages. |
| `train_interleaved` | `train_interleaved.parquet` | 100,000 | Stratified training set where rows are interleaved across tasks and languages to stabilize learning and gradient updates in RL. |
| `validation` | `val.parquet` | 10,000 | Main validation dataset. |
| `validation_mini` | `val_mini.parquet` | ~1,000 | Mini validation dataset containing one example per task-language specification. |
| `held_out_languages` | `held_out_languages_validation.parquet` | 2,000 | Generalization test set covering languages not included in SFT or training (Dutch `nl`, Turkish `tr`). |
| `held_out_tasks` | `held_out_tasks.parquet` | 1,040 | Generalization test set covering tasks held out during training (e.g. `circuit_logic`, `codeio`, `emoji_mystery`, `game_of_life_halting`, `propositional_logic`, `rush_hour`, `string_insertion`, `tsumego`). |

## Usage

You can load these splits directly using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

# Load train_interleaved (used for RL training)
dataset = load_dataset("MauroPello/reasoning-gym-verl-datasets", split="train_interleaved")

# Load generalization tasks validation split
held_out_tasks = load_dataset("MauroPello/reasoning-gym-verl-datasets", split="held_out_tasks")
```

Each example contains:
- `data_source`: The identifier of the Reasoning Gym task.
- `prompt`: Conversational turn list containing the system instructions and user request.
- `ability`: Capability tag (always `rgym`).
- `reward_model`: Dictionary containing the expected `ground_truth` and matching rule style.
- `extra_info`: Metadata specifying the target language, original indices, task name, and developer prompt options.
