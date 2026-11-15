---
license: other
license_name: upe-research-release-with-third-party-terms
license_link: LICENSE.md
base_model: Qwen/Qwen3.5-0.8B
base_model_relation: finetune
datasets:
- shantanugoel/universal-prompt-enhancer
language:
- en
- hi
- es
- fr
- ja
- zh
- ko
- ar
- de
- pt
tags:
- prompt-enhancement
- multimodal
- research
- qwen3_5
pipeline_tag: image-text-to-text
library_name: transformers
---

# Universal-Prompt-Enhancer-0.8B

**Built with Qwen. Improved using Qwen. Public research/evaluation release.**

A small multimodal prompt compiler fine-tuned from Qwen3.5-0.8B. It turns a rough
request and optional source image into JSON for image, video, sound, and music
generators. It produces prompts, not images, video, or audio. Quality is experimental:
valid JSON does not imply faithful preservation of intent or negative constraints.

## Examples

These are actual Q6_K outputs with greedy decoding and thinking disabled. The
model returns JSON; below we show its `rewritten_prompt` and relevant fields.
Full responses are in [release_validation.json](release_validation.json) and
[evaluation/sample_outputs.json](evaluation/sample_outputs.json).

### Text to image

**Input** (`mode: t2i`, `target: generic`):

> three red robots, square image

**Output prompt:**

> Three red robots standing in a row, square image format, studio lighting, clean background, high detail, realistic textures, 8k resolution

The JSON also contains `"aspect_ratio": "1:1"` and
`"constraints": ["three", "red"]`.

### Image editing

**Input** (`mode: edit`, `target: generic`), with a source photo of a girl boarding
a school bus:

> make the girl ginger

**Output prompt:**

> Change the girl's hair color to ginger, keeping her identity, clothing, backpack, and the school bus unchanged.

### Sound effects

**Input** (`mode: sfx`, `target: stable-audio`):

> Rain on a tin roof for 10 seconds, no thunder, no music.

**Output prompt:**

> Continuous, steady rainfall striking a corrugated tin roof. The sound features a dense, high-frequency metallic patter with sharp, bright onsets and quick decays. The texture is consistent and immersive, filling the stereo field. No thunder, no wind, no music. The acoustic environment is dry and close-mic'd, emphasizing the direct impact of water droplets on the metal surface. The intensity remains constant throughout the 10-second duration.

The JSON also contains `"duration_s": 10`.

## Supported modes

| Mode | Targets |
|---|---|
| t2i | generic, qwen-image-2.1 |
| edit | generic, qwen-image-2.1 |
| t2v | generic-video, wan2.2, hunyuanvideo-1.5 |
| i2v | generic-video, wan2.2, hunyuanvideo-1.5 |
| sfx | generic-audio, stable-audio |
| music | generic-audio, stable-audio |

Wan2.2 and HunyuanVideo-1.5 i2v conventionally produce Chinese; most other targets
produce English. Language labels in the corpus are incomplete and are not a claim
of evaluated coverage across all languages. Image input is intended for edit/i2v.

## Format

Use the exact system prompt in [student_system.txt](student_system.txt) and a user message:

```text
Mode: t2i
Target: generic
User request: three red robots holding a sign saying "HELLO", square image
```

The output keys are `rewritten_prompt` (string), `aspect_ratio` (string, empty when
unspecified), `ratio_follow` (string, commonly `"True"` or empty; not a JSON boolean),
`duration_s` (number or null), and `constraints` (list of strings). The constraints
list is a partial lexical extraction, not a complete representation of intent.
Check output before passing it to a generator.

## Training and provenance

- Base: `Qwen/Qwen3.5-0.8B`. Local weight content verified against revision `2fc06364715b967f1860aea9cf38778875588b17`;
  the original download revision was not recorded.
- Rank-16 LoRA, alpha 32, dropout 0.05; 10,822,656 trainable parameters.
  Language projections trained, vision tower frozen.
- 39,729 train / 2,271 validation / 2,184 test rows. Two epochs, 4,968 optimizer
  steps, batch 1 × accumulation 16, learning rate 1e-4 with cosine scheduling, BF16.
- Run: DGX Spark GB10; recorded software torch 2.14.1+cu130, transformers 5.18,
  peft 0.21.2. Training scripts are in `reproducibility/`; training is not rerun at release.
- Bulk teacher and A/B judge: `turboderp/Qwen3.8-Flash-Next-exl3`, revision
  `55a732e0c4c3d4614bc42b68493bb930d9b02c0a`, 4.05bpw_h6_ng6 EXL3.
- Image teachers: `Qwen/Qwen-Image-2.1-PE-T2I` at
  `f3ed7985c788ad75b3ab7223e0c4c51e2a43545b`, and PE-I2I at
  `72927bc08afc99b7888ceb7d7d51a12db3700bbd`; exact upstream teacher prompts
  were used. Teacher weights are not included.

## Evaluation and limitations

Historical base+adapter BF16 evaluation on 2,184 test records:

| Metric | Result | Denominator |
|---|---|---|
| JSON validity | 99.18% | all 2,184 rows |
| Constraint checks | 98.75% | 2,166 valid JSON rows |
| Target conventions | 97.74% | 2,166 valid JSON rows |
| All checks pass | 95.79% | all 2,184 rows |
| All checks pass, conditional | 96.58% | 2,166 valid JSON rows |

