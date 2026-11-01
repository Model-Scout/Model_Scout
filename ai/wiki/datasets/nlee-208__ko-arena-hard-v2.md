---
type: "dataset"
id: "nlee-208/ko-arena-hard-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nlee-208/ko-arena-hard-v2"
downloads: 36
summary: "LMSYS 스타일의 한국어 대결형 벤치마크 데이터셋으로, GPT-5-mini가 생성한 기준 답변과 GPT-4.1 심판 모델을 사용해 평가함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
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
# nlee-208/ko-arena-hard-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nlee-208/ko-arena-hard-v2)

LMSYS 스타일의 한국어 대결형 벤치마크 데이터셋으로, GPT-5-mini가 생성한 기준 답변과 GPT-4.1 심판 모델을 사용해 평가함.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `an LMSYS-style head-to-head benchmark where a strong judge model rates a candidate model's answer against a fixed baseline answer` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `491 prompts in Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `baseline_answer` | string | `gpt-5-mini`'s answer; the fixed B-side of every comparison` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4753` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `491 prompts in Korean, drawn from CohereLabs/m-ArenaHard-v2.0` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `the dataset works as a drop-in benchmark without any field remapping` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `baseline_answer` 열 p90 7130자 ≈ 4753 토큰 (viewer statistics, default/test)
