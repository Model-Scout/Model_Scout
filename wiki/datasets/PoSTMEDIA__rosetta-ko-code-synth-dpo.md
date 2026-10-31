---
type: "dataset"
id: "PoSTMEDIA/rosetta-ko-code-synth-dpo"
source: "huggingface"
url: "https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-dpo"
downloads: 8
summary: "한국어 코딩 문제와 실행 검증된 해답으로 구성된 Rosetta-KO 합성 데이터셋입니다."
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoSTMEDIA/rosetta-ko-code-synth-dpo

> dataset · [Hugging Face](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-dpo)

한국어 코딩 문제와 실행 검증된 해답으로 구성된 Rosetta-KO 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `preference pairs (`chosen`/`rejected`)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = ``prompt` (string) — the Korean question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``chosen` / `rejected` — assistant responses; `chosen` is the verified-correct / better-grounded answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean-native coding data — problems with solutions whose unit tests were actually executed and passed` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic data generated with the Qwen3.6-27B teacher model — part of the Rosetta-KO suite` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
