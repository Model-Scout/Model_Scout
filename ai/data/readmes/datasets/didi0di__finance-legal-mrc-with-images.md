---
dataset_info:
  config_name: tableqa
  features:
  - name: doc_title
    dtype: string
  - name: context
    dtype: string
  - name: table_title
    dtype: string
  - name: table_html
    dtype: string
  - name: question
    dtype: string
  - name: answer_text
    dtype: string
  - name: origin_id
    dtype: int64
  - name: unique_id
    dtype: string
  - name: table_image
    dtype: image
  splits:
  - name: test
    num_bytes: 1833993261.24
    num_examples: 1197
  download_size: 141756890
  dataset_size: 1833993261.24
configs:
- config_name: tableqa
  data_files:
  - split: test
    path: tableqa/test-*
license: cc-by-sa-4.0
task_categories:
- table-question-answering
- text-generation
language:
- ko
tags:
- finance
- legal
pretty_name: flm_w_img
size_categories:
- 1K<n<10K
---

# 🧾 finance-legal-mrc-with-images (tableqa/test)

**Multimodal-ready table image dataset** designed for TIG (Table Information Generation) input  
**TIG 입력 전용 테이블 이미지 데이터셋 (VLM 활용 가능)**

---

## 📦 Dataset Overview | 데이터셋 개요

| Feature            | Description (EN)                                         | 설명 (KR)                                   |
|--------------------|----------------------------------------------------------|----------------------------------------------|
| 🧩 Split            | `tableqa / test`                                         | `tableqa / test` 스플릿                       |
| 📄 Total Rows       | 1,197 (unique tables only)                               | 총 1,197건 (중복 제거된 고유 테이블 기준)     |
| 🖼️ Image Format     | PNG (rendered from raw HTML tables)                     | 원본 HTML 테이블을 PNG 이미지로 렌더링        |
| 🔗 Source           | Derived from [`shchoice/finance-legal-mrc`](https://huggingface.co/datasets/shchoice/finance-legal-mrc) | 기존 MRC 데이터셋에서 확장됨 |

> ⚠️ **Note:**  
> This dataset does not include TIG outputs (e.g., title, description, summary, key_entities).  
> Use it as input for VLM-based TIG generation.  
>  
> ⚠️ **주의:**  
> 본 데이터셋은 TIG 결과물(title, description 등)을 포함하지 않습니다.  
> 비전-언어 모델 기반 TIG 생성을 위한 **입력 전용** 데이터셋입니다.

---

## 🧠 Use Cases | 활용 예시

- 🎯 **TIG Input for VLM**  
  이미지 기반 테이블 정보를 입력으로 활용해 GPT-4o 등의 모델에서 TIG 수행

- 📊 **Table Structure Understanding**  
  모델이 테이블 구조, 패턴, 분포를 시각적으로 해석하도록 학습

- 🔍 **Multimodal RAG or Retrieval Tasks**  
  이미지 기반 질의응답 또는 검색(RAG) 프레임워크 테스트

---

## 🖼️ Sample | 샘플 예시

| unique_id           | table_title                                       | table_image        |
|---------------------|---------------------------------------------------|--------------------|
| unique_table_id_0   | [표 1] 세대별 총 인구수 변화                     | ![img](https://datasets-server.huggingface.co/assets/didi0di/finance-legal-mrc-with-images/--/1f8fb57ee745b5f4b44bdf53f9e55967cac5b670/--/tableqa/test/0/table_image/image.png?Expires=1753887766&Signature=dEwMqD0mAxVnsYzeFJI-vArL6tkbOXDtORw--6R1mqwu8CNsAtB8N6JnKgIBEu4xIdW~GU5FJgl2PHnweOtK~mU34kFiGdymY7Z5by0ZcGAprbMtPJkzl-QXq8U3T8e5qt3s9n2~oKkSCXAIpK5F06b-Mq4m7Wy-IqOh-pOKecamnae9onbD2b6zgT~lffiuYIHZvOwTYBFYna2ZrHAzHKAd9m2lZVcmVW-HcdaMrzUqXW1CXaG5DOGCq9SRd4DOcYwQPtU0cDTjOZM2ln8n6PAu9Tenl3d7HKftyflf-FNQRRsXkK5mfR3AO5RrNihCOc3mdNBHygxLAZiWV-pF~w__&Key-Pair-Id=K3EI6M078Z3AC3)|
| unique_table_id_1   | [표 2] 고령운전자 교통사고 사망률 비교           | ![img](https://datasets-server.huggingface.co/assets/didi0di/finance-legal-mrc-with-images/--/1f8fb57ee745b5f4b44bdf53f9e55967cac5b670/--/tableqa/test/1/table_image/image.png?Expires=1753887843&Signature=NQVcWaLQ81XZ5Tq0WQB3br8rOJlpYI7faodpRfv2RdTqlY7KmCV0xrVPNR~oXa0nMMxumlutlSI3749hmQb5R6IAC1Vels3uzP6pVcobPdZcYk5JjoQmfvpbaWsyuuW5XuwgLpEbZtKMj6yDm3h~-1~~USHKIKYbVjzSCpgAoAi~7WFMRrcmIZcl-O-PHke8q2wS-Nt21irJK4Jz-LHCQ9wFwLIFXlpZ-wXJUCeN907uEBp32mHk7RThHpa8Ml9~7kJ3FMEv~ijboFTRyrK4O~OEimcqQi2VxlPU7fmZPJe5QSNa9J8P9tWGqW3ImHCHif1R~natKumuspEx0005wQ__&Key-Pair-Id=K3EI6M078Z3AC3)|

---

## 📁 Data Fields | 포함된 필드

- `unique_id`: 유니크한 테이블 ID (`unique_table_id_0` 등)
- `origin_id`: 원본 `finance-legal-mrc` 데이터셋에서의 인덱스
- `document_title`: 테이블이 포함된 문서 제목
- `context`: 테이블 주변 문맥 정보
- `table_title`: 표 제목
- `table_html`: 원본 HTML 테이블
- `table_image`: 시각화된 테이블 이미지 (Hugging Face viewer 지원)

---

## ✨ How It Was Created | 생성 과정

1. `finance-legal-mrc/tableqa/test`에서 중복되지 않는 테이블 1,197개 추출
2. HTML 테이블을 이미지(PNG)로 렌더링
3. 메타데이터(JSON + 이미지 경로) 구성 후 `datasets.Image` 타입으로 처리
4. `DatasetDict`를 구성해 `tableqa/test` 스플릿으로 업로드

---

## 📌 Citation

```bibtex
@misc{didi0di_finance_legal_mrc_with_images,
  author = {didi0di},
  title = {Finance-Legal-MRC with Images},
  year = {2025},
  howpublished = {\url{https://huggingface.co/datasets/didi0di/finance-legal-mrc-with-images}},
  note = {TIG input dataset based on shchoice/finance-legal-mrc, extended with table images}
}
````

---

## 🛠 Maintainer

* ✍️ didi0di ([Hugging Face Profile](https://huggingface.co/didi0di))
* 📫 Questions or feedback? Feel free to open a discussion or contact me on Hugging Face!

---

