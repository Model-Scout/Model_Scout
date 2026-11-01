---
type: "dataset"
id: "heegyu/OIG-small-chip2-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko"
downloads: 64
summary: "OIG-small-chip2-ko는 OIG-small-chip2 데이터셋을 한국어로 번역한 대화형 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# heegyu/OIG-small-chip2-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko)

OIG-small-chip2-ko는 OIG-small-chip2 데이터셋을 한국어로 번역한 대화형 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `example
{
 "user": "Is there a good way to clean up my credit report?\n\n",
 "chip2": "That depends on why your credit score is low. Would you like to share mor` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `"user": "Is there a good way to clean up my credit report?\n\n"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `"chip2": "That depends on why your credit score is low. Would you like to share more details about your situation?"` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `356` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `210282 items` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chip2` 열 p90 534자 ≈ 356 토큰 (viewer statistics, default/train)
