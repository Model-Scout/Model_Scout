---
type: "dataset"
id: "ChuGyouk/Ko-MTS-Dialog"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/Ko-MTS-Dialog"
downloads: 31
summary: "Ko-MTS-Dialog는 1.7천건의 의사-환자 대화와 요약문을 포함한 한국어 번역 의료 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ChuGyouk/Ko-MTS-Dialog

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/Ko-MTS-Dialog)

Ko-MTS-Dialog는 1.7천건의 의사-환자 대화와 요약문을 포함한 한국어 번역 의료 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[요약]] — ner · readme = `MTS-Dialog dataset is a collection of 1.7k short doctor-patient conversations and corresponding summaries.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `doctor-patient conversations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `corresponding summaries` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1025` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `dialogue` 열 p90 1537자 ≈ 1025 토큰 (viewer statistics, default/train)
