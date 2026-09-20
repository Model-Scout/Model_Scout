---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
library_name: transformers
pipeline_tag: image-text-to-text
tags:
  - qwen3.6
  - roleplay
  - conversational
  - mixture-of-experts
  - multimodal
  - gguf
  - mtp
  - abliterated
language:
  - en
  - zh
  - multilingual
---

<p align="center">
  <img src="assets/joyfox-banner.png" alt="JoyFox" width="100%">
</p>

<h1 align="center">JoyFox-Qwen3.6-35B-A3B-RP-Aggressive</h1>

<p align="center">
  A roleplay-specialized, multimodal Mixture-of-Experts model built on Qwen3.6-35B-A3B.
</p>

<p align="center">
  <strong>English</strong> · <a href="https://huggingface.co/joyfox/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/blob/main/README_ZH.md">简体中文</a>
</p>

JoyFox-Qwen3.6-35B-A3B-RP-Aggressive is designed for sustained character voice, direct instruction following, coherent scene continuation, low role-break frequency, and long-context creative dialogue. It combines roleplay supervised fine-tuning, preference optimization, explicit response-length control, and a final activation-space refusal-direction intervention.

The model retains the original Qwen3.6 multimodal architecture, 262K native context, Mixture-of-Experts routing, and native Multi-Token Prediction head.

## 🦊 Model at a glance

| | |
|---|---|
| Primary focus | Long-context roleplay, character fidelity, creative dialogue, scene continuation |
| Architecture | 35B-parameter MoE; approximately 3B active parameters per token |
| Expert routing | 256 experts; 8 selected per token |
| Context | 262,144 tokens natively |
| Modalities | Text, image, and video |
| Generation | Thinking and non-thinking modes; native MTP speculative decoding |
| Post-training | Roleplay instruction tuning → character preference → response-length calibration |
| Behavioral variant | Aggressive two-pass refusal-direction intervention |

## ⚡ What “Aggressive” means

The Aggressive variant applies the stronger form of the refusal-direction intervention. It is intended to answer directly instead of falling into repetitive policy-style refusals, prematurely ending a scene, or breaking character. “Aggressive” describes the strength of the behavioral intervention, not the model's personality or default writing tone.

This intervention changes refusal behavior; it does not add factual knowledge, reasoning ability, or new training examples. The model can still follow a calm, gentle, formal, comedic, or restrained character card when those traits are specified in the prompt.

The model may still produce mistakes, fictional claims, undesirable content, or occasional disclaimers inherited from earlier post-training. Users remain responsible for prompts, outputs, deployment controls, and compliance with applicable law.

## 🧬 Post-training

JoyFox uses a layered post-training strategy rather than relying on a single “uncensoring” edit. Roleplay instruction tuning establishes character voice and scene behavior; preference optimization improves consistency and interaction quality; length calibration controls over-writing; and the final two-pass activation-space intervention changes refusal behavior without replacing the learned roleplay style.

### Roleplay instruction tuning

The base model is adapted on multi-turn character conversations and identity-consistency instructions. Training uses the native non-thinking Qwen chat template and masks prompt tokens so the language-model loss is applied to assistant responses.

This stage adapts the text model while keeping the vision tower and multimodal projector unchanged. Its purpose is to teach the model how to:

- maintain character voice and relationship state across turns;
- continue the current scene instead of summarizing or explaining it;
- combine dialogue, actions, and environmental details naturally;
- avoid speaking or deciding on behalf of the user;
- preserve identity and formatting under long character cards.

### Character-preference optimization

The roleplay model is then optimized on chosen/rejected response pairs using the sigmoid DPO objective:

```text
L_DPO = -log σ(β [(log πθ(y+|x) - log πref(y+|x))
                  - (log πθ(y-|x) - log πref(y-|x))])
```

The preference signal emphasizes character consistency, correct use of scene context, natural interaction, emotional continuity, and avoidance of role breaks. A small supervised fine-tuning term is mixed into the preference loss to reduce drift away from the SFT model.

### Response-length calibration

The selected preference model becomes the reference point for a second DPO stage. Here the preferred response is the concise, complete roleplay continuation and the rejected response is an unnecessarily expanded version of the same interaction.

This does not train the model to answer with a fixed number of tokens. It teaches a relative preference: preserve the essential action, voice, emotion, and conversational hook while removing redundant narration, repeated conclusions, and unwanted scene inflation.

### Optimization overview

| Component | Training signal | Intended behavior |
|---|---|---|
| Roleplay instruction tuning | Assistant-response language modeling | Character voice, dialogue rhythm, scene continuation, identity stability |
| Character preference | Chosen/rejected response preference | Context following, character consistency, natural interaction, reduced role breaks |
| Length calibration | Concise/over-expanded response preference | Complete replies without redundant narration or scene inflation |
| Aggressive intervention | Two-pass activation-space direction removal | Reduced refusal behavior with the trained roleplay style retained |

The final refusal-direction intervention is applied only after roleplay post-training is complete. Training corpus names, private examples, dataset sizes, and implementation-specific training settings are not part of this release.

## 🧪 Technical method

