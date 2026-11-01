---
type: "dataset"
id: "jaeyong2/RAG-COT-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/RAG-COT-Ko"
downloads: 23
summary: "HAERAE-HUB 한국어 웹텍스트와 합성 텍스트를 활용해 Qwen 모델로 COT 답변 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/RAG-COT-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/RAG-COT-Ko)

HAERAE-HUB 한국어 웹텍스트와 합성 텍스트를 활용해 Qwen 모델로 COT 답변 생성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to generate answer with COT.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `source dataset from HAERAE-HUB/KOREAN-WEBTEXT and HAERAE-HUB/KOREAN-SyntheticText-1.5B` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We used Qwen/Qwen2-72B-Instruct model to generate answer with COT.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3340` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `source dataset from HAERAE-HUB/KOREAN-WEBTEXT and HAERAE-HUB/KOREAN-SyntheticText-1.5B` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `source dataset from HAERAE-HUB/KOREAN-WEBTEXT and HAERAE-HUB/KOREAN-SyntheticText-1.5B` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 5010자 ≈ 3340 토큰 (viewer statistics, default/train)
