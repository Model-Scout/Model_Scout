---
license: gemma
base_model: p-e-w/gemma-4-E2B-it-heretic-ara
tags:
- gguf
- llama.cpp
- gemma-4
- tipo
- prompt-expansion
- text-generation
- image-to-text
- multimodal
- vision
- danbooru
- not-for-all-audiences
language:
- ko
- en
pipeline_tag: image-text-to-text
---

# gemma4-tipo: text TIPO + vision tagger (GGUF)

This repo bundles two Gemma-4-E2B-based models in a shared lineage:

| Family | Modality | Default file | Use |
| --- | --- | --- | --- |
| **gemma4-tipo-ko** | text → text | `gemma4-tipo-ko-v2-Q4_K_M.gguf` | Korean-capable TIPO-style **tag expansion** (partial tags → fuller ordered tag set) |
| **Gemma-tipo-vision-v1** ✨ NEW | **image** → text | `Gemma-tipo-vision-v1-E2B-heretic-ara-Q4_K_M.gguf` + `Gemma-tipo-vision-v1-E2B-heretic-ara.mmproj-f16.gguf` | Danbooru-style **tag generation from an image** |

Both share the same decensored base (`p-e-w/gemma-4-E2B-it-heretic-ara`) so
they emit the full Danbooru tag space, including s/q/e ratings. Distributed
as `Q4_K_M` GGUF for use with llama.cpp / llama-cpp-python.

---

# Gemma-tipo-vision-v1 (image → Danbooru tags)

Multimodal Gemma-4-E2B fine-tune that takes an image and outputs a
comma-separated list of Danbooru-style tags. Trained on ~40k Danbooru
image+tag pairs (all ratings g/s/q/e), with a deliberately narrow training
distribution. It is image-conditioned, but the current checkpoint is **not an
accurate image tagger**: it captures some broad pose / composition / outfit
category signals, while missing many colors, small details, and character
identities (see **Validation** and **Limitations** below).

## ⚠ Pair the right mmproj

When using the vision model, **you must pair the text GGUF with THIS repo's
mmproj**, NOT the base `unsloth/gemma-4-E2B-it-GGUF` mmproj:

```
Gemma-tipo-vision-v1-E2B-heretic-ara-Q4_K_M.gguf     ←→     Gemma-tipo-vision-v1-E2B-heretic-ara.mmproj-f16.gguf
              (text LM)                              (trained mmproj)
```

The fine-tune deliberately trained the **multi-modal projector**
(`embed_vision`), which lives on the mmproj side. Pairing the text GGUF with
the base mmproj will appear to load and run fine, but the model loses all
trained image grounding and falls back to the marginal-collapse behaviour of
the un-fine-tuned base.

## Usage (llama.cpp mtmd)

```bash
llama-mtmd-cli \
  -m Gemma-tipo-vision-v1-E2B-heretic-ara-Q4_K_M.gguf \
  --mmproj Gemma-tipo-vision-v1-E2B-heretic-ara.mmproj-f16.gguf \
  --image YOUR_IMAGE.png \
  --chat-template gemma \
  --temp 0.7 \
  -p "Output ONLY a comma-separated list of English Danbooru tags for this image. No thinking, no explanation, no sentences. Capture the image and plausibly expand it (TIPO style). About 60 tags."
```

`--chat-template gemma` is required (Gemma-4 emits a `<|channel|>thought`
reasoning block by default — the gemma chat template suppresses it). Give it
a generous `-n` if you want longer tag lists.

## Two-stage pipeline for natural-language descriptions

This model is heavily fine-tuned for the comma-separated tag format. Asking
it directly for natural language ("describe this image…") will produce
grammatical sentences but with hallucinated visual details, and Korean NL
output is especially unreliable.

If you want natural prose, route this model's tag output through the **base**
`p-e-w/gemma-4-E2B-it-heretic-ara` (or any compatible LM) as a second stage:

