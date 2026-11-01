---
language:
- ko
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:11668
- loss:CosineSimilarityLoss
datasets:
- klue/klue
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
widget:
- source_sentence: 이는 지난 15일 개최된 제1차 주요국 외교장관간 협의에 뒤이은 것이다.
  sentences:
  - 100일간의 유럽 여행 중 단연 최고의 숙소였습니다!
  - 이것은 7월 15일에 열린 주요 국가의 외무 장관들 간의 첫 번째 회담에 이은 것입니다.
  - 거실옆 작은 방에도 싱글 침대가 두개 있습니다.
- source_sentence: 3000만원 이하 소액대출은 지역신용보증재단 심사를 기업은행에 위탁하기로 했다.
  sentences:
  - 그 집은 두 사람이 살기에 충분히 크고 깨끗했습니다.
  - 3,000만원 미만의 소규모 대출은 기업은행에 의해 국내 신용보증재단을 검토하도록 의뢰될 것입니다.
  - 지하철, 버스, 기차 모두 편리했습니다.
- source_sentence: 공간은 4명의 성인 가족이 사용하기에 부족함이 없었고.
  sentences:
  - 특히 모든 부처 장관들이 책상이 아닌 현장에서 직접 방역과 민생 경제의 중심에 서 주시기 바랍니다.
  - 구시가까지 걸어서 15분 정도 걸립니다.
  - 그 공간은 4인 가족에게는 충분하지 않았습니다.
- source_sentence: 클락키까지 걸어서 10분 정도 걸려요.
  sentences:
  - 가족 여행이나 4명정도 같이 가는 일행은 정말 좋은 곳 같아요
  - 외출 시 방범 모드는 어떻게 바꿔?
  - 타이페이 메인 역까지 걸어서 10분 정도 걸립니다.
- source_sentence: SR은 동대구·김천구미·신경주역에서 승하차하는 모든 국민에게 운임 10%를 할인해 준다.
  sentences:
  - 그 방은 두 사람이 쓰기에는 조금 좁아요.
  - 수강신청 하는 날짜가 어느 날짜인지 아시는지요?
  - SR은 동대구역, 김천구미역, 신주역을 오가는 모든 승객을 대상으로 요금을 10% 할인해 드립니다.
