---
type: "dataset"
id: "PrompTartLAB/PTT_en_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/PrompTartLAB/PTT_en_ko"
downloads: 93
summary: "기술 용어의 정확한 번역을 위한 영어-한국어 문장 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# PrompTartLAB/PTT_en_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/PrompTartLAB/PTT_en_ko)

기술 용어의 정확한 번역을 위한 영어-한국어 문장 쌍 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `evaluating and training models in translating technical terms while maintaining clarity and accuracy` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `English-Korean bilingual sentence pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Korean translation of the source sentence, with the English technical terms presented in parentheses.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `382` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `The primary dataset covers the artificial intelligence (AI) domain, with additional out-of-domain (OOD) datasets for physics and biology used for evaluation pur` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Validation | 144` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training | 1,116` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 573자 ≈ 382 토큰 (viewer statistics, default/validation)
