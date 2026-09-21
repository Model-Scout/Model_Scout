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

# moco-sentencebertV2.0

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

- 이 모델은 [bongsoo/mbertV2.0](https://huggingface.co/bongsoo/mbertV2.0) MLM 모델을
<br>sentencebert로 만든 후,추가적으로 STS Tearch-student 증류 학습 시켜 만든 모델 입니다.
- **vocab: 152,537 개**(기존 119,548 vocab 에 32,989 신규 vocab 추가)

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence_transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('bongsoo/moco-sentencebertV2.0')
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
[[ 0.16649279 -0.2933038  -0.00391259 ...  0.00720964  0.18175027  -0.21052675]
 [ 0.10106096 -0.11454111 -0.00378215 ... -0.009032   -0.2111504   -0.15030429]]
*cosine_score:0.3352515697479248
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
tokenizer = AutoTokenizer.from_pretrained('bongsoo/moco-sentencebertV2.0')
model = AutoModel.from_pretrained('bongsoo/moco-sentencebertV2.0')

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
tensor([[ 0.1665, -0.2933, -0.0039,  ...,  0.0072,  0.1818, -0.2105],
        [ 0.1011, -0.1145, -0.0038,  ..., -0.0090, -0.2112, -0.1503]])
*cosine_score:0.3352515697479248
```

## Evaluation Results

<!--- Describe how your model was evaluated -->

- 성능 측정을 위한 말뭉치는,  아래 한국어 (kor), 영어(en)  평가 말뭉치를 이용함
<br> 한국어 : **korsts(1,379쌍문장)** 와 **klue-sts(519쌍문장)** 
<br> 영어 : [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)(1,376쌍문장) 와 [glue:stsb](https://huggingface.co/datasets/glue/viewer/stsb/validation) (1,500쌍문장)
- 성능 지표는 **cosin.spearman** 측정하여 비교함.
- 평가 측정 코드는 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-test.ipynb) 참조

|모델     |korsts|klue-sts|korsts+klue-sts|stsb_multi_mt|glue(stsb)
|:--------|------:|--------:|--------------:|------------:|-----------:|
|distiluse-base-multilingual-cased-v2|0.747|0.785|0.577|0.807|0.819|
|paraphrase-multilingual-mpnet-base-v2|0.820|0.799|0.711|0.868|0.890|
|bongsoo/sentencedistilbertV1.2|0.819|0.858|0.630|0.837|0.873|
|bongsoo/moco-sentencedistilbertV2.0|0.812|0.847|0.627|0.837|0.877|
|bongsoo/moco-sentencebertV2.0|0.824|0.841|0.635|0.843|0.879|

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training(훈련 과정)
The model was trained with the parameters:

**1. MLM 훈련**
- 입력 모델 : bert-base-multilingual-cased
- 말뭉치 : 훈련 : bongsoo/moco-corpus-kowiki2022(7.6M) , 평가: bongsoo/bongevalsmall
- HyperParameter : LearningRate : 5e-5, epochs: 8, batchsize: 32, max_token_len : 128
- vocab : 152,537개 (기존 119,548 에 32,989 신규 vocab 추가)
- 출력 모델 : mbertV2.0 (size: 813MB)
- 훈련시간 : 90h/1GPU (24GB/19.6GB use)
- loss : 훈련loss: 2.258400, 평가loss: 3.102096, perplexity: 19.78158(bong_eval:1,500)
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/bert/bert-MLM-Trainer-V1.2.ipynb) 참조

**2. STS 훈련**
=>bert를 sentencebert로 만듬. 
- 입력 모델 : mbertV2.0
- 말뭉치 : korsts + kluestsV1.1 + stsb_multi_mt + mteb/sickr-sts (총:33,093)
- HyperParameter : LearningRate : 3e-5, epochs: 200, batchsize: 32, max_token_len : 128
- 출력 모델 : sbert-mbertV2.0 (size: 813MB)
- 훈련시간 : 9h20m/1GPU (24GB/9.0GB use)
- loss(cosin_spearman) : 0.799(말뭉치:korsts(tune_test.tsv))
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조
    
**3.증류(distilation) 훈련**
- 학생 모델 : sbert-mbertV2.0
- 교사 모델 : paraphrase-multilingual-mpnet-base-v2
- 말뭉치 : en_ko_train.tsv(한국어-영어 사회과학분야 병렬 말뭉치 : 1.1M)
- HyperParameter : LearningRate : 5e-5, epochs: 40, batchsize: 128, max_token_len : 128
- 출력 모델 : sbert-mlbertV2.0-distil
- 훈련시간 : 17h/1GPU (24GB/18.6GB use)
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-distillaton.ipynb) 참조

**4.STS 훈련**
=> sentencebert 모델을 sts 훈련시킴
- 입력 모델 : sbert-mlbertV2.0-distil
- 말뭉치 : korsts(5,749) + kluestsV1.1(11,668) + stsb_multi_mt(5,749) + mteb/sickr-sts(9,927) + glue stsb(5,749) (총:38,842)
- HyperParameter : LearningRate : 3e-5, epochs: 800, batchsize: 64, max_token_len : 128
- 출력 모델 : moco-sentencebertV2.0
- 훈련시간 : 25h/1GPU (24GB/13GB use)
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
  "_name_or_path": "../../data11/model/sbert/sbert-mbertV2.0-distil",
  "architectures": [
    "BertModel"
  ],
  "attention_probs_dropout_prob": 0.1,
  "classifier_dropout": null,
  "directionality": "bidi",
  "hidden_act": "gelu",
  "hidden_dropout_prob": 0.1,
  "hidden_size": 768,
  "initializer_range": 0.02,
  "intermediate_size": 3072,
  "layer_norm_eps": 1e-12,
  "max_position_embeddings": 512,
  "model_type": "bert",
  "num_attention_heads": 12,
  "num_hidden_layers": 12,
  "pad_token_id": 0,
  "pooler_fc_size": 768,
  "pooler_num_attention_heads": 12,
  "pooler_num_fc_layers": 3,
  "pooler_size_per_head": 128,
  "pooler_type": "first_token_transform",
  "position_embedding_type": "absolute",
  "torch_dtype": "float32",
  "transformers_version": "4.21.2",
  "type_vocab_size": 2,
  "use_cache": true,
  "vocab_size": 152537
}

```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
bongsoo