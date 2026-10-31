---
language:
- en
- ar
- de
- fr
- es
- aa
- ab
- ae
- af
- ak
- am
- an
- as
- av
- ay
- az
- ba
- be
- bg
- bh
- bi
- bm
- bn
- bo
- br
- bs
- ca
- ce
- ch
- co
- cr
- cs
- cu
- cv
- cy
- da
- dv
- dz
- ee
- el
- eo
- et
- eu
- fa
- ff
- fi
- fj
- fo
- fy
- ga
- gd
- gl
- gn
- gu
- gv
- ha
- he
- hi
- ho
- hr
- ht
- hu
- hy
- hz
- ia
- id
- ie
- ig
- ii
- ik
- io
- is
- it
- iu
- ja
- jv
- ka
- kg
- ki
- kj
- kk
- kl
- km
- kn
- ko
- kr
- ks
- ku
- lt
- kw
- kv
- ky
- la
- lb
- lg
- li
- ln
- lo
- lu
- lv
- mg
- mh
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- na
license: apache-2.0
size_categories:
- 10M<n<100M
task_categories:
- question-answering
pretty_name: Reranking, Retreiver
configs:
- config_name: NQ
  data_files:
  - split: train
    path: bm25/nq/train.json
  - split: dev
    path: bm25/nq/dev.json
  - split: test
    path: bm25/nq/test.json
- config_name: TriviaQA
  data_files:
  - split: train
    path: bm25/triviaqa/train.json
  - split: dev
    path: bm25/triviaqa/dev.json
  - split: test
    path: bm25/triviaqa/test.json
- config_name: 2WikimultihopQA
  data_files:
  - split: train
    path: bm25/2wikimultihopqa/train.json
  - split: dev
    path: bm25/2wikimultihopqa/dev.json
- config_name: ArchivialQA
  data_files:
  - split: test
    path: bm25/ArchivialQA/test.json
  - split: dev
    path: bm25/ArchivialQA/val.json
- config_name: ChroniclingAmericaQA
  data_files:
  - split: test
    path: bm25/ChroniclingAmericaQA/test.json
  - split: dev
    path: bm25/ChroniclingAmericaQA/val.json
- config_name: EntityQuestions
  data_files:
  - split: test
    path: bm25/triviaqa/test.json
- config_name: AmbigQA
  data_files:
  - split: train
    path: bm25/ambig_qa/train.json
  - split: dev
    path: bm25/ambig_qa/dev.json
- config_name: ARC
  data_files:
  - split: train
    path: bm25/arc/train.json
  - split: dev
    path: bm25/arc/dev.json
  - split: test
    path: bm25/arc/test.json
- config_name: ASQA
  data_files:
  - split: train
    path: bm25/asqa/train.json
  - split: dev
    path: bm25/asqa/dev.json
- config_name: AY2
  data_files:
  - split: train
    path: bm25/ay2/train.json
  - split: dev
    path: bm25/ay2/dev.json
- config_name: ASQA
  data_files:
  - split: train
    path: bm25/asqa/train.json
  - split: dev
    path: bm25/asqa/dev.json
- config_name: Bamboogle
  data_files:
  - split: test
    path: bm25/bamboogle/test.json
- config_name: Eli5
  data_files:
  - split: train
    path: bm25/eli5/train.json
  - split: dev
    path: bm25/eli5/dev.json
- config_name: Fermi
  data_files:
  - split: train
    path: bm25/fermi/train.json
  - split: dev
    path: bm25/fermi/dev.json
  - split: test
    path: bm25/fermi/test.json
- config_name: Fever
  data_files:
  - split: train
    path: bm25/fever/train.json
  - split: dev
    path: bm25/fever/dev.json
  - split: test
    path: bm25/fever/test.json
- config_name: Hellaswag
  data_files:
  - split: train
    path: bm25/fever/train.json
  - split: dev
    path: bm25/fever/dev.json
