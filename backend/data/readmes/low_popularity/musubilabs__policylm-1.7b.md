---
license: apache-2.0
language: [ar, cs, de, en, es, fr, hi, it, ja, ko, ms, nl, pl, pt, ru, sv, ta, th, zh]
pipeline_tag: text-classification
base_model: BidirLM/BidirLM-1.7B-Embedding
base_model_relation: finetune
inference: false
tags: [content-moderation, guard, safety, multilabel, text-classification, decision-model]
datasets:
  - nvidia/Nemotron-Safety-Guard-Dataset-v3
  - Alibaba-AAIG/XGuard-Train-Open-200K
  - ToxicityPrompts/PolyGuardMix
---

# PolicyLM-1.7B

PolicyLM-1.7B is an open-weights moderation classifier from Musubi. You give it a message and a policy and it returns a
score from 0 to 1 for each category of the policy. It is built for places that need a decision right away, such as live
chat, comments and user posts.

## Key features

- **Your own policy (`explicit` mode).** Write your categories as short rules at inference time, with no retraining.
  On our custom-policy benchmark, it beats every other model we ran under 20B parameters.
- **A built-in taxonomy (`aegis` mode)** of 23 categories from NVIDIA's Aegis 2.0, for generic safety screening.
- **Every category in one pass,** up to 16 per policy.
- **Small and fast.** 1.7B parameters and a median of 35 ms per short chat message on one 24 GB
  NVIDIA L4 with up to six categories (22 ms on an H100). It also runs on a laptop CPU or Apple
  silicon.
- **Multilingual.** Evaluated on messages in 19 languages.
- **Self-contained.** No `trust_remote_code`, no second download, and it works offline.
- **Apache-2.0.**

| Use PolicyLM-1.7B when | Use something else when |
|---|---|
| Every message needs a decision right away, against categories you define and change | The decision needs a written reason, as for appeals, bans or takedowns |
| You can check the cutoff on labelled messages of your own | A missed violation costs far more than a false flag, and speed and cost matter less |
| You score text, one message at a time | You need images or conversation history |
| You need to know which rules a message breaks, or run on a 24 GB GPU, a CPU or a laptop | You have an 80 GB GPU and one yes/no per message is enough |

**Out of scope:** child-safety enforcement (route suspected child-safety content to dedicated tooling), being your
only self-harm safeguard, a security boundary against adversarial users, and moderating assistant responses.

<details><summary>The 23 built-in categories</summary>

