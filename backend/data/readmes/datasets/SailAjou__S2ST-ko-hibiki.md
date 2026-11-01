---
license: other
license_name: mixed-source-redistribution-restricted
language:
- ko
- en
task_categories:
- translation
- automatic-speech-recognition
- text-to-speech
tags:
- speech-to-speech-translation
- simultaneous-translation
- korean
- english
- mimi
- hibiki
- s2st
pretty_name: "S2ST-ko-hibiki — Korean→English Simultaneous Speech-to-Speech"
size_categories:
- 1M<n<10M
viewer: false
extra_gated_prompt: >-
  This corpus is derived from several Korean speech datasets (AI-Hub,
  KlecSpeech, KsponSpeech, CoreaSpeech, Emilia, kosp2e) that each retain their
  own license. The upstream sources DO NOT permit redistribution — access here
  is granted on manual review for research use only, and you must hold your own
  agreements with the upstream providers where their terms require it.
---

# S2ST-ko-hibiki — Korean→English Simultaneous Speech-to-Speech Translation

A large-scale corpus for **Korean → English simultaneous (streaming)
speech-to-speech translation**, built to fine-tune a
[Hibiki](https://github.com/kyutai-labs/hibiki)-style streaming model. Each
item pairs **real Korean source speech** with an **English translation (text)**
and **synthesized English speech**, plus **Mimi neural-codec tokens** for both
languages and **word-level alignment timestamps** — so the whole set loads
directly into a streaming S2S training loop.

Backs the paper *TransOrder: Reinforcement Learning for Word Reordering in
Simultaneous Speech-to-Speech Translation* (SAIL, Ajou University).
<!-- ⚠️ CONFIRM final title / venue / authors before publishing -->

> **Access is gated (manual approval).** The upstream corpora state
> **redistribution is not permitted**; see Licensing.

---

## Composition

Training-ready segments in `packed_v2` (post-QC, evaluation ids excluded).
Hours are of the synthesized English audio unless noted.

| Source key | Official dataset | AI-Hub ID | Content | Speakers | Segments | EN hours |
|---|---|---|---|---:|---:|---:|
| `aihub130` | 한국인 대화음성 (Korean conversational speech) | 130 | 2-person dialogue (economy/daily/commerce) | (source meta) | 873,839 | 3,009 |
| `klec` | KlecSpeech 한국어 강의음성 (Korean lecture speech) | KlecSpeech | 20-domain lectures, 14 difficulty levels | 7,942 | 973,603 | 4,777 |
| `aihub71481` | 전문분야 심층인터뷰 (expert in-depth interviews) | 71481 | host/panel interviews (rich demographic meta) | ~2,679 interviews ⚠️ | 291,773 | 1,511 |
| `kspon` | KsponSpeech 한국어 음성 | KsponSpeech | spontaneous free speech | 2,000 (official) | 204,969 | 739 |
| `aihub637` | 감성·발화스타일별 음성합성 (SKT) | 637 | 9 emotions (neutral/anger/sadness/joy…) | 508 | 67,989 | 256 |
| `coreaspeech` | CoreaSpeech | (HuggingFace) | Korean speech | 799 | 116,603 | 600 |
| `aihub71668` | 라이브 스트리밍 영어 통번역 (live-stream EN interpretation) | 71668 | YouTuber native EN + KO clone-voice; **KO+EN both real** | 105 | 197,686 | 865 |
| `aihub031` | 방송콘텐츠 한-영 통·번역 음성 (broadcast interpretation) | 71379 | documentary/entertainment; KO + native EN | 59 | 114,778 | 395 |
| `aihub71261` | 한-영·한-중 음성발화 (KO-EN/KO-ZH utterances) | 71261 | native EN speech utterances | (source meta) | 26,842 | 94 |
| **Total** | | | | | **2,868,082** | **12,245.6** |

Totals across `packed_v2`: **2,868,082 segments · 6,275,250 members · KO
10,418.3 h · EN 12,245.6 h** (`notes/datacard_stats.json`).

<!-- ⚠️ CONFIRM: aihub71481 speaker count is inconsistent across sources
     (2,382 label registry vs 8,916 per-clip spk.txt vs 2,679 interviews).
     130 / 71261 speaker counts not yet extracted. -->

---

## Dataset structure

```
S2ST-ko-hibiki/
├── README.md
├── ko/                    # Korean source audio (tar.zst shards) — one folder per source key above
├── en/                    # English synthesized audio (OmniVoice)
├── packed_v2/             # ★ training-ready pack: KO+EN Mimi tokens + EN/KO text + delay anchors + ids
├── align/
│   ├── ko/                # KO word-level forced-alignment timestamps (MMS)
│   └── en/                # EN word-level forced-alignment timestamps (MMS)
├── code/                  # data-pipeline scripts (pack / synth / qc / align / train / eval / rl)
├── splits/                # frozen dev/test ids + Emilia eval set
└── stats/                 # per-source counts, durations, QC dumps
```

`packed_v2/` is the single canonical training artifact; per source it holds
`<key>.tok.bin` (Mimi RVQ tokens, KO+EN interleaved per frame), `<key>.txt.bin`
(English translation, SentencePiece), `<key>.kotext.txt` (Korean transcript),
`<key>.rows.npz` (offsets + delay anchors), `<key>.ids.txt`, and
`<key>.meta.json`.

### `ko/` folder → source mapping

Korean source audio is stored as `tar.zst` shards under `ko/<source key>/`.
Folder names follow the source keys above. Three keys differ from their earlier
raw-backup folder names:

| `ko/` folder | earlier raw-backup name | note |
|---|---|---|
| `klec` | `raw_aihub_ebs` | KlecSpeech (lecture speech) — **not** a broadcast set |
| `aihub031` | `raw_aihub71379_broadcast` | same corpus as AI-Hub 71379 (broadcast interpretation) |
| `aihub71668` | `raw_no_kor_data` | folder was mis-named; holds AI-Hub 71668 (+ an Emilia-KO latin subset) |

`ko/` also carries held-out-only Korean audio (`kosp2e`, `emilia_ko`) that
is **never used for training**. The raw audio for `aihub71261` is not included
in this backup (only its tokens/text/alignment are in `packed_v2`).

---

## How it was built

1. **Source speech** — real Korean recordings from the corpora above.
2. **Translation (KO→EN text)** — original English references where available,
   plus **Hunyuan-MT-7B re-translation**, scored with **CometKiwi QE** and
   merged **keep-max** (higher-QE of original vs. re-translation per segment).
3. **English speech synthesis** — rendered with **OmniVoice** (`lang=en`,
   `speed=0.9`, target duration matched to the source segment). The accented
   ("Konglish") delivery is an intentional, documented property, not a defect.
4. **Neural-codec tokenization** — both Korean and English audio encoded to
   **Mimi** RVQ tokens (12.5 Hz); English text tokenized with SentencePiece.
5. **Forced alignment** — Korean **word-level timestamps** via **MMS** forced
   alignment (used as the latency-reward clock in the paper).
6. **Quality control** — automatic language-ID screening drops segments whose
   synthesis came out non-English; text-contaminated segments (~0.97%) removed;
   foreign+high-WER cases re-synthesized once, then re-QC'd.
7. **Packing** — merged into the streaming grid (`packed_v2`) with per-segment
   delay anchors; evaluation ids held out.

### Translation quality (measured)
- **QE (CometKiwi-DA)** on the full ~7.4 M sentences: per-dataset mean ≈ 0;
  low-quality share (QE < −0.3) 0.00–1.26% (weakest: coreaspeech 1.26%,
  aihub71261 0.60%).
- **LaBSE cosine (KO↔EN, 2 k sample/dataset)**: mostly mean 0.75–0.78. Outliers
  with mis-alignment tails: **aihub71261 (19.3% below 0.5)**, aihub637 (9.4%) —
  aihub71261 also shows the largest KO/EN duration mismatch (48%).

---

## Splits

- **Train** — `packed_v2` (source-level split; evaluation material removed via
  `splits/exclude_from_train.*`, 80,755 segments).
- **Internal dev / test** — frozen id lists in `splits/` (seed 46,
  source-disjoint; two broadcast programs held fully unseen).
- **Emilia eval** — `splits/emilia_eval/`: 500 short (3–15 s) + 500 long
  (25–90 s) reference-free clips (DNSMOS-filtered).
- External benchmarks (FLEURS/FLoRes KO→EN, kosp2e) are referenced in the paper
  but not used for training.

---

## Licensing

⚠️ **This corpus aggregates material under several different upstream licenses,
and the upstream providers DO NOT permit redistribution.** It is published with
**manual-approval gating** for research use only.

- **AI-Hub** (`aihub130`, `aihub637`, `aihub031`/71379, `aihub71481`,
  `aihub71668`, `aihub71261`), **KlecSpeech** (`klec`), **KsponSpeech**
  (`kspon`): governed by their AI-Hub terms — <https://www.aihub.or.kr>.
  Approved recipients are expected to hold their own AI-Hub agreements.
- **CoreaSpeech** (`coreaspeech`), **Emilia** (`emilia_ko`), **kosp2e**:
  governed by their original release terms.
- **Derived artifacts produced by us** — English translations, OmniVoice
  English speech, Mimi tokens, and MMS alignments — are provided for research
  use. Mimi tokens are a lossy, non-invertible representation.

If you are a rights holder with concerns about any content, please open a
discussion on this repository.

---

## Intended use & limitations

- **Intended use**: research on simultaneous / streaming speech-to-speech
  translation, KO→EN translation, and neural-codec speech modeling.
- **English speech is synthetic** (OmniVoice), with intentional accented
  delivery — a translation target for training, not a natural-speech corpus.
- Translations are largely machine-generated (except native-EN sources);
  expect residual translation noise (notably aihub71261).
- Broadcast sources (aihub031, aihub71261) contain multi-speaker, possibly
  real-person audio — review privacy before any downstream release. Not for
  speaker identification or de-anonymization.

---

## Citation

```bibtex
@inproceedings{transorder2026,
  title     = {TransOrder: Reinforcement Learning for Word Reordering in Simultaneous Speech-to-Speech Translation},
  author    = {⚠️ CONFIRM author list},
  booktitle = {⚠️ CONFIRM venue},
  year      = {2026}
}
```

## Contact

SAIL, Ajou University. <!-- ⚠️ CONFIRM contact email / lab page -->