- config_name: HotpotQA
  data_files:
  - split: train
    path: bm25/hotpotqa/train.json
  - split: dev
    path: bm25/hotpotqa/dev.json
- config_name: MMLU
  data_files:
  - split: train
    path: bm25/mmlu/train.json
  - split: dev
    path: bm25/mmlu/dev.json
  - split: test
    path: bm25/mmlu/test.json
- config_name: MMLU
  data_files:
  - split: 5_shot
    path: bm25/mmlu/5_shot.json
  - split: train
    path: bm25/mmlu/train.json
  - split: dev
    path: bm25/mmlu/dev.json
  - split: test
    path: bm25/mmlu/test.json
- config_name: Musique
  data_files:
  - split: train
    path: bm25/musique/train.json
  - split: dev
    path: bm25/musique/dev.json
- config_name: NarrativeQA
  data_files:
  - split: train
    path: bm25/narrativeqa/train.json
  - split: dev
    path: bm25/narrativeqa/dev.json
  - split: test
    path: bm25/narrativeqa/test.json
- config_name: OpenbookQA
  data_files:
  - split: train
    path: bm25/openbookqa/train.json
  - split: dev
    path: bm25/openbookqa/dev.json
  - split: test
    path: bm25/openbookqa/test.json
- config_name: PIQA
  data_files:
  - split: train
    path: bm25/piqa/train.json
  - split: dev
    path: bm25/piqa/dev.json
- config_name: PoPQA
  data_files:
  - split: test
    path: bm25/popqa/test.json
- config_name: Quartz
  data_files:
  - split: train
    path: bm25/quartz/train.json
  - split: dev
    path: bm25/quartz/dev.json
  - split: test
    path: bm25/quartz/test.json
- config_name: SIQA
  data_files:
  - split: train
    path: bm25/siqa/train.json
  - split: dev
    path: bm25/siqa/dev.json
- config_name: SQuAD
  data_files:
  - split: train
    path: bm25/squad/train.json
  - split: dev
    path: bm25/squad/dev.json
  - split: test
    path: bm25/squad/test.json
- config_name: StrategyQA
  data_files:
  - split: train
    path: bm25/squad/train.json
- config_name: TREX
  data_files:
  - split: dev
    path: bm25/trex/dev.json
- config_name: TruthfulQA
  data_files:
  - split: dev
    path: bm25/truthful_qa/dev.json
- config_name: WebQA
  data_files:
  - split: train
    path: bm25/web_questions/train.json
  - split: test
    path: bm25/web_questions/test.json
- config_name: WikiQA
  data_files:
  - split: train
    path: bm25/wiki_qa/train.json
  - split: dev
    path: bm25/wiki_qa/dev.json
  - split: test
    path: bm25/wiki_qa/test.json
- config_name: WikiASP
  data_files:
  - split: train
    path: bm25/wikiasp/train.json
  - split: dev
    path: bm25/wikiasp/dev.json
  - split: test
    path: bm25/wikiasp/test.json
- config_name: WikiPassageQA
  data_files:
  - split: train
    path: bm25/wikipassageqa/train.json
  - split: dev
    path: bm25/wikipassageqa/dev.json
  - split: test
    path: bm25/wikipassageqa/test.json
- config_name: Wned
  data_files:
  - split: dev
    path: bm25/wned/dev.json
- config_name: WoW
  data_files:
  - split: train
    path: bm25/wow/train.json
  - split: dev
    path: bm25/wow/dev.json
- config_name: ZSRE
  data_files:
  - split: train
    path: bm25/zsre/train.json
  - split: dev
    path: bm25/zsre/dev.json
---

# <div align="center">🔥 Rankify: A Comprehensive Python Toolkit for Retrieval, Re-Ranking, and Retrieval-Augmented Generation 🔥<div>  
### ReRanking Datasets : A comprehensive collection of retrieval and reranking datasets with full passage contexts, including titles, text, and metadata for in-depth research.




