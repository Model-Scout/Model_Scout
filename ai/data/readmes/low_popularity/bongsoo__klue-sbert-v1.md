---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
---

# klue-sbert-v1

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

klue/bert-base 모델을 sentencebert로 파인튜닝한 모델

## Evaluation Results

- 성능 측정을 위한 말뭉치는,  아래 한국어 (kor), 영어(en)  평가 말뭉치를 이용함
<br> 한국어 : **korsts(1,379쌍문장)** 와 **klue-sts(519쌍문장)** 
<br> 영어 : [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)(1,376쌍문장) 와 [glue:stsb](https://huggingface.co/datasets/glue/viewer/stsb/validation) (1,500쌍문장)
- 성능 지표는 **cosin.spearman**
- 평가 측정 코드는 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-test3.ipynb) 참조
- 
|모델     |korsts|klue-sts|glue(stsb)|stsb_multi_mt(en)|
|:--------|------:|--------:|--------------:|------------:|
|distiluse-base-multilingual-cased-v2   |0.7475    |0.7855    |0.8193           |0.8075|
|paraphrase-multilingual-mpnet-base-v2  |0.8201    |0.7993    |0.8907           |0.8682|
|bongsoo/albert-small-kor-sbert-v1      |0.8305    |0.8588    |0.8419           |0.7965|
|bongsoo/kpf-sbert-v1.0                 |0.8590    |0.8924    |0.8840           |0.8531|
|**bongsoo/klue-sbert-v1.0**                |0.8529    |0.8952    |0.8813           |0.8469|

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})

## Training
- [klue/bert-base](https://huggingface.co/klue/bert-base) 모델을 sts(10)-distil(10)-nli(3)-sts(10) 훈련 시킴

The model was trained with the parameters:

**공통**
- **do_lower_case=1, correct_bios=0, polling_mode=mean**
  
**1.STS**
- 말뭉치 : korsts(5,749) + kluestsV1.1(11,668) + stsb_multi_mt(5,749) + mteb/sickr-sts(9,927) + glue stsb(5,749) (총:38,842)
- Param : **lr: 1e-4, eps: 1e-6, warm_step=10%, epochs: 10, train_batch: 128, eval_batch: 64, max_token_len: 72**
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentece-bert-sts.ipynb) 참조
    
**2.distilation**
- 교사 모델 : paraphrase-multilingual-mpnet-base-v2(max_token_len:128)
- 말뭉치 : news_talk_en_ko_train.tsv (영어-한국어 대화-뉴스 병렬 말뭉치 : 1.38M)
- Param : **lr: 5e-5, eps: 1e-8, epochs: 10, train_batch: 128, eval/test_batch: 64, max_token_len: 128(교사모델이 128이므로 맟춰줌)**
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sbert-distillaton.ipynb) 참조

**3.NLI**
- 말뭉치 : 훈련(967,852) : kornli(550,152), kluenli(24,998), glue-mnli(392,702) / 평가(3,519) : korsts(1,500), kluests(519), gluests(1,500) ()
- HyperParameter : **lr: 3e-5, eps: 1e-8, warm_step=10%, epochs: 3, train/eval_batch: 64, max_token_len: 128**
- 훈련코드 [여기](https://github.com/kobongsoo/BERT/blob/master/sbert/sentence-bert-nli.ipynb) 참조
- 
## Citing & Authors

bongsoo