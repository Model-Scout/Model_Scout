---
type: "dataset"
id: "davidkim205/ko_common_gen"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/ko_common_gen"
downloads: 32
summary: "뉴스 데이터를 이용해 제작한 common gen 데이터셋으로 문장 생성을 위한 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# davidkim205/ko_common_gen

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/ko_common_gen)

뉴스 데이터를 이용해 제작한 common gen 데이터셋으로 문장 생성을 위한 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `뉴스 데이터를 이용하여 제작한 common gen 데이터셋.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `"concept_set": "concept set: {해석이, 스마트워치, 이끈다는, 마이크, LED 시장 성장}"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `"ending0": "마이크로 스마트워치가 LED 시장 성장을 이끈다는 해석이다."` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `33` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `뉴스 데이터를 이용하여 제작한 common gen 데이터셋.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `뉴스 데이터를 이용하여 제작한 common gen 데이터셋. 총 4,639개.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `concept_set` 열 p90 49자 ≈ 33 토큰 (viewer statistics, default/test)
