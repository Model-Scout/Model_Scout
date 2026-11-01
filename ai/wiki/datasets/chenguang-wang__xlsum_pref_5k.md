---
type: "dataset"
id: "chenguang-wang/xlsum_pref_5k"
source: "huggingface"
url: "https://huggingface.co/datasets/chenguang-wang/xlsum_pref_5k"
downloads: 37
summary: "xlsum 원본 데이터 기반으로 요약 선호도를 주석한 테스트용 선호도 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# chenguang-wang/xlsum_pref_5k

> dataset · [Hugging Face](https://huggingface.co/datasets/chenguang-wang/xlsum_pref_5k)

xlsum 원본 데이터 기반으로 요약 선호도를 주석한 테스트용 선호도 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `chenguang-wang/Qwen2.5-3B-Instruct-summary-sft-adapter is used to generate completion` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `This is a Preference dataset compatible with TRL DPO training.` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking, task:summarization = `Based on the addition of System Prompt and User Prompt Prefix` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `used together with the summary field in the source dataset to annotate the preference.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The original data comes from csebuetnlp/xlsum.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is not guaranteed to be of high quality and is only used for testing, learning and communication.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
