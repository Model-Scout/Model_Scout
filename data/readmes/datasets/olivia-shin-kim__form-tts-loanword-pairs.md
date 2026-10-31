---
license: cc-by-4.0
language:
- ko
task_categories:
- automatic-speech-recognition
size_categories:
- 1K<n<10K
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- machine-generated
pretty_name: FORM synthetic Korean loanword / native pairs
tags:
- loanwords
- korean
- synthetic-speech
- written-form
configs:
- config_name: default
  default: true
  data_files:
  - split: test
    path:
    - metadata.jsonl
    - audio/*.wav
---

# FORM synthetic Korean loanword / native pairs

Synthetic speech for a controlled comparison in the thesis *FORM: Form-tolerant Outcomes of Recognition for Multi-form Items* (Kim,
Emory University, 2026). Each of 203 pairs is one Korean carrier sentence spoken with a Korean-adapted loanword (버그, "bug") or
with its native Korean equivalent (오류), by four voices of one text-to-speech model: 1624 clips. Recorded speech offers no
such minimal pair; here everything but the word is fixed, so recognition of the loanword can be compared with recognition of its
native counterpart in the same sentence. The clips are a separate synthetic experiment and were never pooled with HiKE.

Code: https://github.com/olivia-shin-kim/form-asr.

## Loading

```python
from datasets import load_dataset
clips = load_dataset("olivia-shin-kim/form-tts-loanword-pairs", split="test")
pairs = load_dataset("json", data_files="hf://datasets/olivia-shin-kim/form-tts-loanword-pairs/pairs.jsonl", split="train")
```

One split, `test`, with 1624 clips. Each row is one clip with its pair and its acceptance set; `pairs.jsonl` (203 rows) and
`accept_sets.tts.v1.jsonl` (406 rows, one per sentence) hold the same information per pair and per sentence.

## Fields

**Clips.** `audio` (16 kHz mono, 32-bit float WAV, bit-exact to the arrays the recognizers decoded), `clip_id`, `type_key` (pair,
`Hangul|Latin`), `member` (`loanword` or `native`), `voice_id`, `word` (the target word), `text` (the synthesized sentence),
`start` and `end` (character offsets of `word` in `text`), `accepted_forms` (written forms scored as correct: both scripts for a
loanword, the standard form and spacing variants for a native word), `duration_s`, `seed` (synthesis seed), `array_sha256` (hash of
the float32 samples), `in_analysis`, and the pair's fields below.

**Pairs** (`pairs.jsonl`). `type_key`, `loanword_hangul`, `loanword_latin`, `native_replacement`, `native_type` (고유어 native or 한자어
Sino-Korean), `sense_en`, `zipf_loanword` (Zipf frequency of the loanword).

**Acceptance sets** (`accept_sets.tts.v1.jsonl`). `item_id`, `corpus`, `utt_id` (clip id without the voice), `start`, `end`,
`type_key`, `member`, `members` (= `accepted_forms`), `member_sources`.

`voices.json` describes the four voices.

## How the clips were made

The loanword types come from HiKE. The pairs and their carrier sentences were generated using Claude and reviewed by a native
Korean speaker before synthesis. Each pair was synthesized with Qwen3-TTS 12Hz 1.7B (`Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`,
`-VoiceDesign` and `-Base`; Apache-2.0) in four voices: one of the model's built-in speakers (Sohee) and three voices designed from
text descriptions with the VoiceDesign checkpoint and then cloned from that synthetic reference with the Base checkpoint. No
recording of any person was used. Audio was generated at 24 kHz and resampled to 16 kHz; every clip records its seed. A listening
screen before any decode found three pairs misrendered; their 24 clips have `in_analysis` false, leaving 200 pairs.

## Intended use and limitations

For controlled tests of how speech recognizers handle loanwords against native words. The speech is synthetic, from one model,
synthesized from Hangul input, and read in a neutral register; results on it need not carry over to recorded or spontaneous
speech.

## License

CC BY 4.0. The loanword types come from HiKE (Paik et al., 2026; Apache-2.0); Zipf frequencies are from wordfreq 3.1.1 (Speer;
data CC BY-SA 4.0).

## Citation

```bibtex
@mastersthesis{kim2026form,
  author = {Kim, Olivia S.},
  title  = {{FORM}: Form-tolerant Outcomes of Recognition for Multi-form Items},
  school = {Emory University},
  year   = {2026}
}
```
