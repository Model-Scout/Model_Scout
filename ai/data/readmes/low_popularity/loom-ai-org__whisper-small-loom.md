---
license: apache-2.0
language:
- en
- zh
- de
- es
- ru
- ko
- fr
- ja
- pt
- tr
- pl
- ca
- nl
- ar
- sv
- it
- id
- hi
- fi
- vi
- he
- uk
- el
- ms
- cs
- ro
- da
- hu
- ta
- no
- th
- ur
- hr
- bg
- lt
- la
- mi
- ml
- cy
- sk
- te
- fa
- lv
- bn
- sr
- az
- sl
- kn
- et
- mk
- br
- eu
- is
- hy
- ne
- mn
- bs
- kk
- sq
- sw
- gl
- mr
- pa
- si
- km
- sn
- yo
- so
- af
- oc
- ka
- be
- tg
- sd
- gu
- am
- yi
- lo
- uz
- fo
- ht
- ps
- tk
- nn
- mt
- sa
- lb
- my
- bo
- tl
- mg
- as
- tt
- haw
- ln
- ha
- ba
- jw
- su
base_model:
- openai/whisper-small
pipeline_tag: automatic-speech-recognition
tags:
- loom
- automatic-speech-recognition
library_name: loom-py-rt
---
# Whisper Small

OpenAI's Whisper small encoder-decoder ASR model, exported for loom.cpp.

This is a [loom.cpp](https://github.com/loom-ai-org/loom.cpp) export: a single self-describing GGUF
that carries its own graph topologies, tokenizer (if any) and driver script, produced by
[loom-exporter](https://github.com/loom-ai-org/loom-exporter).

## Original model

Exported from [`openai/whisper-small`](https://huggingface.co/openai/whisper-small). Weights are unmodified; this repo packages the same parameters into
loom.cpp's GGUF format.

## License

`apache-2.0`, inherited from the base model above.

## Language(s)

`en`, `zh`, `de`, `es`, `ru`, `ko`, `fr`, `ja`, `pt`, `tr`, `pl`, `ca`, `nl`, `ar`, `sv`, `it`, `id`, `hi`, `fi`, `vi`, `he`, `uk`, `el`, `ms`, `cs`, `ro`, `da`, `hu`, `ta`, `no`, `th`, `ur`, `hr`, `bg`, `lt`, `la`, `mi`, `ml`, `cy`, `sk`, `te`, `fa`, `lv`, `bn`, `sr`, `az`, `sl`, `kn`, `et`, `mk`, `br`, `eu`, `is`, `hy`, `ne`, `mn`, `bs`, `kk`, `sq`, `sw`, `gl`, `mr`, `pa`, `si`, `km`, `sn`, `yo`, `so`, `af`, `oc`, `ka`, `be`, `tg`, `sd`, `gu`, `am`, `yi`, `lo`, `uz`, `fo`, `ht`, `ps`, `tk`, `nn`, `mt`, `sa`, `lb`, `my`, `bo`, `tl`, `mg`, `as`, `tt`, `haw`, `ln`, `ha`, `ba`, `jw`, `su`

## Usage

Run it with [loom-py](https://github.com/loom-ai-org/loom-py) -- `loom-py-rt` on PyPI:

```sh
pip install -U "loom-py-rt[hub]"
```

```python
import loom

model = loom.Model.from_pretrained("loom-ai-org/whisper-small-loom")

# Audio is a mono float list at 16 kHz. Long files are windowed for you, and a model that emits
# timestamps is seeked to where it closed its last segment rather than cut at a fixed stride.
# Omit `language=` to let the model detect it; `task="translate"` renders the speech in English.
result = model.speech2text.infer(audio, language="en", timestamps=True)
print(result.text)
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

- `whisper-small.gguf` -- the model, exported with loom-exporter.
