---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:82069
- loss:MSELoss
base_model: sentence-transformers/LaBSE
widget:
- source_sentence: Kendi kendine yardım etsen Tanrı da sana yardımcı olur.
  sentences:
  - nasin sina li pona seme?
  - ona li jan sona.
  - o pana e pona tawa sama sina la mama sewi li pana e pona tawa sina.
- source_sentence: 星星在夜里出现。
  sentences:
  - tenpo pimeja la mun li kama.
  - sina unpa lukin kin.
  - 'jan ni li toki ike tan mi. ona li wile ala pilin e ni: mi kama tawa ona.'
- source_sentence: 오렌지 주스를 좀 주세요.
  sentences:
  - mi ken la mi pana e pona tawa sina.
  - jan Ton en jan Mewi li tawa ma Oselija lon tenpo sike pini.
  - mi wile e telo pi kili jelo.
- source_sentence: Ён чакае адпраўлення цягніка.
  sentences:
  - 'ona li awen tawa ni: tomo tawa linja li tawa weka.'
  - lon ma tomo sina la telo li kama ala kama tan sewi?
  - 'jan li sona ala e ni: tenpo seme la utala li pini.'
- source_sentence: 我只想暖和一下。
  sentences:
  - mi wile kama seli taso.
  - tomo tawa sina li lon ni.
  - mi moku e kili.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- negative_mse
- src2trg_accuracy
- trg2src_accuracy
- mean_accuracy
model-index:
- name: SentenceTransformer based on sentence-transformers/LaBSE
  results:
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: eval data
      type: eval_data
    metrics:
    - type: negative_mse
      value: -0.04922879859805107
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: eval data
      type: eval_data
    metrics:
    - type: src2trg_accuracy
      value: 0.8380595265994845
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.7736114366065151
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.8058354816029998
      name: Mean Accuracy
datasets:
- NetherQuartz/tatoeba-tokipona
- NetherQuartz/lipu-sewi
- NetherQuartz/minecraft-translations
language:
- tok
- en
- ru
- uk
- be
- fr
- es
- pt
- it
- de
- vi
- ja
- zh
- ko
- ar
- he
- pl
- tr
- la
- el
---