There are 18 invalid JSON records spanning
16 unique original IDs. JSON validity missed the 99.5%
goal; target conventions missed 99%. Earlier reports used 96.58% as the combined
score without emphasizing the valid-JSON denominator. The unconditional result
is 95.79%. Automatic checks are lexical heuristics; they miss
semantic reversals, some negative constraints, word counts, and translated colors.
Test records include repeated IDs. Splits have disjoint concept keys, but some
original source identities overlap; see `provenance/release_audit.json`.

A/B: 592 judged pairs of 596 attempted, randomized order. Student wins 18.07%,
teacher reference wins 68.24%, ties 13.68%. The judge is the same model as the
bulk teacher: this is not an independent evaluation. Downstream generator A/B
validation was not performed. This is a compact student, not teacher parity.

Merge verification: 99.26% top-1 agreement over 23,597 teacher-forced positions;
BF16 rounding can change long greedy generations. Historical BF16 scores above
are not a fresh full evaluation of the merged downloadable checkpoint.

Historical GGUF comparison, same 500 held-out records per arm, 768-token cap:

| Format | JSON valid | All checks | Generation tok/s | Weight size |
|---|---|---|---|---|
| BF16 GGUF | 99.2% | 98.2% | 122 | 1.52 GB |
| Q8_0 | 98.2% | 97.0% | 176 | 0.81 GB |
| Q6_K (recommended) | 98.8% | 98.0% | 197 | 0.63 GB |
| Q4_K_M | 99.4% | 97.6% | 207 | 0.53 GB |

The GGUF suite uses lexical checks and omits the separate HF convention checks;
its all-checks metric is not directly comparable with the BF16 full suite. The
small sample does not establish quantization equivalence. Speed is specific to
this machine and workload; projector is an additional 207 MB. Approximately
2–3 GB runtime memory was reported for Q6_K plus projector at 8k context.

## Actual sample behavior

Q6_K, greedy, thinking disabled (2026-10-16; raw JSON in `evaluation/sample_outputs.json`):

- **Image editing, photo provided:** “make the girl ginger” → “Change the girl's
  hair color to ginger, keeping her identity, clothing, backpack, and the school bus unchanged.”
- **Sound:** rain on tin roof, 10 seconds, no thunder/music → descriptive rainfall
  prompt with duration 10 and both exclusions preserved.
- **Failure:** Hindi sunset request → output says **sunrise**.
- **Failure:** paper boat, static camera, no people → Chinese output introduces
  background pedestrians. Duration 5 and static camera were retained.
- **Overrestriction:** piano, 80 BPM, no drums/vocals → adds **no bass**.
- **Ambiguity:** three robots holding a sign → makes each robot hold a sign.

All six samples parsed as JSON; that did not catch these semantic problems.
Use for exploratory generative-media preprocessing with human review.

## Related repositories

- [Merged model](https://huggingface.co/shantanugoel/Universal-Prompt-Enhancer-0.8B)
- [GGUFs](https://huggingface.co/shantanugoel/Universal-Prompt-Enhancer-0.8B-GGUF)
- [LoRA](https://huggingface.co/shantanugoel/Universal-Prompt-Enhancer-0.8B-LoRA)
- [Dataset](https://huggingface.co/datasets/shantanugoel/universal-prompt-enhancer)

## Licensing

See [LICENSE.md](LICENSE.md), [NOTICE](NOTICE), and `LICENSES/`. The base is
Apache-2.0; the release as a whole is not advertised as Apache-2.0. Teacher
distillation terms and MusicCaps-derived content require care. Research-only
student terms are conservative and do not imply clearance for commercial use.
This release does not claim that selecting generic targets removes obligations.

## Citation

```bibtex
@misc{goel2026universalpromptenhancer,
  author = {Goel, Shantanu},
  title = {Universal Prompt Enhancer 0.8B},
  year = {2026},
  url = {https://huggingface.co/shantanugoel/Universal-Prompt-Enhancer-0.8B}
}
```

## Run with Transformers

Install `torch`, `transformers>=5.18`, `accelerate`, `peft`, `pillow`, and
`huggingface_hub` in an environment compatible with your GPU. Public downloads
do not require authentication.

```bash
hf download shantanugoel/Universal-Prompt-Enhancer-0.8B --local-dir upe
python upe/examples/infer_transformers.py --model ./upe \
  --mode t2i --target generic --request 'three red robots, square image'
python upe/examples/infer_transformers.py --model ./upe \
  --mode edit --target generic --request 'make the hair ginger' \
  --image /path/to/source.jpg
```

The helper uses `AutoModelForImageTextToText`, the saved processor, the exact
system prompt, thinking disabled, greedy decoding, and a 4096-token output cap.
The adapter helper loads its pinned base and applies PEFT. Image requests must
include the image placeholder and actual pixels. No teacher model is needed.

## Release verification

Before publication, the release was downloaded into a separate cache and checked against
its SHA-256 manifests. Dataset records/images were checked, and downloaded
merged, adapter, and Q6_K models passed text/image inference smoke checks.
See [release_validation.json](release_validation.json) for pinned tested
revisions and outputs. These checks verify packaging and I/O, not prompt
quality, full benchmark reproduction, or public-release licensing clearance.
