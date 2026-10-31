---
type: "dataset"
id: "ducut91/Judgement-De-Identification-Result"
source: "huggingface"
url: "https://huggingface.co/datasets/ducut91/Judgement-De-Identification-Result"
downloads: 84
summary: "법원 판결문 개인정보 비식별 모델 성능 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
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
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ducut91/Judgement-De-Identification-Result

> dataset · [Hugging Face](https://huggingface.co/datasets/ducut91/Judgement-De-Identification-Result)

법원 판결문 개인정보 비식별 모델 성능 평가 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `법원 판결문 개인정보 비식별 성능` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `법원 판결문 개인정보 비식별 성능` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `정확도 재현율 F1 점수` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2132` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `법원 판결문 비식별 모델의 성능 결과입니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 3199자 ≈ 2132 토큰 (viewer statistics, default/train)