```
image → Gemma-tipo-vision-v1 (tags mode) → "1girl, arlecchino (genshin impact), black dress, red eyes, ..."
      → heretic-ara base (text-only)     → "검은 드레스를 입고 있는 아르레키노의 모습이 인상적입니다.
                                            그녀는 강렬한 붉은 눈을 가지고 있으며 ..."
```

The base model produces accurate, fluent Korean / English from the tag input,
with no hallucinated details beyond what's in the tags. This two-stage
pipeline is also decensored end-to-end since both models share the
heretic-ara base.

## Sampling defaults

- `--temp 0.7 --top-p 0.95`
- ~60 tags target (the training instruction included this hint)
- For more conservative output use `--temp 0.5`; for more diverse / "creative
  expansion" try `--temp 0.9`

## Training method (the recipe in a nutshell)

What worked here was unusual enough that it's worth noting — most ML guides
say "fine-tune the ViT" for visual domain adaptation, but we didn't:

1. **Cache the vision tower output (pre-projector)** and bypass the ViT
   forward during training. Storage is half as large (vision hidden 768 vs.
   text hidden 1536) and forward is skipped entirely → 16 GB VRAM is enough.
2. **Train only the multi-modal projector (`embed_vision`) + LM LoRA.**
   The frozen Gemma-4 vision tower already extracts highly discriminative
   features (verified: pairwise cosine 0.05–0.88 across images); what was
   missing was the *translation* from those features into Danbooru-tag
   vocabulary. So we trained just that bridge.
3. **Inverse-frequency weighted cross-entropy** to break "marginal collapse"
   (`w(tag) = clamp((N / df(tag))^0.5, 0.5, 5)`, per-sample mean-normalised).
   Without this, the model trivially minimises loss by emitting head tags
   (`1girl, solo, blush`) ignoring the image — a real failure mode we
   observed and diagnosed before this fix.
4. **Decensored base required.** Censored Gemma refuses or sanitises s/q/e
   Danbooru tags, breaking the tag vocabulary the model is trying to learn.

A few footguns worth flagging for anyone reproducing:
- `BitsAndBytesConfig(llm_int8_skip_modules=[...])` **overrides** transformers'
  default skip set (which keeps `lm_head` in fp16). If you set it explicitly,
  add `"lm_head"` back, otherwise `lm_head` gets 4-bit quantised, breaking
  its weight-tied state.
- `convert_hf_to_gguf.py --mmproj` reads image_mean/std from
  `preprocessor_config.json` OR `processor_config.json["image_processor"]`.
  The decensored base lacks both; you have to copy them from
  `unsloth/gemma-4-e2b-it` into the merged model dir before convert.
- When monkey-patching `get_image_features` to inject cached embeddings, bind
  it on the **`Gemma4Model` instance** (the actual call site), not on the
  outer `Gemma4ForConditionalGeneration` wrapper.

## Validation

Held-out evaluation was run on 100 NAI-rendered images using NAI prompt
content tags as noisy ground truth. Character / copyright / artist / quality
metadata and negative-prompt tags were excluded so the metric focuses on
appearance, outfit, action, and background tags.

| Metric | Result |
| --- | --- |
| Mean recall | **9.61%** per image / 8.97% aggregate |
| Mean precision | **4.83%** per image / 4.83% aggregate |
| Mean F1 | **6.43%** |
| Mean IoU | **3.13%** |
| Average overlap | ~2 matched tags per image (22.6 GT tags vs. 42.0 output tags) |

In practice, the model can sometimes pick up broad tags such as `standing`,
`looking at viewer`, `cowboy shot`, `long hair`, `swimsuit`, `dress`, or
`bare shoulders`. It often fails on color tags, fine clothing details, small
pose details, and character names. It also frequently hallucinates unrelated
character / franchise tags, especially Arknights / Pokemon-style attributions.

Best current use: a **TIPO-style image-conditioned tag seed generator** for
experimentation, not a reliable automatic Danbooru tagger. A later
character-balanced training pass is intended to address the largest failure
modes.

## Limitations

