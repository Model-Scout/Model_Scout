---
type: "dataset"
id: "Taegyuu/KoAlpaca_hira_v1.1a"
source: "huggingface"
url: "https://huggingface.co/datasets/Taegyuu/KoAlpaca_hira_v1.1a"
downloads: 26
summary: "KoAlpaca_hira_v1.1a는 한국어 질문-답변 데이터로 텍스트 생성에 활용됩니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Taegyuu/KoAlpaca_hira_v1.1a

> dataset · [Hugging Face](https://huggingface.co/datasets/Taegyuu/KoAlpaca_hira_v1.1a)

KoAlpaca_hira_v1.1a는 한국어 질문-답변 데이터로 텍스트 생성에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `features: ['instruction', 'input', 'output']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `features: ['instruction', 'input', 'output']` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `398` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `양파는 어떤 식물 부위인가요? 그리고 고구마는 뿌리인가요?` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `>>> ds = load_dataset("beomi/KoAlpaca-v1.1a", split="train")` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 598자 ≈ 398 토큰 (viewer statistics, default/train)
