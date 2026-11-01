---
type: "dataset"
id: "werty1248/Magpie-Ko-Qwen2.5-Reasoning-2k-example"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Magpie-Ko-Qwen2.5-Reasoning-2k-example"
downloads: 14
summary: "Magpie-Ko-Qwen2.5-Reasoning-2k-example은 한자/영어 필터링과 문제 난이도 확인용 테스트 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# werty1248/Magpie-Ko-Qwen2.5-Reasoning-2k-example

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Magpie-Ko-Qwen2.5-Reasoning-2k-example)

Magpie-Ko-Qwen2.5-Reasoning-2k-example은 한자/영어 필터링과 문제 난이도 확인용 테스트 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `instruction에 대한 BGE-m3 embedding + T-SNE` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `샘플 데이터 생성 ✅` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `instruction에 대한 BGE-m3 embedding + T-SNE` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `답변에도 한자/영어 필터링 적용해야 함` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1319` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `데이터 확인 및 테스트용` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 1979자 ≈ 1319 토큰 (viewer statistics, default/train)
