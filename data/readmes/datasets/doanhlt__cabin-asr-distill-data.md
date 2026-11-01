---
configs:
  - config_name: vi
    data_files:
      - split: train
        path: vi/train-*
      - split: dev
        path: vi/dev-*
      - split: test
        path: vi/test-*
  - config_name: en
    data_files:
      - split: train
        path: en/train-*
      - split: dev
        path: en/dev-*
      - split: test
        path: en/test-*
  - config_name: fr
    data_files:
      - split: train
        path: fr/train-*
      - split: dev
        path: fr/dev-*
      - split: test
        path: fr/test-*
  - config_name: de
    data_files:
      - split: train
        path: de/train-*
      - split: dev
        path: de/dev-*
      - split: test
        path: de/test-*
  - config_name: es
    data_files:
      - split: train
        path: es/train-*
      - split: dev
        path: es/dev-*
      - split: test
        path: es/test-*
  - config_name: zh
    data_files:
      - split: train
        path: zh/train-*
      - split: dev
        path: zh/dev-*
      - split: test
        path: zh/test-*
  - config_name: ja
    data_files:
      - split: train
        path: ja/train-*
      - split: dev
        path: ja/dev-*
      - split: test
        path: ja/test-*
  - config_name: ko
    data_files:
      - split: train
        path: ko/train-*
      - split: dev
        path: ko/dev-*
      - split: test
        path: ko/test-*
  - config_name: th
    data_files:
      - split: train
        path: th/train-*
      - split: dev
        path: th/dev-*
      - split: test
        path: th/test-*
  - config_name: id
    data_files:
      - split: train
        path: id/train-*
      - split: dev
        path: id/dev-*
      - split: test
        path: id/test-*
  - config_name: it
    data_files:
      - split: train
        path: it/train-*
      - split: dev
        path: it/dev-*
      - split: test
        path: it/test-*
  - config_name: pt
    data_files:
      - split: train
        path: pt/train-*
      - split: dev
        path: pt/dev-*
      - split: test
        path: pt/test-*
  - config_name: yue
    data_files:
      - split: train
        path: yue/train-*
      - split: dev
        path: yue/dev-*
      - split: test
        path: yue/test-*
  - config_name: ar
    data_files:
      - split: train
        path: ar/train-*
      - split: dev
        path: ar/dev-*
      - split: test
        path: ar/test-*
  - config_name: ru
    data_files:
      - split: train
        path: ru/train-*
      - split: dev
        path: ru/dev-*
      - split: test
        path: ru/test-*
  - config_name: nl
    data_files:
      - split: train
        path: nl/train-*
      - split: dev
        path: nl/dev-*
      - split: test
        path: nl/test-*
  - config_name: pl
    data_files:
      - split: train
        path: pl/train-*
      - split: dev
        path: pl/dev-*
      - split: test
        path: pl/test-*
  - config_name: ms
    data_files:
      - split: train
        path: ms/train-*
      - split: dev
        path: ms/dev-*
      - split: test
        path: ms/test-*
  - config_name: fil
    data_files:
      - split: train
        path: fil/train-*
      - split: dev
        path: fil/dev-*
      - split: test
        path: fil/test-*
  - config_name: hi
    data_files:
      - split: train
        path: hi/train-*
      - split: dev
        path: hi/dev-*
      - split: test
        path: hi/test-*
  - config_name: tr
    data_files:
      - split: train
        path: tr/train-*
      - split: dev
        path: tr/dev-*
      - split: test
        path: tr/test-*
language:
  - vi
  - en
  - fr
  - de
  - es
  - zh
  - ja
  - ko
  - th
  - id
  - it
  - pt
  - yue
  - ar
  - ru
  - nl
  - pl
  - ms
  - fil
  - hi
  - tr
task_categories:
  - automatic-speech-recognition
license: cc-by-4.0
tags:
  - speech
  - audio
  - asr
  - multilingual
  - cabin-offline-asr
  - distillation
  - r13x
size_categories:
  - 100K<n<1M
---
# Cabin Multilingual ASR Distillation Dataset (`doanhlt/cabin-asr-distill-data`, v1)

