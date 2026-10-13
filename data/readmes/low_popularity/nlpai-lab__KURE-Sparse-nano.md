---
tags:
- sentence-transformers
- sparse-encoder
- sparse
- splade
- learned-sparse-retrieval
- feature-extraction
language:
- ko
- en
base_model: nlpai-lab/KURE-v2-unsupervised
pipeline_tag: feature-extraction
library_name: sentence-transformers
license: apache-2.0
---

<a href="https://github.com/nlpai-lab/KURE">
  <img src="https://huggingface.co/nlpai-lab/KURE-v2/resolve/main/kure_logo.png" width="50%"/>
</a>


# 🔎 KURE-Sparse-nano

**KURE-Sparse-nano** is a compact (0.1B) Korean-English learned sparse retrieval model. It shows state-of-the-art performance among < 0.5B sparse models supporting Korean, averaging **0.7716** nDCG@10 on MTEB(kor, v2) Retrieval. It also outperforms much larger dense models, such as pplx-embed-v1-4b and harrier-oss-v1-27b.

## Key Characteristics

- **Learned Sparse Retrieval (LSR)**: every vector lives in a fixed vocabulary of 36,282 terms, so documents can be indexed in
  an inverted index and matched terms are inspectable.
- **Compact**: 0.1B parameters.
- **Long documents**: up to 8,192 tokens.
- **Sparse at both ends**: on average 147 active dimensions per query and 843 per document.

## Usage

```bash
pip install -U sentence-transformers
```

Use `encode_query` / `encode_document`: they add the query and document markers the model was trained with.

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("nlpai-lab/KURE-Sparse-nano", trust_remote_code=True)

query = "훈민정음은 언제 만들어졌나요?"
documents = [
    "세종대왕은 1443년에 훈민정음을 창제하고 1446년에 이를 반포하였다.",
    "김치는 배추나 무를 소금에 절인 뒤 고춧가루와 젓갈을 넣어 발효시킨 음식이다.",
    "한라산은 해발 1,947m로 남한에서 가장 높은 산이며 제주도 중앙에 자리한다.",
]

query_embeddings = model.encode_query(query)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# torch.Size([36282]) torch.Size([3, 36282])