# SentenceTransformer based on sentence-transformers/LaBSE

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) on Toki Pona dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, bitext mining and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE) <!-- at revision 836121a0533e5664b21c7aacc5d22951f2b8b25b -->
- **Maximum Sequence Length:** 256 tokens
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
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
  (3): Normalize()
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
model = SentenceTransformer("NetherQuartz/LaBSE-tokipona")
# Run inference
sentences = [
    '我只想暖和一下。',
    'mi wile kama seli taso.',
    'tomo tawa sina li lon ni.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8126, 0.2629],
#         [0.8126, 1.0000, 0.4022],
#         [0.2629, 0.4022, 1.0000]])
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

* Dataset: `eval_data`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value       |
|:-----------------|:------------|
| **negative_mse** | **-0.0492** |

#### Translation

* Dataset: `eval_data`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.8381     |
| trg2src_accuracy  | 0.7736     |
| **mean_accuracy** | **0.8058** |

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

* Size: 82,069 training samples
* Columns: <code>natural</code>, <code>tok</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | natural                                                                           | tok                                                                               | label                                |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | string                                                                            | list                                 |
  | details | <ul><li>min: 3 tokens</li><li>mean: 10.66 tokens</li><li>max: 43 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 13.96 tokens</li><li>max: 47 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | natural                                      | tok                                        | label                                                                                                                              |
  |:---------------------------------------------|:-------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
  | <code>Я держу руку.</code>                   | <code>mi sewi e luka mi.</code>            | <code>[-0.02380160242319107, -0.05106028914451599, -0.054335981607437134, -0.050830986350774765, -0.05793563649058342, ...]</code> |
  | <code>Я змарыўся ад працы.</code>            | <code>tan pali mi la mi pilin lape.</code> | <code>[-0.03956804797053337, 0.008637639693915844, -0.045203790068626404, -0.06055501475930214, -0.06817363947629929, ...]</code>  |
  | <code>Mi bolso necesita ser reparado.</code> | <code>poki mi li pakala.</code>            | <code>[-0.06031221151351929, -0.006717301905155182, -0.03342252969741821, -0.03583073988556862, -0.0651949867606163, ...]</code>   |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Evaluation Dataset

#### Unnamed Dataset

* Size: 4,267 evaluation samples
* Columns: <code>natural</code>, <code>tok</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | natural                                                                           | tok                                                                              | label                                |
  |:--------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | string                                                                           | list                                 |
  | details | <ul><li>min: 5 tokens</li><li>mean: 10.59 tokens</li><li>max: 43 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 13.7 tokens</li><li>max: 59 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | natural                                             | tok                                                  | label                                                                                                                                 |
  |:----------------------------------------------------|:-----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Da quanto tempo sei/state in Germania?</code> | <code>tenpo pi suli seme la sina lon ma Tosi?</code> | <code>[-0.025023534893989563, -0.0016661343397572637, -0.02266993746161461, -0.061682481318712234, -0.035705942660570145, ...]</code> |
  | <code>Habesne difficultatem hac re?</code>          | <code>ni li ike tawa sina anu seme?</code>           | <code>[0.033313240855932236, -0.04223407432436943, -0.012467658147215843, -0.06204398348927498, -0.06461521983146667, ...]</code>     |
  | <code>אני לא הולך להפסיד.</code>                    | <code>mi kama ala anpa.</code>                       | <code>[-0.05783797428011894, -0.04036393761634827, -0.0631723552942276, -0.03369426354765892, -0.05813731253147125, ...]</code>       |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#mseloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `learning_rate`: 2e-05
- `num_train_epochs`: 12
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
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 12
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
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch       | Step      | Training Loss | Validation Loss | eval_data_negative_mse | eval_data_mean_accuracy |
|:-----------:|:---------:|:-------------:|:---------------:|:----------------------:|:-----------------------:|
| 0.0779      | 100       | 0.0009        | -               | -                      | -                       |
| 0.1559      | 200       | 0.0007        | -               | -                      | -                       |
| 0.2338      | 300       | 0.0006        | -               | -                      | -                       |
| 0.3118      | 400       | 0.0006        | -               | -                      | -                       |
| 0.3897      | 500       | 0.0005        | -               | -                      | -                       |
| 0.4677      | 600       | 0.0005        | -               | -                      | -                       |
| 0.5456      | 700       | 0.0005        | -               | -                      | -                       |
| 0.6235      | 800       | 0.0004        | -               | -                      | -                       |
| 0.7015      | 900       | 0.0004        | -               | -                      | -                       |
| 0.7794      | 1000      | 0.0004        | -               | -                      | -                       |
| 0.8574      | 1100      | 0.0004        | -               | -                      | -                       |
| 0.9353      | 1200      | 0.0004        | -               | -                      | -                       |
| 1.0133      | 1300      | 0.0004        | -               | -                      | -                       |
| 1.0912      | 1400      | 0.0004        | -               | -                      | -                       |
| 1.1691      | 1500      | 0.0004        | -               | -                      | -                       |
| 1.2471      | 1600      | 0.0004        | -               | -                      | -                       |
| 1.3250      | 1700      | 0.0003        | -               | -                      | -                       |
| 1.4030      | 1800      | 0.0003        | -               | -                      | -                       |
| 1.4809      | 1900      | 0.0003        | -               | -                      | -                       |
| 1.5588      | 2000      | 0.0003        | 0.0003          | -0.0572                | 0.7559                  |
| 1.6368      | 2100      | 0.0003        | -               | -                      | -                       |
| 1.7147      | 2200      | 0.0003        | -               | -                      | -                       |
| 1.7927      | 2300      | 0.0003        | -               | -                      | -                       |
| 1.8706      | 2400      | 0.0003        | -               | -                      | -                       |
| 1.9486      | 2500      | 0.0003        | -               | -                      | -                       |
| 2.0265      | 2600      | 0.0003        | -               | -                      | -                       |
| 2.1044      | 2700      | 0.0003        | -               | -                      | -                       |
| 2.1824      | 2800      | 0.0003        | -               | -                      | -                       |
| 2.2603      | 2900      | 0.0003        | -               | -                      | -                       |
| 2.3383      | 3000      | 0.0003        | -               | -                      | -                       |
| 2.4162      | 3100      | 0.0003        | -               | -                      | -                       |
| 2.4942      | 3200      | 0.0003        | -               | -                      | -                       |
| 2.5721      | 3300      | 0.0003        | -               | -                      | -                       |
| 2.6500      | 3400      | 0.0003        | -               | -                      | -                       |
| 2.7280      | 3500      | 0.0003        | -               | -                      | -                       |
| 2.8059      | 3600      | 0.0003        | -               | -                      | -                       |
| 2.8839      | 3700      | 0.0003        | -               | -                      | -                       |
| 2.9618      | 3800      | 0.0003        | -               | -                      | -                       |
| 3.0398      | 3900      | 0.0003        | -               | -                      | -                       |
| 3.1177      | 4000      | 0.0003        | 0.0003          | -0.0528                | 0.7850                  |
| 3.1956      | 4100      | 0.0003        | -               | -                      | -                       |
| 3.2736      | 4200      | 0.0003        | -               | -                      | -                       |
| 3.3515      | 4300      | 0.0003        | -               | -                      | -                       |
| 3.4295      | 4400      | 0.0003        | -               | -                      | -                       |
| 3.5074      | 4500      | 0.0003        | -               | -                      | -                       |
| 3.5853      | 4600      | 0.0003        | -               | -                      | -                       |
| 3.6633      | 4700      | 0.0003        | -               | -                      | -                       |
| 3.7412      | 4800      | 0.0003        | -               | -                      | -                       |
| 3.8192      | 4900      | 0.0003        | -               | -                      | -                       |
| 3.8971      | 5000      | 0.0003        | -               | -                      | -                       |
| 3.9751      | 5100      | 0.0003        | -               | -                      | -                       |
| 4.0530      | 5200      | 0.0003        | -               | -                      | -                       |
| 4.1309      | 5300      | 0.0003        | -               | -                      | -                       |
| 4.2089      | 5400      | 0.0003        | -               | -                      | -                       |
| 4.2868      | 5500      | 0.0003        | -               | -                      | -                       |
| 4.3648      | 5600      | 0.0003        | -               | -                      | -                       |
| 4.4427      | 5700      | 0.0003        | -               | -                      | -                       |
| 4.5207      | 5800      | 0.0003        | -               | -                      | -                       |
| 4.5986      | 5900      | 0.0003        | -               | -                      | -                       |
| 4.6765      | 6000      | 0.0003        | 0.0003          | -0.0512                | 0.7936                  |
| 4.7545      | 6100      | 0.0003        | -               | -                      | -                       |
| 4.8324      | 6200      | 0.0003        | -               | -                      | -                       |
| 4.9104      | 6300      | 0.0003        | -               | -                      | -                       |
| 4.9883      | 6400      | 0.0003        | -               | -                      | -                       |
| 5.0663      | 6500      | 0.0003        | -               | -                      | -                       |
| 5.1442      | 6600      | 0.0003        | -               | -                      | -                       |
| 5.2221      | 6700      | 0.0003        | -               | -                      | -                       |
| 5.3001      | 6800      | 0.0003        | -               | -                      | -                       |
| 5.3780      | 6900      | 0.0003        | -               | -                      | -                       |
| 5.4560      | 7000      | 0.0003        | -               | -                      | -                       |
| 5.5339      | 7100      | 0.0003        | -               | -                      | -                       |
| 5.6118      | 7200      | 0.0003        | -               | -                      | -                       |
| 5.6898      | 7300      | 0.0003        | -               | -                      | -                       |
| 5.7677      | 7400      | 0.0003        | -               | -                      | -                       |
| 5.8457      | 7500      | 0.0003        | -               | -                      | -                       |
| 5.9236      | 7600      | 0.0003        | -               | -                      | -                       |
| 6.0016      | 7700      | 0.0003        | -               | -                      | -                       |
| 6.0795      | 7800      | 0.0003        | -               | -                      | -                       |
| 6.1574      | 7900      | 0.0003        | -               | -                      | -                       |
| 6.2354      | 8000      | 0.0003        | 0.0003          | -0.0504                | 0.8022                  |
| 6.3133      | 8100      | 0.0003        | -               | -                      | -                       |
| 6.3913      | 8200      | 0.0003        | -               | -                      | -                       |
| 6.4692      | 8300      | 0.0003        | -               | -                      | -                       |
| 6.5472      | 8400      | 0.0003        | -               | -                      | -                       |
| 6.6251      | 8500      | 0.0003        | -               | -                      | -                       |
| 6.7030      | 8600      | 0.0003        | -               | -                      | -                       |
| 6.7810      | 8700      | 0.0003        | -               | -                      | -                       |
| 6.8589      | 8800      | 0.0003        | -               | -                      | -                       |
| 6.9369      | 8900      | 0.0003        | -               | -                      | -                       |
| 7.0148      | 9000      | 0.0003        | -               | -                      | -                       |
| 7.0928      | 9100      | 0.0003        | -               | -                      | -                       |
| 7.1707      | 9200      | 0.0003        | -               | -                      | -                       |
| 7.2486      | 9300      | 0.0003        | -               | -                      | -                       |
| 7.3266      | 9400      | 0.0003        | -               | -                      | -                       |
| 7.4045      | 9500      | 0.0003        | -               | -                      | -                       |
| 7.4825      | 9600      | 0.0003        | -               | -                      | -                       |
| 7.5604      | 9700      | 0.0003        | -               | -                      | -                       |
| 7.6383      | 9800      | 0.0003        | -               | -                      | -                       |
| 7.7163      | 9900      | 0.0003        | -               | -                      | -                       |
| 7.7942      | 10000     | 0.0003        | 0.0003          | -0.0497                | 0.8034                  |
| 7.8722      | 10100     | 0.0003        | -               | -                      | -                       |
| 7.9501      | 10200     | 0.0003        | -               | -                      | -                       |
| 8.0281      | 10300     | 0.0003        | -               | -                      | -                       |
| 8.1060      | 10400     | 0.0003        | -               | -                      | -                       |
| 8.1839      | 10500     | 0.0003        | -               | -                      | -                       |
| 8.2619      | 10600     | 0.0003        | -               | -                      | -                       |
| 8.3398      | 10700     | 0.0003        | -               | -                      | -                       |
| 8.4178      | 10800     | 0.0003        | -               | -                      | -                       |
| 8.4957      | 10900     | 0.0003        | -               | -                      | -                       |
| 8.5737      | 11000     | 0.0003        | -               | -                      | -                       |
| 8.6516      | 11100     | 0.0003        | -               | -                      | -                       |
| 8.7295      | 11200     | 0.0003        | -               | -                      | -                       |
| 8.8075      | 11300     | 0.0003        | -               | -                      | -                       |
| 8.8854      | 11400     | 0.0003        | -               | -                      | -                       |
| 8.9634      | 11500     | 0.0003        | -               | -                      | -                       |
| 9.0413      | 11600     | 0.0003        | -               | -                      | -                       |
| 9.1193      | 11700     | 0.0003        | -               | -                      | -                       |
| 9.1972      | 11800     | 0.0003        | -               | -                      | -                       |
| 9.2751      | 11900     | 0.0003        | -               | -                      | -                       |
| 9.3531      | 12000     | 0.0003        | 0.0003          | -0.0495                | 0.8049                  |
| 9.4310      | 12100     | 0.0003        | -               | -                      | -                       |
| 9.5090      | 12200     | 0.0003        | -               | -                      | -                       |
| 9.5869      | 12300     | 0.0003        | -               | -                      | -                       |
| 9.6648      | 12400     | 0.0003        | -               | -                      | -                       |
| 9.7428      | 12500     | 0.0003        | -               | -                      | -                       |
| 9.8207      | 12600     | 0.0003        | -               | -                      | -                       |
| 9.8987      | 12700     | 0.0003        | -               | -                      | -                       |
| 9.9766      | 12800     | 0.0003        | -               | -                      | -                       |
| 10.0546     | 12900     | 0.0003        | -               | -                      | -                       |
| 10.1325     | 13000     | 0.0003        | -               | -                      | -                       |
| 10.2104     | 13100     | 0.0003        | -               | -                      | -                       |
| 10.2884     | 13200     | 0.0003        | -               | -                      | -                       |
| 10.3663     | 13300     | 0.0003        | -               | -                      | -                       |
| 10.4443     | 13400     | 0.0003        | -               | -                      | -                       |
| 10.5222     | 13500     | 0.0003        | -               | -                      | -                       |
| 10.6002     | 13600     | 0.0003        | -               | -                      | -                       |
| 10.6781     | 13700     | 0.0003        | -               | -                      | -                       |
| 10.7560     | 13800     | 0.0003        | -               | -                      | -                       |
| 10.8340     | 13900     | 0.0003        | -               | -                      | -                       |
| **10.9119** | **14000** | **0.0003**    | **0.0003**      | **-0.0492**            | **0.8058**              |
| 10.9899     | 14100     | 0.0003        | -               | -                      | -                       |
| 11.0678     | 14200     | 0.0003        | -               | -                      | -                       |
| 11.1458     | 14300     | 0.0003        | -               | -                      | -                       |
| 11.2237     | 14400     | 0.0003        | -               | -                      | -                       |
| 11.3016     | 14500     | 0.0003        | -               | -                      | -                       |
| 11.3796     | 14600     | 0.0003        | -               | -                      | -                       |
| 11.4575     | 14700     | 0.0003        | -               | -                      | -                       |
| 11.5355     | 14800     | 0.0003        | -               | -                      | -                       |
| 11.6134     | 14900     | 0.0003        | -               | -                      | -                       |
| 11.6913     | 15000     | 0.0003        | -               | -                      | -                       |
| 11.7693     | 15100     | 0.0003        | -               | -                      | -                       |
| 11.8472     | 15200     | 0.0003        | -               | -                      | -                       |
| 11.9252     | 15300     | 0.0003        | -               | -                      | -                       |
| 12.0        | 15396     | -             | 0.0003          | -0.0492                | 0.8058                  |

* The bold row denotes the saved checkpoint.
</details>

### Framework Versions
- Python: 3.13.7
- Sentence Transformers: 5.3.0
- Transformers: 4.55.2
- PyTorch: 2.10.0+cu128
- Accelerate: 1.13.0
- Datasets: 4.7.0
- Tokenizers: 0.21.4

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