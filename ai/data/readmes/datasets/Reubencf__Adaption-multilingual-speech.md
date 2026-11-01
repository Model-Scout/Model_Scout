---
annotations_creators: []
language:
  - ja
  - ru
  - de
  - ko
  - es
  - pt
  - zh
  - en
  - fr
language_creators: []
license: cc-by-4.0
multilinguality:
  - multilingual
pretty_name: Multilingual Speech (Adaption)
size_categories:
  - 10K<n<100K
source_datasets:
  - extended|https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts
tags:
  - adaption
  - instruction-tuning
  - speech
  - tts
  - voice-cloning
  - qwen3-tts
  - multilingual
  - synthetic
task_categories:
  - text-to-speech
  - automatic-speech-recognition
task_ids: []
---

![banner](https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/b205b24e-09ab-4653-814f-ce4fda2a14b4.png)

This dataset is a remastered version of
[`Reubencf/multilingual-synthetic-tts`](https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts)
prepared using [Adaption's](https://adaptionlabs.ai/app/auth) Adaptive Data platform.

# Multilingual Speech (Adaption)

**10,274 audio + text rows** selected from the original 68,677-clip
multilingual synthetic speech corpus, with Adaption-sharpened
`enhanced_prompt` and `enhanced_completion` columns. Every row carries
the synthesised audio, the ground-truth text, and language/style/voice
metadata — ready for speech SFT.

## Original dataset (for context)

A large-scale synthetic multilingual speech dataset — **68,677 clips
across 9 languages**, generated with **Qwen3-TTS-12Hz-1.7B-Base** using
zero-shot voice cloning from 5 reference speakers. Intended for training
and evaluating TTS, ASR, voice conversion, and multilingual speech
models. Each clip is paired with the ground-truth text and metadata
(language, style, voice).

### Original dataset summary

- **Total clips**: 68,677
- **Languages**: 9 (en, ja, zh, ko, de, es, fr, ru, pt)
- **Voices**: 5 (zero-shot cloned)
- **Audio format**: WAV, 12 kHz mono
- **Sentence source**: LLM-generated prompts spanning conversational
  speech, informational/technical text, emotional utterances, and
  traditional proverbs.
- **Full corpus**:
  [`Reubencf/multilingual-synthetic-tts`](https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts)

## This Adaption dataset — size

**10,274 rows** (subsampled from 68,677 for the Adaption pipeline,
instruction-tuning format).

## Language split (full breakdown)

Unlike the Adaption auto-stats line (which surfaces only the top three),
the actual distribution spans all 9 source languages:

| Language | Code | Rows | Share |
|---|---|---:|---:|
| Japanese | `ja` | 2,088 | 20.3 % |
| Russian | `ru` | 1,363 | 13.3 % |
| German | `de` | 1,343 | 13.1 % |
| Korean | `ko` | 1,217 | 11.8 % |
| Spanish | `es` | 1,185 | 11.5 % |
| Portuguese | `pt` | 814 | 7.9 % |
| Mandarin Chinese | `zh` | 811 | 7.9 % |
| English | `en` | 772 | 7.5 % |
| French | `fr` | 681 | 6.6 % |
| **Total** | | **10,274** | 100 % |

### Domain
- Personal-growth (12%)
- Architecture-design (10%)
- Science (8%)

### Tone
- Informative (28%)
- Helpful (10%)
- Philosophical (8%)

## Schema

| Column | Type | Meaning |
|---|---|---|
| `audio` | Audio | Synthesised waveform (WAV, 12 kHz mono) |
| `text` | string | Ground-truth text spoken in the clip |
| `language` | string | ISO-639-1 language code |
| `language_name` | string | Human-readable language name |
| `style` | string | Prompt style (conversational / informational / emotional / proverbs / …) |
| `voice` | string | Which of the 5 cloned voices was used |
| `sample_rate` | int | Native sampling rate |
| `enhanced_prompt` | string | Adaption-sharpened prompt |
| `enhanced_completion` | string | Adaption-sharpened completion |

## Intended Use

- TTS instruction tuning and voice-cloning model fine-tuning.
- Multilingual ASR training / data augmentation.
- Cross-lingual voice-conversion research.
- Speech-language model evaluation across nine languages.

## Limitations

- All audio is synthetic (Qwen3-TTS), so phonetic coverage reflects the
  TTS model's strengths and artifacts rather than real speaker variation.
- Voices are zero-shot clones of 5 reference speakers — speaker diversity
  is limited.
- Emotional and technical styles are LLM-generated and may sound
  stylistically homogeneous compared to organic human speech.
- Adaption's sharpening was performed by a text model; the `audio` column
  itself was not regenerated — only the prompt/completion text was
  improved.

## License

**CC-BY-4.0**. Synthesised audio and Adaption-generated text columns are
released for open research. Credit both this dataset and
`Reubencf/multilingual-synthetic-tts` if you use it.

## Related

- Original corpus (68,677 clips, 9 languages, full audio):
  [`Reubencf/multilingual-synthetic-tts`](https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts)
- Adaption collection:
  [`Reubencf/proper-adaption`](https://huggingface.co/collections/Reubencf/proper-adaption)

## Evaluation Results

- **Quality Gains:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/bc2eab2a-4505-4a5f-be67-b6ebe5af0e95.png" alt="QualityGains" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Grade Improvement:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/57b92cfb-a506-4b52-9c50-6f4a29edd4e3.png" alt="Grade" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Percentile Chart:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/84849bee-e3cd-4bc7-8f4f-a0f355ea45ea.png" alt="Percentile Chart" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

## Citation

If you use this dataset in your research or downstream work, please cite:

```bibtex
@misc{adaption_multilingual_speech_2026,
  author       = {Fernandes, Reuben Chagas},
  title        = {Adaption Multilingual Speech: TTS Subset with Enhanced Prompts/Completions},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Reubencf/Adaption-multilingual-speech}}
}
```

APA-style:

> Reuben Chagas Fernandes (2026). *Adaption Multilingual Speech: TTS Subset with Enhanced Prompts/Completions* [Dataset]. Hugging Face. https://huggingface.co/datasets/Reubencf/Adaption-multilingual-speech

