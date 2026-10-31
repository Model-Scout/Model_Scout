---
language:
- en
- fr
- es
- zh
- de
- it
- pt
- ko
- ru
pretty_name: Biomed-Enriched
task_categories:
- text-classification
dataset_info:
  features:
  - name: id
    dtype: string
  - name: article_id
    dtype: string
  - name: path
    dtype: string
  - name: text
    dtype: string
  - name: language
    dtype: string
  - name: section_title
    dtype: string
  - name: domain
    dtype: string
  - name: document_type
    dtype: string
  - name: educational_score
    dtype: float64
  - name: domain_scores
    sequence: float64
  - name: document_type_scores
    sequence: float64
  - name: language_score
    dtype: float64
  - name: authors
    sequence: string
  - name: article_url
    dtype: string
  - name: license_url
    dtype: string
  splits:
  - name: commercial
    num_bytes: 126945006652
    num_examples: 98595508
  - name: noncommercial
    num_bytes: 19998737015
    num_examples: 47449067
  download_size: 52228107549
  dataset_size: 146943743667
configs:
- config_name: default
  data_files:
  - split: commercial
    path: data/commercial-*
  - split: noncommercial
    path: data/noncommercial-*
---

![Biomed-Enriched](logo.png)

# Biomed-Enriched: A Biomedical Dataset Enriched with LLMs for Pretraining and Extracting Rare and Hidden Content 

### Dataset Authors

**Rian Touchent, Nathan Godey & Eric de la Clergerie**  
*Sorbonne Université, INRIA Paris*

### Overview

