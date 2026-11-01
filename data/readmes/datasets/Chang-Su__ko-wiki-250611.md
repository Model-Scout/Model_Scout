---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 988975558
    num_examples: 909724
  download_size: 579400197
  dataset_size: 988975558
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---


---
license: cc-by-sa-4.0
language:
- ko
---

# **ko-wiki-250611**

## **데이터셋 요약 (Dataset Summary)**

본 데이터셋은 위키미디어(Wikimedia)에서 제공하는 한국어 위키피디아(Wikipedia)의 최신 덤프 파일(2025년 6월 11일 기준)을 기반으로 구축되었습니다. 최신 정보가 반영된 한국어 자연어 처리(NLP) 연구 및 모델 학습을 위해 문장 단위로 분할하고, 일정 길이의 세그먼트로 재구성하여 사용 편의성을 높였습니다.

* **데이터 소스:** [한국어 위키피디아 덤프](https://dumps.wikimedia.org/kowiki/)
* **지식 기준일 (Knowledge Cutoff):** 2025년 6월 11일 05:00 (KST)
* **언어:** 한국어 (ko)

## **데이터셋 구축 (Dataset Creation)**

최신 한국어 위키피디아 데이터를 활용하고자 하는 필요성에 의해 직접 데이터를 정제하고 분할하여 본 데이터셋을 구축했습니다. 위키미디어의 원본 덤프 데이터를 다운로드하여 불필요한 마크업과 태그를 제거한 후, 자연어 문장을 기준으로 텍스트를 분할했습니다.

### **전처리 (Preprocessing)**

* **분할 단위 (Chunking Strategy):** 문장 (sentence)
* **세그먼트 크기 (Segment Size):** 10개 문장 (`--seg_size 10`)
* **스트라이드 (Stride):** 1개 문장 (`--stride 1`)

각 데이터 샘플은 10개의 연속된 문장으로 구성되며, 다음 샘플은 1개 문장씩 겹치도록 구성하여 문맥 정보의 손실을 최소화하고 데이터의 양을 증강했습니다.

## **데이터 구조 (Data Structure)**

### **데이터 필드 (Data Fields)**

* `text` (string): 전처리 과정을 거친 텍스트 데이터. 10개의 문장으로 구성된 하나의 문자열입니다.

## **사용 방법 (How to Use)**

```python
from datasets import load_dataset

dataset = load_dataset("Chang-Su/ko-wiki-250611")
print(dataset['train'][0])
````

## **라이선스 (License)**

원본 위키피디아 데이터는 국제 라이선스([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/))를 따릅니다. 본 데이터셋 또한 동일한 라이선스 정책을 준수합니다.

## **인용 정보 (Citation)**

본 데이터셋을 연구에 사용하실 경우, 다음과 같이 인용을 부탁드립니다.

```bibtex
@dataset{
  author = "ChangSu Choi",
  title = "ko-wiki-250611",
  year = "2025",
  url = "https://huggingface.co/datasets/Chang-Su/ko-wiki-250611"
}
```