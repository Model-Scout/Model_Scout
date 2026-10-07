---
license: cc-by-nc-4.0
pipeline_tag: text-generation
base_model: google/gemma-4-E4B-it
tags:
- gemma4
- gemma
- google
- translation
- japanese
- korean
- chinese
library_name: transformers
---

# shamrock-0-e4b

Gemma 4 E4B fine-tuned for the [Oxalis](https://oxalis.ink) desktop app's
language-learning surfaces (camera translate, text translate, tutor, talk,
dictionary) across Japanese, Korean, and Simplified Chinese. The E4B sibling
of [`oxalis-ink/shamrock-0-e2b`](https://huggingface.co/oxalis-ink/shamrock-0-e2b).

## Layout

| Path | Contents |
| --- | --- |
| repo root | Merged fp16 checkpoint |
| `gguf/` | `shamrock-0-e4b-q4_k_m.gguf` + `mmproj-shamrock-0-e4b-f16.gguf`, what the app's llama.cpp runtime loads |
| `MTP/` | Multi-token-prediction drafter for speculative decoding: `mtp-shamrock-0-e4b-Q8_0.gguf` (llama.cpp, serve with `--spec-type draft-mtp`) and the same head in HF format under `MTP/assistant/` |

## License

shamrock-0-e4b is licensed under
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (see [LICENSE](LICENSE)).
You can use, share and adapt it for non-commercial purposes, including
personal projects and research, as long as you give credit. Commercial use,
such as selling the weights, serving them in a paid product or API, or
bundling them into a commercial app, is not permitted. For commercial
licensing, reach out via [oxalis.ink](https://oxalis.ink).

When you share this model or anything built from it, credit it as:

> shamrock-0-e4b by Oxalis (https://oxalis.ink), licensed under CC BY-NC 4.0

and say whether you changed it.

shamrock-0-e4b is a modified version of
[Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it) by Google DeepMind:
its weights were fine-tuned and merged, then converted to GGUF with an added
MTP drafter. Gemma 4 itself is licensed under the Apache License 2.0
(see [LICENSE-GEMMA](LICENSE-GEMMA) and the
[Gemma 4 license](https://ai.google.dev/gemma/docs/gemma_4_license)); the CC
BY-NC 4.0 terms cover Oxalis's modifications. See [NOTICE](NOTICE).
