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
- claude-only
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
    num_examples: 12126
  dataset_size: 13500000
configs:
- config_name: default
  data_files:
  - split: train
    path: "*.parquet"
---

# Claude Opus Reasoning 12K - Korean (Filtered v2, Claude-Only)

[Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered)의 **엄격 필터링 버전**입니다.

**12,126개의 Claude Opus 전용 한국어 추론 데이터셋**으로, 비-Claude 데이터(Qwen 생성)를 모두 제거했습니다.

## Filtered v1 대비 변경사항

| 버전 | 건수 | 설명 |
|------|------|------|
| 원본 | 12,842 | 원시 병합 데이터셋 |
| Filtered v1 | 12,757 | 거절 + 빈 응답 제거 |
| **Filtered v2** | **12,126** | v1 + Qwen 데이터 제거 (Claude 전용) |

### v2 변경사항
- `Jackrong/Qwen3.5-reasoning-700x` 소스에서 **631건 제거**
- **Claude Opus가 생성한 추론 데이터만** 포함
- v1의 모든 품질 필터 유지 (거절 제거, 빈 응답 정리, 깨진 번역 복구)

## 소스별 분포

| 소스 | 건수 | 비율 |
|------|------|------|
| Roman1111111/claude-opus-4.6-10000x | 9,601 | 79.2% |
| nohurry/Opus-4.6-Reasoning-3000x-filtered | 2,276 | 18.8% |
| TeichAI/claude-4.5-opus-high-reasoning-250x | 249 | 2.1% |

## 도메인별 분포

| 도메인 | 건수 | 비율 |
|--------|------|------|
| simple logic and math | 7,468 | 61.6% |
| math | 4,143 | 34.2% |
| code | 266 | 2.2% |

> 참고: `science`와 `instruction_following` 도메인은 전부 Qwen 소스였으므로 제거되었습니다.

## 난이도별 분포

| 난이도 | 건수 |
|--------|------|
| medium | 11,749 |
| phd | 69 |
| hard | 59 |

## 스키마

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `id` | string | 고유 식별자 |
| `source` | string | 원본 데이터셋 출처 |
| `messages` | string | `{role, content}` 쌍의 JSON 배열 (user/assistant) |
| `domain` | string | 과제 도메인 (math, code) |
| `difficulty` | string | 난이도 (medium, hard, phd) |
| `teacher_model` | string | 응답 생성 모델 (`claude-opus-4.6`) |
| `language` | string | 언어 코드 (`ko`) |

## 필터링 과정

1. **v1 필터**: 거절 탐지(58건), 빈 응답 제거(26건), 깨진 번역 복구(11건)
2. **v2 필터**: Qwen 소스 데이터 제거(631건) — 순수 Claude Opus 추론만 남김
3. **모델 기반 검증**: Gemma 4 26B로 50건 검증 (추가 문제 0건)

## 사용법

```python
from datasets import load_dataset
dataset = load_dataset("Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2")
```

## 관련 데이터셋

| 데이터셋 | 언어 | 건수 | 설명 |
|----------|------|------|------|
| [claude-opus-4.6-reasoning-12k](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k) | EN | 12,842 | 원본 |
| [claude-opus-4.6-reasoning-12k-ko](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko) | KO | 12,842 | 한국어 번역 |
| [claude-opus-4.6-reasoning-12k-en-filtered](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-en-filtered) | EN | 12,757 | 필터링 v1 |
| [claude-opus-4.6-reasoning-12k-ko-filtered](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered) | KO | 12,757 | 필터링 v1 한국어 |
| [claude-opus-4.6-reasoning-12k-en-filtered-v2](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-en-filtered-v2) | EN | 12,126 | 필터링 v2 |
| **claude-opus-4.6-reasoning-12k-ko-filtered-v2** | **KO** | **12,126** | **필터링 v2 (현재)** |

## 라이선스

Apache 2.0
