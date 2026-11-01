---
type: "dataset"
id: "nmixx-fin/twice_korfin-asc_sent_cls"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_korfin-asc_sent_cls"
downloads: 21
summary: "금융 보고서 텍스트의 감성 분류 데이터셋으로 긍정, 중립, 부정 감성 분류에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_korfin-asc_sent_cls

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_korfin-asc_sent_cls)

금융 보고서 텍스트의 감성 분류 데이터셋으로 긍정, 중립, 부정 감성 분류에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Sentiment classification of text in financial reports` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Sentiment classification of text in financial reports (POSITIVE / NEUTRAL / NEGATIVE).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `90` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 135자 ≈ 90 토큰 (viewer statistics, default/train)
