---
type: "dataset"
id: "moon1ite/kor_hate"
source: "huggingface"
url: "https://huggingface.co/datasets/moon1ite/kor_hate"
downloads: 330
summary: "한국 연예 뉴스 댓글에서 성별 편향, 사회적 편향, 혐오 발언을 탐지하기 위한 한국어 혐오 발언 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# moon1ite/kor_hate

> dataset · [Hugging Face](https://huggingface.co/datasets/moon1ite/kor_hate)

한국 연예 뉴스 댓글에서 성별 편향, 사회적 편향, 혐오 발언을 탐지하기 위한 한국어 혐오 발언 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `Human-annotated Korean corpus collected from a popular domestic entertainment news aggregation platform` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `The data is split into a training and development (test) set.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is split into a training and development (test) set.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
