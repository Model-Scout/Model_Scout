---
license: other
license_name: ztts1-eval-derived
license_link: https://github.com/Zyphra/ZTTS1-Eval
language:
- en
- zh
- ko
- ja
- es
- ru
- de
tags:
- tts
- zero-shot-tts
- speech-evaluation
- cartesia
configs:
- config_name: comparison_full500
  data_files:
  - split: train
    path: comparison_full500/train-*
- config_name: comparison_s150
  data_files:
  - split: train
    path: comparison_s150/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: elevenlabs_v3_clone_full500
  data_files:
  - split: train
    path: elevenlabs_v3_clone_full500/train-*
- config_name: elevenlabs_v3_clone_s150
  data_files:
  - split: train
    path: elevenlabs_v3_clone_s150/train-*
- config_name: openai_gpt4o_mini_tts_full500
  data_files:
  - split: train
    path: openai_gpt4o_mini_tts_full500/train-*
- config_name: openai_gpt4o_mini_tts_s150
  data_files:
  - split: train
    path: openai_gpt4o_mini_tts_s150/train-*
- config_name: qwen3_tts_base_clone_full500
  data_files:
  - split: train
    path: qwen3_tts_base_clone_full500/train-*
- config_name: qwen3_tts_base_clone_s150
  data_files:
  - split: train
    path: qwen3_tts_base_clone_s150/train-*
- config_name: qwen3_tts_customvoice_full500
  data_files:
  - split: train
    path: qwen3_tts_customvoice_full500/train-*
- config_name: qwen3_tts_customvoice_s150
  data_files:
  - split: train
    path: qwen3_tts_customvoice_s150/train-*
dataset_info:
- config_name: comparison_full500
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: target_text
    dtype: string
  - name: prompt_text
    dtype: string
  - name: audio_reference
    dtype: audio
  - name: audio_cartesia
    dtype: audio
  - name: cartesia_transcript
    dtype: string
  - name: cartesia_wer
    dtype: float32
  - name: cartesia_cer
    dtype: float32
  - name: cartesia_sim
    dtype: float32
  - name: cartesia_qwen_transcript
    dtype: string
  - name: cartesia_qwen_wer
    dtype: float32
  - name: audio_elevenlabs
    dtype: audio
  - name: elevenlabs_transcript
    dtype: string
  - name: elevenlabs_wer
    dtype: float32
  - name: elevenlabs_cer
    dtype: float32
  - name: elevenlabs_sim
    dtype: float32
  - name: elevenlabs_qwen_transcript
    dtype: string
  - name: elevenlabs_qwen_wer
    dtype: float32
  - name: audio_openai
    dtype: audio
  - name: openai_transcript
    dtype: string
  - name: openai_wer
    dtype: float32
  - name: openai_cer
    dtype: float32
  - name: openai_sim
    dtype: float32
  - name: openai_qwen_transcript
    dtype: string
  - name: openai_qwen_wer
    dtype: float32
  - name: audio_qwen3tts
    dtype: audio
  - name: qwen3tts_transcript
    dtype: string
  - name: qwen3tts_wer
    dtype: float32
  - name: qwen3tts_cer
    dtype: float32
  - name: qwen3tts_sim
    dtype: float32
  - name: qwen3tts_qwen_transcript
    dtype: string
  - name: qwen3tts_qwen_wer
    dtype: float32
  - name: audio_qwen3base
    dtype: audio
  - name: qwen3base_transcript
    dtype: string
  - name: qwen3base_wer
    dtype: float32
  - name: qwen3base_cer
    dtype: float32
  - name: qwen3base_sim
    dtype: float32
  - name: qwen3base_qwen_transcript
    dtype: string
  - name: qwen3base_qwen_wer
    dtype: float32
  splits:
  - name: train
    num_bytes: 9851375901
    num_examples: 3500
  download_size: 9852319218
  dataset_size: 9851375901
- config_name: comparison_s150
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: target_text
    dtype: string
  - name: prompt_text
    dtype: string
  - name: audio_reference
    dtype: audio
  - name: audio_cartesia
    dtype: audio
  - name: audio_elevenlabs
    dtype: audio
  - name: cartesia_transcript
    dtype: string
  - name: elevenlabs_transcript
    dtype: string
  - name: cartesia_wer
    dtype: float32
  - name: cartesia_cer
    dtype: float32
  - name: cartesia_sim
    dtype: float32
  - name: elevenlabs_wer
    dtype: float32
  - name: elevenlabs_cer
    dtype: float32
  - name: elevenlabs_sim
    dtype: float32
  splits:
  - name: train
    num_bytes: 2968636958
    num_examples: 1050
  download_size: 2968948960
  dataset_size: 2968636958
