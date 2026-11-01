---
type: "dataset"
id: "Chrisryugj/kordoc-ocr-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/Chrisryugj/kordoc-ocr-bench"
downloads: 139
summary: "한국 공공기관 PDF 문서의 쪽 이미지와 정답 텍스트로 구성된 OCR 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Chrisryugj/kordoc-ocr-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/Chrisryugj/kordoc-ocr-bench)

한국 공공기관 PDF 문서의 쪽 이미지와 정답 텍스트로 구성된 OCR 평가용 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality, task:ocr = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `이미지: 같은 쪽을 pdfium으로 216dpi(72dpi × 3) 렌더한 PNG입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `그 쪽의 정답 텍스트를 담았습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1750` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `한국 공공기관 PDF(보도자료·예산서·계획서·회의록·법령 서식 등)의 쪽 이미지와, 그 쪽의 정답 텍스트를 담았습니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `kordoc의 OCR 회귀 벤치(bench/ocr-accuracy.mjs)를 모델과 상관없이 돌릴 수 있게 옮긴 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `markdown` 열 p90 2625자 ≈ 1750 토큰 (viewer statistics, default/test)
