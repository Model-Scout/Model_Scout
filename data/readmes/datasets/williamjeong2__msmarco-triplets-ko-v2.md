---
task_categories:
- feature-extraction
language:
- ko
---



# MS MARCO Triplets - Korean Version (v2)

## Introduction

Welcome to the Korean version of the MS MARCO Triplets dataset. This project aims to provide a comprehensive, high-quality translation of the original MS MARCO Triplets dataset into Korean, facilitating natural language processing and information retrieval research for the Korean language community.

## Dataset Description

The MS MARCO (Microsoft Machine Reading Comprehension) Triplets dataset is a large-scale dataset designed for information retrieval tasks. It consists of query-document pairs along with relevance judgments, making it an invaluable resource for training and evaluating information retrieval systems.

This Korean version maintains the structure and integrity of the original dataset while offering content in the Korean language. It includes:

- Queries: Questions or search queries in Korean
- Positive Documents: Relevant passages or documents translated into Korean
- Negative Documents: Non-relevant passages or documents translated into Korean

### Key Features

1. Large-scale dataset suitable for machine learning model training
2. Diverse range of topics covered
3. Human-quality translations preserving semantic meanings
4. Maintained triplet structure for relevance assessments

### Data Format

The dataset is provided in JSONL (JSON Lines) format. Each line in the file represents a single data point with the following structure:

```json
{"query": "Korean query", "pos": ["Positive Korean sentence"], "neg": ["Negative Korean sentence 1", "Negative Korean sentence 2", ...]}
```

- `query`: A string containing the Korean query
- `pos`: An array containing a single string, which is the positive (relevant) document for the query
- `neg`: An array containing one or more strings, each representing a negative (non-relevant) document for the query

## Translation Process

### Methodology

The translation was performed using the [Translation-EnKo/EXAONE-3.0-7.8B-Instruct-translation-general12m-en-ko-e1-b64-trc1400k-e1-b64-trc313eval45-e2-b16](https://huggingface.co/Translation-EnKo/EXAONE-3.0-7.8B-Instruct-translation-general12m-en-ko-e1-b64-trc1400k-e1-b64-trc313eval45-e2-b16) model. This advanced language model was chosen for its capability to handle nuanced translations and maintain contextual accuracy.

### Known Limitations

During the translation process, we encountered a limitation that affected some data points:

- Repetitive Translations: Due to constraints in the translation model, some data points contain repetitive phrases or sentences in their Korean translations. This occurs when the model reaches its output limit and repeats the last translated segment.

Users should be aware of this limitation when working with the dataset. While these instances are present, they represent a small portion of the overall dataset and should not significantly impact its utility for most applications.

## Usage

This Korean version of the MS MARCO Triplets dataset is suitable for a wide range of natural language processing and information retrieval tasks, including but not limited to:

1. Training and evaluating Korean language information retrieval systems
2. Developing and testing question-answering models for Korean
3. Researching semantic similarity and relevance ranking in Korean
4. Cross-lingual information retrieval studies (when used in conjunction with the original English dataset)
5. Benchmarking machine learning models for Korean language understanding

### Loading the Dataset

To load and use the dataset, you can use libraries such as `jsonlines` in Python. Here's a simple example:

```python
import jsonlines
def load_dataset(file_path):
    data = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            data.append(obj)
    return data
# Usage
dataset = load_dataset('path_to_your_jsonl_file.jsonl')
# Accessing data
for item in dataset:
    query = item['query']
    positive_doc = item['pos'][0]
    negative_docs = item['neg']
    # Process your data here
```

## Ethical Considerations

When using this dataset, please consider the following ethical points:

1. Bias: While efforts have been made to maintain the integrity of the original dataset, unconscious biases may have been introduced during the translation process.
2. Privacy: Ensure that your use of the dataset complies with relevant privacy laws and regulations.
3. Responsible AI: Develop models and applications with this dataset in a manner that promotes fairness, transparency, and accountability.

## License

This dataset inherits the license of the original MS MARCO Triplets dataset. Users are required to comply with the [terms and conditions](https://microsoft.github.io/msmarco/Submission#terms-and-conditions) set forth in the original license.

## Citation

If you use this dataset in your research or applications, please cite both this Korean version and the original MS MARCO Triplets dataset. Suggested citations:

(For this Korean version)
```
[Jinwoo Jeong]. (2024). MS MARCO Triplets - Korean Version (v2) [Data set]. Hugging Face. https://huggingface.co/datasets/williamjeong2/msmarco-triplets-korean-v2
```

(For the original MS MARCO dataset)
```
@article{bajaj2016ms,
title={Ms marco: A human generated machine reading comprehension dataset},
author={Bajaj, Payal and Campos, Daniel and Craswell, Nick and Deng, Li and Gao, Jianfeng and Liu, Xiaodong and Majumder, Rangan and McNamara, Andrew and Mitra, Bhaskar and Nguyen, Tri and others},
journal={arXiv preprint arXiv:1611.09268},
year={2016}
}
```

## Acknowledgments

We would like to express our gratitude to:

- The creators and maintainers of the original MS MARCO Triplets dataset for providing this valuable resource to the research community.
- The developers of the [Translation-EnKo/EXAONE-3.0-7.8B-Instruct-translation-general12m-en-ko-e1-b64-trc1400k-e1-b64-trc313eval45-e2-b16](https://huggingface.co/Translation-EnKo/EXAONE-3.0-7.8B-Instruct-translation-general12m-en-ko-e1-b64-trc1400k-e1-b64-trc313eval45-e2-b16) model, which made this high-quality Korean translation possible.
- The open-source community for their continuous support and contributions to natural language processing research.

## Contact and Support

For questions, feedback, or issues related to this Korean version of the MS MARCO Triplets dataset, please:

1. Open an issue in this repository
2. Contact the maintainer at [wjd5480@gmail.com]

We welcome contributions and suggestions to improve the quality and usability of this dataset for the Korean NLP community.