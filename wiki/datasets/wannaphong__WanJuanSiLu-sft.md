---
type: "dataset"
id: "wannaphong/WanJuanSiLu-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/wannaphong/WanJuanSiLu-sft"
downloads: 86
summary: "아랍어, 러시아어, 한국어, 베트남어, 태국어의 문화 관련 질문-답변 쌍을 포함한 SFT 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[th]]"
  - "[[vi]]"
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
  - "[[중규모 데이터]]"
---
# wannaphong/WanJuanSiLu-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/wannaphong/WanJuanSiLu-sft)

아랍어, 러시아어, 한국어, 베트남어, 태국어의 문화 관련 질문-답변 쌍을 포함한 SFT 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `culturally relevant question-answer pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `culturally relevant question-answer pairs` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `322` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Provide a non-English cultural corpus (such as local life/traditional customs) to alleviate stereotypes dominated by English data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `180,000 SFT data` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1287자 ≈ 322 토큰 (viewer statistics, default/train)
