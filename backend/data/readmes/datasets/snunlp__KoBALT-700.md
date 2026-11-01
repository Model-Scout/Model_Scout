---
license: cc-by-nc-4.0
language:
  - ko

configs:
  - config_name: kobalt_v1
    data_files:
      - split: raw
        path: data/train.jsonl
---

# **[KoBALT: Korean Benchmark For Advanced Linguistic Tasks](https://arxiv.org/pdf/2505.16125)**

**KoBALT** is designed to advance the evaluation of large language models (LLMs) in Korean, a morphologically rich language, by addressing the limitations of conventional benchmarks that often lack linguistic depth and typological grounding. It consists of **700 expert-written multiple-choice questions** covering **24 fine-grained linguistic phenomena** across five core linguistic domains:

- **Syntax (300)**
- **Semantics (215)**
- **Pragmatics (81)**
- **Phonetics/Phonology (62)**
- **Morphology (42)**

The benchmark is designed to minimize training data contamination, with items showing less than **8.6% bigram** and **0.7% trigram** overlap with standard Korean corpora—making KoBALT a robust tool for evaluating genuine language understanding.

KoBALT combines expert-crafted linguistic tasks and LLM-generated items to probe deep linguistic competence. Its typologically aware design provides both a detailed diagnostic for Korean LLMs and a blueprint for high-quality benchmarks in other languages.

---

## Quick Start

