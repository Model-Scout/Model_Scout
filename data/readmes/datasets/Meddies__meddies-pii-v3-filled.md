---
license: cc-by-nc-4.0
language:
- vi
- en
- ko
- ms
- de
- es
- zh
- id
- jv
- su
- ru
- th
- fil
- ta
- ja
- pt
- my
- km
- lo
- fr
task_categories:
- token-classification
tags:
- pii
- de-identification
- healthcare
- synthetic
- ner
- multilingual
pretty_name: Meddies PII v3 (filled)
size_categories:
- 100K<n<1M
configs:
- config_name: vi
  data_files:
  - split: train
    path: data/vi/train.jsonl.gz
  - split: test
    path: data/vi/test.jsonl.gz
- config_name: en
  data_files:
  - split: train
    path: data/en/train.jsonl.gz
  - split: test
    path: data/en/test.jsonl.gz
- config_name: ko
  data_files:
  - split: train
    path: data/ko/train.jsonl.gz
  - split: test
    path: data/ko/test.jsonl.gz
- config_name: ms
  data_files:
  - split: train
    path: data/ms/train.jsonl.gz
  - split: test
    path: data/ms/test.jsonl.gz
- config_name: de
  data_files:
  - split: train
    path: data/de/train.jsonl.gz
  - split: test
    path: data/de/test.jsonl.gz
- config_name: es
  data_files:
  - split: train
    path: data/es/train.jsonl.gz
  - split: test
    path: data/es/test.jsonl.gz
- config_name: zh
  data_files:
  - split: train
    path: data/zh/train.jsonl.gz
  - split: test
    path: data/zh/test.jsonl.gz
- config_name: id
  data_files:
  - split: train
    path: data/id/train.jsonl.gz
  - split: test
    path: data/id/test.jsonl.gz
- config_name: jv
  data_files:
  - split: train
    path: data/jv/train.jsonl.gz
  - split: test
    path: data/jv/test.jsonl.gz
- config_name: su
  data_files:
  - split: train
    path: data/su/train.jsonl.gz
  - split: test
    path: data/su/test.jsonl.gz
- config_name: ru
  data_files:
  - split: train
    path: data/ru/train.jsonl.gz
  - split: test
    path: data/ru/test.jsonl.gz
- config_name: th
  data_files:
  - split: train
    path: data/th/train.jsonl.gz
  - split: test
    path: data/th/test.jsonl.gz
- config_name: fil
  data_files:
  - split: train
    path: data/fil/train.jsonl.gz
  - split: test
    path: data/fil/test.jsonl.gz
- config_name: ta
  data_files:
  - split: train
    path: data/ta/train.jsonl.gz
  - split: test
    path: data/ta/test.jsonl.gz
- config_name: ja
  data_files:
  - split: train
    path: data/ja/train.jsonl.gz
  - split: test
    path: data/ja/test.jsonl.gz
- config_name: pt
  data_files:
  - split: train
    path: data/pt/train.jsonl.gz
  - split: test
    path: data/pt/test.jsonl.gz
- config_name: my
  data_files:
  - split: train
    path: data/my/train.jsonl.gz
  - split: test
    path: data/my/test.jsonl.gz
- config_name: km
  data_files:
  - split: train
    path: data/km/train.jsonl.gz
  - split: test
    path: data/km/test.jsonl.gz
- config_name: lo
  data_files:
  - split: train
    path: data/lo/train.jsonl.gz
  - split: test
    path: data/lo/test.jsonl.gz
- config_name: fr
  data_files:
  - split: train
    path: data/fr/train.jsonl.gz
  - split: test
    path: data/fr/test.jsonl.gz
---

# Meddies PII v3 — filled documents

Synthetic, span-labelled documents for training and evaluating PII detection in healthcare and everyday text, in
20 languages. Each document is a skeleton of
[`Meddies/meddies-pii-v3-skeleton`](https://huggingface.co/datasets/Meddies/meddies-pii-v3-skeleton) (revision
`7580222186034cfbd02e8904d310341c0a828b7a`) whose `⟦slot⟧`s were filled with synthetic values; every value's character span is recorded while the
text is built. **All people, numbers and contact details are synthetic.**