# Dot-product scores (higher is more relevant)
scores = model.similarity(query_embeddings, document_embeddings)
print(scores)
# tensor([[119.3931,  11.5758,   6.4037]])
```

## Evaluation

KURE-Sparse-nano is evaluated on the nine **MTEB(kor, v2) Retrieval** tasks. We report nDCG@10.

| Model | Params | Avg | AutoRAG | PubHealthQA | Ko-StrategyQA | LawIRKo | SQuADKorV1 | Belebele (ko-ko) | MrTidy | MLDR | MIRACL |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Our Models** | | | | | | | | | | | |
| **[nlpai-lab/KURE-Sparse-base](https://huggingface.co/nlpai-lab/KURE-Sparse-base)** | 0.6B | **0.7984** | 0.9445 | 0.8099 | 0.8188 | 0.7244 | 0.9815 | 0.9703 | 0.6255 | 0.5716 | 0.7395 |
| **[nlpai-lab/KURE-Sparse-nano](https://huggingface.co/nlpai-lab/KURE-Sparse-nano)** | 0.1B | 0.7716 | 0.9360 | 0.7711 | 0.7924 | 0.7226 | 0.9774 | 0.9608 | 0.5618 | 0.5133 | 0.7091 |
| **Sparse Models** | | | | | | | | | | | |
| omai-research/milco-650m | 0.6B | 0.7824 | 0.9483 | 0.8219 | 0.8143 | 0.6724 | 0.9700 | 0.9623 | 0.6997 | 0.4318 | 0.7209 |
| telepix/PIXIE-Splade-v1.5 | 0.1B | 0.7608 | 0.9412 | 0.7910 | 0.7993 | 0.7667 | 0.9687 | 0.9651 | 0.5132 | 0.4938 | 0.6085 |
| yjoonjang/splade-ko-v1 | 0.1B | 0.7526 | 0.9423 | 0.7977 | 0.7583 | 0.6509 | 0.9754 | 0.9576 | 0.5299 | 0.5162 | 0.6451 |
| telepix/PIXIE-Splade-v1.0 | 0.1B | 0.6636 | 0.9597 | 0.7860 | 0.7352 | 0.5330 | 0.9417 | 0.9413 | 0.2909 | 0.3991 | 0.3858 |
| opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1 | 0.2B | 0.5444 | 0.6482 | 0.5506 | 0.5553 | 0.3554 | 0.7770 | 0.7321 | 0.5526 | 0.1219 | 0.6064 |
| **Dense (Single-Vector) Models** | | | | | | | | | | | |
| nvidia/Nemotron-3-Embed-8B-BF16 | 8.0B | 0.8127 | 0.9311 | 0.8898 | 0.8405 | 0.8481 | 0.9650 | 0.9714 | 0.6540 | 0.4785 | 0.7363 |
| sionic-ai/comsat-embed-ko-8b-preview | 7.6B | 0.7927 | 0.8518 | 0.8871 | 0.8394 | 0.8164 | 0.9168 | 0.9853 | 0.6253 | 0.5157 | 0.6964 |
| Qwen/Qwen3-Embedding-8B | 7.6B | 0.7826 | 0.8276 | 0.8721 | 0.8363 | 0.8171 | 0.9063 | 0.9824 | 0.6187 | 0.5046 | 0.6783 |
| nvidia/Nemotron-3-Embed-1B-BF16 | 1.1B | 0.7817 | 0.9074 | 0.8642 | 0.8136 | 0.7758 | 0.9505 | 0.9629 | 0.6084 | 0.4202 | 0.7325 |
| Qwen/Qwen3-Embedding-4B | 4.0B | 0.7737 | 0.8431 | 0.8693 | 0.8270 | 0.7769 | 0.9044 | 0.9522 | 0.6076 | 0.5022 | 0.6803 |
| perplexity-ai/pplx-embed-v1-4b | 4.0B | 0.7705 | 0.8321 | 0.9042 | 0.8326 | 0.7736 | 0.9402 | 0.9624 | 0.5778 | 0.4343 | 0.6775 |
| microsoft/harrier-oss-v1-27b | 27.0B | 0.7667 | 0.8176 | 0.8971 | 0.8361 | 0.8737 | 0.9204 | 0.9546 | 0.5306 | 0.4046 | 0.6653 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | 0.6B | 0.7653 | 0.9093 | 0.8337 | 0.8050 | 0.7735 | 0.9447 | 0.9518 | 0.5712 | 0.4304 | 0.6685 |
| codefuse-ai/F2LLM-v2-8B | 7.6B | 0.7638 | 0.7678 | 0.9380 | 0.8371 | 0.8405 | 0.8874 | 0.9513 | 0.6162 | 0.4047 | 0.6313 |
| telepix/PIXIE-Rune-v1.5 | 0.6B | 0.7618 | 0.8927 | 0.8426 | 0.8064 | 0.7705 | 0.9457 | 0.9617 | 0.5492 | 0.4482 | 0.6393 |
| [nlpai-lab/KURE-v1](https://huggingface.co/nlpai-lab/KURE-v1) | 0.6B | 0.7616 | 0.8708 | 0.8193 | 0.7999 | 0.7426 | 0.9357 | 0.9502 | 0.5909 | 0.4637 | 0.6816 |
| nvidia/llama-nemotron-embed-1b-v2 | 1.2B | 0.7564 | 0.8708 | 0.8177 | 0.8055 | 0.7329 | 0.9345 | 0.9519 | 0.5988 | 0.3952 | 0.7004 |
| dragonkue/BGE-m3-ko | 0.6B | 0.7547 | 0.8738 | 0.8155 | 0.7959 | 0.7322 | 0.9414 | 0.9503 | 0.6099 | 0.3899 | 0.6833 |
| BAAI/bge-m3 | 0.6B | 0.7509 | 0.8301 | 0.8041 | 0.7941 | 0.7174 | 0.9038 | 0.9315 | 0.6471 | 0.4287 | 0.7015 |
| perplexity-ai/pplx-embed-v1-0.6b | 0.6B | 0.7390 | 0.8414 | 0.8255 | 0.8100 | 0.7444 | 0.9174 | 0.9393 | 0.5524 | 0.3179 | 0.7026 |
| [nlpai-lab/KoE5](https://huggingface.co/nlpai-lab/KoE5) | 0.6B | 0.7337 | 0.8434 | 0.8351 | 0.8001 | 0.7756 | 0.8980 | 0.9425 | 0.5841 | 0.3015 | 0.6235 |
| Qwen/Qwen3-Embedding-0.6B | 0.6B | 0.7140 | 0.8338 | 0.8107 | 0.7586 | 0.7526 | 0.8490 | 0.9124 | 0.4870 | 0.4199 | 0.6023 |

### Performance-Sparsity

<p align="center">
  <img src="assets/ndcg_flops.png" width="80%" alt="Average nDCG@10 vs. average FLOPs of sparse retrievers on MTEB(kor, v2) Retrieval">
</p>

Average active dimensions per vector and FLOPs, averaged over the nine tasks.

| Model | Params | Query dims | Document dims | FLOPs |
| :--- | :--- | ---: | ---: | ---: |
| **KURE-Sparse-base** | 0.6B | 100 | 1,897 | 36.5 |
| **KURE-Sparse-nano** | 0.1B | 147 | 843 | 23.0 |
| omai-research/milco-650m | 0.6B | 105 | 1,167 | 32.3 |
| telepix/PIXIE-Splade-v1.5 | 0.1B | 117 | 1,541 | 37.3 |
| yjoonjang/splade-ko-v1 | 0.1B | 109 | 742 | 29.1 |
| telepix/PIXIE-Splade-v1.0 | 0.1B | 121 | 625 | 22.4 |
| opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1 | 0.2B | 29 | 176 | 6.8 |

### English Retrieval (BEIR)

KURE-Sparse-nano is also evaluated on the 13 English BEIR tasks (BEIR-13) with nDCG@10. SparseUp runs at its own length limits (128 query and 512 document tokens), and the other models at up to 8,192 tokens.

| Model | Params | BEIR-13 | FLOPs |
| :--- | :--- | ---: | ---: |
| **Our Models** | | | |
| **KURE-Sparse-base** | 0.6B | **0.5864** | 55.8 |
| **KURE-Sparse-nano** | 0.1B | 0.5317 | 37.0 |
| **Sparse Models** | | | |
| Linkup-Platform/linkup-sparseup-embed-v1 | 0.2B | 0.5645 | 8.5 |
| omai-research/milco-650m | 0.6B | 0.5545 | 20.6 |
| telepix/PIXIE-Splade-v1.5 | 0.1B | 0.4149 | 125.6 |

<details>
<summary>Per-task nDCG@10</summary>

| Model | Avg | ArguAna | ClimateFEVER | DBPedia | FEVER | FiQA | HotpotQA | NFCorpus | NQ | Quora | SCIDOCS | SciFact | TREC-COVID | Touche-2020 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Our Models** | | | | | | | | | | | | | | |
| **KURE-Sparse-base** | **0.5864** | 0.5896 | 0.3959 | 0.4837 | 0.9325 | 0.4720 | 0.8084 | 0.3678 | 0.6758 | 0.8252 | 0.1741 | 0.7183 | 0.8260 | 0.3535 |
| **KURE-Sparse-nano** | 0.5317 | 0.5075 | 0.2865 | 0.4214 | 0.9079 | 0.4080 | 0.7476 | 0.3340 | 0.5647 | 0.7825 | 0.1581 | 0.7120 | 0.7637 | 0.3183 |
| **Sparse Models** | | | | | | | | | | | | | | |
| Linkup-Platform/linkup-sparseup-embed-v1 | 0.5645 | 0.5648 | 0.3747 | 0.4150 | 0.8969 | 0.4687 | 0.7761 | 0.3523 | 0.5717 | 0.8656 | 0.1852 | 0.7376 | 0.7823 | 0.3478 |
| omai-research/milco-650m | 0.5545 | 0.6157 | 0.3079 | 0.4501 | 0.8353 | 0.4262 | 0.7780 | 0.3629 | 0.6495 | 0.8818 | 0.1704 | 0.7020 | 0.7476 | 0.2813 |
| telepix/PIXIE-Splade-v1.5 | 0.4149 | 0.2185 | 0.1302 | 0.3519 | 0.6475 | 0.2753 | 0.5756 | 0.3325 | 0.3858 | 0.6878 | 0.1468 | 0.6694 | 0.7068 | 0.2650 |

</details>

## Citation

```bibtex
@misc{kure-sparse,
  title  = {KURE-Sparse: a Korean-English bilingual learned sparse retriever},
  author = {Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Lim, Heuiseok},
  year   = {2026},
  url    = {https://huggingface.co/nlpai-lab/KURE-Sparse-nano},
}
```

```bibtex
@misc{kure-v2,
  title  = {KURE-v2: a Korean-English bilingual late-interaction retriever},
  author = {Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Lim, Heuiseok},
  year   = {2026},
  url    = {https://huggingface.co/nlpai-lab/KURE-v2},
}
```

```bibtex
@inproceedings{jang2025kure,
  title={KURE: Embedding Model for Korean-Specific Retrieval},
  author={Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Park, JeongBae and Lim, Heuiseok},
  booktitle={Annual Conference on Human and Language Technology},
  pages={129--134},
  year={2025},
  organization={Human and Language Technology}
}
```
