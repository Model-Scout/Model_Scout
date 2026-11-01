---
license: odc-by
task_categories:
  - text-generation
language:
 - en
 - de
 - ja
 - fr
 - es
 - it
 - ru
 - pt
 - pl
 - nl
 - cs
 - zh
 - ro
 - sv
 - hu
 - sk
 - uk
 - th
 - da
 - id
 - el
 - fi
 - ca
 - tr
 - dag
 - hr
 - fa
 - bg
 - nb
 - kiu
 - ar
 - vi
 - sr
 - ko
 - sl
 - lt
 - hi
 - he
 - bs
 - ms
 - et
 - lv
 - bn
 - frp
 - is
 - glk
 - eu
 - gl
 - sq
 - mk
 - mr
 - ne
 - ka
 - la
 - pcm
 - mt
 - cy
 - vec
 - hy
 - nrm
 - wuu
 - anp
 - bcc
 - ur
 - af
 - az
 - ta
 - kk
 - nn
pretty_name: FinePDFs-Edu
size_categories:
  - n>1T
configs:
 - config_name: eng_Latn
   default: true
   data_files:
   - split: train
     path: data/eng_Latn/train/*
 - config_name: deu_Latn
   data_files:
   - split: train
     path: data/deu_Latn/train/*
 - config_name: jpn_Jpan
   data_files:
   - split: train
     path: data/jpn_Jpan/train/*
 - config_name: fra_Latn
   data_files:
   - split: train
     path: data/fra_Latn/train/*
 - config_name: spa_Latn
   data_files:
   - split: train
     path: data/spa_Latn/train/*
 - config_name: ita_Latn
   data_files:
   - split: train
     path: data/ita_Latn/train/*
 - config_name: rus_Cyrl
   data_files:
   - split: train
     path: data/rus_Cyrl/train/*
 - config_name: por_Latn
   data_files:
   - split: train
     path: data/por_Latn/train/*
 - config_name: pol_Latn
   data_files:
   - split: train
     path: data/pol_Latn/train/*
 - config_name: nld_Latn
   data_files:
   - split: train
     path: data/nld_Latn/train/*
 - config_name: ces_Latn
   data_files:
   - split: train
     path: data/ces_Latn/train/*
 - config_name: cmn_Hani
   data_files:
   - split: train
     path: data/cmn_Hani/train/*
 - config_name: ron_Latn
   data_files:
   - split: train
     path: data/ron_Latn/train/*
 - config_name: swe_Latn
   data_files:
   - split: train
     path: data/swe_Latn/train/*
 - config_name: hun_Latn
   data_files:
   - split: train
     path: data/hun_Latn/train/*
 - config_name: slk_Latn
   data_files:
   - split: train
     path: data/slk_Latn/train/*
 - config_name: ukr_Cyrl
   data_files:
   - split: train
     path: data/ukr_Cyrl/train/*
 - config_name: tha_Thai
   data_files:
   - split: train
     path: data/tha_Thai/train/*
 - config_name: dan_Latn
   data_files:
   - split: train
     path: data/dan_Latn/train/*
 - config_name: ind_Latn
   data_files:
   - split: train
     path: data/ind_Latn/train/*
 - config_name: ell_Grek
   data_files:
   - split: train
     path: data/ell_Grek/train/*
 - config_name: fin_Latn
   data_files:
   - split: train
     path: data/fin_Latn/train/*
 - config_name: cat_Latn
   data_files:
   - split: train
     path: data/cat_Latn/train/*
 - config_name: tur_Latn
   data_files:
   - split: train
     path: data/tur_Latn/train/*
 - config_name: dag_Latn
   data_files:
   - split: train
     path: data/dag_Latn/train/*
 - config_name: hrv_Latn
   data_files:
   - split: train
     path: data/hrv_Latn/train/*
 - config_name: fas_Arab
   data_files:
   - split: train
     path: data/fas_Arab/train/*
 - config_name: bul_Cyrl
   data_files:
   - split: train
     path: data/bul_Cyrl/train/*
 - config_name: nob_Latn
   data_files:
   - split: train
     path: data/nob_Latn/train/*
 - config_name: kiu_Latn
   data_files:
   - split: train
     path: data/kiu_Latn/train/*
 - config_name: arb_Arab
   data_files:
   - split: train
     path: data/arb_Arab/train/*
 - config_name: vie_Latn
   data_files:
   - split: train
     path: data/vie_Latn/train/*
 - config_name: srp_Cyrl
   data_files:
   - split: train
     path: data/srp_Cyrl/train/*
 - config_name: kor_Hang
   data_files:
   - split: train
     path: data/kor_Hang/train/*
 - config_name: slv_Latn
   data_files:
   - split: train
     path: data/slv_Latn/train/*
 - config_name: lit_Latn
   data_files:
   - split: train
     path: data/lit_Latn/train/*
 - config_name: hin_Deva
   data_files:
   - split: train
     path: data/hin_Deva/train/*
 - config_name: heb_Hebr
   data_files:
   - split: train
     path: data/heb_Hebr/train/*
 - config_name: bos_Latn
   data_files:
   - split: train
     path: data/bos_Latn/train/*
 - config_name: zsm_Latn
   data_files:
   - split: train
     path: data/zsm_Latn/train/*
 - config_name: ekk_Latn
   data_files:
   - split: train
     path: data/ekk_Latn/train/*
 - config_name: lvs_Latn
   data_files:
   - split: train
     path: data/lvs_Latn/train/*
 - config_name: ben_Beng
   data_files:
   - split: train
     path: data/ben_Beng/train/*
 - config_name: frp_Latn
   data_files:
   - split: train
     path: data/frp_Latn/train/*
 - config_name: isl_Latn
   data_files:
   - split: train
     path: data/isl_Latn/train/*
 - config_name: glk_Arab
   data_files:
   - split: train
     path: data/glk_Arab/train/*
 - config_name: eus_Latn
   data_files:
   - split: train
     path: data/eus_Latn/train/*
 - config_name: glg_Latn
   data_files:
   - split: train
     path: data/glg_Latn/train/*
 - config_name: als_Latn
   data_files:
   - split: train
     path: data/als_Latn/train/*
 - config_name: mkd_Cyrl
   data_files:
   - split: train
     path: data/mkd_Cyrl/train/*
 - config_name: mar_Deva
   data_files:
   - split: train
     path: data/mar_Deva/train/*
 - config_name: npi_Deva
   data_files:
   - split: train
     path: data/npi_Deva/train/*
 - config_name: kat_Geor
   data_files:
   - split: train
     path: data/kat_Geor/train/*
 - config_name: lat_Latn
   data_files:
   - split: train
     path: data/lat_Latn/train/*
 - config_name: pcm_Latn
   data_files:
   - split: train
     path: data/pcm_Latn/train/*
 - config_name: mlt_Latn
   data_files:
   - split: train
     path: data/mlt_Latn/train/*
 - config_name: cym_Latn
   data_files:
   - split: train
     path: data/cym_Latn/train/*
 - config_name: vec_Latn
   data_files:
   - split: train
     path: data/vec_Latn/train/*
 - config_name: hye_Armn
   data_files:
   - split: train
     path: data/hye_Armn/train/*
 - config_name: nrm_Latn
   data_files:
   - split: train
     path: data/nrm_Latn/train/*
 - config_name: wuu_Hani
   data_files:
   - split: train
     path: data/wuu_Hani/train/*
 - config_name: anp_Deva
   data_files:
   - split: train
     path: data/anp_Deva/train/*
 - config_name: bcc_Arab
   data_files:
   - split: train
     path: data/bcc_Arab/train/*
 - config_name: urd_Arab
   data_files:
   - split: train
     path: data/urd_Arab/train/*
 - config_name: afr_Latn
   data_files:
   - split: train
     path: data/afr_Latn/train/*
 - config_name: azj_Latn
   data_files:
   - split: train
     path: data/azj_Latn/train/*
 - config_name: tam_Taml
   data_files:
   - split: train
     path: data/tam_Taml/train/*
 - config_name: kaz_Cyrl
   data_files:
   - split: train
     path: data/kaz_Cyrl/train/*
 - config_name: nno_Latn
   data_files:
   - split: train
     path: data/nno_Latn/train/*
---

# 📚 FinePDFs-Edu 

![FinePDFs](https://cdn-uploads.huggingface.co/production/uploads/626ede24d2fa9e7d598c8709/dgGeCo6yfZvThn-Fc6Q8k.png)

> 350B+ of highly educational tokens from PDFs 📄

## What is it?

📚 FinePDFs-Edu dataset consists of **350B+ tokens** of educational PDFs filtered from 📄 [FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) dataset covering 69 languages.

FinePDFs was created using the formula inspired from [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu), we developed an [educational quality classifier](HuggingFaceFW/finepdfs_edu_classifier_eng_Latn) using annotations generated by Qwen3-235B-A22B-Instruct-2507 for each of 69 languages present in this dataset.
We then used this classifier to retain only the most educational web pages. FinePDFs-Edu outperforms FinePDFs on popular benchmarks and shows the power of classifiers trained on synthetic data. 

The [Dataset Curation](https://huggingface.co/datasets/HuggingFaceFW/finepdfs_edu#dataset-curation) section details the process for creating the dataset.
While it might seem that the dataset is an order of magnitude smaller than FineWeb-Edu, unlike its web ancestor, this dataset is globally deduplicated!


![datasets_comparison_edu](https://cdn-uploads.huggingface.co/production/uploads/626ede24d2fa9e7d598c8709/ivVKeFDP2J2MAyQL9s4xy.png)

## What is being released?

Along with the dataset, which includes all filtered CommonCrawl dumps since `CC-MAIN-2013-20` to `CC-MAIN-2025-08`, we also release:
- The [educational classifier](https://huggingface.co/HuggingFaceFW/finepdfs_edu_classifier_eng_Latn) used for the filtering (for each language)
- The [dataset](https://huggingface.co/datasets/HuggingFaceFW/finepdfs_eng_Latn_labeled) with educational (and 3 other) labels by Qwen3-235B-A22B-Instruct-2507 for English.
- The [dataset](HuggingFaceFW/finepdfs_fw_edu_labeled) with educational labels by Qwen3-235B-A22B-Instruct-2507 for 69 languages beyond English.
- The [code](https://github.com/huggingface/finepdfs) for training it and running inference.

## How to download and use 📄 FinePDFs-Edu

See the tables above for the `subset` of the language you want to download.

We currently do not provide smaller `sample` versions, but by setting `limit` or using `streaming=True` you can easily fetch a sample of the data. If there is interest from the community we might upload smaller sampled versions later on.

### Using 🏭 [`datatrove`](https://github.com/huggingface/datatrove/)

```python
from datatrove.pipeline.readers import ParquetReader

# limit determines how many documents will be streamed (remove for all)
# this will fetch the Portuguese filtered data
data_reader = ParquetReader("hf://datasets/HuggingFaceFW/finepdfs-edu/data/por_Latn/train", limit=1000) 
for document in data_reader():
    # do something with document
    print(document)

###############################    
# OR for a processing pipeline:
###############################

from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.readers import ParquetReader
from datatrove.pipeline.filters import LambdaFilter
from datatrove.pipeline.writers import JsonlWriter

pipeline_exec = LocalPipelineExecutor(
    pipeline=[
        ParquetReader("hf://datasets/HuggingFaceFW/finepdfs-edu/data/por_Latn/train", limit=1000),
        LambdaFilter(lambda doc: "hugging" in doc.text),
        JsonlWriter("some-output-path")
    ],
    tasks=10
)
pipeline_exec.run()
```

### Using `huggingface_hub`

```python
from huggingface_hub import snapshot_download
folder = snapshot_download(
                "HuggingFaceFW/finepdfs-edu", 
                repo_type="dataset",
                local_dir="./finepdfs-edu/",
                # download the Czech filtered
                allow_patterns=["data/ces_Latn/train/*"])
```

For faster downloads, make sure to install `pip install huggingface_hub[hf_transfer]` and set the environment variable `HF_HUB_ENABLE_HF_TRANSFER=1`.

### Using `datasets`
```python
from datasets import load_dataset
# get Croatian data
fw = load_dataset("HuggingFaceFW/finepdfs-edu", name="hrv_Latn", split="train", streaming=True)
```

Similiar to original FinePDFs, this dataset contains high amount of language switching samples, we thus recommend using the [filtering function](https://huggingface.co/datasets/HuggingFaceFW/finepdfs#code-switching) if this is not desired.

## Dataset curation
We have used the same approach for FineWeb-Edu with minimal adjustments of the prompt. To scale to languages beyond English we decided to train separate classifier for each.

### Educational Scoring

We used [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) to score approximately 300,000 FinePDFs samples for educational quality on a 0–5 scale. The final prompt used for scoring is available [here](https://huggingface.co/HuggingFaceFW/finepdfs_edu_classifier_eng_Latn/blob/main/prompt.txt).

After experimenting with several prompt variants, we found that the **FineWeb-Edu** prompt yielded the most consistent and reliable results. As in FineWeb-Edu, we observed that highly technical or graduate-level content did not correlate well with the benchmarks we track. However, unlike in FineWeb-Edu, the overall average score was noticeably lower—if we had used a fixed threshold of `score = 3`, only about 2% of samples would have been retained.
To address this, we instead selected the **top 10%** of samples based on their education score.

| Threshold | Drop Rate |
| :-------: | :-------: |
|     1     |   0.3028  |
|     2     |   0.9451  |
|     3     |   0.9802  |
|     4     |   0.9906  |
|     5     |   0.9987  |

We also replaced the teacher model to improve multilingual coverage and take advantage of the better inference efficiency offered by Mixture-of-Experts (MoE) architectures. To identify a suitable model, we aimed for one that was most *“Claude-like”*, i.e., whose scoring behavior most closely matched **Claude Sonnet-4**. We compared models using mean squared error (MSE) on a 10k-sample development set and found that **Qwen3-235B-A22B-Instruct-2507** was both the most Claude-like and highly efficient—processing up to **14 chunks/sec on a single H100 GPU**.

| Model                                         | MSE (vs. Sonnet-4) |
| :-------------------------------------------- | -----------------: |
| Qwen_Qwen3-235B-A22B-Instruct-2507            |          **0.398** |
| Qwen_Qwen3-235B-A22B-Thinking-2507            |              0.812 |
| Qwen_Qwen3-30B-A3B-Instruct-2507              |              0.364 |
| Qwen_Qwen3-30B-A3B-Thinking-2507              |              0.925 |
| google_gemma-3-27b-it                         |              2.727 |
| meta-llama_Llama-3.3-70B-Instruct             |              0.553 |
| meta-llama_Llama-4-Maverick-17B-128E-Instruct |              0.707 |
| meta-llama_Llama-4-Scout-17B-16E-Instruct     |              1.177 |
| mistralai_Magistral-Small-2507                |              0.717 |
| zai-org_GLM-4.5-Air-FP8                       |              0.510 |

For long documents, we take the first 2,048 tokens from the top of the document. If the document exceeds 10,000 characters, we also take the last 2,048 tokens and compute the final score as `max(top_score, bottom_score)`.

### Classifier Training

We fine-tuned a BERT-like regression model using these annotations, based on [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) for English and [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) for other languages. Both models achieved the best F1 performance among the options we evaluated, while supporting FA2, which allowed us to label over 220 samples per second on an H100 GPU.

For each model, we unfroze both the classifier head and the last four transformer layers. To address severe class imbalance, we rebalanced the training data.

The resulting classifiers are available at:
`https://huggingface.co/HuggingFaceFW/finepdfs_edu_classifier_{lang}`

### Filtering and results

We then built 📚 FinePDFs-Edu by filtering out 90% of samples with lowest edu score for each language. Our ablation demonstrated that this refined dataset surpasses 📄 FinePDFs and all other open web datasets, with remarkable improvements on educational benchmarks such as MMLU and ARC.
You will find all the ablation models and datasets in [this collection](https://huggingface.co/collections/HuggingFaceFW/finepdfs).

## Considerations for Using the Data
See: [FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs).

## Additional Information

### Licensing Information

The dataset is released under the **Open Data Commons Attribution License (ODC-By) v1.0** [license](https://opendatacommons.org/licenses/by/1-0/). The use of this dataset is also subject to [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use).

## Citation Information
```
@misc{kydlicek2025finepdfs,
      title={FinePDFs}, 
      author={Hynek Kydl{\'\i}{\v{c}}ek and Guilherme Penedo and Leandro von Werra},
      year={2025},
      publisher = {Hugging Face},
      journal = {Hugging Face repository},
      howpublished = {\url{https://huggingface.co/datasets/HuggingFaceFW/finepdfs_edu}}
}
```