
---
license: other
language:
- ko
---

# Dataset Card for KB-sLLM-QA-Dataset-Final-Split

## Dataset Summary

이 데이터셋은 **KB금융그룹의 페르소나를 가진 금융 도메인 특화 소형 언어 모델(sLLM) 개발**을 위해 제작된 질의응답(Q&A) 데이터셋입니다.

KB금융그룹의 공개된 233개의 PDF 문서를 기반으로, OpenAI의 GPT-4o-mini 모델을 활용하여 1,157개의 Q&A 쌍을 생성했습니다.

각 질문은 금융 고객이나 내부 직원이 가질 법한 구체적인 질문으로 구성되었으며, 답변은 **오직 제공된 PDF 문서 내용에만 근거**하여 생성되었습니다.

이 데이터셋은 모델이 KB금융그룹에 특화된 지식을 얼마나 잘 학습했는지 객관적으로 평가하기 위한 테스트셋(test set)을 포함하고 있습니다.

- **총 데이터 수:** 1,157
- **학습용 (Train):** 1,007
- **평가용 (Test):** 150
- **언어:** 한국어 (Korean)

## How to Get Started

`datasets` 라이브러리를 사용하여 쉽게 데이터셋을 로드할 수 있습니다.

```python
from datasets import load_dataset

# 전체 데이터셋 로드 (train/test 포함)
dataset = load_dataset("rucipheryn/KB-sLLM-QA-Dataset-Final-Split")

# 학습용 데이터셋
train_dataset = dataset['train']

# 평가용 데이터셋
test_dataset = dataset['test']

print(train_dataset)
```

Dataset Structure

데이터셋은 다음과 같은 3개의 컬럼으로 구성됩니다.

question (string): 사용자의 질문입니다.

answer_B (string): source_pdf 문서 내용에 근거한 답변입니다.

source_pdf (string): 질문과 답변의 출처가 된 원본 PDF 파일의 이름입니다.

Data Instances

아래는 데이터셋의 한 가지 예시입니다.

```python
{
  "question": "CD수익률의 정의와 그 용도는 무엇인가요?",
  "answer_B": "CD수익률이란 신용평가회사로부터 AAA이상의 신용등급을 받은 시중은행이 발행한 만기가 91일인 CD의 발행수익률로서, 기초자료제출기관이 금융투자협회에 제출한 기초수익률을 기반으로 협회가 산출한 수익률을 말합니다. CD수익률은 금융계약·거래에서 해당 계약·거래의 상대방에게 지급·교환하고자 하는 금액 또는 금융상품의 가치를 결정할 때 기준으로 사용됩니다.",
  "source_pdf": "KB_CD수익률표준설명서(가계).pdf"
}
```

Source Data

원본 데이터 출처: sumilee/SKN14-Final-3Team-Data2

문서 종류: KB금융그룹 관련 상품 설명서, 정책, 약관 등 233개의 PDF 파일

Generation Process

텍스트 추출: PyMuPDF 라이브러리를 사용하여 각 PDF 문서에서 텍스트를 추출했습니다.

청킹 (Chunking): 긴 텍스트는 tiktoken을 기준으로 chunk_size=2000, overlap=200으로 설정하여 의미 있는 여러 조각으로 분할했습니다.

Q&A 생성: 각 텍스트 조각을 OpenAI의 gpt-4o-mini 모델에 입력하여, "문서 내용에만 근거한 전문적인 Q&A 쌍"을 생성하도록 요청했습니다.

결과물은 JSON 형식으로 받았습니다.

후처리 및 검증:

생성된 Q&A 쌍을 파싱하여 question, answer_B 컬럼으로 정리했습니다.

임시로 부여했던 pdf_0_... 형식의 파일명을 원본 데이터셋의 실제 PDF 파일명과 매핑하여 source_pdf 컬럼을 업데이트했습니다.

데이터 분할: 최종 1,157개의 데이터를 train_test_split을 사용하여 훈련셋(1,007개)과 테스트셋(150개)으로 분할했습니다.

Intended Uses & Limitations

주요 사용 목적: KB금융 특화 sLLM의 파인튜닝 후, 모델이 도메인 지식을 얼마나 정확하고 충실하게(faithfully) 답변하는지 평가하는 용도.

제한 사항: 이 데이터셋의 답변은 2025년 특정 시점의 PDF 문서를 기반으로 하므로, 최신 금융 정보나 정책을 반영하지 않을 수 있습니다.

또한, 생성 모델의 한계로 인해 미세한 오류가 포함될 수 있습니다.

Citation

이 데이터셋을 연구나 프로젝트에 사용하신다면 아래와 같이 인용을 부탁드립니다.
```python
@misc{kb_sllm_qa_2024,
  author = {rucipheryn},
  title = {KB-sLLM-QA-Dataset-Final-Split: A Korean Q&A Dataset for KB Financial Group Domain},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/datasets/your-username/KB-sLLM-QA-Dataset-Final-Split}}
}
```