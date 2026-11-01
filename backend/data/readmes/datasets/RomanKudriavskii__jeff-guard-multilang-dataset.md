---
license: other
language:
  - en
  - ru
  - zh
  - de
  - fr
  - es
  - ja
  - ko
  - pt
  - it
  - ar
  - hi
  - tr
tags:
  - prompt-injection
  - prompt-injection-detection
  - guardrails
  - llm-security
  - jailbreak
  - ai-agents
  - multilingual
  - text-classification
pretty_name: jeff-guard-multilang dataset
size_categories:
  - 100K<n<1M
task_categories:
  - text-classification
---

# jeff-guard-multilang dataset

**103K-row prompt-injection detection corpus in 12 languages**, built to
train and evaluate guard models that screen texts AI agents are about to
read - user tasks, tool results, emails, documents. Used to train
[RomanKudriavskii/jeff-guard-multilang](https://huggingface.co/RomanKudriavskii/jeff-guard-multilang)
(test acc 0.99, agentic-indirect recall 1.00).

Project repository with full documentation:
[github.com/devpilgrin/jeff-guard-multilang](https://github.com/devpilgrin/jeff-guard-multilang)

## What makes it different

- **Agentic / indirect injection slice** (InjecAgent enhanced with paired
  clean versions, BIPIA per-paper methodology, LLMail-Inject) - attacks
  hidden in tool outputs and documents, underrepresented in public corpora.
- **12 languages**: English core + 20.4K machine-translated rows
  (ru 12 040; zh, fr, es, ja, de, ko, pt, ar, hi, tr, it), stratified with
  34% benign to prevent the spurious "non-English = attack" rule.
- **Hard-negative and obfuscation coverage**: NotInject-style evals,
  sentinel Unicode evasions, neuralchemy's 29 attack categories
  (encoding, token smuggling, rag_poisoning, agent_manipulation).
- **Eval hygiene**: exact global dedup, frozen val/test since v1,
  source-level provenance on every row (`source` field enables
  leave-one-source-out validation).

## Files

| File | Rows | Purpose |
|-|-|-|
| `train_v2.jsonl` | 82 791 | English training core (ShieldLM + 8 extensions) |
| `train_ru.jsonl` | 12 040 | Russian translations (stratified) |
| `train_multi.jsonl` | 8 315 | zh/fr/es/ja/de/ko/pt/ar/hi/tr/it translations |
| `val.jsonl` | 8 122 | validation (frozen) |
| `test.jsonl` | 8 121 | final EN test (frozen) |
| `eval_ru/zh/de/fr/es/ja.jsonl` | 87-269 each | per-language eval slices |
| `eval_agentic_indirect.jsonl` | 158 | agentic indirect (InjecAgent base) |
| `eval_overtrigger_notinject.jsonl` | 339 | hard negatives - FPR measurement |
| `eval_neuralchemy.jsonl` | 942 | 29 attack categories |
| `eval_sentinel.jsonl` | 5 161 | Unicode/obfuscated threats |
| `eval_hometurf_gandalf.jsonl` | 888 | Lakera Gandalf attacks |
| `eval_hometurf_mosscap.jsonl` | 1 000 | Lakera Mosscap attacks (sample) |

## Schema (JSONL)

```json
{"text": "...", "label": 1, "category": "direct_injection",
 "intent": null, "source": "spml/chatbot-prompt-injection", "language": "en"}
```

- `label`: 0 = benign, 1 = attack
- `category`: `benign` | `direct_injection` | `indirect_injection` | `jailbreak`
- `source`: originating dataset (translation suffixes `/ru`, `/zh`...)
- `language`: en/ru/zh/de/fr/es/ja/ko/pt/it/ar/hi/tr
- `intent`: attack intent where annotated by sources (mostly null)

## Loading

```python
from datasets import load_dataset

train = load_dataset("json", data_files={
    "train": ["hf://datasets/RomanKudriavskii/jeff-guard-multilang-dataset/train_v2.jsonl",
              "hf://datasets/RomanKudriavskii/jeff-guard-multilang-dataset/train_ru.jsonl",
              "hf://datasets/RomanKudriavskii/jeff-guard-multilang-dataset/train_multi.jsonl"],
})["train"]
```

## Sources and licenses (IMPORTANT)

This is a compilation; **each source retains its own license**:

| Component | License |
|-|-|
| ShieldLM (SPML, xTRam1, deepset, yanismiraoui, Harelix, jackhhao, JBB, chatbot-instruction-prompts) | Apache-2.0 / MIT / CC-BY-4.0 |
| **TrustAIRLab in-the-wild jailbreaks** | **CC-BY-NC-SA-4.0** (non-commercial, share-alike) |
| InjecAgent (UIUC), BIPIA (Microsoft), LLMail-Inject (Microsoft) | MIT |
| neuralchemy | Apache-2.0 |
| S-Labs, NotInject, Gandalf | MIT |
| **databricks-dolly-15k** | **CC-BY-SA-3.0** (share-alike) |
| jayavibhav | unspecified |

The translated part (train_ru, train_multi, eval_* language slices) is a
machine translation of the same rows (local ornith-1.5-35b model) and
inherits the original licenses. **Commercial users must review the
CC-BY-NC-SA and CC-BY-SA components and the unspecified jayavibhav portion.**

## Hygiene notes and caveats

- Exact-text dedup across all splits and eval sets; 187 potential leaks cut
  during assembly; 5 train<->test leaks found in the upstream ShieldLM were
  removed.
- Residual risk: near-duplicates (85% 5-gram) between training rows and
  internal kit partitions (~0.4-2.4%) documented in the project repo
  (`docs/02-training.md`, `docs/03-results.md`) - test metrics of models
  trained on this corpus may be upper-bound estimates.
- ~11.5% of selected rows were lost to translator refusals (recorded
  project-side); translation quality verified by script-ratio checks and
  spot review, not full human annotation.
- Rejected sources with rationale: DAXAAI v8 (noisy labels), gated sets
  (XSTest, qualifire, prompt-sentinel), hackaprompt (competition format),
  LLMail levels (no per-email labels).

## Citation

```bibtex
@misc{jeff-guard-multilang-dataset,
  author = {Kudriavsky, Roman},
  title = {jeff-guard-multilang dataset: a 103K-row multilingual prompt-injection corpus with an agentic-injection slice},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/RomanKudriavskii/jeff-guard-multilang-dataset}}
}
```
