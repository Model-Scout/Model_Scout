---
type: "dataset"
id: "hwany79/google-open-images-hair-style-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hwany79/google-open-images-hair-style-dataset"
downloads: 96
summary: "Google Open Images V7에서 다양한 헤어 스타일 사람 이미지를 필터링한 컴퓨터 비전용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hwany79/google-open-images-hair-style-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hwany79/google-open-images-hair-style-dataset)

Google Open Images V7에서 다양한 헤어 스타일 사람 이미지를 필터링한 컴퓨터 비전용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `헤어 스타일 분류` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `사람 탐지` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · tags, task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `이미지` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `이미지 수준의 레이블` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `픽셀 단위 인스턴스 세그멘테이션 마스크` · 신뢰도 low
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `바운딩 박스 좌표` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `이미지 수준의 레이블` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `98` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `컴퓨터 비전 연구 및 응용` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `label` 열 p90 147자 ≈ 98 토큰 (viewer statistics, default/validation)
