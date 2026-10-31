---
type: "dataset"
id: "florapeterpaul3/geeklink-ocr-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/florapeterpaul3/geeklink-ocr-benchmark"
downloads: 242
summary: "비디오 자막 OCR 성능 평가용 6개 언어 자막 이미지 1,140개 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[el]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# florapeterpaul3/geeklink-ocr-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/florapeterpaul3/geeklink-ocr-benchmark)

비디오 자막 OCR 성능 평가용 6개 언어 자막 이미지 1,140개 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Metrics are CER (character error rate) and WER (word error rate), broken down by language and by whether the sample has a watermark.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:visual_qa = `1,140 subtitle images across 6 languages` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:visual_qa = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — metadata · modality = `video` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `Metrics are CER (character error rate) and WER (word error rate)` · 신뢰도 medium
- **언어**: [[el]] — metadata · languages = `el` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This dataset is an open benchmark we use to evaluate our own OCR model against other engines` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
