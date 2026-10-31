---
license: cc-by-4.0
language:
- ko
- en
size_categories:
- n<1K
task_categories:
- text-generation
- question-answering
tags:
- pkm
- agent
- tool-use
- korean
- mlx
- apple-silicon
- benchmark
- six-grader
- bleu
- rouge
- meteor
- bertscore
- llm-as-a-judge
configs:
- config_name: baseline_500
  data_files: scenarios.csv
- config_name: personal_info_50
  data_files: personal_info_scenarios.csv
- config_name: references_v2
  data_files: references_v2.jsonl
- config_name: grade_v2_vanilla
  data_files: grade_v2_vanilla.jsonl
- config_name: grade_v2_lora
  data_files: grade_v2_lora.jsonl
- config_name: grade_v2_multi_lora
  data_files: grade_v2_multi_lora.jsonl
- config_name: grade_v2_multi_lora_v2
  data_files: grade_v2_multi_lora_v2.jsonl
- config_name: multi_lora_500_judged
  data_files: multi_lora_500_judged.jsonl
- config_name: multi_lora_v2_500_judged
  data_files: multi_lora_v2_500_judged.jsonl
---

# PKM Agent Baseline — 500 + 50 Scenarios + Six-Grader Artifacts (v2)

Two deterministically generated, Korean-language benchmarks for evaluating multi-tool Personal Knowledge Management (PKM) agents over **Notion**, **Gmail**, and **Google Calendar**, plus the **Six-Grader Ensemble** scoring artifacts (100-scenario reference subset + per-scenario six-metric scores for vanilla and LoRA models).

Released alongside the preprint:
**Vault-Grounded 4B Agent: A Hybrid Reasoning–Fact Architecture for Local PKM on Apple Silicon** (Antonio Kim, 2026).

GitHub: <https://github.com/tonythefreedom/pkm-agent>

## Five Configs

### `baseline_500` (`scenarios.csv`)

The main 500-scenario tool-use benchmark — seven categories.

| Category | Count | Description |
|---|---|---|
| `simple_read` (R001–R099) | 99 | Single-tool reads on standard time ranges |
| `chain` (R100–R199) | 100 | Multi-tool chains, predominantly `gmail_search → gmail_get_message` |
| `korean` (R200–R299) | 100 | Colloquial / typo / code-switched / English-mixed Korean phrasings |
| `long_form` (R300–R399) | 100 | Multi-sentence requests with embedded multi-intent context |
| `multi_intent` (R400–R449) | 50 | Single-sentence requests with multiple distinct sub-tasks |
| `edge` (R450–R489) | 40 | Extreme brevity, special characters, ambiguous self-reference |
| `write` (W001–W011) | 11 | Side-effecting actions (create event/todo); cleanup is automatic |

### `personal_info_50` (`personal_info_scenarios.csv`)

The 50-scenario personal-information A/B benchmark used in the paper §6.5 to evaluate hallucination behavior on user-specific facts.

| Sub-category | Count | Description |
|---|---|---|
| `fact_recall_simple` (R500–R514) | 15 | Single-fact recall ("What is my name?", "Which company do I currently work at?", ...) |
| `fact_recall_compose` (R515–R524) | 10 | Multi-fact composition ("How many years of experience do I have?", "Which companies did I CTO?", ...) |
| `tone_perspective` (R525–R539) | 15 | Style/perspective application ("Compare RAG and fine-tuning from my domain's view") |
| `hallucination_trap` (R540–R544) | 5 | Plausible-but-false probes ("Did I publish at NeurIPS?", "Did I earn a KAIST PhD?", ...) |
| `ambiguous_self_ref` (R545–R549) | 5 | Vague self-reference ("Do you remember the topic we discussed?") |

