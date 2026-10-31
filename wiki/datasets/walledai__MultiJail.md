---
type: "dataset"
id: "walledai/MultiJail"
source: "huggingface"
url: "https://huggingface.co/datasets/walledai/MultiJail"
downloads: 87
summary: "다국어 감옥 탈출 챌린지를 위한 LLM 안전성 연구 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# walledai/MultiJail

> dataset · [Hugging Face](https://huggingface.co/datasets/walledai/MultiJail)

다국어 감옥 탈출 챌린지를 위한 LLM 안전성 연구 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 low
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Our research investigates the safety challenges of LLMs in multilingual settings.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `To address the identified risks and vulnerabilities, we commit to open-sourcing the data used in our study.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 122자 ≈ 31 토큰 (viewer statistics, default/ar)

## 이 데이터로 학습한 모델

- [[Verm1ion__injection-sentry-xlmr|Verm1ion/injection-sentry-xlmr]]
