---
type: "dataset"
id: "mncai/KSPG-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/mncai/KSPG-Bench"
downloads: 197
summary: "한국어 서비스 정책 준수 평가 벤치마크로, 가드레일 모델의 정책별 허용·차단 판정을 평가합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mncai/KSPG-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/mncai/KSPG-Bench)

한국어 서비스 정책 준수 평가 벤치마크로, 가드레일 모델의 정책별 허용·차단 판정을 평가합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `사용자 질문 판정(input)과 챗봇 응답 판정(response)을 따로 평가합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `사용자 질문 판정(input)과 챗봇 응답 판정(response)을 따로 평가합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `실제 민원·챗봇 질문에 법령과 기관 업무를 바탕으로 쓴 합성 정책을 붙였고` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `평가 전용입니다. 학습·튜닝에 쓰지 말아 주세요.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
