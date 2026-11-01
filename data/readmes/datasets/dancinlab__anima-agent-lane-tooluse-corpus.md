---
license: apache-2.0
language: [en, fr, de, es, ko]
tags: [byte-level, tool-use, agent, anima, consciousness-lm, grounding]
task_categories: [text-generation]
---

# anima-agent-lane-tooluse-corpus

Agent-lane tool-USE demo corpus for [anima](https://github.com/dancinlab/anima)'s
rung-0 tool-use grounding fire (design §6/§7). It teaches the byte-LM mouth the
sentinel tool-call **grammar** (`0xFE fact_lookup KEY 0xFF`, vocab256-safe dead-UTF-8
delimiters) + grounding **behaviour** — NOT tool facts/trivia. Deterministic, $0.

## two register variants (the key finding)

- **`agent_lane_chatreg.txt`** (1,060,800 B) — grammar taught IN the `사용자:/도우미:`
  chat register. This is the variant that delivered the **🟢 F-TOOLUSE-FABDROP
  terminal PASS** (fabrication 0.5556 → 0.0).
- **`agent_lane_5lang_disjoint.txt`** (980,880 B) — grammar in a plain-prose register
  DISJOINT from the chat turn. Closed-negative: the grammar was learned but stayed
  siloed and did NOT transfer to the chat surface (FABDROP FAIL). **Lesson: teach the
  grammar in the same register it will fire in.**

## shape distribution (each variant)

a/b/c/d balanced 1200 each (needs-tool · no-tool-needed · don't-know-call · tier-too-low-refuse).
Hard invariants (re-verified): `fabricated_result_count == 0`, sentinels balanced
(0xFE=0xFF=3600), all non-frame bytes valid UTF-8, philosophy grep (`[role:`/`[persona:`/
`[character:`/`[assistant:`/`[system:`) == 0. Held-out probe values appear in NEITHER
variant (falsifier leak guard).

## philosophy (p1..p8 — HELD)

The `0xFE`/`0xFF` are LEARNED grammar bytes, NOT identity injection. NO system prompt /
persona / role / RLHF. sha256 manifest: `SHA256SUMS.txt`.

Scope (a_scale_honest_scope): TOY 18M rung corpus; mid/7B transfer UNVERIFIED.
