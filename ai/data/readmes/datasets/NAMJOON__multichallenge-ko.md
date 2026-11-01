---
language:
- ko
license: other
task_categories:
- text-generation
tags:
- multi-turn
- dialogue
- korean
- machine-translated
- benchmark
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
- config_name: korean_only
  data_files:
  - split: train
    path: data/korean_only.jsonl
---

# MultiChallenge (한국어 번역)

[MultiChallenge](https://aclanthology.org/2025.findings-acl.958/) (Sirdeshmukh et al., Findings of ACL 2025) 를 한국어로 기계 번역한 자료입니다. 번역 벤치마크와 한국어로 직접 작성한 벤치마크를 비교하는 연구를 위해 만들었습니다.

## 불러오기

```python
from datasets import load_dataset
ds = load_dataset("NAMJOON/multichallenge-ko")                  # 한국어 + 원문
ds = load_dataset("NAMJOON/multichallenge-ko", "korean_only")   # 한국어만
```

## 구성

273 대화, 4개 축. 원본 구조를 유지합니다.

- `AXIS`: INSTRUCTION_RETENTION, INFERENCE_MEMORY, RELIABLE_VERSION_EDITING, SELF_COHERENCE
- `CONVERSATION`: 번역됨. 모든 대화가 사용자 턴으로 끝나며, 평가 대상은 모델이 생성할 다음 응답입니다
- `TARGET_QUESTION`: 채점자가 그 응답에 적용하는 예/아니오 질문. 대화와 함께 번역해 표현을 맞췄습니다
- `PASS_CRITERIA`: YES 또는 NO. 원본 그대로

## 번역 방식

- 번역기: `openai/gpt-6-luna` (OpenRouter 경유)
- **대화 단위 번역**: 대화 하나를 통째로 한 번에 번역해 턴 사이의 지칭과 표기를 맞췄습니다.
  조각이 빠지면 빠진 조각만 다시 요청했습니다.
- **충실성 우선**: 정보를 더하거나 빼지 않고, 모호한 지칭을 해소하지 않으며, 원문의 오류와
  모순도 그대로 옮겼습니다. 원문에 없는 호응이나 상투구("알겠습니다", "물론이죠")를 붙이지
  않도록 했습니다.
- **보존**: 코드, 수식, URL, 자리표시자, 숫자, 단위는 원문 그대로 두었습니다.
- **화계는 지정하지 않았습니다.** 원문 턴의 말투에 맞추도록만 지시했습니다. 영어는 존댓말
  등급을 표시하지 않으므로, 한국어 화계는 번역 모델이 고른 값입니다.
- 원문은 각 항목에 `*_en` 필드로 함께 들어 있습니다.
- 번역에 쓴 시스템 프롬프트 전문은 `translation_prompt.txt` 에 있습니다. 모든 데이터셋에 같은
  프롬프트를 썼고, 데이터셋별 주의사항은 대화마다 붙는 메모로만 전달했습니다.

## 한계

- 기계 번역이며 사람 검수를 거치지 않았습니다.
- 번역 과정에서 원 과제가 재던 영어 고유 현상(대명사 해소, 철자, 운율 등)이 약해지거나
  달라질 수 있습니다.
- 한국어 화계와 말투는 원문에 근거가 없는 값이며 번역 모델에 따라 달라질 수 있습니다.

## 원 자료와 라이선스

[MultiChallenge](https://aclanthology.org/2025.findings-acl.958/) (Sirdeshmukh et al., Findings of ACL 2025)

원본: https://huggingface.co/datasets/nmayorga7/multichallenge

원 저장소(Scale AI)에는 라이선스 표기가 없습니다. 이 번역은 MIT 로 표기된 허깅페이스 재배포본 `nmayorga7/multichallenge` 를 원본으로 사용했습니다. 이용 조건은 원 저작자를 따릅니다. 사용할 때는 원 논문과 이 저장소를 함께 인용해 주십시오.
