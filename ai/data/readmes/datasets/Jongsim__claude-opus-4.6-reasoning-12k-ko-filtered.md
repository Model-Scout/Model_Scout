---
language:
- ko
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- text-generation
tags:
- reasoning
- chain-of-thought
- filtered
- korean
- claude
- opus
- translated
dataset_info:
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: messages
    dtype: string
  - name: domain
    dtype: string
  - name: difficulty
    dtype: string
  - name: teacher_model
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_examples: 12757
  dataset_size: 26100000
configs:
- config_name: default
  data_files:
  - split: train
    path: "*.parquet"
---

# Claude Opus Reasoning 12K - Korean (Filtered)

[Jongsim/claude-opus-4.6-reasoning-12k-ko](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko)의 **필터링 및 품질 개선 버전**입니다.

**12,757개의 고품질 한국어 추론 데이터셋**으로, 거절 응답 제거 + 깨진 번역 복구가 적용되었습니다.

## 필터링 요약

| 변경 내용 | 건수 | 설명 |
|-----------|------|------|
| 거절/거부 응답 제거 | 58건 | AI가 요청을 거부하거나 안전 지침을 인용하는 응답 |
| 빈/깨진 응답 제거 | 26건 | assistant 응답이 없거나 극단적으로 짧은 항목 |
| 깨진 번역 복구 | +11건 | Gemma 4 26B 모델로 재번역하여 복구 |
| **최종 데이터셋** | **12,757건** | 원본 12,842건에서 85건 제거 |

## 데이터셋 상세

### 소스별 분포

| 소스 | 건수 | 비율 |
|------|------|------|
| Roman1111111/claude-opus-4.6-10000x | 9,601 | 75.3% |
| nohurry/Opus-4.6-Reasoning-3000x-filtered | 2,276 | 17.8% |
| Jackrong/Qwen3.5-reasoning-700x | 631 | 4.9% |
| TeichAI/claude-4.5-opus-high-reasoning-250x | 249 | 2.0% |

### 도메인별 분포

| 도메인 | 건수 | 비율 |
|--------|------|------|
| simple logic and math | 7,468 | 58.5% |
| math | 4,372 | 34.3% |
| code | 364 | 2.9% |
| science | 166 | 1.3% |
| instruction_following | 138 | 1.1% |

### 난이도별 분포

| 난이도 | 건수 |
|--------|------|
| medium | 11,749 |
| phd | 69 |
| hard | 59 |

### 스키마

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `id` | string | 고유 식별자 |
| `source` | string | 원본 데이터셋 출처 |
| `messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant) |
| `domain` | string | 과제 도메인 (math, code, science 등) |
| `difficulty` | string | 난이도 (medium, hard, phd) |
| `teacher_model` | string | 응답 생성 모델 (`claude-opus-4.6`) |
| `language` | string | 언어 코드 (`ko`) |

### 필터링 과정

1. **패턴 기반 거절 탐지** — EN/KO 양쪽에서 AI 거절/거부 표현 정규식 탐지
2. **빈 응답 탐지** — assistant 응답이 없거나 10자 미만인 항목
3. **모델 기반 검증** — Gemma 4 26B로 50건 랜덤 샘플 거절 여부 확인 (추가 발견 0건)
4. **번역 품질 검증** — Gemma 4 26B로 30건 EN-KO 쌍 비교 검증 (전체 통과)
5. **깨진 번역 복구** — 빈 한국어 응답 12건 중 11건을 Gemma 4 26B로 재번역

## 사용법

```python
from datasets import load_dataset
dataset = load_dataset("Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered")
```

## 관련 데이터셋

- [Jongsim/claude-opus-4.6-reasoning-12k](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k) — 영어 원본 (12,842건)
- [Jongsim/claude-opus-4.6-reasoning-12k-ko](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko) — 한국어 번역 (12,842건)
- [Jongsim/claude-opus-4.6-reasoning-12k-en-filtered](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-en-filtered) — 필터링된 영어 (12,757건)

## 라이선스

Apache 2.0