- config_name: default
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 2170521295
    num_examples: 3500
  download_size: 2170054032
  dataset_size: 2170521295
- config_name: elevenlabs_v3_clone_full500
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 1422860075
    num_examples: 3500
  download_size: 1422335212
  dataset_size: 1422860075
- config_name: elevenlabs_v3_clone_s150
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 426688499
    num_examples: 1050
  download_size: 426534049
  dataset_size: 426688499
- config_name: openai_gpt4o_mini_tts_full500
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 1767152993
    num_examples: 3500
  download_size: 1766638494
  dataset_size: 1767152993
- config_name: openai_gpt4o_mini_tts_s150
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 527573875
    num_examples: 1050
  download_size: 527431539
  dataset_size: 527573875
- config_name: qwen3_tts_base_clone_full500
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 1551628767
    num_examples: 3500
  download_size: 1551038774
  dataset_size: 1551628767
- config_name: qwen3_tts_base_clone_s150
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 449712998
    num_examples: 1050
  download_size: 449548401
  dataset_size: 449712998
- config_name: qwen3_tts_customvoice_full500
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 1721984638
    num_examples: 3500
  download_size: 1721424440
  dataset_size: 1721984638
- config_name: qwen3_tts_customvoice_s150
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: prompt_text
    dtype: string
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_bytes: 513169955
    num_examples: 1050
  download_size: 513014772
  dataset_size: 513169955
---

# Cartesia sonic-preview — ZTTS1-Eval zero-shot synthesis + scores

Zero-shot voice-cloning TTS on the **ZTTS1-Eval** benchmark (Zyphra, FLEURS-R
based), now at **full scale: 7 languages x 500 utterances = 3,500 per engine**,
five engines side by side:

| engine | mode | model |
|---|---|---|
| Cartesia | zero-shot clone | `sonic-preview` (Sonic-3.6 beta at generation time) |
| ElevenLabs | zero-shot clone (IVC) | `eleven_v3` |
| Qwen3-TTS **Base** | zero-shot clone | `Qwen/Qwen3-TTS-12Hz-1.7B-Base` (self-hosted, vLLM-Omni) |
| OpenAI | preset voices | `gpt-4o-mini-tts` (11 voices, md5-rotated) |
| Qwen3-TTS **CustomVoice** | preset voices | `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` (self-hosted) |

Clone engines copy each utterance's prompt speaker; preset engines read the
same texts with fixed built-in voices (their SIM is not a cloning signal).
Dual scoring: ① **official ZTTS1 stack** — Qwen/Qwen3-ASR-1.7B via vLLM,
`utils/run_wer.py` normalization (zh/ja/ko character-tokenized), WER_CLIP;
② Whisper large-v3 WER/CER + WavLM-SV speaker similarity (Seed-TTS-eval
protocol).

## Configs

Full-500 configs (one row per utterance, audio + texts + both scorings):

| config | rows | what it is |
|---|--:|---|
| `default` | 3500 | **Cartesia sonic-preview, full 500/lang x 7** |
| `elevenlabs_v3_clone_full500` | 3500 | ElevenLabs eleven_v3 IVC clone |
| `qwen3_tts_base_clone_full500` | 3500 | Qwen3-TTS-1.7B Base zero-shot clone |
| `openai_gpt4o_mini_tts_full500` | 3500 | OpenAI gpt-4o-mini-tts preset |
| `qwen3_tts_customvoice_full500` | 3500 | Qwen3-TTS-1.7B CustomVoice preset |
| `comparison_full500` | 3500 | **side-by-side listening**: `audio_reference` + one audio column per engine, with per-utterance Whisper WER/CER/SIM and official Qwen transcripts/WER |

Engine configs share one schema (`utt`, `language`, `audio`, `target_text`,
`asr_transcript`, `wer`, `cer`, `sim`, `prompt_text`, `reference_voice`,
`model_id`, `mode`). The `*_s150` configs are the earlier 150-per-language
subsets (strict subsets of the full500 rows, kept for continuity); the
`comparison_s150` config likewise. Raw wav trees live under `audio*/`;
per-utterance score files under `scores/full500/` and `scores/qwen/full500/`.

## Main result — official Qwen3-ASR WER_CLIP %, 500/lang x 7

| lang | Cartesia (clone) | ElevenLabs (clone) | Qwen3 Base (clone) | OpenAI (preset) | Qwen3 CustomVoice (preset) |
|---|--:|--:|--:|--:|--:|
| en | **2.07** | 2.34 | 2.47 | 2.12 | 2.17 |
| zh | 4.09 | 3.86 | 3.76 | **2.98** | 3.02 |
| ko | **2.51** | 3.53 | 2.59 | 3.46 | 2.94 |
| ja | **3.42** | 3.90 | 3.84 | 3.73 | 4.58 |
| es | 2.37 | 3.26 | 2.36 | **2.27** | 5.15 |
| ru | **5.36** | 7.48 | 5.85 | 5.96 | 7.86 |
| de | **3.01** | 3.43 | 3.25 | 3.31 | 7.24 |
| **avg** | **3.26** | 3.97 | 3.45 | 3.40 | 4.71 |

