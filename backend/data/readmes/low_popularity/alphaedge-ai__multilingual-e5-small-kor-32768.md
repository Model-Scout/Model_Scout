---
pipeline_tag: sentence-similarity
language: kor
license: mit
tags:
  - trimmed
library_name: sentence-transformers
base_model: intfloat/multilingual-e5-small
base_model_relation: quantized
datasets:
  - lbourdois/fineweb-2-trimming
---

# multilingual-e5-small-kor-32768
This model is a **70.91% smaller** version of [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) optimized for **Korean** language via vocabulary size reduction using the [trimming](https://huggingface.co/blog/lbourdois/introduction-to-trimming) method.  
This trimmed model should perform similarly to the original model with only 32,768 tokens and a much smaller memory footprint. However, it may not perform well for other languages as tokens not commonly used in the selected languages were removed from the vocabulary.

## Model Statistics
| Metric | Original | Trimmed | Reduction |
|--------|----------|---------|-----------|
| **Vocabulary size** | 250,037 tokens | 32,768 tokens | **86.89%** |
| **Model size** | 117,653,760 params | 34,222,464 params | **70.91%** |

![image](https://raw.githubusercontent.com/lbourdois/blog/refs/heads/master/assets/images/Trimming/me5-small-32768.png)

## Mining Dataset Statistics
- **Number of texts used for mining**: 200,000 texts  
- **Dataset**: [lbourdois/fineweb-2-trimming](https://huggingface.co/datasets/lbourdois/fineweb-2-trimming)

## Usage
```python
from sentence_transformers import SentenceTransformer
# Download from the 🤗 Hub
model = SentenceTransformer("alphaedge-ai/multilingual-e5-small-kor-32768")
# Run inference with queries and documents
query = "My query in Korean"
documents = [
    "Chunk in Korean",
    "Chunk in Korean",
    "Chunk in Korean",
]
query_embeddings = model.encode_query(query)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# Compute similarities to determine a ranking
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
```

## Citations

#### Multilingual E5
```
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```

#### Trimming blog post
```
@misc{hf_blogpost_trimming,
      title={Introduction to Trimming}, 
      author={Loïck BOURDOIS and Tom AARSEN and Bram VANROY and Christopher AKIKI and Woojun JUNG and Manuel ROMERO and Prithiv SAKTHI},
      year={2026},
      url={https://huggingface.co/blog/lbourdois/introduction-to-trimming}, 
}
```