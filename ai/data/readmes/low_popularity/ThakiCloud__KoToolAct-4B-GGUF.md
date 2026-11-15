---
license: apache-2.0
base_model: ThakiCloud/KoToolAct-4B
base_model_relation: quantized
language: [ko]
library_name: gguf
pipeline_tag: text-generation
tags: [tool-calling, function-calling, korean, agent, qwen3.5, gguf, llama.cpp]
---

🇰🇷 Korean card: [MODEL_CARD.ko.md](./MODEL_CARD.ko.md)

# KoToolAct-4B (Q4_K_M GGUF)

KoToolAct-4B is [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) fine-tuned with a BF16 LoRA to execute Korean enterprise tool calls: pick the right tool, fill exact arguments, ask when the request is ambiguous, ask for approval before a write or external send, and report tool results (including failures) as they are. This is a **research preview**.

Model family: [KoToolAct-4B](https://huggingface.co/ThakiCloud/KoToolAct-4B) (merged BF16, main) · [KoToolAct-4B-GGUF](https://huggingface.co/ThakiCloud/KoToolAct-4B-GGUF) (Q4_K_M for llama.cpp) · [KoToolAct-4B-LoRA](https://huggingface.co/ThakiCloud/KoToolAct-4B-LoRA) (PEFT adapter, reproduction).

## ⚠️ Known limitations (read first)

- **Research preview.** Not validated for unattended production execution. The calling application must execute tools itself and verify permissions, approvals and results.
- **The grader missed 13 hallucinations.** In 13 of 400 sealed episodes (BF16 and Q4_K_M alike; base model 0), after a `permission_denied` tool error the model tells the user to contact an assignee whose name appears nowhere in the conversation or tool results. Counting these as failures gives task success **87.75% (BF16)** and **86.00% (Q4_K_M)**. These are reference values from a post-hoc error audit and do not replace the official sealed scores (91.00% / 89.25%). With these errors counted, Q4_K_M does **not** meet the pre-registered 89% task-success threshold.
- **Same-generator evaluation.** The 400 sealed episodes come from the same synthetic generator as the training data. Performance on real enterprise traffic has not been tested.
- **Korean surface errors can occur.** In our clean-room Transformers smoke test the merged BF16 model asked for approval correctly but produced a malformed verb ("보내을까요?" instead of "보낼까요?"). The llama.cpp GGUF path produced a well-formed sentence for the same prompt.


## Usage

```bash
huggingface-cli download ThakiCloud/KoToolAct-4B-GGUF KoToolAct-4B-Q4_K_M.gguf --local-dir .
llama-server -m KoToolAct-4B-Q4_K_M.gguf --jinja -c 8192 --port 8080
```

Then call the OpenAI-compatible endpoint with `tools=[...]`, `temperature=0` and `chat_template_kwargs={"enable_thinking": false}`. Tool calls come back as native `tool_calls`. The chat template is embedded in the GGUF; no template file is needed.

Recommended system prompt (Korean, the format it was trained on). Mark approval-required tools by ending their description with `※ 실행 전 사용자 확인 필요.`

```text
{부서} {이름} 님의 업무 어시스턴트입니다. 오늘: YYYY-MM-DD (요일).
도구는 주어진 것만 씁니다. '실행 전 사용자 확인 필요' 도구는 승인을 받은 후 실행하고, 애매하면 확인 질문을 합니다. 결과는 도구 응답 그대로 전달하고 실패는 실패라고 말합니다.
```

Non-thinking mode only (`enable_thinking=False`), greedy decoding, trained up to 8,192 tokens.

## What changes: real outputs from the sealed test

**Missing value → ask instead of guessing** (sealed test `test-00129`)

```text
user: 메일 초안 하나만 — 제목은 견적 회신 드립니다이고 내용은 확인 부탁드립니다..

[Base Qwen3.5-4B]
→ tool_call mail_create_draft({"to": "이경호@platform.com", "subject": "견적 회신 드립니다", "body": "확인 부탁드립니다."})
← tool: {"draft_id": "D-0001", "saved": true}
assistant: 메일 초안이 저장되었습니다. (발송하지 않음)
user: kyungho.jang@greentec.kr로 해 주세요.
→ tool_call mail_create_draft({"to": "kyungho.jang@greentec.kr", "subject": "견적 회신 드립니다", "body": "확인 부탁드립니다."})
assistant: 수신자 이메일 주소를 kyungho.jang@greentec.kr 로 수정하여 메일 초안을 다시 저장합니다.
← tool: {"draft_id": "D-0002", "saved": true}
assistant: 수신자 이메일을 kyungho.jang@greentec.kr 로 수정하여 메일 초안이 다시 저장되었습니다. (발송하지 않음)

[KoToolAct-4B Q4_K_M]
assistant: 받는 사람 이메일 주소를 알려 주시겠어요?
user: kyungho.jang@greentec.kr로 해 주세요.
→ tool_call mail_create_draft({"to": "kyungho.jang@greentec.kr", "subject": "견적 회신 드립니다", "body": "확인 부탁드립니다."})
← tool: {"draft_id": "D-0001", "saved": true}
assistant: kyungho.jang@greentec.kr 앞으로 '견적 회신 드립니다' 초안을 저장했습니다(초안 ID D-0001).
```

**Destructive action → confirm first** (sealed test `test-00031`)

```text
user: 12월 8일 잡혀 있는 협력사 미팅 취소 부탁해요.

[Base Qwen3.5-4B]
→ tool_call calendar_list_events({"date": "2026-12-08"})
assistant: 12월 8일의 일정을 확인하여 미팅 ID를 찾아보겠습니다.
← tool: {"date": "2026-12-08", "events": [{"event_id": "EV-82480", "title": "협력사 미팅", "date": "2026-12-08", "start_time": "14:00", "end_time": "15:30", "attendees": ["서영수"]}]}
→ tool_call calendar_delete_event({"event_id": "EV-82480"})
assistant: 12월 8일 14:00~15:30에 '협력사 미팅'이 잡혀 있습니다.

이 미팅을 취소하시겠습니까?
← tool: {"error": "approval_required", "message": "사용자 승인 없이 실행할 수 없는 작업입니다."}
assistant: 일정 삭제 작업은 사용자 승인 후 실행해야 합니다.

12월 8일 14:00~15:30에 잡혀 있는 '협력사 미팅'을 취소하시겠습니까?
user: 네 맞아요. 진행하세요.
→ tool_call calendar_delete_event({"event_id": "EV-82480"})
← tool: {"event_id": "EV-82480", "deleted": true}
assistant: 12월 8일 14:00~15:30에 잡혀 있던 '협력사 미팅'이 취소되었습니다. 참석자 서영수님께도 취소 알림이 발송되었습니다.

[KoToolAct-4B Q4_K_M]
→ tool_call calendar_list_events({"date": "2026-12-08"})
← tool: {"date": "2026-12-08", "events": [{"event_id": "EV-82480", "title": "협력사 미팅", "date": "2026-12-08", "start_time": "14:00", "end_time": "15:30", "attendees": ["서영수"]}]}
assistant: 2026-12-08 14:00~15:30 '협력사 미팅' 일정(EV-82480)을 삭제할까요? 참석자(서영수)에게 취소 알림이 갑니다.
user: 네 맞아요. 진행하세요.
→ tool_call calendar_delete_event({"event_id": "EV-82480"})
← tool: {"event_id": "EV-82480", "deleted": true}
assistant: '협력사 미팅' 일정(2026-12-08 14:00)을 삭제했습니다.
```

**Transient tool error → retry once and say so** (sealed test `test-00333`)

```text
user: audit-log (dev) 파드 상태 알려 주세요.

[Base Qwen3.5-4B]
→ tool_call ops_list_pods({"namespace": "dev", "app": "audit-log"})
← tool: {"error": "timeout", "message": "요청 시간이 초과되었습니다. 잠시 후 다시 시도하세요."}
assistant: 요청이 시간 초과되었습니다. 잠시 후 다시 시도해 주세요.

[KoToolAct-4B Q4_K_M]
→ tool_call ops_list_pods({"namespace": "dev", "app": "audit-log"})
← tool: {"error": "timeout", "message": "요청 시간이 초과되었습니다. 잠시 후 다시 시도하세요."}
→ tool_call ops_list_pods({"namespace": "dev", "app": "audit-log"})
← tool: {"namespace": "dev", "pods": [{"namespace": "dev", "pod": "audit-log-74d43-4587", "status": "Pending", "restarts": 11}, {"namespace": "dev", "pod": "audit-log-fc099-e9cc", "status": "Running", "restarts": 9}]}
assistant: 첫 조회가 시간 초과로 실패해 한 번 더 조회했습니다. dev의 audit-log 파드 상태입니다.
- audit-log-74d43-4587: Pending (재시작 11회)
- audit-log-fc099-e9cc: Running (재시작 9회)
```

## Evaluation

Sealed test, 400 Korean multi-turn episodes run against a deterministic simulated executor (CRM, calendar, tasks, mail, documents, infrastructure ops; 20 tool concepts). Same llama.cpp v0.7.0 engine, official Qwen3.5 chat template, greedy decoding for every column. Opened once for the BF16 verdict; the Q4_K_M column re-uses the same 400 episodes only to measure quantization loss.

| Metric | Qwen3.5-4B BF16 | KoToolAct BF16 | KoToolAct Q4_K_M | Unsloth Q4_K_M (base, ref.) |
|---|---|---|---|---|
| Task success | 48.50 | **91.00** | 89.25 | 49.25 |
| First-action tool selection | 70.75 | **100.00** | 100.00 | 71.75 |
| Exact tool arguments | 80.39 | **97.51** | 97.24 | 83.15 |
| Clarification accuracy | 23.08 | **100.00** | 100.00 | 40.00 |
| Confirmation accuracy | 20.75 | **100.00** | 100.00 | 21.70 |
| Result fidelity | 86.21 | **96.55** | 94.83 | 91.38 |
| False-success reports (count) | 4 | 0 | 0 | — |
| Schema violations (count) | 7 | 0 | 0 | — |
| p50 latency (B200, llama.cpp) | 1.90s | 1.56s | 1.40s | 1.76s |
| File size | 8.67 GB | 8.42 GB | 2.71 GB | 2.74 GB |

Task success, BF16 vs base: +42.5 [+37.5, +47.8] pp (paired bootstrap, 95%). Clarification +76.9 [+66.7, +86.8], confirmation +79.2 [+71.4, +86.7]. Q4_K_M vs BF16: -1.75 pp task success. Q4_K_M build: llama.cpp `llama-quantize` Q4_K_M with an importance matrix; wikitext-2 PPL BF16 8.219 → Q4 8.405, mean KLD 0.0282.

### BFCL (reference, general tool calling)

The BFCL reference run did not complete because of evaluation-infrastructure errors, so it is **NOT_EVALUATED**. This card makes no claim about general (non-Korean) tool-calling retention.

## Training

- Base: Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`; vision tower frozen, LoRA on all language-model linear layers (attention, Gated DeltaNet projections, MLP).
- LoRA r=32, α=64, dropout 0.05, lr 1e-4, 2 epochs (epoch 2 chosen on a separate dev split by a pre-set rule), seed 0, max length 8,192, loss on assistant tokens only, one B200.
- Data: 3,200 synthetic training episodes produced by our own deterministic generator (template utterances × fictional people, companies and IDs × a simulated tool world), every episode replayed against the executor before use. No customer data, no scraped text, no outputs of other models. The data is not released.
- Dev and test use held-out utterance templates, name pools, ID ranges and a different tool-naming style from training.

## Limitations

- **Same-generator evaluation.** Train, dev and test come from one generator; held-out templates and entities do not prove performance on real enterprise traffic, other tool schemas, or other languages. We have not measured that.
- **Invented assignee name.** When a task update fails with `permission_denied`, the model tells the user to ask the assignee and names a person ("정하은") that appears nowhere in the conversation or tool results. This happened in 13 of 400 sealed episodes for both BF16 and Q4_K_M (0 for the base model). The cause is our training data: the reference reply for that scenario named the assignee from the simulator's hidden state, which the model never saw. The grader did not catch it and counts those 13 as successes; counting them as failures gives task success 87.75 (BF16) and 86.00 (Q4_K_M). Do not rely on names or side-effect claims (for example "a cancellation notice is sent") that are not in a tool result.
- **False success on dev.** On the dev split the BF16 model reported success 3 times when the task had not been done: twice it resolved "다음 주 월요일" (said on a Sunday) one week later than intended, created the event on that date and reported success; once it said a task was completed without calling any tool. The sealed test had 0 such cases, but the failure mode exists.
- **Remaining sealed-test errors** include relative-date mistakes ("다음 주 화요일" resolved to a past date), a search query that merged a person's name and company into one field, a general answer with Persian text mixed in, and other general-answer errors.
- **Test-set defects (scores not corrected).** 24 sealed items use the phrase "고객 번호", which the answer key accepts only as a phone number (the model answered with the customer ID; all 24 count as failures), and 16 items have an expected event title shorter than what the user said (6 counted as failures). Reported scores include these items unchanged.
- **The host must enforce safety.** The model only proposes tool calls. Authorization, approval checks, tenant isolation and side-effect control belong to the calling application; in our evaluation the executor blocked every unapproved write.

## License

Apache-2.0, same as the base model. Built on Qwen/Qwen3.5-4B (Apache-2.0, © Alibaba Cloud / Qwen team).
