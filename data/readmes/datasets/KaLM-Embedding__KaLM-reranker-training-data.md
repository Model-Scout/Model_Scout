---
license: mit
language:
- multilingual
- ar
- bn
- de
- en
- es
- fa
- fi
- fr
- hi
- id
- ja
- ko
- ru
- sw
- te
- th
- yo
- zh
size_categories:
- 1M<n<10M
task_categories:
- text-ranking
- text-retrieval
tags:
- reranking
- retrieval
- instruction-tuning
- knowledge-distillation
- information-retrieval
- hard-negative-mining
- query-document-pairs
pretty_name: ' KaLM-Reranker Training Data'
---

# Lychee-KaLM-Reranker Training Data

A large-scale, ready-to-use multilingual dataset for fine-tuning reranking models.

This repository contains **3,885,265 training samples** collected from **54 datasets**, covering English, Chinese, and multilingual retrieval tasks. Each sample includes task instructions, positive passages, at least 16 hard negatives, and teacher scores annotated by **Qwen3-Reranker-8B**.

When expanded into point-wise query–passage pairs, the dataset provides **at least 66 million training instances.**

All datasets have been preprocessed and stored in Parquet format, allowing them to be used directly for reranker fine-tuning.


## Languages
The dataset contains Multilingual, English, and Chinese data.

## Dataset Structure
Each sample follows the structure below:
- `prompt`, `string`, the task instruction
- `query`, `string`, one query per sample
- `pos`, `list[string]`, containing one or more positive examples
- `neg`, `list[string]`, containing at least 16 negative examples
- `pos_scores`, `list[float]`, the scores assigned to the positive examples by Qwen3-Reranker-8B, calculated as the `yes` logit minus the `no` logit
- `neg_scores`, `list[float]`, the scores assigned to the negative examples by Qwen3-Reranker-8B, calculated as the `yes` logit minus the `no` logit

Each score is calculated as the `yes` logit minus the `no` logit:

```text
score = yes_logit - no_logit
```

Applying the sigmoid function to a score gives the teacher model's probability of predicting `yes`:

```text
P(yes) = sigmoid(score) = 1 / (1 + exp(-score))
```

## Usage

Install the Hugging Face `datasets` library:

```bash
pip install datasets
```

Stream the complete dataset without downloading all files:

```python
from datasets import load_dataset

dataset = load_dataset(
    "KaLM-Embedding/KaLM-reranker-training-data",
    split="train",
    streaming=True,
)
```

Load a specific source dataset:

```python
from datasets import load_dataset

dataset = load_dataset(
    "KaLM-Embedding/KaLM-reranker-training-data",
    data_dir="msmarco",
    split="train",
)
```

## Dataset Summary
All these datasets have been preprocessed and can be used directly to fine-tune your reranking or retrieval models.

