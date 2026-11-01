---
type: "dataset"
id: "nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1"
source: "huggingface"
url: "https://huggingface.co/datasets/nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1"
downloads: 24
summary: "한국어 대화 샘플 63개로 구성된 검수 통과 골든셋으로, 한국어 응답 톤과 구조 참고용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1

> dataset · [Hugging Face](https://huggingface.co/datasets/nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1)

한국어 대화 샘플 63개로 구성된 검수 통과 골든셋으로, 한국어 응답 톤과 구조 참고용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `한국어 대화 샘플 63개(JSONL)로 구성된 골든셋(검수 통과)입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `model_response : 응답 구성 요소` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `46` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `ds = load_dataset("nowsika/NOBLE_GoldenSet-KR_Verified-v3.2.1")
ds["train"][0]` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `scenario` 열 p90 69자 ≈ 46 토큰 (viewer statistics, default/train)
