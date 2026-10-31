---
dataset_info:
- config_name: de
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 112194692
    num_examples: 10000
  download_size: 55470235
  dataset_size: 112194692
- config_name: en
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 118839202
    num_examples: 11400
  download_size: 59479060
  dataset_size: 118839202
- config_name: es
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 115049190
    num_examples: 10000
  download_size: 56715198
  dataset_size: 115049190
- config_name: fr
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 115896846
    num_examples: 10000
  download_size: 57154915
  dataset_size: 115896846
- config_name: hi
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 160225278
    num_examples: 10000
  download_size: 79264346
  dataset_size: 160225278
- config_name: it
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 113354149
    num_examples: 10000
  download_size: 56114042
  dataset_size: 113354149
- config_name: ja
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 120417106
    num_examples: 10000
  download_size: 59599554
  dataset_size: 120417106
- config_name: ko
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 116798018
    num_examples: 10000
  download_size: 57019302
  dataset_size: 116798018
- config_name: pl
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 112764209
    num_examples: 10000
  download_size: 55941481
  dataset_size: 112764209
- config_name: pt
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 112771620
    num_examples: 10000
  download_size: 55575982
  dataset_size: 112771620
- config_name: ru
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 146321134
    num_examples: 10000
  download_size: 72719585
  dataset_size: 146321134
- config_name: uk
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 143150035
    num_examples: 10000
  download_size: 70962683
  dataset_size: 143150035
- config_name: zh
  features:
  - name: task_name
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_llm_generated
    dtype: bool
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    dtype: string
  - name: curriculum_level
    dtype: int64
  - name: curriculum_max_levels
    dtype: int64
  - name: curriculum_attributes
    dtype: string
  - name: config
    dtype: string
  - name: oracle_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: llm_boxed_answer
    dtype: string
  splits:
  - name: train
    num_bytes: 114632940
    num_examples: 10000
  download_size: 56314885
  dataset_size: 114632940
configs:
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: pl
  data_files:
  - split: train
    path: pl/train-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: uk
  data_files:
  - split: train
    path: uk/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- en
- de
- fr
- es
- hi
- it
- ja
- ko
- pl
- pt
- ru
- uk
- zh
tags:
- reasoning
- mathematics
- logic
- sft
- reinforcement-learning
- reasoning-gym
- synthetic-data
---


# Reasoning Gym SFT Dataset

This dataset contains Supervised Fine-Tuning (SFT) reasoning data procedurally generated using **Reasoning Gym** environments.

It is designed to train reasoning models (such as DeepSeek-R1-style or Qwen-Coder-style models) to explain their step-by-step reasoning chain before outputting a final answer wrapped inside LaTeX `\boxed{...}`.

## Where Does This Dataset Come From?

This dataset is procedurally generated from **Reasoning Gym**, an open-source library of procedural dataset generators and algorithmically verifiable environments for training and evaluating reasoning models.

