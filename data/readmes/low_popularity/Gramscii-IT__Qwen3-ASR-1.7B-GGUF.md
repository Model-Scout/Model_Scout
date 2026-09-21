---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-ASR-1.7B
base_model:
- Qwen/Qwen3-ASR-1.7B
library_name: llama.cpp
pipeline_tag: automatic-speech-recognition
language:
- zh
- en
- yue
- ar
- de
- fr
- es
- pt
- id
- it
- ko
- ru
- th
- vi
- ja
- tr
- hi
- ms
- nl
- sv
- da
- fi
- pl
- cs
- fil
- fa
- el
- hu
- mk
- ro
tags:
- gguf
- llama.cpp
- asr
- speech-to-text
- audio
---

# Qwen3-ASR 1.7B, GGUF (Q8_0)

Speech to text for [SDG](https://github.com/gramscii/semantic-deterministic-graph)'s
audio and video transcription seat: two files, served by the same
`llama-server` SDG already runs for every other model, over the same
`input_audio` chat-completion field it uses for images.

## Provenance

Nothing was reconverted. Both files are byte-identical to the ones published
by [unslothai/Qwen3-ASR-1.7B-GGUF](https://huggingface.co/unslothai/Qwen3-ASR-1.7B-GGUF),
which is itself a GGUF conversion of Qwen's own release:

| step | source | revision |
|------|--------|----------|
| original weights | [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | `7278e1e70fe206f11671096ffdd38061171dd6e5` |
| GGUF conversion | [unslothai/Qwen3-ASR-1.7B-GGUF](https://huggingface.co/unslothai/Qwen3-ASR-1.7B-GGUF) | `cad2b8497d1541a8b6f9f7ad32e8c6f9c9908da3` |

| file | bytes | sha256 |
|------|-------|--------|
| `Qwen3-ASR-1.7B-Q8_0.gguf` | 2165034944 | `58e22d0532d4eacaf034cfac17a6fed159f37c41390c710186783be439d1fc57` |
| `mmproj-Qwen3-ASR-1.7B-Q8_0.gguf` | 355709344 | `46c1d533af3f354ceb37ce855dbceff7da7fa7cf1e6a523df3b13440bd164c0d` |

## Why Q8_0 and not bf16

This repository publishes one quantization. Measured against the bf16 of the
same conversion, on the same four Italian recordings, served the same way:

| recording | Q8_0 against bf16 | speed |
|-----------|-------------------|-------|
| synthetic voice | **0.00%** | 1.56x |
| lecture, good microphone | **0.00%** | 1.49x |
| rap over a musical bed | 2.70% | 1.49x |
| speech off the cuff | **0.00%** | 1.37x |

Word for word identical on three of the four, and half again as fast at
3.73 GB resident against 5.80. Q8_0 is not the compromise here, it is the
better file on every axis but singing over music, where it drifts 2.70%.

## Why the 1.7B and not the 0.6B

Qwen also publishes a 0.6B variant, a third of the size. We measured both on
the same four Italian recordings and the smaller one is not usable: it
degenerates on real speech, transcribing "Shadow AI" as "scedo vagaino" and
"una chat gratuita" as "un alcheto gratuita", with no punctuation. It is also
slower than the 1.7B on the same audio (15.63 s against 9.33 s for 136
seconds), because a worse transcript costs more decoding, not less. The 1.7B
is both the more accurate model and the faster one.

## Why no forced aligner

Qwen3-ASR's own word-level timestamps come from a second model,
`Qwen3-ForcedAligner-0.6B`, run separately. We did not include it: the only
GGUF conversion of it has 47 downloads, is not published by the same team
that converts the ASR model, is undeclared by llama.cpp, and caps at five
minutes of audio per call. SDG's transcription seat instead cuts audio into
blocks of up to 120 seconds on silence boundaries and times the transcript
to the block, not the word. That granularity is what this model was measured
and integrated for.

## What we measured

Apple M4 Pro, 64 GB, Metal, `llama-server` from SDG's own runtime.

- **Fits SDG's serving contract as is**: `input_audio` over the same
  `/v1/chat/completions` endpoint and the same server SDG already runs for
  every other seat. No new engine.
- **About 14 prompt tokens per second of audio**: a 14.7 s clip costs 212
  prompt tokens, so SDG's 16384-token context holds roughly 20 minutes of
  audio in one call.
- **Cutting into blocks costs accuracy, and shorter blocks cost more**:
  measured against transcribing one file whole, 30-second blocks drift
  4.74%, 60-second blocks 3.32%, 120-second blocks 0.71%. A 30-second block
  reintroduces exactly the kind of error this model over transducer models
  was chosen to avoid ("lei ha i acte operativo" instead of "l'AI Act è
  operativo").
- **Overlapping blocks makes it worse, not better**: the model carries no
  memory between calls, so the same seconds decoded twice come back worded
  differently, and stitching the seam back together loses more than the
  overlap recovers. 5 s of overlap on 30-second blocks raised the drift from
  4.74% to 8.53%; 10 s raised it to 13.51%.
- **A one-hour recording transcribes in about 194 seconds** at 120-second
  blocks, measured by extrapolating this file's per-block cost.
- **Peak memory while serving**: 5.43 GB resident with an idle seat present,
  at `-c 16384`.

## Usage

Served like every other SDG seat, with `--mmproj` for the audio projector.
The window holds the longest block SDG cuts, 120 seconds, which costs about
1590 prompt tokens:

```bash
llama-server -m Qwen3-ASR-1.7B-Q8_0.gguf \
  --mmproj mmproj-Qwen3-ASR-1.7B-Q8_0.gguf -c 4096 -ngl 99 --jinja
```

`--jinja` is not optional: the chat template ships inside the GGUF and is
not one llama-server knows, so without it the server refuses to start.

The request shape is the one Qwen's own package builds: the user turn
carries **only the audio**, with no instruction text, and the system turn
carries the context string or nothing.

```python
{
  "messages": [
    {"role": "system", "content": ""},
    {"role": "user", "content": [
      {"type": "input_audio", "input_audio": {"data": "<base64 wav>", "format": "wav"}},
    ]},
  ],
  "temperature": 0,
}
```

The response carries a `language <name><asr_text>...` marker; read the text
after `<asr_text>`.

Two options exist and neither is worth taking here, both measured on a
120-second block:

- **Forcing the language** by prefilling the assistant turn with
  `language Italian<asr_text>` skips language identification. It saves 20%
  on a 30-second block and nothing measurable on a 120-second one, and the
  text is identical either way.
- **A context string** in the system turn changes nothing when it is bare
  keywords, and actively hurts when it is a sentence: "AI Act, Shadow AI in
  azienda" as context turned a correct opening into "Da agosto lei AI Act è
  operativo". A long enough block already gets those terms right without
  help.

## License and attribution

Apache 2.0, inherited unchanged from Qwen's release. The model is Qwen's
work; the GGUF conversion is [unslothai](https://huggingface.co/unslothai)'s.
This repository redistributes the conversion and adds the measurements
above.
