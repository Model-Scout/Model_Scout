---
annotations_creators:
- human-annotated
language:
- ko
license:
- mit
multilinguality:
- monolingual
source_datasets:
- extended|allganize/RAG-Evaluation-Dataset-KO
task_categories:
- other
dataset_info:
  - config_name: default
    features:
      - name: __key__
        dtype: string
      - name: __url__
        dtype: string
      - name: json
        struct:
          - name: domain
            dtype: string
          - name: file_name
            dtype: string
          - name: page_number
            dtype: int64
          - name: pages
            dtype: int64
          - name: pid
            dtype: string
          - name: test_cases
            list:
              - name: context_type
                dtype: string
              - name: pid
                dtype: string
              - name: qid
                dtype: string
              - name: question
                dtype: string
              - name: target_answer
                dtype: string
              - name: target_page_no
                dtype: string
      - name: pdf
        dtype: binary
    splits:
      - name: test
        num_bytes: 460216362
        num_examples: 1450
    download_size: 429930358
    dataset_size: 460216362
  - config_name: documents_meta
    features:
      - name: pid
        dtype: string
      - name: domain
        dtype: string
      - name: file_name
        dtype: string
      - name: pages
        dtype: int64
      - name: qid_count
        dtype: int64
      - name: qid_list
        sequence: string
    splits:
      - name: meta
        num_bytes: 9762
        num_examples: 64
    download_size: 8728
    dataset_size: 9762
  - config_name: questions_meta
    features:
      - name: qid
        dtype: string
      - name: question
        dtype: string
      - name: pid
        dtype: string
      - name: file_name
        dtype: string
      - name: target_page_no
        dtype: string
      - name: context_type
        dtype: string
      - name: target_answer
        dtype: string
    splits:
      - name: meta
        num_bytes: 192716
        num_examples: 300
    download_size: 102039
    dataset_size: 192716
configs:
  - config_name: default
    data_files:
      - split: test
        path: data/test-*
  - config_name: documents_meta
    data_files:
      - split: meta
        path: documents_meta/meta-*
  - config_name: questions_meta
    data_files:
      - split: meta
        path: questions_meta/meta-*
---

# Dataset Card for Reconstructed RAG Evaluation Dataset (KO)

## Dataset Summary
본 데이터셋은 `allganize/RAG-Evaluation-Dataset-KO`를 기반으로 PDF 파일을 포함하도록 재구성한 한국어 평가 데이터셋입니다. 원본 데이터셋에서는 PDF 파일의 경로만 제공되어 수동으로 파일을 다운로드해야 하는 불편함이 있었고, 일부 PDF 파일의 경로가 유효하지 않은 문제를 보완하기 위해 PDF 파일을 포함한 데이터셋을 재구성하였습니다.

## Supported Tasks and Leaderboards
- RAG Evaluation: 본 데이터는 한국어 RAG 파이프라인에 대한 E2E Evaluation이 가능합니다.

## Languages
The dataset is in Korean (`ko`).

## Dataset Structure

### Data Instances
데이터셋의 각 샘플은 PDF 문서의 페이지 단위로 분리되어 제공됩니다. 아래는 샘플 예제입니다:
```json
{
  "__key__": "0001",
  "__url__": "<tar 파일이 저장된 로컬 경로>",
  "json": {
    "domain": "law",
    "file_name": "[민사] 미성년자 성형외과 코필러 주입술 시 필러물질이 미성년자에 대한 사용금지 조치를 받은 상태였던 사안.pdf",
    "page_number": 1,
    "pages": 20,
    // pdf 파일에 대한 id
    "pid": "p_50",
    // 해당 pdf와 관련된 qa 데이터들의 모음.
    "test_cases": [ 
      {
        "context_type": "paragraph",
        "pid": "p_50",
        "qid": "q_222",
        "question": "원고 A이 시력 저하등의 증상이 발생한 시점은 언제로 보고, 그 시점 판단의 기준은 무엇인가요?",
        "target_answer": "원고 A의 시력 저하 등의 증상은 2017년 2월 25일 이전, 즉 필러 주입술 직후의 시점에 일어났다고 판단된다. 이 판단의 기준은 원고 A이 필러 주입술 3일 뒤인 2월 25일에 병원을 방문해 시력저하 등의 증상을 호소했지만, 진료기록에 '이미 그 전에 증상이 있었으나 환자는 쌍꺼풀 수술을 해서 그럴 것이라고 생각하였다'는 내용이 있었고, 필러 주입 후 코에 보호대를 착용했어서 초기에 증상을 알아차리기 어려웠을 것으로 보여진다는 점이다.",
        "target_page_no": "7"
      },
      ...
    ]
  },
  "pdf": "<PDF 바이너리 데이터>"
}
```

