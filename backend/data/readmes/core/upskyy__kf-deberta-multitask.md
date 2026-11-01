---
pipeline_tag: sentence-similarity
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - transformers
language: ko

---

# kf-deberta-multitask

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. You can check the training recipes on [GitHub](https://github.com/upskyy/kf-deberta-multitask).

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]

model = SentenceTransformer("upskyy/kf-deberta-multitask")
embeddings = model.encode(sentences)
print(embeddings)
```

## Usage (HuggingFace Transformers)

Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("upskyy/kf-deberta-multitask")
model = AutoModel.from_pretrained("upskyy/kf-deberta-multitask")

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

## Evaluation Results

<!--- Describe how your model was evaluated -->

KorSTS, KorNLI 학습 데이터셋으로 멀티 태스크 학습을 진행한 후 KorSTS 평가 데이터셋으로 평가한 결과입니다.

- Cosine Pearson: 85.75
- Cosine Spearman: 86.25
- Manhattan Pearson: 84.80
- Manhattan Spearman: 85.27
- Euclidean Pearson: 84.79
- Euclidean Spearman: 85.25
- Dot Pearson: 82.93
- Dot Spearman: 82.86

<br>

|model|cosine_pearson|cosine_spearman|euclidean_pearson|euclidean_spearman|manhattan_pearson|manhattan_spearman|dot_pearson|dot_spearman|
|:-------------------------|-----------------:|------------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|---------------:|
|[kf-deberta-multitask](https://huggingface.co/upskyy/kf-deberta-multitask)|**85.75**|**86.25**|**84.79**|**85.25**|**84.80**|**85.27**|**82.93**|**82.86**|
|[ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask)|84.77|85.6|83.71|84.40|83.70|84.38|82.42|82.33|
|[ko-sbert-multitask](https://huggingface.co/jhgan/ko-sbert-multitask)|84.13|84.71|82.42|82.66|82.41|82.69|80.05|79.69|
|[ko-sroberta-base-nli](https://huggingface.co/jhgan/ko-sroberta-nli)|82.83|83.85|82.87|83.29|82.88|83.28|80.34|79.69|
|[ko-sbert-nli](https://huggingface.co/jhgan/ko-sbert-multitask)|82.24|83.16|82.19|82.31|82.18|82.3|79.3|78.78|
|[ko-sroberta-sts](https://huggingface.co/jhgan/ko-sroberta-sts)|81.84|81.82|81.15|81.25|81.14|81.25|79.09|78.54|
|[ko-sbert-sts](https://huggingface.co/jhgan/ko-sbert-sts)|81.55|81.23|79.94|79.79|79.9|79.75|76.02|75.31|

<br>

## Training

The model was trained with the parameters:

**DataLoader**:

`sentence_transformers.datasets.NoDuplicatesDataLoader.NoDuplicatesDataLoader` of length 4442 with parameters:

```
{'batch_size': 128}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:

  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 719 with parameters:

```
{'batch_size': 8, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss`

Parameters of the fit()-Method:

```
{
    "epochs": 10,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 719,
    "weight_decay": 0.01
}
```

## Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: DebertaV2Model 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->

```bibtex
@proceedings{jeon-etal-2023-kfdeberta,
  title         = {KF-DeBERTa: Financial Domain-specific Pre-trained Language Model},
  author        = {Eunkwang Jeon, Jungdae Kim, Minsang Song, and Joohyun Ryu},
  booktitle     = {Proceedings of the 35th Annual Conference on Human and Cognitive Language Technology},
  moth          = {oct},
  year          = {2023},
  publisher     = {Korean Institute of Information Scientists and Engineers},
  url           = {http://www.hclt.kr/symp/?lnb=conference},
  pages         = {143--148},
}
```

```bibtex
@article{ham2020kornli,
  title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
  author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
  journal={arXiv preprint arXiv:2004.03289},
  year={2020}
}
```