Values come from [meddies-faker](https://hdt-0103.github.io/meddies-faker-site/), one country pack per language: people
drawn from published statistics (age, sex, region, ethnicity, names), identifiers with their official structure and
check digits, addresses, organisations and dates that agree within a document, written in the language's own
script, formats and spoken forms. Javanese and Sundanese use the Indonesian pack with its Javanese and Sundanese
populations. Slots meddies-faker does not cover (amounts, drug names, vital signs and a few others) are filled by the
pipeline's own providers.

## Languages

| Config | Language | Country | Train | Test | Spans | Distinct names |
|---|---|---|---|---|---|---|
| `vi` | Vietnamese | Viet Nam | 20,216 | 5,170 | 304,734 | 73% |
| `en` | English | United States | 20,926 | 5,258 | 326,244 | 98% |
| `ko` | Korean | South Korea | 15,268 | 3,846 | 252,132 | 85% |
| `ms` | Malay | Malaysia | 20,106 | 5,012 | 312,534 | 98% |
| `de` | German | Germany | 17,042 | 4,314 | 261,064 | 99% |
| `es` | Spanish | Spain | 18,230 | 4,658 | 280,490 | 97% |
| `zh` | Chinese | China | 15,834 | 4,018 | 260,590 | 80% |
| `id` | Indonesian | Indonesia | 18,124 | 4,526 | 275,436 | 86% |
| `jv` | Javanese | Indonesia (Javanese) | 17,202 | 4,280 | 270,042 | 85% |
| `su` | Sundanese | Indonesia (Sundanese) | 17,338 | 4,356 | 277,606 | 84% |
| `ru` | Russian | Russia | 13,214 | 3,328 | 209,670 | 96% |
| `th` | Thai | Thailand | 14,858 | 3,782 | 237,004 | 100% |
| `fil` | Filipino | Philippines | 19,966 | 4,864 | 325,996 | 100% |
| `ta` | Tamil | India (Tamil Nadu) | 13,426 | 3,346 | 212,416 | 90% |
| `ja` | Japanese | Japan | 15,402 | 3,788 | 243,228 | 99% |
| `pt` | Portuguese | Brazil | 17,782 | 4,364 | 266,342 | 96% |
| `my` | Burmese | Myanmar | 12,210 | 3,132 | 201,082 | 88% |
| `km` | Khmer | Cambodia | 13,304 | 3,324 | 226,744 | 86% |
| `lo` | Lao | Laos | 12,280 | 3,080 | 204,436 | 86% |
| `fr` | French | France | 17,078 | 4,240 | 256,356 | 99% |

*Distinct names*: share of distinct names among the people of the config (one name per person per document: their
first mention). Names follow real frequencies, so common names repeat where they are common in reality.

```python
from datasets import load_dataset
ds = load_dataset("Meddies/meddies-pii-v3-filled", "vi")  # any config above
```

## Record

```json
{
  "id": "sg-...-s42-f0", "lang": "vi",
  "text": "Họ tên bệnh nhân: Nguyễn Văn An ...",
  "spans": [{"start": 18, "end": 31, "text": "Nguyễn Văn An", "entity_type": "human_name", "entity_subtype": "patient",
             "label": "NAME", "group": "DIRECT_PII", "polarity": "positive", "mask_action": "MASK",
             "persona_id": "p1"}]
}
```

- `text[start:end] == span.text` for every span; spans are sorted and never overlap.
- `polarity`: `positive` = PII of a person in the document (mask it); `op` = operational value (bed, queue, order
  number); `trap` = shaped like an ID but not one; `neg` = public entity. Non-positive spans have `mask_action: KEEP`.
- `persona_id`: the same person within one document (`p1`, `p2` …).
- Each skeleton is filled twice with different values (`id` ends in `-f0` / `-f1`). Train and test are split by
  source skeleton, so no skeleton's wording appears in both.
- Relative dates (admission, follow-up, expiry …) were drawn around the generation date, 2026-10-30 (vi, en, ko, ms, de, es, zh, id, jv, su) and 2026-10-31 (ru, th, fil, ta, ja, pt, my, km, lo, fr).

## How it was made

`fill-v3 --lang <lang> --fills 2 --seed 42 --revision 7580222186034cfbd02e8904d310341c0a828b7a` of the Meddies PII v3 pipeline (generator in each
split's `stats.json`), generated on 2026-10-30 (vi, en, ko, ms, de, es, zh, id, jv, su) and 2026-10-31 (ru, th, fil, ta, ja, pt, my, km, lo, fr). Every language passed the pipeline's audit (offsets, shapes, leaks,
identity, duplicates) and has 0 value collisions between different people. `data/<lang>/report.json` holds the label
and format distributions, rejection reasons and audit results.

## Licence and attribution

Released under CC BY-NC 4.0, as the skeleton corpus it is built on. Generated values come from meddies-faker (code
Apache-2.0; pack data CC BY-SA 4.0 with the sources listed in each pack's `ATTRIBUTION.md`). The documents are
synthetic and must not be used to identify real people.
