---
type: "dataset"
id: "heegyu/korquad-chat-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/heegyu/korquad-chat-v1"
downloads: 53
summary: "KorQuAD 1.0 문서를 기반으로 ChatGPT가 생성한 9619개 한국어 지식기반 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# heegyu/korquad-chat-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/heegyu/korquad-chat-v1)

KorQuAD 1.0 문서를 기반으로 ChatGPT가 생성한 9619개 한국어 지식기반 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `총 9619개의 한국어 지식기반 대화 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `총 9619개의 한국어 지식기반 대화 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `총 9619개의 한국어 지식기반 대화 데이터셋입니다.` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `341` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KorQuAD 1.0 데이터에 있는 문서를 ChatGPT에게 준 뒤 생성했습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `KorQuAD 1.0 데이터에 있는 문서를 ChatGPT에게 준 뒤 생성했습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1363자 ≈ 341 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[heegyu__llama-2-ko-7b-chat|heegyu/llama-2-ko-7b-chat]]
