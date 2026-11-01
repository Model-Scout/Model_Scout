---
license: apache-2.0
language:
- ko
task_categories:
- text-generation
tags:
- rlvr
- reasoning
- countdown
pretty_name: Countdown RLVR
---

# Countdown RLVR

Qwen3-4B의 검증 가능한 추론 학습에 사용하는 Countdown 데이터셋입니다.
주어진 숫자를 각각 한 번 사용하여 목표값을 만드는 수식을 생성합니다.

## 1. 데이터 구성

| 분할 | 개수 | 숫자 개수 | 목표값 | SHA-256 |
|---|---:|---:|---:|---|
| train | 1,024 | 4 | 10~100 | `aa7abb6242d8ada72e55a6d8d0917e3618473ddf2f0f880b288814394b231131` |
| validation | 128 | 4 | 10~100 | `b06a1be3604d637aa19bd61af57aadf98fbbffcb8ef4db8d477fe8535c617497` |
| test | 256 | 4 | 10~100 | `416c02076321875cccfeed19f742e56048269b4b9d24112f6a2bee82ba301815` |

`demo.jsonl`에는 검증 흐름을 확인하는 숫자 3개 문제를 둡니다.

## 2. 데이터 필드

| 필드 | 의미 |
|---|---|
| `problem_id` | 문제 식별자 |
| `split` | train, validation, test 분할 |
| `number_count` | 문제에 사용하는 숫자 개수 |
| `numbers` | 각각 한 번 사용할 숫자 목록 |
| `target` | 수식의 목표값 |
| `prompt` | 모델에 전달하는 한국어 문제 문자열 |

문제 생성기는 solver로 해답 존재 여부를 확인한 뒤 `solution`을 저장하지 않습니다.
따라서 RLVR 학습 입력에는 정답 수식이나 reasoning 궤적이 포함되지 않습니다.

## 3. 생성과 검증

문제 생성기는 다음 조건을 적용합니다.

- 허용 연산: 두 수 사이의 `+`, `-`, `*`, `/`와 괄호
- 숫자 사용: 입력 숫자를 각각 정확히 한 번 사용
- 목표값 일치: 수식 계산 결과와 `target` 비교
- 해답 존재: 결정적 solver로 확인

보상은 형식 0.3, 수식 규칙 0.2, 목표값 일치 0.5의 가중합입니다.
형식 보상은 마지막으로 완결된 `answer` 태그의 내용 존재 여부를 검사합니다.
태그 안에 허용하지 않는 문자가 있으면 형식 보상은 유지되고 수식 규칙 보상은 0이 됩니다.

## 4. 사용 예

```python
from src.artifacts import load_jsonl, resolve_artifact

path = resolve_artifact(
    "data/countdown/test.jsonl",
    "NotoriousH2/countdown-rlvr",
    filename="test.jsonl",
)
test_rows = load_jsonl(path)
```

`revision`을 생략하면 프로젝트의 publish manifest에 기록된 commit을 사용합니다.

## 5. 생성 계보

Countdown 문제와 해답 존재 여부는 `src/countdown.py`가 결정적으로 생성합니다.
Teacher 모델은 이 데이터셋 생성에 사용하지 않습니다.

## 6. 제한

이 데이터셋은 숫자 4개와 사칙연산으로 범위를 제한합니다.
수학적 추론 능력 전반이나 자유 형식 증명을 평가하지 않습니다.
평가 수치는 공개 모델의 실행 결과 JSON과 model card에서 확인합니다.