<div align="center">
    <a href="https://github.com/DataScienceUIBK/Rankify/tree/main"  style="display: inline-block; margin: 2px;" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github">
    </a>
    <a href="https://arxiv.org/abs/2502.02464" target="_blank" style="display: inline-block; margin: 2px;">
        <img src="https://img.shields.io/badge/arXiv-b5212f.svg?logo=arxiv">
    </a>
    <a href="https://huggingface.co/datasets/abdoelsayed/reranking-datasets" target="_blank" style="display: inline-block; margin: 2px;">
        <img src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace%20Datasets-27b3b4.svg">
    </a>
    <a href="https://huggingface.co/datasets/abdoelsayed/reranking-datasets-light" target="_blank" style="display: inline-block; margin: 2px;">
        <img src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace%20Datasets%20light-orange.svg">
    </a>
    <a style="display: inline-block; margin: 2px;">
        <img alt="Static Badge" src="https://img.shields.io/badge/Python-3.10_3.11-blue">
    </a>
    <a href="https://opensource.org/license/apache-2-0" style="display: inline-block; margin: 5px;">
        <img src="https://img.shields.io/static/v1?label=License&message=Apache-2.0&color=red">
    </a>
    <a href="https://github.com/DataScienceUIBK/rankify/releases" style="display: inline-block; margin: 5px;">
        <img alt="GitHub release" src="https://img.shields.io/github/release/DataScienceUIBK/rankify.svg?label=Version&color=orange">
    </a>
</div>

