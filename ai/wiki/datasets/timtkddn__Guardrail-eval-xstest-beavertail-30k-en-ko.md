---
type: "dataset"
id: "timtkddn/Guardrail-eval-xstest-beavertail-30k-en-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/timtkddn/Guardrail-eval-xstest-beavertail-30k-en-ko"
downloads: 17
summary: "영어와 한국어로 된 XSTest와 BeaverTail 30K 평가용 데이터셋으로, 안전성 평가 및 다국어 비교에 사용됨."
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# timtkddn/Guardrail-eval-xstest-beavertail-30k-en-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/timtkddn/Guardrail-eval-xstest-beavertail-30k-en-ko)

영어와 한국어로 된 XSTest와 BeaverTail 30K 평가용 데이터셋으로, 안전성 평가 및 다국어 비교에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `These configs contain short prompts labeled as `safe` or `unsafe`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `prompt safety classification evaluation` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is organized for multilingual evaluation with English and Korean variants for each benchmark.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `All four configs are exported as `test` splits.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
