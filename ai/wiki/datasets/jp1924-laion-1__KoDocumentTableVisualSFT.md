---
type: "dataset"
id: "jp1924-laion-1/KoDocumentTableVisualSFT"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/KoDocumentTableVisualSFT"
downloads: 10
summary: "ImageTextToTextPipeline 참고해 제작한 대화형 멀티모달 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[표 질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924-laion-1/KoDocumentTableVisualSFT

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/KoDocumentTableVisualSFT)

ImageTextToTextPipeline 참고해 제작한 대화형 멀티모달 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `ImageTextToTextPipeline을 참고해서 conversations를 제작했다.` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `ImageTextToTextPipeline` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:table_qa, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:table_qa, task:visual_qa = `ImageTextToTextPipeline을 참고해서 conversations를 제작했다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
