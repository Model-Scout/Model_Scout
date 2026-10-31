---
type: "dataset"
id: "iontail/KoSum"
source: "huggingface"
url: "https://huggingface.co/datasets/iontail/KoSum"
downloads: 125
summary: "KoSum은 700개의 한국어 유튜브 영상으로 구성된 멀티모달 영상 요약 및 하이라이트 검출 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[요약]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# iontail/KoSum

> dataset · [Hugging Face](https://huggingface.co/datasets/iontail/KoSum)

KoSum은 700개의 한국어 유튜브 영상으로 구성된 멀티모달 영상 요약 및 하이라이트 검출 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `KoSum provides per-second visual, audio, and text features aligned with YouTube Most-Replayed importance scores.` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `highlight detection` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, tags, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `KoSum provides per-second visual, audio, and text features aligned with YouTube Most-Replayed importance scores.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:reranking, task:summarization = `KoSum provides per-second visual, audio, and text features aligned with YouTube Most-Replayed importance scores.` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `KoSum provides per-second visual, audio, and text features aligned with YouTube Most-Replayed importance scores.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoSum is a Korean YouTube benchmark for video summarization and highlight detection.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains metadata, multimodal features, ground-truth annotations, and standardized train/validation/test splits.` · 신뢰도 medium
