---
type: "dataset"
id: "junbrro/openarm-human-rlhnd-prq-fp48"
source: "huggingface"
url: "https://huggingface.co/datasets/junbrro/openarm-human-rlhnd-prq-fp48"
downloads: 60
summary: "OpenArm Human RLHND PRQ/FP48 데이터셋은 휴이원 WAM-v1 서브셋으로, 로봇 조작 관련 프레임과 라벨을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# junbrro/openarm-human-rlhnd-prq-fp48

> dataset · [Hugging Face](https://huggingface.co/datasets/junbrro/openarm-human-rlhnd-prq-fp48)

OpenArm Human RLHND PRQ/FP48 데이터셋은 휴이원 WAM-v1 서브셋으로, 로봇 조작 관련 프레임과 라벨을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The seven skill categories are PnP, PnP x 2, Open, Close, Pour, Move, and Flip.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Offline PRQ labels, FP48 targets, validity masks, freshly recomputed per-subset state/action statistics` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Each `frame_maps/*.jsonl` identifies exact reference RGB frames` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Each `frame_maps/*.jsonl` identifies exact reference RGB frames` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `prompt strings match that dataset's metadata` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Offline PRQ labels, FP48 targets, validity masks, freshly recomputed per-subset state/action statistics` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The default release is now exactly the 1,187 episodes in `/data/huiwon/data/openarm_wam_v1/human_as_openarm28/`.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `No new RLHND inference was performed for this subset release.` · 신뢰도 low
