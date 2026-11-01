---
base_model: klue/roberta-base
datasets: []
language: []
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
- pearson_manhattan
- spearman_manhattan
- pearson_euclidean
- spearman_euclidean
- pearson_dot
- spearman_dot
- pearson_max
- spearman_max
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10501
- loss:CosineSimilarityLoss
widget:
- source_sentence: 기업은 생존 문제에 직면하고, 자영업자와 소상공인의 고통은 이루 말할 수 없을 정도입니다.
  sentences:
  - 자유무역은 기업이 서로를 신뢰하고, 미래의 불확실성을 낮추는 안전장치입니다.
  - 국가 임상연구 승인, 시행기관 지정, 장기 추적조사 등 안전관리체계를 구축하고 치료 개발 및 임상연구 수행을 위한 RD 투자를 확대합니다.
  - 중심가와 거리가 조금 먼 점 빼고는 정말 모든게 너무 좋았던 숙소입니다!
- source_sentence: 타이페이를 다시 간다면 여기 또 올거예요.
  sentences:
  - 사진으로 봤던것보다 훨씬 더 좋았습니다
  - 겨울에 난방 온도 이십오도 이상으로 올리지마라고 경고했어
  - 만약 내가 다시 타이페이에 간다면, 나는 여기에 다시 올 것입니다.
- source_sentence: 호주의 좋은 가정집에서 묵는 느낌이었어요.
  sentences:
  - 어린이 교통사고 위험지역에 CCTV 2087대, 신호등 2146개를 올해 상반기 중으로 설치하고 옐로카펫과 노란발자국 등을 올해 하반기에 초등학교
    100곳에 시범 설치한다.
  - 호주에 있는 좋은 집에서 지내는 것 같았어요.
  - 그러나 호텔업계 노사가 가장 어려운 시기에, 가장 모범적으로 함께 마음을 모았습니다.
- source_sentence: 그들덕분에 우리는 4일간 편안히 쉴 수 있었습니다.
  sentences:
  - 그들 덕분에, 우리는 4일 동안 쉴 수 있었어요.
  - 주변에 두 개의 지하철역이 있습니다. 큰 공원, 큰 슈퍼마켓, 그리고 편의점이 있습니다.
  - 방은 쾌적하고 에어컨도 아주 잘 나와요.
- source_sentence: 테라스에서 봤던 뷰와 그곳에서 먹었던 식사가 그리울 것 같아요.
  sentences:
  - 테라스에서 본 풍경과 거기서 먹었던 음식이 그리울 것 같아요.
  - 이쪽 주변에서 여행할 계획이라면 추천합니다!
  - 저희 할아버지는 매우 친절하고 친절하십니다.
co2_eq_emissions:
  emissions: 7.379414346751554
  energy_consumed: 0.016863301234344347
  source: codecarbon
  training_type: fine-tuning
  on_cloud: false
  cpu_model: 13th Gen Intel(R) Core(TM) i7-13700
  ram_total_size: 62.56697463989258
  hours_used: 0.057
  hardware_used: 1 x NVIDIA GeForce RTX 4090
model-index:
- name: SentenceTransformer based on klue/roberta-base
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: Unknown
      type: unknown
    metrics:
    - type: pearson_cosine
      value: 0.34770704341988723
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.3673846313946801
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.36460670798564826
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.3607451203867209
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.35482778401649034
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.21251167982120983
      name: Pearson Dot
    - type: spearman_dot
      value: 0.20063256899469895
      name: Spearman Dot
    - type: pearson_max
      value: 0.3673846313946801
      name: Pearson Max
    - type: spearman_max
      value: 0.36460670798564826
      name: Spearman Max
    - type: pearson_cosine
      value: 0.961968864970919
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9196100863981246
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.9530332430579778
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.9186168431687389
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.9532923011007042
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.9190754386835427
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.9493179101338206
      name: Pearson Dot
    - type: spearman_dot
      value: 0.8999468521869318
      name: Spearman Dot
    - type: pearson_max
      value: 0.961968864970919
      name: Pearson Max
    - type: spearman_max
      value: 0.9196100863981246
      name: Spearman Max
---

