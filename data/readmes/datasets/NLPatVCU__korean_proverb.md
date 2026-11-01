---
language:
  - ko
  - en
license: other
license_name: cc-by-sa-2.0-kr
license_link: https://creativecommons.org/licenses/by-sa/2.0/kr/
homepage: https://github.com/taylorsm9/korean_proverbs
pretty_name: Korean proverbs → English (Urimalsaem)
tags:
  - korean
  - proverbs
  - urimalsaem
  - machine-translation
  - 속담
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/korean_proverbs_en.parquet
annotations_creators:
  - machine-generated
source_datasets:
  - original
task_categories:
  - translation
---

# Korean proverbs → English

Every proverb (속담) entry in the Urimalsaem dictionary (우리말샘, National Institute of Korean Language), machine-translated to English. Code and pipeline details: <https://github.com/taylorsm9/korean_proverbs>.

The thinking-on translations come with the model's full reasoning traces, one per row. To our knowledge, as of October 2026, this is the largest public set of reasoning traces for idioms or proverbs, about six times the size of the next largest ([Chengyu-Bench](https://aclanthology.org/2025.emnlp-main.119/), which released 1,834 DeepSeek-R1 traces), and the only one for translation.

## Structure of this dataset (read this first)

Urimalsaem is a sense-level dictionary: a single proverb can have more than one recorded meaning, and each meaning is a separate entry. This dataset follows that structure.

- **One row per dictionary sense.** 10,763 rows total.
- **9,612 unique proverbs.** 1,094 proverbs have two or more senses; the other 8,518 have one.
- When a proverb has multiple senses, the same `ko` string appears on multiple rows, each with its own `definition_ko` and its own English translations. All senses of a given proverb share the same `headword_raw`.
- `sense_no` is Urimalsaem's own ordering within a headword (`"001"`, `"002"`, …). This dataset does not pick a primary sense for you.

**If you want one row per proverb**, you need to pick a sense yourself. The simplest options:

```python
# Keep the lowest-numbered sense per proverb (Urimalsaem's own order):
one_per = df.sort_values(["headword_raw", "sense_no"]).drop_duplicates("headword_raw", keep="first")
```

## Scale

| Measure | Value |
|---|---|
| Total rows | 10,763 |
| Unique proverbs (unique `headword_raw`) | 9,612 |
| Proverbs with multiple senses | 1,094 |

## Load it

```python
from datasets import load_dataset
ds = load_dataset("NLPatVCU/korean_proverb", split="train")
df = ds.to_pandas()
```

Or load the parquet directly:

```python
import pandas as pd
from huggingface_hub import hf_hub_download
path = hf_hub_download("NLPatVCU/korean_proverb", "data/korean_proverbs_en.parquet", repo_type="dataset")
df = pd.read_parquet(path)
```

## Columns

| Column | Description |
|---|---|
| `id` | Urimalsaem `target_code` for this sense |
| `headword_raw` | Raw headword text, including Urimalsaem's `[A/B]` / `(C)` variant notation |
| `ko` | Canonical form of the proverb (variant notation stripped) |
| `sense_no` | Sense number within this proverb, as assigned by Urimalsaem (`"001"`, `"002"`, …) |
| `type` | Urimalsaem's usage-category label for this sense (`일반어` is the standard-usage code; see Urimalsaem for the other codes) |
| `definition_ko` | Dictionary definition (synonym tag and following synonym list are stripped out) |
| `synonyms_ko` | The stripped synonym list: proverb-length strings that are their own dictionary entries |
| `proverb_en_nonthinking` | English translation of the proverb, thinking off |
| `definition_en_nonthinking` | English translation of the definition, thinking off |
| `proverb_en_thinking` | English translation of the proverb, thinking on |
| `definition_en_thinking` | English translation of the definition, thinking on |
| `reasoning` | The model's reasoning for the thinking-on translations |

## Companion embeddings

Vector embeddings of the Korean and English texts, computed with two models, are shipped as separate parquet files:

```
embeddings/
  kanana.parquet         # 1,792-dim
  qwen3.parquet          # 4,096-dim
```

Each row carries `id` plus six `list[float32]` columns: `ko_embedding`, `definition_ko_embedding`, `proverb_en_nonthinking_embedding`, `definition_en_nonthinking_embedding`, `proverb_en_thinking_embedding`, `definition_en_thinking_embedding`. Join on `id`:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

df  = pd.read_parquet(hf_hub_download("NLPatVCU/korean_proverb", "data/korean_proverbs_en.parquet", repo_type="dataset"))
emb = pd.read_parquet(hf_hub_download("NLPatVCU/korean_proverb", "embeddings/kanana.parquet",       repo_type="dataset"))
joined = df.merge(emb, on="id")
```

Both the proverb side and the definition side are embedded with the same prompt, so they share one space (useful for cosine similarity between a proverb and its own meaning). For Qwen3-Embedding the prompt is:

```
Instruct: Given a Korean or English text, retrieve texts with the same meaning
Query:
```

## Source

- 우리말샘 (Urimalsaem), National Institute of Korean Language (국립국어원).
- Dump dated 2026-06-02, via the GitHub mirror [`spellcheck-ko/korean-dict-nikl`](https://github.com/spellcheck-ko/korean-dict-nikl), pinned to commit `42c0d01`, folder `opendict/` only.

## License

- The **dataset** (Korean proverbs, Korean definitions, English translations, reasoning): **CC-BY-SA-2.0-KR**, matching Urimalsaem. See <https://creativecommons.org/licenses/by-sa/2.0/kr/>. Attribution: 국립국어원 (NIKL), 우리말샘.
- `embeddings/kanana.parquet`: **CC-BY-NC-4.0** (non-commercial only), inherited from `kakaocorp/kanana-nano-2.1b-embedding`.
- `embeddings/qwen3.parquet`: **Apache-2.0**, inherited from `Qwen/Qwen3-Embedding-8B`.

## Translation setup

- Model: `nvidia/Qwen3.5-122B-A10B-NVFP4` served by vLLM 0.28.0 on NVIDIA DGX Spark.
- Every row was translated twice with the same prompt: once with thinking off (`*_nonthinking` columns) and once with thinking on (`*_thinking` columns).
- Sampling with thinking off (`enable_thinking: false`): `temperature=0.7, top_p=0.8, top_k=20, min_p=0, presence_penalty=0, repetition_penalty=1.0, max_tokens=1024`.
- Sampling with thinking on (`enable_thinking: true`): `temperature=1.0, top_p=0.95, top_k=20, min_p=0, presence_penalty=1.5, repetition_penalty=1.0, max_tokens=20480, thinking_token_budget=16384`.
- Seed per row: `int(id)`.
- Output constrained to a Pydantic JSON schema via `response_format`.
- No thinking-off translation hit the `max_tokens=1024` ceiling. The longest completion seen was 156 tokens.
- No thinking-on request hit the thinking budget. The longest reasoning trace was 11,488 tokens.

## Limitations

- Machine-translated; no human review.
- Multiple rows share the same `ko` when a proverb has multiple senses. Dedupe on `headword_raw` if you want unique proverb strings (see "Structure" above).
- Only the canonical form of each proverb is translated; variant notation in `headword_raw` is not expanded.

## Citation

If you use this dataset, please cite the source dictionary:

> 국립국어원 (National Institute of Korean Language). 우리말샘 (Urimalsaem).
> Available via [`spellcheck-ko/korean-dict-nikl`](https://github.com/spellcheck-ko/korean-dict-nikl).
