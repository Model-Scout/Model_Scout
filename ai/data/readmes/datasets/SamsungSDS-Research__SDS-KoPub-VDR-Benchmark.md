---
license: cc-by-sa-4.0
language:
- ko
- en
tags:
- multimodal
- retrieval
- question-answering
- public-domain
- visual-document-retrieval
- rag
configs:
  - config_name: SDS-KoPub-QA
    data_files:
      - split: test
        path: "SDS-KoPub-QA.parquet"
  - config_name: SDS-KoPub-corpus
    data_files:
      - split: test
        path: "SDS-KoPub-corpus.parquet"
  - config_name: SDS-KoPub-annotations
    data_files:
      - split: test
        path: "SDS-KoPub-annotations.parquet"
task_categories:
- visual-document-retrieval
size_categories:
- 10K<n<100K
paperswithcode_id: sds-kopub-vdr

---


## 📘 Dataset Summary
**SDS KoPub-VDR** is a benchmark dataset for **Visual Document Retrieval (VDR)** in the context of <br>
**Korean public documents**. It contains real-world government document images paired with natural-language <br>
queries, corresponding answer pages, and ground-truth answers. The dataset is designed to evaluate AI models that <br>
go beyond simple text matching, requiring comprehensive understanding of **visual layouts, tables, graphs, and images** <br>
to accurately locate relevant information. The technical report is publicly available at https://arxiv.org/abs/2511.04910. 

### 🔍 Key Features
* **Authentic Public Data:** Includes diverse images of real Korean public documents.  
* **Multimodal Design:** Pairs textual queries with page-level visual evidence and answers.  
* **Beyond Text Matching:** Measures document-level visual understanding and retrieval capability.  

### 📊 Document and Page Distribution
| Source | Topic | # Docs | # Pages | Avg. Words/Page | URL |
|:--------|:------|-------:|--------:|----------------:|:----|
| **NAS** | Reports on diplomatic trends, international affairs | 7 | 366 | 215.45 | [NAS](https://nas.na.go.kr/nas/bbs/BNAS1011/list.do?menuNo=1800043) |
| **NARS** | Reports on administrative actions, legislative cases | 125 | 8,176 | 180.22 | [NARS](https://www.nars.go.kr/) |
| **NABO** | Fiscal analyses, project evaluation reports | 2 | 310 | 278.41 | [NABO](https://www.nabo.go.kr/) |
| **PRISM** | Research on social, environmental, and industrial policy | 122 | 31,500 | 244.23 | [PRISM](https://www.prism.go.kr) |
| **MOLEG** | Legal guides, statutory interpretations, case studies | 105 | 429 | 218.69 | [MOLEG](https://www.easylaw.go.kr) |

---

## 🧮 Dataset Creation Process

The SDS-KoPub-VDR QA dataset was constructed through a multi-stage pipeline designed to ensure both realism and reliability in multimodal question–answer generation.

### 1️⃣ QA Generation
We automatically generated multimodal QA pairs using **GPT-4o** and **Qwen2.5-VL-72B**, leveraging preprocessed page images, OCR text, and metadata.  
To ensure realistic and context-aware queries, three complementary prompting strategies were employed:
- **Instruction-based prompting:** Models were instructed to generate questions as if the user had not seen the page, with answers strictly grounded in on-page evidence.  
- **Persona-augmented prompting:** Domain-specific personas (e.g., *Policy Maker*, *Citizen Petitioner*, *Journalist*) encouraged queries reflecting real-world user intent and reasoning.  
- **Dynamic few-shot prompting:** Relevant examples were dynamically retrieved from a domain-specific few-shot pool, enabling domain-consistent question styles and response formats.

### 2️⃣ Automated Validation (GPT-4.5)
All generated QA pairs underwent **semantic validation using GPT-4.5**, which evaluated:
- **Context relevance** – Is the question answerable based on the page content?  
- **Answer faithfulness** – Is the answer accurately grounded in the page evidence?  
- **Hallucination check** – Does the answer contain fabricated or external information?  
Low-quality pairs were filtered out based on these criteria, ensuring semantic consistency and factual correctness.

### 3️⃣ Human Expert Review
Finally, domain researchers performed a **full manual review** using a custom annotation tool.  
Each QA pair was verified for:
- Query clarity and specificity  
- Answer correctness and completeness  
- Evidence alignment and modality appropriateness  


#### This dataset was developed using OpenAI’s GPT-4o and GPT-4.5 models, as well as Alibaba’s Qwen series (notably Qwen2.5-VL 72B) — Built with Qwen.

---

## 📂 Dataset Structure

### Components

The dataset is composed of three components:

| Component | File / Folder | Description |
|:-----------|:---------------|:-------------|
| **Document metadata** | `SDS-KoPub-annotations.parquet` | Metadata linking each document to its constituent pages and QA pairs |
| **Multimodal corpus** | `SDS-KoPub-corpus.parquet` | Page-level corpus containing multimodal inputs (image, text, OCR) |
| **QA dataset** | `SDS-KoPub-QA.parquet` | Question–answer annotations and page-level representations |

### 1️⃣ Document Metadata
**File:** `SDS-KoPub-annotations.parquet`
| Name | Type | Description |
|:-----|:-----|:------------|
| `file_id` | string | Unique document identifier |
| `file_name` | string | Original document name |
| `down_url` | string | Public download link of the document |
| `page_indices` | list[int] | List of page indices included in `SDS-KoPub-corpus` |
| `query_indices` | list[int] | List of query–answer indices linked from `SDS-KoPub-QA` |
| `indication_of_the_source` | string | The source and license of the work |

### 2️⃣ Corpus
**File:** `SDS-KoPub-corpus.parquet`
| Name | Type | Description |
|:-----|:-----|:------------|
| `id` | string | Unique identifier for a page |
| `file_name` | string | Source document name |
| `image` | PIL.Image.Image | Rendered page image (PIL format) |
| `text` | string | Extracted text using PdfReader (pypdf, pypdfium2) |
| `ocr` | string | Raw OCR Output |


### 3️⃣ QA dataset
**File:** `SDS-KoPub-QA.parquet`
| Name | Type | Description |
|:-----|:-----|:------------|
| `id` | string | Page ID for ground-truth evidence (not unique) |
| `query` | string | Natural language question |
| `answer` | string | Ground-truth answer |
| `type` | string | Query modality type (`text`, `visual`, or `cross`) |
| `domain` | string | Domain or category of the document |
| `ground_truth` | list[] | Ground-truth evidence page indices |

---

## 📊 Statistics

| Metric | Value |
|:--------|:-------|
| Documents | 361 |
| Pages | 40,781 |
| QA Pairs | 600 |
| Domains | 6 (Society, Environment, Education, Industry, Diplomacy, Finance) |
| Modality Types | Text / Visual / Cross-modal |

## Citation

```bibtex
@misc{lee2025sdskopubvdrbenchmark,
      title={SDS KoPub VDR: A Benchmark Dataset for Visual Document Retrieval in Korean Public Documents}, 
      author={Jaehoon Lee and Sohyun Kim and Wanggeun Park and Geon Lee and Seungkyung Kim and Minyoung Lee},
      year={2025},
      eprint={2511.04910},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.04910}, 
}
```

## Contributor
- Jaehoon Lee (jhlee19.lee@samsung.com)
- Sohyun Kim (sh_sds.kim@samsung.com)
- Wanggeun Park (wking.park@samsung.com)
- Geun Lee (go.lee@samsung.com)
- Seungkyung Kim (seungkyung.kim@samsung.com)
- Minyoung Lee (miny.lee@samsung.com)