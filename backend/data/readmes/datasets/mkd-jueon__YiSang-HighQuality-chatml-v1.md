---
license: apache-2.0
language:
- ko
task_categories:
- text-generation
tags:
- sft
- instruction-tuning
- korean
- chatml
- reasoning
size_categories:
- 100K<n<1M
pretty_name: YiSang-HighQuality ChatML (Korean) v1
configs:
- config_name: default
  data_files: "*_shard_*.jsonl"
---

# YiSang-HighQuality ChatML (Korean) v1

[KOREAson/YiSang-HighQuality](https://huggingface.co/datasets/KOREAson/YiSang-HighQuality)를 한국어 SFT용으로 가공한 데이터셋입니다. 원본 `response`에 포함된 `<think>...</think>` 영어 추론 트레이스를 **전부 제거**하고 실제 답변만 남긴 뒤, 정제 → 품질 필터 → 안전성 필터 → 중복 제거 → ChatML 포맷팅 → 토크나이즈 검증을 거친 결과물입니다.

- **총 샘플 수**: 259,596
- **총 토큰 수**: 약 1.78억 (178,406,073 tokens, keural tokenizer 기준, 평균 687 tokens/sample)
- **포맷**: ChatML (`<|im_start|>role ... <|im_end|>`)
- **최대 길이**: 8,192 tokens (초과 시 truncate)
- **추론 트레이스**: 최종 산출물 전수 검사 기준 `<think>`/`</think>` 잔존 **0건**
- **생성일**: 2026-07-10

## 데이터 구조

JSONL 형식이며, 레코드 스키마는 다음과 같습니다:

```json
{"text": "<|im_start|>user\n질문...\n<|im_end|>\n<|im_start|>assistant\n응답...\n<|im_end|>"}
```

## 원본 데이터셋

| 이름 | 소스 | 수집 | 최종 | 태스크 | 생성 방식 | 라이선스 |
|------|------|-----:|-----:|--------|-----------|----------|
| yisang_highquality | [KOREAson/YiSang-HighQuality](https://huggingface.co/datasets/KOREAson/YiSang-HighQuality) | 283,688 | 259,596 | reasoning | synthetic | Apache-2.0 |

## 처리 단계별 샘플 흐름

| 단계 | 출력 샘플 수 | 비고 |
|------|-----------:|------|
| 수집 | 283,688 | HF Hub 전체 다운로드 |
| 구조화 | 283,687 | 표준 messages 스키마 변환 |
| 클린 (**think 제거**) | 283,684 | `<think>...</think>` 트레이스 제거, 제거 후 빈 응답 0건 |
| 품질 필터 | 282,835 | 품질 스코어 < 0.6 제거 (849건) |
| 안전 필터 | 281,974 | 유해/PII 태깅 제거 (861건) |
| 중복 제거 | 259,596 | MinHash near-dup 22,378건 제거 (92.1% 유지) |

## 토큰 길이 분포

| 구간 (tokens) | 샘플 수 |
|---------------|--------:|
| 0–512 | 94,352 |
| 512–1,024 | 123,521 |
| 1,024–2,048 | 40,429 |
| 2,048–4,096 | 1,289 |
| 4,096+ | 5 |

## 전처리 파이프라인

1. **Collect** — HuggingFace Hub에서 원본 전체 수집
2. **Structure** — `{instruction, response}` → 표준 messages 스키마 정규화
3. **Clean** — `strip_think` 적용: assistant 응답의 `<think>...</think>` 추론 트레이스 제거 후 제어문자/공백 정리 (길이·placeholder 검사는 제거 후의 실제 답변 기준)
4. **Quality / Safety** — 품질 스코어(≥0.6) 및 유해 콘텐츠 필터
5. **Dedup** — instruction+output SHA-256 exact match + MinHash(128 perm, threshold 0.8) near-dup 제거
6. **Format** — ChatML 템플릿 적용
7. **Tokenize / Package** — keural tokenizer 기준 토큰 수 검증 후 샤드 분할

무결성 검증용 SHA-256 체크섬은 `manifest.json`에 포함되어 있습니다. 스키마 감사 결과 위반 0건.

## 라이선스 및 주의사항

- 원본(KOREAson/YiSang-HighQuality)의 **Apache-2.0** 라이선스를 따릅니다.
- 원본의 추론 트레이스(`<think>` 블록, 주로 영어)는 이 릴리스에서 제거되었습니다. 추론 트레이스가 필요한 용도(예: reasoning 증류)라면 원본 데이터셋을 사용하세요.
- 답변은 LLM 생성(synthetic) 기반이므로 품질 편차가 있을 수 있습니다.
- 중복 제거는 이 데이터셋 내부 기준입니다. 다른 SFT 데이터셋과 병합할 경우 cross-dataset 중복 확인을 권장합니다.
