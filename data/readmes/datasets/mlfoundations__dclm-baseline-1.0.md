---
license: cc-by-4.0
dataset_info:
  features:
  - name: bff_contained_ngram_count_before_dedupe
    dtype: int64
  - name: language_id_whole_page_fasttext
    struct:
    - name: en
      dtype: float64
  - name: metadata
    struct:
    - name: Content-Length
      dtype: string
    - name: Content-Type
      dtype: string
    - name: WARC-Block-Digest
      dtype: string
    - name: WARC-Concurrent-To
      dtype: string
    - name: WARC-Date
      dtype: timestamp[s]
    - name: WARC-IP-Address
      dtype: string
    - name: WARC-Identified-Payload-Type
      dtype: string
    - name: WARC-Payload-Digest
      dtype: string
    - name: WARC-Record-ID
      dtype: string
    - name: WARC-Target-URI
      dtype: string
    - name: WARC-Type
      dtype: string
    - name: WARC-Warcinfo-ID
      dtype: string
    - name: WARC-Truncated
      dtype: string
  - name: previous_word_count
    dtype: int64
  - name: text
    dtype: string
  - name: url
    dtype: string
  - name: warcinfo
    dtype: string
  - name: fasttext_openhermes_reddit_eli5_vs_rw_v2_bigram_200k_train_prob
    dtype: float64
---
## DCLM-baseline 
DCLM-baseline is a 4T token / 3B document pretraining dataset that achieves strong performance on language model benchmarks.


Below are comparisions of model trained on DCLM-baseline with other models in the 7B regime.

| Model         | Params | Tokens | Open dataset? | CORE     | MMLU     | EXTENDED |
|---------------|--------|--------|---------------|----------|----------|----------|
| **Open weights, closed datasets** |        |        |               |          |          |          |
| Llama2        | 7B     | 2T     | ✗             | 49.2     | 45.8     | 34.1     |
| DeepSeek      | 7B     | 2T     | ✗             | 50.7     | 48.5     | 35.3     |
| Mistral-0.3   | 7B     | ?      | ✗             | 57.0     | 62.7     | 45.1     |
| QWEN-2        | 7B     | ?      | ✗             | 57.5     | **71.9** | 50.5     |
| Llama3        | 8B     | 15T    | ✗             | 57.6     | 66.2     | 46.3     |
| Gemma         | 8B     | 6T     | ✗             | 57.8     | 64.3     | 44.6     |
| Phi-3         | 7B     | ?      | ✗             | **61.0** | 69.9     | **57.9** |
| **Open weights, open datasets** |        |        |               |          |          |          |
| Falcon        | 7B     | 1T     | ✓             | 44.1     | 27.4     | 25.1     |
| Amber         | 7B     | 1.2T   | ✓             | 39.8     | 27.9     | 22.3     |
| Crystal       | 7B     | 1.2T   | ✓             | 48.0     | 48.2     | 33.2     |
| OLMo-1.7      | 7B     | 2.1T   | ✓             | 47.0     | 54.0     | 34.2     |
| MAP-Neo       | 7B     | 4.5T   | ✓             | **50.2** | **57.1** | **40.4** |
| **Models we trained** |        |        |               |          |          |          |
| FineWeb edu   | 7B     | 0.14T  | ✓             | 38.7     | 26.3     | 22.1     |
| FineWeb edu   | 7B     | 0.28T  | ✓             | 41.9     | 37.3     | 24.5     |
| **DCLM-BASELINE** | 7B     | 0.14T  | ✓             | 44.1     | 38.3     | 25.0     |
| **DCLM-BASELINE** | 7B     | 0.28T  | ✓             | 48.9     | 50.8     | 31.8     |
| **DCLM-BASELINE** | 7B     | 2.6T   | ✓             | **57.1** | **63.7** | **45.4** |


## Dataset Details
### Dataset Description
- **Curated by:** The DCLM Team
- **Language(s) (NLP):** English
- **License:**  CC-by-4.0
### Dataset Sources
- **Repository:** https://datacomp.ai/dclm
- **Paper:**: https://arxiv.org/abs/2406.11794
- **Construction Code**: https://github.com/mlfoundations/dclm



