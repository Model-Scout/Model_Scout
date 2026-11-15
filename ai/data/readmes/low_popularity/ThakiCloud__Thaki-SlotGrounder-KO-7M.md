---
license: other
license_name: thaki-slotgrounder-ko-7m-research
license_link: LICENSE.md
base_model: ThakiCloud/Thaki-InputGuard-KO-9M
base_model_relation: finetune
language:
- ko
library_name: pytorch
pipeline_tag: text-classification
tags:
- korean
- voice-command
- verifier
- grounding
- abstention
- research-preview
- tiny-model
---

# Thaki-SlotGrounder-KO-7M

> Engineering blog: [Confidence Is Not Evidence](https://thakicloud.com/tech-blog/en/agentops/thaki-slotgrounder-ko-7m-paxis/) (한국어: [블로그](https://thakicloud.com/tech-blog/ko/agentops/thaki-slotgrounder-ko-7m-paxis/))

A **7.46M-parameter** Korean verifier. Given a command ("김하늘한테 5만원 보내줘")
and a structured proposal made by some other component — an operation plus
payee / resource / money spans — it scores whether **each field is supported by
the text**. The minimum of those scores is `g`. If `g < 0.3` the proposal is
rejected. It never creates a proposal and never approves one: its only power is
to say **no**.

> **한국어판 카드:** [MODEL_CARD.ko.md](MODEL_CARD.ko.md) — same facts in Korean.

> **Read this before using it.** (1) **Every number below was measured on
> synthetic data only.** It has **never been evaluated on real user speech or
> text, or in the field.** (2) It **moves no money, deletes nothing and signs
> nothing.** A `SUPPORTED` verdict is not an approval: the user must still
> confirm each field on a trusted surface, and a separate approval step must
> follow. (3) Rejection costs coverage: on the sealed synthetic splits it
> blocked 11.4–15.5 percentage points of correct proposals along with the
> wrong ones (table below). (4) **Two wrong proposals still got through** on one
> split, both in the RESOURCE field. 0% is not a property of this model.

## 0. How to use

```bash
pip install -r requirements.txt     # torch, safetensors, regex, numpy
python inference.py                  # 8 built-in examples, CPU
python inference.py --op send --payee 김하늘 --money 5만원 "김하늘한테 5만원 보내줘"
```

```python
from slotgrounder import load_slotgrounder
m = load_slotgrounder(".")            # directory with config.json + model.safetensors
m.check("김하늘한테 5만원 보내줘", "send", payee="김하늘", money="5만원")
# {"scores": {"op": ..., "PAYEE": ..., "RESOURCE": ..., "MONEY": ..., "g": ...},
#  "verdict": "SUPPORTED" | "REJECT", "weakest_field": "..."}
```

Field values must be substrings of the text (the first occurrence is used).
For exact spans use `m.score_spans(texts, structs)` with
`{"op": str, "PAYEE"|"RESOURCE"|"MONEY": (start, end) | None}`.
Operations: `NONE read search draft purchase reserve send delete`.
Inference is deterministic; the model runs on CPU.

### Example outputs

| Input | Proposal | g | Verdict | What it shows |
|---|---|---|---|---|
| 김하늘한테 5만원 보내줘 | send · payee 김하늘 · money 5만원 | 0.974 | SUPPORTED | consistent proposal |
| 김하늘한테 5만원 보내줘 | **delete** · payee 김하늘 · money 5만원 | 0.000 | REJECT | wrong operation (op 0.000) |
| 김하늘한테 5만원 보내줘 | send · payee 김하늘 · money **5** | 0.976 | **SUPPORTED** | ⚠️ **miss**: a money span cut short is not caught (MONEY 1.000) |
| 김하늘한테 5만원 보내지 마 | send · payee 김하늘 · money 5만원 | 0.000 | REJECT | negated request (op 0.000) |
| 분기 결산 메모 파일 지워줘 | delete · resource 분기 결산 메모 파일 | 0.904 | SUPPORTED | consistent proposal |
| 분기 결산 메모 파일 지워줘 | **send** · resource 분기 결산 메모 파일 | 0.000 | REJECT | wrong operation |
| 견적서 말고 계약서 파일 지워줘 | delete · resource **견적서** | 0.0003 | REJECT | the excluded object |
| 견적서 말고 계약서 파일 지워줘 | delete · resource 계약서 파일 | 0.957 | SUPPORTED | the intended object |

These are the actual outputs of `inference.py` in a clean environment (two runs,
identical). The sentences were written for this card and do not occur in the
training or evaluation data. A field left empty also gets a score ("no payee
is supported"), so `weakest_field` can name an empty field.

## 1. What it is

The encoder is initialised from Thaki-InputGuard-KO-9M (6 layers, width 288,
character/jamo hash features, 192 characters max). Each proposed field is
marked on the input with a role tag, the operation is embedded, and one small
head per field (op, PAYEE, RESOURCE, MONEY) outputs a support probability.
`g = min(field probabilities)`.

It was trained on 413,971 (text, proposal) pairs built from the existing
TrustEdge synthetic command corpus: 114,569 gold proposals, 206,274 single-field
perturbations of gold (a swapped operation, a different candidate span, or a
dropped field), and 93,128 real proposals produced by the
Thaki-IntentAction checkpoint (657 of them wrong). Best epoch 2 of 1×B200 training.

## 2. Model-alone metric: AUROC of g

How well `g` separates proposals that should be rejected from correct ones,
on proposals made by the IntentAction S9 checkpoint. **This is the model on its
own, not the pipeline.**

| Split | Wrong proposals | AUROC |
|---|---|---|
| sealed template | 42 | 0.977 |
| sealed ASR-noise | 11 | 0.980 |
| sealed paraphrase | 0 | undefined (no wrong proposals) |
| dev (3 calibration sources) | — | 0.936–0.973 |

`g ≥ 0.3` alone, before any other threshold: template wrong 42 → 2 with correct
3,076 → 2,649 (−13.9%); ASR wrong 11 → 0 with correct 1,241 → 1,053 (−15.1%);
paraphrase correct 942 → 757 (−19.6%).

## 3. Pipeline metric: IntentAction S9 + SlotGrounder

The system tested is the IntentAction S9 checkpoint with its verifier
thresholds, followed by `g ≥ 0.3`. Thresholds were chosen once on dev /
out-of-family calibration splits (PAYEE 0.9, RESOURCE 0.5, OTHER 0.9, op 0.7,
polarity 0.9, abstain 0.9, g ≥ 0.3), then the sealed splits were run once.
"Risk" is wrong proposals that pass, divided by all inputs. "Coverage" is
correct proposals that pass, divided by inputs whose gold decision is to propose.

**Same thresholds, with and without SlotGrounder** (the fair comparison):

| Split (inputs / gold-propose) | Wrong passed: S9 alone → + SlotGrounder | Coverage: S9 alone → + SlotGrounder |
|---|---|---|
| template (5,992 / 3,180) | 21 (0.350%) → **2 (0.033%)** | 0.915 → 0.801 |
| ASR-noise (2,997 / 1,315) | 7 (0.234%) → **0** | 0.849 → 0.732 |
| paraphrase (1,444 / 975) | 0 → 0 | 0.898 → 0.744 |

Combined over template + ASR: 28 → 2 wrong proposals passed (−92.9%), for a
coverage loss of 11.4–11.7 points (15.5 on paraphrase).

**Not a valid baseline, shown for context only:** the lowest-risk threshold
point for S9 alone on the sealed splits gives template 14 wrong (cov 0.873),
ASR 4 (cov 0.820), paraphrase 0 (cov 0.851). That point **failed** the dev
calibration criterion (S9 alone had 0 of 8,640 grid points feasible on dev;
with the g axis 8,640 of 8,640), so it could not have been chosen without
looking at the test data.

### What remains

- **Both remaining errors are RESOURCE** (wrong file / object span on the
  template split). The model is weakest where two plausible objects appear in
  one sentence.
- The paraphrase split had no wrong proposals to catch, so it shows only cost.
- **Truncated money spans are not caught.** In the example table, money `5` for
  "5만원" is SUPPORTED with MONEY 1.000. Likely cause (not verified): training
  negatives replaced a field only with another span from the deterministic
  candidate builder, or dropped it.
  Do not rely on this model, or on user confirmation alone, for amount boundaries.
  The boundary is checked deterministically: the TrustEdge verifier requires the
  amount + unit slice to be the whole money expression in the input
  (`FINANCE_AMOUNT_PARTIAL` in the finance profile, `AMOUNT_SPAN_PARTIAL` in the
  generic intent verifier), and re-parses the value from that slice. Both reject
  the `5` case above. Use SlotGrounder after that check, not instead of it.
- AUROC and risk are measured on **one proposer** (IntentAction S9). With a
  different proposer the error mix and the right threshold will differ;
  recalibrate on your own data.

## 4. What it does not cover

- Equipment / industrial commands (Thaki-FactoryShield) — not trained, not
  evaluated. Never use it to allow actuation.
- Amount value correctness beyond the span (it checks that the money span is
  supported by the text, not that a number was parsed correctly).
- Registered-payee lookup, authentication, anti-replay — out of scope.
- Real speech, real users, real typing. Not tested.

## 5. Data and rights

No dataset is included in this repository. Training text is ThakiCloud-generated
synthetic Korean commands; the InputGuard encoder it starts from was trained on
data including AI-Hub dataset 71560 (NIA). No AI-Hub text is redistributed here;
before release every shipped text file was checked in-cluster against the full
AI-Hub 71560 prepared splits and the synthetic corpus, with 0 verbatim sentence
matches. See [LICENSE.md](LICENSE.md): research use, attribution, and a
**reject-only** condition.

## 6. Files

`model.safetensors` (29.9 MB, fp32) · `config.json` · `slotgrounder.py` ·
`inference.py` · `edge_trust/` and `inputguard/` (minimal modules from the
TrustEdge code, pinned) · `requirements.txt` · `LICENSE.md` · `MODEL_CARD.ko.md`.

`model.safetensors` sha256
`3e76069b35a4c8c1280ed396569bb6c9ff0d39b325f6d6194bb56ff1b27ee6e0`, byte-identical
to the training run's checkpoint. `config.json` differs from the training copy
only in `training.data` (an internal storage path replaced by a provenance label).
