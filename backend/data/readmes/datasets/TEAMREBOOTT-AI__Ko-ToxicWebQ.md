---
license: cc-by-nc-sa-4.0
language:
- ko
size_categories:
- 10K<n<100K
pretty_name: 'Ko-ToxicWebQ: Korean Toxic Web Query Dataset'
dataset_info:
  features:
  - name: query
    dtype: string
  - name: sub_category
    dtype: string
  - name: manipulation
    dtype: int64
  - name: abbreviation
    dtype: int64
  - name: w/o_transformation
    dtype: int64
  splits:
  - name: train
    num_bytes: 2305606
    num_examples: 38175
  - name: test
    num_bytes: 575772
    num_examples: 9539
  download_size: 1067434
  dataset_size: 2881378
extra_gated_heading: ⚠️ Restricted Access Dataset
extra_gated_description: This dataset contains toxic and sensitive real-world web
  queries, including sexually explicit and legally restricted content. Automatic access
  approval is enabled.
extra_gated_prompt: By requesting access, you agree to use this dataset solely for
  research and to handle sensitive content responsibly.
extra_gated_button_content: Agree and Request Access
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# Ko-ToxicWebQ: Korean Toxic Web Query Dataset

**Ko-ToxicWebQ** is a dataset consisting of 47,714 real-world Korean web search queries annotated for harmfulness and obfuscation strategies. The queries are extracted from Microsoft Bing search logs and labeled according to culturally specific toxicity categories and linguistic evasion tactics. The dataset is designed for evaluating moderation systems and training language models to handle adversarial or sensitive inputs in Korean.

> ⚠️ **Warning**: This dataset includes explicit, potentially offensive, and legally sensitive content. Researchers must take necessary precautions when using or sharing model outputs trained on this dataset.

## Ethics Statement

We recognize that providing real examples of this content may be uncomfortable or distressing. These samples, however, are critical for developing robust detection systems that can mitigate harm and prevent the circulation of illicit content. We urge researchers to handle this dataset responsibly, with appropriate safeguards for user well-being.

Since conceptions of toxic or illegal content vary widely across jurisdictions, we emphasize that our annotations are grounded in South Korean laws and societal norms. We neither endorse nor condone the content found in these queries; our sole aim is to enable the development of more effective toxicity detection methods.

---

## 💡 Dataset Highlights

- **Language**: Korean (`ko`)
- **Size**: 47,714 queries
- **Labels**:
  - `sub_category`: One of 7 toxicity categories
  - `manipulation`, `abbreviation`, `w/o_transformation`: Binary flags for obfuscation strategies

---

## 🗂 Features

| Name               | Type     | Description                                                   |
|--------------------|----------|---------------------------------------------------------------|
| `query`            | `string` | Raw web search query in Korean                               |
| `sub_category`     | `string` | One of {clean, gambling, sexuality, social, copyright, prostitution, others} |
| `manipulation`     | `int`    | 1 if query contains character-level manipulation, else 0     |
| `abbreviation`     | `int`    | 1 if query uses abbreviation (e.g., ㅇㄷ → 야동), else 0        |
| `w/o_transformation` | `int`  | 1 if query is plain without evasion, else 0                   |

---

## 🔎 Category Description

Toxicity categories follow Korean regulatory standards (e.g., KCSC):

| Category     | Description |
|--------------|-------------|
| `clean`      | Non-toxic query |
| `gambling`   | Illegal betting or casino platforms |
| `sexuality`  | Explicit adult content, erotic material |
| `social`     | Sexual exploitation or adult streams on platforms |
| `copyright`  | Torrenting, illegal streaming or software cracking |
| `prostitution` | Online sex solicitation or red-light area keywords |
| `others`     | Hacking, self-harm, drug-related, or uncategorized |

---

## 🔐 Gated Access (Automatic Approval)

This dataset is gated on Hugging Face due to the presence of harmful and sensitive content. However, **automatic approval is enabled**, and users only need to click to request access.

By accessing the dataset, you agree to:
- Use it solely for research or academic purposes
- Avoid public dissemination of raw toxic queries
- Apply safety filters if used in generation/inference tasks

---

## 📦 Usage Example

```python
from datasets import load_dataset

dataset = load_dataset("TEAMREBOOTT-AI/Ko-ToxicWebQ", token="hf_your_token")
print(dataset["train"][0])
```

## Term of Use

This dataset is partially based on the MS MARCO Web Search data and is provided strictly for non-commercial research purposes only. It is made available free of charge to promote research in artificial intelligence and related fields. You may only use this dataset if you agree to and comply with all of the following conditions:

Conditions of Use:
* This dataset must be used for non-commercial purposes only and may not be used, either directly or indirectly, in any commercial product or service.

* The datasets are provided "as is" without warranty and usage of the data has risks since we may not own the underlying rights in the documents. We are not be liable for any damages related to use of the dataset. 