pipeline_tag: sentence-similarity
model-index:
- name: SentenceTransformer
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts dev
      type: sts-dev
    metrics:
    - type: pearson_cosine
      value: 0.8475782145205365
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8545963681447005
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.7968150076303364
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.7965856716776553
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.7968904585865801
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.7972334023226009
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.756409438338087
      name: Pearson Dot
    - type: spearman_dot
      value: 0.7638472444119945
      name: Spearman Dot
    - type: pearson_max
      value: 0.8475782145205365
      name: Pearson Max
    - type: spearman_max
      value: 0.8545963681447005
      name: Spearman Max
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained on the [klue/klue](https://huggingface.co/datasets/klue/klue) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [klue/klue](https://huggingface.co/datasets/klue/klue)
- **Language:** ko
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
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
model = SentenceTransformer("snunlp/KR-SBERT-Medium-klueNLI-klueSTS")
# Run inference
sentences = [
    'SR은 동대구·김천구미·신경주역에서 승하차하는 모든 국민에게 운임 10%를 할인해 준다.',
    'SR은 동대구역, 김천구미역, 신주역을 오가는 모든 승객을 대상으로 요금을 10% 할인해 드립니다.',
    '수강신청 하는 날짜가 어느 날짜인지 아시는지요?',
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
* Dataset: `sts-dev`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.8476     |
| **spearman_cosine** | **0.8546** |
| pearson_manhattan   | 0.7968     |
| spearman_manhattan  | 0.7966     |
| pearson_euclidean   | 0.7969     |
| spearman_euclidean  | 0.7972     |
| pearson_dot         | 0.7564     |
| spearman_dot        | 0.7638     |
| pearson_max         | 0.8476     |
| spearman_max        | 0.8546     |

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

#### klue/klue

* Dataset: [klue/klue](https://huggingface.co/datasets/klue/klue) at [349481e](https://huggingface.co/datasets/klue/klue/tree/349481ec73fff722f88e0453ca05c77a447d967c)
* Size: 11,668 training samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                         | sentence2                                                                         | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 7 tokens</li><li>mean: 18.53 tokens</li><li>max: 56 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 18.02 tokens</li><li>max: 60 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.44</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                                  | sentence2                                               | label                            |
  |:-----------------------------------------------------------|:--------------------------------------------------------|:---------------------------------|
  | <code>숙소 위치는 찾기 쉽고 일반적인 한국의 반지하 숙소입니다.</code>              | <code>숙박시설의 위치는 쉽게 찾을 수 있고 한국의 대표적인 반지하 숙박시설입니다.</code> | <code>0.7428571428571428</code>  |
  | <code>위반행위 조사 등을 거부·방해·기피한 자는 500만원 이하 과태료 부과 대상이다.</code> | <code>시민들 스스로 자발적인 예방 노력을 한 것은 아산 뿐만이 아니었다.</code>      | <code>0.0</code>                 |
  | <code>회사가 보낸 메일은 이 지메일이 아니라 다른 지메일 계정으로 전달해줘.</code>       | <code>사람들이 주로 네이버 메일을 쓰는 이유를 알려줘</code>                 | <code>0.06666666666666667</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Evaluation Dataset

#### klue/klue

* Dataset: [klue/klue](https://huggingface.co/datasets/klue/klue) at [349481e](https://huggingface.co/datasets/klue/klue/tree/349481ec73fff722f88e0453ca05c77a447d967c)
* Size: 519 evaluation samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                        | sentence2                                                                         | label                                                         |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            | float                                                         |
  | details | <ul><li>min: 7 tokens</li><li>mean: 18.6 tokens</li><li>max: 61 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 18.16 tokens</li><li>max: 60 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.5</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                                                                     | sentence2                                                                                | label                            |
  |:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:---------------------------------|
  | <code>무엇보다도 호스트분들이 너무 친절하셨습니다.</code>                                                         | <code>무엇보다도, 호스트들은 매우 친절했습니다.</code>                                                     | <code>0.9714285714285713</code>  |
  | <code>주요 관광지 모두 걸어서 이동가능합니다.</code>                                                           | <code>위치는 피렌체 중심가까지 걸어서 이동 가능합니다.</code>                                                 | <code>0.2857142857142858</code>  |
  | <code>학생들의 균형 있는 영어능력을 향상시킬 수 있는 학교 수업을 유도하기 위해 2018학년도 수능부터 도입된 영어 영역 절대평가는 올해도 유지한다.</code> | <code>영어 영역의 경우 학생들이 한글 해석본을 암기하는 문제를 해소하기 위해 2016학년도부터 적용했던 EBS 연계 방식을 올해도 유지한다.</code> | <code>0.25714285714285723</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `num_train_epochs`: 10
- `warmup_ratio`: 0.1
- `fp16`: True
- `load_best_model_at_end`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 10
- `max_steps`: -1
- `lr_scheduler_type`: linear
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
- `bf16`: False
- `fp16`: True
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
- `load_best_model_at_end`: True
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
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | loss   | sts-dev_spearman_cosine |
|:------:|:----:|:-------------:|:------:|:-----------------------:|
| 0      | 0    | -             | -      | 0.2874                  |
| 0.0109 | 1    | 0.1046        | -      | -                       |
| 0.5435 | 50   | 0.0703        | 0.0605 | 0.6007                  |
| 1.0870 | 100  | 0.0203        | 0.0340 | 0.8140                  |
| 1.6304 | 150  | 0.0118        | 0.0304 | 0.8342                  |
| 2.1739 | 200  | 0.0094        | 0.0298 | 0.8480                  |
| 2.7174 | 250  | 0.0054        | 0.0311 | 0.8503                  |
| 3.2609 | 300  | 0.0048        | 0.0303 | 0.8488                  |
| 3.8043 | 350  | 0.0043        | 0.0307 | 0.8526                  |
| 4.3478 | 400  | 0.0035        | 0.0305 | 0.8515                  |
| 4.8913 | 450  | 0.0033        | 0.0302 | 0.8513                  |
| 5.4348 | 500  | 0.0028        | 0.0306 | 0.8546                  |


### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 3.0.1
- Transformers: 4.41.2
- PyTorch: 2.0.1
- Accelerate: 0.31.0
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