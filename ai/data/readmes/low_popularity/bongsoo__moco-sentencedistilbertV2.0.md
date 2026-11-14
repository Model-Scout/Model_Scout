---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- ko
- en
widget:
  source_sentence: "대한민국의 수도는?"
  sentences:
    - "서울특별시는 한국이 정치,경제,문화 중심 도시이다."
    - "부산은 대한민국의 제2의 도시이자 최대의 해양 물류 도시이다."
    - "제주도는 대한민국에서 유명한 관광지이다"
    - "Seoul is the capital of Korea"
    - "울산광역시는 대한민국 남동부 해안에 있는 광역시이다" 
---

# moco-sentencedistilbertV2.0

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

- 이 모델은 [mdistilbertV1.1](https://huggingface.co/bongsoo/mdistilbertV1.1) 모델에 [moco-corpus 말뭉치](https://huggingface.co/datasets/bongsoo/moco-corpus)(MOCOMSYS 추출 3.2M 문장)로 
<br>sentencebert로 만든 후,추가적으로 STS Tearch-student 증류 학습 시켜 만든 모델 입니다.
- **vocab: 164,314 개**(기존 mdistilbertV1.1 vocab(146,444 개)에 17,870개 vocab 추가)
<br> **MLM 모델 : bongsoo/mdistilbertV2.0** 

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence_transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('bongsoo/moco-sentencedistilbertV2.0')
embeddings = model.encode(sentences)
print(embeddings)

# sklearn 을 이용하여 cosine_scores를 구함
# => 입력값 embeddings 은 (1,768) 처럼 2D 여야 함.
from sklearn.metrics.pairwise import paired_cosine_distances, paired_euclidean_distances, paired_manhattan_distances
cosine_scores = 1 - (paired_cosine_distances(embeddings[0].reshape(1,-1), embeddings[1].reshape(1,-1)))

print(f'*cosine_score:{cosine_scores[0]}')

```
#### 출력(Outputs)
```
[[ 9.7172342e-02 -3.3226651e-01 -7.7130608e-05 ...  1.3900512e-02 2.1072578e-01 -1.5386048e-01]
 [ 2.3313640e-02 -8.4675789e-02 -3.7715461e-06 ...  2.4005771e-02 -1.6602692e-01 -1.2729791e-01]]
*cosine_score:0.3383665680885315
```

## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.
- 평균 폴링(mean_pooling) 방식 사용. ([cls 폴링](https://huggingface.co/sentence-transformers/bert-base-nli-cls-token), [max 폴링](https://huggingface.co/sentence-transformers/bert-base-nli-max-tokens))
```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('bongsoo/moco-sentencedistilbertV2.0')
model = AutoModel.from_pretrained('bongsoo/moco-sentencedistilbertV2.0')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)

# sklearn 을 이용하여 cosine_scores를 구함
# => 입력값 embeddings 은 (1,768) 처럼 2D 여야 함.
from sklearn.metrics.pairwise import paired_cosine_distances, paired_euclidean_distances, paired_manhattan_distances
cosine_scores = 1 - (paired_cosine_distances(sentence_embeddings[0].reshape(1,-1), sentence_embeddings[1].reshape(1,-1)))

print(f'*cosine_score:{cosine_scores[0]}')
```
#### 출력(Outputs)
```
Sentence embeddings:
tensor([[ 9.7172e-02, -3.3227e-01, -7.7131e-05,  ...,  1.3901e-02, 2.1073e-01, -1.5386e-01],
        [ 2.3314e-02, -8.4676e-02, -3.7715e-06,  ...,  2.4006e-02, -1.6603e-01, -1.2730e-01]])