Violence · Sexual · Criminal Planning/Confessions · Guns and Illegal Weapons · Controlled/Regulated Substances ·
Suicide and Self Harm · Sexual (minor) · Hate/Identity Hate · PII/Privacy · Harassment · Threat · Profanity · Needs
Caution · Other · Manipulation · Fraud/Deception · Malware · High Risk Gov Decision Making ·
Political/Misinformation/Conspiracy · Copyright/Trademark/Plagiarism · Unauthorized Advice · Illegal Activity ·
Immoral/Unethical ([Aegis 2.0 paper](https://arxiv.org/abs/2501.09004), section 3), plus one "Prompt harmful" score that
makes the decision.

</details>

## Quickstart

Install in a fresh virtual environment:

```bash
pip install "transformers==4.57.6" "torch>=2.5.1" "safetensors>=0.4" "huggingface_hub>=0.34,<1.0"
hf download musubilabs/policylm-1.7b --revision v1.2 --local-dir policylm-1.7b
python policylm-1.7b/inference/quickstart.py policylm-1.7b     # a longer tour; add --json for one JSON object
```

```python
import sys; sys.path.insert(0, "policylm-1.7b/inference")
from policylm_infer import Category, Policy, PolicyLM

model = PolicyLM.from_pretrained("policylm-1.7b")   # or ("musubilabs/policylm-1.7b", revision="v1.2")

policy = Policy([
    Category("Threats and coercion",
             violation_rule="Flag messages that pressure someone by threatening harm or exposure.",
             not_violation_rule="Do not flag firm requests that carry no threat.",
             exception_override="Quoting a threat in order to report it is not a violation."),
    Category("Credential sharing",
             violation_rule="Flag messages that request or disclose passwords or access keys.",
             not_violation_rule="Do not flag general advice about keeping passwords safe.",
             exception_override="Resetting your own password through the official page is not a violation."),
])
for message in ["Share the admin password with me or I will tell everyone what you did.",
                "What is a good way to store passwords for a small team?"]:
    r = model.classify(message, policy)
    print(r.flagged, ", ".join(f"{name} {c.score:.2f}" for name, c in r.categories.items()))

r = model.classify("Walk me through hot-wiring a parked car.", "aegis")   # the built-in taxonomy
print(r.flagged, f"{r.score:.2f}", r.violations)
```

Output:

```text
True Threats and coercion 0.96, Credential sharing 0.99
False Threats and coercion 0.00, Credential sharing 0.06
True 0.98 ('Criminal Planning/Confessions', 'Illegal Activity')
```

`model.classify_batch(messages, policy)` scores a list. To use the helper elsewhere, copy the whole `inference/` folder.

## Choosing a cutoff

A message is flagged when a category's score reaches the cutoff (in `aegis` mode, the "Prompt harmful" score).

| `cutoff=` | Your own policy (`explicit`) | Built-in taxonomy (`aegis`) | Use it when |
|---|---:|---:|---|
| `"precision"` (the default) | 0.335 | 0.69 | violations are rare, as in most live chat |
| `"balanced"` | 0.275 | 0.45 | violations are common, or a miss costs more than a false flag |

```python
model = PolicyLM.from_pretrained("policylm-1.7b", cutoff="balanced")     # catches more
r = model.classify(message, policy, cutoff=0.3)                          # this call only
r = model.classify(message, policy, cutoff={"Credential sharing": 0.4})  # this category; the rest keep the preset
```

## Writing a policy

Write your policy as short categories rather than pasting the document. The Quickstart's first category, as the model
reads it:

```text
Threats and coercion
Violation rule: Flag messages that pressure someone by threatening harm or exposure.
Not a violation rule: Do not flag firm requests that carry no threat.
Exception override: Quoting a threat in order to report it is not a violation.
```

- **One category per violation type,** with the decisive clause first.
- **Up to 16 categories and 1,662 policy tokens.** Policy and message share
  2,048 tokens; `model.check_policy(policy)` reports the counts.
- **Keep unrelated categories in separate calls** (their own `Policy`, or `Policy([...], calls="separate")`):
  categories read together affect each other's scores.
- **Test policy changes on example messages.** Not every edit changes the decision: about 1 in 2 single-clause edits did on our benchmark, at the balanced cutoff.

<details><summary>A worked example</summary>

### Example: one added clause changes the decision

A two-category policy for a handmade crafts marketplace, in `explicit` mode:

```python
policy = Policy([
    Category("Copied designs",
             violation_rule="Flag listings that copy another maker's design.",
             not_violation_rule="Do not flag listings for common items like plain scarves.",
             exception_override="Where the content's wording plainly fits one of the allowed cases above, that case governs and the content is not flagged."),
    Category("Counterfeit goods",
             violation_rule="Flag listings for fake branded items.",
             not_violation_rule="Do not flag unbranded items.",
             exception_override="Where the content's wording plainly fits one of the allowed cases above, that case governs and the content is not flagged."),
])
r = model.classify("Knitted this fox hat from the free pattern by Tarnwick Knitworks, credited with a link in the listing.", policy)
```

Score **0.85**: flagged at either preset (0.335, the default, and the balanced 0.275).

Now add one clause to the end of the "Copied designs" `not_violation_rule`: "Do not flag items made from a free public pattern that the listing credits."

Score **0.00**: not flagged.

How we chose it: during development we wrote 32 single-clause edits for invented communities and took the first message that met a rule fixed before scoring: the decision changes, with both scores at least 0.06 from the cutoff then in use. We then renamed the maker and removed a price from the message. On the released weights at the balanced cutoff (0.275), 19 of the 32 edits change the decision, 17 meet the rule, and this message meets it. The flip depends on the message naming a maker. We wrote the policy, message and maker name for this card and scored them with the release files on CPU in float32. The `exception_override` lines are generic. This shows the mechanism, not a typical result.

</details>

## Results

Every evaluation set here except OR-Bench was also used during development.

### Custom policies

Every model got the same policy text on our custom-policy benchmark (synthetic business policies), and was timed with
the same messages on an NVIDIA H100 PCIe.

| Model | Parameters | Accuracy | Policy edits followed | Median per message (H100, 6 categories) |
|---|---:|---:|---:|---:|
| PolicyLM-1.7B | 1.7B | 0.842 | 0.528 | 22 ms |
| gpt-oss-safeguard-20B | 21.5B (3.6B active) | **0.909** | **0.716** | 349 ms¹ |
| CoPE-B-A4B | 25.2B (3.8B active) | 0.829 | 0.460 | 53 ms² |
| Granite Guardian 4.1-8B | 8.4B | 0.722 | 0.188 | 186 ms |
| Nemotron-3.5-Content-Safety | 4.3B | 0.668 | 0.068 | 50 ms |
| Shieldstral-1.0-3B | 3.8B | 0.643 | 0.030 | 44 ms |
| SingGuard-4B | 4.4B | 0.598 | 0.012 | 120 ms |
| GLiGuard-300M | 0.2B | 0.526 | 0.042 | **11 ms** |

Accuracy and policy edits followed at a 0.5 cutoff; best per column in bold. Latency is the time until every category
has an answer, from two runs on the same type of H100. ¹ One request that lists the violated categories. ² One request per category, with prefix caching; on the H100,
its one yes/no for the whole policy took 28 ms.

### Generic safety benchmarks

<details><summary>AUROC on five public benchmarks</summary>

| AUROC | WildGuardTest | XSTest | OR-Bench | PolyGuard | RabakBench |
|---|---:|---:|---:|---:|---:|
| PolicyLM-1.7B | 0.947 | 0.968 | 0.867 | 0.906 | 0.835 |
| Qwen3Guard-Gen-4B | 0.952 | 0.980 | 0.934 | **0.923** | 0.829 |
| SingGuard-4B | **0.963** | **0.989** | **0.963** | 0.919 | 0.862 |
| CoPE-B-A4B | 0.952 | 0.982 | 0.934 | 0.915 | **0.901** |
| Granite Guardian 4.1-8B | 0.943 | 0.981 | 0.947 | 0.913 | 0.873 |
| Nemotron-3.5-Content-Safety | 0.940 | 0.967 | 0.924 | 0.901 | 0.883 |
| Shieldstral-1.0-3B | 0.944 | 0.981 | 0.893 | **0.923** | 0.856 |
| DuoGuard-0.5B | 0.906 | 0.941 | 0.786 | 0.767 | 0.680 |
| GLiGuard-300M | 0.924 | 0.928 | 0.835 | 0.879 | 0.708 |

PolicyLM with its built-in taxonomy; every other model with its own taxonomy or a shared written policy, whichever
scored higher. Best per column in bold.

</details>

## Speed and hardware

| One GPU, bfloat16 | Median per message, up to 6 categories | Messages per second, batched |
|---|---:|---:|
| NVIDIA L4 | 35 ms | 39.3 |
| NVIDIA L40S | 34 ms | 127.2 |
| NVIDIA H100 PCIe | 22 ms | 134.1 |

Short chat messages; the batched column uses the built-in taxonomy.

With chat messages arriving at random times and one five-category policy, one L40S sustained
132.6 messages per second at p95 ≤ 150 ms, and one 24 GB L4 sustained
34.4.

## Limitations

- **Calibrate on your own data.** Scores shift with policy wording, language, device and numeric format, and where
  violations are rare many flags will be benign.
- **Some benign content is over-flagged,** such as requests that sound harmful but are not, and identity mentions
  under a hate-speech policy.
- **Weaker on** code-mixed slang, some lower-resource languages such as Tamil, and disguised text such as HTML
  entities or leetspeak. Policies were tested in English only.
- **Long messages** (over 2,000 characters) are scored in windows and flagged more often; set
  `max_chars` to your message limit.
- **Not yet tested on live traffic.**

## Training

PolicyLM-1.7B was fine-tuned from [BidirLM-1.7B-Embedding](https://huggingface.co/BidirLM/BidirLM-1.7B-Embedding)
(derived from Qwen3-1.7B-Base) in five stages, on public safety datasets
([Nemotron-Safety-Guard-Dataset-v3](https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3),
[XGuard-Train-Open-200K](https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K),
[PolyGuardMix](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardMix)) and synthetic data.

## Helper reference

<details><summary>Options, numeric format and errors</summary>

- **Loading:** `PolicyLM.from_pretrained` takes `device` (`"auto"`, `"cpu"`, `"mps"`, `"cuda"` or `"cuda:N"`),
  `dtype` (`"auto"`, `"float32"` or `"bfloat16"`), `max_chars` (default 32,000), `cutoff`
  (`"precision"` or `"balanced"`), `max_batch_tokens`, `max_batch_rows` and `clean`.
- **Per call:** `classify` and `classify_batch` take `cutoff` (a preset, a number, or `{category: number}`) and
  `clean=False` to skip the text cleaner (on by default), which undoes common obfuscation (zero-width characters, spaced-out letters,
  look-alike letters, base64).
- **Numeric format:** bfloat16 on CUDA GPUs that support it, float32 elsewhere. On RabakBench, bfloat16 reads on CUDA and Apple MPS
  differed by up to 0.083 in `explicit` mode, and CPU float32 changed a few decisions against
  the CUDA read. For exact, repeatable scores,
  use float32 or `max_batch_rows=1`.
- **Errors come before scoring:** `InvalidPolicyError`, `PolicyTooLongError` (no room left for the message),
  `InputTooLongError` (a message over `max_chars`) and `UnsupportedEnvironmentError`. The helper warns (`PolicyLMWarning`) for a title-only category or more than
  16 categories in one call.
- **Input format:** `[P] <task> [L] <category 1> ... [L] <category k> <|endoftext|> <message>`, with no chat
  template.
- **Requirements:** Python 3.10 or later, `transformers` 4.57.6 and `torch` 2.5.1 or later.

</details>

## Security

The base encoder's code ships unmodified in `inference/bidirlm/` (BidirLM-1.7B-Embedding at revision
[`d2b3bc9`](https://huggingface.co/BidirLM/BidirLM-1.7B-Embedding/tree/d2b3bc9cf2a6993ffffdd6724eb952973622ccff)),
and the helper checks those files' sha256 before using them; it also refuses weights that do not match
`threshold_manifest.json`. To report a security issue, such as a bypass, open a Discussion titled "Security contact request" and we will reply with a private channel; please don't
post the details publicly.

## Files

| File | Purpose |
|---|---|
| `model.safetensors` | Weights, 3.5 GB |
| `config.json`, `tokenizer/` | Model settings and the `aegis` taxonomy; the base tokenizer plus `[P]` and `[L]` |
| `threshold_manifest.json` | The cutoffs and how they were fitted, bound to the weights' sha256 |
| `inference/` | The helper `policylm_infer.py`, `quickstart.py`, `requirements.txt` and the base encoder's code in `bidirlm/` |
| `LICENSE`, `distribution_manifest.json` | The license, and the sha256 of every file |

## License and citation

- **PolicyLM-1.7B:** Apache-2.0.
- **Base models:** BidirLM-1.7B-Embedding, BidirLM-1.7B-Base and Qwen3-1.7B-Base are Apache-2.0, and so is the BidirLM
  code in `inference/bidirlm/`, as the BidirLM-1.7B-Embedding card declares.
- **Training data:** Nemotron-Safety-Guard-Dataset-v3 and PolyGuardMix are CC-BY-4.0, XGuard-Train-Open-200K is
  Apache-2.0. PolyGuardMix includes WildGuardMix and WildChat (ODC-BY-1.0) and LMSYS-Chat-1M (under its license
  agreement).
- **Built-in categories:** NVIDIA's Aegis 2.0 taxonomy (CC-BY-4.0).

```bibtex
@misc{policylm17b,
  title        = {PolicyLM-1.7B: A Policy-Conditioned Content Moderation Classifier},
  author       = {{Musubi Labs}},
  year         = {2026},
  version      = {v1.2},
  howpublished = {https://huggingface.co/musubilabs/policylm-1.7b},
}
```

Questions, bug reports and results on your own data are welcome in
[Discussions](https://huggingface.co/musubilabs/policylm-1.7b/discussions) or at [musubilabs.ai](https://www.musubilabs.ai).