# SentenceTransformer based on klue/roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [klue/roberta-base](https://huggingface.co/klue/roberta-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [klue/roberta-base](https://huggingface.co/klue/roberta-base) <!-- at revision 02f94ba5e3fcb7e2a58a390b8639b0fac974a8da -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
    '테라스에서 봤던 뷰와 그곳에서 먹었던 식사가 그리울 것 같아요.',
    '테라스에서 본 풍경과 거기서 먹었던 음식이 그리울 것 같아요.',
    '이쪽 주변에서 여행할 계획이라면 추천합니다!',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

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

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.3477     |
| spearman_cosine    | 0.3556     |
| pearson_manhattan  | 0.3674     |
| spearman_manhattan | 0.3646     |
| pearson_euclidean  | 0.3607     |
| spearman_euclidean | 0.3548     |
| pearson_dot        | 0.2125     |
| spearman_dot       | 0.2006     |
| pearson_max        | 0.3674     |
| **spearman_max**   | **0.3646** |

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.962      |
| spearman_cosine    | 0.9196     |
| pearson_manhattan  | 0.953      |
| spearman_manhattan | 0.9186     |
| pearson_euclidean  | 0.9533     |
| spearman_euclidean | 0.9191     |
| pearson_dot        | 0.9493     |
| spearman_dot       | 0.8999     |
| pearson_max        | 0.962      |
| **spearman_max**   | **0.9196** |

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


* Size: 10,501 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                        | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 7 tokens</li><li>mean: 20.23 tokens</li><li>max: 64 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 19.94 tokens</li><li>max: 63 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.44</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                      | sentence_1                                                                                                        | label                            |
  |:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|:---------------------------------|
  | <code>지하철 역 내려서 1분정도의 아주 가까운 거리입니다.</code>                                                                      | <code>지하철역에서 1분 정도 아주 가까운 거리입니다.</code>                                                                           | <code>0.86</code>                |
  | <code>그것빼곤 2인여행자들에게는 좋은숙소에요!</code>                                                                             | <code>계단이 많다는거 빼곤 완벽한 숙소에요!</code>                                                                                | <code>0.27999999999999997</code> |
  | <code>이어 현금이 286만 가구(13.2%) 1조3007억원, 선불카드가 75만 가구(3.5%) 4990억원, 지역사랑상품권은 63만 가구(2.9%) 4171억원으로 각각 집계됐다.</code> | <code>이어 현금 286만 가구(13.2%), 현금 1조337억 원, 선불카드 75만 가구(3.5%), 4990억 원, 지역사랑상품권 63만 가구(2.9%), 4171억 원 순이었습니다.</code> | <code>0.86</code>                |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 4
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 4
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
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
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
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
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
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
- `eval_on_start`: False
- `eval_use_gather_object`: False
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch  | Step | Training Loss | spearman_max |
|:------:|:----:|:-------------:|:------------:|
| 0      | 0    | -             | 0.3646       |
| 0.7610 | 500  | 0.0283        | -            |
| 1.0    | 657  | -             | 0.9075       |
| 1.5221 | 1000 | 0.0082        | 0.9148       |
| 2.0    | 1314 | -             | 0.9148       |
| 2.2831 | 1500 | 0.0047        | -            |
| 3.0    | 1971 | -             | 0.9180       |
| 3.0441 | 2000 | 0.0034        | 0.9168       |
| 3.8052 | 2500 | 0.0027        | -            |
| 4.0    | 2628 | -             | 0.9196       |


### Environmental Impact
Carbon emissions were measured using [CodeCarbon](https://github.com/mlco2/codecarbon).
- **Energy Consumed**: 0.017 kWh
- **Carbon Emitted**: 0.007 kg of CO2
- **Hours Used**: 0.057 hours

### Training Hardware
- **On Cloud**: No
- **GPU Model**: 1 x NVIDIA GeForce RTX 4090
- **CPU Model**: 13th Gen Intel(R) Core(TM) i7-13700
- **RAM Size**: 62.57 GB

### Framework Versions
- Python: 3.9.0
- Sentence Transformers: 3.0.1
- Transformers: 4.44.1
- PyTorch: 2.3.1+cu121
- Accelerate: 0.33.0
- Datasets: 2.19.1
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