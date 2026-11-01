---
pretty_name: Korean Web Corpus (Morphologically Analyzed, Kiwi-based)
language:
- ko
license: cc-by-4.0
task_categories:
- token-classification
- text-generation
multilinguality: monolingual
size_categories:
- 1M<n<10M
source_datasets:
- AIHub Korean Web Corpus
homepage: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=624
dataset_summary: Morphologically analyzed Korean web corpus derived from AIHub using word identifier; stored as user-prepared Arrow shards with Parquet indexing on the Hub.
---

## Dataset Description

This dataset contains the AIHub Korean Web Corpus cleaned and morphologically annotated with the word identifier.  
Each record stores morpheme-level tokens and two subsets: **semantic** and **stylistic**.  

---

## Dataset Structure

### Data Fields
| Field           | Type         | Description                                                     |
|-----------------|--------------|-----------------------------------------------------------------|
| `text`          | `string`     | Original sentence reconstructed from morphemes                  |
| `semantic`      | `list[dict]` | Subset of content-bearing morphemes                             |
| `stylistic`     | `list[dict]` | Subset of grammatical/stylistic morphemes                       |

#### Example
```json
{
  "text": "정부가 LTE 서비스 도입 등...",
  "semantic": [
    {"form": "정부", "tag": "NNG"},
    {"form": "LTE", "tag": "SL"},
    {"form": "도입", "tag": "NNG"},
    {"form": "추진", "tag": "NNG"}
  ],
  "stylistic": [
    {"form": "가", "tag": "JKS"},
    {"form": "을", "tag": "JKO"},
    {"form": "한다", "tag": "VX+EF"}
  ],
}
```

### Tag Sets

- **Semantic (examples)**:  
  `NNG, NNP, NNB, NR, NP, VV, VA, VX, VCP, VCN, XR, MM, MAG, MAJ, SN, SL, XPN`, and `USER*`

- **Stylistic (examples)**:  
  `JKS, JKC, JKG, JKO, JKB, JKV, JKQ, JX, JC, EP, EF, EC, ETN, ETM, IC, XSN, XSV, XSA, XSM`

- **Dropped (examples)**:  
  `SF, SP, SS, SSO, SSC, SE, SO, SW`, plus `W_URL, W_EMAIL, W_HASHTAG, W_MENTION, W_SERIAL, W_EMOJI`

---

### Data Splits

- **Split**: `train`  
- **Composition**: Consists of user-prepared Apache Arrow shards (e.g., `data-00000-of-XXXXX.arrow`),  
  with additional Parquet indexing and cache structures automatically managed by 🤗 Datasets after upload.

---

### Source Data

- **Original dataset**: AIHub Korean Web Corpus (2021)  
- **Tokenizer / POS tagger**: Kiwi (Kiwipiepy, CoNg model)

---

### Preprocessing

- The original AIHub corpus was cleaned by removing HTML tags, URLs, emails, mentions, and hashtags,  
  normalizing punctuation and spacing, and filtering out overly short or long samples.  
- Each document was morphologically analyzed using **Kiwi (CoNg)**, producing morpheme-level annotations  
  separated into **semantic** (content-bearing) and **stylistic** (grammatical) subsets.  
- The processed data was saved as **Apache Arrow shards** for upload to the Hub.

---

### Usage
```python
from datasets import load_dataset

# Replace with your repo id, e.g., "Geonwoohong/ko-web-kiwi-morph"
ds = load_dataset("YOUR_USERNAME/YOUR_REPO", split="train")

print(ds[0]["text"])
print(ds[0]["semantic"][:5])
print(ds[0]["stylistic"][:5])
```

---

## Data Files

- Stored as **user-prepared Apache Arrow shards** on the Hub.  
- 🤗 Datasets automatically manages **Parquet-based indexing and caching structures** for efficient streaming and loading.  
- You don’t need to reference individual files — simply load the dataset using its repository ID as shown in *Usage*.

---

## Limitations

- Possible **domain bias** from the source AIHub web corpus.  
- **Morphological tagging** quality depends on the Kiwi (CoNg) analyzer and may vary by domain or sentence style.  
- Token-level boundaries can occasionally differ from other Korean analyzers (e.g., MeCab, Khaiii),  
  so users should ensure consistency when combining datasets.

---

## Citation

> AIHub. *Korean Web Corpus.*  
> Available at: <https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=624>

> Kiwi. *Korean Intelligent Word Identifier.*  
> Available at: <https://github.com/bab2min/Kiwi>