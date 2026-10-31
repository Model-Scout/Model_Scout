---
type: "dataset"
id: "pulse-ai/PulseBench-Tab"
source: "huggingface"
url: "https://huggingface.co/datasets/pulse-ai/PulseBench-Tab"
downloads: 187
summary: "PulseBench-Tab은 9개 언어 문서 이미지에서 표 추출을 위한 다국어 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[표 질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pulse-ai/PulseBench-Tab

> dataset · [Hugging Face](https://huggingface.co/datasets/pulse-ai/PulseBench-Tab)

PulseBench-Tab은 9개 언어 문서 이미지에서 표 추출을 위한 다국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `A frontier multilingual benchmark for table extraction from document images.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — metadata · tags, task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Each sample is a table image paired with a ground truth HTML table` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction, task:table_qa, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:table_qa, task:visual_qa = `ground truth HTML table that preserves full structural markup` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A frontier multilingual benchmark for table extraction from document images.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `We evaluated 9 providers on all 1,820 samples using T-LAG.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `table_stats` 열 p90 72자 ≈ 18 토큰 (viewer statistics, default/train)
