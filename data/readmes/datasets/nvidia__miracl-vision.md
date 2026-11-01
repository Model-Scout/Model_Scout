---
language:
  - ar
  - bn
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
  - zh
  - de
  - yo
multilinguality:
  - multilingual
license:
  - cc-by-sa-4.0
task_ids:
  - document-retrieval
tags:
  - text
  - image
configs:
- config_name: queries-ar
  data_files:
  - split: default
    path: "ar/queries.parquet" 
- config_name: corpus-ar
  data_files:
  - split: default
    path: "ar/corpus.parquet" 
- config_name: qrels-ar
  data_files:
  - split: default
    path: "ar/qrels.parquet" 
- config_name: images-ar
  data_files:
  - split: default
    path: "ar/images.parquet" 
- config_name: queries-bn
  data_files:
  - split: default
    path: "bn/queries.parquet" 
- config_name: corpus-bn
  data_files:
  - split: default
    path: "bn/corpus.parquet" 
- config_name: qrels-bn
  data_files:
  - split: default
    path: "bn/qrels.parquet" 
- config_name: images-bn
  data_files:
  - split: default
    path: "bn/images.parquet" 
- config_name: queries-de
  data_files:
  - split: default
    path: "de/queries.parquet" 
- config_name: corpus-de
  data_files:
  - split: default
    path: "de/corpus.parquet" 
- config_name: qrels-de
  data_files:
  - split: default
    path: "de/qrels.parquet" 
- config_name: images-de
  data_files:
  - split: default
    path: "de/images.parquet" 
- config_name: queries-en
  data_files:
  - split: default
    path: "en/queries.parquet" 
- config_name: corpus-en
  data_files:
  - split: default
    path: "en/corpus.parquet" 
- config_name: qrels-en
  data_files:
  - split: default
    path: "en/qrels.parquet" 
- config_name: images-en
  data_files:
  - split: default
    path: "en/images.parquet" 
- config_name: queries-es
  data_files:
  - split: default
    path: "es/queries.parquet" 
- config_name: corpus-es
  data_files:
  - split: default
    path: "es/corpus.parquet" 
- config_name: qrels-es
  data_files:
  - split: default
    path: "es/qrels.parquet" 
- config_name: images-es
  data_files:
  - split: default
    path: "es/images.parquet" 
- config_name: queries-fa
  data_files:
  - split: default
    path: "fa/queries.parquet" 
- config_name: corpus-fa
  data_files:
  - split: default
    path: "fa/corpus.parquet" 
- config_name: qrels-fa
  data_files:
  - split: default
    path: "fa/qrels.parquet" 
- config_name: images-fa
  data_files:
  - split: default
    path: "fa/images.parquet" 
- config_name: queries-fi
  data_files:
  - split: default
    path: "fi/queries.parquet" 
- config_name: corpus-fi
  data_files:
  - split: default
    path: "fi/corpus.parquet" 
- config_name: qrels-fi
  data_files:
  - split: default
    path: "fi/qrels.parquet" 
- config_name: images-fi
  data_files:
  - split: default
    path: "fi/images.parquet" 
- config_name: queries-fr
  data_files:
  - split: default
    path: "fr/queries.parquet" 
- config_name: corpus-fr
  data_files:
  - split: default
    path: "fr/corpus.parquet" 
- config_name: qrels-fr
  data_files:
  - split: default
    path: "fr/qrels.parquet" 
- config_name: images-fr
  data_files:
  - split: default
    path: "fr/images.parquet" 
- config_name: queries-hi
  data_files:
  - split: default
    path: "hi/queries.parquet" 
- config_name: corpus-hi
  data_files:
  - split: default
    path: "hi/corpus.parquet" 
- config_name: qrels-hi
  data_files:
  - split: default
    path: "hi/qrels.parquet" 
- config_name: images-hi
  data_files:
  - split: default
    path: "hi/images.parquet" 
- config_name: queries-id
  data_files:
  - split: default
    path: "id/queries.parquet" 
- config_name: corpus-id
  data_files:
  - split: default
    path: "id/corpus.parquet" 
- config_name: qrels-id
  data_files:
  - split: default
    path: "id/qrels.parquet" 
- config_name: images-id
  data_files:
  - split: default
    path: "id/images.parquet" 
- config_name: queries-ja
  data_files:
  - split: default
    path: "ja/queries.parquet" 
