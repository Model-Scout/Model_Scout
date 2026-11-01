---
type: "dataset"
id: "SamsungSDS-Research/Policy-on-the-Fly-Benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/SamsungSDS-Research/Policy-on-the-Fly-Benchmark"
downloads: 72
summary: "PoFBench는 LLM 기반 시스템의 정책 필터 성능을 평가하는 테스트 전용 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SamsungSDS-Research/Policy-on-the-Fly-Benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/SamsungSDS-Research/Policy-on-the-Fly-Benchmark)

PoFBench는 LLM 기반 시스템의 정책 필터 성능을 평가하는 테스트 전용 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each row represents a single evaluation sample, consisting of a prompt, a policy, and the expected verdict for that combination` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `300` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Existing AI safety benchmarks evaluate against fixed risk taxonomies predefined by experts` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `policy` 열 p90 450자 ≈ 300 토큰 (viewer statistics, pofbench_ko/test)
