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
- source_sentence: 숙소가 지하라는 사실이 맘에 안들었다,
  sentences:
  - 숙소가 지하에 있다는 사실이 마음에 들지 않았어요.
  - 2006년 첫 콜마 BNH가 설립된 이후 14년 만에 연구소기업들이 900개를 돌파했습니다.
  - 그 방은 제가 사진에서 본 것과 똑같아서 가격에 아주 좋습니다.
- source_sentence: 침실은 최대 4인이라고 합니다만, 3인이 적당합니다.
  sentences:
  - 내일 골프 치기로 약속한 곳이 어디인지 아니?
  - 그들은 매우 아름답고 멋진 친구들이에요.
  - 피렌체에서 가장 좋은 집이라고 확신합니다.
- source_sentence: 부모님 결혼기념일이 언제였더라?
  sentences:
  - 또한 의료인이 코딩 없이 인공지능 연구를 수행할 수 있는 자체 플랫폼을 통해 의료 인공지능 기술 향상을 촉진할 수 있도록 지원하였습니다.
  - 야구 경기 보러 언제 가냐?
  - 가장 중요한 숙소의 위치는 공항버스에서 하차하면 바로 앞에 건물이 보입니다.
- source_sentence: 여기 집안에 불 켜진 곳 있나?
  sentences:
  - 누나, 안방 온도 이십오도와 삼십도 중에 얼마로 하고싶어?
  - 그리고 저는 세 사람이 함께 살기에 따뜻한 물이 충분하지 않다고 생각해요.
  - 지금까지 가본 호텔보다 더 좋은 숙소였습니다.
- source_sentence: 저는 어릴때부터 파리를 방문하는 게 꿈이었어요.
  sentences:
  - 파리를 충분히 즐길수 있는 멋진 공간이였어요.
  - 결혼식 여자친구랑 올렸던게 언제였지?
  - 주로 대중음악인들과 실시간 온라인 소통에 대한 만족을 표했다.
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
      value: 0.3477071155282182
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
    - type: pearson_cosine
      value: 0.96186103743537
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9233906600158011
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
    '저는 어릴때부터 파리를 방문하는 게 꿈이었어요.',
    '파리를 충분히 즐길수 있는 멋진 공간이였어요.',
    '결혼식 여자친구랑 올렸던게 언제였지?',
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

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.3477     |
| **spearman_cosine** | **0.3556** |

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.9619     |
| **spearman_cosine** | **0.9234** |

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
  | details | <ul><li>min: 5 tokens</li><li>mean: 20.69 tokens</li><li>max: 70 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 19.89 tokens</li><li>max: 64 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.45</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                        | sentence_1                                                                        | label             |
  |:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:------------------|
  | <code>다른 메일함 말고 스팸메일함에서 쇼핑몰 메일을 저장해줘.</code>                                      | <code>스팸메일함에서 다른 메일은 무시하고 쇼핑몰 메일만 저장해주세요.</code>                                  | <code>0.72</code> |
  | <code>또 온누리상품권 1인 구매 한도도 70만원에서 100만원으로 확대하고 총 발행규모도 2조5000억원에서 3조원으로 늘린다.</code> | <code>또한 온누리상품권 구매 한도가 70만원에서 100만원으로 확대되며 발행 총액은 2조 5000억원에서 3조원으로 확대됩니다.</code> | <code>0.86</code> |
  | <code>비옷과 우산 중 당신이 원하는 것을 말해주십시오.</code>                                          | <code>어디입니까? 태풍이 발생되는 곳은.</code>                                                  | <code>0.0</code>  |
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

</details>

### Training Logs
| Epoch  | Step | Training Loss | spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|
| 0      | 0    | -             | 0.3556          |
| 0.7610 | 500  | 0.0289        | -               |
| 1.0    | 657  | -             | 0.9094          |
| 1.5221 | 1000 | 0.0078        | 0.9189          |
| 2.0    | 1314 | -             | 0.9166          |
| 2.2831 | 1500 | 0.0051        | -               |
| 3.0    | 1971 | -             | 0.9213          |
| 3.0441 | 2000 | 0.0034        | 0.9222          |
| 3.8052 | 2500 | 0.0025        | -               |
| 4.0    | 2628 | -             | 0.9234          |


### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.3.1
- Transformers: 4.57.3
- PyTorch: 2.9.0+cu128
- Accelerate: 1.12.0
- Datasets: 3.2.0
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