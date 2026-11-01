---
type: "dataset"
id: "kifai/KoInFoBench"
source: "huggingface"
url: "https://huggingface.co/datasets/kifai/KoInFoBench"
downloads: 62
summary: "KoInFoBench는 한국어 지시문 수행 능력을 평가하는 LLM 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
# kifai/KoInFoBench

> dataset · [Hugging Face](https://huggingface.co/datasets/kifai/KoInFoBench)

KoInFoBench는 한국어 지시문 수행 능력을 평가하는 LLM 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KoInFoBench is a specialized evaluation dataset designed to assess the performance of Large Language Models (LLMs) on capabilities of Korean instructions follow` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Decomposed Requirements Following Ratio(DRFR) is the metric to evaluate how LLMs accurately respond to the instruction/input.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `144` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Inspired by InFoBench dataset, we extends their concpet by focusing on the nuances and features of Korean language.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `KoInFoBench is a specialized evaluation dataset designed to assess the performance of Large Language Models (LLMs) on capabilities of Korean instructions follow` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 216자 ≈ 144 토큰 (viewer statistics, default/train)
