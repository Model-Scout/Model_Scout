---
license: apache-2.0
base_model: NbAiLab/nb-whisper-small
language:
  - "no"
  - nb
  - nn
tags:
  - whisper
  - coreml
  - whisperkit
  - automatic-speech-recognition
  - asr
  - audio
  - norwegian
  - apple-silicon
pipeline_tag: automatic-speech-recognition
---

# nb-whisper-small — WhisperKit CoreML

[NbAiLab/nb-whisper-small](https://huggingface.co/NbAiLab/nb-whisper-small)
converted to CoreML for [WhisperKit](https://github.com/argmaxinc/WhisperKit),
so it runs on the Apple Neural Engine.

**This is a format conversion, not a new model.** No retraining, no fine-tuning,
no distillation. Weights and behaviour are NbAiLab's; the changes are the
PyTorch → CoreML conversion and the folder layout WhisperKit expects. All credit
for the model belongs to [NbAiLab](https://huggingface.co/NbAiLab).

## Contents

```
nb-whisper-small/
├── MelSpectrogram.mlmodelc     372 KB
├── AudioEncoder.mlmodelc       170 MB
├── TextDecoder.mlmodelc        293 MB
├── config.json
└── generation_config.json
```

Float16 activations. The layout mirrors `argmaxinc/whisperkit-coreml`, which is
what `WhisperKitConfig(model:modelRepo:)` expects to find.

## Usage

With [papegøye](https://github.com/bredebjorhovd/papegoye), a bilingual
Norwegian/English macOS dictation daemon — it downloads this repo automatically:

```sh
parrot --bilingual
```

Directly with WhisperKit:

```swift
let config = WhisperKitConfig(
    model: "nb-whisper-small",
    modelRepo: "Barrymanalow/nb-whisper-coreml"
)
let pipe = try await WhisperKit(config)
```

**Requires** macOS 14+ on Apple Silicon. Verified with WhisperKit 0.9 on
macOS 15; loads and transcribes Norwegian correctly.

## Conversion

Converted with [whisperkittools](https://github.com/argmaxinc/whisperkittools)
via [`scripts/convert-nb-whisper.sh`](https://github.com/bredebjorhovd/papegoye/blob/main/scripts/convert-nb-whisper.sh)
in the papegøye repo. Two things that trip up a naive run, both handled by that
script:

- `whisperkittools` pins `torch==2.5.0`, which has no wheels above CPython 3.12.
  On a Mac defaulting to a newer Python, `pip install` fails with a bare "no
  matching distribution" that never mentions the version.
- `whisperkit-generate-model` emits only the compiled `.mlmodelc` bundles.
  `config.json` and `generation_config.json` stay behind in the source snapshot
  and have to be copied across, or WhisperKit has no config to read.

Reproduce with:

```sh
scripts/convert-nb-whisper.sh small
```

## Caveats

**It is a multilingual model, not a Norwegian-only one.** NB-Whisper is Whisper
small fine-tuned on Norwegian, so the multilingual tokenizer is intact
(`vocab_size` 51865). Practical consequences:

- English words inside Norwegian speech are transcribed rather than mangled.
- Forcing the `<|no|>` token onto **English** audio does not fail loudly — it
  renders the English speech as fluent Norwegian, which reads like a correct
  translation. Anything routing audio to this model should be confident the
  audio really is Norwegian. See
  [papegøye#22](https://github.com/bredebjorhovd/papegoye/issues/22).

Not verified here: Apple Neural Engine residency under `powermetrics`, and a
systematic word-level diff against the PyTorch checkpoint. The CoreML compute
plan targets ANE for nearly every operation, but that is the plan, not a
measurement.

## License

Apache-2.0, inherited from
[NbAiLab/nb-whisper-small](https://huggingface.co/NbAiLab/nb-whisper-small).
The conversion adds no restrictions. If you use this, cite NbAiLab's work — not
this repo, which only changed the file format.
