---
type: "dataset"
id: "ByteDance/MTVQA"
source: "huggingface"
url: "https://huggingface.co/datasets/ByteDance/MTVQA"
downloads: 1160
summary: "9개 언어의 다국어 텍스트 장면에 대한 시각적 질의응답 데이터셋으로, 다국어 이미지 이해 향상에 활용됨."
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
  - "[[ar]]"
  - "[[de]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[th]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ByteDance/MTVQA

> dataset · [Hugging Face](https://huggingface.co/datasets/ByteDance/MTVQA)

9개 언어의 다국어 텍스트 장면에 대한 시각적 질의응답 데이터셋으로, 다국어 이미지 이해 향상에 활용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `The dataset is oriented toward visual question answering of multilingual text scenes in nine languages` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · tags, task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `The dataset is oriented toward visual question answering of multilingual text scenes` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `The question-answer pairs are labeled by native annotators following a series of rules` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `The question-answer pairs are labeled by native annotators following a series of rules` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `153` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is oriented toward visual question answering of multilingual text scenes in nine languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Test Images
250
250
250
250
250
250
116
250
250
2116` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train Images
580
1039
622
635
984
792
319
568
1139
6678` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `qa_pairs` 열 p90 611자 ≈ 153 토큰 (viewer statistics, default/test)
