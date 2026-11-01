---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
base_model: skt/A.X-3.1-Light
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- instruction-tuning
- merged-model
- answer-first
---

# A.X-3.1-Light SFT B12K QCDD 1E

This is a full BF16 model obtained by merging a LoRA supervised fine-tuning
adapter into [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light).
No separate adapter is required for inference.

## Model description

This model is a Korean question-answering and instruction-following model
fine-tuned to place the answer first and optionally provide a short reason.
The training set was selected from a frozen AI Hub candidate universe using
quality, complexity, difficulty, and diversity-aware selection. The model is
intended for research and evaluation of Korean text generation; its answers
can be incorrect and it is not a substitute for professional judgment.

## Training

- Base model: `skt/A.X-3.1-Light`
- Base revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Method: LoRA supervised fine-tuning with assistant-only causal-LM loss
- Precision: BF16
- Epochs: 1
- Learning rate: `5e-5`
- Effective batch size: 8
- Maximum sequence length: 2,048
- Optimizer: `adamw_torch_fused`
- Scheduler: linear
- Warmup steps: 0
- Weight decay: 0
- Seed: 42
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Training examples: 12,000
- Training objective: `정답: <label or answer> (근거: 짧은 설명)` answer-first format

The selected set contains 8,851 examples with a reasoning target and 3,149
examples without a reasoning target. The target contract limits an optional
reason to a short explanation. Nine long-context examples required context
trimming during serialization; no training target was truncated.

## Training data

The examples were selected from 258,170 frozen clean candidates under the
`kds.selection.B12K_qcdd_scale.v1` policy, preserving the STEP 10 A1
source-independent greedy-selection semantics. Benchmark questions, answers,
and evaluation artifacts are not included in this repository.

| AI Hub dataset | Description | Selected examples |
|---|---|---:|
| 569 | 행정 문서 대상 기계독해 | 6,894 |
| 71610 | 금융·법률 문서 기계독해 | 1,594 |
| 71857 | 국어 교과 지문형 문제 | 1,476 |
| 71874 | 전문 의학지식 | 2,036 |

The source datasets are referenced by dataset ID only. Users must follow the
applicable AI Hub terms of use.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/AX-3.1-Light-sft_B12K_qcdd_1e"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

Use the tokenizer's bundled chat template for conversational inference.

## Local evaluation

These are local proxy results on the KDS canonical suite, not official K-AI
leaderboard scores. The main average is the unweighted mean of the five main
axes below, using the deterministic `B1_constrained` probe. HLE uses the
text-only subset; Original MuSR is supplementary.

| Metric | Score |
|---|---:|
| Main-axis average | 42.56% |
| KMMLU-Pro | 37.88% |
| CLIcK | 65.01% |
| HLE text-only | 4.68% |
| SNU Ko-MuSR | 53.07% |
| Com2-main | 52.16% |

## License and limitations

This model is derived from the Apache-2.0 licensed `skt/A.X-3.1-Light` model.
The original base-model license, notices, and SK Telecom trademark terms also
apply. AI Hub dataset terms apply to the source data. See `LICENSE` for the
redistribution notice.

This model can produce inaccurate, incomplete, or poorly formatted answers.
It should not be used as the sole basis for medical, legal, financial, or
other high-impact decisions.
