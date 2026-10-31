---
type: "dataset"
id: "davidstap/NTREX"
source: "huggingface"
url: "https://huggingface.co/datasets/davidstap/NTREX"
downloads: 1668
summary: "영어에서 128개 언어로 번역 평가용 뉴스 테스트 참조 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# davidstap/NTREX

> dataset · [Hugging Face](https://huggingface.co/datasets/davidstap/NTREX)

영어에서 128개 언어로 번역 평가용 뉴스 테스트 참조 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `News Test References for MT Evaluation from English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `News Test References for MT Evaluation from English into a total of 128 target languages.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `107 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `News Test References for MT Evaluation` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `News Test References for MT Evaluation` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 115자 ≈ 29 토큰 (viewer statistics, kor_Hang/test)