* **Original Open-Source Project**: [open-thought/reasoning-gym](https://github.com/open-thought/reasoning-gym)
* **What it provides**: Over 100 reasoning tasks spanning algebra, arithmetic, logic, geometry, graph theory, cognition, and common games.

While Reasoning Gym is typically used to dynamically generate training data or act as a gym environment during reinforcement learning (RL) loops, this dataset represents a pre-computed offline SFT corpus. It translates the environments into multi-turn SFT conversation traces across multiple languages, with optional step-by-step reasoning chains bootstrapped and verified against the environments' programmatic verifiers.

---

## Dataset Structure

The dataset contains the following columns/features:

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `task_name` | `string` | The unique name of the Reasoning Gym task (e.g., `spell_backward`, `number_sorting`, `rubiks_cube`). |
| `language` | `string` | The language code of the prompt and response (e.g., `en`, `de`, `fr`, `zh`). |
| `question` | `string` | The input user prompt/question generated by the Reasoning Gym task environment. |
| `answer` | `string` | The target assistant response. Depending on configuration, it is either the raw oracle answer or the verified, step-by-step LLM-generated reasoning chain. |
| `answer_llm_generated` | `bool` | `True` if the answer contains a verified step-by-step explanation generated by a bootstrapped LLM, `False` if it uses the default short oracle answer. |
| `messages` | `list` | Conversation messages in standard chat template format (System, User, Assistant) for direct SFT training. |
| `metadata` | `string` | A JSON-serialized string containing task execution details, intermediate states, and reasoning parameters. |
| `curriculum_level` | `int64` | The 0-indexed level of the task's curriculum configuration, if applicable; otherwise `null`. |
| `curriculum_max_levels` | `int64` | The total number of levels available in the task's curriculum; otherwise `null`. |
| `curriculum_attributes` | `string` | A JSON-serialized string of task attributes matching the curriculum level; otherwise `null`. |
| `config` | `string` | A JSON-serialized string of the exact configuration dict used to initialize the task generator. |
| `oracle_answer` | `string` | The original ground truth oracle answer generated by the environment. |
| `llm_answer` | `string` | The raw unfiltered assistant explanation returned by the LLM (if LLM generation was enabled); otherwise `null`. |
| `llm_boxed_answer` | `string` | The extracted final answer content from within the `\boxed{...}` tags of the LLM response; otherwise `null`. |

---

## Generation & Verification Pipeline

The dataset is generated using procedural configurations from Reasoning Gym tasks and optionally enriched via LLM bootstrapping:

1. **Procedural Task Generation**: Reasoning Gym constructs the question and deterministic metadata. If curriculum learning is supported for the task, examples are distributed across curriculum levels.
2. **System Prompt Injection**: Examples are framed using a system prompt that requests a step-by-step reasoning path ending with a single final answer inside `\boxed{...}`.
3. **LLM Bootstrapping & Programmatic Verification (Optional)**:
   - During generation, a bootstrapped LLM is queried to produce step-by-step explanations.
   - The LLM-generated explanation is verified by extracting the `\boxed{...}` answer and validating it using Reasoning Gym's native programmatic scorer.
   - If the score matches or exceeds the threshold (`1.0`), the explanation is saved in `answer` and `messages`. Otherwise, it falls back to the ground truth oracle target to maintain dataset quality.

---

## How to Use

### 1. Loading the Dataset

You can load the dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("username/reasoning-gym-sft", "en")

# View the first example
print(dataset["train"][0])
```

### 2. Formatting for Chat/SFT Training

The `messages` column is ready to use with standard SFT training frameworks like TRL, Axolotl, LLaMA-Factory, or verl. For example:

```json
[
  {
    "role": "system",
    "content": "You are a reasoning assistant. Solve the user's problem by first explaining your reasoning step by step, then conclude with the final answer..."
  },
  {
    "role": "user",
    "content": "How many legs are there in total if you have 1 sea slug, 1 deer?"
  },
  {
    "role": "assistant",
    "content": "A sea slug has 0 legs.\nA deer has 4 legs.\nIn total, 0 + 4 = 4.\nThe final answer is \\boxed{4}."
  }
]
```

### 3. Programmatic Evaluation & Reward Verification (RL / Verification)

Because the dataset preserves the task `config` and `metadata` for every item, you can programmatically reconstruct the environment using the open-source `reasoning-gym` package and score new model completions.

First, install the library:
```bash
pip install reasoning-gym
```

Then, run the scoring routine:
```python
import json
from reasoning_gym.factory import DATASETS

# Extract task and config from dataset row
item = dataset["train"][0]
task_name = item["task_name"]
config_data = json.loads(item["config"])
metadata_data = json.loads(item["metadata"])

# Reconstruct environment
dataset_cls, config_cls = DATASETS[task_name]
env = dataset_cls(config=config_cls(**config_data))

# Score a model response
student_answer = "4" # Extracted from model output
entry = {
    "question": item["question"],
    "answer": item["oracle_answer"],
    "metadata": metadata_data
}

score = env.score_answer(answer=student_answer, entry=entry)
print(f"Verified Score: {score}")  # Returns float representation of success (e.g. 1.0 for correct)
```
