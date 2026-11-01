---
type: "dataset"
id: "rucipheryn/KB-sLLM-QA-Dataset-Final-Split"
source: "huggingface"
url: "https://huggingface.co/datasets/rucipheryn/KB-sLLM-QA-Dataset-Final-Split"
downloads: 20
summary: "KB금융그룹 금융 도메인 특화 소형 언어 모델 개발용 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# rucipheryn/KB-sLLM-QA-Dataset-Final-Split

> dataset · [Hugging Face](https://huggingface.co/datasets/rucipheryn/KB-sLLM-QA-Dataset-Final-Split)

KB금융그룹 금융 도메인 특화 소형 언어 모델 개발용 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `질의응답(Q&A) 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `각 질문은 금융 고객이나 내부 직원이 가질 법한 구체적인 질문으로 구성되었으며` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `답변은 오직 제공된 PDF 문서 내용에만 근거하여 생성되었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `139` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `KB금융그룹의 페르소나를 가진 금융 도메인 특화 소형 언어 모델(sLLM) 개발` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `평가용 (Test): 150` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습용 (Train): 1,007` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer_B` 열 p90 208자 ≈ 139 토큰 (viewer statistics, default/test)
