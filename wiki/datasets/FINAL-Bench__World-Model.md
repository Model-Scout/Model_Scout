---
type: "dataset"
id: "FINAL-Bench/World-Model"
source: "huggingface"
url: "https://huggingface.co/datasets/FINAL-Bench/World-Model"
downloads: 630
summary: "WM Bench는 세계 최초의 월드 모델과 구현 AI의 인지 능력 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# FINAL-Bench/World-Model

> dataset · [Hugging Face](https://huggingface.co/datasets/FINAL-Bench/World-Model)

WM Bench는 세계 최초의 월드 모델과 구현 AI의 인지 능력 평가 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `WM Bench is the world's first benchmark for evaluating the cognitive capabilities of World Models and Embodied AI systems.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Any environment via JSON input` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `WM Bench measures something different: Does the model think correctly?` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WM Bench is the world's first benchmark for evaluating the cognitive capabilities of World Models and Embodied AI systems.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `WM Bench is the world's first benchmark for evaluating the cognitive capabilities of World Models and Embodied AI systems.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `name` 열 p90 41자 ≈ 27 토큰 (viewer statistics, default/train)
