---
language:
- en
- multilingual
- ar
- bg
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- ka
- ko
- ku
- lt
- lv
- mk
- mn
- mr
- ms
- my
- nb
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- th
- tr
- uk
- ur
- vi
- zh
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:404981
- loss:MSELoss
base_model: FacebookAI/xlm-roberta-base
widget:
- source_sentence: It's not negative; it's positive.
  sentences:
  - Las partes en conflicto también deben estar preparadas para volver a la mesa de
    negociación si se estanca la implementación del acuerdo.
  - A veces refieren a él como al Campo de Prisioneros de Guerra Número 334, lugar
    donde viven ahora los lakota.
  - No es negativo, es positivo.
- source_sentence: So the first of the three is design for education.
  sentences:
  - El primer enfoque es diseñar para la educación.
  - Las enfermedades cardiacas y  cardiovasculares siguen matando a más gente, no
    sólo en  este país sino también en todo el mundo, que cualquier  otra combinación
    de lo demás, sin embargo casi todos  podemos prevenirlo por completo.
  - Siempre que discutimos uno de estos problemas que tenemos que abordar... el trabajo
    infantil en las granjas de algodón de India, este año vamos a monitorear 50.000
    granjas de algodón en India.
- source_sentence: So take a look around this auditorium today.
  sentences:
  - Lo dispuesto en el acuerdo puede ser complejo, pero también lo es el conflicto
    subyacente.
  - Y puedo ver que algo más murió allí en el fango sangriento y fue enterrado en
    la tormenta de nieve.
  - Miremos alrededor, en este auditorio.
- source_sentence: Every time he has visitors, it's the first place that he takes
    them.
  sentences:
  - Siempre que tiene visitas es el primer lugar al que los lleva.
  - El desempleo en la reserva aborigen de Pine Ridge fluctúa entre el 85% y el 90%.
  - Si la conexión es débil, los motores se quedarán apagados y la mosca seguirá derecho
    en su curso.
- source_sentence: We need a different machine.
  sentences:
  - Vayan al sitio web. Vean los resultados de las auditorías.
  - Necesitamos una máquina diferente.
  - Entonces, ¿dónde nos deja esto?
datasets:
- sentence-transformers/parallel-sentences-talks
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- negative_mse
- src2trg_accuracy
- trg2src_accuracy
- mean_accuracy
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on FacebookAI/xlm-roberta-base
  results:
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en es
      type: en-es
    metrics:
    - type: negative_mse
      value: -10.183618545532227
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en es
      type: en-es
    metrics:
    - type: src2trg_accuracy
      value: 0.9878787878787879
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.990909090909091
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.9893939393939395
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 es en test
      type: sts17-es-en-test
    metrics:
    - type: pearson_cosine
      value: 0.7671256411244319
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.790302203590485
      name: Spearman Cosine
---