## Uses
### Direct Use
DCLM-Baseline is intended to be used as a research baseline for the DCLM benchmark. It demonstrates the importance of data curation in training performant language models. 
### Out-of-Scope Use
DCLM-Baseline is not intended for training production-ready models or for specific domains such as code and math. It may not perform as well as domain-specific datasets for these tasks. Due to these limitations, the dataset is intended for research use only.
DCLM-Baseline is a subset of the DCLM-Pool, which is a corpus of 240 trillion tokens derived from Common Crawl. The dataset is in plain text format.
## Dataset Creation
### Curation Rationale
DCLM-Baseline was created to demonstrate the effectiveness of the DCLM testbed in developing high-quality training sets for language models. It serves as a proof of concept for the data curation strategies enabled by DCLM and is designed to be a research baseline for the benchmark.
### Source Data
#### Data Collection and Processing
DCLM-Baseline was created by applying a series of cleaning, filtering, and deduplication steps to the raw Common Crawl data (DCLM-Pool). The key steps include:
1. Heuristic cleaning and filtering (reproduction of RefinedWeb)
2. Deduplication using a Bloom filter
3. Model-based filtering using a fastText classifier trained on instruction-formatted data (OpenHermes 2.5 and r/ExplainLikeImFive)
#### Who are the source data producers?
The source data is from Common Crawl, which is a repository of web crawl data.
### Personal and Sensitive Information
[More Information Needed]
## Bias, Risks, and Limitations
The dataset may contain biases present in the Common Crawl data. The dataset's performance on code and math tasks is limited compared to its performance on language understanding tasks. DCLM-Baseline is designed for research purposes only.
### Recommendations
Users should be aware of the potential biases and limitations of the dataset, especially when using it for specific domains like code and math. The dataset should only be used for research purposes in the context of the DCLM benchmark.
## Citation

```bibtex
@misc{li2024datacomplm,
      title={DataComp-LM: In search of the next generation of training sets for language models}, 
      author={Jeffrey Li and Alex Fang and Georgios Smyrnis and Maor Ivgi and Matt Jordan and Samir Gadre and Hritik Bansal and Etash Guha and Sedrick Keh and Kushal Arora and Saurabh Garg and Rui Xin and Niklas Muennighoff and Reinhard Heckel and Jean Mercat and Mayee Chen and Suchin Gururangan and Mitchell Wortsman and Alon Albalak and Yonatan Bitton and Marianna Nezhurina and Amro Abbas and Cheng-Yu Hsieh and Dhruba Ghosh and Josh Gardner and Maciej Kilian and Hanlin Zhang and Rulin Shao and Sarah Pratt and Sunny Sanyal and Gabriel Ilharco and Giannis Daras and Kalyani Marathe and Aaron Gokaslan and Jieyu Zhang and Khyathi Chandu and Thao Nguyen and Igor Vasiljevic and Sham Kakade and Shuran Song and Sujay Sanghavi and Fartash Faghri and Sewoong Oh and Luke Zettlemoyer and Kyle Lo and Alaaeldin El-Nouby and Hadi Pouransari and Alexander Toshev and Stephanie Wang and Dirk Groeneveld and Luca Soldaini and Pang Wei Koh and Jenia Jitsev and Thomas Kollar and Alexandros G. Dimakis and Yair Carmon and Achal Dave and Ludwig Schmidt and Vaishaal Shankar},
      year={2024},
      eprint={2406.11794},
      archivePrefix={arXiv},
      primaryClass={id='cs.LG' full_name='Machine Learning' is_active=True alt_name=None in_archive='cs' is_general=False description='Papers on all aspects of machine learning research (supervised, unsupervised, reinforcement learning, bandit problems, and so on) including also robustness, explanation, fairness, and methodology. cs.LG is also an appropriate primary category for applications of machine learning methods.'}

```



