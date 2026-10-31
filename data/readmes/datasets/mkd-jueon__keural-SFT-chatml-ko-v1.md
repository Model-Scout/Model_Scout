---
license: other
license_name: mixed-open-license
license_link: https://huggingface.co/datasets/mkd-jueon/keural-SFT-chatml-ko-v1/blob/main/README.md
language:
- ko
task_categories:
- text-generation
tags:
- sft
- instruction-tuning
- korean
- chatml
- conversational
size_categories:
- 100K<n<1M
pretty_name: Keural SFT ChatML (Korean) v1
configs:
- config_name: default
  data_files: "*_shard_*.jsonl"
- config_name: kocommercial
  data_files: kocommercial_shard_*.jsonl
- config_name: kullm_v2
  data_files: kullm_v2_shard_*.jsonl
- config_name: openorca_gugugo_ko
  data_files: openorca_gugugo_ko_shard_*.jsonl
- config_name: openorca_ko
  data_files: openorca_ko_shard_*.jsonl
- config_name: kopen_platypus
  data_files: kopen_platypus_shard_*.jsonl
- config_name: korean_safe_conversation
  data_files: korean_safe_conversation_shard_*.jsonl
- config_name: medical_reasoning_ko
  data_files: medical_reasoning_ko_shard_*.jsonl
- config_name: claude_reasoning_ko
  data_files: claude_reasoning_ko_shard_*.jsonl
---
# Keural SFT ChatML (Korean) v1

한국어 SFT(Supervised Fine-Tuning)용 통합 데이터셋입니다. 공개 한국어 instruction/대화 데이터셋 8종을 수집하여 정제 → 품질 필터링 → 안전성 필터링 → 중복 제거(exact + MinHash near-dup) → ChatML 포맷팅 → 토크나이즈 검증을 거친 결과물입니다.

- **총 샘플 수**: 710,278
- **총 토큰 수**: 약 1.9억 (190,724,939 tokens, keural tokenizer 기준)
- **포맷**: ChatML (`<|im_start|>role ... <|im_end|>`)
- **최대 길이**: 8,192 tokens (초과 시 truncate)
- **생성일**: 2026-07-10

## 데이터 구조

각 샤드는 JSONL 형식이며, 레코드 스키마는 다음과 같습니다:

```json
{"text": "<|im_start|>user\n질문...\n<|im_end|>\n<|im_start|>assistant\n응답...\n<|im_end|>"}
```

## 구성 데이터셋

| 이름 | 소스 | 수집 | 최종 | 태스크 | 생성 방식 | 라이선스 |
|------|------|-----:|-----:|--------|-----------|----------|
| openorca_gugugo_ko | [squarelike/OpenOrca-gugugo-ko](https://huggingface.co/datasets/squarelike/OpenOrca-gugugo-ko) | 400,000 (of 2.24M) | 316,553 | general | synthetic | MIT |
| kocommercial | [MarkrAI/KoCommercial-Dataset](https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset) | 175,455 | 171,441 | general | mixed | MIT |
| kullm_v2 | [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | 152,631 | 127,943 | general | synthetic | Apache-2.0 |
| korean_safe_conversation | [jojo0217/korean_safe_conversation](https://huggingface.co/datasets/jojo0217/korean_safe_conversation) | 53,959 | 26,803 | safety | mixed | Apache-2.0 |
| medical_reasoning_ko | [ChuGyouk/medical-o1-reasoning-SFT-Ko](https://huggingface.co/datasets/ChuGyouk/medical-o1-reasoning-SFT-Ko) | 25,683 | 24,207 | reasoning | synthetic | Apache-2.0 |
| kopen_platypus | [kyujinpy/KOpen-platypus](https://huggingface.co/datasets/kyujinpy/KOpen-platypus) | 24,927 | 17,444 | reasoning | mixed | CC-BY-4.0 |
| openorca_ko | [kyujinpy/OpenOrca-KO](https://huggingface.co/datasets/kyujinpy/OpenOrca-KO) | 21,633 | 14,852 | general | synthetic | MIT |
| claude_reasoning_ko | [Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2) | 12,127 | 11,035 | reasoning | synthetic | Apache-2.0 |

- **수집** = 원본에서 받아온 샘플 수, **최종** = 정제·필터·중복 제거 후 릴리스에 포함된 샘플 수

## 토큰 길이 분포

| 구간 (tokens) | 샘플 수 |
| ------------- | ------: |
| 0–512        | 669,770 |
| 512–1,024    |  36,164 |
| 1,024–2,048  |   3,939 |
| 2,048–4,096  |     399 |
| 4,096+        |       6 |

## 전처리 파이프라인

1. **Collect** — HuggingFace Hub에서 원본 수집 (openorca_gugugo_ko는 400K 스트리밍 캡)
2. **Structure** — 원본 필드를 표준 messages 스키마로 정규화
3. **Clean / Quality** — 최소/최대 응답 길이, 품질 스코어(≥0.6) 필터
4. **Safety** — 유해 콘텐츠 필터링
5. **Dedup** — instruction+output SHA-256 exact match + MinHash(128 perm, threshold 0.8) near-dup 제거 (데이터셋 내부 기준)
6. **Format** — ChatML 템플릿 적용
7. **Tokenize / Package** — keural tokenizer 기준 토큰 수 검증 후 샤드 분할

무결성 검증용 SHA-256 체크섬은 `manifest.json`에 포함되어 있습니다.

## 라이선스 및 주의사항

- 이 데이터셋은 서로 다른 라이선스(MIT, Apache-2.0, CC-BY-4.0)의 공개 데이터셋을 통합한 것입니다. 사용 시 **각 구성 데이터셋의 원본 라이선스**를 준수해야 합니다.
- KOpen-platypus의 일부 원본(Open-Platypus) 서브셋은 비상업 라이선스 논란이 있으므로, 엄격한 상업적 이용 시 원본의 `data_source`별 확인을 권장합니다.
- 중복 제거는 데이터셋 내부 단위로만 수행되었으며, 데이터셋 간(cross-dataset) 중복(예: OpenOrca 번역본 간)은 남아 있을 수 있습니다.
- 대부분의 데이터가 기계 번역 또는 LLM 생성(synthetic) 기반이므로 품질 편차가 있을 수 있습니다.
