---
type: "dataset"
id: "meaecosystem/pustaka"
source: "huggingface"
url: "https://huggingface.co/datasets/meaecosystem/pustaka"
downloads: 74434
summary: "Pustaka는 인도네시아어 중심의 대규모 공개 텍스트 코퍼스로, 언어 모델 사전학습 및 NLP 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# meaecosystem/pustaka

> dataset · [Hugging Face](https://huggingface.co/datasets/meaecosystem/pustaka)

Pustaka는 인도네시아어 중심의 대규모 공개 텍스트 코퍼스로, 언어 모델 사전학습 및 NLP 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — tag_match · tags = `language-modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Pustaka adalah korpus teks terbuka berskala besar yang dikembangkan oleh MEA Ecosystem, dimulai dengan fokus penuh pada Bahasa Indonesia.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6741` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 26964자 ≈ 6741 토큰 (viewer statistics, default/train)
