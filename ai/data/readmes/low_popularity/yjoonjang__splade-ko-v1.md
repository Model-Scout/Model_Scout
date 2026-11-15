---
tags:
- sentence-transformers
- sparse-encoder
- sparse
- splade
- generated_from_trainer
- loss:SpladeLoss
- loss:SparseMultipleNegativesRankingLoss
- loss:FlopsLoss
base_model: skt/A.X-Encoder-base
pipeline_tag: feature-extraction
library_name: sentence-transformers
license: apache-2.0
language:
- ko
---

# splade-ko-v1

**splade-ko-v1** is a Korean-specific SPLADE Sparse Encoder model finetuned from [skt/A.X-Encoder-base](https://huggingface.co/skt/A.X-Encoder-base) using the [sentence-transformers](https://www.SBERT.net) library. It maps sentences & paragraphs to a 50000-dimensional sparse vector space and can be used for semantic search and sparse retrieval.
## Model Details

### Model Description
- **Model Type:** SPLADE Sparse Encoder
- **Base model:** [skt/A.X-Encoder-base](https://huggingface.co/skt/A.X-Encoder-base) <!-- at revision b5c71f3601aedf38372fe21383ac7d04991af187 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 50000 dimensions
- **Similarity Function:** Dot Product

### Full Model Architecture

```
SparseEncoder(
  (0): MLMTransformer({'max_seq_length': 8192, 'do_lower_case': False, 'architecture': 'ModernBertForMaskedLM'})
  (1): SpladePooling({'pooling_strategy': 'max', 'activation_function': 'relu', 'word_embedding_dimension': 50000})
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
from sentence_transformers import SparseEncoder

# Download from the 🤗 Hub
model = SparseEncoder("yjoonjang/splade-ko-v1")
# Run inference
sentences = [
    '양이온 최적화 방법은 산소공공을 감소시키기 때문에 전자 농도가 증가하는 문제점을 갖고있을까?',
    '산화물 TFT 소자 신뢰성 열화기구\n그러나 이와 같은 양이온 최적화 방법은 산소공공을 감소시키기 때문에 전자농도 역시 감소하게 되어 전계 이동도가 감소하는 문제점을 않고 있다.\n이는 산화물 반도체의 전도기구가 Percolation Conduction에 따르기 때문이다. ',
    '세포대사 기능 분석을 위한 광학센서 기반 용존산소와 pH 측정 시스템의 제작 및 특성 분석\n수소이온 농도가 증가하는 경우인 \\( \\mathrm{pH} \\) 가 낮아지면 다수의 수소이온들과 충돌한 방출 광이 에너지를 잃고 짧은 검출시간을 갖는다. \n반대로 \\( \\mathrm{pH} \\)가 높아질수록 형광물질로부터 방출된 광의 수명이 길어져 긴 검출시간을 가진다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 50000]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 46.0239,  57.8961,  22.8014],
#         [ 57.8961, 270.6235,  56.5666],
#         [ 22.8014,  56.5666, 275.8828]], device='cuda:0')
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

## MTEB-ko-retrieval Leaderboard
Evaluated all the Korean Retrieval Benchmarks on [MTEB](https://github.com/embeddings-benchmark/mteb)
### Korean Retrieval Benchmark
| Dataset                                                               | Description                                                                                             | Average Length (characters) |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------|
| [Ko-StrategyQA](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA) | Korean ODQA multi-hop retrieval dataset (translated from StrategyQA)                                   | 305.15                      |
| [AutoRAGRetrieval](https://huggingface.co/datasets/yjoonjang/markers_bm) | Korean document retrieval dataset constructed by parsing PDFs across 5 domains: finance, public sector, healthcare, legal, and commerce         | 823.60                      |
| [MIRACLRetrieval](https://huggingface.co/datasets/miracl/miracl)         | Wikipedia-based Korean document retrieval dataset                                                              | 166.63                      |
| [PublicHealthQA](https://huggingface.co/datasets/xhluca/publichealth-qa)   | Korean document retrieval dataset for medical and public health domains                                                  | 339.00                      |
| [BelebeleRetrieval](https://huggingface.co/datasets/facebook/belebele)   | FLORES-200-based Korean document retrieval dataset                                                             | 243.11                      |
| [MrTidyRetrieval](https://huggingface.co/datasets/mteb/mrtidy)           | Wikipedia-based Korean document retrieval dataset                                                              | 166.90                      |
| [MultiLongDocRetrieval](https://huggingface.co/datasets/Shitao/MLDR)   | Korean long document retrieval dataset across various domains                                                               | 13,813.44                   |
<!-- - [XPQARetrieval](https://huggingface.co/datasets/jinaai/xpqa): 다양한 도메인의 한국어 문서 검색 데이터셋 -->

<details>
<summary>Reasons for excluding XPQARetrieval</summary>

- In our evaluation, we excluded the [XPQARetrieval](https://huggingface.co/datasets/jinaai/xpqa) dataset. XPQA is a dataset designed to evaluate Cross-Lingual QA capabilities, and we determined it to be inappropriate for evaluating retrieval tasks that require finding supporting documents based on queries.
- Examples from the XPQARetrieval dataset are as follows:
  ```json
  {
  	"query": "Is it unopened?",
  	"document": "No. It is a renewed product."
  },
  {
  	"query": "Is it compatible with iPad Air 3?",
  	"document": "Yes, it is possible."
  }
  ```
- Details for excluding this dataset is shown in the [Github Issue](https://github.com/embeddings-benchmark/mteb/discussions/3099)

</details>

### Evaluation Metrics
- Recall@10
- NDCG@10
- MRR@10
- AVG_Query_Active_Dims
- AVG_Corpus_Active_Dims

### Evaluation Code
Our evaluation uses the [SparseInformationRetrievalEvaluator](https://github.com/UKPLab/sentence-transformers/blob/master/sentence_transformers/sparse_encoder/evaluation/SparseInformationRetrievalEvaluator.py#L23-L308) from the [sentence-transformers](https://www.SBERT.net) library.
<details><summary>Code</summary>

```python
from sentence_transformers import SparseEncoder
from datasets import load_dataset
from sentence_transformers.sparse_encoder.evaluation import SparseInformationRetrievalEvaluator
import os
import pandas as pd
from tqdm import tqdm
import json
from multiprocessing import Process, current_process
import torch
from setproctitle import setproctitle
import traceback

# GPU별로 평가할 데이터셋 매핑
DATASET_GPU_MAPPING = {
	0: [
		"yjoonjang/markers_bm",
		"taeminlee/Ko-StrategyQA",
		"facebook/belebele",
		"xhluca/publichealth-qa",
		"Shitao/MLDR"
	],
	1: [
		"miracl/mmteb-miracl",
	],
	2: [
		"mteb/mrtidy",
	]
}

model_name = "yjoonjang/splade-ko-v1"

def evaluate_dataset(model_name, gpu_id, eval_datasets, output_dir):
	output_dir = f"{output_dir}/{model_name}"
	os.makedirs(output_dir, exist_ok=True)
	
	"""단일 GPU에서 할당된 데이터셋들을 평가하는 함수"""
	import torch
	try:
		device = torch.device(f"cuda:{str(gpu_id)}") 
		torch.cuda.set_device(device)
		
		setproctitle(f"yjoonjang splade-eval-gpu{gpu_id}")
		print(f"Running datasets: {eval_datasets} on GPU {gpu_id} in process {current_process().name}")
		
		# 모델 로드
		model = SparseEncoder(model_name, trust_remote_code=True, device=device)
		
		for eval_dataset in eval_datasets:
			short_dataset_name = eval_dataset.split("/")[-1]
			
			prediction_filepath = f"{output_dir}/{short_dataset_name}.json"
			if os.path.exists(prediction_filepath):
				print(f"Skipping evaluation for {eval_dataset} as output already exists at {prediction_filepath}")
				continue

			corpus = {}
			queries = {}
			relevant_docs = {}
			split = "dev"
			if eval_dataset == "yjoonjang/markers_bm" or eval_dataset == "yjoonjang/squad_kor_v1":
				split = "test"

			if eval_dataset in ["yjoonjang/markers_bm", "taeminlee/Ko-StrategyQA"]:
				dev_corpus = load_dataset(eval_dataset, "corpus", split="corpus")
				dev_queries = load_dataset(eval_dataset, "queries", split="queries")
				relevant_docs_data = load_dataset(eval_dataset, "default", split=split)
				
				queries = dict(zip(dev_queries["_id"], dev_queries["text"]))
				# Combine title and text if title exists (MTEB format)
				if "title" in dev_corpus.column_names and "text" in dev_corpus.column_names:
					corpus = {
						row["_id"]: (row["title"] + " " + row["text"]).strip()
						for row in dev_corpus
					}
				elif "text" in dev_corpus.column_names:
					corpus = dict(zip(dev_corpus["_id"], dev_corpus["text"]))
				else:
					raise ValueError(f"Corpus dataset must have 'text' field")
				for row in relevant_docs_data:
					qid_str = str(row["query-id"])
					corpus_ids_str = str(row["corpus-id"])
					score = row.get("score", 1)  # Default to 1 if no score field
					if score >= 1:  # Only include relevant documents (score >= 1)
						if qid_str not in relevant_docs:
							relevant_docs[qid_str] = set()
						relevant_docs[qid_str].add(corpus_ids_str)

			elif eval_dataset == "facebook/belebele":
				split = "test"
				ds = load_dataset(eval_dataset, "kor_Hang", split=split)
				
				corpus_df = pd.DataFrame(ds)
				corpus_df = corpus_df.drop_duplicates(subset=["link"])
				corpus_df["cid"] = [f"C{i}" for i in range(len(corpus_df))]
				corpus = dict(zip(corpus_df["cid"], corpus_df["flores_passage"]))
				
				link_to_cid = dict(zip(corpus_df["link"], corpus_df["cid"]))
				
				queries_df = pd.DataFrame(ds)
				queries_df = queries_df.drop_duplicates(subset=["question"])
				queries_df["qid"] = [f"Q{i}" for i in range(len(queries_df))]
				queries = dict(zip(queries_df["qid"], queries_df["question"]))
				
				question_to_qid = dict(zip(queries_df["question"], queries_df["qid"]))

				for row in tqdm(ds, desc="Processing belebele"):
					qid = question_to_qid[row["question"]]
					cid = link_to_cid[row["link"]]
					if qid not in relevant_docs:
						relevant_docs[qid] = set()
					relevant_docs[qid].add(cid)

			elif eval_dataset == "miracl/mmteb-miracl":
				split = "dev"
				corpus_ds = load_dataset(eval_dataset, "corpus-ko", split="corpus", trust_remote_code=True)
				queries_ds = load_dataset(eval_dataset, "queries-ko", split="queries", trust_remote_code=True)
				qrels_ds = load_dataset(eval_dataset, "ko", split=split, trust_remote_code=True)

				# Combine title and text if title exists (MTEB format)
				if "title" in corpus_ds.column_names:
					corpus = {
						row['docid']: (row['title'] + " " + row['text']).strip()
						for row in corpus_ds
					}
				else:
					corpus = {row['docid']: row['text'] for row in corpus_ds}
				queries = {row['query_id']: row['query'] for row in queries_ds}

				for row in qrels_ds:
					qid = row["query_id"]
					cid = row["docid"]
					score = row.get("score", 1)  # Default to 1 if no score field
					if score >= 1:  # Only include relevant documents (score >= 1)
						if qid not in relevant_docs:
							relevant_docs[qid] = set()
						relevant_docs[qid].add(cid)

			elif eval_dataset == "mteb/mrtidy":
				split = "test"
				corpus_ds = load_dataset(eval_dataset, "korean-corpus", split="train", trust_remote_code=True)
				queries_ds = load_dataset(eval_dataset, "korean-queries", split=split, trust_remote_code=True)
				qrels_ds = load_dataset(eval_dataset, "korean-qrels", split=split, trust_remote_code=True)

				# Combine title and text if title exists (MTEB format)
				if "title" in corpus_ds.column_names and "text" in corpus_ds.column_names:
					corpus = {
						row["_id"]: (row["title"] + " " + row["text"]).strip()
						for row in corpus_ds
					}
				elif "text" in corpus_ds.column_names:
					corpus = {row['_id']: row['text'] for row in corpus_ds}
				else:
					raise ValueError(f"Corpus dataset must have 'text' field")
				queries = {row['_id']: row['text'] for row in queries_ds}

				for row in qrels_ds:
					qid = str(row["query-id"])
					cid = str(row["corpus-id"])
					score = row.get("score", 1)  # Default to 1 if no score field
					if score >= 1:  # Only include relevant documents (score >= 1)
						if qid not in relevant_docs:
							relevant_docs[qid] = set()
						relevant_docs[qid].add(cid)

			elif eval_dataset == "Shitao/MLDR":
				split = "dev"
				corpus_ds = load_dataset(eval_dataset, "corpus-ko", split="corpus", trust_remote_code=True)
				lang_data = load_dataset(eval_dataset, "ko", split=split, trust_remote_code=True)
				
				# Combine title and text if title exists (MTEB format)
				if "title" in corpus_ds.column_names:
					corpus = {
						row['docid']: (row['title'] + " " + row['text']).strip()
						for row in corpus_ds
					}
				else:
					corpus = {row['docid']: row['text'] for row in corpus_ds}
				queries = {row['query_id']: row['query'] for row in lang_data}

				for row in lang_data:
					qid = row["query_id"]
					cid = row["positive_passages"][0]["docid"]
					if qid not in relevant_docs:
						relevant_docs[qid] = set()
					relevant_docs[qid].add(cid)

			elif eval_dataset == "xhluca/publichealth-qa":
				split = "test"
				ds = load_dataset(eval_dataset, "korean", split=split, trust_remote_code=True)
				
				ds = ds.filter(lambda x: x["question"] is not None and x["answer"] is not None)
				
				corpus_df = pd.DataFrame(list(ds))
				corpus_df = corpus_df.drop_duplicates(subset=["answer"])
				corpus_df["cid"] = [f"D{i}" for i in range(len(corpus_df))]
				corpus = dict(zip(corpus_df["cid"], corpus_df["answer"]))
				answer_to_cid = dict(zip(corpus_df["answer"], corpus_df["cid"]))

				queries_df = pd.DataFrame(list(ds))
				queries_df = queries_df.drop_duplicates(subset=["question"])
				queries_df["qid"] = [f"Q{i}" for i in range(len(queries_df))]
				queries = dict(zip(queries_df["qid"], queries_df["question"]))
				question_to_qid = dict(zip(queries_df["question"], queries_df["qid"]))
				
				for row in tqdm(ds, desc="Processing publichealth-qa"):
					qid = question_to_qid[row["question"]]
					cid = answer_to_cid[row["answer"]]
					if qid not in relevant_docs:
						relevant_docs[qid] = set()
					relevant_docs[qid].add(cid)

			else:
				continue
			
			if torch.cuda.get_device_name().startswith('NVIDIA A100'):
				batch_size = 16
			else:
				batch_size = 4
					
			evaluator = SparseInformationRetrievalEvaluator(
				queries=queries,
				corpus=corpus,
				relevant_docs=relevant_docs,
				write_csv=False,
				name=f"{eval_dataset}",
				show_progress_bar=True,
				batch_size=batch_size,
				write_predictions=False
			)
			short_dataset_name = eval_dataset.split("/")[-1]
			output_filepath = f"{output_dir}/{short_dataset_name}.json"
			metrics = evaluator(model)
			print(f"GPU {gpu_id} - {eval_dataset} metrics: {metrics}")
			with open(output_filepath, "w", encoding="utf-8") as f:
				json.dump(metrics, f, ensure_ascii=False, indent=2)
				
	except Exception as ex:
		print(f"Error on GPU {gpu_id}: {ex}")
		traceback.print_exc()

if __name__ == "__main__":
	torch.multiprocessing.set_start_method('spawn')
	
	print(f"Starting evaluation for model: {model_name}")
	output_dir = "./results_inference_free_new_idf"
	# output_dir = "./results_inference_free_new"
	processes = []
	
	for gpu_id, datasets in DATASET_GPU_MAPPING.items():
		p = Process(target=evaluate_dataset, args=(model_name, gpu_id, datasets, output_dir))
		p.start()
		processes.append(p)
	
	for p in processes:
		p.join()
	
	print(f"Completed evaluation for model: {model_name}")
```
</details>

### Evaluation Results

| Model | Parameters | Recall@10 | NDCG@10 | MRR@10 | AVG_Query_Active_Dims | AVG_Corpus_Active_Dims |
|-------|------------|-----------|---------|--------|----------------------|------------------------|
| **yjoonjang/splade-ko-v1** | **0.1B** | **0.8391** | **0.7376** | **0.7260** | **110.7664** | **783.7026** |
| [telepix/PIXIE-Splade-Preview](https://huggingface.co/telepix/PIXIE-Splade-Preview) | 0.1B | 0.8107 | 0.7175 | 0.7072 | 30.481 | 566.8242 |
| [opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1](https://huggingface.co/opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1) | 0.1B | 0.6570 | 0.5383 | 0.5233 | 27.8722 | 177.5564 |

### Comparison with Dense Embedding models (NDCG@10)

Look [here](https://github.com/nlpai-lab/KURE/tree/leaderboard?tab=readme-ov-file#average-results) for more details.
| Model | Parameters | Average NDCG@10 |
| :--- | :--- | :--- |
| **Sparse Embedding**  |
| yjoonjang/splade-ko-v1 | 0.1B | 0.7376 |
| telepix/PIXIE-Splade-Preview | 0.1B | 0.7175 |
| opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1 | 0.1B | 0.5383 |
||||
| **Dense Embedding**  |
| Qwen/Qwen3-Embedding-8B | 8B | 0.7635 |
| Qwen/Qwen3-Embedding-4B | 4B | 0.7484 |
| telepix/PIXIE-Rune-Preview | 0.6B | 0.7420 |
| nlpai-lab/KURE-v1 | 0.6B | 0.7395 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | 0.6B | 0.7386 |
| telepix/PIXIE-Spell-Preview-1.7B | 1.7B | 0.7342 |
| BAAI/bge-m3 | 0.6B | 0.7339 |
| dragonkue/BGE-m3-ko | 0.6B | 0.7312 |
| Snowflake/snowflake-arctic-embed-l-v2.0 | 0.6B | 0.7179 |
| telepix/PIXIE-Spell-Preview-0.6B | 0.6B | 0.7106 |
| intfloat/multilingual-e5-large | 0.6B | 0.7075 |
| FronyAI/frony-embed-medium-arctic-ko-v2.5 | 0.6B | 0.7067 |
| nlpai-lab/KoE5 | 0.6B | 0.7043 |
| google/embeddinggemma-300m | 0.3B | 0.6944 |
| BAAI/bge-multilingual-gemma2 | 9.4B | 0.6931 |
| Qwen/Qwen3-Embedding-0.6B | 0.6B | 0.6895 |
| Alibaba-NLP/gte-multilingual-base | 0.3B | 0.6879 |
| jinaai/jina-embeddings-v3 | 0.6B | 0.6872 |
| SamilPwC-AXNode-GenAI/PwC-Embedding_expr | 0.6B | 0.6846 |
| nomic-ai/nomic-embed-text-v2-moe | 0.5B | 0.6799 |
| intfloat/multilingual-e5-large-instruct | 0.6B | 0.6799 |
| intfloat/multilingual-e5-base | 0.3B | 0.6709 |
| Alibaba-NLP/gte-Qwen2-7B-instruct | 7.6B | 0.6689 |
| intfloat/e5-mistral-7b-instruct | 7.1B | 0.6649 |
| openai/text-embedding-3-large | Unkown | 0.6513 |
| upskyy/bge-m3-korean | 0.6B | 0.6434 |
| Salesforce/SFR-Embedding-2_R | 2.6B | 0.6391 |
| jhgan/ko-sroberta-multitask | 0.1B | 0.5165 |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 2
- `learning_rate`: 2e-05
- `num_train_epochs`: 2
- `warmup_ratio`: 0.1
- `bf16`: True
- `negs_per_query`: 6 (from our dataset)
- `gather_device`: True (Makes samples available to be shared across devices)

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 2
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
- `num_train_epochs`: 2
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
- `local_rank`: 7
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
- `parallelism_config`: None
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
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
</details>

### Framework Versions
- Python: 3.10.18
- Sentence Transformers: 5.1.1
- Transformers: 4.56.2
- PyTorch: 2.8.0+cu128
- Accelerate: 1.10.1
- Datasets: 4.1.1
- Tokenizers: 0.22.1

## Citation

### BibTeX
```bitex
@software{spladeko,
  author       = {Youngjoon, Jang},
  title        = {splade-ko-v1},
  subtitle     = {Independent Korean SPLADE Model for the Industry},
  publisher    = {Hugging Face},
  year         = {2025},
  version      = {1.0.0},
  url          = {https://huggingface.co/yjoonjang/splade-ko-v1}
}
```

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

#### SpladeLoss
```bibtex
@misc{formal2022distillationhardnegativesampling,
      title={From Distillation to Hard Negative Sampling: Making Sparse Neural IR Models More Effective},
      author={Thibault Formal and Carlos Lassance and Benjamin Piwowarski and Stéphane Clinchant},
      year={2022},
      eprint={2205.04733},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2205.04733},
}
```

#### SparseMultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

#### FlopsLoss
```bibtex
@article{paria2020minimizing,
    title={Minimizing flops to learn efficient sparse representations},
    author={Paria, Biswajit and Yeh, Chih-Kuan and Yen, Ian EH and Xu, Ning and Ravikumar, Pradeep and P{'o}czos, Barnab{'a}s},
    journal={arXiv preprint arXiv:2004.05665},
    year={2020}
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