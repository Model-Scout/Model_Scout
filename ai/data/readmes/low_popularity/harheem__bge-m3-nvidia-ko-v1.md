---
base_model: BAAI/bge-m3
language:
- ko
library_name: sentence-transformers
license: apache-2.0
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dataset_size:1K<n<10K
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: 하이브리다이저란 무엇인가요?
  sentences:
  - 하이퍼바이저는 보안에서 어떤 역할을 합니까?
  - 지난 몇 년간 CUDA 생태계는 어떻게 발전해 왔나요?
  - 로컬 메모리 액세스 성능을 결정하는 요소는 무엇입니까?
- source_sentence: 임시 구독의 용도는 무엇입니까?
  sentences:
  - 메모리 액세스 최적화에서 프리패치의 역할은 무엇입니까?
  - CUDA 인식 MPI는 확장 측면에서 어떻게 작동합니까?
  - CUDA 8이 해결하는 계산상의 과제에는 어떤 것이 있습니까?
- source_sentence: '''saxpy''는 무엇을 뜻하나요?'
  sentences:
  - CUDA C/C++의 맥락에서 SAXPY는 무엇입니까?
  - Numba는 다른 GPU 가속 방법과 어떻게 다른가요?
  - 장치 LTO는 CUDA 애플리케이션에 어떤 이점을 제공합니까?
- source_sentence: USD/Hydra란 무엇인가요?
  sentences:
  - 쿠다란 무엇인가요?
  - y 미분 계산에 사용되는 접근 방식의 단점은 무엇입니까?
  - Pascal 아키텍처는 통합 메모리를 어떻게 개선합니까?
- source_sentence: CUDAcast란 무엇인가요?
  sentences:
  - CUDACast 시리즈에서는 어떤 주제를 다룰 예정인가요?
  - 이 게시물에 기여한 것으로 인정받은 사람은 누구입니까?
  - WSL 2에서 NVML의 목적은 무엇입니까?
model-index:
- name: BGE base Financial Matryoshka
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 768
      type: dim_768
    metrics:
    - type: cosine_accuracy@1
      value: 0.5443037974683544
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7749648382559775
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8523206751054853
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9409282700421941
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.5443037974683544
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.2583216127519925
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.17046413502109703
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09409282700421939
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.5443037974683544
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7749648382559775
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8523206751054853
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9409282700421941
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7411108924386547
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.677065054807671
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6802131506478553
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 512
      type: dim_512
    metrics:
    - type: cosine_accuracy@1
      value: 0.5386779184247539
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7749648382559775
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8593530239099859
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9451476793248945
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.5386779184247539
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.2583216127519925
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.17187060478199717
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09451476793248943
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.5386779184247539
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7749648382559775
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8593530239099859
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9451476793248945
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7413571133247474
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.6759917844306029
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.678939165210132
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 256
      type: dim_256
    metrics:
    - type: cosine_accuracy@1
      value: 0.540084388185654
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7791842475386779
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8621659634317862
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9423347398030942
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.540084388185654
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.25972808251289264
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.1724331926863572
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09423347398030943
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.540084388185654
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7791842475386779
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8621659634317862
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9423347398030942
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7403981257690416
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.6756379344986938
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6787046866761269
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 128
      type: dim_128
    metrics:
    - type: cosine_accuracy@1
      value: 0.5218002812939522
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7679324894514767
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8635724331926864
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9367088607594937
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.5218002812939522
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.2559774964838256
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.17271448663853725
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09367088607594935
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.5218002812939522
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7679324894514767
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8635724331926864
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9367088607594937
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7305864977688176
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.6641673922264634
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6671648971944116
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 64
      type: dim_64
    metrics:
    - type: cosine_accuracy@1
      value: 0.509142053445851
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7426160337552743
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8284106891701828
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9310829817158931
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.509142053445851
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.24753867791842477
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.16568213783403654
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09310829817158929
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.509142053445851
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7426160337552743
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8284106891701828
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9310829817158931
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7135661304090457
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.6444829549259928
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6474431148702396
      name: Cosine Map@100
---

# BGE base Financial Matryoshka

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) <!-- at revision 5617a9f61b028005a4858fdac845db406aefb181 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'CUDAcast란 무엇인가요?',
    'CUDACast 시리즈에서는 어떤 주제를 다룰 예정인가요?',
    '이 게시물에 기여한 것으로 인정받은 사람은 누구입니까?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval
* Dataset: `dim_768`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.5443     |
| cosine_accuracy@3   | 0.775      |
| cosine_accuracy@5   | 0.8523     |
| cosine_accuracy@10  | 0.9409     |
| cosine_precision@1  | 0.5443     |
| cosine_precision@3  | 0.2583     |
| cosine_precision@5  | 0.1705     |
| cosine_precision@10 | 0.0941     |
| cosine_recall@1     | 0.5443     |
| cosine_recall@3     | 0.775      |
| cosine_recall@5     | 0.8523     |
| cosine_recall@10    | 0.9409     |
| cosine_ndcg@10      | 0.7411     |
| cosine_mrr@10       | 0.6771     |
| **cosine_map@100**  | **0.6802** |

#### Information Retrieval
* Dataset: `dim_512`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.5387     |
| cosine_accuracy@3   | 0.775      |
| cosine_accuracy@5   | 0.8594     |
| cosine_accuracy@10  | 0.9451     |
| cosine_precision@1  | 0.5387     |
| cosine_precision@3  | 0.2583     |
| cosine_precision@5  | 0.1719     |
| cosine_precision@10 | 0.0945     |
| cosine_recall@1     | 0.5387     |
| cosine_recall@3     | 0.775      |
| cosine_recall@5     | 0.8594     |
| cosine_recall@10    | 0.9451     |
| cosine_ndcg@10      | 0.7414     |
| cosine_mrr@10       | 0.676      |
| **cosine_map@100**  | **0.6789** |

#### Information Retrieval
* Dataset: `dim_256`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.5401     |
| cosine_accuracy@3   | 0.7792     |
| cosine_accuracy@5   | 0.8622     |
| cosine_accuracy@10  | 0.9423     |
| cosine_precision@1  | 0.5401     |
| cosine_precision@3  | 0.2597     |
| cosine_precision@5  | 0.1724     |
| cosine_precision@10 | 0.0942     |
| cosine_recall@1     | 0.5401     |
| cosine_recall@3     | 0.7792     |
| cosine_recall@5     | 0.8622     |
| cosine_recall@10    | 0.9423     |
| cosine_ndcg@10      | 0.7404     |
| cosine_mrr@10       | 0.6756     |
| **cosine_map@100**  | **0.6787** |

#### Information Retrieval
* Dataset: `dim_128`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.5218     |
| cosine_accuracy@3   | 0.7679     |
| cosine_accuracy@5   | 0.8636     |
| cosine_accuracy@10  | 0.9367     |
| cosine_precision@1  | 0.5218     |
| cosine_precision@3  | 0.256      |
| cosine_precision@5  | 0.1727     |
| cosine_precision@10 | 0.0937     |
| cosine_recall@1     | 0.5218     |
| cosine_recall@3     | 0.7679     |
| cosine_recall@5     | 0.8636     |
| cosine_recall@10    | 0.9367     |
| cosine_ndcg@10      | 0.7306     |
| cosine_mrr@10       | 0.6642     |
| **cosine_map@100**  | **0.6672** |

#### Information Retrieval
* Dataset: `dim_64`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.5091     |
| cosine_accuracy@3   | 0.7426     |
| cosine_accuracy@5   | 0.8284     |
| cosine_accuracy@10  | 0.9311     |
| cosine_precision@1  | 0.5091     |
| cosine_precision@3  | 0.2475     |
| cosine_precision@5  | 0.1657     |
| cosine_precision@10 | 0.0931     |
| cosine_recall@1     | 0.5091     |
| cosine_recall@3     | 0.7426     |
| cosine_recall@5     | 0.8284     |
| cosine_recall@10    | 0.9311     |
| cosine_ndcg@10      | 0.7136     |
| cosine_mrr@10       | 0.6445     |
| **cosine_map@100**  | **0.6474** |

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

#### Unnamed Dataset


* Size: 6,397 training samples
* Columns: <code>positive</code> and <code>anchor</code>
* Approximate statistics based on the first 1000 samples:
  |         | positive                                                                            | anchor                                                                           |
  |:--------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                           |
  | details | <ul><li>min: 11 tokens</li><li>mean: 48.46 tokens</li><li>max: 107 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 21.0 tokens</li><li>max: 48 tokens</li></ul> |
* Samples:
  | positive                                                                                                                                              | anchor                                                        |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | <code>Warp-stride 및 block-stride 루프는 스레드 동작을 재구성하고 공유 메모리 액세스 패턴을 최적화하는 데 사용되었습니다.</code>                                                             | <code>코드에서 공유 메모리 액세스 패턴을 최적화하기 위해 어떤 유형의 루프가 사용되었습니까?</code> |
  | <code>Nsight Compute의 규칙은 성능 병목 현상을 식별하기 위한 구조화된 프레임워크를 제공하고 최적화 프로세스를 간소화하기 위한 실행 가능한 통찰력을 제공합니다.</code>                                             | <code>Nsight Compute의 맥락에서 규칙이 중요한 이유는 무엇입니까?</code>          |
  | <code>NVIDIA Nsight와 같은 도구의 가용성으로 인해 개발자가 단일 GPU에서 디버깅할 수 있게 되어 CUDA 개발 속도가 크게 향상되었습니다. CUDA 메모리 검사기는 메모리 액세스 문제를 식별하여 코드 품질을 향상시키는 데 도움이 됩니다.</code> | <code>디버깅 도구의 가용성이 CUDA 개발에 어떤 영향을 미쳤습니까?</code>              |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `gradient_accumulation_steps`: 16
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `bf16`: True
- `tf32`: True
- `load_best_model_at_end`: True
- `optim`: adamw_torch_fused
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 16
- `eval_accumulation_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: True
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch    | Step   | Training Loss | dim_128_cosine_map@100 | dim_256_cosine_map@100 | dim_512_cosine_map@100 | dim_64_cosine_map@100 | dim_768_cosine_map@100 |
|:--------:|:------:|:-------------:|:----------------------:|:----------------------:|:----------------------:|:---------------------:|:----------------------:|
| 0.8      | 10     | 1.3103        | -                      | -                      | -                      | -                     | -                      |
| 0.96     | 12     | -             | 0.6512                 | 0.6539                 | 0.6688                 | 0.6172                | 0.6679                 |
| 1.6      | 20     | 0.4148        | -                      | -                      | -                      | -                     | -                      |
| 2.0      | 25     | -             | 0.6615                 | 0.6688                 | 0.6783                 | 0.6417                | 0.6763                 |
| 2.4      | 30     | 0.2683        | -                      | -                      | -                      | -                     | -                      |
| **2.88** | **36** | **-**         | **0.6672**             | **0.6787**             | **0.6789**             | **0.6474**            | **0.6802**             |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.0.0
- Transformers: 4.41.2
- PyTorch: 2.1.2+cu121
- Accelerate: 0.31.0
- Datasets: 2.18.0
- Tokenizers: 0.19.1

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

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning}, 
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply}, 
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
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