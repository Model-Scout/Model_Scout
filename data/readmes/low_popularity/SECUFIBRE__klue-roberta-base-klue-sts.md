---
language:
- ko
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10501
- loss:CosineSimilarityLoss
base_model: klue/roberta-base
widget:
- source_sentence: 청결도, 화장실청소상태,방분위기 모두 훌륭했습니다.
  sentences:
  - 체크인, 청소 및 고객서비스는 모두 훌륭했습니다.
  - 냉장고 문 여는 건 좀 아닌거같애
  - 체크인하고 체크아웃하는 것이 조금 불편했습니다.
- source_sentence: 변비를 예방하고 싶으면 아침 운동은 거르지 말도록 하렴.
  sentences:
  - 만약 당신이 호스트가 구글에서 당신에게 알려준 주소를 찾는다면, 당신은 같은 호수에 있는 호텔을 찾을 수 있을 것입니다.
  - 건설근로자공제회 지점은 서울, 경기, 인천, 부산, 대구, 광주, 대전에 있으며, 센터는 구로, 원주, 의정부, 창원, 안동, 전주, 제주,
    청주에 위치하고 있습니다.
  - 처음 뵐 때 가기 좋을 만한 공간 어디 없습니까?
- source_sentence: 메일이 몇 통까지 받은 메일함에 저장되는지 아세요?
  sentences:
  - 또한 공연 취소로 어려움을 겪고 있는 200개의 공연예술소극장당 제작비와 홍보비도 최대 6000만원까지 지원할 계획입니다.
  - 받은 메일함에 최대로 들어갈 수 있는 메일 수는?
  - 지난 9일 국회 본회의를 통과한 기초연금법, 장애인연금법, 국민연금법의 주요 내용, 기대효과, 향후 계획 등을 살펴봅니다.
- source_sentence: 좋은 위치, 편리한 교통, 친절한 호스트 모든걸 다 갖췄습니다.
  sentences:
  - 여름철 수영 전 잊지 말고 준비운동 해줘.
  - 제가 여태까지 써 본 에어비앤비 중에 최고였어요!
  - 좋은 위치에, 탁트인 전망에 너무 좋았습니다.
- source_sentence: 보일러로 난방하는 방법 좀 알려줘
  sentences:
  - 당신이 좋아하는 뉴스 채널이 뭐였더라?
  - 그리고 숙소 올라가는 길에 계단 조금 있어요
  - 보일러 켜는 방법 좀 설명해줘
datasets:
- klue/klue
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
co2_eq_emissions:
  emissions: 5.747781269519202
  energy_consumed: 0.013134723491938343
  source: codecarbon
  training_type: fine-tuning
  on_cloud: false
  cpu_model: Intel(R) Core(TM) i7-14700K
  ram_total_size: 62.505760192871094
  hours_used: 0.036
  hardware_used: 1 x NVIDIA GeForce RTX 4090
model-index:
- name: SentenceTransformer based on klue/roberta-base
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts test
      type: sts-test
    metrics:
    - type: pearson_cosine
      value: 0.3477071661197065
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts eval
      type: sts-eval
    metrics:
    - type: pearson_cosine
      value: 0.9607715158140949
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9196062588633074
      name: Spearman Cosine
---

# SentenceTransformer based on klue/roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [klue/roberta-base](https://huggingface.co/klue/roberta-base) on the [klue](https://huggingface.co/datasets/klue) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [klue/roberta-base](https://huggingface.co/klue/roberta-base) <!-- at revision 02f94ba5e3fcb7e2a58a390b8639b0fac974a8da -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [klue](https://huggingface.co/datasets/klue)
- **Language:** ko
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
    '보일러로 난방하는 방법 좀 알려줘',
    '보일러 켜는 방법 좀 설명해줘',
    '당신이 좋아하는 뉴스 채널이 뭐였더라?',
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

* Datasets: `sts-test` and `sts-eval`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | sts-test   | sts-eval   |
|:--------------------|:-----------|:-----------|
| pearson_cosine      | 0.3477     | 0.9608     |
| **spearman_cosine** | **0.3556** | **0.9196** |

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