Speaker similarity among the **cloning** engines (WavLM-SV vs the prompt
speaker, same 500/lang):

| lang | Cartesia | Qwen3 Base | ElevenLabs |
|---|--:|--:|--:|
| en | **0.9615** | 0.9589 | 0.9415 |
| zh | **0.9664** | 0.9569 | 0.9367 |
| ko | **0.9759** | 0.9704 | 0.9452 |
| ja | **0.9770** | 0.9703 | 0.9500 |
| es | **0.9760** | 0.9704 | 0.9554 |
| ru | **0.9782** | 0.9669 | 0.9570 |
| de | **0.9804** | 0.9773 | 0.9662 |

### Takeaways (full 500/lang)

* **Cartesia is the best cloning engine overall**: first on SIM in all seven
  languages and first on intelligibility in en/ko/ja/ru/de (best 7-language
  average, 3.26). Its en 2.07 sits at the top of the ZTTS1 leaderboard range.
* **Qwen3-TTS Base is a strong open-weights runner-up**: beats ElevenLabs on
  SIM in all seven languages and on WER_CLIP in 6/7 (everything but en), and
  takes the best zh/es intelligibility among clone engines. Caveat: rare
  runaway generations (>60s; trimmed for scoring).
* **ElevenLabs eleven_v3** trails both clone rivals on SIM everywhere and only
  edges Cartesia on zh WER. Note the ~3-20s ZTTS1 prompts are shorter than its
  recommended 1-2 min IVC reference.
* **Preset engines**: OpenAI's fixed voices win zh/es outright (no cloning
  burden) and average 3.40; Qwen3 CustomVoice is competitive only where it has
  a native built-in speaker (en/zh/ko) and degrades sharply on es/ru/de (7.2-7.9).
* Versus the earlier 150-sample: every conclusion holds except zh, where
  the full set flips Cartesia (4.09) slightly behind ElevenLabs (3.86) and
  Qwen3 Base (3.76) on WER_CLIP — the s150 zh subset was easier for Cartesia.

## Whisper-protocol reference (large-v3 WER/CER + SIM, 500/lang)

Whisper zh/ja whitespace WER is not meaningful (zh ground-truth clips floor at
~10-13 CER); use the official Qwen table above for cross-engine calls. CER %:

| lang | Cartesia | ElevenLabs | Qwen3 Base | OpenAI | Qwen3 CV |
|---|--:|--:|--:|--:|--:|
| en | 0.78 | 1.03 | 4.48 | 0.80 | 1.02 |
| zh | 9.91 | 14.06 | 11.82 | 9.86 | 9.93 |
| ko | 3.98 | 5.18 | 4.10 | 4.60 | 6.82 |
| ja | 4.54 | 4.69 | 4.57 | 4.88 | 5.65 |
| es | 0.86 | 1.14 | 0.94 | 0.98 | 3.16 |
| ru | 1.26 | 1.59 | 1.81 | 1.74 | 2.55 |
| de | 0.88 | 1.03 | 0.92 | 1.11 | 2.52 |

Per-utterance JSONs: `scores/full500/scores_<lang>_<engine>_full500.json`
(Whisper+SIM) and `scores/qwen/full500/<engine>_<lang>.json` (official ASR).

## Dataset / protocol notes

* Benchmark: [ZTTS1-Eval](https://github.com/Zyphra/ZTTS1-Eval) zero-shot set —
  FLEURS-R texts, one prompt clip per utterance (~3-20s), 500 utterances per
  language; en/zh/ko/ja/es/ru/de used here.
* Clone engines: per-utterance instant clone of the prompt speaker
  (Cartesia `/voices/clone`; ElevenLabs IVC; Qwen3 Base `ref_audio`+`ref_text`),
  synth of `target_text`, temp voices deleted after use.
* Preset engines: OpenAI voice rotated per utterance by md5 over 11 public
  voices; Qwen3 CustomVoice uses the model-card native speaker per language
  (Vivian/Ryan/Ono-Anna/Sohee; Ryan reads es/ru/de — no native speaker exists).
* `reference_voice` column: prompt clip id (clone engines) or preset voice name.
* Generation dates: 2026-08 (sonic-preview = Sonic-3.6 beta channel).

## License

Derived from ZTTS1-Eval (FLEURS-R); see the upstream repository for data
licensing. Synthetic audio is provided for research evaluation of the
respective TTS systems.
