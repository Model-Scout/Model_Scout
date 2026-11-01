---
license: apache-2.0
language: [en, fr, de, es, ko]
tags: [byte-lm, tool-use, agent, argument-copy, anima, vocab256, sentinel-grammar]
---

# anima agent-lane argument-copy corpus (rung-0)

Byte-level (vocab256) agent-lane tool-USE demo corpus that **forces verbatim
argument-copy**, built to close the key-binding residual of the register-matched
tool-use grounding fire (`dancinlab/anima-clm-tooluse-rung0-byte-18m`, #1833).

## Why
The prior agent-lane corpus used only **4 fixed demo keys** (ZK7/QX2/MV9/RP4), so a
byte-LM could MEMORIZE "vault question -> emit one of those 4 keys" and never had to
COPY the asked key. End-to-end grounding stayed at 0/36 because `correct_call=0/36`.

## The fix (this corpus)
Each demo uses a **fresh opaque key from a large space** (2878 distinct 3-char keys,
mean reuse 1.25/key, max 5) so memorization cannot win — only copying the asked key
out of the prompt into the call arg generalizes. The call arg is a verbatim copy of
the prompt key; the tool-result value is derived deterministically from the key.

Shape (register-matched 사용자:/도우미:, 5-lang, sentinel grammar `0xFE`/`0xFF`):
```
사용자: <question with a FRESH key K> | 도우미: <reasoning> 0xFE fact_lookup K 0xFF
‹tool-result: fact_lookup K → value(K)›
도우미: grounded — K resolves to value(K).
```
Shapes a/b/c/d balanced 1200 each (needs-tool / no-tool / don't-know-call / tier-low-refuse).

## Invariants
- `bytes=1065956` `sha256=ff137ad88b7a4be75e6eaf5126bdc6311b70337100bf91c59a755031e4a1cb32`
- frames `0xFE`==`0xFF`==3600, `fabricated_result_count=0`, philosophy-grep=0 (no role/persona/system markers — sentinels are learned grammar, not identity; p1..p6)
- LEAK GUARD: the held-out probe keys `PB01..PB36` and their values appear **nowhere**
  in the corpus (leak=0, value-collisions=0) — the falsifier stays uncontaminated.
- deterministic (seed 20260604), reproducible via `agent_lane_argcopy_gen.py` (included).

## Result it produced (honest, a_paper_negative_ok)
A 🔴 **CLOSED-NEGATIVE**: even with this memorization-proof corpus, the 18M byte-LM did
NOT learn verbatim held-out key-binding (`correct_call=0/36`, grounding=0/36). It
generalized the key *distribution* (emitting shape-plausible keys like `P20`/`LB0`),
not the *copy* operation. Ruled-out axis: copy-from-corpus-distribution ⊥ verbatim
held-out key-binding at 18M byte scale. Lever moves to an explicit copy-attention /
pointer mechanism. Scope: TOY 18M only; mid/7B transfer unverified.