This release uses a white-box activation-space weight edit related to the method described in [*Refusal in Language Models Is Mediated by a Single Direction*](https://arxiv.org/abs/2406.11717). It is not a new gradient-training stage.

For paired refusal-triggering and ordinary instructions, residual activations are collected at the final user-token position. A refusal direction is estimated by the normalized difference of means:

```text
r_l = normalize(mean(h_refusal,l) - mean(h_ordinary,l))
```

For a weight matrix whose output can express this direction, the corresponding component is projected out:

```text
W'_l = W_l - r_l (r_l^T W_l)
```

The exact multiplication orientation is transposed when required by the stored tensor layout. The intervention used here has the following properties:

1. One difference-of-means direction is estimated from paired refusal-triggering and ordinary prompts.
2. Activations are collected through the native chat template.
3. Layers 0 and 1 are protected; text-model layers 2–39 and the output head are edited.
4. Attention and feed-forward output paths are included.
5. A second pass re-probes the already edited model and removes the newly exposed residual direction.
6. Vision weights and the native MTP component are copied without modification.

The second re-probed pass was important: weaker late-layer-only edits, multi-direction top-layer edits, output-head-only edits, and single-pass variants did not consistently eliminate full-answer refusals.

## 🏗️ Architecture overview

| Property | Value |
|---|---:|
| Model family | Qwen3.6 multimodal MoE |
| Total parameters | 35B |
| Active parameters | ~3B per token |
| Hidden size | 2,048 |
| Decoder layers | 40 |
| Experts | 256 |
| Routed experts per token | 8 |
| Attention pattern | 3 linear-attention layers : 1 full-attention layer |
| Native context | 262,144 tokens |
| Modalities | Text, image, video |
| Multi-Token Prediction | 1 native MTP head |

## 📊 Evaluation summary

All figures below are generation-based results, not logits-only proxies. Exact scores can vary with runtime, template, sampler, context length, and quantization.

| Evaluation | Result |
|---|---:|
| Full-answer refusal suite | 0 / 100 refusals |
| Q6_K verification subset | 0 / 20 refusals; 0 generation failures |
| Long-context roleplay scenes | 100 / 100 valid generations |
| Role breaks | 0 / 100 |
| Empty outputs | 0 / 100 |
| Leaked `<think>` tags | 0 / 100 |
| Average roleplay response length | 133.65 characters |
| General capability regression set | 30 / 30 substantively correct |

The roleplay suite uses fixed long-context character scenes and checks output validity, role breaks, leaked reasoning tags, repetition, response length, and reference-style similarity. These results indicate that the intervention preserved the source model's concise roleplay style while changing refusal behavior.

## 💾 GGUF downloads and precision guide

Every main GGUF was independently quantized from the same BF16 export. These are standard llama.cpp quantizations without an importance matrix. They are not HauhauCS K_P quantizations, and no K_P quality claim is made here.

`Q4_K` and `Q5_K` are llama.cpp aliases for `Q4_K_M` and `Q5_K_M`; duplicate alias files are intentionally omitted. IQ quantizations are a separate non-linear family and are outside this Q4–Q8 standard set.

| File | Quant | Effective BPW | File size | Relative quality | Recommended use |
|---|---:|---:|---:|---|---|
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q4_0.gguf` | Q4_0 | 4.55 | 18.81 GiB | Entry-level | Legacy compatibility; use only when K-quants are unavailable |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q4_1.gguf` | Q4_1 | 5.04 | 20.84 GiB | Entry-level+ | Legacy 4-bit with additional scale/min data |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q4_K_S.gguf` | Q4_K_S | 4.59 | 18.97 GiB | Good | Lowest-memory modern K-quant in this release |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q4_K_M.gguf` | Q4_K_M | 4.89 | 20.22 GiB | Very good | **Recommended 4-bit**; best balance for constrained systems |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_0.gguf` | Q5_0 | 5.53 | 22.88 GiB | Good+ | Legacy 5-bit compatibility |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_1.gguf` | Q5_1 | 6.02 | 24.91 GiB | Good+ | Legacy 5-bit with additional scale/min data |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_K_S.gguf` | Q5_K_S | 5.53 | 22.88 GiB | High | Smaller modern 5-bit option |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_K_M.gguf` | Q5_K_M | 5.71 | 23.61 GiB | High+ | **Recommended balance** for roleplay quality and memory |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q6_K.gguf` | Q6_K | 6.58 | 27.20 GiB | Very high | **Recommended high-quality** deployment |
| `JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q8_0.gguf` | Q8_0 | 8.52 | 35.21 GiB | Highest GGUF fidelity | Maximum fidelity when memory is not constrained |
| `mmproj-JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-f16.gguf` | mmproj F16 | — | 0.84 GiB | Lossless projector | Required only for image/video input through llama.cpp |

Weight memory is approximately the file size when fully offloaded, but runtime memory is higher. Context/KV cache, batching, MTP draft state, multimodal embeddings, and backend buffers must also fit. A 128K or 262K context can require substantially more memory than a short-context launch.

### Which quant should I choose?

| Available memory priority | Start with | Why |
|---|---|---|
| Minimum practical footprint | Q4_K_S | Smallest modern K-quant in the set |
| Limited memory, quality still important | Q4_K_M | Strong 4-bit balance |
| General roleplay deployment | Q5_K_M | Better dialogue nuance with moderate size increase |
| High-quality long sessions | Q6_K | Low quantization loss; recommended when it fits |
| Fidelity comparison or abundant memory | Q8_0 | Closest GGUF option to BF16 |

Avoid choosing by nominal bit count alone: `_K_M` preserves selected tensor classes at higher precision than `_K_S`, while `_0` and `_1` are older block formats. Backend support can also affect speed, so benchmark the two nearest candidates on the intended runtime.

## 🚀 GGUF usage

Use a recent [llama.cpp](https://github.com/ggml-org/llama.cpp) build with Qwen3.6 and MTP support.

### Download one quant

```bash
hf download joyfox/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive \
  GGUF/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_K_M.gguf \
  --local-dir JoyFox-Qwen3.6-35B-A3B-RP-Aggressive
```

### Text chat

```bash
llama-cli \
  -m JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/GGUF/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q5_K_M.gguf \
  --jinja -c 32768 -ngl 99 \
  --temp 0.85 --top-p 0.95 --top-k 40 --min-p 0.02
```

### OpenAI-compatible server

```bash
llama-server \
  -m JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/GGUF/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q6_K.gguf \
  --jinja -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

For partial GPU offload, replace `-ngl 99` with the number of layers that fit. Reduce `-c` first if KV-cache memory is the limiting factor.

### Enable native MTP speculative decoding

All main GGUF files contain the native MTP tensors. A recent llama.cpp build can use them directly from the main model:

```bash
llama-server \
  -m JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/GGUF/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q6_K.gguf \
  --jinja -c 131072 -ngl 99 \
  --spec-type draft-mtp --spec-draft-n-max 3
```

MTP is an optional speed feature, not a quality mode. If the runtime does not support `draft-mtp`, omit the two speculative-decoding flags. Increase the draft length only after measuring acceptance rate, latency, and memory use on the intended workload.

### Multimodal inference

Download the F16 projector in addition to one main quant, then pass it with `--mmproj`:

```bash
llama-cli \
  -m JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/GGUF/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-Q6_K.gguf \
  --mmproj JoyFox-Qwen3.6-35B-A3B-RP-Aggressive/GGUF/mmproj-JoyFox-Qwen3.6-35B-A3B-RP-Aggressive-f16.gguf \
  --jinja -c 32768 -ngl 99
```

## 🎛️ Recommended sampling presets

These are starting points, not hard requirements.

| Scenario | Thinking | Temperature | Top-p | Top-k | Min-p | Presence penalty |
|---|---:|---:|---:|---:|---:|---:|
| Roleplay / creative dialogue | Off | 0.85 | 0.95 | 40 | 0.02 | 0.0–0.5 |
| General chat | Off | 0.70 | 0.80 | 20 | 0.00 | 1.5 |
| General reasoning | On | 1.00 | 0.95 | 20 | 0.00 | 1.5 |
| Coding / precise tasks | On | 0.60 | 0.95 | 20 | 0.00 | 0.0 |

For strict character continuity, place the character card and non-negotiable style rules in the system message. A lower presence penalty usually preserves recurring names, motifs, and setting details better; a higher value encourages novelty but can push long roleplay away from established phrasing.

## 🤗 Transformers usage

The repository root is the complete BF16 multimodal checkpoint.

```python
from transformers import pipeline

pipe = pipeline(
    "image-text-to-text",
    model="joyfox/JoyFox-Qwen3.6-35B-A3B-RP-Aggressive",
    device_map="auto",
    dtype="auto",
)

messages = [
    {"role": "system", "content": "Stay in character and write vivid, coherent dialogue."},
    {"role": "user", "content": "The rain has stopped. Continue the scene from the inn doorway."},
]

result = pipe(messages, max_new_tokens=512)
print(result[0]["generated_text"][-1]["content"])
```

Use the repository's chat template. Do not manually concatenate role labels or expose internal reasoning tags in the prompt.

## ⚠️ Limitations

- Abliteration changes refusal behavior and cannot guarantee uniformly improved responses.
- Quantization can reduce subtle prose quality, factual precision, multilingual consistency, and very-long-context stability.
- Q4 variants are most likely to lose small stylistic distinctions; use Q5_K_M or Q6_K when sustained character voice matters.
- Long native context does not mean every deployment can allocate a 262K KV cache.
- MTP speedup depends on token acceptance, backend support, prompt shape, and hardware.
- Multimodal GGUF inference requires the separate F16 projector.
- Generated content may be inaccurate or unsuitable. Evaluate the model for the intended application before deployment.

## 📜 License and attribution

Released under Apache-2.0, following the base model license. Qwen3.6 is created by the Qwen team. The refusal-direction technique is inspired by Arditi et al.; GGUF conversion and quantization use llama.cpp.

## 🔗 References

- [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [llama.cpp speculative decoding documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md)