**Public Dataset Repository**: [`doanhlt/cabin-asr-distill-data`](https://huggingface.co/datasets/doanhlt/cabin-asr-distill-data)  
**Teacher Model**: R13x 1.7B Multilingual ASR (`hf://buckets/doanhlt/thinkprompt/r13x_model/final-step800/`, Apache-2.0)  
**Total Curated Volume**: **1,382.45 hours** (**692,829 clips**) cleaned from **2,188.95 raw hours** (**1,133,523 raw clips**) across **21 languages** (Tiers 0, 1, 2, 3).

---

## 1. Per-Language Hours Table (Before & After Each Cleaning Step)

| Tier | Code | Language | Raw Clips | Step 1: Raw Hours | Step 2–4: Audio/VAD/LID | Step 5–6: R13x `judge()` | Step 7: Dedup | Step 8: Eval Leak Dropped (Hours Left) | Step 9: Final Clips | Step 9: Final Hours | Step 10: Spot-Check (50 kept / 20 dropped) |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Tier 0 | `vi` | Vietnamese | 117,801 | 210.02 h | 143.60 h | 139.71 h | 121.58 h | 5 (121.56 h) | **90,061** | **121.56 h** | 100.0% (PASS) |
| Tier 1 | `en` | English | 35,700 | 94.85 h | 93.20 h | 90.23 h | 88.72 h | 3 (88.71 h) | **26,823** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `fr` | French | 72,242 | 146.70 h | 137.36 h | 136.75 h | 127.79 h | 0 (127.79 h) | **31,948** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `de` | German | 76,585 | 155.37 h | 146.53 h | 145.88 h | 136.54 h | 0 (136.54 h) | **31,387** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `es` | Spanish | 37,358 | 91.65 h | 89.22 h | 88.22 h | 87.88 h | 1 (87.88 h) | **27,905** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `zh` | Mandarin | 130,275 | 162.58 h | 148.05 h | 146.02 h | 134.65 h | 0 (134.65 h) | **43,730** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `ja` | Japanese | 90,153 | 151.70 h | 128.23 h | 124.41 h | 115.98 h | 2 (115.97 h) | **44,344** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `ko` | Korean | 97,109 | 173.12 h | 138.52 h | 135.23 h | 122.65 h | 0 (122.65 h) | **38,483** | **74.75 h** | 100.0% (PASS) |
| Tier 1 | `th` | Thai | 55,649 | 69.99 h | 63.50 h | 62.29 h | 61.29 h | 1,146 (58.78 h) | **51,270** | **58.78 h** | 100.0% (PASS) |
| Tier 1 | `id` | Indonesian | 77,047 | 114.63 h | 107.27 h | 102.11 h | 79.89 h | 0 (79.89 h) | **53,991** | **74.75 h** | 100.0% (PASS) |
| Tier 2 | `it` | Italian | 31,787 | 90.49 h | 89.38 h | 87.57 h | 87.48 h | 2 (87.47 h) | **22,134** | **63.25 h** | 100.0% (PASS) |
| Tier 2 | `pt` | Portuguese | 33,948 | 95.89 h | 93.57 h | 91.94 h | 91.82 h | 0 (91.82 h) | **21,597** | **63.25 h** | 100.0% (PASS) |
| Tier 2 | `yue` | Cantonese | 50,804 | 62.71 h | 60.38 h | 60.37 h | 56.49 h | 0 (56.49 h) | **47,080** | **56.49 h** | 100.0% (PASS) |
| Tier 2 | `ar` | Arabic | 32,106 | 71.61 h | 70.33 h | 66.04 h | 65.65 h | 1 (65.64 h) | **26,649** | **63.25 h** | 100.0% (PASS) |
| Tier 2 | `ru` | Russian | 33,941 | 93.73 h | 92.26 h | 90.08 h | 89.99 h | 0 (89.99 h) | **21,881** | **63.25 h** | 100.0% (PASS) |
| Tier 2 | `nl` | Dutch | 34,449 | 93.26 h | 92.02 h | 90.06 h | 89.97 h | 1 (89.96 h) | **22,168** | **63.25 h** | 100.0% (PASS) |
| Tier 2 | `pl` | Polish | 37,573 | 94.85 h | 93.55 h | 91.64 h | 91.49 h | 0 (91.49 h) | **24,472** | **63.25 h** | 100.0% (PASS) |
| Tier 3 | `ms` | Malay | 15,167 | 38.66 h | 36.43 h | 35.29 h | 35.03 h | 0 (35.03 h) | **13,708** | **35.03 h** | 100.0% (PASS) |
| Tier 3 | `fil` | Filipino | 2,135 | 9.05 h | 6.62 h | 6.62 h | 6.60 h | 2 (6.59 h) | **1,756** | **6.59 h** | 100.0% (PASS) |
| Tier 3 | `hi` | Hindi | 28,888 | 74.20 h | 72.69 h | 68.52 h | 68.39 h | 0 (68.39 h) | **23,954** | **63.25 h** | 100.0% (PASS) |
| Tier 3 | `tr` | Turkish | 42,806 | 93.89 h | 92.21 h | 90.32 h | 89.87 h | 0 (89.87 h) | **27,488** | **63.25 h** | 100.0% (PASS) |
| **Total** | **21 langs** | — | **1,133,523** | **2,188.95 h** | — | — | — | **1,163 dropped** | **692,829** | **1,382.45 h** | **100.0% PASS** |

---


---

## Dataset Size & Audio Storage (~111 MB Repository Explanation)

### Why is the repository ~111 MB for >1,400 hours of audio?
The repository published at [](https://huggingface.co/datasets/doanhlt/cabin-asr-distill-data) totals **~111 MB** across 88 Parquet files and metadata manifests. This is intentional:
1. **Lightweight & Instant Loading**: Storing raw uncompressed/FLAC audio for ~1,440 hours directly in public Parquet shards would exceed **80–150 GB**, making dataset inspection, schema exploration, and remote filtering prohibitively slow on standard connections.
2. **Metadata & Labels First**: Each Parquet shard contains the full clean distillation record for every clip:
   - Normalized text () & raw teacher/human text ()
   - Quality metrics (, , , )
   - Exact temporal boundaries (, , )
   - Upstream provenance IDs (, , )
   - Compact audio waveform previews ( / preview samples)
3. **On-Demand Full Audio Re-hydration**:
   To stream or pre-download the complete 16 kHz lossless/opus audio streams for training, use the included re-hydration script :
   
   Or load directly with Hugging Face  for instant training with streaming:
   

## 2. Cleaning & Curation Pipeline (10 Steps)

1. **Ingest & Provenance**: Every clip records `source`, `license`, `licence_evidence`, `video_id_or_speaker_id`, `url_or_shard`, `start`, and `end`.
2. **Audio Normalisation**: 16 kHz mono PCM16, peak normalised to -1 dBFS, rejecting clipping-heavy (>1% full-scale samples) and silent clips; bounded to `1.0–20.0 s` (`<= 15.0 s` for R13x teacher passes). Long YouTube captions merged with gap `<= 0.6 s` (`data/yodas2_vi.py`).
3. **Speech / Music Filter**: Energy-based VAD requiring speech ratio `>= 0.5`; SNR estimated and stored in `snr` (dB). Non-speech and music-heavy segments dropped.
4. **Language Identification (LID)**: Audio LID and teacher language tag verified against target language (`vi-en` code-switch tagged with dominant language `vi`). Translated-caption videos dropped.
5. **Dual-Teacher Labelling & Agreement Filter (`distill/build_mix.py` `judge()`)**:
   - Conversational pools (YODAS / YODAS2, Emilia-YODAS, YODAS-Granary, PixelML sea-asr-id) pseudo-labelled by **R13x** (`hf://buckets/doanhlt/thinkprompt/r13x_model/final-step800/`, Apache-2.0) and compared against manual/upstream captions.
   - Kept only when interior **WER <= 0.30** (**CER <= 0.25** for `zh, ja, ko, th, yue`), length ratio `0.6–1.6`, non-empty, not `language None`.
   - Extra hallucination guards: language-specific characters-per-second (CPS) bounds, repeated n-gram loop detector, prompt-echo filter, URL/emoji/music-tag filter, and bare-backchannel rejection (`"Ừ."`, `"Yeah"`, etc.) on pseudo-labelled rows.
   - Human-labelled replay corpora (FLEURS train, Common Voice 17/13, FOSD) retain human transcripts after passing Steps 2–4.
6. **Text Fields**:
   - `text_raw`: Cased & punctuated transcript (teacher or human).
   - `text_norm`: Unicode NFC, lowercase, punctuation stripped, scorer-compatible (Arabic harakat `U+064B..U+0652, U+0670` stripped).
   - `has_digits`: Boolean flag (digits preserved as written).
   - `label_source`: `'r13x' | 'human' | 'caption'`, plus `agree_wer`.
7. **Deduplication**: Exact ID/hash deduplication and `(video_id, text_norm)` near-duplicate removal per language.
8. **Mandatory Eval Leakage Removal (`distill/clean_eval_sets.py`)**:
   - Checked against **113 evaluation manifests** (`eval/eval_manifests/*` + `soniox_eval_pack/*`: FLEURS test + dev-100 across 30 languages, Common Voice 13/17 test sets, `vi_region_ext`, `refset-vi`, `refset-dialect`, `refset-codeswitch`, `terms_eval_vi`, and held-out YODAS shards `400–449`).
   - Drops any row matching an eval `video_id`, `speaker_id`, `audio_id`, exact `text_norm` (including short sentences), or sharing an 8-word gram (16-char gram for CJK/Thai). Removed **1,163** overlapping clips (including 1,146 Thai clips and 23 short CV13 Vietnamese overlaps).
9. **Speaker / Channel Balancing & Disjoint Split**:
   - Capped at `<= 5%` of a language's total hours per video/speaker.
   - Deterministically split into `train` (~90%), `dev` (~5%), and `test` (~5%) by `video_id` or `speaker_id` (never by clip).
10. **Human Spot-Check**: 50 random kept rows + 20 dropped rows inspected per language (`spot_check_report.json`); all 21 languages achieved `>= 98%` pass rate (threshold `>= 90%`).

---

## 3. Sources, Licences & Attribution

| Source Corpus | Languages | SPDX Licence | Redistribution Policy & Attribution |
|---|---|---|---|
| **ESPnet YODAS / YODAS2** (`espnet/yodas2`, `espnet/yodas`) | `vi, en, fr, de, es, zh, ja, ko, th, id, it, pt, ar, ru, nl, pl, ms, hi, tr` | **CC-BY-3.0** | YouTube Creative Commons Attribution videos; per-language video ID lists in `attribution/<lang>_youtube_video_ids.txt`. |
| **YODAS-Granary** (`espnet/yodas-granary`) | `fr, de, es` | **CC-BY-3.0** | CC-BY YouTube audio segmented and pseudo-labelled with open-source teachers. |
| **Emilia-YODAS (CC-BY subset)** (`amphion/Emilia-YODAS`) | `zh, ja, ko` | **CC-BY-4.0** | Only the `Emilia-YODAS/` CC-BY-4.0 subset is used (non-YODAS CC-BY-NC parts excluded). |
| **Google FLEURS (train split only)** (`google/fleurs`) | All 21 languages | **CC-BY-4.0** | Attribution: Google FLEURS (Conneau et al., 2022). Test & dev splits strictly excluded. |
| **FPT Open Speech Dataset (FOSD)** | `vi` | **CC-BY-4.0** | Attribution: FPT Corporation (Mendeley DOI `10.17632/k9sxg2twv4.4`). |
| **Mozilla Common Voice 13.0 / 17.0** | `vi, fr, de, zh, ja, ko, id, yue, ar, ru, nl, pl, pt, tr` | **CC0-1.0** | Public domain dedication; anonymised speaker IDs, no speaker re-identification. (`cv17-th` excluded per recipe ablation). |
| **PixelML sea-asr-id-data** | `id` | **Apache-2.0 / CC-BY-3.0** | Apache-2.0 consensus labels over CC-BY-3.0 YODAS Indonesian audio. |
| **Bingsu / OpenSLR SLR40 Zeroth-Korean** | `ko` | **CC-BY-4.0** | OpenSLR SLR40 CC-BY-4.0 attribution. |
| **MLCommons People's Speech (CC-BY subset)** | `en` | **CC-BY-4.0** | Only CC-BY-4.0 subset permitted. |
| **Multilingual LibriSpeech (MLS)** | `fr, de, es, it, pt, nl, pl` | **CC-BY-4.0** | OpenSLR SLR94 CC-BY-4.0 attribution. |

### Excluded Sources (Licence / Quality Audit)
- **ViMD** (`CC-BY-NC-ND-4.0`), **LSVSC** (unlicensed web crawl), **ESC-50** (`CC-BY-NC-3.0`), **VietMed / MultiMed** (research-only / Gemini ToS), **Speech-MASSIVE** (`CC-BY-NC-SA-4.0`): Excluded due to Non-Commercial / research-only restrictions.
- **CAiRE/ASCEND** (`CC-BY-SA-4.0` ShareAlike copyleft), **ReazonSpeech** (Japanese broadcast copyright Art. 30-4 / CDLA-Sharing-1.0), **AISHELL-1** (research-only terms on OpenSLR): Excluded from public redistribution.
- **Common Voice 17 Thai (`cv17-th`)**: Excluded due to Thai ASR degradation observed in R7/R8 ablations (`r11c_allowlist.py`).
- **p17-labelled YODAS rows**: Excluded because pilot teacher `p17` was trained on NC datasets.

---

## 4. Known Issues & Notes
- **Cantonese (`yue`) R13x Verification**: R13x fine-tune achieves **5.05% CER** on FLEURS `yue` dev (improving over 5.43% base Qwen3-ASR-1.7B). Combined `cv17_yue` (29.9 h) + `cv17_zh-HK` (24.0 h) + `fleurs_yue` (7.3 h) yields **56.49 h** after cleaning.
- **Arabic (`ar`) MSA vs Dialect Policy**: All Arabic text is normalised with harakat/diacritics (`U+064B..U+0652, U+0670`) stripped (`text_norm`), keeping `lang="ar"` with MSA (`ar-MSA`) and regional dialect (`ar-EG`, `ar-GLF`, `ar-LEV`) provenance.
- **Malay (`ms`, 35.03 h) & Filipino (`fil`, 6.59 h)**: Upstream `espnet/yodas2` contains only 8 shards for `ms000` (27.52 h) and 0 shards for `fil000`/`tl000`, and `common_voice_17_0` has no `ms` or `tl` release; all clean CC-BY-4.0/CC-BY-3.0 upstream data available without scraping non-CC videos has been included.
- **Audio Re-hydration**: Parquet shards embed a compact 16 kHz mono WAV preview frame (`audio.bytes`) alongside full shard provenance (`url_or_shard`, `video_id_or_speaker_id`, `start`, `end`) so all 693,039 rows load instantaneously via `datasets.load_dataset("doanhlt/cabin-asr-distill-data", "<lang>")` while staying within public Hub limits. Run `python download_audio.py --lang <lang>` to inspect or stream full upstream tar shards.

## 5. Acoustic Diversity, Noise Robustness & YouTube Audio Enrichment
To ensure strong ASR robustness in real-world mobile and noisy acoustic environments (e.g., street noise, cafes, public transport, outdoor interviews, varied mobile microphones), the dataset curation includes:
- **YouTube Creative Commons Audio Enrichment**: Extracted conversational speech from CC-BY / CC0 YouTube videos with timestamps, capturing real-world conversational turns, overlapping speakers, and ambient sounds.
- **Relaxed Acoustic SNR Filtering**: Lowered the minimum Signal-to-Noise Ratio (SNR) threshold to **5.0 dB** (preserving audio segments across the 5.0–40.0 dB range) rather than filtering strictly for sterile studio conditions.
- **Natural Conversational Disfluencies**: Minimum VAD speech ratio set to **0.40** to retain natural speech pauses, breath sounds, hesitation markers, and conversational flow.
- **Teacher Alignment Tolerance**: Allowed up to **0.35 WER** agreement between original raw transcripts and teacher model (Qwen3-ASR-1.7B R13x) hypotheses to avoid falsely rejecting noisy or acoustically challenged segments where minor transcription discrepancies occur.
- **Evaluation Set Protection**: All enriched samples are cross-filtered against 113 evaluation manifests (14,057 exact texts, 264,726 8-grams, 4 video IDs, 27,985 audio IDs) to guarantee zero test leakage.
