---
type: "dataset"
id: "jiyeony/event-sae-head-full10-results"
source: "huggingface"
url: "https://huggingface.co/datasets/jiyeony/event-sae-head-full10-results"
downloads: 171
summary: "LIBERO-Spatial 실험의 Event-SAE Head 완료 결과 데이터로, 3600회 실험 롤아웃과 평가 케이스를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[코드 (입력 형식)|코드]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[평가용]]"
---
# jiyeony/event-sae-head-full10-results

> dataset · [Hugging Face](https://huggingface.co/datasets/jiyeony/event-sae-head-full10-results)

LIBERO-Spatial 실험의 Event-SAE Head 완료 결과 데이터로, 3600회 실험 롤아웃과 평가 케이스를 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The reports contain the measured Head-KL/Event results and their scope.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Source public dense activations, full model weights, inherited TopK tensors and the SAE checkpoint` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Predictor comparison` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Read results immediately` · 신뢰도 low
- **입력 형식**: [[코드 (입력 형식)|코드]] — ner · readme = `The archive also contains the exact source at commit `8924a8d9b62edb16d261785cbc2124729017f2b1`` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:reranking, task:retrieval = `the complete generated `head-inputs/full10` metadata/input directory` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The reports contain the measured Head-KL/Event results and their scope.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `This public release preserves 3600 completed rollouts, 18 conditions, 200 paired evaluation cases and 16 ablated features.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `These are post-pilot follow-up results, not a fully held-out confirmatory study.` · 신뢰도 low
