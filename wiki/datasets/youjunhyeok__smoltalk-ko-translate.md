---
type: "dataset"
id: "youjunhyeok/smoltalk-ko-translate"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/smoltalk-ko-translate"
downloads: 228
summary: "HuggingFaceTB/smoltalk 데이터셋을 한국어로 번역한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# youjunhyeok/smoltalk-ko-translate

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/smoltalk-ko-translate)

HuggingFaceTB/smoltalk 데이터셋을 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `nayohan/llama3-instrucTrans-enko-8b 모델을 사용해 번역했습니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `messages 중 4096 token 이 넘어가는 content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `번역했습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HuggingFaceTB/smoltalk 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `split/train 4205413 4162254` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `original_idx` 열 p90 10자 ≈ 7 토큰 (viewer statistics, merge/test)
