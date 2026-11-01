---
type: "dataset"
id: "lawcompany/KLAID"
source: "huggingface"
url: "https://huggingface.co/datasets/lawcompany/KLAID"
downloads: 48
summary: "한국 법률 인공지능 기술 개발을 위한 법률 판결 예측 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lawcompany/KLAID

> dataset · [Hugging Face](https://huggingface.co/datasets/lawcompany/KLAID)

한국 법률 인공지능 기술 개발을 위한 법률 판결 예측 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `+ "fact": a `string` feature` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `+ "laws_service_id": a classification label, with 177 legal judgment values` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `642` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `Korean Legal Artificial Intelligence Datasets(KLAID) is a dataset for the development of Korean legal artificial intelligence technology.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `An example of 'train' looks as follows.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `fact` 열 p90 963자 ≈ 642 토큰 (viewer statistics, ljp/train)