#### klue

* Dataset: [klue](https://huggingface.co/datasets/klue) at [349481e](https://huggingface.co/datasets/klue/tree/349481ec73fff722f88e0453ca05c77a447d967c)
* Size: 10,501 training samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                         | sentence2                                                                         | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 6 tokens</li><li>mean: 20.29 tokens</li><li>max: 58 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 19.81 tokens</li><li>max: 55 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.45</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                    | sentence2                                | label                           |
  |:---------------------------------------------|:-----------------------------------------|:--------------------------------|
  | <code>시설은 좋으나 잠자리 민감하신 분들은 다른 곳으로 가세요</code> | <code>시설도 좋지만, 잠자리라면 다른 곳으로 가보세요.</code> | <code>0.6799999999999999</code> |
  | <code>유럽 에어비엔비 숙소 중에서 제일 잘 터졌습니다!</code>     | <code>유럽에서 가장 좋은 호텔이에요!</code>           | <code>0.38</code>               |
  | <code>고모가 원하는게 볼륨 이단계야 삼단계야?</code>          | <code>에어컨 사용료로 이번 달 얼마 정도 내야하나요?</code>  | <code>0.0</code>                |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Evaluation Dataset

#### klue

* Dataset: [klue](https://huggingface.co/datasets/klue) at [349481e](https://huggingface.co/datasets/klue/tree/349481ec73fff722f88e0453ca05c77a447d967c)
* Size: 1,167 evaluation samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                         | sentence2                                                                         | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 6 tokens</li><li>mean: 19.99 tokens</li><li>max: 62 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 19.26 tokens</li><li>max: 64 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.45</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                 | sentence2                                        | label                           |
  |:------------------------------------------|:-------------------------------------------------|:--------------------------------|
  | <code>4인은 멀티탭을 1개 준비하시면 편할것입니다.</code>    | <code>멀티탭 1개를 준비하시면 4명이 편리하게 이용하실 수 있습니다.</code> | <code>0.6799999999999999</code> |
  | <code>청결도, 화장실청소상태,방분위기 모두 훌륭했습니다.</code> | <code>체크인, 청소 및 고객서비스는 모두 훌륭했습니다.</code>         | <code>0.26</code>               |
  | <code>심지어 사진보다 조금 넓었던 것 같다.</code>        | <code>그것은 심지어 사진보다 조금 더 넓었습니다.</code>            | <code>0.8</code>                |
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
- `warmup_steps`: 100
- `remove_unused_columns`: False

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
- `max_grad_norm`: 1.0
- `num_train_epochs`: 4
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 100
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
- `remove_unused_columns`: False
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `tp_size`: 0
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
- `hub_private_repo`: None
- `hub_always_push`: False
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
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | Validation Loss | sts-test_spearman_cosine | sts-eval_spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|:------------------------:|:------------------------:|
| -1     | -1   | -             | -               | 0.3556                   | -                        |
| 0.7610 | 500  | 0.0272        | -               | -                        | -                        |
| 1.5221 | 1000 | 0.0095        | 0.0172          | -                        | 0.9120                   |
| 2.2831 | 1500 | 0.0059        | -               | -                        | -                        |
| 3.0441 | 2000 | 0.004         | 0.0146          | -                        | 0.9196                   |
| 3.8052 | 2500 | 0.0025        | -               | -                        | -                        |


### Environmental Impact
Carbon emissions were measured using [CodeCarbon](https://github.com/mlco2/codecarbon).
- **Energy Consumed**: 0.013 kWh
- **Carbon Emitted**: 0.006 kg of CO2
- **Hours Used**: 0.036 hours

### Training Hardware
- **On Cloud**: No
- **GPU Model**: 1 x NVIDIA GeForce RTX 4090
- **CPU Model**: Intel(R) Core(TM) i7-14700K
- **RAM Size**: 62.51 GB

### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 4.0.1
- Transformers: 4.50.2
- PyTorch: 2.6.0+cu124
- Accelerate: 0.34.1
- Datasets: 2.19.1
- Tokenizers: 0.21.1

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