---
type: "dataset"
id: "augustine223/korean-imatrix-calibration-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/augustine223/korean-imatrix-calibration-corpus"
downloads: 59
summary: "한국어 중심 imatrix 보정 코퍼스로, 한국어 토큰 분포 양자화 손실 보정에 사용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# augustine223/korean-imatrix-calibration-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/augustine223/korean-imatrix-calibration-corpus)

한국어 중심 imatrix 보정 코퍼스로, 한국어 토큰 분포 양자화 손실 보정에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `importance matrix는 거의 전부 영어 위주 코퍼스로 수집됩니다. 그 결과 한국어 토큰 분포에서의 양자화 손실이 체계적으로 커집니다.` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `한국어 중심 imatrix 보정 코퍼스의 첫 공개 릴리스` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `한국어 중심 imatrix 보정 코퍼스의 첫 공개 릴리스` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `332` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 중심 imatrix 보정 코퍼스의 첫 공개 릴리스` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 그 공백을 메우기 위해 만들어졌고, 실측으로 효과가 입증됐습니다.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 497자 ≈ 332 토큰 (viewer statistics, default/test)
