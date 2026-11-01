---
dataset_info:
  features:
    - name: url
      dtype: string
    - name: text
      dtype: string
    - name: date
      dtype: string
    - name: metadata
      dtype: string
  splits:
    - name: train
      num_bytes: 56651995057
      num_examples: 6315233
  download_size: 16370689925
  dataset_size: 56651995057
  license: odc-by
  task_categories:
    - text-generation
  language:
    - en
  pretty_name: OpenWebMath
  size_categories:
    - 10B<n<100B
---

<img src="imgs/OpenWebMath-left.png" width="300">

[Keiran Paster](https://keirp.com)\*, [Marco Dos Santos](https://marco-dossantos.github.io/)\*, [Zhangir Azerbayev](https://zhangir-azerbayev.github.io/), [Jimmy Ba](https://jimmylba.github.io/)

[GitHub ](https://github.com/keirp/OpenWebMath) | [ArXiv](https://arxiv.org/abs/2310.06786)
| [PDF](https://arxiv.org/pdf/2310.06786.pdf)

**OpenWebMath** is a dataset containing the majority of the high-quality, mathematical text from the internet. It is filtered and extracted from over 200B HTML files on Common Crawl down to a set of **6.3 million documents** containing a total of **14.7B tokens**. OpenWebMath is intended for use in _pretraining_ and _finetuning_ large language models.

You can download the dataset using Hugging Face:

```python
from datasets import load_dataset
ds = load_dataset("open-web-math/open-web-math")
```

# OpenWebMath Contents

The dataset is structured as follows:

```python
{
  "text": ...,  # document text.
  "url": ...,  # document url.
  "date": ...,  # date the page was crawled.
  "metadata": ...,  # JSON containing information from the extraction process.
}
```

OpenWebMath contains documents from over 130k different domains, including data from forums, educational pages, and blogs. The dataset contains documents covering mathematics, physics, statistics, computer science, and more. The following table shows the most common domains in OpenWebMath by character count.

| Domain            | # Characters  | % Characters |
| ----------------- | ------------- | ------------ |
| stackexchange.com | 4,655,132,784 | 9.55%        |
| nature.com        | 1,529,935,838 | 3.14%        |
| wordpress.com     | 1,294,166,938 | 2.66%        |
| physicsforums.com | 1,160,137,919 | 2.38%        |
| github.io         | 725,689,722   | 1.49%        |
| zbmath.org        | 620,019,503   | 1.27%        |
| wikipedia.org     | 618,024,754   | 1.27%        |
| groundai.com      | 545,214,990   | 1.12%        |
| blogspot.com      | 520,392,333   | 1.07%        |
| mathoverflow.net  | 499,102,560   | 1.02%        |

# OpenWebMath Pipeline

<img src="imgs/pipeline.png" alt="Overview of the OpenWebMath Pipeline">

OpenWebMath builds on the massive [Common Crawl](https://commoncrawl.org/) dataset, which contains over 200B HTML documents. We filtered the data to only include documents that are: (1) in English, (2) contain mathematical content, and (3) are of high quality. We also put a strong emphasis on extracting LaTeX content from the HTML documents as well as reducing boilerplate in comparison to other web datasets.

The OpenWebMath pipeline consists of five steps:

1. **Prefiltering HTML Documents**:
   - We apply a simple prefilter to all HTML documents in Common Crawl in order to skip documents without mathematical content to unnecessary processing time.
2. **Text Extraction**:
   - Extract text, including LaTeX content, from the HTML documents while removing boilerplate.
3. **Content Classification and Filtering**:
   - Apply a [FastText language identification model](https://fasttext.cc/docs/en/language-identification.html) to keep only English documents.
   - Filter high perplexity documents using a [KenLM](https://github.com/kpu/kenlm) model trained on [Proof-Pile](https://huggingface.co/datasets/hoskinson-center/proof-pile).
   - Filter non-mathematical documents using our own _MathScore_ model.
4. **Deduplication**:
   - Deduplicate the dataset using SimHash in [text-dedup](https://github.com/ChenghaoMou/text-dedup).
5. **Manual Inspection**:
   - Inspect the documents gathered from previous steps and remove low quality pages.

For a detailed discussion on the processing pipeline, please refer to our paper.

# License

OpenWebMath is made available under an ODC-By 1.0 license; users should also abide by the CommonCrawl ToU: [https://commoncrawl.org/terms-of-use/](https://commoncrawl.org/terms-of-use/). We do not alter the license of any of the underlying data.

# Citation Information

```
@misc{paster2023openwebmath,
      title={OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text},
      author={Keiran Paster and Marco Dos Santos and Zhangir Azerbayev and Jimmy Ba},
      year={2023},
      eprint={2310.06786},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
