---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:10501
- loss:CosineSimilarityLoss
base_model: klue/roberta-base
widget:
- source_sentence: 니 생각엔 어떤 방법이 거실 청소를 할 때에 가장 효과적일 것 같아?
  sentences:
  - 너가 생각하기에 거실 청소하는데 가장 효과적인 방법은 뭐야?
  - 숙소가 청결한 점이 가장 마음에 들었습니다.
  - 요즘 시간 떼우기에 좋은 오락프로그램이 뭐야?
- source_sentence: 엄청 깨끗하고 신축건물같은 느낌이 든다.
  sentences:
  - 집은 깨끗하고 집주인은 매우 친절합니다.
  - 뉴스 채널에서 채널 바꾸는거 금지야
  - 그것은 매우 깨끗하고 새로운 건물처럼 느껴집니다.
- source_sentence: 주택가에 있어서 밤에 굉장히 조용합니다.
  sentences:
  - 선풍기 조정하는 명령어 중에 풍향을 조정하기 위한 명령어는 뭐니?
  - 아토차역에서 9분 정도 떨어진 주택가에 위치해서 굉장히 조용합니다.
  - 세계 인구와 무역 규모가 전 세계에서 차지하는 비중이 30%에 달하는 세계 최대 FTA(자유무역협정) 시장이 탄생했다.
- source_sentence: 이번 사업 대상지로 선정된 실외정원은 평택역, 육군 특전사령부, 공주대학교 천안캠퍼스, 전북대학교병원, 목포대학교
    등 5곳이다.
  sentences:
  - 이 프로젝트에 선정된 다섯 개의 야외 정원은 평택역, 육군 특전사령부, 공주대학교 천안 캠퍼스, 전북대학교 병원, 목포대학교입니다.
  - 한편, 주요 및 일반 관리 시설에는 포함되지 않은 박물관, 도서관, 미술관 등 실내 다중 사용 시설에서는 마스크를 착용하는 것이 의무화될 것입니다.
  - 낮에 조명등 켜놓는 건 금지되어있어
- source_sentence: 한편 국회는 이날 코로나19 국면에서 민생·경제 피해 최소화를 위한 세제 지원 내용을 담은 ‘조세특례제한법’ 개정안도
    통과시켰다.
  sentences:
  - 기획재정부는 8일 국무회의에서 이같은 내용을 담은 ‘2021년도 예산배정계획’을 확정했다.
  - 다운타운까지 30분도 안걸리고 공항은 물론 빅토리아까지 가는 페리 터미널에 가기도 편리합니다.
  - 겨울에 누구 만나려면 어디서 보는 게 좋아?
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
      value: 0.34770711920109076
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
    - type: pearson_cosine
      value: 0.9616011157938198
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9219703093701542
      name: Spearman Cosine
---

# SentenceTransformer based on klue/roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [klue/roberta-base](https://huggingface.co/klue/roberta-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [klue/roberta-base](https://huggingface.co/klue/roberta-base) <!-- at revision 02f94ba5e3fcb7e2a58a390b8639b0fac974a8da -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False, 'architecture': 'RobertaModel'})
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
    '한편 국회는 이날 코로나19 국면에서 민생·경제 피해 최소화를 위한 세제 지원 내용을 담은 ‘조세특례제한법’ 개정안도 통과시켰다.',
    '기획재정부는 8일 국무회의에서 이같은 내용을 담은 ‘2021년도 예산배정계획’을 확정했다.',
    '다운타운까지 30분도 안걸리고 공항은 물론 빅토리아까지 가는 페리 터미널에 가기도 편리합니다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.0080, -0.0047],
#         [ 0.0080,  1.0000, -0.0492],
#         [-0.0047, -0.0492,  1.0000]])
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

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.3477     |
| **spearman_cosine** | **0.3556** |

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| pearson_cosine      | 0.9616    |
| **spearman_cosine** | **0.922** |

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
  | details | <ul><li>min: 6 tokens</li><li>mean: 20.26 tokens</li><li>max: 53 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 19.63 tokens</li><li>max: 54 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.46</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                             | sentence_1                                         | label             |
  |:---------------------------------------|:---------------------------------------------------|:------------------|
  | <code>가격도 저렴한데 위치나 시설도 우수합니다.</code>   | <code>비싼 오스트리아 물가에 비해 가격도 너무나 저렴합니다.</code>        | <code>0.36</code> |
  | <code>태풍 경로를 지나지 말고 피해서 여행하십시오.</code> | <code>높을지 낮을지 알려주세요. 미세먼지 농도.</code>               | <code>0.0</code>  |
  | <code>다만 여러 게스트가 화장실을 하나 공유하다</code>   | <code>게스트의 친절한 안내가 인상적이었음.  처음으로 해외민박을 이용하다</code> | <code>0.12</code> |
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
| 0.7610 | 500  | 0.027         | -               |
| 1.0    | 657  | -             | 0.9102          |
| 1.5221 | 1000 | 0.0081        | 0.9133          |
| 2.0    | 1314 | -             | 0.9175          |
| 2.2831 | 1500 | 0.0051        | -               |
| 3.0    | 1971 | -             | 0.9220          |


### Framework Versions
- Python: 3.13.5
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.8.0
- Accelerate: 1.11.0
- Datasets: 4.3.0
- Tokenizers: 0.22.1

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