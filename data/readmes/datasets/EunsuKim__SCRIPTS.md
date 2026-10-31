---
license: cc-by-nc-nd-4.0
task_categories:
- question-answering
language:
- en
- ko
tags:
- social-reasoning
- dialogue
- conversation-analysis
size_categories:
- n<1K
---

<div align="center">
  <h1> Are they lovers or friends? Evaluating LLMs' Social Reasoning in English and Korean Dialogues </h1>
  <p>
    <a href="https://arxiv.org/pdf/2510.19028">
      <img src="https://img.shields.io/badge/ArXiv-SCRIPTS-red" alt="Paper">
    </a>
    <a href="https://github.com/rladmstn1714/SCRIPTS">
      <img src="https://img.shields.io/badge/GitHub-Code-blue" alt="GitHub">
    </a>
    <a href="https://huggingface.co/datasets/EunsuKim/SCRIPTS">
      <img src="https://img.shields.io/badge/🤗_HuggingFace-Dataset-yellow" alt="Hugging Face">
    </a>
  </p>
</div>

**Official dataset for [Are they lovers or friends? Evaluating LLMs' Social Reasoning in English and Korean Dialogues](https://arxiv.org/pdf/2510.19028).**

## Dataset Description

SCRIPTS is a bilingual dialogue dataset for evaluating social reasoning capabilities of Large Language Models. The dataset contains dialogues with rich annotations about relationships, social dimensions, and demographic attributes.

### Dataset Splits

- **`en`**: 580 English dialogues
- **`ko`**: 567 Korean dialogues

### Languages

- English
- Korean (한국어)

## Dataset Structure

### Data Fields

Each example contains the following fields:

#### Core Fields
- `scene_id` (string): Unique identifier for each dialogue
- `dialogue` (string): Conversation text with speaker markers `[A]:` and `[B]:`

#### Social Relation 
- `relation_high_probable_gold` (string): Ground truth high-probability social relation
- `relation_impossible_gold` (string): Relations annotated as impossible/unlikely
- `high_probable_agreement` (string): Inter-annotator agreement level

#### Social Dimensions
- `intimacy_gold` (string): Intimacy level (intimate, not intimate, neutral, unknown)
- `intimacy_agreement` (float): Inter-annotator agreement score
- `formality_gold` (string): Formality/task orientation (formal, informal, neutral, unknown)
- `formality_agreement` (float): Inter-annotator agreement score
- `hierarchy_gold` (string): Power dynamics (equal, hierarchical, unknown)
- `hierarchy_agreement` (float): Inter-annotator agreement score

#### Demographics
- `age-a_gold` (string): Age category for speaker A
- `age-b_gold` (string): Age category for speaker B
- `age_diff_gold` (string): Age comparison (A>B, A<B, A=B, Unknown)
- `gender-a_gold` (string): Gender for speaker A
- `gender-b_gold` (string): Gender for speaker B
- `gender_diff_gold` (string): Gender comparison (Same, Different, Unknown)

### Data Example

**English (`en` split):**
```python
{
  'scene_id': 'scene300',
  'dialogue': '[B]: [A], right? Happy to meet you.\n[A]: Officially almost human again...',
  'relation_high_probable_gold': "{'rank1': {'Police-Victim': 0.67, 'Police officer-Civilian': 0.33}, ...}",
  'intimacy_gold': 'Unintimate',
  'formality_gold': 'Task-oriented',
  'hierarchy_gold': 'A<B',
  'age-a_gold': "['(20–35) Young adult']",
  'gender-a_gold': "['Cannot be determined']",
  ...
}
```

**Korean (`ko` split):**
```python
{
  'scene_id': '0',
  'dialogue': 'B: 눈깔 안 돌리면 뽑아서 골프공으로 쓴다!...고 속으로 말했습니다...',
  'relation_high_probable_gold': "['친구', '성직자-신도', '지인']",
  'intimacy_gold': '친함',
  'formality_gold': '즐거움 중심',
  'hierarchy_gold': 'A=B',
  'age-a_gold': "['대학생(20-24)', '청년(25-39)', '중장년(40-59)', '노년(65-)']",
  'gender-a_gold': "['남성', '여성']",
  ...
}
```

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load both splits
dataset = load_dataset('EunsuKim/SCRIPTS')

# Access English dialogues
en_data = dataset['en']
print(f"English samples: {len(en_data)}")

# Access Korean dialogues
ko_data = dataset['ko']
print(f"Korean samples: {len(ko_data)}")

# View a sample
print(en_data[0])
```

### Loading Specific Split

```python
# Load only English
en_dataset = load_dataset('EunsuKim/SCRIPTS', split='en')

# Load only Korean
ko_dataset = load_dataset('EunsuKim/SCRIPTS', split='ko')
```

### Example: Filtering by Relation Type

```python
from datasets import load_dataset

dataset = load_dataset('EunsuKim/SCRIPTS', split='en')

# Filter dialogues with high intimacy
intimate_dialogues = dataset.filter(lambda x: 'intimate' in x['intimacy_gold'].lower())
print(f"Found {len(intimate_dialogues)} intimate dialogues")
```

## License

**CC-BY-NC-ND 4.0** (Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International)

## Citation

```bibtex
@misc{kim2025loversfriendsevaluatingllms,
      title={Are they lovers or friends? Evaluating LLMs' Social Reasoning in English and Korean Dialogues}, 
      author={Eunsu Kim and Junyeong Park and Juhyun Oh and Kiwoong Park and Seyoung Song and A. Seza Dogruoz and Najoung Kim and Alice Oh},
      year={2025},
      eprint={2510.19028},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.19028}, 
}
```

## Contact

For questions or issues, please:
- Open an issue on [GitHub](https://github.com/rladmstn1714/SCRIPTS)
- Refer to the [paper](https://arxiv.org/pdf/2510.19028) for detailed methodology

