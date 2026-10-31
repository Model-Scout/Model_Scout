---
language: ko
license: other
tags:
- autonomous-driving
- legal
- rag
- notebooklm
- qwen
- finetuning
- alpaca
pretty_name: "KR Self-Driving Legal QA"
size_categories:
- 1K<n<10K
---

# 📚 KR-Self-Driving-Legal-QA
**대한민국 자율주행자동차 법령 및 가이드라인 기반 Q&A 데이터셋**

이 데이터셋은 한국의 자율주행자동차 관련 법령, 규칙, 가이드라인(총 13개 핵심 문서)을 기반으로 생성된 고품질 질의응답(Q&A) 데이터셋입니다.
**LLM Fine-Tuning** 및 **RAG(Retrieval-Augmented Generation)** 시스템 구축을 위해 최적화되었습니다.

## 📌 데이터셋 개요 (Overview)

- **출처:** 대한민국 법령정보센터, 국토교통부 (공식 문서)
- **생성 도구:** Google NotebookLM + Custom Python Parser
- **포맷:** Alpaca Clean Format (`instruction`, `input`, `output`)
- **규모:** 720개 Q&A 쌍 (엄선된 고품질 데이터)
- **특징:**
  - **법적 근거 명시:** 각 질문에 출처 문서(예: 레벨3 안전기준, 사이버보안 가이드라인)가 명시됨.
  - **RAG 최적화:** 불필요한 긴 법령 원문(Context)을 제거하여 LLM이 **"정답 생성 패턴"**만 학습하도록 설계됨. (실제 법령 내용은 외부 검색으로 주입 권장)

---

## 🏗️ 데이터 생성 파이프라인 (Creation Pipeline)

이 데이터셋은 다음과 같은 체계적인 과정을 거쳐 생성되었습니다.

### 1. 원천 데이터 수집 (Source Collection)
- **주요 출처 (Primary Source):** 법제처 및 국토교통부 (공식 법령/지침 원문)
- **보조 출처 (Secondary Source):** [찾기쉬운 생활법령정보 (자율주행자동차)](https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1593&ccfNo=1&cciNo=1&cnpClsNo=1) - 법령의 이해를 돕기 위한 해설 자료
- **대상 목록 (Target Documents):**
  1. 부분 자율주행시스템(레벨 3) 안전기준
  2. 조건부 완전자율주행시스템(레벨 4) 안전지침
  3. 자율주행자동차 사이버보안 확보 가이드라인
  4. 자율주행자동차 윤리 가이드라인
  5. 자율주행자동차 임시운행허가 가이드라인
  6. 자율주행자동차 운행구간 및 시범운행지구 지정
  7. (기타 7건)

### 2. Q&A 생성 (Q&A Generation with NotebookLM)
- **도구:** Google NotebookLM
- **방법:** 각 법령 문서를 업로드하고, *"이 법령에 대해 실무자가 궁금해할 만한 핵심 질문과 답변 100개를 생성해줘.(법령별로 반복 실행)"*라는 프롬프트를 사용하여 초안을 생성했습니다.
- **결과:** 법령별로 30~80개 내외의 고품질 Q&A 텍스트 파일 13개 확보.
- **검증:** 생성된 Q&A의 정확성을 법령 원문과 비교 검토하였습니다.

### 3. 데이터 파싱 및 정제 (Parsing & Cleaning)
- **스크립트:** `create_clean_alpaca.py` (포함됨)
- **과정:**
  1. NotebookLM 출력 텍스트(`raw_data/*.txt`)를 정규식으로 파싱하여 Q&A 쌍 추출.
  2. 출처 정보(`[출처: 문서명]`)를 Input 필드에 자동 삽입.
  3. 불필요한 중복 텍스트(긴 Context) 제거 -> **Clean Dataset** 확보.
  4. Alpaca JSON 포맷으로 변환.

---

## 📂 파일 구조 (File Structure)

```
/
├── dataset_alpaca_clean.json  # [메인] 파인튜닝용 정제 데이터셋 (Alpaca Format)
│
├── raw_data/                  # [원본] NotebookLM 생성 Q&A 텍스트
│   ├── 레벨3_안전기준.txt
│   ├── 레벨4_안전지침.txt
│   └── ... (총 13개)
│
├── docs/                      # [참고] 법령 원문 파일 (PDF/DOC)
│   ├── 레벨3_안전기준.pdf
│   └── ...
│
└── code/                      # [도구] 데이터 생성 및 처리 스크립트
    ├── create_clean_alpaca.py # 텍스트 -> Alpaca JSON 변환 스크립트
    ├── analyze_dataset.py     # 데이터 통계 분석 스크립트
    └── ...
```

---

## 🚀 활용 예시 (Usage)

### 1. LLM Fine-Tuning (with unsloth / huggingface)
이 데이터셋을 사용하여 `Llama`, `Qwen`, `Gemma` 등 한국어 가능한 LLM을 "자율주행 법률 전문가"로 튜닝할 수 있습니다.

```python
from datasets import load_dataset

dataset = load_dataset("bluejude10/KR-Self-Driving-Legal-QA", split="train")
print(dataset[0])
# {'instruction': '...', 'input': '레벨3란 무엇인가요?\n[출처: 레벨3 안전기준]', 'output': '...'}
```

### 2. RAG System Evaluation
RAG 시스템의 **Retrieval(검색)** 성능이나 **Generation(생성)** 정확도를 평가하는 벤치마크 데이터셋으로 활용할 수 있습니다.

---

## ⚠️ 라이선스 및 주의사항 (License & Disclaimer)

- **라이선스:** Apache 2.0
- **주의사항:** 본 데이터셋은 법적 효력이 없으며, 실제 법적 자문은 변호사와 상의해야 합니다. 데이터는 2026년 2월 기준 법령을 반영하고 있습니다.
- **기여:** 본 데이터셋은 `bluejude10`에 의해 생성 및 공개되었습니다.

---

**Created Date:** 2026-02-14