# SentenceTransformer based on FacebookAI/xlm-roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) on the [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) <!-- at revision e73636d4f797dec63c3081bb6ed5c7b0bb3f2089 -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
- **Languages:** en, multilingual, ar, bg, ca, cs, da, de, el, es, et, fa, fi, fr, gl, gu, he, hi, hr, hu, hy, id, it, ja, ka, ko, ku, lt, lv, mk, mn, mr, ms, my, nb, nl, pl, pt, ro, ru, sk, sl, sq, sr, sv, th, tr, uk, ur, vi, zh
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
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
model = SentenceTransformer("vallabh001/xlm-roberta-base-multilingual-en-es")
# Run inference
sentences = [
    'We need a different machine.',
    'Necesitamos una máquina diferente.',
    'Entonces, ¿dónde nos deja esto?',
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

#### Knowledge Distillation

* Dataset: `en-es`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-10.1836** |

#### Translation

* Dataset: `en-es`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.9879     |
| trg2src_accuracy  | 0.9909     |
| **mean_accuracy** | **0.9894** |

#### Semantic Similarity

* Dataset: `sts17-es-en-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.7671     |
| **spearman_cosine** | **0.7903** |

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

#### en-es

* Dataset: [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [0c70bc6](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/0c70bc6714efb1df12f8a16b9056e4653563d128)
* Size: 404,981 training samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.77 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 25.42 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                | non_english                                                                                                                              | label                                                                                                                        |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>And then there are certain conceptual things that can also benefit from hand calculating, but I think they're relatively small in number.</code> | <code>Y luego hay ciertas aspectos conceptuales que pueden beneficiarse del cálculo a mano pero creo que son relativamente pocos.</code> | <code>[-0.59398353099823, 0.9714106321334839, 0.6800687313079834, -0.21585586667060852, -0.7509507536888123, ...]</code>     |
  | <code>One thing I often ask about is ancient Greek and how this relates.</code>                                                                        | <code>Algo que pregunto a menudo es sobre el griego antiguo y cómo se relaciona.</code>                                                  | <code>[-0.09777131676673889, 0.07093200832605362, -0.42989036440849304, -0.1457505226135254, 1.4382765293121338, ...]</code> |
  | <code>See, the thing we're doing right now is we're forcing people to learn mathematics.</code>                                                        | <code>Vean, lo que estamos haciendo ahora es forzar a la gente a aprender matemáticas.</code>                                            | <code>[0.39432215690612793, 0.1891053169965744, -0.3788300156593323, 0.438666433095932, 0.2727019190788269, ...]</code>      |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Evaluation Dataset

#### en-es

* Dataset: [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [0c70bc6](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/0c70bc6714efb1df12f8a16b9056e4653563d128)
* Size: 990 evaluation samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 990 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 26.42 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 26.47 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                    | non_english                                                                                                                                                       | label                                                                                                                       |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
  | <code>Thank you so much, Chris.</code>                                                                                                                     | <code>Muchas gracias Chris.</code>                                                                                                                                | <code>[-0.43312570452690125, 1.0602686405181885, -0.07791059464216232, -0.41704198718070984, 1.676845908164978, ...]</code> |
  | <code>And it's truly a great honor to have the opportunity to come to this stage twice; I'm extremely grateful.</code>                                     | <code>Y es en verdad un gran honor tener la oportunidad de venir a este escenario por segunda vez. Estoy extremadamente agradecido.</code>                        | <code>[0.27005693316459656, 0.5391747951507568, -0.2580487132072449, -0.6613675951957703, 0.6738824248313904, ...]</code>   |
  | <code>I have been blown away by this conference, and I want to thank all of you for the many nice comments about what I had to say the other night.</code> | <code>He quedado conmovido por esta conferencia, y deseo agradecer a todos ustedes sus amables comentarios acerca de lo que tenía que decir la otra noche.</code> | <code>[-0.2532017230987549, 0.04791336879134178, -0.1317490190267563, -0.7357572913169861, 0.23663584887981415, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `learning_rate`: 2e-05
- `num_train_epochs`: 5
- `warmup_ratio`: 0.1
- `bf16`: True

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
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 5
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
- `bf16`: True
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
<details><summary>Click to expand</summary>

| Epoch  | Step  | Training Loss | en-es loss | en-es_negative_mse | en-es_mean_accuracy | sts17-es-en-test_spearman_cosine |
|:------:|:-----:|:-------------:|:----------:|:------------------:|:-------------------:|:--------------------------------:|
| 0.0158 | 100   | 0.6528        | -          | -                  | -                   | -                                |
| 0.0316 | 200   | 0.5634        | -          | -                  | -                   | -                                |
| 0.0474 | 300   | 0.4418        | -          | -                  | -                   | -                                |
| 0.0632 | 400   | 0.3009        | -          | -                  | -                   | -                                |
| 0.0790 | 500   | 0.2744        | -          | -                  | -                   | -                                |
| 0.0948 | 600   | 0.2677        | -          | -                  | -                   | -                                |
| 0.1106 | 700   | 0.2661        | -          | -                  | -                   | -                                |
| 0.1264 | 800   | 0.2614        | -          | -                  | -                   | -                                |
| 0.1422 | 900   | 0.2583        | -          | -                  | -                   | -                                |
| 0.1580 | 1000  | 0.2582        | -          | -                  | -                   | -                                |
| 0.1738 | 1100  | 0.2579        | -          | -                  | -                   | -                                |
| 0.1896 | 1200  | 0.256         | -          | -                  | -                   | -                                |
| 0.2054 | 1300  | 0.2511        | -          | -                  | -                   | -                                |
| 0.2212 | 1400  | 0.2467        | -          | -                  | -                   | -                                |
| 0.2370 | 1500  | 0.2423        | -          | -                  | -                   | -                                |
| 0.2528 | 1600  | 0.2364        | -          | -                  | -                   | -                                |
| 0.2686 | 1700  | 0.2305        | -          | -                  | -                   | -                                |
| 0.2845 | 1800  | 0.2248        | -          | -                  | -                   | -                                |
| 0.3003 | 1900  | 0.2184        | -          | -                  | -                   | -                                |
| 0.3161 | 2000  | 0.2143        | -          | -                  | -                   | -                                |
| 0.3319 | 2100  | 0.2098        | -          | -                  | -                   | -                                |
| 0.3477 | 2200  | 0.2055        | -          | -                  | -                   | -                                |
| 0.3635 | 2300  | 0.1999        | -          | -                  | -                   | -                                |
| 0.3793 | 2400  | 0.1965        | -          | -                  | -                   | -                                |
| 0.3951 | 2500  | 0.1919        | -          | -                  | -                   | -                                |
| 0.4109 | 2600  | 0.1889        | -          | -                  | -                   | -                                |
| 0.4267 | 2700  | 0.1858        | -          | -                  | -                   | -                                |
| 0.4425 | 2800  | 0.1826        | -          | -                  | -                   | -                                |
| 0.4583 | 2900  | 0.18          | -          | -                  | -                   | -                                |
| 0.4741 | 3000  | 0.1774        | -          | -                  | -                   | -                                |
| 0.4899 | 3100  | 0.1758        | -          | -                  | -                   | -                                |
| 0.5057 | 3200  | 0.1738        | -          | -                  | -                   | -                                |
| 0.5215 | 3300  | 0.1706        | -          | -                  | -                   | -                                |
| 0.5373 | 3400  | 0.1678        | -          | -                  | -                   | -                                |
| 0.5531 | 3500  | 0.1664        | -          | -                  | -                   | -                                |
| 0.5689 | 3600  | 0.1647        | -          | -                  | -                   | -                                |
| 0.5847 | 3700  | 0.163         | -          | -                  | -                   | -                                |
| 0.6005 | 3800  | 0.1605        | -          | -                  | -                   | -                                |
| 0.6163 | 3900  | 0.1594        | -          | -                  | -                   | -                                |
| 0.6321 | 4000  | 0.1576        | -          | -                  | -                   | -                                |
| 0.6479 | 4100  | 0.1561        | -          | -                  | -                   | -                                |
| 0.6637 | 4200  | 0.1541        | -          | -                  | -                   | -                                |
| 0.6795 | 4300  | 0.1545        | -          | -                  | -                   | -                                |
| 0.6953 | 4400  | 0.1535        | -          | -                  | -                   | -                                |
| 0.7111 | 4500  | 0.1523        | -          | -                  | -                   | -                                |
| 0.7269 | 4600  | 0.1502        | -          | -                  | -                   | -                                |
| 0.7427 | 4700  | 0.1487        | -          | -                  | -                   | -                                |
| 0.7585 | 4800  | 0.1486        | -          | -                  | -                   | -                                |
| 0.7743 | 4900  | 0.1477        | -          | -                  | -                   | -                                |
| 0.7901 | 5000  | 0.1465        | 0.1390     | -14.681906         | 0.9803              | 0.6371                           |
| 0.8059 | 5100  | 0.1469        | -          | -                  | -                   | -                                |
| 0.8217 | 5200  | 0.1449        | -          | -                  | -                   | -                                |
| 0.8375 | 5300  | 0.1437        | -          | -                  | -                   | -                                |
| 0.8534 | 5400  | 0.142         | -          | -                  | -                   | -                                |
| 0.8692 | 5500  | 0.1423        | -          | -                  | -                   | -                                |
| 0.8850 | 5600  | 0.1424        | -          | -                  | -                   | -                                |
| 0.9008 | 5700  | 0.1415        | -          | -                  | -                   | -                                |
| 0.9166 | 5800  | 0.1407        | -          | -                  | -                   | -                                |
| 0.9324 | 5900  | 0.1396        | -          | -                  | -                   | -                                |
| 0.9482 | 6000  | 0.1388        | -          | -                  | -                   | -                                |
| 0.9640 | 6100  | 0.1391        | -          | -                  | -                   | -                                |
| 0.9798 | 6200  | 0.1368        | -          | -                  | -                   | -                                |
| 0.9956 | 6300  | 0.1366        | -          | -                  | -                   | -                                |
| 1.0114 | 6400  | 0.1367        | -          | -                  | -                   | -                                |
| 1.0272 | 6500  | 0.1343        | -          | -                  | -                   | -                                |
| 1.0430 | 6600  | 0.1341        | -          | -                  | -                   | -                                |
| 1.0588 | 6700  | 0.1349        | -          | -                  | -                   | -                                |
| 1.0746 | 6800  | 0.1327        | -          | -                  | -                   | -                                |
| 1.0904 | 6900  | 0.1334        | -          | -                  | -                   | -                                |
| 1.1062 | 7000  | 0.133         | -          | -                  | -                   | -                                |
| 1.1220 | 7100  | 0.1316        | -          | -                  | -                   | -                                |
| 1.1378 | 7200  | 0.1308        | -          | -                  | -                   | -                                |
| 1.1536 | 7300  | 0.1316        | -          | -                  | -                   | -                                |
| 1.1694 | 7400  | 0.1298        | -          | -                  | -                   | -                                |
| 1.1852 | 7500  | 0.1294        | -          | -                  | -                   | -                                |
| 1.2010 | 7600  | 0.1295        | -          | -                  | -                   | -                                |
| 1.2168 | 7700  | 0.13          | -          | -                  | -                   | -                                |
| 1.2326 | 7800  | 0.1285        | -          | -                  | -                   | -                                |
| 1.2484 | 7900  | 0.1278        | -          | -                  | -                   | -                                |
| 1.2642 | 8000  | 0.1272        | -          | -                  | -                   | -                                |
| 1.2800 | 8100  | 0.1262        | -          | -                  | -                   | -                                |
| 1.2958 | 8200  | 0.1275        | -          | -                  | -                   | -                                |
| 1.3116 | 8300  | 0.1266        | -          | -                  | -                   | -                                |
| 1.3274 | 8400  | 0.1252        | -          | -                  | -                   | -                                |
| 1.3432 | 8500  | 0.1256        | -          | -                  | -                   | -                                |
| 1.3590 | 8600  | 0.1246        | -          | -                  | -                   | -                                |
| 1.3748 | 8700  | 0.1254        | -          | -                  | -                   | -                                |
| 1.3906 | 8800  | 0.1242        | -          | -                  | -                   | -                                |
| 1.4064 | 8900  | 0.1249        | -          | -                  | -                   | -                                |
| 1.4223 | 9000  | 0.1233        | -          | -                  | -                   | -                                |
| 1.4381 | 9100  | 0.1238        | -          | -                  | -                   | -                                |
| 1.4539 | 9200  | 0.1231        | -          | -                  | -                   | -                                |
| 1.4697 | 9300  | 0.122         | -          | -                  | -                   | -                                |
| 1.4855 | 9400  | 0.1217        | -          | -                  | -                   | -                                |
| 1.5013 | 9500  | 0.1225        | -          | -                  | -                   | -                                |
| 1.5171 | 9600  | 0.1213        | -          | -                  | -                   | -                                |
| 1.5329 | 9700  | 0.1208        | -          | -                  | -                   | -                                |
| 1.5487 | 9800  | 0.1214        | -          | -                  | -                   | -                                |
| 1.5645 | 9900  | 0.1205        | -          | -                  | -                   | -                                |
| 1.5803 | 10000 | 0.12          | 0.1120     | -12.20076          | 0.9843              | 0.7137                           |
| 1.5961 | 10100 | 0.1205        | -          | -                  | -                   | -                                |
| 1.6119 | 10200 | 0.12          | -          | -                  | -                   | -                                |
| 1.6277 | 10300 | 0.1187        | -          | -                  | -                   | -                                |
| 1.6435 | 10400 | 0.1184        | -          | -                  | -                   | -                                |
| 1.6593 | 10500 | 0.1178        | -          | -                  | -                   | -                                |
| 1.6751 | 10600 | 0.1188        | -          | -                  | -                   | -                                |
| 1.6909 | 10700 | 0.1184        | -          | -                  | -                   | -                                |
| 1.7067 | 10800 | 0.1168        | -          | -                  | -                   | -                                |
| 1.7225 | 10900 | 0.1175        | -          | -                  | -                   | -                                |
| 1.7383 | 11000 | 0.1158        | -          | -                  | -                   | -                                |
| 1.7541 | 11100 | 0.1159        | -          | -                  | -                   | -                                |
| 1.7699 | 11200 | 0.1178        | -          | -                  | -                   | -                                |
| 1.7857 | 11300 | 0.1158        | -          | -                  | -                   | -                                |
| 1.8015 | 11400 | 0.1161        | -          | -                  | -                   | -                                |
| 1.8173 | 11500 | 0.1151        | -          | -                  | -                   | -                                |
| 1.8331 | 11600 | 0.1147        | -          | -                  | -                   | -                                |
| 1.8489 | 11700 | 0.1152        | -          | -                  | -                   | -                                |
| 1.8647 | 11800 | 0.1144        | -          | -                  | -                   | -                                |
| 1.8805 | 11900 | 0.1145        | -          | -                  | -                   | -                                |
| 1.8963 | 12000 | 0.1144        | -          | -                  | -                   | -                                |
| 1.9121 | 12100 | 0.1139        | -          | -                  | -                   | -                                |
| 1.9279 | 12200 | 0.1144        | -          | -                  | -                   | -                                |
| 1.9437 | 12300 | 0.1144        | -          | -                  | -                   | -                                |
| 1.9595 | 12400 | 0.1124        | -          | -                  | -                   | -                                |
| 1.9753 | 12500 | 0.1134        | -          | -                  | -                   | -                                |
| 1.9912 | 12600 | 0.1133        | -          | -                  | -                   | -                                |
| 2.0070 | 12700 | 0.1125        | -          | -                  | -                   | -                                |
| 2.0228 | 12800 | 0.1108        | -          | -                  | -                   | -                                |
| 2.0386 | 12900 | 0.1112        | -          | -                  | -                   | -                                |
| 2.0544 | 13000 | 0.1109        | -          | -                  | -                   | -                                |
| 2.0702 | 13100 | 0.1105        | -          | -                  | -                   | -                                |
| 2.0860 | 13200 | 0.1112        | -          | -                  | -                   | -                                |
| 2.1018 | 13300 | 0.1105        | -          | -                  | -                   | -                                |
| 2.1176 | 13400 | 0.1105        | -          | -                  | -                   | -                                |
| 2.1334 | 13500 | 0.11          | -          | -                  | -                   | -                                |
| 2.1492 | 13600 | 0.1096        | -          | -                  | -                   | -                                |
| 2.1650 | 13700 | 0.1098        | -          | -                  | -                   | -                                |
| 2.1808 | 13800 | 0.1093        | -          | -                  | -                   | -                                |
| 2.1966 | 13900 | 0.1089        | -          | -                  | -                   | -                                |
| 2.2124 | 14000 | 0.1091        | -          | -                  | -                   | -                                |
| 2.2282 | 14100 | 0.1091        | -          | -                  | -                   | -                                |
| 2.2440 | 14200 | 0.1086        | -          | -                  | -                   | -                                |
| 2.2598 | 14300 | 0.1089        | -          | -                  | -                   | -                                |
| 2.2756 | 14400 | 0.1087        | -          | -                  | -                   | -                                |
| 2.2914 | 14500 | 0.1083        | -          | -                  | -                   | -                                |
| 2.3072 | 14600 | 0.1091        | -          | -                  | -                   | -                                |
| 2.3230 | 14700 | 0.1083        | -          | -                  | -                   | -                                |
| 2.3388 | 14800 | 0.1088        | -          | -                  | -                   | -                                |
| 2.3546 | 14900 | 0.1071        | -          | -                  | -                   | -                                |
| 2.3704 | 15000 | 0.1085        | 0.1015     | -11.243325         | 0.9843              | 0.7625                           |
| 2.3862 | 15100 | 0.1077        | -          | -                  | -                   | -                                |
| 2.4020 | 15200 | 0.1076        | -          | -                  | -                   | -                                |
| 2.4178 | 15300 | 0.108         | -          | -                  | -                   | -                                |
| 2.4336 | 15400 | 0.1066        | -          | -                  | -                   | -                                |
| 2.4494 | 15500 | 0.1062        | -          | -                  | -                   | -                                |
| 2.4652 | 15600 | 0.1065        | -          | -                  | -                   | -                                |
| 2.4810 | 15700 | 0.1058        | -          | -                  | -                   | -                                |
| 2.4968 | 15800 | 0.1071        | -          | -                  | -                   | -                                |
| 2.5126 | 15900 | 0.1071        | -          | -                  | -                   | -                                |
| 2.5284 | 16000 | 0.1066        | -          | -                  | -                   | -                                |
| 2.5442 | 16100 | 0.1067        | -          | -                  | -                   | -                                |
| 2.5601 | 16200 | 0.1057        | -          | -                  | -                   | -                                |
| 2.5759 | 16300 | 0.106         | -          | -                  | -                   | -                                |
| 2.5917 | 16400 | 0.1061        | -          | -                  | -                   | -                                |
| 2.6075 | 16500 | 0.1047        | -          | -                  | -                   | -                                |
| 2.6233 | 16600 | 0.1057        | -          | -                  | -                   | -                                |
| 2.6391 | 16700 | 0.106         | -          | -                  | -                   | -                                |
| 2.6549 | 16800 | 0.1055        | -          | -                  | -                   | -                                |
| 2.6707 | 16900 | 0.105         | -          | -                  | -                   | -                                |
| 2.6865 | 17000 | 0.1047        | -          | -                  | -                   | -                                |
| 2.7023 | 17100 | 0.1042        | -          | -                  | -                   | -                                |
| 2.7181 | 17200 | 0.1057        | -          | -                  | -                   | -                                |
| 2.7339 | 17300 | 0.1051        | -          | -                  | -                   | -                                |
| 2.7497 | 17400 | 0.1055        | -          | -                  | -                   | -                                |
| 2.7655 | 17500 | 0.1047        | -          | -                  | -                   | -                                |
| 2.7813 | 17600 | 0.1043        | -          | -                  | -                   | -                                |
| 2.7971 | 17700 | 0.1034        | -          | -                  | -                   | -                                |
| 2.8129 | 17800 | 0.1039        | -          | -                  | -                   | -                                |
| 2.8287 | 17900 | 0.1038        | -          | -                  | -                   | -                                |
| 2.8445 | 18000 | 0.1032        | -          | -                  | -                   | -                                |
| 2.8603 | 18100 | 0.103         | -          | -                  | -                   | -                                |
| 2.8761 | 18200 | 0.1035        | -          | -                  | -                   | -                                |
| 2.8919 | 18300 | 0.1024        | -          | -                  | -                   | -                                |
| 2.9077 | 18400 | 0.1032        | -          | -                  | -                   | -                                |
| 2.9235 | 18500 | 0.1031        | -          | -                  | -                   | -                                |
| 2.9393 | 18600 | 0.1034        | -          | -                  | -                   | -                                |
| 2.9551 | 18700 | 0.1033        | -          | -                  | -                   | -                                |
| 2.9709 | 18800 | 0.1036        | -          | -                  | -                   | -                                |
| 2.9867 | 18900 | 0.1029        | -          | -                  | -                   | -                                |
| 3.0025 | 19000 | 0.1024        | -          | -                  | -                   | -                                |
| 3.0183 | 19100 | 0.1017        | -          | -                  | -                   | -                                |
| 3.0341 | 19200 | 0.1012        | -          | -                  | -                   | -                                |
| 3.0499 | 19300 | 0.1016        | -          | -                  | -                   | -                                |
| 3.0657 | 19400 | 0.1012        | -          | -                  | -                   | -                                |
| 3.0815 | 19500 | 0.1009        | -          | -                  | -                   | -                                |
| 3.0973 | 19600 | 0.1015        | -          | -                  | -                   | -                                |
| 3.1131 | 19700 | 0.1014        | -          | -                  | -                   | -                                |
| 3.1290 | 19800 | 0.1004        | -          | -                  | -                   | -                                |
| 3.1448 | 19900 | 0.1011        | -          | -                  | -                   | -                                |
| 3.1606 | 20000 | 0.1006        | 0.0952     | -10.662492         | 0.9879              | 0.7811                           |
| 3.1764 | 20100 | 0.1007        | -          | -                  | -                   | -                                |
| 3.1922 | 20200 | 0.1015        | -          | -                  | -                   | -                                |
| 3.2080 | 20300 | 0.1005        | -          | -                  | -                   | -                                |
| 3.2238 | 20400 | 0.1017        | -          | -                  | -                   | -                                |
| 3.2396 | 20500 | 0.1012        | -          | -                  | -                   | -                                |
| 3.2554 | 20600 | 0.0998        | -          | -                  | -                   | -                                |
| 3.2712 | 20700 | 0.0997        | -          | -                  | -                   | -                                |
| 3.2870 | 20800 | 0.1001        | -          | -                  | -                   | -                                |
| 3.3028 | 20900 | 0.1009        | -          | -                  | -                   | -                                |
| 3.3186 | 21000 | 0.1           | -          | -                  | -                   | -                                |
| 3.3344 | 21100 | 0.1001        | -          | -                  | -                   | -                                |
| 3.3502 | 21200 | 0.1008        | -          | -                  | -                   | -                                |
| 3.3660 | 21300 | 0.0996        | -          | -                  | -                   | -                                |
| 3.3818 | 21400 | 0.0993        | -          | -                  | -                   | -                                |
| 3.3976 | 21500 | 0.1004        | -          | -                  | -                   | -                                |
| 3.4134 | 21600 | 0.0996        | -          | -                  | -                   | -                                |
| 3.4292 | 21700 | 0.0993        | -          | -                  | -                   | -                                |
| 3.4450 | 21800 | 0.0997        | -          | -                  | -                   | -                                |
| 3.4608 | 21900 | 0.0997        | -          | -                  | -                   | -                                |
| 3.4766 | 22000 | 0.0997        | -          | -                  | -                   | -                                |
| 3.4924 | 22100 | 0.0984        | -          | -                  | -                   | -                                |
| 3.5082 | 22200 | 0.0999        | -          | -                  | -                   | -                                |
| 3.5240 | 22300 | 0.099         | -          | -                  | -                   | -                                |
| 3.5398 | 22400 | 0.0992        | -          | -                  | -                   | -                                |
| 3.5556 | 22500 | 0.0988        | -          | -                  | -                   | -                                |
| 3.5714 | 22600 | 0.0989        | -          | -                  | -                   | -                                |
| 3.5872 | 22700 | 0.0989        | -          | -                  | -                   | -                                |
| 3.6030 | 22800 | 0.0978        | -          | -                  | -                   | -                                |
| 3.6188 | 22900 | 0.0987        | -          | -                  | -                   | -                                |
| 3.6346 | 23000 | 0.0997        | -          | -                  | -                   | -                                |
| 3.6504 | 23100 | 0.0994        | -          | -                  | -                   | -                                |
| 3.6662 | 23200 | 0.0984        | -          | -                  | -                   | -                                |
| 3.6820 | 23300 | 0.0985        | -          | -                  | -                   | -                                |
| 3.6979 | 23400 | 0.0983        | -          | -                  | -                   | -                                |
| 3.7137 | 23500 | 0.0992        | -          | -                  | -                   | -                                |
| 3.7295 | 23600 | 0.0983        | -          | -                  | -                   | -                                |
| 3.7453 | 23700 | 0.0987        | -          | -                  | -                   | -                                |
| 3.7611 | 23800 | 0.0983        | -          | -                  | -                   | -                                |
| 3.7769 | 23900 | 0.0969        | -          | -                  | -                   | -                                |
| 3.7927 | 24000 | 0.0984        | -          | -                  | -                   | -                                |
| 3.8085 | 24100 | 0.0976        | -          | -                  | -                   | -                                |
| 3.8243 | 24200 | 0.0984        | -          | -                  | -                   | -                                |
| 3.8401 | 24300 | 0.0974        | -          | -                  | -                   | -                                |
| 3.8559 | 24400 | 0.0982        | -          | -                  | -                   | -                                |
| 3.8717 | 24500 | 0.0983        | -          | -                  | -                   | -                                |
| 3.8875 | 24600 | 0.0986        | -          | -                  | -                   | -                                |
| 3.9033 | 24700 | 0.0977        | -          | -                  | -                   | -                                |
| 3.9191 | 24800 | 0.0974        | -          | -                  | -                   | -                                |
| 3.9349 | 24900 | 0.0979        | -          | -                  | -                   | -                                |
| 3.9507 | 25000 | 0.0974        | 0.0916     | -10.330441         | 0.9904              | 0.7840                           |
| 3.9665 | 25100 | 0.0974        | -          | -                  | -                   | -                                |
| 3.9823 | 25200 | 0.097         | -          | -                  | -                   | -                                |
| 3.9981 | 25300 | 0.0978        | -          | -                  | -                   | -                                |
| 4.0139 | 25400 | 0.0969        | -          | -                  | -                   | -                                |
| 4.0297 | 25500 | 0.0966        | -          | -                  | -                   | -                                |
| 4.0455 | 25600 | 0.0965        | -          | -                  | -                   | -                                |
| 4.0613 | 25700 | 0.0974        | -          | -                  | -                   | -                                |
| 4.0771 | 25800 | 0.0966        | -          | -                  | -                   | -                                |
| 4.0929 | 25900 | 0.0964        | -          | -                  | -                   | -                                |
| 4.1087 | 26000 | 0.0961        | -          | -                  | -                   | -                                |
| 4.1245 | 26100 | 0.0958        | -          | -                  | -                   | -                                |
| 4.1403 | 26200 | 0.0964        | -          | -                  | -                   | -                                |
| 4.1561 | 26300 | 0.097         | -          | -                  | -                   | -                                |
| 4.1719 | 26400 | 0.0967        | -          | -                  | -                   | -                                |
| 4.1877 | 26500 | 0.0968        | -          | -                  | -                   | -                                |
| 4.2035 | 26600 | 0.0965        | -          | -                  | -                   | -                                |
| 4.2193 | 26700 | 0.0956        | -          | -                  | -                   | -                                |
| 4.2351 | 26800 | 0.0963        | -          | -                  | -                   | -                                |
| 4.2509 | 26900 | 0.0958        | -          | -                  | -                   | -                                |
| 4.2668 | 27000 | 0.0969        | -          | -                  | -                   | -                                |
| 4.2826 | 27100 | 0.0951        | -          | -                  | -                   | -                                |
| 4.2984 | 27200 | 0.0958        | -          | -                  | -                   | -                                |
| 4.3142 | 27300 | 0.0956        | -          | -                  | -                   | -                                |
| 4.3300 | 27400 | 0.0965        | -          | -                  | -                   | -                                |
| 4.3458 | 27500 | 0.0952        | -          | -                  | -                   | -                                |
| 4.3616 | 27600 | 0.0956        | -          | -                  | -                   | -                                |
| 4.3774 | 27700 | 0.0956        | -          | -                  | -                   | -                                |
| 4.3932 | 27800 | 0.0966        | -          | -                  | -                   | -                                |
| 4.4090 | 27900 | 0.0972        | -          | -                  | -                   | -                                |
| 4.4248 | 28000 | 0.0954        | -          | -                  | -                   | -                                |
| 4.4406 | 28100 | 0.0961        | -          | -                  | -                   | -                                |
| 4.4564 | 28200 | 0.0963        | -          | -                  | -                   | -                                |
| 4.4722 | 28300 | 0.0958        | -          | -                  | -                   | -                                |
| 4.4880 | 28400 | 0.0961        | -          | -                  | -                   | -                                |
| 4.5038 | 28500 | 0.0961        | -          | -                  | -                   | -                                |
| 4.5196 | 28600 | 0.0956        | -          | -                  | -                   | -                                |
| 4.5354 | 28700 | 0.0955        | -          | -                  | -                   | -                                |
| 4.5512 | 28800 | 0.0957        | -          | -                  | -                   | -                                |
| 4.5670 | 28900 | 0.0953        | -          | -                  | -                   | -                                |
| 4.5828 | 29000 | 0.0952        | -          | -                  | -                   | -                                |
| 4.5986 | 29100 | 0.0964        | -          | -                  | -                   | -                                |
| 4.6144 | 29200 | 0.0955        | -          | -                  | -                   | -                                |
| 4.6302 | 29300 | 0.0948        | -          | -                  | -                   | -                                |
| 4.6460 | 29400 | 0.0946        | -          | -                  | -                   | -                                |
| 4.6618 | 29500 | 0.0953        | -          | -                  | -                   | -                                |
| 4.6776 | 29600 | 0.0954        | -          | -                  | -                   | -                                |
| 4.6934 | 29700 | 0.0956        | -          | -                  | -                   | -                                |
| 4.7092 | 29800 | 0.0958        | -          | -                  | -                   | -                                |
| 4.7250 | 29900 | 0.0956        | -          | -                  | -                   | -                                |
| 4.7408 | 30000 | 0.0962        | 0.0900     | -10.183619         | 0.9894              | 0.7903                           |
| 4.7566 | 30100 | 0.0953        | -          | -                  | -                   | -                                |
| 4.7724 | 30200 | 0.0959        | -          | -                  | -                   | -                                |
| 4.7882 | 30300 | 0.0949        | -          | -                  | -                   | -                                |
| 4.8040 | 30400 | 0.0958        | -          | -                  | -                   | -                                |
| 4.8198 | 30500 | 0.0952        | -          | -                  | -                   | -                                |
| 4.8357 | 30600 | 0.0952        | -          | -                  | -                   | -                                |
| 4.8515 | 30700 | 0.095         | -          | -                  | -                   | -                                |
| 4.8673 | 30800 | 0.0949        | -          | -                  | -                   | -                                |
| 4.8831 | 30900 | 0.0949        | -          | -                  | -                   | -                                |
| 4.8989 | 31000 | 0.0953        | -          | -                  | -                   | -                                |
| 4.9147 | 31100 | 0.0955        | -          | -                  | -                   | -                                |
| 4.9305 | 31200 | 0.0964        | -          | -                  | -                   | -                                |
| 4.9463 | 31300 | 0.0955        | -          | -                  | -                   | -                                |
| 4.9621 | 31400 | 0.0955        | -          | -                  | -                   | -                                |
| 4.9779 | 31500 | 0.0954        | -          | -                  | -                   | -                                |
| 4.9937 | 31600 | 0.0959        | -          | -                  | -                   | -                                |

</details>

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.3.1
- Transformers: 4.46.3
- PyTorch: 2.5.1+cu124
- Accelerate: 1.2.1
- Datasets: 3.2.0
- Tokenizers: 0.20.3

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

#### MSELoss
```bibtex
@inproceedings{reimers-2020-multilingual-sentence-bert,
    title = "Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2004.09813",
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