---
configs:
  - config_name: ragas_eval_v3
    data_files:
      - split: baseline
        path: data/ragas_eval_v3/baseline.parquet
  - config_name: ragas_eval
    data_files:
      - split: baseline
        path: data/ragas_eval/baseline.parquet
  - config_name: main
    data_files:
      - split: train
        path: data/main/train.parquet
      - split: validation
        path: data/main/validation.parquet
      - split: test
        path: data/main/test.parquet
  - config_name: corpus
    data_files:
      - split: corpus
        path: data/corpus/corpus.parquet
language:
  - en
license: cc-by-sa-4.0
task_categories:
  - question-answering
size_categories:
  - 10K<n<100K
---

# FiQA Dataset for RAG Evaluation

The FiQA (Financial Opinion Mining and Question Answering) dataset reformatted specifically for evaluating Retrieval-Augmented Generation (RAG) systems. This dataset contains financial domain questions with ground truth answers and retrieved contexts, making it ideal for testing RAG pipelines on domain-specific content.

## Recommended Usage: `ragas_eval_v3`

The `ragas_eval_v3` configuration is the **primary and recommended** way to use this dataset. It contains pre-generated RAG outputs ready for evaluation with a standardized schema.

### Dataset Structure (`ragas_eval_v3`)

Each sample contains:
- **user_input**: The financial question to be answered
- **reference**: Ground truth answer for evaluation
- **response**: Generated answer from a RAG system
- **retrieved_contexts**: List of retrieved context passages used to generate the answer

### Example

```python
{
  'user_input': 'How to deposit a cheque issued to an associate in my business into my business account?',
  'reference': 'Have the check reissued to the proper payee.Just have the associate sign the back and then deposit it...',
  'response': 'The best way to deposit a cheque issued to an associate in your business into your business account is to open a business account with the bank...',
  'retrieved_contexts': ["Just have the associate sign the back and then deposit it. It's called a third party cheque...", "I have checked with Bank of America, and they say..."]
}
```

### Usage

```python
from datasets import load_dataset

# Load the evaluation dataset (recommended)
dataset = load_dataset("explodinggradients/fiqa", "ragas_eval_v3")

# Access the baseline split
eval_data = dataset["baseline"]

# Use for RAG evaluation
for sample in eval_data:
    user_input = sample["user_input"]
    reference = sample["reference"]
    response = sample["response"]
    contexts = sample["retrieved_contexts"]
    # Your evaluation code here (e.g., using ragas)
```

## Alternative Configurations

### `main` Configuration

Training/validation/test splits with questions and ground truth answers only (no generated answers or contexts).

**Structure:**
- **question**: The financial question
- **ground_truths**: List of reference answers

**Splits:**
- `train`: 5,500 question-answer pairs
- `validation`: 500 question-answer pairs
- `test`: 648 question-answer pairs

```python
# Load main configuration
dataset = load_dataset("explodinggradients/fiqa", "main")
train_data = dataset["train"]
val_data = dataset["validation"]
test_data = dataset["test"]
```

### `corpus` Configuration

The complete document corpus of 57,638 financial documents that can be used for retrieval.

**Structure:**
- **doc**: The document text

```python
# Load corpus
corpus = load_dataset("explodinggradients/fiqa", "corpus")
documents = corpus["corpus"]
```

## Dataset Statistics

| Configuration | Split(s) | Samples | Description |
|--------------|----------|---------|-------------|
| `ragas_eval_v3` | baseline | 30 | Pre-generated RAG outputs (v3 schema) - **Recommended** |
| `ragas_eval` | baseline | 30 | Pre-generated RAG outputs (legacy) - Deprecated |
| `main` | train/val/test | 6,648 total | Question-answer pairs for training |
| `corpus` | corpus | 57,638 | Full document collection |

## Legacy Configuration

> ⚠️ **Note**: The `ragas_eval` configuration is deprecated. Please use `ragas_eval_v3` for all new projects.

<details>
<summary>Legacy ragas_eval schema (click to expand)</summary>

The old `ragas_eval` configuration uses:
- **question** instead of user_input
- **ground_truths** (list) instead of reference (string)
- **answer** instead of response
- **contexts** instead of retrieved_contexts

```python
# Legacy usage (not recommended)
dataset = load_dataset("explodinggradients/fiqa", "ragas_eval")
```

</details>

## Use Cases

1. **RAG System Evaluation**: Use `ragas_eval_v3` to benchmark your RAG pipeline against baseline outputs
2. **Question Answering**: Train models using the `main` configuration
3. **Information Retrieval**: Build retrieval systems using the `corpus` configuration
4. **End-to-End RAG**: Combine `main` questions with `corpus` documents to build and test complete RAG systems

## Citation

If you use this dataset, please cite the original FiQA paper:

```bibtex
@article{maia2018www,
  title={WWW'18 Open Challenge: Financial Opinion Mining and Question Answering},
  author={Maia, Macedo and Handschuh, Siegfried and Freitas, Andr{\'e} and Davis, Brian and McDermott, Ross and Zarrouk, Manel and Balahur, Alexandra},
  booktitle={Companion Proceedings of the The Web Conference 2018},
  pages={1941--1942},
  year={2018}
}
```

## Additional Information

- **Homepage**: https://sites.google.com/view/fiqa/
- **License**: CC BY-SA 4.0
- **Language**: English
- **Domain**: Financial Services

## Related Work

This dataset is optimized for use with [Ragas](https://github.com/explodinggradients/ragas), a framework for evaluating RAG systems.
