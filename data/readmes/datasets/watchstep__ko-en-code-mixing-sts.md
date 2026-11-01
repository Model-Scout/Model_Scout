---
pretty_name: Korean–English Code-Mixing STS Dataset
task_categories:
  - sentence-similarity
language:
  - ko
  - en
tags:
  - code-mixing
  - sentence-similarity
source_datasets:
  - mteb/KLUE-STS

license: cc-by-sa-4.0
---

# Korean–English Code-Mixing STS Dataset

This dataset contains 1,500 Korean–English code-mixed pairs derived from KLUE-STS. We keep the original `sentence_a` and apply insertion-only code-mixing to `sentence_b` using an LLM (Gemini 2.5 Flash), recording where and how code-mixing occurred.

## Interactive Dashboard

🌐 **Explore the dataset interactively**: [https://watchstep.github.io/ko-en-cm/](https://watchstep.github.io/ko-en-cm/)

The dashboard provides:
- Interactive data exploration and filtering
- Sample visualization with code-mixing highlights
- Statistics and distribution analysis
- Quality metrics and evaluation insights

## Files
- `data/ko-en-cm-sts.jsonl`
- `data/ko-en-cm-sts.csv`

## Data fields

- `id`: A unique identifier for each sample (e.g., `pair_00000`).
- `sentence_a`: The first sentence in Korean.
- `sentence_b`: The second sentence, with Korean–English code-mixing applied.
- `sentence_b_org`: The original second sentence in Korean, before code-mixing.
- `sentence_mixed_from`: Indicates which sentence (`a` or `b`) was modified. It is always `b` in this dataset.
- `mixed_list`: A list of dictionaries containing information about the mixed words:
    - `from`: The original Korean word.
    - `to`: The translated English word.
    - `pos`: The part-of-speech tag of the original word.
- `mixed_k`: The number of code-mixed words in the sentence (ranges from 1 to 4).
- `min_k`, `max_k`: The min/max number of words to be mixed per sentence during generation (1 to 5).
- `source`: The source of the original data (`KLUE-STS`).
- `score_org`: The original semantic similarity score from KLUE-STS, ranging from 0.0 to 5.0.

## Data Sample

```json
{
  "id": "pair_00002",
  "sentence_a": "아쉬웠던 점은 우선 역에서는 조금 멀기 때문에 버스를 타야한다.",
  "sentence_b": "슬픈 것은 station에서 조금 멀기 때문에 bus를 타야 한다는 것입니다.",
  "sentence_b_org": "슬픈 것은 역에서 조금 멀기 때문에 버스를 타야 한다는 것입니다.",
  "sentence_mixed_from": "b",
  "mixed_list": [{"from": "역", "to": "station", "pos": "NNG"}, {"from": "버스", "to": "bus", "pos": "NNG"}],
  "mixed_k": 2,
  "min_k": 1,
  "max_k": 5,
  "source": "KLUE-STS",
  "score_org": 3.6
}
```

## License
This dataset is derived from **mteb/KLUE-STS** (CC BY-SA 4.0).
Original data © their respective authors.
We performed automatic **Korean–English code-mixing** transformations and added fields (e.g., `sentence_b`, `mixed_list`, `score_org`, etc.).
This dataset is released under **CC BY-SA 4.0**, in compliance with the Share-Alike requirement.

## Attribution
- Source dataset: [mteb/KLUE-STS](https://huggingface.co/datasets/mteb/KLUE-STS) (CC BY-SA 4.0)
- Paper(s): KLUE (Park et al., 2021), MTEB (Muennighoff et al., 2022/2025)
