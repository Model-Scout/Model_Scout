---
license: cc-by-nc-4.0
task_categories:
  - text-generation
language:
  - zh
  - en
  - ja
  - de
  - es
  - fr
  - pt
  - th
  - vi
  - ru
  - id
  - ar
  - tr
  - uk
  - ko
  - it
tags:
  - role-playing
  - character-simulation
  - novel
  - multilingual
  - sft
  - chat
  - quality-scored
  - llm-filtered
  - llm-labeled
  - nsfw-filtered
pretty_name: Novel-RP Multilingual Role-Playing Dataset
size_categories:
  - 10K<n<100K
configs:
  - config_name: train
    data_files:
      - split: train
        path: train/sft_sharegpt_all.jsonl
  - config_name: labeled_filtered
    data_files:
      - split: train
        path: labeled/filtered/messages_merged.jsonl
  - config_name: labeled_raw
    data_files:
      - split: train
        path: labeled/raw/*.jsonl
  - config_name: test_raw
    data_files:
      - split: test
        path: test/raw/test_set.jsonl
  - config_name: test_sft_preview
    data_files:
      - split: test
        path: test/sft_preview/sft_sample.jsonl
---

# Novel-RP: Multilingual Novel Role-Playing Dataset

A multilingual novel-based role-playing dataset for training and evaluating LLMs on character persona simulation.

## 📖 Overview

**Novel-RP** is a multilingual role-playing dataset built from web novels and role-playing conversations, specifically designed for training large language models on character role-playing tasks. 

This dataset contains two main subsets:
1. **train**: Novel-based role-playing data (ShareGPT format) - from CoSER pipeline
2. **labeled**: LLM-labeled role-playing conversations with quality & safety annotations

## ⚖️ License

**CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)**

- ✅ Allowed: Research, learning, personal use, derivative works
- ❌ Prohibited: Commercial use
- 📝 Required: Attribution

---

## 📊 Dataset 1: Novel-Based Training Data (`train`)

### Statistics

| Language | # of Novels | # of Samples | Language Name |
|----------|-------------|--------------|---------------|
| 🇩🇪 de | 90 | 721 | German |
| 🇬🇧 en | 76 | 1,308 | English |
| 🇪🇸 es | 81 | 1,460 | Spanish |
| 🇫🇷 fr | 94 | 548 | French |
| 🇯🇵 ja | 91 | 1,019 | Japanese |
| 🇧🇷 pt | 81 | 491 | Portuguese |
| 🇷🇺 ru | 92 | 255 | Russian |
| 🇹🇭 th | 90 | 475 | Thai |
| 🇻🇳 vi | 77 | 1,987 | Vietnamese |
| 🇨🇳 zh | 78 | 1,796 | Chinese |
| **Total** | **850** | **10,060** | **10 Languages** |

- **Training Samples**: 10,060 (ShareGPT format, LLM quality-scored ≥80/100)
- **Test Samples**: 200 (100 ID + 100 OOD)

### Data Format (ShareGPT)

```json
{
  "conversations": [
    {"from": "system", "value": "You are Xia Yu from \"Rebirth of the Strongest Tycoon\"..."},
    {"from": "human", "value": "===Conversation Start===\n\n..."},
    {"from": "assistant", "value": "*Xia Yu's eyes flicker* \"...\""}
  ]
}
```

### Quality Scoring System

Each conversation sample is evaluated by LLM across four dimensions (0-25 points each, total 100):
- **Dialogue Quality**: Natural flow, coherence, and proper action/speech format
- **Character Consistency**: Alignment with profile, personality reflection, no OOC moments
- **Setting Alignment**: Correct use of world-building elements, terminology, and lore
- **Training Value**: Learnable patterns, format quality, character depth

Only samples scoring ≥80/100 are included.

---

## 📊 Dataset 2: LLM-Labeled Conversations (`labeled`)

This dataset has two versions:
- **`labeled_raw`**: All 44,545 samples with labels (unfiltered)
- **`labeled_filtered`**: 14,527 high-quality samples (filtered)

### Statistics

| Metric | Raw | Filtered |
|--------|-----|----------|
| **Total Samples** | 44,545 | 14,527 |
| **Format** | Messages + Labels | Messages + Labels |
| **Quality Filter** | None | Score ≥ 4/5 |
| **Safety Filter** | None | Minor NSFW risk < high |

### Language Distribution

| Language | Samples | Percentage |
|----------|---------|------------|
| 🇪🇸 Spanish (es) | 5,868 | 40.4% |
| 🇬🇧 English (en) | 5,144 | 35.4% |
| 🇧🇷 Portuguese (pt) | 1,728 | 11.9% |
| 🇷🇺 Russian (ru) | 1,208 | 8.3% |
| 🇮🇩 Indonesian (id) | 175 | 1.2% |
| 🇹🇭 Thai (th) | 159 | 1.1% |
| 🇫🇷 French (fr) | 130 | 0.9% |
| Others | 115 | 0.8% |

### NSFW Level Distribution

| Level | Samples | Percentage |
|-------|---------|------------|
| SFW | 5,381 | 37.0% |
| Suggestive | 5,444 | 37.5% |
| NSFW | 2,541 | 17.5% |
| Explicit | 1,161 | 8.0% |

### Safety & Quality Filtering

This subset has been carefully filtered:
1. **Quality Score ≥ 4/5**: Only high-quality conversations
2. **Minor NSFW Risk < High**: Removed content with high/critical risk
3. **Recommendation ≠ Remove**: Excluded content flagged for removal

### Data Format (Messages + Labels)

```json
{
  "messages": [
    {"role": "system", "content": "Character description and scenario..."},
    {"role": "assistant", "content": "*Action* \"Dialogue\""},
    {"role": "user", "content": "User response..."}
  ],
  "labels": {
    "nsfw_level": "sfw|suggestive|nsfw|explicit",
    "minor_nsfw_detected": false,
    "minor_nsfw_risk": "none|low|medium",
    "primary_language": "en",
    "fluency_score": 4,
    "grammar_score": 4,
    "repetition_score": 4,
    "overall_quality": 4,
    "recommendation": "keep|review",
    "token_count": 4000,
    "message_count": 20
  }
}
```

---

## 📁 Dataset Structure

```
novel-rp/
├── train/
│   └── sft_sharegpt_all.jsonl      # Novel-based training data (ShareGPT format)
├── labeled/
│   ├── raw/                         # Raw LLM-labeled data (all 44,545 samples)
│   │   ├── messages_part_001_labeled.jsonl
│   │   ├── messages_part_002_labeled.jsonl
│   │   ├── messages_part_003_labeled.jsonl
│   │   └── labeling_stats.json
│   └── filtered/
│       └── messages_merged.jsonl    # Filtered high-quality data (14,527 samples)
├── test/
│   ├── raw/
│   │   └── test_set.jsonl          # Raw test set data
│   ├── sft_preview/
│   │   └── sft_sample.jsonl        # SFT format sample preview
│   └── held_out_plots.json         # Held-out plot data
└── final/
    ├── de/                         # German novel data
    ├── en/                         # English novel data
    ├── es/                         # Spanish novel data
    ├── fr/                         # French novel data
    ├── ja/                         # Japanese novel data
    ├── pt/                         # Portuguese novel data
    ├── ru/                         # Russian novel data
    ├── th/                         # Thai novel data
    ├── vi/                         # Vietnamese novel data
    └── zh/                         # Chinese novel data
```

## 🎭 Dialogue Format

Both datasets use a role-playing format:
- `*Asterisks*` wrap actions, expressions, environmental descriptions, and inner thoughts
- `"Double quotes"` are used only for spoken dialogue

Example:
```
*He leans against the wall, arms crossed, a playful glint in his eyes.* "Do you really think I would believe that?" *The corner of his mouth curves up slightly, but the smile doesn't reach his eyes.*
```

## 🚀 Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load novel-based training data (ShareGPT format)
train_data = load_dataset("taozi555/novel-rp", "train", split="train")

# Load LLM-labeled conversations (filtered, 14,527 samples)
labeled_filtered = load_dataset("taozi555/novel-rp", "labeled_filtered", split="train")

# Load LLM-labeled conversations (raw, all 44,545 samples)
labeled_raw = load_dataset("taozi555/novel-rp", "labeled_raw", split="train")

# Load test sets
test_raw = load_dataset("taozi555/novel-rp", "test_raw", split="test")
test_sft = load_dataset("taozi555/novel-rp", "test_sft_preview", split="test")

# Load specific language raw data
zh_data = load_dataset("taozi555/novel-rp", data_dir="final/zh")
```

### Filtering Labeled Data

```python
# Use raw data for custom filtering
labeled_raw = load_dataset("taozi555/novel-rp", "labeled_raw", split="train")

# Filter by language
english_data = labeled_raw.filter(lambda x: x['labels']['primary_language'] == 'en')

# Filter by NSFW level
sfw_data = labeled_raw.filter(lambda x: x['labels']['nsfw_level'] == 'sfw')

# Filter by quality
high_quality = labeled_raw.filter(lambda x: x['labels']['overall_quality'] >= 4)

# Or just use pre-filtered data
labeled_filtered = load_dataset("taozi555/novel-rp", "labeled_filtered", split="train")
```

### Converting Labeled Data to ShareGPT

```python
def to_sharegpt(record):
    conversations = []
    for msg in record['messages']:
        role_map = {'system': 'system', 'user': 'human', 'assistant': 'gpt'}
        conversations.append({
            'from': role_map.get(msg['role'], msg['role']),
            'value': msg['content']
        })
    return {'conversations': conversations}

sharegpt_data = labeled_filtered.map(to_sharegpt)
```

### For SFT Training

Both datasets are compatible with:
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)
- Other training frameworks supporting ShareGPT/Messages format

## 📚 Data Sources

- **train subset**: Built from [taozi555/novel-multilingual](https://huggingface.co/datasets/taozi555/novel-multilingual) using the [CoSER](https://github.com/Neph0s/CoSER) pipeline
- **labeled subset**: Curated from role-playing conversations, labeled by Claude LLM

## ⚠️ Important Notes

1. **License Restriction**: CC BY-NC 4.0, **commercial use is prohibited**
2. **Content Warning**: Some content contains mature themes (suggestive/nsfw/explicit)
3. **Safety Filtered**: High-risk content has been removed from `labeled` subset
4. **Quality Assured**: 
   - `train`: Score ≥ 80/100 by LLM evaluation
   - `labeled`: Score ≥ 4/5 by LLM evaluation
5. **Use Labels**: Leverage the detailed labels in `labeled` subset for additional filtering

## 🙏 Acknowledgments

- [CoSER](https://github.com/Neph0s/CoSER) - Data construction methodology
- [taozi555/novel-multilingual](https://huggingface.co/datasets/taozi555/novel-multilingual) - Raw novel data
- Claude LLM - Quality labeling and evaluation

## 📧 Contact

For questions or suggestions, please submit an Issue on Hugging Face.

---

**Keywords**: Role-Playing, Character Simulation, Multilingual, Novel, LLM Training, SFT Data, Quality Scoring, LLM-Labeled, Safety-Filtered