Biomed-Enriched is a PubMed-derived dataset created using a two-stage annotation process. Initially, [Llama 3.1 70B Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) annotated 400K paragraphs for document type, domain, and educational quality. These annotations were then used to fine-tune a [smaller model](https://huggingface.co/almanach/Biomed-Enriched-classifier), which propagated the labels across the entire PubMed Central Open Access corpus. This process yielded 2M clinical case paragraphs, with over 450K high-quality paragraphs licensed for commercial use. This dataset provides a large-scale, openly available alternative to private clinical text. In continual pre-training experiments with OLMo2, curated subsets showed targeted improvements: clinical upsampling boosted MMLU ProfMed scores by ~5%, and educational quality filtering improved MedQA and MedMCQA by ~1%. Combining these methods achieved similar performance compared to standard continual-pretraining with just one-third of the training tokens, highlighting the potential for more efficient biomedical pretraining.

The dataset is structured into two primary splits:

* **Commercial**
* **Non-Commercial**

## Dataset Structure

### Commercial Split

* **text**: Textual content of the paragraphs.
* **path**: Precise XML path referencing original paragraph locations.
* **license\_url**: URL linking to the license.
* **authors**: Comprehensive list of authors per paragraph for proper attribution compliance.

### Non-Commercial Split

* **path**: Precise XML path referencing original paragraph locations.
* **license\_url**: URL linking to the license.
* **authors**: Comprehensive list of authors per paragraph for proper attribution compliance.

> **Note:** The non-commercial split does not contain text data due to licensing restrictions. However, we provide scripts to populate the `text` field from a local PMC Open Access XML dump. See below for installation and usage instructions.

```bash
pip install biomed-enriched
```

### With Python
```python
from biomed_enriched import populate

DATASET_DIR = "/path/to/biomed-enriched"  # input dataset
PMC_XML_ROOT = "/path/to/pmc/non-comm/xml"          # PMC XML dump
OUTPUT_DIR = "/path/to/populated-biomed-enriched"  # drop arg to overwrite in-place

populate(DATASET_DIR, PMC_XML_ROOT, output_path=OUTPUT_DIR, splits="noncommercial", num_proc=1)
```
The call overwrites the dataset in-place, adding a new `text` column as the third column (after `article_id`, `path`).

### With CLI
```bash
biomed-enriched \
  --input /path/to/biomed-enriched \
  --xml-root /path/to/pmc/non-comm/xml \
  --num-proc 8
```
Add `--output DIR` if you prefer writing to a new directory instead of overwriting.

## Annotation Process

The dataset was created using a two-stage annotation framework:

1. **Initial Annotation by Large Language Model**:

* Annotated a subset of paragraphs for the following categories:
   
 - **Document Type**: Categorizes the structure and purpose of the content.
   - **Clinical Case**: Detailed report of symptoms, diagnosis, treatment, and follow-up of individual patients.
   - **Study**: Research paragraph with methods, results, and discussion of experiments or observations.
   - **Review**: Summary or synthesis of current knowledge on a specific topic.
   - **Other**: Content not fitting above categories (editorials, commentaries, policy paragraphs).
 - **Domain**: Identifies the subject area focus.
   - **Clinical**: Content relating to patient care, clinical trials, case reports, or practice guidelines.
   - **Biomedical**: Scientific aspects of medicine and biology.
   - **Other**: Content mentioning biomedical topics but focusing on administrative, policy, or general communications.
 - **Educational Quality**: Assesses pedagogical value for college-level biomedical learning on a scale from 1 (minimal value) to 5 (exceptional value) inspired by FineWeb-edu.
   - **Score 1**: Basic information relevant to biomedical topics, may contain irrelevant content.
   - **Score 2**: Addresses biomedical education elements but with limitations in coherence or depth.
   - **Score 3**: Appropriate for college-level curricula, introduces key concepts with reasonable coherence.
   - **Score 4**: Highly relevant educational content with clear writing style, minimal irrelevant information.
   - **Score 5**: Outstanding educational value, detailed reasoning with profound insights for college-level learning.

2. **Annotation Scaling via Model Distillation**:

* These annotations were distilled into a XLM-RoBERTa-base model, enabling scalability to the entire PMC dataset.

## Annotation Statistics

Here is the distribution of educational scores per domain:

| Educational Score | Biomedical (n=116 221 134) | Clinical (n=2 182 784) | Other (n=15 213 051) |
| :---------------: | :------------------------: | :--------------------: | :------------------: |
|         1         |            1.8 %           |          6.0 %         |        60.1 %        |
|         2         |            9.4 %           |         23.4 %         |        29.4 %        |
|         3         |           10.9 %           |         26.6 %         |         8.3 %        |
|         4         |           75.3 %           |         44.0 %         |         2.1 %        |
|         5         |            2.6 %           |            –           |           –          |

Here is the distribution of educational scores per document type:

| Educational Score | Study (n=100 387 809) | Review (n=6 811 226) | Clinical case (n=2 122 403) | Other (n=24 295 531) |
|:-----------------:|:---------------------:|:--------------------:|:---------------------------:|:--------------------:|
| 1                 | 0.7 %                 | 0.3 %                | 4.0 %                       | 43.4 %               |
| 2                 | 7.9 %                 | 1.6 %                | 14.4 %                      | 30.9 %               |
| 3                 | 10.0 %                | 5.0 %                | 24.6 %                      | 14.6 %               |
| 4                 | 78.7 %                | 86.9 %               | 57.0 %                      | 11.1 %               |
| 5                 | 2.6 %                 | 6.1 %                | 0.0 %                       | 0.0 %                |

### Language Distribution


| Language | Articles | Paragraphs | Clinical Case Paragraphs | % Clinical Cases |
|----------|----------|------------|-------------------------|-----------------|
| en       | 4,113,275| 131,579,445| 2,113,185               | 1.61            |
| es       | 4,339    | 181,779    | 1,235                   | 0.68            |
| zh-cn    | 3,649    | 59,719     | 0                       | 0.00            |
| fr       | 3,410    | 173,325    | 2,586                   | 1.49            |
| de       | 2,976    | 248,608    | 51                      | 0.02            |
| it       | 2,708    | 274,819    | 521                     | 0.19            |
| pt       | 934      | 85,242     | 4,540                   | 5.33            |
| ko       | 636      | 25,535     | 0                       | 0.00            |
| ru       | 222      | 10,553     | 0                       | 0.00            |
| id       | 189      | 91,865     | 15                      | 0.02            |


## Key Applications

* Improve efficiency in biomedical pretraining by focusing on high-quality, specific content.
* Create new biomedical subsets tailored to specific research needs based on document type and domain.

## Evaluation

Our evaluation focuses on isolating the effects of data curation rather than pursuing state-of-the-art scores on benchmarks. A more powerful foundation model would likely yield higher absolute scores but would obscure the precise impact of our dataset. We therefore selected `OLMo2-7B-stage1` as our foundation model, as this intermediate checkpoint provides strong baseline capabilities while allowing for a clear attribution of performance gains to our enrichment strategies. This model has already developed strong language modeling capabilities but precedes the knowledge-intensive tuning of stage 2, providing an ideal balance without the risk of catastrophic forgetting of instruction-following abilities during domain adaptation. Notably, the data mix used in phase 1 includes DCLM, a dataset filtered from web data using a classifier trained on instruction data, which gives OLMo2-7B relatively strong question-answering capabilities even after stage 1.

Each Biomed-Enriched variant was trained for exactly 33.6 billion tokens using identical hyperparameters. We follow the annealing strategy of OLMo2 used in the mid-training phase. By maintaining strict parameter parity across experiments, we created a controlled environment focused solely on measuring the effectiveness of different data curation strategies.

These experiments are designed to illustrate how our granular annotations enable targeted improvements in model capabilities. For instance, by specifically upsampling clinical content (`BE-Clinical` and `BE-ClinicalCase` variants), we expect to see a notable increase in performance on the MMLU Professional Medicine benchmark, underscoring the dataset's potential for developing specialized models.

The following variants were created for this evaluation:
*   **BE-Base:** The complete unmodified PMC Open Access Subset serving as baseline.
*   **BE-Educational:** Preserves all articles but removes paragraphs with educational quality scores below 3.
*   **BE-Clinical:** Replicates articles with predominantly clinical domain content 10× in the training mix.
*   **BE-ClinicalCase:** Replicates articles containing at least one clinical case paragraph 10× to increase exposure to clinical narratives.
*   **BE-Prefix:** Prefixes each paragraph with its predicted annotations to allow modeling of metadata-content relationships.
*   **BE-French:** Upsamples articles containing French text 10× to address language imbalance.
*   **BE-All:** Combines quality filtering (score ≥ 3), upsampling of clinical content, French text, and clinical cases, plus metadata prefixing.

### Performance Results

**SOTA Models for reference**

| Model             | MedQA | MedMCQA | PubMedQA | Anat  | Clin  | Bio   | Med   | Gen   | Prof  | Avg   |
| ----------------- | :---: | :-----: | :------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Llama-3-8B        | 59.70 |  57.47  |  74.80   | 68.89 | 74.72 | 78.47 | 61.85 | 83.00 | 70.22 | 69.90 |
| Meditron-70B      | 57.10 |  46.80  |  76.60   | 53.30 | 66.70 | 76.30 | 63.00 | 69.00 | 71.60 | 64.49 |

**Benchmark Results by Dataset Variant (continual pre-training of OLMo2-7B-stage1)**

| Variant         | MedQA          | MedMCQA        | PubMedQA       | Anat           | Clin           | Bio            | Med            | Gen            | Prof           | Avg            |
| --------------- | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |
| OLMo2-7B-stage1   | 45.33 |  41.14  |  75.60   | 54.81 | 63.40 | 69.44 | 53.18 | 69.00 | 59.93 | 59.09 |
| BE-Base         | 44.85          | 41.91          | 76.40          | 57.04          | 64.15          | **70.83**      | **59.54**      | 69.00          | 59.93          | 60.41          |
| BE-Clinical     | 41.95          | 39.35          | 76.60          | 53.33          | 63.40          | 65.28          | 58.38          | 66.00          | **63.97**      | 58.70          |
| BE-ClinicalCase | 42.11          | 39.52          | 76.60          | 57.04          | 64.91          | 66.67          | **59.54**      | 69.00          | 62.87          | 59.81          |
| BE-Prefix       | 45.72          | 41.76          | **77.80**      | 57.04          | 64.53          | 68.75          | 57.23          | 66.00          | 61.76          | 60.07          |
| BE-Educational  | 45.64          | **43.08**      | 77.00          | 57.04          | 65.28          | 68.06          | 56.65          | **71.00**      | 58.82          | 60.29          |
| BE-All          | **47.21**      | 42.79          | 76.60          | **60.00**      | **65.66**      | 68.06          | 58.96          | 69.00          | 61.40          | **61.08**      |

*Note: The first three columns represent Medical QA benchmarks. The following six (Anat, Clin, Bio, Med, Gen, Prof) are sub-tasks from MMLU Medical. MMLU abbreviations: Anat=Anatomy, Clin=Clinical Knowledge, Bio=College Biology, Med=College Medicine, Gen=Medical Genetics, Prof=Professional Medicine.*

### Results Analysis

**Overall performance.** BE-All achieved the highest average performance across benchmarks at 61.08%, surpassing BE-Base (60.41%) by a small but consistent margin (+0.67 pts, see table above). Its strongest improvements appeared in MedQA (47.21%), MMLU Anatomy (60.00%), and Clinical Knowledge (65.66%), suggesting the effectiveness of combining multiple targeted enrichment strategies.

**Clinical enrichment.** Clinical enrichment (BE-Clinical) significantly boosted performance on MMLU Professional Medicine benchmark (63.97%, +4.04 pts vs. BE-Base, Figure 2). This improvement was stable from early training, highlighting how clinical narratives enhance the model’s clinical reasoning abilities efficiently.

**Educational filtering.** Educational filtering (BE-Educational) consistently improved performance on medical question-answering tasks, notably Medical Genetics (71.00%, +2 pts), MedMCQA (43.08%, +1.17 pts), and PubMedQA (77.00%, +0.6 pts). These tasks likely benefit from the knowledge present in educationally high-quality paragraphs (Figure 2).

**Metadata prefixing.** Metadata prefixing (BE-Prefix) specifically improved performance on PubMedQA (77.80%, +1.4 pts vs. BE-Base). Providing explicit paragraph-level metadata helped primarily with structured document comprehension, but it had limited benefits for other tasks.

**General biomedical knowledge trade-off.** BE-Base performed better on College Biology (70.83%) than others. Building a biology variant (BE-Bio) could be an interesting future direction, as the current dataset does not specifically target this domain.

**Non-English enrichment.** BE-French showed clear improvements in French medical QA (FrenchMedMCQA), achieving 40.5% accuracy, significantly surpassing BE-Base and the OLMo2-7B-stage1 baseline (38.32%, Figure 1). These results illustrate effective adaptation to non-English contexts without modifying the underlying model architecture.

![Benchmark Results](french_medmcqa_performance.png)

**Data efficiency and training stability.** As shown in Figure 2, BE-All reached robust benchmark performance using roughly one-third of the tokens required by BE-Base. Individual enrichments (Educational, Clinical) also displayed early and stable improvements, underscoring potential reductions in training time and computational cost.

![Benchmark Results](combined_plot.png)

## Licensing

The Biomed-Enriched annotations (document type, domain, educational quality scores, and metadata) are released under the MIT License.

The textual content licensing depends on the individual article licenses from PubMed Central Open Access. Each paragraph includes a `license_url` field pointing to the specific license. Users must comply with the respective license terms when using the textual data.

## How to Cite

Please cite Biomed-Enriched using:

```

@inproceedings{touchent-etal-2026-biomed,
    title = "Biomed-Enriched: Data-Efficient Biomedical Pretraining via Paragraph-Level Annotation",
    author = "Touchent, Rian  and
      Godey, Nathan  and
      Villemonte de la Clergerie, {\'E}ric",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {ACL} 2026",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-acl.1713/",
    doi = "10.18653/v1/2026.findings-acl.1713",
    pages = "34276--34287",
    ISBN = "979-8-89176-395-1",
    abstract = "We annotate PubMed Central paragraphs for document type, domain, and educational quality using a two-stage pipeline: Llama-3.1-70B labels 400K paragraphs, then a fine-tuned XLM-RoBERTa propagates annotations to the full corpus. This paragraph-level approach captures content diversity within scientific articles that document-level labels miss. The resulting Biomed-Enriched corpus contains 2M clinical case paragraphs, providing a publicly available alternative to restricted clinical datasets. For decoders, continual pretraining experiments enable targeted improvements, with clinical upsampling boosting performance by 4 points on MMLU ProfMed and educational filtering improving MedQA and MedMCQA by {\textasciitilde}1 point. Combinations of these techniques led to faster convergence, reaching the same performance with a third of training tokens. For encoders, our best recipe matches BioClinical-ModernBERT on 11 tasks (77.3{\%} vs 77.1{\%} F1) while using 2.5x fewer tokens and only public data."
}

@misc{touchent2025biomedenrichedbiomedicaldatasetenriched,
      title={Biomed-Enriched: A Biomedical Dataset Enriched with LLMs for Pretraining and Extracting Rare and Hidden Content}, 
      author={Rian Touchent and Nathan Godey and Eric de la Clergerie},
      year={2025},
      eprint={2506.20331},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.20331}, 
}
```

[Paper](https://huggingface.co/papers/2506.20331)