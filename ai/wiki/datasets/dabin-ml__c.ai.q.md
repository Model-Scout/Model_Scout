---
type: "dataset"
id: "dabin-ml/c.ai.q"
source: "huggingface"
url: "https://huggingface.co/datasets/dabin-ml/c.ai.q"
downloads: 27
summary: "대한민국 세관·관세 행정 질의응답 사례를 정리한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dabin-ml/c.ai.q

> dataset · [Hugging Face](https://huggingface.co/datasets/dabin-ml/c.ai.q)

대한민국 세관·관세 행정 질의응답 사례를 정리한 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Input: 세관/관세 관련 질문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Response: 공식 답변/설명` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `422` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `대한민국 세관·관세 행정 질의응답 사례` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Split: train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 633자 ≈ 422 토큰 (viewer statistics, default/train)
