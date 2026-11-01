---
type: "dataset"
id: "Yuyongkim/inconvenience-msds"
source: "huggingface"
url: "https://huggingface.co/datasets/Yuyongkim/inconvenience-msds"
downloads: 54
summary: "한국 점자 규정에 따른 화학물질 안전보건자료(MSDS)를 점자로 인코딩한 접근성 인프라 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Yuyongkim/inconvenience-msds

> dataset · [Hugging Face](https://huggingface.co/datasets/Yuyongkim/inconvenience-msds)

한국 점자 규정에 따른 화학물질 안전보건자료(MSDS)를 점자로 인코딩한 접근성 인프라 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Accessibility infrastructure for Korean chemical safety information.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:translation = `Korean chemical safety information.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `encoded as Korean braille following the 2017 한국 점자 규정 (Korean Braille Standards).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `Accessibility infrastructure for Korean chemical safety information.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `cas_no` 열 p90 10자 ≈ 7 토큰 (viewer statistics, default/train)
