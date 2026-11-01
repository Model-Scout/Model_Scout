---
type: "dataset"
id: "limmak/verified-step-claims-1k-preview"
source: "huggingface"
url: "https://huggingface.co/datasets/limmak/verified-step-claims-1k-preview"
downloads: 14
summary: "수학적 검증과 증거를 포함한 단계별 수학 주장 데이터로 프로세스 감독 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# limmak/verified-step-claims-1k-preview

> dataset · [Hugging Face](https://huggingface.co/datasets/limmak/verified-step-claims-1k-preview)

수학적 검증과 증거를 포함한 단계별 수학 주장 데이터로 프로세스 감독 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Direct `(step, verdict)` pairs for reward model training` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = ``fail` claims with counterexamples for training error-localization models` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `Full step text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``pass` or `fail`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `covering Korean CSAT (수능), national mock exams, and advanced textbook problems` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is a 1K preview sampled from a larger in-progress corpus` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `step_text` 열 p90 48자 ≈ 32 토큰 (viewer statistics, default/train)
