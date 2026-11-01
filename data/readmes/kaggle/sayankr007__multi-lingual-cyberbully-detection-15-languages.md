# Multi-Lingual Semantic Cyberbully Detection

Designed For Few Shot Sampling & Advanced Cross-lingual Analysis  (15 Languages)

## 📄 Dataset Description:

This dataset is a curated multilingual collection designed to facilitate **few-shot learning research**, particularly in **hate speech detection** across a wide range of languages and classes. The data has been sourced from multiple publicly available hate speech and offensive language datasets and merged into a single unified format with consistent labels.

We provide:
- **Full Dataset**: Contains all available samples (279,127 rows).
- **Balanced Dataset**: Downsampled and upsampled version (around ~65,000 rows) to ensure more balanced class distribution for few-shot learning algorithms such as **MAML**, **ProtoNet**, and **RelationNet**.

---

## 📦 Format

The dataset is available in **CSV format** with the following columns:

- `text` — the content (text or comment) from social media or online platforms.
- `label` — the annotated class label (standardized with a `lang_type` format, e.g., `eng_race` or `hin_offense`).

---

## 🌐 Languages & Labels

Each language's dataset has been re-labeled in a way that preserves both **language identity** and **category type**. Below are the main categories for the three major languages:

---

### 🇬🇧 English Labels (from a cyberbullying detection dataset):

| Label        | Description                                 |
|--------------|---------------------------------------------|
| `eng_race`   | Texts with hate or bullying based on race or ethnicity |
| `eng_sex`    | Sexist, gender-biased, or sexually harassing content |
| `eng_religion` | Religion-based hate speech or derogatory content |
| `eng_neutral`  | Non-cyberbullying or neutral statements      |

---

### 🇮🇳 Hindi Labels (from a hostile post detection dataset):

| Label         | Description                                             |
|---------------|---------------------------------------------------------|
| `hin_hate`    | Posts containing hate speech                            |
| `hin_offense` | Offensive, vulgar or abusive language                   |
| `hin_defame`  | Attempts to defame an individual or group               |
| `hin_fake`    | Posts spreading misinformation or fake narratives       |
| `hin_neutral` | Non-hostile, regular content                            |

*Note: Original data contained multi-labels. Only one label per text was considered (row-level normalization).*

---

### 🇧🇩 Bengali Labels (from a troll and threat classification dataset):

| Label           | Description                                  |
|------------------|----------------------------------------------|
| `ben_political`  | Politically motivated hate or offensive content |
| `ben_sexual`     | Sexually explicit or abusive language          |
| `ben_troll`      | Trolling or deliberately provocative comments |
| `ben_threat`     | Threats of violence or harm                   |
| `ben_neutral`    | Non-toxic or safe content                     |

---

## 🗣 Other Languages

Other languages included in the dataset are:
- Arabic (`ara_*`)
- German (`ger_*`)
- Russian (`rus_*`)
- French (`fre_*`)
- Italian (`ita_*`)
- Spanish (`spa_*`)
- Korean (`kor_*`)
- Turkish (`tur_*`)
- Chinese (`chi_*`)
- Portuguese (`por_*`)
- Indonesian (`ind_*`)
- Roman Hindi/Urdu (`rom_*`)

Each has two standard labels:
- `&lt;lang&gt;_bully`: contains hate/offensive speech
- `&lt;lang&gt;_nonbully`: safe or neutral text

---

## 🔬 Ideal Use Cases

- Few-shot learning & meta-learning (e.g., MAML, Prototypical Networks)
- Cross-lingual hate speech detection
- Class imbalance & data augmentation research
- Benchmarking for multilingual NLP tasks

---

## 📁 Files Included

- `fewshot_dataset.csv` – Full version (~279k samples)
- `fewshot_balanced_dataset.csv` – Balanced version (~35k samples)

---

## 📚 License

You may redistribute, adapt, and build upon the data **for non-commercial research purposes**. If you use this dataset in your research or publication, please cite appropriately (refer to credits/acknowledgments in original sources if reused).

---

## 🙏 Acknowledgments

This dataset is built upon publicly available resources from multiple Kaggle datasets, including multilingual hate speech datasets and language-specific toxic comment datasets. Label mappings and language unification were performed for the purpose of standardized few-shot NLP tasks.

출처: Kaggle (sayankr007/multi-lingual-cyberbully-detection-15-languages)
태그: intermediate, nlp, text classification, cyber security, multilingual and cross-lingual capabilities
라이선스: MIT
수정일: 2025-06-03T00:12:48.587Z
