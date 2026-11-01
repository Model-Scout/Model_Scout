---
license: other
language:
- ko
- en
task_categories:
- text-generation
tags:
- korean
- sft
- keural
- moe
size_categories:
- 100K<n<1M
---

# Keural v2 — MoE Fine-Tuning Dataset

**상태: 비공개 (private) — 공개 배포 대상 아님**

Keural MoE Pro v2 모델 파인튜닝을 위해 8개 카테고리(A~H)로 구성된 SFT 학습 데이터셋입니다. 자세한 수집·처리 기준은 `mkd-minju/Keural-MoE-Pro-v2` GitHub 저장소의 `docs/V2-DATASET-PREP.md` 계획 문서를 따릅니다.

## 카테고리 구성

| 파일 | 카테고리 | 목표 건수 | 언어 | 주요 출처 | 라이선스 |
|---|---|---:|---|---|---|
| `A_korean_conversation.jsonl` | 한국어 대화/지침 | 50,000 | ko | `mkd-chanwoo/keural-conversation-chatml-ko`, `mkd-chanwoo/keural-rag-chatml-ko`, `Mkd-Yonas/keural-SFT-chatml-ko-v1`(kullm_v2/kocommercial/korean_safe_conversation), 백업: `nlpai-lab/kullm-v2`, `beomi/KoAlpaca-v1.1a` | MIT / Apache-2.0 / CC BY / CC BY-SA만 사용 |
| `B_kmmlu_mcq.jsonl` | 한국어 객관식/지식 | 15,000 | ko | `HAERAE-HUB/KMMLU` (`train`/`dev` 스플릿만, `test` 제외) | CC-BY-4.0 |
| `C_english_mcq.jsonl` | 영어 객관식/지식 | 10,000 | en | `cais/mmlu`(`auxiliary_train`만), `allenai/ai2_arc`, `openbookqa`(train 스플릿) | 각 원본 라이선스 |
| `D_math_reasoning.jsonl` | 수학 추론(CoT) | 20,000 | ko+en | `openai/gsm8k`(`train`만), `meta-math/MetaMathQA`, `TIGER-Lab/MathInstruct`, 한국어 `orca_math_korean`(keural-SFT 내) | 각 원본 라이선스 |
| `E_code_clean.jsonl` | 코드(들여쓰기 검증됨) | 25,000 | en/ko | `ise-uiuc/Magicoder-Evol-Instruct-110K`, `ise-uiuc/Magicoder-OSS-Instruct-75K`, `m-a-p/CodeFeedback-Filtered-Instruction` | MIT |
| `F_english_replay.jsonl` | 영어 일반(망각 방지) | 25,000 | en | `HuggingFaceH4/ultrachat_200k`, `Open-Orca/OpenOrca`, `teknium/OpenHermes-2.5` | 각 원본 라이선스 |
| `G_korean_longform.jsonl` | 한국어 장문 답변 | 5,000 | ko | 신규 수집 없음 — A 카테고리에서 고품질 장문 답변만 선별 | A와 동일 |
| `H_identity.jsonl` | 정체성/페르소나 | 1,500 | ko+en | 100% 자체 작성 (외부 소스 없음) | internal |

## 처리 및 검증 기준

수집된 원본 데이터에 다음과 같은 필수 검증을 적용했습니다(`docs/V2-DATASET-PREP.md` §6). **테스트 스플릿 배제** — KMMLU/MMLU/GSM8K/ARC/OpenBookQA는 `train`/`auxiliary_train`/`dev` 스플릿만 사용하고 `test`(MMLU는 `validation` 포함)는 전량 제외했습니다. **코드 들여쓰기 검증** — 모든 assistant 코드 블록을 `ast.parse`로 실제 파싱 가능한지 확인, 실패 시 해당 행 제외(v1.0의 HumanEval 회귀 재발 방지). **정체성 오염 필터링** — OpenAI/Anthropic/Google/ChatGPT/GPT-4/Gemini/Claude/Qwen 등을 자신이라고 답하는 assistant 응답을 제거 또는 정정.

추가로 상업적으로 문제없는 라이선스(MIT/Apache-2.0/CC BY/CC BY-SA)만 유지하고, 불확실한 경우 `unknown`으로 표기했습니다(허용 라이선스로 임의 추정하지 않음).

## 스키마

```json
{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}], "source_name": "kmmlu_train", "license": "cc-by-4.0"}
```

`source_name`은 데이터 출처를 식별하는 짧은 태그입니다(예: `magicoder_clean`, `kmmlu_train`, `keural_identity`). `license`는 행 단위의 실제 라이선스 문자열입니다.

## MKD 소유권 및 라이선스 고지 / MKD Ownership and License Notice

`H_identity.jsonl`은 주식회사 MKD(MKD Inc.)가 100% 자체 작성한 콘텐츠이며 `license: internal`로 표시됩니다. 나머지 카테고리(A~G)는 위 표에 명시된 각 원저작자의 공개 데이터셋에서 수집되었으며, 그 라이선스(MIT/Apache-2.0/CC BY/CC BY-SA/CC-BY-4.0)를 그대로 따릅니다.

**이 데이터셋의 수집, 선별, 처리 및 검증 기준(테스트 스플릿 배제, 코드 들여쓰기 검증, 정체성 오염 필터링) 적용은 주식회사 MKD(MKD Inc.)가 수행했습니다.** 이 저장소의 큐레이션·구성·자체 작성 콘텐츠(H_identity)에 대한 권리는 주식회사 MKD에 있으며, 사전 서면 동의 없이 무단 복제, 배포, 재사용을 금지합니다. 각 카테고리의 원본 소스 데이터는 위 표에 명시된 원저작자의 라이선스를 그대로 따릅니다.

`H_identity.jsonl` is 100% original content authored by MKD Inc. (주식회사 MKD) and is marked `license: internal`. The remaining categories (A–G) were collected from the public datasets of their respective original publishers listed in the table above and remain governed by those licenses (MIT / Apache-2.0 / CC BY / CC BY-SA / CC-BY-4.0).

**The collection, curation, and application of the validation criteria described above (test-split exclusion, code indentation validation, identity-contamination filtering) for this dataset were performed by MKD Inc. (주식회사 MKD).** Rights to this repository's curation, composition, and self-authored content (H_identity) belong to MKD Inc. and may not be copied, distributed, or reused without prior written permission. The original source data for each category remains governed by the license of its original publisher as listed above.