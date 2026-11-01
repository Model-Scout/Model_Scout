---
type: "dataset"
id: "Elda-AI/elda-coref-ko-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Elda-AI/elda-coref-ko-v2"
downloads: 31
summary: "CorefUD Korean-ECMT를 학습 형식으로 변환한 한국어 조응 코어퍼런스 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
# Elda-AI/elda-coref-ko-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Elda-AI/elda-coref-ko-v2)

CorefUD Korean-ECMT를 학습 형식으로 변환한 한국어 조응 코어퍼런스 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `우리 학습 형식(턴 · 멘션 · 선행사)으로 옮긴 것입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:language_modeling = `한 줄 = 한 문서. `turns[]` 안에 `words` · `items`(멘션) · `gold`(`ref_to: {turn,item} | null`) · `cands`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = ``gold`(`ref_to: {turn,item} | null`)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CorefUD Korean-ECMT` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train.jsonl 1,204문서 · dev.jsonl 133문서.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
