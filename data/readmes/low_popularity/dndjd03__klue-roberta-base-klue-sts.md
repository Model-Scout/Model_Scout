---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10501
- loss:CosineSimilarityLoss
base_model: klue/roberta-base
widget:
- source_sentence: 가급적이면 에어컨보단 선풍기를 쓰자
  sentences:
  - 가습기말고 에어컨을 꼭 필요할때만 켜자
  - 우선, 숙소와 침대에 좋은 향기가 있어서 기분이 좋았습니다.
  - 부엌을 이용하시려는 분들은 참고하시기 바랍니다.
- source_sentence: 시스템반도체 분야에서는 고성능 반도체 설계자산(IP) 개발·판매 기업인 ‘오픈엣지 테크놀로지’가 성과를 발표했다.
  sentences:
  - 유리 테이블은 사실 꽤 컸습니다.
  - 지진 발생 시에는 건물 안에 있지 말고 건물 밖으로 피신하십시오.
  - 시스템 반도체 분야에서는 고성능 반도체 설계자산(IP)을 개발, 판매하는 '오픈 에지 테크놀로지'가 그 결과를 발표했습니다.
- source_sentence: 약속을 저녁에 잡을 때는 여러개를 하지말고 하나만 잡게나.
  sentences:
  - fif 확진환자의 증상중 확진환자와 밀접하게 접촉한 후 14일 이내에 발열 또는 호흡기 증상(기침, 인후염 등)을 경험하는 사람
  - 저녁에는 많은 약속들을 잡기 보다는 하나만 잡으세요.
  - 특히 부엌과 편안한 침실은 완벽했습니다.
- source_sentence: 지역사랑상품권은 카드·모바일형은 만원 단위로, 종이 형태는 최소 권종 안에서 기부금액을 정하면 된다.
  sentences:
  - 또 이달 말부터 감염병전담병원은 시설·장비비, 인건비 및 운영비를, 국가지정 입원치료병상과 중증환자 긴급치료 병상을 운영 중인 의료기관은 장비와
    운영비를 지원받게 된다.
  - 로컬 숙소의 모습 그대로를 느낄 수 있다.
  - 할인 기준은 8만원 이상 결제 시 30,000원 환불입니다.
- source_sentence: 아울러 종목단체가 주중에 개최하는 대회 건수도 연차별로 줄어들고, 진천선수촌 내 학습지원센터를 통한 국가대표 학생선수의
    학습 지원도 강화될 것으로 예상된다.
  sentences:
  - 또한 체육단체들의 주중 대회 개최 건수는 매년 줄어들 것으로 예상되며, 진천선수촌 학습지원센터를 통한 전국 학생선수 지원도 강화될 예정입니다.
  - 무엇보다도, 그 장소는 관광하기에 매우 좋았습니다.
  - 지급형태별 신청 가구는 누적 기준으로 신용·체크카드 충전이 1303만 가구로 전체의 60%를 차지했다.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
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
      value: 0.34770713905843553
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
    - type: pearson_cosine
      value: 0.9614639025976739
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9198721684765138
      name: Spearman Cosine
---

# SentenceTransformer based on klue/roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [klue/roberta-base](https://huggingface.co/klue/roberta-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [klue/roberta-base](https://huggingface.co/klue/roberta-base) <!-- at revision 02f94ba5e3fcb7e2a58a390b8639b0fac974a8da -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'RobertaModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
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
    '아울러 종목단체가 주중에 개최하는 대회 건수도 연차별로 줄어들고, 진천선수촌 내 학습지원센터를 통한 국가대표 학생선수의 학습 지원도 강화될 것으로 예상된다.',
    '또한 체육단체들의 주중 대회 개최 건수는 매년 줄어들 것으로 예상되며, 진천선수촌 학습지원센터를 통한 전국 학생선수 지원도 강화될 예정입니다.',
    '무엇보다도, 그 장소는 관광하기에 매우 좋았습니다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.7620, 0.0771],
#         [0.7620, 1.0000, 0.0525],
#         [0.0771, 0.0525, 1.0000]])
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

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.3477     |
| **spearman_cosine** | **0.3556** |

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.9615     |
| **spearman_cosine** | **0.9199** |

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
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                        | sentence_1                                                                        | label                                                          |
  |:---------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type     | string                                                                            | string                                                                            | float                                                          |
  | modality | text                                                                              | text                                                                              |                                                                |
  | details  | <ul><li>min: 8 tokens</li><li>mean: 18.56 tokens</li><li>max: 45 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 18.75 tokens</li><li>max: 58 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.41</li><li>max: 0.9</li></ul> |
* Samples:
  | sentence_0                                       | sentence_1                                        | label                           |
  |:-------------------------------------------------|:--------------------------------------------------|:--------------------------------|
  | <code>근처 유명한 관광지는 15분 내에 움직 일 수 있었던 것 같아요</code> | <code>15분만에 근처의 유명한 관광지를 여행할 수 있었던 것 같아요.</code>  | <code>0.82</code>               |
  | <code>위치가 중심가와 가깝고 호스트의 답변이 신속합니다.</code>        | <code>위치가 좋고 호스트님과의 연락이 훌륭해요.</code>              | <code>0.6799999999999999</code> |
  | <code>지메일 자동완성 기능의 성능에 대해 평가해줘</code>            | <code>트위치 계정을 다른 것보다 특히 페이스북과 연동하는 것을 추천해.</code> | <code>0.0</code>                |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss",
      "cos_score_transformation": "torch.nn.modules.linear.Identity"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 4
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
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
- `lr_scheduler_kwargs`: None
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
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
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
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
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
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|
| -1     | -1   | -             | 0.3556          |
| 0.7610 | 500  | 0.0268        | -               |
| 1.0    | 657  | -             | 0.9097          |
| 1.5221 | 1000 | 0.0082        | 0.9102          |
| 2.0    | 1314 | -             | 0.9154          |
| 2.2831 | 1500 | 0.0052        | -               |
| 3.0    | 1971 | -             | 0.9184          |
| 3.0441 | 2000 | 0.0035        | 0.9185          |
| 3.8052 | 2500 | 0.0025        | -               |
| 4.0    | 2628 | -             | 0.9199          |


### Training Time
- **Training**: 15.4 minutes

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 5.5.1
- Transformers: 4.57.6
- PyTorch: 2.11.0+cu128
- Accelerate: 1.13.0
- Datasets: 5.0.0
- Tokenizers: 0.22.2

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