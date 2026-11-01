---
tags:
- ColBERT
- multi-vector
- PyLate
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
pipeline_tag: sentence-similarity
library_name: PyLate
license: apache-2.0
language:
- ko
---

# colbert-ko-v1

**colbert-ko-v1** is a Korean colbert model finetuned with [PyLate](https://github.com/lightonai/pylate). This model is trained exclusively on Korean dataset. It maps sentences & paragraphs to sequences of 128-dimensional dense vectors and can be used for semantic textual similarity using the MaxSim operator.

## Model Details

### Model Description
- **Model Type:** Multi-vector embedding model
- **Document Length:** 1024 tokens
- **Query Length:** 32 tokens
- **Output Dimensionality:** 128 tokens
- **Similarity Function:** MaxSim
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->


### Full Model Architecture

```
ColBERT(
  (0): Transformer({'max_seq_length': 1023, 'do_lower_case': False}) with Transformer model: ModernBertModel 
  (1): Dense({'in_features': 768, 'out_features': 128, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})
)
```

## Evaluation

### Evaluation Dataset
| Dataset                                                               | Description                                                                                             | Average Length (characters) |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------|
| [Ko-StrategyQA](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA) | Korean ODQA multi-hop retrieval dataset (translated from StrategyQA) | 305.15 |
| [AutoRAGRetrieval](https://huggingface.co/datasets/yjoonjang/markers_bm) | Korean document retrieval dataset constructed by parsing PDFs from 5 domains: finance, public, medical, legal, and commerce | 823.60 |
| [PublicHealthQA](https://huggingface.co/datasets/xhluca/publichealth-qa) | Korean document retrieval dataset for medical and public health domains | 339.00 |
| [BelebeleRetrieval](https://huggingface.co/datasets/facebook/belebele) | Korean document retrieval dataset based on FLORES-200 | 243.11 |
| [MultiLongDocRetrieval](https://huggingface.co/datasets/Shitao/MLDR) | Korean long document retrieval dataset covering various domains | 13,813.44 |
<!-- | [MrTidyRetrieval](https://huggingface.co/datasets/mteb/mrtidy) | Korean document retrieval dataset based on Wikipedia | 166.90 | -->
<!-- | [MIRACLRetrieval](https://huggingface.co/datasets/miracl/miracl) | Korean document retrieval dataset based on Wikipedia | 166.63 | -->
We omit MIRACLRetrieval and MrTidyRetrieval in evalution due to our device conditions.


### Average Results

| Model                                         | Parameters | Average Recall@10 | Average Precision@10 | Average NDCG@10 | Average F1@10 |
|-----------------------------------------------|------------|----------------|-------------------|--------------|------------|
| **colbert-ko-v1**                   | **0.1B**     | **0.7999**    | **0.0930**       | **0.7172**  | **0.1655**|
| [jina-colbert-v2](https://huggingface.co/jinaai/jina-colbert-v2)                     | 0.5B         | 0.7518        | 0.0888           | 0.6671      | 0.1577    |

## Usage

### Sentence Transformers

This model can be used with [Sentence Transformers](https://www.sbert.net/) as a multi-vector (ColBERT-style late interaction) retriever via the `MultiVectorEncoder`:

```bash
pip install "sentence-transformers>=6.0.0"
```

```python
from sentence_transformers import MultiVectorEncoder

model = MultiVectorEncoder("yjoonjang/colbert-ko-v1")

query = "붉은 행성으로 알려진 행성은 무엇인가요?"
documents = [
    "금성은 크기와 근접성이 비슷하여 종종 지구의 쌍둥이라고 불린다.",
    "화성은 붉은 겉모습 때문에 종종 붉은 행성이라고 불린다.",
    "태양계에서 가장 큰 행성인 목성에는 뚜렷한 붉은 반점이 있다.",
    "고리로 유명한 토성은 때때로 붉은 행성으로 오인된다.",
]

query_embeddings = model.encode_query(query)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings[0].shape)
# (32, 128) (19, 128)

# MaxSim late-interaction scoring (higher is more relevant)
scores = model.similarity(query_embeddings, document_embeddings)
print(scores)
# tensor([[10.9423, 22.7836, 19.7410, 22.4239]])
```

### PyLate for reranking

If you only want to use the colbert model to perform reranking on top of your first-stage retrieval pipeline without building an index, you can simply use rank function and pass the queries and documents to rerank:

```python
from pylate import rank, models

queries = [
    "query A",
    "query B",
]

documents = [
    ["document A", "document B"],
    ["document 1", "document C", "document B"],
]

documents_ids = [
    [1, 2],
    [1, 3, 2],
]

model = models.ColBERT(
    model_name_or_path="yjoonjang/colbert-ko-v1",
)

queries_embeddings = model.encode(
    queries,
    is_query=True,
)

documents_embeddings = model.encode(
    documents,
    is_query=False,
)

reranked_documents = rank.rerank(
    documents_ids=documents_ids,
    queries_embeddings=queries_embeddings,
    documents_embeddings=documents_embeddings,
)
```

### Usage with [MUVERA](https://arxiv.org/abs/2405.19504)
First install the [muvera-py](https://github.com/sionic-ai/muvera-py) (Python implementation of MUVERA):

```bash
git clone --branch feat/pylate https://github.com/yjoonjang/muvera-py.git
cd muvera-py
```

Then run the main file:

```bash
uv run main_pylate.py
```

</details>

<details>
<summary>Usage with PLAID</summary>
First install the PyLate library:

```bash
pip install -U pylate
```

### Retrieval

Use this model with PyLate to index and retrieve documents. The index uses [FastPLAID](https://github.com/lightonai/fast-plaid) for efficient similarity search.

#### Indexing documents

Load the ColBERT model and initialize the PLAID index, then encode and index your documents:

```python
from pylate import indexes, models, retrieve

# Step 1: Load the ColBERT model
model = models.ColBERT(
    model_name_or_path="yjoonjang/colbert-ko-v1",
)

# Step 2: Initialize the PLAID index
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
    override=True,  # This overwrites the existing index if any
)

# Step 3: Encode the documents
documents_ids = ["1", "2", "3"]
documents = ["document 1 text", "document 2 text", "document 3 text"]

documents_embeddings = model.encode(
    documents,
    batch_size=32,
    is_query=False,  # Ensure that it is set to False to indicate that these are documents, not queries
    show_progress_bar=True,
)

# Step 4: Add document embeddings to the index by providing embeddings and corresponding ids
index.add_documents(
    documents_ids=documents_ids,
    documents_embeddings=documents_embeddings,
)
```

Note that you do not have to recreate the index and encode the documents every time. Once you have created an index and added the documents, you can re-use the index later by loading it:

```python
# To load an index, simply instantiate it with the correct folder/name and without overriding it
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
)
```

#### Retrieving top-k documents for queries

Once the documents are indexed, you can retrieve the top-k most relevant documents for a given set of queries.
To do so, initialize the ColBERT retriever with the index you want to search in, encode the queries and then retrieve the top-k documents to get the top matches ids and relevance scores:

```python
# Step 1: Initialize the ColBERT retriever
retriever = retrieve.ColBERT(index=index)

# Step 2: Encode the queries
queries_embeddings = model.encode(
    ["query for document 3", "query for document 1"],
    batch_size=32,
    is_query=True,  #  # Ensure that it is set to False to indicate that these are queries
    show_progress_bar=True,
)

# Step 3: Retrieve top-k documents
scores = retriever.retrieve(
    queries_embeddings=queries_embeddings,
    k=10,  # Retrieve the top 10 matches for each query
)
```
</details>

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

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details
* Loss: <code>pylate.losses.cached_contrastive.CachedContrastive</code>

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 32
- `learning_rate`: 3e-06
- `num_train_epochs`: 1
- `warmup_ratio`: 0.1
- `bf16`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 3e-06
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
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
- `multi_dataset_batch_sampler`: proportional

</details>

### Framework Versions
- Python: 3.10.18
- Sentence Transformers: 4.0.2
- PyLate: 1.3.0
- Transformers: 4.52.3
- PyTorch: 2.8.0+cu128
- Accelerate: 1.10.1
- Datasets: 3.6.0
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
    url = "https://arxiv.org/abs/1908.10084"
}
```

#### PyLate
```bibtex
@misc{PyLate,
title={PyLate: Flexible Training and Retrieval for Late Interaction Models},
author={Chaffin, Antoine and Sourty, Raphaël},
url={https://github.com/lightonai/pylate},
year={2024}
}
```

#### CachedContrastive
```bibtex
@misc{gao2021scaling,
    title={Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup},
    author={Luyu Gao and Yunyi Zhang and Jiawei Han and Jamie Callan},
    year={2021},
    eprint={2101.06983},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
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