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
- source_sentence: 6단계 조치결과 등 보고 단계의 경우 관계기관은 담당자 현황 및 경보 조치결과를 작성·보고한다.
  sentences:
  - 6단계 조치결과 등 보고단계의 경우 해당 기관은 담당자의 현황 및 경보조치 결과를 작성하여 보고해야 합니다.
  - 거실에 있는 집주인의 친절한 안내문을 놓치지 마세요.
  - 원칙적으로, 학생들의 평가는 그들이 원격 수업에서 배운 것을 바탕으로 방과 후에 실시될 것입니다.
- source_sentence: 또 숙소가 상가 내에 위치하여 저녁에는 아주 조용합니다.
  sentences:
  - 메일을 보내기 전엔 바로 보내지 말고 내용을 두 번 체크해봐.
  - 특히, 옥상에서 열린 새해 불꽃놀이는 환상적이었습니다.
  - 또한, 그 숙소는 쇼핑몰에 위치해 있어서 저녁에는 매우 조용합니다.
- source_sentence: 영하의 날씨에는 얇게 입고 나가면 안돼.
  sentences:
  - 특히 2가족 이상 여행객들에게 좋을 것 같습니다.
  - 검색해줘. 오늘 최고 기온이 삼십도 이상일지 이하일지.
  - 거장들의 공연을 부담 없이 즐길 수 있다는 점을 긍정적으로 언급했다.
- source_sentence: 침실에 누웠을 때 보이는 도루강 뷰는 정말 좋았어요.
  sentences:
  - 지리적위치와 침대 매트리스는 정말 좋았어요.
  - 이번 년도에는 어느 도시에서 단풍이 처음 피나요?
  - 편의시설은 근처에 대형마트와 12시까지 하는 소형마트도 있어서 편리합니다.
- source_sentence: 네이버 메일을 사람들이 주로 사용하게 된 계기가 무엇일까?
  sentences:
  - 농협카드 청구서가 메일로 왔는데 어떻게 여는지 알려줘
  - 혹시 거실 말고 안방은 로봇청소기로 어떻게 해야할지 아시나요?
  - 자외선 강할 때에는 다른 것 말고 선글라스 쓰기를 권합니다.
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
      value: 0.3477071661197065
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.35560473197486514
      name: Spearman Cosine
    - type: pearson_cosine
      value: 0.9614354401976586
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9219302243151195
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
    '네이버 메일을 사람들이 주로 사용하게 된 계기가 무엇일까?',
    '농협카드 청구서가 메일로 왔는데 어떻게 여는지 알려줘',
    '혹시 거실 말고 안방은 로봇청소기로 어떻게 해야할지 아시나요?',
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
| pearson_cosine      | 0.9614     |
| **spearman_cosine** | **0.9219** |

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
  | details | <ul><li>min: 6 tokens</li><li>mean: 19.56 tokens</li><li>max: 59 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 19.39 tokens</li><li>max: 64 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.45</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                          | sentence_1                                          | label                           |
  |:----------------------------------------------------|:----------------------------------------------------|:--------------------------------|
  | <code>여름 낮시간은 너무 더우니까 약속을 잡지 맙시다.</code>            | <code>여름 낮에 약속 잡을 생각은 아예 하지 않도록 하십시오.</code>        | <code>0.58</code>               |
  | <code>예전처럼 잊지 말고 부모님과 한 약속은 지키도록 노력하셨으면 합니다.</code> | <code>부모님과 한 약속은 갑자기 변경하지 말고 지키기 위해 노력해주십시오.</code> | <code>0.6599999999999999</code> |
  | <code>야 새벽 아니고 낮이니까 조명등 밝기 좀 낮춰서 쓰자</code>          | <code>너희가 좋아한다는 그 라디오 방송 채널 이름이 뭐니</code>           | <code>0.0</code>                |
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
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch  | Step | Training Loss | spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|
| -1     | -1   | -             | 0.3556          |
| 0.7610 | 500  | 0.0271        | -               |
| 1.0    | 657  | -             | 0.9144          |
| 1.5221 | 1000 | 0.0081        | 0.9165          |
| 2.0    | 1314 | -             | 0.9183          |
| 2.2831 | 1500 | 0.0049        | -               |
| 3.0    | 1971 | -             | 0.9194          |
| 3.0441 | 2000 | 0.0035        | 0.9200          |
| 3.8052 | 2500 | 0.0026        | -               |
| 4.0    | 2628 | -             | 0.9219          |


### Framework Versions
- Python: 3.12.9
- Sentence Transformers: 4.0.1
- Transformers: 4.51.0
- PyTorch: 2.6.0+cu126
- Accelerate: 1.6.0
- Datasets: 3.5.0
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