---
license: cc-by-nc-sa-4.0
language:
- ko
size_categories:
- n<1K
task_categories:
- text-generation
pretty_name: Korean AIME 2024
configs:
- config_name: default
  data_files:
  - split: test
    path: test.jsonl
---

# KoAIME24

30 Korean-language AIME 2024 problems for mathematical reasoning evaluation, with integer gold answers.

```python
from datasets import load_dataset

data = load_dataset("bzantium/koaime24", split="test")
```

Fields: `id`, `problem` (Korean statement with LaTeX), and `expected_answer` (string). The legacy `solution` field repeats the final answer; it is not a worked solution.

IDs `koaime24-0`–`koaime24-29` preserve the legacy order: AIME I then II, each with problem numbers 1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9. `source.jsonl` records the exact mapping.

## Sources and review

Preserves the existing 30-row Korean AIME24 dataset with nine reviewed corrections: I #5, #6, #8, #10, #11; II #3, #5, #8, #14. Existing IDs, ordering, expected answers, and the legacy solution field are unchanged.

Source: [MathArena AIME 2024](https://huggingface.co/datasets/MathArena/aime_2024_I); original contest: Mathematical Association of America. [AIME I](https://live.poshenloh.com/past-contests/aime/2024I) and [AIME II](https://live.poshenloh.com/past-contests/aime/2024II) provide MAA-authorized reference statements. See `source.jsonl` for English comparison statements and `provenance.json` for pinned revisions and the Korean data checksum.

Translation and review were performed in separate AI-assisted passes. All 30 answers and the source mapping were checked. This is not an official MAA translation or an independent bilingual human review. Model evaluation scores are not used to select or rewrite statements.

## License

The MathArena source versions are distributed under CC BY-NC-SA 4.0. This Korean adaptation retains those terms and attributes the original problems to MAA and source transcription to MathArena. Original problem rights remain with their respective owners.
