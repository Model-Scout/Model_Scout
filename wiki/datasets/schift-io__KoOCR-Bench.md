---
type: "dataset"
id: "schift-io/KoOCR-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/schift-io/KoOCR-Bench"
downloads: 446
summary: "한국어 문서 OCR 및 문서 파싱 평가용 벤치마크 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# schift-io/KoOCR-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/schift-io/KoOCR-Bench)

한국어 문서 OCR 및 문서 파싱 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme, task:ocr = `한국어 문서 OCR·문서 파싱 벤치마크입니다.` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `글자, 표, 제목, 읽기 순서, 좌표를 함께 평가합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `2026학년도 대학수학능력시험` · 신뢰도 low
- **도메인**: [[행정·민원]] — ner · readme = `korea.kr 정책브리핑 첨부 (공공누리 제1유형)` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `평가 전용입니다. 학습에 쓰지 마세요.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 38자 ≈ 26 토큰 (viewer statistics, default/train)