- config_name: corpus-ja
  data_files:
  - split: default
    path: "ja/corpus.parquet" 
- config_name: qrels-ja
  data_files:
  - split: default
    path: "ja/qrels.parquet" 
- config_name: images-ja
  data_files:
  - split: default
    path: "ja/images.parquet" 
- config_name: queries-ko
  data_files:
  - split: default
    path: "ko/queries.parquet" 
- config_name: corpus-ko
  data_files:
  - split: default
    path: "ko/corpus.parquet" 
- config_name: qrels-ko
  data_files:
  - split: default
    path: "ko/qrels.parquet" 
- config_name: images-ko
  data_files:
  - split: default
    path: "ko/images.parquet" 
- config_name: queries-ru
  data_files:
  - split: default
    path: "ru/queries.parquet" 
- config_name: corpus-ru
  data_files:
  - split: default
    path: "ru/corpus.parquet" 
- config_name: qrels-ru
  data_files:
  - split: default
    path: "ru/qrels.parquet" 
- config_name: images-ru
  data_files:
  - split: default
    path: "ru/images.parquet" 
- config_name: queries-sw
  data_files:
  - split: default
    path: "sw/queries.parquet" 
- config_name: corpus-sw
  data_files:
  - split: default
    path: "sw/corpus.parquet" 
- config_name: qrels-sw
  data_files:
  - split: default
    path: "sw/qrels.parquet" 
- config_name: images-sw
  data_files:
  - split: default
    path: "sw/images.parquet" 
- config_name: queries-te
  data_files:
  - split: default
    path: "te/queries.parquet" 
- config_name: corpus-te
  data_files:
  - split: default
    path: "te/corpus.parquet" 
- config_name: qrels-te
  data_files:
  - split: default
    path: "te/qrels.parquet" 
- config_name: images-te
  data_files:
  - split: default
    path: "te/images.parquet" 
- config_name: queries-th
  data_files:
  - split: default
    path: "th/queries.parquet" 
- config_name: corpus-th
  data_files:
  - split: default
    path: "th/corpus.parquet" 
- config_name: qrels-th
  data_files:
  - split: default
    path: "th/qrels.parquet" 
- config_name: images-th
  data_files:
  - split: default
    path: "th/images.parquet" 
- config_name: queries-yo
  data_files:
  - split: default
    path: "yo/queries.parquet" 
- config_name: corpus-yo
  data_files:
  - split: default
    path: "yo/corpus.parquet" 
- config_name: qrels-yo
  data_files:
  - split: default
    path: "yo/qrels.parquet" 
- config_name: images-yo
  data_files:
  - split: default
    path: "yo/images.parquet" 
- config_name: queries-zh
  data_files:
  - split: default
    path: "zh/queries.parquet" 
- config_name: corpus-zh
  data_files:
  - split: default
    path: "zh/corpus.parquet" 
- config_name: qrels-zh
  data_files:
  - split: default
    path: "zh/qrels.parquet" 
- config_name: images-zh
  data_files:
  - split: default
    path: "zh/images.parquet" 
---

# MIRACL-VISION

