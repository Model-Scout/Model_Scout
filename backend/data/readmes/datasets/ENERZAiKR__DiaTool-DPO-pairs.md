---
license: apache-2.0
language:
- en
- ko
task_categories:
- text-generation
tags:
- dpo
- preference
- tool-use
- function-calling
- multi-turn
size_categories:
- 10K<n<100K
configs:
- config_name: en
  data_files: data_en/diatool_dpo_all.clean.jsonl
- config_name: ko
  data_files: data_ko/diatool_dpo_all.clean.jsonl
---

# DiaTool-DPO Pairs (glaive-seeded, EN/KO)

DiaTool-DPO(arXiv:2504.02882) 방법론 재현으로 구축한 **멀티턴 tool-use 궤적 선호쌍** 데이터셋.
TA-LLM의 대화흐름 제어(slot-filling 질문 / tool call 수락 / 거절 판단)를 DPO로 학습시키기 위한 것.

## 구성

| 파일 | 쌍 수 | 비고 |
|---|---|---|
| `data_en/diatool_dpo_all.clean.jsonl` | 12,359 | easy 7,342 + hard 5,017 |
| `data_ko/diatool_dpo_all.clean.jsonl` | 10,604 | easy 6,378 + hard 4,226 (시드 대화 기계번역) |
| `data_{en,ko}/diatool_dpo_{easy,hard}.clean.jsonl` | — | 난이도 분할본 |
| `data_{en,ko}/validate_report.json` | — | 품질 게이트 리포트(탈락 사유 통계) |

`.clean` = 2단계 품질 게이트 통과분: ① rule 체크(required 값 잔존 검사·쌍 불변식),
② LLM judge(필드별 값-복원 추출 방식 정보누락 판정 + required-only/답변-인자 정합/거절문 판정).

## 스키마 (jsonl 행)

```json
{
  "id": "…", "seed_id": "…",
  "query_type": 1,                  // 1=즉시호출 2=slot-filling 3=거절
  "difficulty": "easy",             // easy | hard
  "lesson": "prevent_redundant_slot_filling",  // Table 1의 학습 목표 7종
  "chosen_traj": "1->3->4->5", "rejected_traj": "1->2->3->4->5",
  "function": "calculate_tip",
  "tools": [ { "type": "function", "function": { … } } ],
  "chosen":   [ {"role":"user"|"assistant"|"tool", "content":…, "tool_calls":[…]} ],
  "rejected": [ … ]                 // 첫 user 발화만 chosen과 공유
}
```

메시지는 OpenAI/Qwen3 chat 포맷(assistant `tool_calls`의 `arguments`는 JSON 문자열,
tool 응답은 `role:"tool"`). 학습 시 user/tool 턴은 loss에서 제외할 것.

## 출처·구축

- 시드: [glaiveai/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) (Apache-2.0)에서
  정형 Type-1 대화 추출(첫 발화에 required 전부 포함된 4턴 구간, 중복 제거)
- 증강·거절문·번역·judge 교사: **Qwen3-235B-A22B-Instruct-2507-FP8** (로컬 vLLM)
- 페어링: 논문 Table 1 재현 (redundant slot-filling / slot hallucination / tool-call accept / reject ×
  easy/hard/M-variant). glaive의 required≥3 부족으로 hard_m 풀은 축소, hard 풀에서 M-variant 보충
- 상세 파이프라인: 사내 `LLM_158/DPO` 레포(01 시드→02 번역(ko)→03 증강·거절→04 페어링→05 검증→06 필터)

## 실전 사용 기록

`data_en/diatool_dpo_all.clean.jsonl`로 ternary QAT 1.7B(agentic SFT 후)에 반복 DPO
(lr 1e-7, chosen NLL 앵커 α=1.0, acc 0.99 조기종료, 도스당 ~30스텝 × 8도스):
tau2-bench pass¹ 10.9→14.4%, evalscope avg10 무손상. 세부는 LLM_Hard_STE 레포 DPO 브랜치.