| Dataset | Language | Size | Number of Parquet Files | URL |
|---|:---:|---:|---:|---|
| `advertisegen` | zh | 17,526 | 1 | [Source](https://huggingface.co/datasets/shibing624/AdvertiseGen) |
| `arguana` | en | 8,130 | 1 | [Source](https://zenodo.org/records/3973258) |
| `arxiv_qa` | en | 17,927 | 1 | [Source](https://huggingface.co/datasets/TitanMLData/arxiv_qa) |
| `aya_dataset` | ml | 26,292 | 1 | [Source](https://huggingface.co/datasets/CohereLabs/aya_dataset) |
| `ccnews` | en | 28,246 | 1 | [Source](https://edoc.hu-berlin.de/items/ad915f2d-bb2c-4abd-887f-3d50bd3f2516) |
| `ccovid-news` | zh | 4,727 | 1 | [Source](https://www.datafountain.cn/competitions/424/datasets) |
| `chef` | zh | 4,824 | 1 | [Source](https://github.com/THU-BPM/CHEF) |
| `cmedqa-v2.0` | zh | 88,109 | 2 | [Source](https://huggingface.co/datasets/wangrongsheng/cMedQA-V2.0) |
| `cmrc2018` | zh | 9,753 | 1 | [Source](https://huggingface.co/datasets/erhwenkuo/squad-cmrc2018-zhtw) |
| `codefeedback` | en | 49,090 | 1 | [Source](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction) |
| `cord19_trec-covid` | en | 48,517 | 1 | [Source](https://huggingface.co/datasets/irds/cord19_trec-covid) |
| `cqa_massive` | en | 22,065 | 1 | [CQADupStack](http://nlp.cis.unimelb.edu.au/resources/cqadupstack/) |
| `csl` | zh | 19,945 | 1 | [Source](https://huggingface.co/datasets/neuclir/csl) |
| `dbpedia-entity` | en | 96,792 | 2 | [Source](https://github.com/iai-group/DBpedia-Entity/) |
| `drcd` | zh | 4,714 | 1 | [Source](https://huggingface.co/datasets/voidful/DRCD) |
| `dureader` | zh | 79,229 | 2 | [Source](https://huggingface.co/datasets/sentence-transformers/dureader) |
| `dureader_mrc` | zh | 97,764 | 2 | [DuReader Checklist](https://huggingface.co/datasets/luozhouyang/dureader) |
| `esci` | en | 26,043 | 1 | [Source](https://huggingface.co/datasets/tasksource/esci) |
| `expertqa` | en | 1,252 | 1 | [Source](https://github.com/chaitanyamalaviya/ExpertQA) |
| `fever` | en | 87,216 | 2 | [Source](https://huggingface.co/datasets/maxzoech/fever) |
| `fiqa` | en | 4,689 | 1 | [Source](https://huggingface.co/datasets/irds/beir_fiqa_train) |
| `gooaq` | en | 49,833 | 1 | [Source](https://github.com/allenai/gooaq) |
| `hotpotqa` | en | 234,381 | 5 | [HotpotQA](https://huggingface.co/datasets/hotpotqa/hotpot_qa)<br>[BGE-M3](https://huggingface.co/datasets/Shitao/bge-m3-data) |
| `law-gpt` | zh | 500 | 1 | [Source](https://huggingface.co/datasets/sentence-transformers/law-gpt) |
| `lawzhidao` | zh | 6,784 | 1 | [Source](https://www.heywhale.com/mw/dataset/5e953ca8e7ec38002d02fca7/content) |
| `lcsts` | zh | 19,535 | 1 | [Source](https://huggingface.co/datasets/hugcyp/LCSTS) |
| `lima-chinese` | zh | 1,991 | 1 | [Source](https://huggingface.co/datasets/paralym/lima-chinese) |
| `medi2bge` | en | 71,790 | 2 | [Source](https://huggingface.co/datasets/GritLM/MEDI2BGE) |
| `miracl` | ml | 128,174 | 3 | [Source](https://huggingface.co/datasets/sentence-transformers/miracl) |
| `mldr` | ml | 41,434 | 1 | [Source](https://huggingface.co/datasets/sentence-transformers/mldr) |
| `mmarco-chinese` | zh | 379,870 | 8 | [Source](https://huggingface.co/datasets/unicamp-dl/mmarco) |
| `mr-tydi` | ml | 96,124 | 2 | [Source](https://huggingface.co/datasets/castorini/mr-tydi) |
| `msmarco` | en | 909,775 | 19 | [MS MARCO Passage](https://huggingface.co/datasets/Tevatron/msmarco-passage)<br>[MS MARCO V2](https://huggingface.co/datasets/mteb/msmarco-v2)<br>[BGE-M3](https://huggingface.co/datasets/Shitao/bge-m3-data) |
| `multi-cpr` | zh | 234,587 | 5 | [Source](https://github.com/Alibaba-NLP/Multi-CPR) |
| `nfcorpus` | en | 10,471 | 1 | [Source](https://huggingface.co/datasets/BeIR/nfcorpus-generated-queries) |
| `nq` | en | 114,931 | 3 | [Wikipedia-NQ](https://huggingface.co/datasets/Tevatron/wikipedia-nq)<br>[BGE-M3](https://huggingface.co/datasets/Shitao/bge-m3-data) |
| `openorca` | en | 38,623 | 1 | [Source](https://huggingface.co/datasets/Open-Orca/OpenOrca) |
| `paq_pairs` | en | 49,849 | 1 | [PAQ](https://huggingface.co/datasets/sentence-transformers/paq) |
| `pubmedqa` | en | 79,954 | 2 | [Source](https://huggingface.co/datasets/qiaojin/PubMedQA) |
| `quora` | en | 83,098 | 2 | [Quora Question Pairs](https://huggingface.co/datasets/AlekseyKorshuk/quora-question-pairs) |
| `rag-dataset-12000` | en | 9,272 | 1 | [Source](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000) |
| `refgpt` | zh | 49,896 | 1 | [Source](https://github.com/sufengniu/RefGPT) |
| `retrieval_data_llm_infgrad` | zh | 32,551 | 1 | [Source](https://huggingface.co/datasets/infgrad/retrieval_data_llm) |
| `scifact` | en | 794 | 1 | [Source](https://huggingface.co/datasets/Tevatron/scifact) |
| `searchqa` | en | 9,988 | 1 | [Source](https://huggingface.co/datasets/kyunghyuncho/search_qa) |
| `squad_v2` | en | 125,816 | 3 | [Source](https://huggingface.co/datasets/rajpurkar/squad_v2) |
| `t2ranking` | zh | 188,606 | 4 | [Source](https://huggingface.co/datasets/THUIR/T2Ranking) |
| `thucnews` | zh | 19,288 | 1 | [Source](https://huggingface.co/datasets/SirlyDreamer/THUCNews) |
| `triviaqa` | en | 104,725 | 3 | [TriviaQA](https://huggingface.co/datasets/multi-train/emb-triviaqa-train)<br>[BGE-M3](https://huggingface.co/datasets/Shitao/bge-m3-data) |
| `umetrip-qa` | zh | 2,537 | 1 | [Source](https://aistudio.baidu.com/datasetdetail/149933) |
| `webcpm` | zh | 1,602 | 1 | [Source](https://github.com/thunlp/WebCPM) |
| `webgpt_comparisons` | en | 18,924 | 1 | [Source](https://huggingface.co/datasets/openai/webgpt_comparisons) |
| `webqa` | zh | 4,988 | 1 | [Source](https://huggingface.co/datasets/suolyer/webqa) |
| `yahoo-answers` | en | 21,724 | 1 | [Source](https://huggingface.co/datasets/sentence-transformers/yahoo-answers) |
| **Total** | — | **3,885,265** | **107** | — |

Here, `en`, `zh`, and `ml` denote English, Chinese, and multilingual data, respectively.

# Citation
If you find these datasets useful, please consider citing our paper.

```
@misc{zhao2026kalmrerankerv1,
      title={KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking}, 
      author={Xinping Zhao and Jiaxin Xu and Ziqi Dai and Xin Zhang and Shouzheng Huang and Danyu Tang and Xinshuo Hu and Meishan Zhang and Baotian Hu and Min Zhang},
      year={2026},
      eprint={2606.22807},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.22807}, 
}

@misc{zhao2025kalmembeddingv2,
      title={KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model}, 
      author={Xinping Zhao and Xinshuo Hu and Zifei Shan and Shouzheng Huang and Yao Zhou and Xin Zhang and Zetian Sun and Zhenyu Liu and Dongfang Li and Xinyuan Wei and Youcheng Pan and Yang Xiang and Meishan Zhang and Haofen Wang and Jun Yu and Baotian Hu and Min Zhang},
      year={2025},
      eprint={2506.20923},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.20923}, 
}

@misc{hu2025kalmembedding,
      title={KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model}, 
      author={Xinshuo Hu and Zifei Shan and Xinping Zhao and Zetian Sun and Zhenyu Liu and Dongfang Li and Shaolin Ye and Xinyuan Wei and Qian Chen and Baotian Hu and Haofen Wang and Jun Yu and Min Zhang},
      year={2025},
      eprint={2501.01028},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.01028}, 
}
```

## Contact
If you encounter any issues, feel free to contact us via the email: <zhaoxinping@stu.hit.edu.cn>