![Dataset Downloads](https://img.shields.io/badge/Datasets-Retrieval_Ready-brightgreen)

_A curated collection of ready-to-use datasets for retrieval and reranking research. Created by [Abdelrahman Abdallah](https://abdoelsayed2016.github.io/)._

---

## About This Repository

Welcome to **ReRanking Datasets**! This repository simplifies retrieval research by providing preprocessed datasets for commonly used retrievers. Instead of running multiple retrievers on your own, download the precomputed results directly and focus on your research!

### What's Inside?

This dataset collection includes popular question-answering datasets:

The following table provides an overview of the availability of different retrieval methods (**BM25, DPR, ColBERT, ANCE, BGE, Contriever**) for each dataset.  

✅ **Completed**
⏳  **Part Completed, Pending other Parts**
🕒 **Pending**  

<table style="width: 100%;">
  <tr>
    <th align="center">Dataset</th> 
    <th align="center">BM25</th> 
    <th align="center">DPR</th> 
    <th align="center">ColBERT</th>
    <th align="center">ANCE</th>
    <th align="center">BGE</th>
    <th align="center">Contriever</th>
  </tr>
  <tr>
    <td align="left">2WikimultihopQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">ArchivialQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">ChroniclingAmericaQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">EntityQuestions</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">AmbigQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">ARC</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">ASQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">MS MARCO</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">AY2</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">Bamboogle</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">BoolQ</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">CommonSenseQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">CuratedTREC</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">ELI5</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">FERMI</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">FEVER</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">HellaSwag</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">HotpotQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">MMLU</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
  <tr>
    <td align="left">Musique</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">NarrativeQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">NQ</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">OpenbookQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">PIQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">PopQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">Quartz</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">SIQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    <tr>
    <td align="left">StrategyQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    </tr>
    <tr>
    <td align="left">TREX</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    </tr>
    <tr>
    <td align="left">TriviaQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
    </tr>
    <tr>
    <td align="left">TruthfulQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
      </tr>
    <tr>
    <td align="left">TruthfulQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
      </tr>
    <tr>
    <td align="left">WebQ</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
      </tr>
    <tr>
    <td align="left">WikiQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
      </tr>
    <tr>
    <td align="left">WikiAsp</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
        </tr>
    <tr>
    <td align="left">WikiPassageQA</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">⏳</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
        </tr>
    <tr>
    <td align="left">WNED</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
        </tr>
    <tr>
    <td align="left">WoW</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
        </tr>
    <tr>
    <td align="left">Zsre</td>
    <td align="center">✅</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
    <td align="center">🕒</td>
  </tr>
</table>



Each dataset has **N different files**, one for each retriever. These files are organized and ready for direct use, saving you time and computation. All passages retrieved from psgs_w100 you can download them from [psgs_w100.tsv](https://huggingface.co/datasets/abdoelsayed/reranking-datasets/resolve/main/psgs_w100/psgs_w100.tsv?download=true) 

---

### Need Full Context?
If you require the complete dataset, including passage titles and full text, you can find it in the full collection:

👉 [ReRanking Contexts](https://huggingface.co/abdoelsayed/reranking-contexts)

---

### Format
The datasets are provided in JSON format, structured as follows:

```
[
    {
        "question": "...",
        "answers": ["...", "...", ...],
        "ctxs": [
            {
                "id": "...",         // Passage ID from database TSV file
                "score": "...",      // Retriever score
                "has_answer": true|false  // Whether the passage contains the answer
            }
        ]
    }
]
```
---
## Ongoing Work

Our goal is to make this repository the go-to resource for retrieval and reranking datasets. Here's what we are currently working on:

- Expanding the dataset collection to include more benchmarks, such as **MS MARCO**, **TREC**, and others.
- Adding retrieval outputs from more retrievers, including cutting-edge methods like **ColBERT**, **ANCE**, and more.
- Continuously improving dataset organization and documentation to ensure researchers' ease of use.

If you have suggestions for additional datasets or retrievers you'd like to see included, feel free to reach out or contribute!

---

## Why Use This Repository?

- 🚀 **Time-Saving:** Avoid the hassle of running retrievers yourself.
- 📂 **Precomputed Results:** Access retrieval outputs for multiple retrievers in one place.
- 🎯 **Research-Ready:** Use datasets directly for reranking tasks or as baselines in your studies.
- 🛠️ **Versatility:** Compatible with diverse retrieval and reranking pipelines.

---

## How to Use

Simply visit the dataset page on [HuggingFace](https://huggingface.co/datasets/abdoelsayed/reranking-datasets) and download the files for your desired dataset and retriever. Each file is structured to integrate seamlessly into your retrieval or reranking workflows.

---
## Example
```
from datasets import load_dataset

# Use streaming mode
dataset = load_dataset("abdoelsayed/reranking-datasets-light", data_files={"test": "bm25/nq-test.json"}, streaming=True)

# Iterate through the dataset
for entry in dataset["test"].take(10):  # Process 10 entries as an example
    print(entry)
```

## Contribution & Feedback

We are actively expanding this repository and welcome contributions from the research community. Have a suggestion for a new dataset or retriever? Found an issue? Feel free to [open an issue](https://huggingface.co/datasets/abdoelsayed/reranking-datasets/issues) or reach out via [Twitter](https://twitter.com/abdoelsayed).

---

## 🌟 Citation

Please kindly cite our paper if helps your research:

```BibTex
@article{abdallah2025rankify,
  title={Rankify: A Comprehensive Python Toolkit for Retrieval, Re-Ranking, and Retrieval-Augmented Generation},
  author={Abdallah, Abdelrahman and Mozafari, Jamshid and Piryani, Bhawna and Ali, Mohammed and Jatowt, Adam},
  journal={arXiv preprint arXiv:2502.02464},
  year={2025}
}
```

## Star History


[![Star History Chart](https://api.star-history.com/svg?repos=DataScienceUIBK/Rankify&type=Date)](https://star-history.com/#DataScienceUIBK/Rankify&Date)

🎉 **Happy Researching!**

**Paper:** [Rankify: A Comprehensive Python Toolkit for Retrieval, Re-Ranking, and Retrieval-Augmented Generation](https://hf.co/papers/2502.02464)