---
type: "dataset"
id: "yuneun92/admin-multiplechoice-100"
source: "huggingface"
url: "https://huggingface.co/datasets/yuneun92/admin-multiplechoice-100"
downloads: 13
summary: "AI Hub 행정 문서 기계독해 데이터셋으로 만든 100개 텍스트의 다지선다 질문-답변 데이터셋입니다."
readme_status: "thin"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# yuneun92/admin-multiplechoice-100

> dataset · [Hugging Face](https://huggingface.co/datasets/yuneun92/admin-multiplechoice-100)

AI Hub 행정 문서 기계독해 데이터셋으로 만든 100개 텍스트의 다지선다 질문-답변 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `질문 생성은 kullm3을, 답변 생성은 gpt 3.5 turbo API를 이용해 생성했습니다.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `행정 문서 기계독해 데이터셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `100개의 텍스트에 대해 각 텍스트마다 5개 이하의 질문-답변 쌍` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `질문-답변 쌍` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `379` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `행정 문서` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `100개의 텍스트에 대해 각 텍스트마다 5개 이하의 질문-답변 쌍을 만든 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 568자 ≈ 379 토큰 (viewer statistics, default/train)
