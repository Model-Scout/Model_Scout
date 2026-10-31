---
type: "dataset"
id: "youjunhyeok/Magpie-DPO-100K-SML-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/Magpie-DPO-100K-SML-ko"
downloads: 40
summary: "Magpie-Align/Magpie-DPO-100K-SML 데이터셋을 번역한 DPO 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# youjunhyeok/Magpie-DPO-100K-SML-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/Magpie-DPO-100K-SML-ko)

Magpie-Align/Magpie-DPO-100K-SML 데이터셋을 번역한 DPO 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `instruction-response pair` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `instruction-response pair` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3132` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is still under internal assessment.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `To create this dataset, we first generate responses from the base model using URIAL as rejected.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response_70b_instruct` 열 p90 4698자 ≈ 3132 토큰 (viewer statistics, default/train)