*cosine_score:0.3383665680885315
```
## Evaluation Results

<!--- Describe how your model was evaluated -->

- 성능 측정을 위한 말뭉치는,  아래 한국어 (kor), 영어(en)  평가 말뭉치를 이용함
<br> 한국어 : **korsts(1,379쌍문장)** 와 **klue-sts(519쌍문장)** 
<br> 영어 : [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)(1,376쌍문장)
- 성능 지표는 **cosin.spearman** 측정하여 비교함.
- 평가 측정 코드는 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-test.ipynb) 참조

|모델     |korsts|klue-sts|korsts+klue-sts|stsb_multi_mt
|:--------|------:|--------:|--------------:|------------:|
|bongsoo/sentencedistilbertV1.2|0.819|0.858|0.630|0.837|
|distiluse-base-multilingual-cased-v2|0.747|0.785|0.577|0.807|
|paraphrase-multilingual-mpnet-base-v2|0.820|0.799|0.711|0.868|
|bongsoo/moco-sentencedistilbertV2.0|0.812|0.847|0.627|0.837|

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training(훈련 과정)
The model was trained with the parameters:

**1. MLM 훈련**
- 입력 모델 : bongsoo/mdistilbertV1.1(*kowiki20220620(4.4M) 말뭉치 훈련된 distilbert-base-multilingual-cased)
- 말뭉치 : nlp_corpus(3.2M) : MOCOMSYS 파일들 정제한 말뭉치
- HyperParameter : LearningRate : 5e-5, epochs: 8, batchsize: 32, max_token_len : 128
- 출력 모델 : mdistilbertV2.0
- 훈련시간 : 27h
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/distilbert/distilbert-MLM-Trainer-V1.2.ipynb) 참조

**2. STS 훈련**
- distilbert를 sentencebert로 만듬. 
- 입력 모델 : mdistilbertV2.0
- 말뭉치 : korsts + kluestsV1.1 + stsb_multi_mt + mteb/sickr-sts (총:33,093)
- HyperParameter : LearningRate : 2e-5, epochs: 200, batchsize: 32, max_token_len : 128
- 출력 모델 : sbert-mdistilbertV2.0
- 훈련시간 : 5h
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조
    
**3.증류(distilation) 훈련**
- 학생 모델 : sbert-mdistilbertV2.0
- 교사 모델 : paraphrase-multilingual-mpnet-base-v2
- 말뭉치 : en_ko_train.tsv(한국어-영어 사회과학분야 병렬 말뭉치 : 1.1M)
- HyperParameter : LearningRate : 5e-5, epochs: 40, batchsize: 32, max_token_len : 128
- 출력 모델 : sbert-mdistilbertV2.0.2-distil
- 훈련시간 : 11h
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-distillaton.ipynb) 참조

**4.STS 훈련**
-sentencebert 모델을 sts 훈련시킴
- 입력 모델 : sbert-mdistilbertV2.0.2-distil
- 말뭉치 : korsts + kluestsV1.1 + stsb_multi_mt + mteb/sickr-sts (총:33,093)
- HyperParameter : LearningRate : 3e-5, epochs: 800, batchsize: 32, max_token_len : 128
- 출력 모델 : moco-sentencedistilbertV2.0
- 훈련시간 : 15h
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조

<br>모델 제작 과정에 대한 자세한 내용은 [여기](https://github.com/kobongsoo/BERT/tree/master)를 참조 하세요.

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 1035 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Config**:

```
{
  "_name_or_path": "../../data11/model/sbert/sbert-mdistilbertV2.0.2-distil",
  "activation": "gelu",
  "architectures": [
    "DistilBertModel"
  ],
  "attention_dropout": 0.1,
  "dim": 768,
  "dropout": 0.1,
  "hidden_dim": 3072,
  "initializer_range": 0.02,
  "max_position_embeddings": 512,
  "model_type": "distilbert",
  "n_heads": 12,
  "n_layers": 6,
  "output_past": true,
  "pad_token_id": 0,
  "qa_dropout": 0.1,
  "seq_classif_dropout": 0.2,
  "sinusoidal_pos_embds": false,
  "tie_weights_": true,
  "torch_dtype": "float32",
  "transformers_version": "4.21.2",
  "vocab_size": 164314
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: DistilBertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
bongsoo