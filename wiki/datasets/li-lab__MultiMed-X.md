---
type: "dataset"
id: "li-lab/MultiMed-X"
source: "huggingface"
url: "https://huggingface.co/datasets/li-lab/MultiMed-X"
downloads: 156
summary: "MultiMed-X는 비영어권 의료 환경에서 다국어 의료 추론 평가를 위한 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[th]]"
  - "[[yo]]"
  - "[[중국어]]"
  - "[[zu]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# li-lab/MultiMed-X

> dataset · [Hugging Face](https://huggingface.co/datasets/li-lab/MultiMed-X)

MultiMed-X는 비영어권 의료 환경에서 다국어 의료 추론 평가를 위한 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `medical natural language inference (NLI)` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `medical reasoning evaluation across natural language inference (NLI) and open-ended question answering (QA)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Gold label (NLI only)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[yo]] — metadata · languages = `yo` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **언어**: [[zu]] — metadata · languages = `zu` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `433` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual benchmark` · 신뢰도 low
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `MultiMed-X is a multilingual benchmark for medical reasoning evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1734자 ≈ 433 토큰 (viewer statistics, default/en)
