---
type: "dataset"
id: "fdemelo/vox-communis-parallel-g2p"
source: "huggingface"
url: "https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p"
downloads: 223
summary: "VoxCommunis 코퍼스에서 파생된 음성-음소 병렬 데이터로 G2P 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# fdemelo/vox-communis-parallel-g2p

> dataset · [Hugging Face](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)

VoxCommunis 코퍼스에서 파생된 음성-음소 병렬 데이터로 G2P 모델 학습에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `to ease the training of grapheme-to-phoneme (G2P) models` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding = `pairs of utterances along with their corresponding phonemes` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `pairs of utterances along with their corresponding phonemes` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `56 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `derived from the VoxCommunis Corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `to ease the training of grapheme-to-phoneme (G2P) models` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
