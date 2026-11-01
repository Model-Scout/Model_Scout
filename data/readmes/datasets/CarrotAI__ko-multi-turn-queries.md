---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
tags:
- query
- korean
- text
- generation
size_categories:
- 1K<n<10K
---

## 데이터셋 개요

이 데이터셋은 한국어 instruction 데이터셋입니다.
- 지시문을 정보 단위로 분해하고, 이를 자연스러운 다중 턴 대화 형태로 변환을 목표로 합니다.

### 특징

- Performance: 평균 응답 품질
- Aptitude (A90): 90 백분위수 성능
- Unreliability (U90-10): 응답 일관성 지표

## 필드 설명

| 필드명 | 타입 | 설명 |
|--------|------|------|
| original_input | string | 원본 복잡한 지시문 |
| segments | list | 원본을 분해한 원자적 정보 단위들 |
| shards | list | 대화형으로 변환된 질문들 (점진적 공개) |
| num_shards | int | 생성된 shard의 총 개수 |
| verification_status | string | 정보 완전성 검증 상태 (complete/incomplete) |
| verification_score | float | 정보 보존도 점수 (0-1) |
| metadata | dict | 생성 시간, 모델, 품질 정보 등 |

## 활용 사례

### 1. 다중 턴 대화 시뮬레이션
```python
conversation = []
for shard in data['shards']:
    conversation.append({"role": "user", "content": shard['text']})
    # 모델이 점진적으로 완전한 답변 구축
    response = model.generate(conversation)
    conversation.append({"role": "assistant", "content": response})
```

### 2. 품질 기반 필터링
```python
# 고품질 데이터만 선택
high_quality = [d for d in dataset if d['verification_score'] > 0.9]
```