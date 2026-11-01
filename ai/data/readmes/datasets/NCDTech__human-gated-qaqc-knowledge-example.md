---
license: cc-by-4.0
language:
  - ko
  - en
tags:
  - qa-qc
  - human-in-the-loop
  - knowledge-management
  - audit-trail
  - on-premise-llm
  - anomaly-detection
  - predictive-maintenance
  - industrial
pretty_name: Human-Gated QA/QC Knowledge Records (Format Example)
---

# Human-Gated QA/QC Knowledge Records: Format Example

![NCDTech 4-layer stack](assets/01_four_layer_stack.png)

**This is a format demonstration, not real operational data.**

All records here are synthetic examples that show the data structures we use in our self QA/QC + on-premise LLM reporting system.

Our system lets operators chat with a local LLM about inspection reports.

Useful conversations become knowledge, but only under administrator approval, and every approved record keeps its full revision history.

Code-based verdicts are never overwritten; agreements about a verdict are stored as annotations next to it.

Three record kinds are shown:

| file | kind | what it shows |
|------|------|---------------|
| `verdict_records.jsonl` | 📐 verdict agreement | how a verdict annotation is recorded, approved, and revised without ever changing the verdict itself |
| `knowledge_records.jsonl` | 📌 raw / 🧠 summary | how a conversation becomes pending knowledge, then official after approval |
| `faq_records.jsonl` | FAQ | how approved knowledge is promoted to a FAQ entry |

How the records in this dataset are produced, from development to operation (development-time QA/QC + FAQ seeding, then the operation loop with the administrator approval gate):

![Development and operation loop](assets/02_dev_and_ops_loop.png)

These are the real screens that produce such records.

All three are frames from our [demo video (22 min, Korean)](https://youtu.be/ftsw_vbfw6E), where the whole loop runs live on a GPU 8GB PC without internet.

Recording a verdict agreement (the source of `verdict_records.jsonl`): the checklist has flagged an issue, and the agreement text is being written **next to** the verdict it annotates, never over it:

![Recording a verdict agreement in the real UI](assets/04_real_ui_stage1.png)

Capturing a conversation as pending knowledge (the source of `knowledge_records.jsonl`): the operator asks why the robot drives in short segments, the local LLM answers citing the stage report as its basis, and the red button ends the capture and saves it for administrator review:

![Capturing a conversation as knowledge in the real UI](assets/05_real_ui_knowledge_capture.png)

The administrator review dialog, the approval gate itself: a pending record is read in full, then accepted into official knowledge, rejected, or revised as a new revision.

Nothing reaches the LLM context until this step:

![The administrator approval gate in the real UI](assets/06_real_ui_admin_approval.png)

Why a conversational layer at all: what code-only inspection cannot do, and the role split between the two layers:

![Why the LLM layer](assets/03_why_llm_and_growth.png)

*(Diagrams are in Korean; they are the same figures used on our website and demo video.)*

## Design rules the format encodes

1. **Verdict immutability.** A record of kind `verdict` annotates a check; it has no
   power to change the check's status. The `check` field names the target; the status
   lives elsewhere, in code.
2. **Approval gate.** `status` moves `pending → accepted` only by an administrator
   action. Nothing is injected into the LLM context while pending.
3. **Append-only revisions.** `revisions[0]` is immutable. Edits append new entries
   with `rev`, `by`, `at`, `note`. There is no delete operation in the API. When a
   record is cited, its revision count is disclosed (e.g. "제3판" = 3rd revision).

## Where this fits: our 4-layer stack

Our systems are built as four layers. This dataset shows the records produced by the
top two.

| layer | what it is | status |
|-------|-----------|--------|
| 1. Embedded measurement & control | our roots: smart monitoring and control, 24 years | in production |
| 2. Edge neural networks | verified through the 8-stage physics simulation workflow of our robot simulation studio | verified in-house |
| 3. Self QA/QC reports | code-based inspections wired into every stage, traffic-light verdicts | **records shown here** |
| 4. Conversational LLM reporting | on-premise LLM that explains those reports and grows under administrator approval | **records shown here** |

We now focus this stack on predictive maintenance (PdM) for aging mechanical equipment.

The record formats shown here are the ones that PdM reporting will use: verdicts staying in code, knowledge growing only through the approval gate, and every record keeping its full revision history.

## 한국어

이 데이터셋은 실데이터가 아니라 **형식 시연용 가상 예제**입니다.

저희 셀프 QA/QC + 온프레미스 LLM 리포팅 시스템이 쓰는 기록 구조 세 가지(판정 합의 · 지식 기록 · FAQ)를 보여줍니다.

핵심 규칙: 판정 불변(합의는 주석일 뿐), 관리자 승인 게이트, append-only 개정 이력(1판 영구 보존, 삭제 API 없음, 인용 시 판수 고지).

저희 시스템은 4계층으로 쌓습니다: ①임베디드 계측·제어(뿌리) ②엣지 신경망(로봇 시뮬레이션 스튜디오의 8단계 물리 시뮬레이션으로 검증) ③셀프 QA/QC 리포트 ④대화형 LLM 리포팅(관리자 승인 아래 성장).

**이 데이터셋의 기록들이 바로 계층 ③·④가 남기는 기록**입니다.

저희는 이 스택을 노후 기계식 설비의 예지보전(PdM)에 집중하고 있고, 예지보전 리포팅도 바로 이 기록 형식(판정은 코드에·지식은 승인 게이트로만·전체 개정 이력 보존)을 씁니다.

Learn more: https://huggingface.co/NCDTech · https://ncdtech.org · Demo video: https://youtu.be/ftsw_vbfw6E
