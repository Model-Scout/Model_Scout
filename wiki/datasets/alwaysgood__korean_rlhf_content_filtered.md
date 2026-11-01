---
type: "dataset"
id: "alwaysgood/korean_rlhf_content_filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/alwaysgood/korean_rlhf_content_filtered"
downloads: 21
summary: "한국어 RLHF 데이터셋에서 필터링한 텍스트 콘텐츠로 언어 모델 사전학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alwaysgood/korean_rlhf_content_filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/alwaysgood/korean_rlhf_content_filtered)

한국어 RLHF 데이터셋에서 필터링한 텍스트 콘텐츠로 언어 모델 사전학습용 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Each row has a single content field suitable for LM pretraining/SFT-style text modeling.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Each row has a single content field suitable for LM pretraining/SFT-style text modeling.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each row has a single content field suitable for LM pretraining/SFT-style text modeling.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `590` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Korean language modeling pretraining
- Continued pretraining / domain adaptation
- SFT-style text-only preparation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 885자 ≈ 590 토큰 (viewer statistics, default/train)
