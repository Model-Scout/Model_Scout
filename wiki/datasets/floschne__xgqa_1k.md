---
type: "dataset"
id: "floschne/xgqa_1k"
source: "huggingface"
url: "https://huggingface.co/datasets/floschne/xgqa_1k"
downloads: 134
summary: "xGQA 1K는 다국어 시각 질문응답 데이터셋 xGQA의 1천개 샘플 하위셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[bn]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[id]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# floschne/xgqa_1k

> dataset · [Hugging Face](https://huggingface.co/datasets/floschne/xgqa_1k)

xGQA 1K는 다국어 시각 질문응답 데이터셋 xGQA의 1천개 샘플 하위셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `xGQA: Cross-Lingual Visual Question Answering` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `all languages contain the same images and questions based on the `imageId` and `semanticStr`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Cross-Lingual Visual Question Answering` · 신뢰도 medium
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `xGQA dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This is a 1K subset of the few_shot-test split of the xGQA dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `full_answer` 열 p90 45자 ≈ 11 토큰 (viewer statistics, default/bn)
