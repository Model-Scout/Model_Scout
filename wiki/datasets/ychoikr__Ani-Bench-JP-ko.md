---
type: "dataset"
id: "ychoikr/Ani-Bench-JP-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ychoikr/Ani-Bench-JP-ko"
downloads: 12
summary: "일본 인기 애니메이션 5작품 관련 한국어 퀴즈 100문제로 LLM 이해도 평가용 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ychoikr/Ani-Bench-JP-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ychoikr/Ani-Bench-JP-ko)

일본 인기 애니메이션 5작품 관련 한국어 퀴즈 100문제로 LLM 이해도 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `퀴즈 형식 문제로 구성되어 있습니다` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `문제: 애니메이션 관련 퀴즈 질문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `답변: 해당 질문에 대한 정답` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `일본의 인기 애니메이션에 관한 지식을 측정하기 위한 Ani-Bench-JP의 한국어 버전 벤치마크 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `test 스플릿으로 업로드되어 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `문제` 열 p90 48자 ≈ 32 토큰 (viewer statistics, default/test)