MIRACL-VISION is a multilingual visual retrieval dataset for 18 different languages. It is an extension of MIRACL, a popular text-only multilingual retrieval dataset. The dataset contains user questions, images of Wikipedia articles and annotations, which article can answer a user question. There are 7898 questions and 338734 images. More details can be found in the paper [MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark](https://arxiv.org/abs/2505.11651).

This dataset is ready for commercial usage for evaluation of the multilingual, multimodal retriever pipelines.

### Correspondence to
Benedikt Schifferer (bschifferer@nvidia.com)

### Dataset Creation Date:
31st January 2025

### License/Terms of Use: 
This dataset is licensed under Creative Commons Attribution-ShareAlike 4.0 International. Additional Information: Apache License 2.0.

### Intended Usage:
Users can evaluate multilingual, multimodal retriever pipelines. 

### Dataset Characterization
Dataset Collection Method: Automated
Labelling Method: Human

### Dataset Format
The images are stored Pillow (PIL) Images in HuggingFace Dataset format
The questions, corpus, questions-corpus pairs are stored in parquet/BEIR format

### Reference(s):
```
@misc{osmulsk2025miraclvisionlargemultilingualvisual,
      title={MIRACL-VISION: A Large, multilingual, visual document retrieval benchmark}, 
      author={Radek Osmulsk and Gabriel de Souza P. Moreira and Ronay Ak and Mengyao Xu and Benedikt Schifferer and Even Oldridge},
      year={2025},
      eprint={2505.11651},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2505.11651}, 
}
```

### Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Example

The requirements are
```
pip install qwen_vl_utils beir==2.0.0
```

The dataset contains an [eval_example](https://huggingface.co/datasets/nvidia/miracl-vision/tree/main/eval_example) using [MrLight/dse-qwen2-2b-mrl-v1](https://huggingface.co/MrLight/dse-qwen2-2b-mrl-v1)​​

```bash
python embedding_eval.py --dataset nvidia/miracl-vision --language en
```

### Loading the Dataset

```python
from datasets import load_dataset

def hf_beir_queries(queries):
    queries_beir = {}
    for query in queries:
        queries_beir[query['_id']] = query['text']
    return(queries_beir)

def hf_beir_corpus(corpus):
    corpus_beir = {}
    for doc in corpus:
        corpus_beir[doc['_id']] = doc
    return(corpus_beir)

def hf_beir_qrels(qrels):
    qrels_beir = {}
    for el in qrels:
        if str(el['query-id']) in qrels_beir:
            qrels_beir[str(el['query-id'])][str(el['corpus-id'])] = el['score']
        else:
            qrels_beir[str(el['query-id'])] = {str(el['corpus-id']): el['score']}
    return(qrels_beir)

def load_data(
    path,
    lang
):
    queries = load_dataset(path, 'queries-' + str(lang), split='default')
    queries = hf_beir_queries(queries)
    corpus = load_dataset(path, 'corpus-' + str(lang), split='default')
    corpus = hf_beir_corpus(corpus)
    qrels = load_dataset(path, 'qrels-' + str(lang), split='default')
    qrels = hf_beir_qrels(qrels)
    images = load_dataset(path, 'images-' + str(lang), split='default')
    return(queries, corpus, qrels, images)

queries, corpus, qrels, images = load_data('nvidia/miracl-vision', 'en')
```

### Dataset Statistics

Number of Images: 338734

Number of questions: 7898

Total Data Storage: 95GB

|              |                   | MIRACL (original) |     MIRACL (original)    |   MIRACL-VISION  |    MIRACL-VISION   |
|--------------|-------------------|:-----------------:|:------------------------:|:----------------:|:------------------:|
| **Language** | **Language Code** | **# of queries**  | **# of document chunks** | **# of queries** | **# of documents** |
| Arabic       | ar                | 2896              | 2061414                  | 2127             | 75444              |
| Bengali      | bn                | 411               | 297265                   | 229              | 8495               |
| Chinese      | zh                | 393               | 4934368                  | 189              | 8672               |
| English      | en                | 799               | 32893221                 | 447              | 42971              |
| Farsi        | fa                | 632               | 2207172                  | 342              | 15846              |
| Finnish      | fi                | 1271              | 1883509                  | 791              | 33679              |
| French       | fr                | 343               | 14636953                 | 142              | 6990               |
| German       | de                | 305               | 15866222                 | 129              | 6302               |
| Hindi        | hi                | 350               | 506264                   | 184              | 8004               |
| Indonesian   | id                | 960               | 1446315                  | 603              | 23842              |
| Japanese     | ja                | 860               | 6953614                  | 387              | 17909              |
| Korean       | ko                | 213               | 1486752                  | 130              | 5700               |
| Russian      | ru                | 1252              | 9543918                  | 564              | 25201              |
| Spanish      | es                | 648               | 10373953                 | 369              | 17749              |
| Swahili      | sw                | 482               | 131924                   | 239              | 7166               |
| Telugu       | te                | 828               | 518079                   | 480              | 15429              |
| Thai         | th                | 733               | 542166                   | 451              | 16313              |
| Yoruba       | yo                | 119               | 49043                    | 95               | 3022               |
|              |                   |                   |                          |                  |                    |
| **Avereage** |                   |           **750** |              **5907342** |          **439** |          **18819** |



### Results

|                         |    MIRACL-VISION (Text)   |        MIRACL-VISION (Text)       |    MIRACL-VISION (Text)   | MIRACL-VISION (Text) |  MIRACL-VISION (Image)  |     MIRACL-VISION (Image)    | MIRACL-VISION (Image) | MIRACL-VISION (Image) |
|-------------------------|:-------------------------:|:---------------------------------:|:-------------------------:|:--------------------:|:-----------------------:|:----------------------------:|:---------------------:|:---------------------:|
|                         | **multilingual-e5-large** | **snowflake-arctic-embed-l-v2.0** | **gte-multilingual-base** | **bge-m3**           | **dse-qwen2-2b-mrl-v1** | **gme-Qwen2-VL-2B-Instruct** | **vdr-2b-multi-v1**   | **colqwen2-v1.0**     |
| LLM Parameters (in M)   |                       560 |                               567 |                       305 |                  567 |                    1543 |                         1543 |                  1543 |                  1543 |
| Language                |                           |                                   |                           |                      |                         |                              |                       |                       |
| Arabic                  |                    0.8557 |                            0.8754 |                    0.8503 |               0.8883 |                  0.3893 |                       0.4888 |                0.4379 |                0.4129 |
| Bengali                 |                    0.8421 |                            0.8325 |                    0.8211 |               0.8585 |                  0.2352 |                       0.3755 |                0.2473 |                0.2888 |
| Chinese                 |                    0.6900 |                            0.7179 |                    0.7167 |               0.7458 |                  0.5962 |                       0.6314 |                0.5963 |                0.4926 |
| English                 |                    0.7029 |                            0.7437 |                    0.7345 |               0.7348 |                  0.6605 |                       0.6784 |                0.6784 |                0.6417 |
| Farsi                   |                    0.6793 |                            0.7001 |                    0.6984 |               0.7297 |                  0.2250 |                       0.3085 |                0.2398 |                0.2616 |
| Finnish                 |                    0.8974 |                            0.9014 |                    0.8957 |               0.9071 |                  0.4162 |                       0.6863 |                0.5283 |                0.6604 |
| French                  |                    0.7208 |                            0.8236 |                    0.7771 |               0.8158 |                  0.7160 |                       0.6851 |                0.7194 |                0.6876 |
| German                  |                    0.7622 |                            0.7774 |                    0.7498 |               0.7695 |                  0.6267 |                       0.6345 |                0.6205 |                0.5995 |
| Hindi                   |                    0.7595 |                            0.7255 |                    0.6916 |               0.7581 |                  0.1740 |                       0.3127 |                0.2058 |                0.2209 |
| Indonesian              |                    0.6793 |                            0.6906 |                    0.6757 |               0.7049 |                  0.4866 |                       0.5416 |                0.5254 |                0.5320 |
| Japanese                |                    0.8378 |                            0.8484 |                    0.8442 |               0.8720 |                  0.6232 |                       0.7305 |                0.6553 |                0.6970 |
| Korean                  |                    0.7327 |                            0.7545 |                    0.7397 |               0.7934 |                  0.4446 |                       0.6202 |                0.4952 |                0.4419 |
| Russian                 |                    0.7857 |                            0.8242 |                    0.8023 |               0.8363 |                  0.6505 |                       0.7202 |                0.6995 |                0.6811 |
| Spanish                 |                    0.6596 |                            0.7250 |                    0.7029 |               0.7268 |                  0.5927 |                       0.6277 |                0.6274 |                0.6224 |
| Swahili                 |                    0.8157 |                            0.8089 |                    0.7987 |               0.8337 |                  0.4156 |                       0.5348 |                0.4509 |                0.4931 |
| Telugu                  |                    0.8948 |                            0.9201 |                    0.9076 |               0.9090 |                  0.0274 |                       0.0893 |                0.0318 |                0.0264 |
| Thai                    |                    0.8424 |                            0.8485 |                    0.8509 |               0.8682 |                  0.2692 |                       0.3563 |                0.3177 |                0.2389 |
| Yoruba                  |                    0.5655 |                            0.5332 |                    0.5698 |               0.5842 |                  0.4178 |                       0.4884 |                0.4577 |                0.5120 |
|                         |                           |                                   |                           |                      |                         |                              |                       |                       |
| **Average**             |                **0.7624** |                        **0.7806** |                **0.7682** |           **0.7964** |              **0.4426** |                   **0.5283** |            **0.4741** |            **0.4728** |
| **Average w/o Telugu** |                **0.7546** |                        **0.7724** |                **0.7600** |           **0.7898** |              **0.4670** |                   **0.5542** |            **0.5002** |            **0.4991** |