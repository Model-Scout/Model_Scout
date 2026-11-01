---
type: "dataset"
id: "iNLP-Lab/multilingual-lima"
source: "huggingface"
url: "https://huggingface.co/datasets/iNLP-Lab/multilingual-lima"
downloads: 55
summary: "LIMA 데이터셋의 영어 프롬프트-응답 쌍을 9개 언어로 번역한 다국어 명령어 튜닝 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[영어]]"
  - "[[it]]"
  - "[[jv]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# iNLP-Lab/multilingual-lima

> dataset · [Hugging Face](https://huggingface.co/datasets/iNLP-Lab/multilingual-lima)

LIMA 데이터셋의 영어 프롬프트-응답 쌍을 9개 언어로 번역한 다국어 명령어 튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `prompt User instruction (translated; en is the original).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `output Assistant response (translated; en is the original).` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[jv]] — metadata · languages = `jv` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `831` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual extension of the LIMA instruction-tuning dataset.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 3322자 ≈ 831 토큰 (viewer statistics, ko/train)
