---
type: "dataset"
id: "joonhok-exo-ai/korean_law_open_data_precedents"
source: "huggingface"
url: "https://huggingface.co/datasets/joonhok-exo-ai/korean_law_open_data_precedents"
downloads: 494
summary: "국가법령정보센터의 대한민국 판례 171,599건을 수집한 법률 판례 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# joonhok-exo-ai/korean_law_open_data_precedents

> dataset · [Hugging Face](https://huggingface.co/datasets/joonhok-exo-ai/korean_law_open_data_precedents)

국가법령정보센터의 대한민국 판례 171,599건을 수집한 법률 판례 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `판례 본문 조회 API의 출력 필드를 대체로 따랐습니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `판례 본문 조회 API의 출력 필드를 대체로 따랐습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `판례 본문 조회 API의 출력 필드를 대체로 따랐습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `51879` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋을 만들게 되었습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `전문` 열 p90 77819자 ≈ 51879 토큰 (viewer statistics, default/train)
