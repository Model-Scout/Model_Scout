---
type: "dataset"
id: "gyung/toolllama-korean-function-calling"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/toolllama-korean-function-calling"
downloads: 60
summary: "ToolLLaMA 데이터셋을 한국어-영어 하이브리드로 변환한 함수 호출 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# gyung/toolllama-korean-function-calling

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/toolllama-korean-function-calling)

ToolLLaMA 데이터셋을 한국어-영어 하이브리드로 변환한 함수 호출 학습용 데이터셋입니다.

## 분류

- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `User 질문
한국어` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Action (함수명)
영어 (유지)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `9190` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Function Calling SFT 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 13785자 ≈ 9190 토큰 (viewer statistics, default/train)
