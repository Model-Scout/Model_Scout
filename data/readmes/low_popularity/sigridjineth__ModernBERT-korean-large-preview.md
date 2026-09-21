---
language:
- ko
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:1120235
- loss:CachedMultipleNegativesRankingLoss
base_model: answerdotai/ModernBERT-large
widget:
- source_sentence: 나, 가스불, 찻물, 올리다
  sentences:
  - 나는 가스불에 꽃을 넣은 찻물을 올렸다.
  - 과제수행 기간중에 연구 현장에 대해 정기점검을 실시하고, 과제 수행 종료 후에도 일정한 안전조치를 이행하도록 규정한다.
  - 고기, 상추, 밥, 나, 올리다
- source_sentence: 파란색 데님 재킷을 입은 여성과 검은색 코트를 입은 여성이 일본 식당 앞에 서 있다.
  sentences:
  - 복합 도금된 시편의 표면과 조성은 전계방출 주사전자현미경(field emission scanning electron microscopy,FESEM)과
    에너지 분산형 X-선 분광기(energy dispersivespectroscopy, EDS)를 이용하여 분석하였다.
  - 재킷을 입은 두 여자가 식당 밖에 서 있다.
  - 두 여자가 식당 밖에서 음식을 먹는다
- source_sentence: 한 남자가 암벽을 오르고 다른 남자가 아래에 있다.
  sentences:
  - 남자가 암벽을 기어오르다
  - 담당 공무원들은 보호 관찰 대상자를 정기적으로 상담을 했다.
  - 한 남자가 암벽에 오른다.
- source_sentence: 골목, 동네, 동, 나누다, 크다, 서
  sentences:
  - 큰 골목이 우리 동네를 동과 서로 나눠 놓았다.
  - 내 아내는 몸에 좋은 음식을 항상 만들어 주었다.
  - 골목, 많다, 공간, 놀이, 골목
- source_sentence: 한 소녀가 자전거를 타고 있고 모든 사람들이 도시에서 그녀에게 달려들고 있다.
  sentences:
  - 소녀는 자전거를 탄다
  - 소녀가 자전거를 타고 있다.
  - 그리고 특수한 소재의 광섬유를 이용한 온도센서는 감도가 고정되는 단점이 있고, 간섭계형 온도센서는 높은 감도의 장점을 가지지만, 2차 코팅이
    이루어지지 않은 광섬유 센서나 팁기반 광섬유 센서는 일반적으로 클래드를 제거하여 융착(splicing)을 하기 때문에 취급상에 불편함과 파손되기
    쉬운 단점을 가지고 있다.
datasets:
- sigridjineth/korean_nli_dataset_reranker_v1
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on answerdotai/ModernBERT-large
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: dev eval
      type: dev-eval
    metrics:
    - type: cosine_accuracy
      value: 0.877
      name: Cosine Accuracy
---

# SentenceTransformer based on answerdotai/ModernBERT-large

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) on the [korean_nli_dataset_reranker_v1](https://huggingface.co/datasets/sigridjineth/korean_nli_dataset_reranker_v1) dataset. It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) <!-- at revision f87846cf8be76fceb18718f0245d18c8e6571215 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [korean_nli_dataset_reranker_v1](https://huggingface.co/datasets/sigridjineth/korean_nli_dataset_reranker_v1)
- **Language:** ko
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: ModernBertModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Evaluation

### Metrics

### AutoRAG Retrieval

| Metrics | sigridjineth/ModernBERT-korean-large-preview (241225) | Alibaba-NLP/gte-multilingual-base | answerdotai/ModernBERT-large |
|------|----------------------------------------------|-----------------------------------|------------------------------|
| **NDCG@10** | 0.72503 | 0.77108 | 0.0 |
| **Recall@10** | 0.87719 | 0.93860 | 0.0 |
| **Precision@1** | 0.57018 | 0.59649 | 0.0 |
| **NDCG@100** | 0.74543 | 0.78411 | 0.01565 |
| **Recall@100** | 0.98246 | 1.0 | 0.09649 |
| **Recall@1000** | 1.0 | 1.0 | 1.0 |

#### Triplet

* Dataset: `dev-eval`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.877** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

* Size: 1,120,235 training samples
* Columns: <code>query</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | query                                                                              | positive                                                                            | negative                                                                             |
  |:--------|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                              | string                                                                               |
  | details | <ul><li>min: 5 tokens</li><li>mean: 55.49 tokens</li><li>max: 476 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 186.0 tokens</li><li>max: 1784 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 120.54 tokens</li><li>max: 2383 tokens</li></ul> |
* Samples:
  | query                                | positive                                                                                                                                                                                                                                                                                                                                                               | negative                                         |
  |:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------|
  | <code>양복을 입은 노인이 짐을 뒤로 끌고 간다.</code> | <code>양복을 입은 남자</code>                                                                                                                                                                                                                                                                                                                                                 | <code>옷을 입은 노인</code>                            |
  | <code>한국의 제1위 서비스 수출 시장은 중국이니</code> | <code>중국은 세계 제2위의 서비스 교역국*이자 우리나라의 제1위 서비스 수출 시장**으로서,<br>* 2016년 중국의 서비스교역 규모는 6,571억불로 미국(12,145억불)에 이어 세계 2위<br>* 중국 서비스산업의 GDP대비 비중은 2015년 50% 돌파, 서비스산업 성장률 98.3%) > GDP 성장률(6.9%)<br>** 2016년 서비스 분야 우리의 對中수출(206억불)은 對세계수출(949억불)의 22%<br>ㅇ 네거티브 방식의 포괄적인 서비스 투자 개방 협정이 중국과 체결될 경우, 양국간 상호 서비스 시장 개방 수준을 높이고, 우리 투자 기업에 대한 실질적 보호를 한층 강화할 수 있을 것으로 기대된다.</code> | <code>우리나라에서 중국으로 수출되는 제품은 점점 계속 증가하고 있다.</code> |
  | <code>아버지, 병원, 치료, 받다, 결심하다</code>   | <code>너무나 아팠던 아버지는 병원에서 치료를 받기로 결심했다.</code>                                                                                                                                                                                                                                                                                                                           | <code>요즘, 아버지, 건강, 걱정</code>                     |
* Loss: [<code>CachedMultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Logs
| Epoch  | Step | dev-eval_cosine_accuracy |
|:------:|:----:|:------------------------:|
| 0      | 0    | 0.331                    |
| 4.8783 | 170  | 0.877                    |


### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 3.3.1
- Transformers: 4.48.0.dev0
- PyTorch: 2.3.0+cu121
- Accelerate: 1.2.1
- Datasets: 3.2.0
- Tokenizers: 0.21.0

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### CachedMultipleNegativesRankingLoss
```bibtex
@misc{gao2021scaling,
    title={Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup},
    author={Luyu Gao and Yunyi Zhang and Jiawei Han and Jamie Callan},
    year={2021},
    eprint={2101.06983},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->