### Dataset Access
- **Hugging Face Hub**: [https://huggingface.co/datasets/snunlp/KoBALT-700](https://huggingface.co/datasets/snunlp/KoBALT-700)
- **GitHub Repository**: [https://github.com/snunlp/KoBALT](https://github.com/snunlp/KoBALT)

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/snunlp/KoBALT.git
cd KoBALT

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file with your API keys
```

### Basic Usage
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("snunlp/KoBALT-700", "kobalt_v1")

# Filter by difficulty level
easy_items = dataset.filter(lambda x: x["Level"] == 1)
hard_items = dataset.filter(lambda x: x["Level"] == 3)

# Filter by domain
syntax_items = dataset.filter(lambda x: x["Class"] == "Syntax")
```

---

## Dataset Composition

KoBALT comprises the following linguistic domains and phenomena:

| **Domain**        | **Phenomenon**                      | **# Items** | **Description**                                                                 |
|------------------|-------------------------------------|-------------|---------------------------------------------------------------------------------|
| **Syntax**        | Agreement                           | 104         | Subject-verb, honorific, tense, polarity, passive/causative alignment          |
|                  | Argument Structure & Valency        | 96          | Predicate-argument relations, case realization                                 |
|                  | Embedded Clauses                    | 86          | Comprehension of complex clauses                                               |
|                  | Ellipsis                            | 11          | Grammatical omission patterns                                                  |
|                  | Scrambling                          | 3           | Word order flexibility                                                         |
| **Semantics**     | Semantic Compatibility              | 60          | Predicate-argument compatibility                                               |
|                  | Rhetorical Expressions              | 28          | Metaphor, irony, idioms                                                        |
|                  | Ambiguity                           | 27          | Lexical, structural, scope ambiguities                                         |
|                  | Word Relationships                  | 28          | Synonymy, antonymy, semantic frames                                            |
|                  | Numeral Classifiers                 | 27          | Classifier morphemes with quantified nouns                                     |
|                  | Conjunctions                        | 24          | Causal, temporal, and entailment-based conjunctions                            |
|                  | Inter-sentence Relations            | 21          | Semantic coherence across sentences                                            |
| **Pragmatics**    | Speech Acts                         | 22          | Statement, question, directive, promise, expressive                            |
|                  | Implicature                         | 22          | Implied meaning beyond literal content                                         |
|                  | Discourse Principles                | 17          | Conversational maxims and discourse strategies                                 |
|                  | Deixis & Reference                  | 17          | Personal, spatial, temporal references                                         |
|                  | Social Relationship Marking         | 3           | Honorifics, speech levels, address forms                                       |
| **Phonetics/Phonology** | Phonological Alternation           | 34          | Substitution, deletion, assimilation, etc.                                     |
|                  | Phonological Constraints            | 14          | Permissible sound patterns                                                     |
|                  | Articulatory Phonetics              | 7           | Production of speech sounds                                                    |
|                  | Suprasegmental Features             | 7           | Intonation, prosody, interrogative cues                                        |
| **Morphology**    | Word Formation                      | 22          | Derivation, compounding                                                        |
|                  | Verbal Conjugation                  | 12          | Inflection of verbs/adjectives                                                 |
|                  | POS & Morphemes                     | 8           | Part-of-speech tagging, morpheme analysis                                      |

---

## Difficulty-Based Subsets

KoBALT provides three difficulty levels for flexible evaluation:

- **Level 1 (Easy)**: 182 items - Basic linguistic phenomena
- **Level 2 (Moderate)**: 220 items - Intermediate complexity
- **Level 3 (Hard)**: 298 items - Advanced linguistic understanding

### Usage Examples
```python
# Create difficulty-based subsets
kobalt_easy = dataset.filter(lambda x: x["Level"] == 1)
kobalt_moderate = dataset.filter(lambda x: x["Level"] == 2) 
kobalt_hard = dataset.filter(lambda x: x["Level"] == 3)

# Domain-specific evaluation
syntax_hard = dataset.filter(lambda x: x["Class"] == "Syntax" and x["Level"] == 3)
```

---

## Sample

Below is a sample entry from the dataset:

```json
{
  "ID": "67ce909c0b81d8ffa89e4fbb",
  "Class": "Semantics",
  "Subclass": "Inter-sentence Relations",
  "Question": "지문:\n영진: 수빈아, 혹시 지금 시간 돼? 다음주 회의 관련해서 부탁할 게 있어서.\n수빈: 무슨 일을 (ㄱ) [  ]? 뭐, 생각해보니 저번에 나도 너한테 신세를 (ㄴ) [  ] 일단 (ㄷ) [ ].\n\n문제: 영진이와 수빈이가 나누는 대화의 맥락상 빈칸에 들어갈 표현으로 가장 적절한 것을 (ㄱ), (ㄴ), (ㄷ) 순서대로 나열하시오.\n\nA: 벌이려고, 면했어서, 들러볼게\nB: 꾸미니, 갚으니깐, 들려볼까\nC: 맡기려나, 졌으니까, 들어보렴\nD: 시키겠는데, 고치도록, 들어볼게\nE: 시키려고, 졌으므로, 들어줘\nF: 계획하는구나, 갚으려면, 들어주라\nG: 벌이게, 졌어서, 들어줬구나\nH: 꾸미길래, 졌어서, 들어봐야지\nI: 계획하는데, 깨달아서, 들러보겠어\nJ: 맡기게, 망쳤어서, 들려본다\n",
  "Answer": "H",
  "Level": 3,
  "Sampling_YN": 0
}
```

### Data Schema

- **`ID`**: Unique identifier for each item
- **`Class`**: Major linguistic domain (Syntax, Semantics, Pragmatics, Morphology, Phonetics/Phonology)
- **`Subclass`**: Fine-grained linguistic phenomenon
- **`Question`**: Question text with multiple-choice options (A-J)
- **`Answer`**: Correct answer key (A-J)
- **`Level`**: Difficulty level (1=Easy, 2=Moderate, 3=Hard)
- **`Sampling_YN`**: Human preference test inclusion flag (1=included, 0=excluded)

---

## Evaluation Protocol

For detailed evaluation guidelines and best practices, please refer to:
- **Evaluation Protocol**: [`evaluation_protocol.md`](./evaluation_protocol.md)
- **Example Scripts**: [`examples/`](./examples/)

### Quick Evaluation
```python
from kobalt.evaluation import evaluate_model

# Evaluate a model on the full benchmark
results = evaluate_model(
    model_name="your-model",
    dataset=dataset,
    config_path="config/evaluation.yaml"
)

# Evaluate on specific difficulty level
hard_results = evaluate_model(
    model_name="your-model", 
    dataset=kobalt_hard,
    config_path="config/evaluation.yaml"
)
```

---

## Baseline Performance (Accuracy by Domain)

| **Model**             | Avg  | Syntax | Semantics | Pragmatics | Morphology | Phonetics |
|-----------------------|------|--------|-----------|------------|------------|-----------|
| Claude-3-7-sonnet     | 0.61 | 0.66   | 0.66      | 0.64       | 0.36       | 0.31      |
| Claude-3-5-sonnet     | 0.52 | 0.52   | 0.65      | 0.51       | 0.36       | 0.24      |
| DeepSeek-V3-XL        | 0.47 | 0.49   | 0.56      | 0.42       | 0.24       | 0.29      |
| GPT-4o                | 0.44 | 0.45   | 0.55      | 0.40       | 0.17       | 0.26      |
| DeepSeek-V3           | 0.43 | 0.41   | 0.57      | 0.42       | 0.26       | 0.23      |
| C4ai-command-a-03     | 0.36 | 0.30   | 0.52      | 0.36       | 0.24       | 0.18      |
| Gemma-3-27b           | 0.35 | 0.30   | 0.53      | 0.27       | 0.24       | 0.11      |
| Qwen2.5-72B           | 0.37 | 0.33   | 0.51      | 0.37       | 0.24       | 0.18      |
| Mistral-Small-24B     | 0.32 | 0.27   | 0.49      | 0.30       | 0.21       | 0.11      |
| Llama-3.3-70B         | 0.32 | 0.25   | 0.50      | 0.35       | 0.17       | 0.15      |
| Qwen2.5-32B           | 0.30 | 0.23   | 0.49      | 0.28       | 0.21       | 0.11      |
| Gemma-2-9b            | 0.21 | 0.17   | 0.34      | 0.15       | 0.12       | 0.11      |
| Aya-expanse-32b       | 0.25 | 0.21   | 0.40      | 0.12       | 0.10       | 0.16      |
| Aya-expanse-8b        | 0.19 | 0.15   | 0.33      | 0.11       | 0.12       | 0.06      |
| Qwen2.5-7B            | 0.19 | 0.14   | 0.33      | 0.11       | 0.19       | 0.06      |
| Llama-3.1-8B          | 0.17 | 0.13   | 0.26      | 0.12       | 0.10       | 0.11      |
| Ministral-8B          | 0.17 | 0.11   | 0.29      | 0.15       | 0.10       | 0.11      |
| Mistral-7B-v0.3       | 0.12 | 0.11   | 0.16      | 0.11       | 0.14       | 0.06      |


## Contributing

We welcome contributions to improve KoBALT! Please see our [contribution guidelines](CONTRIBUTING.md) for details on:

- Reporting issues
- Suggesting improvements
- Adding new language adaptations
- Code quality standards

---

## Contributors

- **Researchers** (SNU NLP Lab, Seoul National University):
  - Dongjun Jang  
  - Wooseok Song  
  - Jaeyoon Kim  
  - Chaeyoung Oh  
  - Hyemi Jo  
  - Youngchae Ahn  
  - Sihyun Oh  
  - Hyohyeong Jang
- **Advisors**:
  - Seoul National University, CL_NLP Lab:
    - Prof. Hyopil Shin
    - Prof. Sangah Lee
  - LG AI Research:
    - Jinsik Lee
    - Sunkyoung Kim
- **Sponsors**: LG AI Research
- **Organizers**:
  - Host: CL_NLP Lab, Seoul National University
    - **Lab homepage**: [http://knlp.snu.ac.kr](http://knlp.snu.ac.kr)
  - Co-organizer: LG AI Research
    - **LG AI Research homepage**: [https://www.lgresearch.ai](https://www.lgresearch.ai)

---

## License

KoBALT is released under the **[Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)** license.

---

## Citation

If you use this resource, please cite as follows:

```bibtex
@misc{shin2025kobaltkoreanbenchmarkadvanced,
      title={KoBALT: Korean Benchmark For Advanced Linguistic Tasks}, 
      author={Hyopil Shin and Sangah Lee and Dongjun Jang and Wooseok Song and Jaeyoon Kim and Chaeyoung Oh and Hyemi Jo and Youngchae Ahn and Sihyun Oh and Hyohyeong Chang and Sunkyoung Kim and Jinsik Lee},
      year={2025},
      eprint={2505.16125},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.16125}, 
}
```
```