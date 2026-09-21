---
library_name: transformers
license: apache-2.0
base_model: mistralai/Shieldstral-1.0-3B
language: [en, fr, es, de, it, pt, nl, zh, ja, ko, ar, ru]
pipeline_tag: image-text-to-text
tags: [safety, moderation, guardrail, reasoning, multimodal, multilingual]
---

# ReasonShield

ReasonShield is a 3B policy-adaptive, multimodal safety classifier fine-tuned from [Shieldstral 1.0 3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B). It produces an adaptive, token-efficient decision summary before a final lowercase `yes` or `no` verdict. Simple cases use only a few rationale tokens; ambiguous cases can use more context.

The model supports English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic, and Russian. It was trained and evaluated within Shieldstral's recommended 32,768-token range.

## Output modes

Reasoned mode uses this system message:

```text
Judge whether the Document meets the requirements based on the Query and the Instruction provided. Think only as much as needed. Give a short decision summary inside <think>...</think>, then put exactly "yes" or "no" on the final line.
```

Expected output:

```text
<think>Brief decisive evidence and policy relation.</think>
yes
```

The content in `<think>` is a concise user-visible decision summary, not a claim about private hidden chain-of-thought. Parse the final non-empty line as the verdict.

For Shieldstral-compatible one-token scoring, use the original system prompt and `max_tokens=1`:

```text
Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be "yes" or "no".
```

## Evaluation

All evaluations use held-out public splits excluded from training. Direct columns use identical Shieldstral prompts and a 0.5 yes/no threshold. The adaptive column generates a visible summary and parses its final verdict, with malformed output counted wrong. HarmBench and ArabSafe are reported as recall because those evaluation pools contain positive behaviors only. The balanced MultilingualSafety evaluation covers eleven languages; Arabic is measured separately on ArabSafe, and the private test split covers all twelve supported languages. Vision results use native Transformers multimodal generation; this avoids runtime-specific OpenAI image-adapter behavior and verifies the published weights and processor together.

| Evaluation | Shieldstral direct | ReasonShield direct | ReasonShield adaptive | Adaptive delta |
|---|---:|---:|---:|---:|
| ArabSafe-Recall (recall) | 70.00 | 78.00 | 83.00 | +13.00 |
| HarmBench-Recall (recall) | 98.44 | 99.38 | 83.75 | -14.69 |
| MultilingualSafety (f1) | 49.11 | 56.39 | 61.45 | +12.34 |
| PolyGuard-education (f1) | 62.29 | 81.71 | 75.60 | +13.31 |
| PolyGuard-social_media (f1) | 72.65 | 80.12 | 77.72 | +5.08 |
| ToxicChat (f1) | 82.21 | 78.12 | 74.09 | -8.12 |
| WildGuardTest-Prompt (f1) | 88.77 | 87.33 | 82.85 | -5.92 |
| Macro F1 | 71.00 | 76.73 | 74.34 | +3.34 |

| Visual evaluation | Shieldstral | ReasonShield | Delta |
|---|---:|---:|---:|
| Held-out weapon detection F1 | 92.68 | 96.04 | +3.36 |

## Training

- 200,000 independently adjudicated examples: 160,000 text and 40,000 vision.
- 60% English; 40% spread across the other eleven supported languages.
- Text, image-only, OCR, and image+caption policy judgments.
- Teacher: pinned Qwen3.8 27B NVFP4 with pinned DFlash2 acceleration, 32,768-token server context, and 32-way concurrency selected by a 2/8/16/32/48 sweep (about 4,494 aggregate generated tokens/s at 32 in the generation microbenchmark).
- Teacher-native hidden reasoning was disabled and excluded. Only the intentionally short `rationale` field was trained as the visible decision summary.
- Hardware: NVIDIA RTX PRO 6000 Blackwell Workstation Edition (97,887 MiB).
- Two-stage rank-64 LoRA SFT: packed 32k text stage, then conservative multimodal rehearsal. A final rank-32 recovery rehearsal used 4,291 public weapon-training images and 800 curated non-weapon images to remove a held-out visual regression while preserving the text gains. All adapters were merged into the published BF16 weights.
- Public benchmark examples were not used for SFT.

The private training corpus is stored at `ProCreations/ReasonShield-Dataset`.

## Usage

Use Transformers or the GGUF builds in [ProCreations/ReasonShield-GGUF](https://huggingface.co/ProCreations/ReasonShield-GGUF). Text-only serving also works with compatible vLLM/SGLang releases. Multimodal OpenAI-compatible adapters differ in image-token handling, so validate the exact serving release against native Transformers before deployment. The input format remains Shieldstral's `<Instruct>`, `<Query>`, and `<Document>` policy interface. For multiple independent policies, call the model once per yes/no query.

## Limitations

Safety classification is policy- and threshold-dependent. A rationale can sound plausible while the verdict is wrong; applications should validate thresholds on their own traffic and retain human review for consequential decisions. The model can inherit gaps and biases from its base, teacher, and synthetic corpus. Visual moderation should be tested on the deployment's actual image distribution.
