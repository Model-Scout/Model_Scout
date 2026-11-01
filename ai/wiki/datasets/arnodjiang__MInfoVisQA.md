---
type: "dataset"
id: "arnodjiang/MInfoVisQA"
source: "huggingface"
url: "https://huggingface.co/datasets/arnodjiang/MInfoVisQA"
downloads: 274
summary: "MInfoVisQA는 24개 언어로 된 시각 정보 질의응답 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# arnodjiang/MInfoVisQA

> dataset · [Hugging Face](https://huggingface.co/datasets/arnodjiang/MInfoVisQA)

MInfoVisQA는 24개 언어로 된 시각 정보 질의응답 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `MInfoVisQA: A Multilingual Benchmark for Information-Visual Question Answering` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `First apply deterministic answer matching. Non-matching predictions are judged for answer equivalence by a separately configured, text-only LLM judge.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Images are localized reconstructions of charts and rendered tables` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:reranking, task:visual_qa = `Only the question, image and optional source context are inference inputs.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Only the question, image and optional source context are inference inputs. Do not send answers, provenance or audit annotations to the model.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `45` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MInfoVisQA: A Multilingual Benchmark for Information-Visual Question Answering` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The single validation split is an evaluation split; no training split is provided.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 180자 ≈ 45 토큰 (viewer statistics, default/validation)
