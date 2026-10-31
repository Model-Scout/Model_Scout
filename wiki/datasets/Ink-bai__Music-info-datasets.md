---
type: "dataset"
id: "Ink-bai/Music-info-datasets"
source: "huggingface"
url: "https://huggingface.co/datasets/Ink-bai/Music-info-datasets"
downloads: 97
summary: "노래 메타데이터, 가사, 댓글 의미, 오디오 특징 등을 포함한 음악 정보 데이터셋으로 음악 분석과 추천에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ink-bai/Music-info-datasets

> dataset · [Hugging Face](https://huggingface.co/datasets/Ink-bai/Music-info-datasets)

노래 메타데이터, 가사, 댓글 의미, 오디오 특징 등을 포함한 음악 정보 데이터셋으로 음악 분석과 추천에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `音乐推荐原型、召回或重排特征实验` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `适合用于个人音乐库分析、标签体系构建、音乐检索、推荐实验、歌词/评论语义分析和音乐信息检索原型` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `本地音频匹配、音频特征和 MERT 表征` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `数据以网易云音乐 song_id 作为统一主键` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:reranking, task:retrieval = `歌曲元数据、歌词、评论语义` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `歌词/评论语义分析` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `音乐检索、推荐实验` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `音乐信息数据集` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `适合用于个人音乐库分析、标签体系构建、音乐检索、推荐实验、歌词/评论语义分析和音乐信息检索原型` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
