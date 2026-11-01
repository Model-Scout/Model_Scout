---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Math Synthetic (Reasoning SFT)
size_categories:
- 100K<n<1M
tags:
- korean
- synthetic
- rosetta
- math
- sft-think
extra_gated_prompt: >-
  By clicking "Agree" I confirm I have read and agree to the PoSTMEDIA Data Agreement
  for Model Training and agree that I intend to use this data for model training
  purposes only.
extra_gated_fields:
  Company: text
  Institutional Email: text
  Intended use: text
  I agree to use this dataset for model training purposes ONLY: checkbox
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
---
# rosetta-ko-math-synth-sft-think

Korean-native mathematics data — problems with step-by-step Korean solutions, answer-verified by Math-Verify (LaTeX `\boxed{}` + symbolic equivalence).

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Math Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-math-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| **[`rosetta-ko-math-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-sft-think)** (this repo) | reasoning SFT (`<think>` chain-of-thought) |
| [`rosetta-ko-math-synth-dpo`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-dpo) | preference pairs (`chosen`/`rejected`) |
| [`rosetta-ko-math-synth-dpo-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-dpo-think) | reasoning preference pairs |
| [`rosetta-ko-math-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-rlvr) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "math",
 "messages": [{"role": "user", "content": "..."},
              {"role": "assistant", "content": "..."}]}
```
- `id` — row-level identifier
- `messages[0]` (user) — self-contained Korean prompt
- `messages[1]` (assistant) — <think> native-Korean reasoning </think> + final answer

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-math-synth-sft-think", split="train")
```

## License

Released under the **Apache License 2.0**.

Seed sources:
- [AI-MO/NuminaMath-1.5](https://huggingface.co/datasets/AI-MO/NuminaMath-1.5)
- [OLAIR/numina_math_ko_verifiable_540k](https://huggingface.co/datasets/OLAIR/numina_math_ko_verifiable_540k)
- [nvidia/OpenMathInstruct-2](https://huggingface.co/datasets/nvidia/OpenMathInstruct-2)
- [nvidia/OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning)
- [zwhe99/DeepMath-103K](https://huggingface.co/datasets/zwhe99/DeepMath-103K)
- [SynthLabsAI/Big-Math-RL-Verified](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified)

## Citation

```bibtex
@misc{rosetta_ko_math_synth,
  title  = {Rosetta-KO Math Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-math-synth-sft-think}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