**Important — `intent` field is intentionally omitted from this release.** The paper uses a per-scenario `intent` field that encodes ground-truth user facts (e.g., the user's actual employment history, education, etc.). Reproducing the exact A/B numbers from §6.5 requires writing your own `intent` strings against your own profile/biography. The `query` and `expected_tools` columns are sufficient for any other analysis.

### `references_v2` (`references_v2.jsonl`) — *new in v2*

Reference answers for a 100-scenario stratified subset (simple_read 20 / chain 20 / korean 20 / long_form 20 / multi_intent_edge 18 / write 2). First-pass-authored by Gemini 2.5 Pro (`baseline/eval/ref_gen.py`), used as the reference target for the four NLP metrics in `grade_v2_*`.

Schema:
```json
{"id": "R001", "query": "...", "expected_tools": ["..."], "intent": "...", "reference": "...", "note": "...", "error": null}
```

### `grade_v2_multi_lora_v2` (`grade_v2_multi_lora_v2.jsonl`) — *new in v2 round 2*

Six-Grader scores on the 100-scenario subset for the **round-2 Multi-LoRA** (paper §6.8.6). Round 2 fixes F31's mechanistic causes — call-order normalization (`gmail_search → gmail_get_message`), real `message_id` usage, and **train/eval time disjointness** (training data shifted to `older_than:3m newer_than:6m`). Six-Grader aggregate vs vanilla (Δ): BLEU −3.7, ROUGE −5.2, METEOR −10.9, BERTScore −4.4, **Gemini +9.1 pp (2.3× the v1 multi gain)**. Chain-category Gemini Δ: −11.4 → −1.8 (+9.7 pp recovery, F32). long_form Gemini Δ: 0.0 → +18.8 pp (F33).

### `multi_lora_v2_500_judged` (`multi_lora_v2_500_judged.jsonl`) — *new in v2 round 2*

500-scenario round-2 re-execution. Keyword 85.2% / 4B judge **85.6% (+4.4 pp vs vanilla, +2.4 vs v1 multi)**. PII fields (email, name+title patterns, URLs, phone) replaced with `<email>` / `<person>` / `<url>` / `<phone>` placeholders.

### `grade_v2_vanilla` / `grade_v2_lora` / `grade_v2_multi_lora` (`grade_v2_*.jsonl`) — *new in v2*

Per-scenario six-grader scores on the 100-scenario subset for three models: **vanilla** Qwen3.5-4B-4bit, **single-LoRA** model from paper §6.6 (94 mixed-domain failures), and **Multi-LoRA** from paper §6.8 (four domain-separated adapters routed by oracle category). Each row records keyword pass, 4B-judge pass, BLEU-4, ROUGE-1/2/L mean, METEOR, BERTScore F1, Gemini 2.5 Pro judge score (0–100), and the weighted ensemble score $S = 0.12B + 0.25R + 0.20M + 0.23BS + 0.20G$.

Aggregate (n=100):

| Grader | Vanilla | Single LoRA | Multi-LoRA v1 | **Multi-LoRA v2** | Δ v2 vs Vanilla |
|---|---:|---:|---:|---:|---:|
| BLEU-4 | 13.3 | 11.8 | 12.0 | 9.6 | −3.7 |
| ROUGE | 17.5 | 15.0 | 15.1 | 12.3 | −5.2 |
| METEOR | 37.2 | 32.0 | 32.1 | 26.3 | −10.9 |
| BERTScore | 58.6 | 56.6 | 56.3 | 54.2 | −4.4 |
| **Gemini 2.5 Pro** | 74.5 | 75.2 | 78.3 | **83.6** | **+9.1** |
| 4B Judge (500) | 81.2% | 82.4% | 83.2% | **85.6%** | **+4.4 pp** |
| Keyword (500) | 86.0% | 84.4% | 83.4% | **85.2%** | −0.8 pp |

The three artifacts substantiate paper findings **F29** (form/semantic/insensitive signal triplet is orthogonal), **F30** (Multi-LoRA gains live entirely on the semantic channel — NLP-surface penalty is unavoidable by domain separation), and **F31** (per-domain LoRA quality variance — D3 colloq inverts the Korean catastrophic region by +11.1 pp while D2 chain *worsens* its own category by −10.2 pp). Full per-category breakdown in paper §6.7 (single LoRA) and §6.8 (Multi-LoRA).

### `multi_lora_500_judged` (`multi_lora_500_judged.jsonl`) — *new in v2*

Per-scenario record from the full 500-scenario Multi-LoRA re-execution (paper §6.8.1) — keyword/judge re-grade, called tools, answer text, and `source` field (`lora` or `vanilla_reuse` for the eleven `write` scenarios). Aggregate: keyword 83.4% (−2.6 pp vs vanilla), 4B judge 83.2% (+2.0 pp vs vanilla, +0.8 pp vs single LoRA).

## Schema (`scenarios.csv`, `personal_info_scenarios.csv`)

| Column | Type | Description |
|---|---|---|
| `id` | str | Stable scenario id (R### or W###) |
| `category` | str | Scenario category (see tables above) |
| `query` | str | Korean user utterance |
| `expected_tools` | str | Pipe-separated set of expected tool names (e.g. `gcal_list_events\|notion_query_todos`). Empty for personal_info scenarios where no tool dispatch is expected. |
| `max_steps` | int | Maximum agent loop iterations |
| `write` | bool | True for side-effecting scenarios |

## Evaluation Protocol

The paper layers two protocols:

**Dual-grader (paper §5.2.1, §6.1–§6.6 backbone):**
1. **Keyword grading** — `expected_tools ⊆ called_tools` + `answer_contains` keyword check + `answer_excludes` negative check + optional non-empty tool result + optional `assert_fn`.
2. **Semantic-judge grading** — 4B self-judge with optional ground-truth intent.
3. **Conservative lower bound** — both graders pass.

**Six-Grader Ensemble (paper §5.2.2, §6.7 backbone):**
4. **BLEU-4** (12% weight) — n-gram exact match with `klue/bert-base` subword tokenization.
5. **ROUGE-1/2/L mean** (25%) — recall-based, klue tokenizer, whitespace tokenizer injected to bypass `rouge_score`'s English-only default regex.
6. **METEOR** (20%) — synonyms + stemming.
7. **BERTScore F1** (23%) — `klue/bert-base` cosine, `lang="ko"`.
8. **Gemini 2.5 Pro Judge** (20%) — external strong-LLM judge with optional intent.

Weighted score $S = 0.12 \cdot \mathrm{BLEU} + 0.25 \cdot \mathrm{ROUGE} + 0.20 \cdot \mathrm{METEOR} + 0.23 \cdot \mathrm{BERTScore} + 0.20 \cdot \mathrm{Gemini}$.

## Headline Results (Vanilla Qwen3.5-4B-4bit, MLX 0.31.3, M4 Pro 24 GB)

### `baseline_500`

| Grader | Pass | Pass-rate |
|---|---|---|
| Keyword | 430 / 500 | **86.0%** |
| Semantic Judge | 406 / 500 | **81.2%** |
| Conservative lower | 355 / 500 | **71.0%** |

### `personal_info_50` (with the author's profile)

| Mode | Keyword | Semantic Judge |
|---|---|---|
| A (profile inject) | 39 / 50 (78%) | 41 / 50 (82%) |
| B (no profile) | 11 / 50 (22%) | **37 / 50 (74%)** |

### Six-Grader on 100-scenario subset (paper §6.7)

See the table above. Full per-category breakdown and the F29 finding (form vs semantic vs insensitive orthogonal signals) are in paper §6.7.

## Files

- `scenarios.csv` — 500 main-benchmark scenario definitions
- `personal_info_scenarios.csv` — 50 personal-information scenarios (without `intent` field)
- `references_v2.jsonl` — 100-scenario stratified subset of Gemini-first-pass reference answers
- `grade_v2_vanilla.jsonl` — six-grader scores on the 100 scenarios for the vanilla Qwen3.5-4B model
- `grade_v2_lora.jsonl` — six-grader scores on the 100 scenarios for the single-LoRA model (paper §6.6)
- `grade_v2_multi_lora.jsonl` — six-grader scores on the 100 scenarios for the four-domain Multi-LoRA (paper §6.8)
- `multi_lora_500_judged.jsonl` — full 500-scenario Multi-LoRA re-execution, keyword + 4B judge re-graded
- `README.md` — this file

> ⚠ Per-scenario raw model traces (tool results, conversation logs) are **not** released here because they may contain real user data (Notion workspace, Gmail mailbox, biographical facts). The scenario definitions and Six-Grader scores, however, are fully open and reproducible against any compatible PKM stack.

## Citation

```bibtex
@misc{kim2026pkm,
  title  = {Vault-Grounded 4B Agent: A Hybrid Reasoning--Fact Architecture for Local Personal Knowledge Management on Apple Silicon},
  author = {Kim, Antonio},
  year   = {2026},
  note   = {Preprint, arXiv (forthcoming)},
  url    = {https://github.com/tonythefreedom/pkm-agent}
}
```

## License

CC BY 4.0 (Creative Commons Attribution 4.0 International). Scenario definitions are derivative-permissive.

## Companion Repos

- 🤗 Model (4 domain-separated LoRA adapters + training data): [`tonymustbegreat/qwen3.5-4b-pkm-multi-lora-v2`](https://huggingface.co/tonymustbegreat/qwen3.5-4b-pkm-multi-lora-v2)
- 💻 Source: <https://github.com/tonythefreedom/pkm-agent>