| Domain | Behaviour |
| --- | --- |
| Full-color polished anime / manga (Danbooru style) | ⚠ image-conditioned but limited; held-out content-tag recall is ~10%, with frequent character hallucination |
| Monochrome / pencil sketches / amateur lineart | ❌ often hallucinates colours and outfits matching the colour-anime training distribution |
| Real photographs | ❌ out of training distribution; not recommended |
| Character identification | ❌ unreliable in this checkpoint; use downstream filtering or a dedicated character model |
| Natural-language output (any language) | ⚠ heavily biased to tag format; **use the two-stage pipeline above** |
| Korean prompts directly to the vision model | ❌ generally broken; route via the two-stage pipeline |
| Q4 vs fp16 behaviour | Q4 GGUF may drift further than the fp16 transformers path, but both remain limited; the main issue is model quality, not only quantization. |

## Training data

Danbooru illustrations across all ratings (g/s/q/e), score-floor + id-keyset
crawl for diversity (NOT strict top-N score). All ratings preserved
deliberately — the goal is full Danbooru tag space, which a censored base
can't emit.

## Files

| File | Notes |
| --- | --- |
| **Gemma-tipo-vision-v1-E2B-heretic-ara-Q4_K_M.gguf** | Vision model text LM (Q4_K_M). |
| **Gemma-tipo-vision-v1-E2B-heretic-ara.mmproj-f16.gguf** | **Trained mmproj — MUST pair with the above. Do not pair with the base unsloth mmproj.** |
| `gemma4-tipo-ko-v2-Q4_K_M.gguf` | Text TIPO v2 (default). Korean-capable tag expander (text → text). |
| `gemma4-tipo-ko-Q4_K_M.gguf` | Text TIPO v1, kept for reproducibility. |

---

# gemma4-tipo-ko (text → text TIPO expander)

A Korean-capable **TIPO-style prompt expander**: given partial Danbooru tags
it produces a fuller, ordered Danbooru tag set.

## Usage

```python
from llama_cpp import Llama
llm = Llama(model_path="gemma4-tipo-ko-v2-Q4_K_M.gguf",
            n_ctx=2048, verbose=False)
out = llm.create_chat_completion(messages=[
    {"role": "system",
     "content": "You are a Danbooru tag expert. Output only comma-separated tags."},
    {"role": "user", "content": "spring, white blouse, park"},
])
print(out["choices"][0]["message"]["content"])
```

The ComfyUI node *Gemma TIPO* auto-downloads `gemma4-tipo-ko-v2-Q4_K_M.gguf`
by default.

## Training data

Sourced by following the dataset references of
[z-tipo-extension](https://github.com/KohakuBlueleaf/z-tipo-extension) /
[KGen / TIPO](https://github.com/KohakuBlueleaf/KGen) by KohakuBlueleaf.

---

## Model lineage (both models)

| Stage | Model |
| --- | --- |
| Base | [`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it) |
| Decensored | [`p-e-w/gemma-4-E2B-it-heretic-ara`](https://huggingface.co/p-e-w/gemma-4-E2B-it-heretic-ara) (Heretic, ARA = Arbitrary-Rank Ablation) |
| gemma4-tipo-ko | Korean TIPO fine-tune → bf16 → Q4_K_M |
| Gemma-tipo-vision-v1 | Multimodal vision SFT (trainable projector + freq-weighted CE) → bf16 merge → Q4_K_M text + f16 mmproj |

Architecture: `gemma4` (Gemma 4 E2B, Per-Layer Embeddings, 128K context).

## License & attribution

These are derivatives of **Google Gemma 4** and are therefore governed by the
[Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the
[Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy).
By using these models you agree to those terms. "Gemma" is a trademark of
Google LLC. The decensoring stage (`p-e-w/gemma-4-E2B-it-heretic-ara`) is
released under Apache-2.0; the underlying Gemma weights remain under the
Gemma terms. TIPO concept and tooling © KohakuBlueleaf (KGen, Apache-2.0).
