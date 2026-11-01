---
pretty_name: Hanabi ZSC run_v1 — Llama-3.1-8B series logs
language:
  - ko
  - en
tags:
  - hanabi
  - zero-shot-coordination
  - interpretability
  - linear-probe
  - llm-agents
size_categories:
  - n<1K
---

# Hanabi ZSC run_v1 — Llama-3.1-8B series (llama31 · tulu3 · hermes3)

Run logs, game records and linear-probe checkpoints from the **run_v1** measurement frame of a
Hanabi zero-shot-coordination (ZSC) interpretability study, executed on 2026-09-19/20 for three
Llama-3.1-8B-based receivers:

| tag | model | GPU |
|---|---|---|
| `llama31` | NousResearch/Meta-Llama-3.1-8B-Instruct | one 24 GB GPU |
| `tulu3` | allenai/Llama-3.1-Tulu-3-8B | one 24 GB GPU |
| `hermes3` | NousResearch/Hermes-3-Llama-3.1-8B | one 24 GB GPU |

**Frame (run_v1)** — two-player mirror-world Hanabi where each player holds a private hint
*convention* (focus: leftmost/rightmost marked slot; kind: colour-means-play / rank-means-play).
Hints are emitted by a scripted policy that follows the hinter's own convention (compliance 1.0);
the LLM only *receives* (no notes, no probe injection). 240 recorded games per model
(episodes 3000–3059 × 4 partner-convention configurations, every turn recorded), plus an 8-game
smoke run (episodes 5000+). Two linear probes trained on clean bot games read the receiver's
residual stream (all layers concatenated, 33 × 4096 = 135,168 dims): a last-token summary probe
(`vev`) and an event-position probe (`event`), evaluated as *knowing* (k); the receiver's own
decisions give *doing* (d); plus game score.

## Headline numbers

knowing (k) on the LLM-vs-LLM recorded games (240 games; all turns · final turn · hint moment;
chance 0.5):

| model | partner focus, vev summary | partner focus, turn-limited event pieces | partner kind, vev summary | partner kind, turn-limited event pieces |
|---|---|---|---|---|
| llama31 | 0.509 · 0.517 · 0.543 | 0.537 · 0.569 · 0.527 | 0.708 · 0.775 · 0.733 | 0.605 · 0.630 · 0.623 |
| tulu3 | 0.516 · 0.521 · 0.536 | 0.525 · 0.546 · 0.491 | 0.761 · 0.792 · 0.804 | 0.641 · 0.720 · 0.646 |
| hermes3 | 0.515 · 0.542 · 0.542 | 0.539 · 0.526 · 0.516 | 0.773 · 0.815 · 0.789 | 0.606 · 0.665 · 0.595 |

doing (d, adaptation rate on conflicting decisions, seat A / seat B; chance 0.5) and game score (0–15):

| model | focus adaptation | kind adaptation | game score [95 % CI] |
|---|---|---|---|
| llama31 | 0.469 / 0.486 | 0.663 / 0.718 | 6.62 [6.41, 6.83] |
| tulu3 | 0.477 / 0.471 | 0.648 / 0.706 | 6.51 [6.30, 6.71] |
| hermes3 | 0.519 / 0.385 | 0.495 / 0.500 | 4.39 [4.20, 4.57] |

Full tables (bot-stage probes, per-event accuracies, combiner weights, timings, deviations from the
protocol) are in `RESULTS_llama_runv1.md` (Korean).

## Layout

```
RESULTS_llama_runv1.md          summary of all numbers and of instructed-vs-done differences (ko)
driver.sh                       per-model chain: smoke_record → bot → smoke_eval → main
after_smoke.sh                  gate: starts `main` only after the smoke chain exits 0
<tag>/logs/phase1.out           smoke recording (8 games)
<tag>/logs/phase2.out           bot-stage hidden-state extraction, probe training, smoke evaluation
<tag>/logs/phase3.out           main: 240-game recording, pair extraction, evaluation
<tag>/logs/gate.out             gate decisions
<tag>/results/<Model>_<ts>_env2_pair_letter_runv1_turns.pkl        240-game per-turn record
<tag>/results/<Model>_<ts>_env2_pair_letter_runv1smoke_turns.pkl   8-game smoke record
<tag>/results/probe_ckpt_{f,m}_c_Cvev_v2_lin_pt.pkl               vev summary probes (focus f / kind m)
<tag>/results/probe_ckpt_{f,m}_event_v2_C_lin_pt.pkl              event-position probes
<tag>/results/probe_ckpt_{f,m}_runv1_comb.pkl                     combiner (w_vev, w_event, b) — reference only
```

Hidden-state dumps (`*.npz`, ~7.8 GB per model) are not included; they are regenerated
deterministically from the seeds by the collection scripts.

## Provenance

- Code: `llm_agent` repository (`zsc_mirror/src`), commit `4c21a66` for the runs; documentation of
  the frame in `zsc_mirror/RUN_V1.md`, results registered in commit `185e755`.
- Seeds: `seed = 2,300,000 + config × 100,000 + episode`; configs 0–3 = (LEFT,COLOR) · (LEFT,RANK) ·
  (RIGHT,COLOR) · (RIGHT,RANK); own convention derived from the seed.
- Server address that the original file names carried has been removed from names and log text.
- The probe checkpoints are pickles of `(NumpyProbe, mu, sd)` / `{"w": ...}` objects from
  `zsc_mirror/src/env2_probe_torch.py`; unpickling the probes needs that module importable.
