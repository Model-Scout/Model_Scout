---
language:
- ko
license: mit
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

# Multi-Turn-Instruct (한국어 번역)

[MultiTurnInstruct](https://aclanthology.org/2025.findings-emnlp.1387/) (Han et al., Findings of EMNLP 2025) 를 한국어로 기계 번역한 자료입니다. 번역 벤치마크와 한국어로 직접 작성한 벤치마크를 비교하는 연구를 위해 만들었습니다.

## 불러오기

```python
from datasets import load_dataset
ds = load_dataset("NAMJOON/multiturninstruct-ko")                  # 한국어 + 원문
ds = load_dataset("NAMJOON/multiturninstruct-ko", "korean_only")   # 한국어만
```

## 구성

981 대화, 9개 범주. 원본 구조를 유지합니다.

- `category`: personalization, triggering, recursive_reasoning, privacy_protection, prioritization, memorization, multitasking, dynamic_environment, dynamic_instruction
- `turns[].text`: 번역됨
- **`turns[].evaluation_reference`**: 응답 안에서 찾는 정답 문자열 목록. 한국어 응답에서 찾을 수 있도록 번역했고, 원문은 `evaluation_reference_en` 에 있습니다. 선택지 글자(A, B)와 숫자(40%, 1973–1974)처럼 언어와 무관한 값은 번역하지 않았습니다. memorization 범주의 정답은 앞선 턴을 인용하므로 같은 호출에서 번역해 번역된 턴과 문자열이 일치하게 했습니다
- 채점할 때는 `evaluation_reference` 와 `evaluation_reference_en` 을 함께 보는 것을 권합니다. 고유명사는 모델이 한글로 쓸 수도 있기 때문입니다

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

[MultiTurnInstruct](https://aclanthology.org/2025.findings-emnlp.1387/) (Han et al., Findings of EMNLP 2025)

원본: https://huggingface.co/datasets/Glaciohound/Multi-Turn-Instruct

원 자료의 MIT 라이선스를 따릅니다. 사용할 때는 원 논문과 이 저장소를 함께 인용해 주십시오.
