---
license: apache-2.0
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
base_model:
- Qwen/Qwen3-ASR-0.6B
pipeline_tag: automatic-speech-recognition
tags:
- loom
- automatic-speech-recognition
library_name: loom-py-rt
---
# Qwen3-ASR-0.6B

Alibaba's Qwen3-ASR 0.6B multilingual ASR model, exported for loom.cpp.

This is a [loom.cpp](https://github.com/loom-ai-org/loom.cpp) export: a single self-describing GGUF
that carries its own graph topologies, tokenizer (if any) and driver script, produced by
[loom-exporter](https://github.com/loom-ai-org/loom-exporter).

## Original model

Exported from [`Qwen/Qwen3-ASR-0.6B`](https://huggingface.co/Qwen/Qwen3-ASR-0.6B). Weights are unmodified; this repo packages the same parameters into
loom.cpp's GGUF format.

## License

`apache-2.0`, inherited from the base model above.

## Language(s)

`zh`, `en`, `yue`, `ar`, `de`, `fr`, `es`, `pt`, `id`, `it`, `ko`, `ru`, `th`, `vi`, `ja`, `tr`, `hi`, `ms`, `nl`, `sv`, `da`, `fi`, `pl`, `cs`, `fil`, `fa`, `el`, `hu`, `mk`, `ro`

exported from the `-hf` mirror of this repo (Transformers-native layout); see [[reference-qwen3-asr-hf-checkpoint]]

## Usage

Run it with [loom-py](https://github.com/loom-ai-org/loom-py) -- `loom-py-rt` on PyPI:

```sh
pip install -U "loom-py-rt[hub]"
```

**Needs `loom-py-rt` 1.0.0rc18 or later.** This file uses the engine's `STFT` op, new in that release; an older runtime stops with `unknown op 'STFT'`.

```python
import loom

model = loom.Model.from_pretrained("loom-ai-org/qwen3-asr-0.6b-loom")

# Audio is a mono float list at 16 kHz. This model decodes in the one language it was trained for and
# takes no `language=` argument -- passing one warns and is ignored, because nothing in its decode
# could act on it.
result = model.speech2text.infer(audio, timestamps=True)
print(result.text)

# It emits no timestamp tokens, so `segments` is one span covering the whole clip and
# `result.timestamped` is False. Check that before treating a start/end as a boundary the model chose.
for segment in result.segments:
    print(segment.start, segment.end, segment.text)
```

### The layer underneath

The call above is the high-level door: one per task, named for the modality pair it maps between, with
the windowing, sampling and assembly this model needs already applied. Under it, `model.infer(...)`
passes your arguments straight to the driver this GGUF embeds -- which is where you go for a knob the
door does not name.

`model.driver_source` prints that driver, including a header comment documenting every argument it
accepts for this model, and is the authority on it. See [loom-py](https://github.com/loom-ai-org/loom-py) for the API and
[loom.cpp](https://github.com/loom-ai-org/loom.cpp) for what the engine does between the two.

## Files

- `qwen3-asr-0.6b.gguf` -- the model, exported with loom-exporter.
