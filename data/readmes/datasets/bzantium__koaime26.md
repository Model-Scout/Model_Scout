---
license: cc-by-nc-sa-4.0
language:
- ko
size_categories:
- n<1K
task_categories:
- text-generation
pretty_name: Korean AIME 2026
configs:
- config_name: default
  data_files:
  - split: test
    path: test.jsonl
---

# KoAIME26

30 Korean-language AIME 2026 problems for mathematical reasoning evaluation, with integer gold answers.

```python
from datasets import load_dataset

data = load_dataset("bzantium/koaime26", split="test")
```

Fields: `id`, `problem` (Korean statement with LaTeX), and `expected_answer` (string).

`koaime26-N` corresponds to `aime26-N` in nemo-skills-harness; IDs use 1–30. Rows are ordered by original problem number (AIME I, then II).

## Sources and review

Uses the pinned MathArena AIME 2026 statements with the verified I #10 perpendicular segment correction (A′C′), and I #13 corrections (nonnegative r; summation index 502m+r). A stray sentence period and empty TeX group after triangle ABC in I #12 are removed.

Source: [MathArena AIME 2026](https://huggingface.co/datasets/MathArena/aime_2026/tree/d2de22f3c656b4f56cf8981212186377d1e23bc3); original contest: Mathematical Association of America. [AIME I](https://live.poshenloh.com/past-contests/aime/2026I) and [AIME II](https://live.poshenloh.com/past-contests/aime/2026II) provide MAA-authorized reference statements. See `source.jsonl` for English comparison statements and `provenance.json` for pinned revisions and the Korean data checksum.

Translation and review were performed in separate AI-assisted passes. All 30 answers and the source mapping were checked. This is not an official MAA translation or an independent bilingual human review. Model evaluation scores are not used to select or rewrite statements.

## License

The MathArena source versions are distributed under CC BY-NC-SA 4.0. This Korean adaptation retains those terms and attributes the original problems to MAA and source transcription to MathArena. Original problem rights remain with their respective owners.
