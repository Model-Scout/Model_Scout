---
tags:
- ColBERT
- PyLate
- late-interaction
- multi-vector
- sentence-transformers
- sentence-similarity
- feature-extraction
- pretrained
language:
- ko
- en
base_model: skt/A.X-Encoder-base
pipeline_tag: sentence-similarity
library_name: PyLate
license: apache-2.0
---

<a href="https://github.com/nlpai-lab/KURE">
  <img src="kure_logo.png" width="50%"/>
</a>

# 🔎 KURE-v2-unsupervised

**KURE-v2-unsupervised** is the *stage-1* checkpoint for KURE-v2: a Korean-English
late-interaction (ColBERT) encoder trained with **unsupervised contrastive learning only**, on
20.7M query–document pairs.

## What this is for

If you would like to train your own late-interaction retriever for Korean-English and would rather not
start from a masked-LM backbone, feel free to use this model. We highly recommend **not** deploying it as-is. 

## Evaluation

nDCG@10 on the nine **MTEB(kor, v2)** retrieval tasks. We report average nDCG@10.

| Model | Params | Avg | AutoRAG | PubHealthQA | Ko-StrategyQA | LawIRKo | SQuADKorV1 | Belebele (ko-ko) | MrTidy | MLDR | MIRACL |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Our Models** | | | | | | | | | | | |
| **[nlpai-lab/KURE-v2](https://huggingface.co/nlpai-lab/KURE-v2)** | 154M | **0.8160** | 0.9718 | 0.8229 | 0.8070 | 0.7550 | 0.9846 | 0.9660 | 0.5974 | 0.7159 | 0.7237 |
| **[nlpai-lab/KURE-v2-unsupervised](https://huggingface.co/nlpai-lab/KURE-v2-unsupervised)** | 154M | 0.7283 | 0.8822 | 0.8240 | 0.7818 | 0.7680 | 0.9427 | 0.9525 | 0.3496 | 0.6130 | 0.4411 |
| **Late-Interaction (Multi-Vector) Models** | | | | | | | | | | | |
| yjoonjang/colbert-ko-en-v2 | 149M | 0.8063 | 0.9686 | 0.8222 | 0.7940 | 0.7181 | 0.9846 | 0.9687 | 0.5783 | 0.6992 | 0.7230 |
| lightonai/mLateOn | 307M | 0.7906 | 0.9392 | 0.8061 | 0.7905 | 0.6431 | 0.9803 | 0.9608 | 0.5817 | 0.7005 | 0.7135 |
| perplexity-ai/pplx-embed-v1-late-0.6b | 596M | 0.7381 | 0.8557 | 0.8089 | 0.7973 | 0.7285 | 0.9696 | 0.9548 | 0.5400 | 0.2816 | 0.7064 |
| dragonkue/colbert-ko-0.1b | 149M | 0.6776 | 0.9700 | 0.7482 | 0.7364 | 0.4475 | 0.9794 | 0.9644 | 0.3966 | 0.2872 | 0.5685 |
| yjoonjang/colbert-ko-v1 | 149M | 0.6282 | 0.9557 | 0.6783 | 0.6560 | 0.4823 | 0.9594 | 0.9154 | 0.3279 | 0.2214 | 0.4575 |
| **Dense (Single-Vector) Models** | | | | | | | | | | | |
| sionic-ai/comsat-embed-ko-8b-preview | 7.6B | 0.7927 | 0.8518 | 0.8871 | 0.8394 | 0.8164 | 0.9168 | 0.9853 | 0.6253 | 0.5157 | 0.6964 |
| Qwen/Qwen3-Embedding-8B | 7.6B | 0.7826 | 0.8276 | 0.8721 | 0.8363 | 0.8171 | 0.9063 | 0.9824 | 0.6187 | 0.5046 | 0.6783 |
| Qwen/Qwen3-Embedding-4B | 4.0B | 0.7737 | 0.8431 | 0.8693 | 0.8270 | 0.7769 | 0.9044 | 0.9522 | 0.6076 | 0.5022 | 0.6803 |
| microsoft/harrier-oss-v1-27b | 27.0B | 0.7667 | 0.8176 | 0.8971 | 0.8361 | 0.8737 | 0.9204 | 0.9546 | 0.5306 | 0.4046 | 0.6653 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | 568M | 0.7653 | 0.9093 | 0.8337 | 0.8050 | 0.7735 | 0.9447 | 0.9518 | 0.5712 | 0.4304 | 0.6685 |
| codefuse-ai/F2LLM-v2-8B | 7.6B | 0.7638 | 0.7678 | 0.9380 | 0.8371 | 0.8405 | 0.8874 | 0.9513 | 0.6162 | 0.4047 | 0.6313 |
| telepix/PIXIE-Rune-v1.5 | 568M | 0.7618 | 0.8927 | 0.8426 | 0.8064 | 0.7705 | 0.9457 | 0.9617 | 0.5492 | 0.4482 | 0.6393 |
| [nlpai-lab/KURE-v1](https://huggingface.co/nlpai-lab/KURE-v1) | 568M | 0.7616 | 0.8708 | 0.8193 | 0.7999 | 0.7426 | 0.9357 | 0.9502 | 0.5909 | 0.4637 | 0.6816 |
| dragonkue/BGE-m3-ko | 568M | 0.7547 | 0.8738 | 0.8155 | 0.7959 | 0.7322 | 0.9414 | 0.9503 | 0.6099 | 0.3899 | 0.6833 |
| BAAI/bge-m3 | 568M | 0.7509 | 0.8301 | 0.8041 | 0.7941 | 0.7174 | 0.9038 | 0.9316 | 0.6471 | 0.4287 | 0.7015 |
| [nlpai-lab/KoE5](https://huggingface.co/nlpai-lab/KoE5) | 560M | 0.7337 | 0.8434 | 0.8351 | 0.8001 | 0.7756 | 0.8980 | 0.9425 | 0.5841 | 0.3015 | 0.6235 |

Late-interaction rows were measured with `mteb` 2.18.16 and PLAID retrieval, and single-vector rows are
taken from the official [MTEB results repository](https://github.com/embeddings-benchmark/results),
except for Belebele, where only the Korean-query / Korean-corpus subset is used. The original
version also includes cross-lingual subsets (Korean query – English corpus, English query – Korean
corpus).

## Citation

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

```bibtex
@inproceedings{santhanam-etal-2022-colbertv2,
  title     = {ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction},
  author    = {Santhanam, Keshav and Khattab, Omar and Saad-Falcon, Jon and Potts, Christopher and Zaharia, Matei},
  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  year      = {2022},
  pages     = {3715--3734},
}
```

```bibtex
@misc{PyLate,
  title  = {PyLate: Flexible Training and Retrieval for Late Interaction Models},
  author = {Chaffin, Antoine and Sourty, Raphaël},
  year   = {2024},
  url    = {https://github.com/lightonai/pylate},
}
```