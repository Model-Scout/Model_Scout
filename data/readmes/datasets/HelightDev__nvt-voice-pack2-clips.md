---
license: other
license_name: per-source
language: [en, de, fr, es, it, pt, nl, sv, ru, pl, uk, cs, zh, ja, ko, vi, th, ar, hi, tr, fi, id, sw]
task_categories: [automatic-speech-recognition, text-to-speech]
pretty_name: NVT Voice pack2 clips
---

# NVT Voice pack2 clips

Speech clips with transcripts in 23 languages, selected from openly licensed corpora for training a small multilingual
speech model (recognition, phone recognition, voice). This is a selection and repackaging of the sources below; all
credit for the recordings and transcripts goes to their creators.

## Layout

Per set (`SOURCE-LANG`): `sets/SET/SET-NNN.tar` (audio, paths inside relative to the pack's root: `audio/SET/SPLIT/SPEAKER/ID.EXT`)
and `sets/SET/SET.tsv`, a line per clip: `KEY<TAB>PATH<TAB>TEXT<TAB>SECONDS`. KEY is `LANG/SPLIT/SPEAKER/ID`
(`LANG/SPLIT/ID` where the source names no speakers); SPLIT is `train` or `test` (held out: whole speakers of the
source's dev and test splits, or a fixed 5 % of its speakers where it has no splits). Audio is the source's own
FLAC or Opus where it came so, else 16-bit FLAC; original sample rate, mono. Transcripts are the sources' own, unchanged.

## What was changed

Clips were selected (hours per language, minutes per speaker capped to spread speakers), cut from longer recordings
where the source gives utterance times (YODAS2), mixed down to mono and re-encoded to FLAC where the source wasn't FLAC
or Opus. YODAS2 subtitles are the uploaders' and unchecked: expect mismatches.

## Sources and licences

| Set | Source | Licence | Link |
|---|---|---|---|
| mls-* | Multilingual LibriSpeech (Pratap et al., 2020) | CC BY 4.0 | https://huggingface.co/datasets/facebook/multilingual_librispeech |
| voxpopuli-* | VoxPopuli, transcribed part (Wang et al., 2021) | CC0 (+ European Parliament legal notice for the audio) | https://huggingface.co/datasets/facebook/voxpopuli |
| fleurs-* | FLEURS (Conneau et al., 2022) | CC BY 4.0 | https://huggingface.co/datasets/google/fleurs |
| granary-uk | YODAS segments used by NVIDIA Granary (espnet/yodas-granary) | CC BY 3.0 | https://huggingface.co/datasets/espnet/yodas-granary |
| yodas2-* | YODAS2 (Li et al., 2023): CC-licensed YouTube videos | CC BY 3.0 | https://huggingface.co/datasets/espnet/yodas2 |
| nst-sv | NST Swedish ASR database (Språkbanken, reorganised sbr-56) | CC0 | https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-56/ |
| ruls-ru | Russian LibriSpeech (OpenSLR 96) | Public domain (US) | https://www.openslr.org/96/ |
| zeroth-ko | Zeroth-Korean (OpenSLR 40) | CC BY 4.0 | https://www.openslr.org/40/ |
| aishell3-zh | AISHELL-3 (OpenSLR 93) | Apache 2.0 | https://www.openslr.org/93/ |
| mediaspeech-* | MediaSpeech (OpenSLR 108) | CC BY 4.0 | https://www.openslr.org/108/ |
| alffa-sw | ALFFA Swahili broadcast news (OpenSLR 25) | MIT | https://www.openslr.org/25/ |

Each clip keeps its source's licence; use the clips under those terms (attribution for the CC BY ones, the Apache 2.0
licence and notice for AISHELL-3, the MIT notice for ALFFA). The speakers recorded for public corpora; to have a
recording removed, contact the source's maintainers, and open a discussion here to have it dropped from this selection.
