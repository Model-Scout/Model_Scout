---
license: cc-by-nc-sa-4.0
language:
- ko
size_categories:
- n<1K
task_categories:
- text-generation
pretty_name: Korean AIME 2025
configs:
- config_name: default
  data_files:
  - split: test
    path: test.jsonl
---

# KoAIME25

30 Korean-language AIME 2025 problems for mathematical reasoning evaluation, with integer gold answers.

```python
from datasets import load_dataset

data = load_dataset("bzantium/koaime25", split="test")
```

Fields: `id`, `problem` (Korean statement with LaTeX), and `expected_answer` (string).

`koaime25-N` corresponds to `aime25-N` in nemo-skills-harness; IDs use 0–29. Rows are ordered by original problem number (AIME I, then II).

## Sources and review

Uses the pinned MathArena AIME 2025 statements. Mathematics and diagrams are retained; Korean sentence order and terminal punctuation are adapted.

Source: [MathArena AIME 2025](https://huggingface.co/datasets/MathArena/aime_2025/tree/c94da77eb22bbd6439e62a323bec18493a421302); original contest: Mathematical Association of America. [AIME I](https://live.poshenloh.com/past-contests/aime/2025I) and [AIME II](https://live.poshenloh.com/past-contests/aime/2025II) provide MAA-authorized reference statements. See `source.jsonl` for English comparison statements and `provenance.json` for pinned revisions and the Korean data checksum.

Translation and review were performed in separate AI-assisted passes. All 30 answers and the source mapping were checked. This is not an official MAA translation or an independent bilingual human review. Model evaluation scores are not used to select or rewrite statements.

## License

The MathArena source versions are distributed under CC BY-NC-SA 4.0. This Korean adaptation retains those terms and attributes the original problems to MAA and source transcription to MathArena. Original problem rights remain with their respective owners.