### Data Preprocessing
	•	PDF 파일을 페이지 단위로 분리하였습니다.
	•	각 페이지를 webdataset 형식의 하나의 예제로 구성하였습니다.

## Dataset Creation

### Curation Rationale
	•	원본 데이터셋의 불편함을 해소하고, 평가 작업을 쉽게 수행할 수 있도록 PDF 파일을 포함한 데이터셋을 재구성하였습니다.
	•	유효하지 않은 PDF 경로 문제를 해결하기 위해 모든 PDF 파일을 로컬 저장소에 포함시켰습니다.

### Source Data
	•	Original Dataset: allganize/RAG-Evaluation-Dataset-KO
	•	Reconstruction: 원본 데이터셋에서 제공된 경로의 PDF 파일을 수집 및 분리.


# RAG Evaluation preparation code.
* 원본 데이터에서 `allganize/RAG-Evaluation-Dataset-KO`, `documents.csv`와 유사한 구조로 데이터를 로드하는 코드.
  * 분리된 pdf binary는 병합하여 로컬 경로에 pdf파일로 저장함.
  
```python
import os
from typing import List
from itertools import groupby

import datasets
import pandas as pd
import fitz # pip install PyMuPDF

def merge_pdf_data(pdf_data_list:List[bytes], output_pdf_path:str):
    """Merge List of pdf binary to pdf files."""
    output_pdf = fitz.open()
    
    for pdf_data in pdf_data_list:
        pdf_document = fitz.open("pdf", pdf_data)
        for page_num in range(len(pdf_document)):
            output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
    
    output_pdf.save(output_pdf_path)
    output_pdf.close()
    
    print(f"Merged PDF saved as {output_pdf_path}")

def load_rag_eval_data(target_pdf_dir:str):
    """Load `allganize/RAG-Evaluation-Dataset-KO` dataset

    Process:
        * Download RAG Eval data from huggingface hub (query and pdf)
        * Build QA DataFrame
        * Cache the pdf_binary to local directory and return pdf metadata.
    """
    # load_dataset
    ds = datasets.load_dataset("datalama/RAG-Evaluation-Dataset-KO", split='test')
    target_pdf_dir = os.path.abspath(os.path.expanduser(target_pdf_dir))

    # get query
    qa_pairs = []
    for meta in ds['json']:
        test_cases = [{**tc, "domain":meta["domain"]} for tc in meta['test_cases']]
        qa_pairs += test_cases
    
    qa_df = pd.DataFrame(qa_pairs).drop_duplicates()
    qa_df['qid_int'] = qa_df['qid'].str.extract(r'(\d+)').astype(int)
    qa_df = qa_df.sort_values(by='qid_int').drop(columns=['qid_int']).reset_index(drop=True)
    cols = ["domain", "qid","question", "target_answer", "pid", "target_page_no", "context_type"]
    qa_df = qa_df.loc[:,cols]

    # get pdfs
    os.makedirs(target_pdf_dir, exist_ok=True)
    pid_indices = [(i, meta['pid']) for i, meta in enumerate(ds['json'])]
    # Grouping by the second element of the tuples
    grouped_pid_indices = {key: [item[0] for item in group] 
                           for key, group in groupby(pid_indices, lambda x: x[1])}
    
    pdf_meta_dict = dict()
    for i in range(len(grouped_pid_indices)):
        pid = f"p_{i}"
        output_path = f"{target_pdf_dir}/{pid}.pdf"
        sub_ds = ds.select(grouped_pid_indices[pid])
        sub_meta = sub_ds[0]['json']
    
        # merge and save pdf in local
        merge_pdf_data(sub_ds['pdf'], output_path)
        pdf_meta_dict[pid] = {
            "pid": pid,
            "domain": sub_meta["domain"],
            "file_name": sub_meta["file_name"],
            "pages": sub_meta["pages"],
            "local_file_path": output_path,
        }
        
    return qa_df, pdf_meta_dict


# Load Metadata
documents_meta = datasets.load_dataset("datalama/RAG-Evaluation-Dataset-KO", name="documents_meta") # 64개 문서에 대한 메타데이터
questions_meta = datasets.load_dataset("datalama/RAG-Evaluation-Dataset-KO", split="questions_meta") # 300개 질문에 대한 메타데이터
```
