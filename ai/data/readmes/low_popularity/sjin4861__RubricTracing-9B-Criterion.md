---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
language:
- ko
pipeline_tag: text-generation
library_name: transformers
tags:
- knowledge-tracing
- education
- rubric
- mathematics
---

# RubricTracing-9B-Criterion

**Rubric Tracing** is knowledge tracing over item-specific rubrics. This model performs
**criterion-level forecasting**: given a student's past interactions and the rubric of the next
problem, it predicts, for each criterion of that problem, whether the student will satisfy it.

It is [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), fully fine-tuned on
[KT-PSP-25](https://huggingface.co/datasets/jungypark/KT-PSP-25) (Korean first-year high-school
mathematics). Its item-level counterpart is
[RubricTracing-9B-Item](https://huggingface.co/sjin4861/RubricTracing-9B-Item).

## Input and output

The student's history is rendered as a **full rubric history**. For each past problem, it contains
the problem, its criteria, the student's Pass/Fail verdict on each criterion together with the
grader's rationale, and the student's written problem-solving process. The target problem follows,
with its reference solution and rubric. The prompts are in Korean, and the system prompt the model
was trained with is `system_prompt.txt` in this repository.

The model answers with a single JSON object, with one verdict per criterion id:

```json
{"verdicts": [{"id": 1, "satisfied": true}, {"id": 2, "satisfied": false}, {"id": 3, "satisfied": false}]}
```

## Results

Results are on the held-out test cohort: 268 students and 4,165 target interactions. Pass denotes
a satisfied criterion. Fine-tuned rows are the mean ± standard deviation over five trainings.

| Model | Macro-F1 | Acc | Pass P | Pass R | Fail P | Fail R |
|---|---|---|---|---|---|---|
| Always-pass | 0.442 | 0.792 | 0.792 | 1.000 | 0.000 | 0.000 |
| Qwen3.5-9B, zero-shot | 0.562 | 0.757 | 0.814 | 0.900 | 0.360 | 0.215 |
| **RubricTracing-9B-Criterion** | **0.610 ± 0.005** | **0.777 ± 0.002** | 0.829 ± 0.002 | 0.905 ± 0.003 | 0.448 ± 0.007 | 0.293 ± 0.011 |

## Revisions

`main` holds the fold-0 model. The branches `fold0` to `fold4` hold all five trainings. Each was
trained on a different train/validation split and evaluated on the same test cohort, and the table
above averages over them.

## Usage

```python
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "sjin4861/RubricTracing-9B-Criterion"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype="bfloat16", device_map="auto")
system = open(hf_hub_download(repo, "system_prompt.txt"), encoding="utf-8").read()

messages = [{"role": "system", "content": system},
            {"role": "user", "content": rubric_history_and_target}]
ids = tok.apply_chat_template(messages, add_generation_prompt=True, enable_thinking=False,
                              return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=256, do_sample=False, eos_token_id=tok.eos_token_id)
print(tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True))
```

- Pass `enable_thinking=False`. The model was trained and evaluated without the thinking block.
- Pass `eos_token_id=tok.eos_token_id` (`<|im_end|>`). The bundled `generation_config.json` also
  stops on it. Without it, generation can continue past the answer.
- The code that renders a rubric history in the trained format is released with the paper.

## Training

- Full fine-tuning of Qwen3.5-9B.
- Learning rate 1e-5 with cosine decay and 3% warmup, no weight decay, gradient clipping at 1.0,
  gradient accumulation of 4, seed 0, four epochs.
- Checkpoint selection: the epoch with the highest Macro-F1 on freely generated answers over a
  fixed sample of 1,000 validation interactions.
- Supervision: criterion verdicts from rubric label set `22289-be26167af4e4`. It was produced by
  a Generator–Grader–Auditor pipeline over Qwen3.5-27B, which writes one rubric per problem and
  grades each student's written solution against it.

## Limitations

- The model was trained and evaluated on one dataset: Korean first-year high-school mathematics.
- Its supervision is model-graded, not human-graded.
- KT-PSP-25 has no recoverable interaction order, so the history is treated as a set. Nothing here
  is a claim about sequence modelling.
- The model forecasts outcomes for research on knowledge tracing. It is not validated for grading
  or for high-stakes decisions about individual students.
