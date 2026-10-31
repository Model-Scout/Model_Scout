---
type: "dataset"
id: "yangwang825/klue-ynat"
source: "huggingface"
url: "https://huggingface.co/datasets/yangwang825/klue-ynat"
downloads: 33
summary: "KLUE-YNAT은 한국어 뉴스 텍스트 분류를 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yangwang825/klue-ynat

> dataset · [Hugging Face](https://huggingface.co/datasets/yangwang825/klue-ynat)

KLUE-YNAT은 한국어 뉴스 텍스트 분류를 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `features:
- name: text
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: label
dtype:
class_label:` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `'0': IT과학
'1': 경제
'2': 사회
'3': 생활문화
'4': 세계
'5': 스포츠
'6': 정치` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 34자 ≈ 22 토큰 (viewer statistics, default/validation)
