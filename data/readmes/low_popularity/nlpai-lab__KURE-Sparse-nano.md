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

<p align="center">
  <img src="assets/kure_ndcg.png" width="100%" alt="Average nDCG@10 on MTEB(kor, v2) Retrieval of the KURE models and baseline retrievers">
</p>

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

| Model | Type | Params | Avg | AutoRAG | PubHealthQA | Ko-StrategyQA | LawIRKo | SQuADKorV1 | Belebele (ko-ko) | MrTidy | MLDR | MIRACL |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **KURE Models** | | | | | | | | | | | | |
| **[nlpai-lab/KURE-Sparse-nano](https://huggingface.co/nlpai-lab/KURE-Sparse-nano)** | Sparse | 0.1B | **0.7716** | 0.9360 | 0.7711 | 0.7924 | 0.7226 | 0.9774 | 0.9608 | 0.5618 | 0.5133 | 0.7091 |
| [nlpai-lab/KURE-v3](https://huggingface.co/nlpai-lab/KURE-v3) | Dense | 1.1B | 0.8027 | 0.9324 | 0.8639 | 0.8192 | 0.8158 | 0.9666 | 0.9673 | 0.6320 | 0.4781 | 0.7489 |
| [nlpai-lab/KURE-v2](https://huggingface.co/nlpai-lab/KURE-v2) | Late-interaction | 0.2B | 0.8160 | 0.9718 | 0.8228 | 0.8070 | 0.7550 | 0.9846 | 0.9660 | 0.5974 | 0.7158 | 0.7237 |
| [nlpai-lab/KURE-Sparse-base](https://huggingface.co/nlpai-lab/KURE-Sparse-base) | Sparse | 0.6B | 0.7984 | 0.9445 | 0.8099 | 0.8188 | 0.7244 | 0.9815 | 0.9703 | 0.6255 | 0.5716 | 0.7395 |
| [nlpai-lab/KURE-v1](https://huggingface.co/nlpai-lab/KURE-v1) | Dense | 0.6B | 0.7616 | 0.8708 | 0.8193 | 0.7999 | 0.7426 | 0.9357 | 0.9502 | 0.5909 | 0.4637 | 0.6816 |
| [nlpai-lab/KoE5](https://huggingface.co/nlpai-lab/KoE5) | Dense | 0.6B | 0.7337 | 0.8434 | 0.8351 | 0.8001 | 0.7756 | 0.8980 | 0.9425 | 0.5841 | 0.3015 | 0.6235 |
| **Dense (Single-Vector) Models** | | | | | | | | | | | | |
| nvidia/Nemotron-3-Embed-8B-BF16 | Dense | 8.0B | 0.8127 | 0.9311 | 0.8898 | 0.8405 | 0.8481 | 0.9650 | 0.9714 | 0.6540 | 0.4785 | 0.7363 |
| sionic-ai/comsat-embed-ko-8b-preview | Dense | 7.6B | 0.7927 | 0.8518 | 0.8871 | 0.8394 | 0.8164 | 0.9168 | 0.9853 | 0.6253 | 0.5157 | 0.6964 |
| Qwen/Qwen3-Embedding-8B | Dense | 7.6B | 0.7826 | 0.8276 | 0.8721 | 0.8363 | 0.8171 | 0.9063 | 0.9824 | 0.6187 | 0.5046 | 0.6783 |
| nvidia/Nemotron-3-Embed-1B-BF16 | Dense | 1.1B | 0.7817 | 0.9074 | 0.8642 | 0.8136 | 0.7758 | 0.9505 | 0.9629 | 0.6084 | 0.4202 | 0.7325 |
| Qwen/Qwen3-Embedding-4B | Dense | 4.0B | 0.7737 | 0.8431 | 0.8693 | 0.8270 | 0.7769 | 0.9044 | 0.9522 | 0.6076 | 0.5022 | 0.6803 |
| perplexity-ai/pplx-embed-v1-4b | Dense | 4.0B | 0.7705 | 0.8321 | 0.9042 | 0.8326 | 0.7736 | 0.9402 | 0.9624 | 0.5778 | 0.4343 | 0.6775 |
| microsoft/harrier-oss-v1-27b | Dense | 27.0B | 0.7667 | 0.8176 | 0.8971 | 0.8361 | 0.8737 | 0.9204 | 0.9546 | 0.5306 | 0.4046 | 0.6653 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | Dense | 0.6B | 0.7653 | 0.9093 | 0.8337 | 0.8050 | 0.7735 | 0.9447 | 0.9518 | 0.5712 | 0.4304 | 0.6685 |
| codefuse-ai/F2LLM-v2-8B | Dense | 7.6B | 0.7638 | 0.7678 | 0.9380 | 0.8371 | 0.8405 | 0.8874 | 0.9513 | 0.6162 | 0.4047 | 0.6313 |
| telepix/PIXIE-Rune-v1.5 | Dense | 0.6B | 0.7618 | 0.8927 | 0.8426 | 0.8064 | 0.7705 | 0.9457 | 0.9617 | 0.5492 | 0.4482 | 0.6393 |
| nvidia/llama-nemotron-embed-1b-v2 | Dense | 1.2B | 0.7564 | 0.8708 | 0.8177 | 0.8055 | 0.7329 | 0.9345 | 0.9519 | 0.5988 | 0.3952 | 0.7004 |
| dragonkue/BGE-m3-ko | Dense | 0.6B | 0.7547 | 0.8738 | 0.8155 | 0.7959 | 0.7322 | 0.9414 | 0.9503 | 0.6099 | 0.3899 | 0.6833 |
| BAAI/bge-m3 | Dense | 0.6B | 0.7509 | 0.8301 | 0.8041 | 0.7941 | 0.7174 | 0.9038 | 0.9315 | 0.6471 | 0.4287 | 0.7015 |
| jinaai/jina-embeddings-v5-text-small-retrieval | Dense | 0.6B | 0.7419 | 0.8409 | 0.8664 | 0.8096 | 0.7483 | 0.8926 | 0.9346 | 0.5779 | 0.3315 | 0.6752 |
| perplexity-ai/pplx-embed-v1-0.6b | Dense | 0.6B | 0.7390 | 0.8414 | 0.8255 | 0.8100 | 0.7444 | 0.9174 | 0.9393 | 0.5524 | 0.3179 | 0.7026 |
| google/embeddinggemma-300m | Dense | 0.3B | 0.7254 | 0.8187 | 0.8170 | 0.8008 | 0.6850 | 0.9114 | 0.9430 | 0.5253 | 0.3844 | 0.6434 |
| Qwen/Qwen3-Embedding-0.6B | Dense | 0.6B | 0.7140 | 0.8338 | 0.8107 | 0.7586 | 0.7526 | 0.8490 | 0.9124 | 0.4870 | 0.4199 | 0.6023 |
| **Late-interaction (Multi-Vector) Models** | | | | | | | | | | | | |
| lightonai/mLateOn | Late-interaction | 0.3B | 0.7906 | 0.9392 | 0.8061 | 0.7905 | 0.6431 | 0.9803 | 0.9608 | 0.5817 | 0.7005 | 0.7135 |
| perplexity-ai/pplx-embed-v1-late-0.6b | Late-interaction | 0.6B | 0.7381 | 0.8557 | 0.8089 | 0.7973 | 0.7285 | 0.9696 | 0.9548 | 0.5400 | 0.2816 | 0.7064 |
| dragonkue/colbert-ko-0.1b | Late-interaction | 0.1B | 0.6776 | 0.9700 | 0.7482 | 0.7364 | 0.4475 | 0.9794 | 0.9644 | 0.3966 | 0.2872 | 0.5685 |
| **Sparse Models** | | | | | | | | | | | | |
| omai-research/milco-650m | Sparse | 0.6B | 0.7824 | 0.9483 | 0.8219 | 0.8143 | 0.6724 | 0.9700 | 0.9623 | 0.6997 | 0.4318 | 0.7209 |
| telepix/PIXIE-Splade-v1.5 | Sparse | 0.1B | 0.7608 | 0.9412 | 0.7910 | 0.7993 | 0.7667 | 0.9687 | 0.9651 | 0.5132 | 0.4938 | 0.6085 |

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

### English Retrieval (BEIR, RTEB)

KURE-Sparse-nano is also evaluated on two English benchmarks with nDCG@10: the 13 BEIR tasks (BEIR-13), and the **eight public English** tasks of [RTEB](https://huggingface.co/blog/rteb) outside the code domain. SparseUp runs at its own length limits (128 query and 512 document tokens), and the other models at up to 8,192 tokens. The RTEB average differs from the RTEB leaderboard score, which also covers private and code tasks.

<p align="center">
  <img src="assets/beir_rteb_sparse.png" width="100%" alt="Average nDCG@10 on BEIR-13 and on the public RTEB English tasks of the KURE-Sparse models and sparse baselines">
</p>

#### BEIR-13

| Model | Params | BEIR-13 | FLOPs |
| :--- | :--- | ---: | ---: |
| **KURE Models** | | | |
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
| **KURE Models** | | | | | | | | | | | | | | |
| **KURE-Sparse-base** | **0.5864** | 0.5896 | 0.3959 | 0.4837 | 0.9325 | 0.4720 | 0.8084 | 0.3678 | 0.6758 | 0.8252 | 0.1741 | 0.7183 | 0.8260 | 0.3535 |
| **KURE-Sparse-nano** | 0.5317 | 0.5075 | 0.2865 | 0.4214 | 0.9079 | 0.4080 | 0.7476 | 0.3340 | 0.5647 | 0.7825 | 0.1581 | 0.7120 | 0.7637 | 0.3183 |
| **Sparse Models** | | | | | | | | | | | | | | |
| Linkup-Platform/linkup-sparseup-embed-v1 | 0.5645 | 0.5648 | 0.3747 | 0.4150 | 0.8969 | 0.4687 | 0.7761 | 0.3523 | 0.5717 | 0.8656 | 0.1852 | 0.7376 | 0.7823 | 0.3478 |
| omai-research/milco-650m | 0.5545 | 0.6157 | 0.3079 | 0.4501 | 0.8353 | 0.4262 | 0.7780 | 0.3629 | 0.6495 | 0.8818 | 0.1704 | 0.7020 | 0.7476 | 0.2813 |
| telepix/PIXIE-Splade-v1.5 | 0.4149 | 0.2185 | 0.1302 | 0.3519 | 0.6475 | 0.2753 | 0.5756 | 0.3325 | 0.3858 | 0.6878 | 0.1468 | 0.6694 | 0.7068 | 0.2650 |

</details>

#### RTEB

| Model | Params | Avg | FLOPs |
| :--- | :--- | ---: | ---: |
| **KURE Models** | | | |
| **[nlpai-lab/KURE-Sparse-nano](https://huggingface.co/nlpai-lab/KURE-Sparse-nano)** | 0.1B | **0.4750** | 109.9 |
| [nlpai-lab/KURE-Sparse-base](https://huggingface.co/nlpai-lab/KURE-Sparse-base) | 0.6B | 0.5093 | 277.6 |
| **Sparse Models** | | | |
| utahnlp/laconic-1b | 1.2B | 0.5092 | 53.5 |
| Linkup-Platform/linkup-sparseup-embed-v1 | 0.2B | 0.4941 | 25.1 |
| opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte | 0.1B | 0.4721 | 12.7 |
| naver/splade-v3 | 0.1B | 0.4596 | 35.0 |
| omai-research/milco-650m | 0.6B | 0.4301 | 163.7 |
| telepix/PIXIE-Splade-v1.5 | 0.1B | 0.3630 | 391.3 |

<details>
<summary>Per-task nDCG@10</summary>

| Model | Params | Avg | CUREv1 | ChatDoctor | FinQA | AILACasedocs | LegalSummarization | HC3Finance | FinanceBench | AILAStatutes | FLOPs |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **KURE Models** | | | | | | | | | | | |
| **[nlpai-lab/KURE-Sparse-nano](https://huggingface.co/nlpai-lab/KURE-Sparse-nano)** | 0.1B | **0.4750** | 0.3591 | 0.4730 | 0.7042 | 0.2860 | 0.6399 | 0.4438 | 0.7005 | 0.1939 | 109.9 |
| [nlpai-lab/KURE-Sparse-base](https://huggingface.co/nlpai-lab/KURE-Sparse-base) | 0.6B | 0.5093 | 0.5996 | 0.3914 | 0.7838 | 0.2298 | 0.5494 | 0.5951 | 0.7525 | 0.1727 | 277.6 |
| **Sparse Models** | | | | | | | | | | | |
| utahnlp/laconic-1b | 1.2B | 0.5092 | 0.5218 | 0.5418 | 0.4922 | 0.2648 | 0.6346 | 0.5715 | 0.7053 | 0.3418 | 53.5 |
| Linkup-Platform/linkup-sparseup-embed-v1 | 0.2B | 0.4941 | 0.4010 | 0.5424 | 0.5805 | 0.2406 | 0.6430 | 0.5900 | 0.6852 | 0.2700 | 25.1 |
| opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte | 0.1B | 0.4721 | 0.3004 | 0.5015 | 0.7344 | 0.2596 | 0.6554 | 0.4265 | 0.6855 | 0.2139 | 12.7 |
| naver/splade-v3 | 0.1B | 0.4596 | 0.3306 | 0.5036 | 0.6374 | 0.3153 | 0.5663 | 0.4118 | 0.6878 | 0.2241 | 35.0 |
| omai-research/milco-650m | 0.6B | 0.4301 | 0.5674 | 0.2344 | 0.7399 | 0.2197 | 0.3078 | 0.5451 | 0.6513 | 0.1747 | 163.7 |
| telepix/PIXIE-Splade-v1.5 | 0.1B | 0.3630 | 0.3414 | 0.2178 | 0.5751 | 0.2082 | 0.5216 | 0.3042 | 0.5180 | 0.2181 | 391.3 |

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
