---
language:
- en
- zh
- ko
- ar
size_categories:
- 10K<n<100K
---
# Memorization or Reasoning? Exploring the Idiom Understanding of LLMs

#### Official Repository for "Memorization or Reasoning? Exploring the Idiom Understanding of LLMs" [[Paper Link (arXiv)]](https://arxiv.org/abs/2505.16216) 

##### Jisu Kim, Youngwoo Shin, Uiji Hwang, Jihun Choi, Richeng Xuan, and Taeuk Kim. *Accepted to EMNLP 2025 long paper*. 

---

<!-- ![MIDAS_Figure](docs/MIDAS.jpg) -->

## 🌏 Multilingual Idiom Dataset Across Six languages (MIDAS)

MIDAS is a comprehensive dataset spanning six typologically and culturally diverse languages: English (EN), German (DE), Chinese (ZH), Korean (KO), Arabic (AR), and Turkish(TR).
It contains approximately 10,000 idiom instances per language, each paired with a figurative meaning. Where available, example sentences are also included.

This repository includes four language subsets of MIDAS. 
German and Turkish had to be excluded due to copyright issues.

### 1. Dataset Format
The dataset includes four JSON files, each corresponding to a specific language.

For example, `EN_Idioms.json` is the English subset of our dataset.

All four subsets share the same schema of ID, Idiom, Meaning, and Sentence:
- `ID`: An identifier assigned to each row. Idioms that have multiple figurative meanings are assigned different IDs for each meaning, such as "n-1", "n-2"...
- `Idiom`: A list of idiom expression variants.
- `Meaning`: The figurative meaning of the idiom.
- `Sentence`: A list of example usage sentences including the idiom.

The following are some actual examples from our English subset:
```json
    {
    "ID": "9-1",
    "Idiom": [
      "800-pound gorilla"
    ],
    "Meaning": "An entity that dominates.",
    "Sentence": [
      "When it comes to the lucrative search market, Google, not Microsoft, is the 800-pound gorilla.",
      "The thing he unfortunately doesn't recognise is there is an 800-pound gorilla when it comes to major American motor sports. The 800-pound gorilla is Nascar.",
      "It was poetically fitting. For almost a year, Mr. Trump has been the 800-pound gorilla whose unpredictable rampages have obsessed the news media. Now he was completing the circle by commenting on the 400-pound gorilla who briefly stole the spotlight from him for one holiday weekend.",
      "Apache Spark is a cluster-computing framework. It’s the 800-pound gorilla you turn to when it’s impossible to fit your data in memory."
    ]
  },
  {
    "ID": "9-2",
    "Idiom": [
      "800-pound gorilla"
    ],
    "Meaning": "Something obvious but unaddressed that is dangerous or intimidating.",
    "Sentence": [
      "However, a co-author of the new study said those arguments ignore the “ 800-pound gorilla ”: sky-high prices everywhere."
    ]
  },
  {
    "ID": "2542",
    "Idiom": [
      "every dog must have his day",
      "every dog must have its day",
      "every dog has his day",
      "every dog has its day"
    ],
    "Meaning": "Everyone experiences success at some point in life.",
    "Sentence": [
      "\"To lose, it hurt. But I learned from that. I learned that every dog has its day. I learned patience.\"",
      "The Hearts manager John McGlynn was thrilled to be drawn against Liverpool in the Europa League play-offs. McGlynn said: \".... I would imagine the bookmakers would favour Liverpool but every dog has its day.\""
    ]
  }
```

### 2. Hugging Face Datasets
MIDAS is also available through the Hugging Face 'datasets' library!

```python
from datasets import load_dataset

dataset = load_dataset("HYU-NLP/MIDAS", data_dir="data/")
print(dataset[0])
```

### 3. Further Details
More details regarding our dataset is specified in Section 3 and Appendix A of our paper!

---

## 📚 Citation

```bibtex
@misc{kim2025memorizationreasoningexploringidiom,
      title={Memorization or Reasoning? Exploring the Idiom Understanding of LLMs}, 
      author={Jisu Kim and Youngwoo Shin and Uiji Hwang and Jihun Choi and Richeng Xuan and Taeuk Kim},
      year={2025},
      eprint={2505.16216},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.16216}, 
}
```