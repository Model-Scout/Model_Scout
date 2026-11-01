---
type: "dataset"
id: "kaggle/hyuksama1/north-korean-nuclear-research"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hyuksama1/north-korean-nuclear-research"
downloads: 101
summary: "북한 과학자들이 발표한 핵 관련 연구 논문 제목과 저자 정보를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hyuksama1/north-korean-nuclear-research

> dataset · [Kaggle](https://www.kaggle.com/datasets/hyuksama1/north-korean-nuclear-research)

북한 과학자들이 발표한 핵 관련 연구 논문 제목과 저자 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Information on nuclear-related studies published by North Korean scientists` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Information on nuclear-related studies published by North Korean scientists` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Information on titles and authors of the studies published between 1991 and 2017.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Information on titles and authors of the studies published between 1991 and 2017.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Information on nuclear-related studies published by North Korean scientists` · 신뢰도 low
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset covering titles and authors of studies on nuclear issues published by the Journal of Kim Il Sung University between 1991 and 2017.` · 신뢰도 low
