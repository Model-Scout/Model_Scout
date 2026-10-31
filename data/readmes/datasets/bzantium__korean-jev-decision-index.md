---
language:
- ko
- en
license: other
license_name: per-source-licenses
license_link: https://huggingface.co/datasets/bzantium/korean-jev-decision-index/blob/main/LICENSES.md
pretty_name: Korean Jev Decision Index
configs:
- config_name: default
  default: true
  data_files:
  - split: test
    path: data/test.parquet
- config_name: complete_cases
  data_files:
  - split: test
    path: data/cases.parquet
- config_name: paired_math
  data_files:
  - split: test
    path: data/paired_math.parquet
- config_name: paired_code
  data_files:
  - split: test
    path: data/paired_code.parquet
- config_name: paired_intent
  data_files:
  - split: test
    path: data/paired_intent.parquet
---

# Korean Jev Decision Index

A Korean benchmark for decision models. Given a state and a question, models predict probabilities over answer choices, yes/no judgments, or ratings.

- **82,452 evaluation requests** across five areas, from reasoning and language understanding to tool use and response preferences.
- Built from Korean datasets and published Korean translations of math and preference data.
- Uses the five areas and weights from [Jev Decision Index 0.3](https://github.com/apolinario/decision-index).

## Composition

| Area | Weight | Requests | Sources and tasks |
|---|---:|---:|---|
| Knowledge & Reasoning | 25.8% | 61,077 | [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) and [KoBEST](https://huggingface.co/datasets/skt/kobest_v1) COPA/HellaSwag; [NOLLI](https://huggingface.co/datasets/HAERAE-HUB/NOLLI) causal graphs, inequalities and minesweeper; [GSM8K](https://github.com/openai/grade-school-math) problems translated in [HRM8K](https://huggingface.co/datasets/HAERAE-HUB/HRM8K). |
| Language Understanding | 25.8% | 16,328 | KoBEST BoolQ/WiC/SentiNeg; [RTP-LX](https://huggingface.co/datasets/ToxicityPrompts/RTP-LX) toxicity ratings; [SQuARe](https://github.com/naver-ai/korean-safety-benchmarks) response acceptability. |
| Retrieval & Classification | 20.0% | 938 | Relevant-passage selection from [MIRACL](https://huggingface.co/datasets/miracl/miracl) and its [corpus](https://huggingface.co/datasets/miracl/miracl-corpus); deciding whether passages contain relevant evidence in [NoMIRACL](https://huggingface.co/datasets/miracl/nomiracl). |
| Tools & Automation | 18.3% | 1,323 | [FunctionChat-Bench](https://github.com/kakao/FunctionChat-Bench): deciding when to call a tool, selecting functions and arguments, and choosing actions in dialogs. |
| Arts & Human Taste | 10.0% | 2,786 | Korean translations of preferred/rejected response pairs from [Multilingual RewardBench](https://huggingface.co/datasets/CohereLabsCommunity/multilingual-reward-bench), based on [RewardBench](https://huggingface.co/datasets/allenai/reward-bench). |

We kept the source text and answers, added Korean instructions, and converted each task to the decision format. GSM8K uses Jev 0.3's 4-choice and 10-choice options; SQuARe keeps its majority labels and annotator votes.

We excluded examples found in our training, validation and calibration sets, together with related variants. We also dropped inconsistent answers and translations that changed the problem's meaning. We used an AI assistant to check the math translations, without a separate human review.

## Quickstart

```python
import json
from datasets import load_dataset

test = load_dataset("bzantium/korean-jev-decision-index", split="test")
sample = json.loads(test[0]["sample"])
state, question, target = sample["state"], sample["question"], sample["target"]
```

The `sample` column holds the full request as JSON text. Other columns identify its source and group and provide passage attribution. All samples are included as Parquet.

The dataset has five configurations:

- **`default`** is the full benchmark: 82,452 requests. Use this for the Korean Index score.
- **`complete_cases`** contains grouping records for 773 NOLLI puzzles and 43 FunctionChat dialogs in `default`. Each record lists the request IDs that belong to one case, so the scorer can check whether the whole puzzle or dialog is correct. These are scoring metadata, not additional model inputs.
- **`paired_math`** contains the same 799 math problems in English and Korean, with both 4-choice and 10-choice questions. Use its 3,196 requests to compare languages on matched problems. Its 1,598 Korean requests are already included in `default`.
- **`paired_code`** contains 567 CRUXEval programs in English and Korean: 1,134 output-selection requests, scored separately from `default`.
- **`paired_intent`** contains 4,125 CLINC intent/OOS utterances in English and Korean: 8,250 requests, scored separately from `default`.

```python
paired = load_dataset("bzantium/korean-jev-decision-index", "paired_math", split="test")
code = load_dataset("bzantium/korean-jev-decision-index", "paired_code", split="test")
intent = load_dataset("bzantium/korean-jev-decision-index", "paired_intent", split="test")
```

## Scoring

Download `score.py`, `requirements.txt` and the `data/` Parquet files, then run:

```bash
pip install -r requirements.txt
python score.py --predictions predictions.jsonl
python score.py --config paired_math --predictions paired_predictions.jsonl
python score.py --config paired_code --predictions code_predictions.jsonl
python score.py --config paired_intent --predictions intent_predictions.jsonl
```

Predictions contain `id`, `status: "ok"`, `candidate_ids` in the given order, and `probabilities`. Missing or unsupported predictions are scored as failures.

The default Index ranges from **0 (chance) to 100 (perfect)**. Chance-adjusted task scores are averaged within each area and combined using the weights above. Related tasks from the same source share a scoring unit.

Scoring requires complete puzzles, all queried argument fields, and both math tracks. KMMLU averages subjects; NOLLI averages puzzle types and difficulty levels. Toxicity ratings use ranked probability score (RPS). See [score.py](score.py) for task metrics. The paired scorer also reports the language difference and bootstrap confidence intervals.

## Notes

- The English and Korean Index cover different tasks, so their overall scores are not a matched language comparison. Use the paired math, code or intent subsets to compare languages on the same examples.
- The default panel does not cover code, chess, or intent classification with out-of-scope detection. Code output selection and intent/OOS classification are available in the paired subsets. Tool tasks ask models to choose actions from fixed histories; they do not execute tools.
- Preference labels come from English responses and have not been rated again in Korean.


## Paired code

`paired_code` contains 567 [CRUXEval](https://github.com/facebookresearch/cruxeval) programs in English and Korean: 1,134 requests. It uses the output choices from [Jev Decision Index 0.3](https://github.com/apolinario/decision-index). Python code, inputs, candidate order and original answers are unchanged; only the fixed task name and instruction are translated into Korean. Three program pairs were excluded by the known-input overlap check.

The scorer reports accuracy and chance-adjusted skill points for each language, plus a paired bootstrap interval for the language difference. Candidate sets have 2–10 values; uniform chance is averaged over the selected programs. This measures output selection under two instruction languages, rather than generated code or native Korean code authorship. It is a separate comparison subset and does not change the default Index score.

## Paired intent

`paired_intent` combines original [CLINC](https://github.com/clinc/oos-eval)
English utterances with reviewed [CLINC150-ko](https://huggingface.co/datasets/neuralfoundry-coder/clinc150-ko)
translations. We removed known input overlaps and translations that changed the
meaning, retaining 4,125 matched utterances and all 151 original intent/OOS classes.
Original annotations and canonical API intent names are preserved. Candidate
descriptions stay English in both views; the utterance language changes.

The scorer reports macro-F1, OOS F1, accuracy, coverage and class support, with
paired text-group bootstrap intervals. Some classes have only two or three
examples. These scores describe the reviewed subset; the original labels were
not annotated again. The subset does not change the default Index score.

## Sources and licenses

Source licenses, revisions and notices are in [LICENSES.md](LICENSES.md). Sample metadata records source IDs and conversions; Wikipedia passages include article and contributor-history links. This evaluation dataset is excluded from this project's training and model selection.
