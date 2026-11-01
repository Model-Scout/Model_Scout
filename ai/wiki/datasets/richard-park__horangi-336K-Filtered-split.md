---
type: "dataset"
id: "richard-park/horangi-336K-Filtered-split"
source: "huggingface"
url: "https://huggingface.co/datasets/richard-park/horangi-336K-Filtered-split"
downloads: 23
summary: "호랑이 리더 보드 점수 향상을 위한 대화 형식 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# richard-park/horangi-336K-Filtered-split

> dataset · [Hugging Face](https://huggingface.co/datasets/richard-park/horangi-336K-Filtered-split)

호랑이 리더 보드 점수 향상을 위한 대화 형식 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `axolotl 지원 format: alpaca, gpteacher (conversation format)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `axolotl 지원 format: alpaca, gpteacher (conversation format)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `axolotl 지원 format: alpaca, gpteacher (conversation format)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `454` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `quality_explanation` 열 p90 681자 ≈ 454 토큰 (viewer statistics, default/test)
