---
type: "dataset"
id: "ViewPulseAI/viewpulse-vpa-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/ViewPulseAI/viewpulse-vpa-sample"
downloads: 8
summary: "View Pulse AI(VPA) 멀티모달 미디어 행동 데이터셋으로 시청자 행동 예측에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ViewPulseAI/viewpulse-vpa-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/ViewPulseAI/viewpulse-vpa-sample)

View Pulse AI(VPA) 멀티모달 미디어 행동 데이터셋으로 시청자 행동 예측에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Reaction_Class (-1, 0, 1) for audience behavior categorization.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `This dataset bridges raw video content with real-time viewer engagement` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Reaction_Class (-1, 0, 1) for audience behavior categorization.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5902` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `View Pulse AI (VPA) is a proprietary multimodal dataset designed for predictive audience behavior analysis.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `Vision_i` 열 p90 8853자 ≈ 5902 토큰 (viewer statistics, default/train)
