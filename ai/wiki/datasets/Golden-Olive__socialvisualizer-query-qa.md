---
type: "dataset"
id: "Golden-Olive/socialvisualizer-query-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/Golden-Olive/socialvisualizer-query-qa"
downloads: 13
summary: "SocialVisualizer query LoRA 어댑터 학습용 이메일·메신저 QA 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# Golden-Olive/socialvisualizer-query-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/Golden-Olive/socialvisualizer-query-qa)

SocialVisualizer query LoRA 어댑터 학습용 이메일·메신저 QA 합성 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — tag_match · readme, tags = `qa` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `QA 세트입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `QA 세트입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `실제 개인 메일/메신저 데이터는 포함되어 있지 않습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `143문항 전체가 train(129)/val(14)로 분할되어 실제 학습(및 체크포인트 선택)에 사용됐습니다.` · 신뢰도 medium
