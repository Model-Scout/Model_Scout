---
type: "dataset"
id: "60base/korea-household-egocentric-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/60base/korea-household-egocentric-samples"
downloads: 262
summary: "60BASE의 한국 가정 내 일상 작업을 촬영한 에고센트릭 비디오 샘플 20개 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# 60base/korea-household-egocentric-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/60base/korea-household-egocentric-samples)

60BASE의 한국 가정 내 일상 작업을 촬영한 에고센트릭 비디오 샘플 20개 모음입니다.

## 분류

- **작업**: [[이미지 인식]] — ner · readme = `Egocentric, monocular RGB video` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `20 MP4 clips × 20 seconds; 6 minutes 40 seconds total` · 신뢰도 high
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `20 MP4 clips × 20 seconds; 6 minutes 40 seconds total` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `66` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These excerpts come from the twenty owner-provided recordings in the 60BASE Korea household sample collection.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 99자 ≈ 66 토큰 (viewer statistics, default/sample)
