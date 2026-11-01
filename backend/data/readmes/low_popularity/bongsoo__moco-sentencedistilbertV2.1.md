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

# moco-sentencedistilbertV2.1

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

- 이 모델은 [bongsoo/mdistilbertV2.1](https://huggingface.co/bongsoo/mdistilbertV2.1) MLM 모델을
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
sentences = ["서울은 한국이 수도이다", "The capital of Korea is Seoul"]

model = SentenceTransformer('bongsoo/moco-sentencedistilbertV2.1')
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
[[ 0.27124503 -0.5836643   0.00736023 ... -0.0038319   0.01802095 -0.09652182]
 [ 0.2765149  -0.5754248   0.00788184 ...  0.07659392 -0.07825544 -0.06120609]]
*cosine_score:0.9513546228408813
```

## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.
```
pip install transformers[torch]
```

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
sentences = ["서울은 한국이 수도이다", "The capital of Korea is Seoul"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('bongsoo/moco-sentencedistilbertV2.1')
model = AutoModel.from_pretrained('bongsoo/moco-sentencedistilbertV2.1')

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
tensor([[ 0.2712, -0.5837,  0.0074,  ..., -0.0038,  0.0180, -0.0965],
        [ 0.2765, -0.5754,  0.0079,  ...,  0.0766, -0.0783, -0.0612]])
*cosine_score:0.9513546228408813
```

## Evaluation Results

<!--- Describe how your model was evaluated -->

- 성능 측정을 위한 말뭉치는,  아래 한국어 (kor), 영어(en)  평가 말뭉치를 이용함
<br> 한국어 : **korsts(1,379쌍문장)** 와 **klue-sts(519쌍문장)** 
<br> 영어 : [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)(1,376쌍문장) 와 [glue:stsb](https://huggingface.co/datasets/glue/viewer/stsb/validation) (1,500쌍문장)
- 성능 지표는 **cosin.spearman/max**(cosine,eculidean,manhatten,doc중 max값)
- 평가 측정 코드는 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-test.ipynb) 참조

|모델     |korsts|klue-sts|glue(stsb)|stsb_multi_mt(en)|
|:--------|------:|--------:|--------------:|------------:|
|distiluse-base-multilingual-cased-v2   |0.7475/0.7556    |0.7855/0.7862    |0.8193           |0.8075/0.8168|
|paraphrase-multilingual-mpnet-base-v2  |0.8201           |0.7993           |**0.8907/0.8919**|**0.8682**   |
|bongsoo/sentencedistilbertV1.2         |0.8198/0.8202    |0.8584/0.8608    |0.8739/0.8740    |0.8377/0.8388|
|bongsoo/moco-sentencedistilbertV2.0    |0.8124/0.8128    |0.8470/0.8515    |0.8773/0.8778    |0.8371/0.8388|
|bongsoo/moco-sentencebertV2.0          |0.8244/0.8277    |0.8411/0.8478    |0.8792/0.8796    |0.8436/0.8456|
|**bongsoo/moco-sentencedistilbertV2.1**|**0.8390/0.8398**|**0.8767/0.8808**|0.8805/0.8816    |0.8548       |

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training(훈련 과정)
The model was trained with the parameters:

**1. MLM 훈련**
- 입력 모델 : distilbert-base-multilingual-cased
- 말뭉치 : 훈련 : bongsoo/moco-corpus-kowiki2022(7.6M) , 평가: bongsoo/bongevalsmall
- HyperParameter : **LearningRate : 5e-5, epochs: 8, batchsize: 32, max_token_len : 128**
- vocab : 152,537개 (기존 119,548 에 32,989 신규 vocab 추가)
- 출력 모델 : mdistilbertV2.1 (size: 643MB)
- 훈련시간 : 63h/1GPU (24GB/23.9 use)
- 평가: **훈련loss: 2.203400, 평가loss: 2.972835, perplexity: 23.43**(bong_eval:1,500)
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/distilbert/distilbert-MLM-Trainer-V1.2.ipynb) 참조

**2. STS 훈련**
<br>=>bert를 sentencebert로 만듬. 
- 입력 모델 : mdistilbertV2.1 (size: 643MB)
- 말뭉치 : korsts(5,749) + kluestsV1.1(11,668) + stsb_multi_mt(5,749) + mteb/sickr-sts(9,927) + glue stsb(5,749) (총:38,842)
- HyperParameter : **LearningRate : 3e-5, epochs: 800, batchsize: 128, max_token_len : 256**
- 출력 모델 : sbert-mdistilbertV2.1  (size: 640MB)
- 훈련시간 : 13h/1GPU (24GB/16.1GB use)
- 평가(cosin_spearman) : **0.790**(말뭉치:korsts(tune_test.tsv))
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조
    
**3.증류(distilation) 훈련**
- 학생 모델 : sbert-mdistilbertV2.1
- 교사 모델 : paraphrase-multilingual-mpnet-base-v2(max_token_len:128)
- 말뭉치 : news_talk_en_ko_train.tsv (영어-한국어 대화-뉴스 병렬 말뭉치 : 1.38M)
- HyperParameter : **LearningRate : 5e-5, epochs: 40, batchsize: 128, max_token_len : 128(교사모델이 128이므로 맟춰줌)**
- 출력 모델 : sbert-mdistilbertV2.1-distil
- 훈련시간 : 17h/1GPU (24GB/9GB use)
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-distillaton.ipynb) 참조

**4.STS 훈련**
<br>=> sentencebert 모델을 sts 훈련시킴
- 입력 모델 : sbert-mdistilbertV2.1-distil
- 말뭉치 : korsts(5,749) + kluestsV1.1(11,668) + stsb_multi_mt(5,749) + mteb/sickr-sts(9,927) + glue stsb(5,749) (총:38,842)
- HyperParameter : **LearningRate : 3e-5, epochs: 1200, batchsize: 128, max_token_len : 256**
- 출력 모델 : moco-sentencedistilbertV2.1
- 훈련시간 : 12/1GPU (24GB/16.1GB use)
- 평가(cosin_spearman) : **0.839**(말뭉치:korsts(tune_test.tsv))
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조

<br>모델 제작 과정에 대한 자세한 내용은 [여기](https://github.com/kobongsoo/BERT/tree/master)를 참조 하세요.


**Config**:

```
{
  "_name_or_path": "../../data11/model/sbert/sbert-mdistilbertV2.1-distil",
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
  "vocab_size": 152537
}

```

## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: DistilBertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## tokenizer_config
```
{
  "cls_token": "[CLS]",
  "do_basic_tokenize": true,
  "do_lower_case": false,
  "mask_token": "[MASK]",
  "max_len": 128,
  "name_or_path": "../../data11/model/sbert/sbert-mdistilbertV2.1-distil",
  "never_split": null,
  "pad_token": "[PAD]",
  "sep_token": "[SEP]",
  "special_tokens_map_file": "../../data11/model/distilbert/mdistilbertV2.1-4/special_tokens_map.json",
  "strip_accents": false,
  "tokenize_chinese_chars": true,
  "tokenizer_class": "DistilBertTokenizer",
  "unk_token": "[UNK]"
}
```

## sentence_bert_config
```
{
  "max_seq_length": 256,
  "do_lower_case": false
}
```

## config_sentence_transformers
```
{
  "__version__": {
    "sentence_transformers": "2.2.0",
    "transformers": "4.21.2",
    "pytorch": "1.10.1"
  }
}
```
## Citing & Authors

<!--- Describe where people can find more information -->
bongsoo