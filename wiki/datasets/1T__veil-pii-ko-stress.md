---
type: "dataset"
id: "1T/veil-pii-ko-stress"
source: "huggingface"
url: "https://huggingface.co/datasets/1T/veil-pii-ko-stress"
downloads: 122
summary: "한국어 PII 탐지 모델의 약점을 평가하기 위한 표기 변형 및 문서 길이별 평가셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 1T/veil-pii-ko-stress

> dataset · [Hugging Face](https://huggingface.co/datasets/1T/veil-pii-ko-stress)

한국어 PII 탐지 모델의 약점을 평가하기 위한 표기 변형 및 문서 길이별 평가셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 PII 탐지 모델이 어디서 무너지는지 보려고 만든 평가셋입니다.` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `512 토큰을 넘는 입력의 뒷부분이 통째로 버려지는 버그를 찾았습니다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `정답 스팬은 그대로 두고 표면형만 바꾼 뒤 오프셋을 다시 계산했습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `원문은 KDPII 이므로 그 데이터의 도메인(일상 대화)을 그대로 물려받습니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `한국어 PII 탐지 모델이 어디서 무너지는지 보려고 만든 평가셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
