---
type: "dataset"
id: "okawaritsuika/nai-shared-styles"
source: "huggingface"
url: "https://huggingface.co/datasets/okawaritsuika/nai-shared-styles"
downloads: 262
summary: "아카라이브 AI 그림 채널의 그림체 공유 게시글에서 수집한 예제 이미지와 NovelAI 생성 메타데이터 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
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
# okawaritsuika/nai-shared-styles

> dataset · [Hugging Face](https://huggingface.co/datasets/okawaritsuika/nai-shared-styles)

아카라이브 AI 그림 채널의 그림체 공유 게시글에서 수집한 예제 이미지와 NovelAI 생성 메타데이터 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `V4.5·V5 그림체를 탐색하고 원본 게시글, 프롬프트와 생성 설정을 함께 확인하기 위한 자료입니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `품질 90 WebP 이미지와 연결·무결성 검증용 manifest.json.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `게시글 출처, 이미지별 프롬프트·네거티브·모델·생성 설정을 담은 메타데이터 전용 SQLite DB.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `품질 90 WebP 이미지와 연결·무결성 검증용 manifest.json.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `아카라이브 AI 그림 채널의 그림체 공유 게시글에서 수집한 예제 이미지와 NovelAI 생성 메타데이터입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이번 배포의 시드와 다운로드 정보가 반영된 NAImakeArtistGroup에서 공유 그림체 수집 → Hugging… See the full description on the dataset page` · 신뢰도 low
