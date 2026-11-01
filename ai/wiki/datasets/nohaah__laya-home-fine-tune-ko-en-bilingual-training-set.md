---
type: "dataset"
id: "nohaah/laya-home-fine-tune-ko-en-bilingual-training-set"
source: "huggingface"
url: "https://huggingface.co/datasets/nohaah/laya-home-fine-tune-ko-en-bilingual-training-set"
downloads: 37
summary: "영어와 한국어 스마트홈 명령어 데이터로 Gantry 음성비서 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nohaah/laya-home-fine-tune-ko-en-bilingual-training-set

> dataset · [Hugging Face](https://huggingface.co/datasets/nohaah/laya-home-fine-tune-ko-en-bilingual-training-set)

영어와 한국어 스마트홈 명령어 데이터로 Gantry 음성비서 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Synthetic smart-home commands in English and Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labelled with the action, room and door a home hub should choose` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `92` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic smart-home commands in English and Korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Used to fine-tune nohaah/laya-home-fine-tune-kr` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `state` 열 p90 139자 ≈ 92 토큰 (viewer statistics, default/train)
