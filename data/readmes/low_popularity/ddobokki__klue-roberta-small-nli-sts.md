---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- ko
---

# ddobokki/klue-roberta-small-nli-sts

한국어 Sentence Transformer 모델입니다.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

[sentence-transformers](https://www.SBERT.net) 라이브러리를 이용해 사용할 수 있습니다.

```
pip install -U sentence-transformers
```

사용법

```python
from sentence_transformers import SentenceTransformer
sentences = ["흐르는 강물을 거꾸로 거슬러 오르는", "세월이 가면 가슴이 터질 듯한"]

model = SentenceTransformer('ddobokki/klue-roberta-small-nli-sts')
embeddings = model.encode(sentences)
print(embeddings)
```



## Usage (HuggingFace Transformers)
transformers 라이브러리만 사용할 경우

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["흐르는 강물을 거꾸로 거슬러 오르는", "세월이 가면 가슴이 터질 듯한"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('ddobokki/klue-roberta-small-nli-sts')
model = AutoModel.from_pretrained('ddobokki/klue-roberta-small-nli-sts')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```

## Performance
- Semantic Textual Similarity test set results <br>

| Model                  | Cosine Pearson | Cosine Spearman | Euclidean Pearson | Euclidean Spearman | Manhattan Pearson | Manhattan Spearman | Dot Pearson | Dot Spearman |
|------------------------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| KoSRoBERTa<sup>small</sup>    | 84.27 | 84.17 | 83.33 | 83.65 | 83.34 | 83.65 | 82.10 | 81.38 |


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->