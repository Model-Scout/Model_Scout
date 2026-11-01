---
type: "dataset"
id: "werty1248/WordNet-Ko-translate-examples-0.3"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/WordNet-Ko-translate-examples-0.3"
downloads: 17
summary: "WordNet에서 가져온 단어와 정의에 한국어 번역 및 예제를 추가한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/WordNet-Ko-translate-examples-0.3

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/WordNet-Ko-translate-examples-0.3)

WordNet에서 가져온 단어와 정의에 한국어 번역 및 예제를 추가한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `문장 추출 및 검증에는 gemini-2.5-pro-exp-03-25와 Qwen3-30B-A3B 모델이 사용되었습니다.` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `word_type, sample은 gemini-2.5-pro-exp-03-25를 이용하여 인공적으로 생성되었습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `word_type, sample은 gemini-2.5-pro-exp-03-25를 이용하여 인공적으로 생성되었습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `word_wiki: sentence_wiki 문장에서 해당 단어의 번역 결과입니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `77` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `ID, Word, POS, definition은 WordNet에서 가져왔습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `word_type, sample은 gemini-2.5-pro-exp-03-25를 이용하여 인공적으로 생성되었습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `definition` 열 p90 115자 ≈ 77 토큰 (viewer statistics, default/train)
