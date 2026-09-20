---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
base_model:
- intfloat/multilingual-e5-small
- dragonkue/multilingual-e5-small-ko
pipeline_tag: sentence-similarity
library_name: sentence-transformers
license: apache-2.0
language:
- ko
- en
---

<img src="https://cdn-uploads.huggingface.co/production/uploads/642b0c2fecec03b4464a1d9b/IxcqY5qbGNuGpqDciIcOI.webp" width="600">

# SentenceTransformer based on intfloat/multilingual-e5-small

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) on datasets that include Korean query-passage pairs for improved performance on Korean retrieval tasks. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

This model is a lightweight Korean retriever, designed for ease of use and strong performance in practical retrieval tasks.
It is ideal for running demos or lightweight applications, offering a good balance between speed and accuracy.

For even higher retrieval performance, we recommend combining it with a reranker.
Suggested reranker models:

- dragonkue/bge-reranker-v2-m3-ko

- BAAI/bge-reranker-v2-m3

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) <!-- at revision c007d7ef6fd86656326059b28395a7a03a7c5846 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Datasets:**

<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("dragonkue/multilingual-e5-small-ko")
# Run inference
sentences = [
    'query: 북한가족법 몇 차 개정에서 이혼판결 확정 후 3개월 내에 등록시에만 유효하다는 조항을 확실히 했을까?',
    'passage: 1990년에 제정된 북한 가족법은 지금까지 4차례 개정되어 현재에 이르고 있다. 1993년에 이루어진 제1차 개정은 주로 규정의 정확성을 기하기 위하여 몇몇 조문을 수정한 것이며, 실체적인 내용을 보완한 것은 상속의 승인과 포기기간을 설정한 제52조 정도라고 할 수 있다. 2004년에 이루어진 제2차에 개정에서는 제20조제3항을 신설하여 재판상 확정된 이혼판결을 3개월 내에 등록해야 이혼의 효력이 발생한다는 것을 명확하게 하였다. 2007년에 이루어진 제3차 개정에서는 부모와 자녀 관계 또한 신분등록기관에 등록한 때부터 법적 효력이 발생한다는 것을 신설(제25조제2항)하였다. 또한 미성년자, 노동능력 없는 자의 부양과 관련(제37조제2항)하여 기존에는 “부양능력이 있는 가정성원이 없을 경우에는 따로 사는 부모나 자녀, 조부모나 손자녀, 형제자매가 부양한다”고 규정하고 있었던 것을 “부양능력이 있는 가정성원이 없을 경우에는 따로 사는 부모나 자녀가 부양하며 그들이 없을 경우에는 조부모나 손자녀, 형제자매가 부양한다”로 개정하였다.',
    'passage: 환경마크 제도, 인증기준 변경으로 기업부담 줄인다\n환경마크 제도 소개\n□ 개요\n○ 동일 용도의 다른 제품에 비해 ‘제품의 환경성*’을 개선한 제품에 로고와 설명을 표시할 수 있도록하는 인증 제도\n※ 제품의 환경성 : 재료와 제품을 제조․소비 폐기하는 전과정에서 오염물질이나 온실가스 등을 배출하는 정도 및 자원과 에너지를 소비하는 정도 등 환경에 미치는 영향력의 정도(「환경기술 및 환경산업 지원법」제2조제5호)\n□ 법적근거\n○ 「환경기술 및 환경산업 지원법」제17조(환경표지의 인증)\n□ 관련 국제표준\n○ ISO 14024(제1유형 환경라벨링)\n□ 적용대상\n○ 사무기기, 가전제품, 생활용품, 건축자재 등 156개 대상제품군\n□ 인증현황\n○ 2,737개 기업의 16,647개 제품(2015.12월말 기준)',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

### Direct Usage (Transformers)

```python
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


# Each input text should start with "query: " or "passage: ", even for non-English texts.
# For tasks other than retrieval, you can simply use the "query: " prefix.
input_texts = ["query: 북한가족법 몇 차 개정에서 이혼판결 확정 후 3개월 내에 등록시에만 유효하다는 조항을 확실히 했을까?",
               "passage: 1990년에 제정된 북한 가족법은 지금까지 4차례 개정되어 현재에 이르고 있다. 1993년에 이루어진 제1차 개정은 주로 규정의 정확성을 기하기 위하여 몇몇 조문을 수정한 것이며, 실체적인 내용을 보완한 것은 상속의 승인과 포기기간을 설정한 제52조 정도라고 할 수 있다. 2004년에 이루어진 제2차에 개정에서는 제20조제3항을 신설하여 재판상 확정된 이혼판결을 3개월 내에 등록해야 이혼의 효력이 발생한다는 것을 명확하게 하였다. 2007년에 이루어진 제3차 개정에서는 부모와 자녀 관계 또한 신분등록기관에 등록한 때부터 법적 효력이 발생한다는 것을 신설(제25조제2항)하였다. 또한 미성년자, 노동능력 없는 자의 부양과 관련(제37조제2항)하여 기존에는 “부양능력이 있는 가정성원이 없을 경우에는 따로 사는 부모나 자녀, 조부모나 손자녀, 형제자매가 부양한다”고 규정하고 있었던 것을 “부양능력이 있는 가정성원이 없을 경우에는 따로 사는 부모나 자녀가 부양하며 그들이 없을 경우에는 조부모나 손자녀, 형제자매가 부양한다”로 개정하였다.",
               "passage: 환경마크 제도, 인증기준 변경으로 기업부담 줄인다\n환경마크 제도 소개\n□ 개요\n○ 동일 용도의 다른 제품에 비해 ‘제품의 환경성*’을 개선한 제품에 로고와 설명을 표시할 수 있도록하는 인증 제도\n※ 제품의 환경성 : 재료와 제품을 제조․소비 폐기하는 전과정에서 오염물질이나 온실가스 등을 배출하는 정도 및 자원과 에너지를 소비하는 정도 등 환경에 미치는 영향력의 정도(「환경기술 및 환경산업 지원법」제2조제5호)\n□ 법적근거\n○ 「환경기술 및 환경산업 지원법」제17조(환경표지의 인증)\n□ 관련 국제표준\n○ ISO 14024(제1유형 환경라벨링)\n□ 적용대상\n○ 사무기기, 가전제품, 생활용품, 건축자재 등 156개 대상제품군\n□ 인증현황\n○ 2,737개 기업의 16,647개 제품(2015.12월말 기준)"]

tokenizer = AutoTokenizer.from_pretrained('dragonkue/multilingual-e5-small-ko')
model = AutoModel.from_pretrained('dragonkue/multilingual-e5-small-ko')

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T)
print(scores.tolist())
```


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

- This evaluation references the KURE GitHub repository. (https://github.com/nlpai-lab/KURE)
- We conducted an evaluation on all **Korean Retrieval Benchmarks** registered in [MTEB](https://github.com/embeddings-benchmark/mteb).

### Korean Retrieval Benchmark
- [Ko-StrategyQA](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA): A Korean **ODQA multi-hop retrieval dataset**, translated from StrategyQA.
- [AutoRAGRetrieval](https://huggingface.co/datasets/yjoonjang/markers_bm): A **Korean document retrieval dataset** constructed by parsing PDFs from five domains: **finance, public, medical, legal, and commerce**.
- [MIRACLRetrieval](https://huggingface.co/datasets/miracl/miracl): A **Korean document retrieval dataset** based on Wikipedia.
- [PublicHealthQA](https://huggingface.co/datasets/xhluca/publichealth-qa): A **retrieval dataset** focused on **medical and public health domains** in Korean.
- [BelebeleRetrieval](https://huggingface.co/datasets/facebook/belebele): A **Korean document retrieval dataset** based on FLORES-200.
- [MrTidyRetrieval](https://huggingface.co/datasets/mteb/mrtidy): A **Wikipedia-based Korean document retrieval dataset**.
- [XPQARetrieval](https://huggingface.co/datasets/jinaai/xpqa): A **cross-domain Korean document retrieval dataset**.

### Metrics

* Standard metric : NDCG@10

#### Information Retrieval
| Model                                                       |   Size(M) |   Average |   XPQARetrieval |   PublicHealthQA |   MIRACLRetrieval |   Ko-StrategyQA |   BelebeleRetrieval |   AutoRAGRetrieval |   MrTidyRetrieval |
|:------------------------------------------------------------|----------:|----------:|----------------:|-----------------:|------------------:|----------------:|--------------------:|-------------------:|------------------:|
| BAAI/bge-m3                                                 |       560 |  0.724169 |         0.36075 |          0.80412 |           0.70146 |         0.79405 |             0.93164 |            0.83008 |           0.64708 |
| Snowflake/snowflake-arctic-embed-l-v2.0                     |       560 |  0.724104 |         0.43018 |          0.81679 |           0.66077 |         0.80455 |             0.9271  |            0.83863 |           0.59071 |
| intfloat/multilingual-e5-large                              |       560 |  0.721607 |         0.3571  |          0.82534 |           0.66486 |         0.80348 |             0.94499 |            0.81337 |           0.64211 |
| intfloat/multilingual-e5-base                               |       278 |  0.689429 |         0.3607  |          0.77203 |           0.6227  |         0.76355 |             0.92868 |            0.79752 |           0.58082 |
| dragonkue/multilingual-e5-small-ko                          |       118 |  0.688819 |         0.34871 |          0.79729 |           0.61113 |         0.76173 |             0.9297  |            0.86184 |           0.51133 |
| **exp-models/dragonkue-KoEn-E5-Tiny**                       |        37 |  0.687496 |         0.34735 |          0.7925  |           0.6143  |         0.75978 |             0.93018 |            0.86503 |           0.50333 |
| intfloat/multilingual-e5-small                              |       118 |  0.670906 |         0.33003 |          0.73668 |           0.61238 |         0.75157 |             0.90531 |            0.80068 |           0.55969 |
| ibm-granite/granite-embedding-278m-multilingual             |       278 |  0.616466 |         0.23058 |          0.77668 |           0.59216 |         0.71762 |             0.83231 |            0.70226 |           0.46365 |
| ibm-granite/granite-embedding-107m-multilingual             |       107 |  0.599759 |         0.23058 |          0.73209 |           0.58413 |         0.70531 |             0.82063 |            0.68243 |           0.44314 |
| sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 |       118 |  0.409766 |         0.21345 |          0.67409 |           0.25676 |         0.45903 |             0.71491 |            0.42296 |           0.12716 |

#### Performance Comparison by Model Size (Based on Average NDCG@10)
<img src="https://cdn-uploads.huggingface.co/production/uploads/642b0c2fecec03b4464a1d9b/aF7YOGJLwELDgCvuoylKH.png" width="1000"/>


<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Datasets
This model was fine-tuned on the same dataset used in dragonkue/snowflake-arctic-embed-l-v2.0-ko, which consists of Korean query-passage pairs.
The training objective was to improve retrieval performance specifically for Korean-language tasks.

### Training Methods

Following the training approach used in dragonkue/snowflake-arctic-embed-l-v2.0-ko, this model constructs in-batch negatives based on clustered passages. In addition, we introduce GISTEmbedLoss with a configurable margin.

**📈 Margin-based Training Results**
- Using the standard MNR (Multiple Negatives Ranking) loss alone resulted in decreased performance.

- The original GISTEmbedLoss (without margin) yielded modest improvements of around +0.8 NDCG@10.

- Applying a margin led to performance gains of up to +1.5 NDCG@10.

- This indicates that simply tuning the margin value can lead to up to 2x improvement, showing strong sensitivity and effectiveness of margin scaling.

This margin-based approach extends the idea proposed in the NV-Retriever paper, which originally filtered false negatives during hard negative sampling.
We adapt this to in-batch negatives, treating false negatives as dynamic samples guided by margin-based filtering.

<img src="https://cdn-uploads.huggingface.co/production/uploads/642b0c2fecec03b4464a1d9b/IpDDTshuZ5noxPOdm6gVk.png" width="800"/>

The sentence-transformers library now supports GISTEmbedLoss with margin configuration, making it easy to integrate into any training pipeline.

You can install the latest version with:

```bash
pip install -U sentence-transformers
```


### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 20000
- `per_device_eval_batch_size`: 4096
- `learning_rate`: 0.00025
- `num_train_epochs`: 3
- `warmup_ratio`: 0.05
- `fp16`: True
- `dataloader_drop_last`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 20000
- `per_device_eval_batch_size`: 4096
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 0.00025
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.05
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
- `dataloader_drop_last`: True
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>


### Framework Versions
- Python: 3.11.10
- Sentence Transformers: 4.1.0
- Transformers: 4.51.3
- PyTorch: 2.7.0+cu126
- Accelerate: 1.6.0
- Datasets: 3.5.1
- Tokenizers: 0.21.1

## FAQ
**1. Do I need to add the prefix "query: " and "passage: " to input texts?**

Yes, this is how the model is trained, otherwise you will see a performance degradation.

Here are some rules of thumb:

Use "query: " and "passage: " correspondingly for asymmetric tasks such as passage retrieval in open QA, ad-hoc information retrieval.

Use "query: " prefix for symmetric tasks such as semantic similarity, bitext mining, paraphrase retrieval.

Use "query: " prefix if you want to use embeddings as features, such as linear probing classification, clustering.

**2. Why does the cosine similarity scores distribute around 0.7 to 1.0?**

This is a known and expected behavior as we use a low temperature 0.01 for InfoNCE contrastive loss.

For text embedding tasks like text retrieval or semantic similarity, what matters is the relative order of the scores instead of the absolute values, so this should not be an issue.

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

#### Base Model
```bibtex
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```
#### NV-Retriever: Improving text embedding models with effective hard-negative mining
```bibtex
@article{moreira2024nvretriever,
  title     = {NV-Retriever: Improving text embedding models with effective hard-negative mining},
  author    = {Moreira, Gabriel de Souza P. and Osmulski, Radek and Xu, Mengyao and Ak, Ronay and Schifferer, Benedikt and Oldridge, Even},
  journal   = {arXiv preprint arXiv:2407.15831},
  year      = {2024},
  url       = {https://arxiv.org/abs/2407.15831},
  doi       = {10.48550/arXiv.2407.15831}
}
```

## Limitations

Long texts will be truncated to at most 512 tokens.

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