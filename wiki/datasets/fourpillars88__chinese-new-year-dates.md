---
type: "dataset"
id: "fourpillars88/chinese-new-year-dates"
source: "huggingface"
url: "https://huggingface.co/datasets/fourpillars88/chinese-new-year-dates"
downloads: 61
summary: "1930년부터 2026년까지 중국 음력 설과 입춘 날짜, 띠와 오행 정보를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# fourpillars88/chinese-new-year-dates

> dataset · [Hugging Face](https://huggingface.co/datasets/fourpillars88/chinese-new-year-dates)

1930년부터 2026년까지 중국 음력 설과 입춘 날짜, 띠와 오행 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Use it to classify birth dates by Chinese zodiac correctly.` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:table_qa = `Columns | Column | Example | Meaning |` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:table_qa = `Columns | Column | Example | Meaning |` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `5` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Chinese New Year and Lichun dates, 1930–2026` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Source and online version: [Four Pillars](https://fourpillars88.com/chinese-new-year-dates)` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `nayin` 열 p90 21자 ≈ 5 토큰 (viewer statistics, default/train)
