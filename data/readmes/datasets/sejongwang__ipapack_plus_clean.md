---
license:
- cc0-1.0
- cc-by-4.0
- cc-by-2.0
- apache-2.0
- cc-by-sa-4.0
pretty_name: "IPAPACK++ Cleaned-Label Overlay (v1)"
task_categories:
- automatic-speech-recognition
language:
- en
- de
- fr
- es
- it
- pt
- nl
- sv
- pl
- cs
- sk
- hr
- ro
- mt
- eu
- gl
- ca
- be
- ru
- uk
- ba
- tr
- kk
- uz
- kmr
- rw
- sw
- so
- ar
- ur
- sd
- bn
- ta
- si
- hu
- lt
- th
- my
- vi
- yue
- zh
- ko
- ja
- ha
- yo
tags:
- phoneme-recognition
- ipa
- multilingual
- label-overlay
- ipapack
- g2p
- data-cleaning
- labels-only
size_categories:
- 1M<n<10M
---

# IPAPACK++ Cleaned-Label Overlay (v1)

A **labels-only, strictly additive** cleaned overlay on [IPAPACK++](https://huggingface.co/datasets/anyspeech/ipapack_plus_meta) (Zhu et al., ZIPA, ACL 2025). It adds a regenerated phoneme label (`phones_v1_clean`) alongside the paper's original `phones`, a `drop_flag` for the rows we could not repair, a per-utterance `sigs` list of which defect (if any) was fixed, and a per-row `license` tag. **The original paper label is preserved on every row, including the dropped ones** — so you can compare, ablate, or refuse the cleanup entirely.

This is **not a re-publication of the audio and not a replacement for the paper.** It is an additive second pass on the labels, built on and crediting IPAPACK++/ZIPA, offered back to the community that uses it. The IPAPACK++ authors were themselves explicit that the G2P-generated transcriptions are noisy, especially for low-resource languages, and named label quality among the paper's limitations; this overlay is extra coverage on top of theirs.

> **Status:** v1, labels-only. No retraining, no audio–IPA forced alignment, no phonetician sign-off yet — see [Limitations](#limitations). Every check verifies a defect is *absent from the regenerated label*, not that the label matches the audio.

---

## TL;DR

- **What this is.** A cleaned-label overlay over the full IPAPACK++ corpus: **8,290,179 cuts / 8,281,384 active / 17,109.4 h across 415 shards**, as Lhotse JSONL cut manifests. We add `phones_v1_clean`, `drop_flag`, `sigs`, and `license`. **Audio is not bundled** — re-pair it from the public `anyspeech/ipapack_plus_*` shards by `cut.id`.
- **What we fixed.** Nine mechanically-identifiable label-defect classes ("signatures"): six fixed directly in the labels, one dropped because it is audio-dependent, two deferred to an eval-time canonicalize layer.
- **How much changed.** **~1.9 M rows** regenerated; **6,383,316 rows (77 %)** ship unchanged at the paper baseline. `drop_flag` covers **8,795 utterances (0.11 %)**.
- **License.** **Mixed, per-source** (recorded per row in the `license` field) — most rows are CC0/CC-BY, but **four crowd-sourced OpenSLR slices (~778 k rows) are CC-BY-SA**. See [Source corpora & licenses](#source-corpora--licenses).
- **How to use it.** Train on `cut["supervisions"][0]["custom"]["phones_v1_clean"]`; filter out `…["custom"]["drop_flag"]`; re-pair audio by `cut.id`. The paper baseline is preserved on every row.

---

## How to use it

This is a **label overlay**: you get cleaned label manifests; you bring your own audio.

```python
from huggingface_hub import snapshot_download
from lhotse import CutSet

# 1) pull the cleaned cut manifests (labels only, no audio)
local = snapshot_download("sejongwang/ipapack_plus_clean", repo_type="dataset",
                          allow_patterns="cuts.*.jsonl.gz")

NO_ROUTE = {"mn", "ia", "ceb", "jv", "ff", "tg", "skr"}  # ship at ipa_v0; filter by ISO

cuts = CutSet.from_jsonl(f"{local}/cuts.000000.jsonl.gz")   # one shard; loop over all 415
for cut in cuts:
    sup    = cut.supervisions[0]
    custom = sup.custom
    if custom.get("drop_flag", False):
        continue                                  # skip Sig-3 / untonable / residue
    if sup.language in NO_ROUTE:
        continue                                  # carries v3_backend="unchanged"
    label   = custom["phones_v1_clean"]           # train on this
    baseline = custom.get("original") or custom.get("phones")   # paper baseline (heterogeneous)
    row_license = cut.custom["license"]           # per-row source license (e.g. cc-by-sa-4.0)
    # re-pair audio: member {cut.id}.flac inside the original recording.NNNNNN.tar (same shard index)
```

**Fields** (all on the supervision's `custom` block unless noted):
- `phones_v1_clean` — the canonical v1 cleaned label; train on this.
- `drop_flag` — `True` for Sig-3 (digit), Sig-4-untonable, and residue drops. Filter these out.
- `original` (a.k.a. `ipa_v0`) — paper baseline; **heterogeneous**: absent on ~1.445 M MLS rows, which keep `phones`. Read as `custom.get("original") or custom.get("phones")`.
- `sigs` — list of signatures fixed on this row.
- `cut.custom.corpus` — source provenance tag (cut level), e.g. `cv:rw`, `mls:german`, `openslr:bengali`.
- `cut.custom.license` — **per-row source license** (cut level). Filter on this if you must avoid ShareAlike rows.

**Two warnings worth tattooing on your dataloader.** `supervisions[0]["text"]` is a **stale phone string, not orthography**. PII (`gender`, `speaker`, `age`, `accents`, `variant`) has been stripped on every row.

**Re-pairing audio.** Join by `cut.id`. Each utterance's audio is the member `{cut.id}.flac` inside the original `recording.NNNNNN.tar` at the **same shard index** as the cut shard (positionally paired). The original audio is the public `anyspeech/ipapack_plus_*` dataset (16 kHz). *(The lhotse `from_shar` re-pairing path was not executed end-to-end here — sanity-check it against your lhotse version.)*

---

## What the audit found: the nine signatures

A **signature** is a single, mechanically-identifiable defect class in IPAPACK++'s phoneme labels. `ipa_v0` is the paper-baseline label; `ipa_v3` (= `phones_v1_clean`) is the cleaned label. The audit, the detector, and the measurements are *our* work; the dataset, its Table-6 hour accounting, and the G2P tools (CharsiuG2P, Epitran) are the paper's.

| # | Signature | What it is | Policy | Scope |
|---|---|---|---|---|
| **1** | Apostrophe letter-name (U+0027) | Orthography split on the apostrophe; orphaned `'s` rendered as the letter-name /ɛs/ ("ess") instead of the genitive sibilant | **CLEAN** | 849,482 utts / ~916 h + **+109.9 h** additional |
| **2** | Typographic apostrophe (U+2019) | Same split path on the typographic `'`; folded with Sig-1 | **CLEAN** | (folded with Sig-1) |
| **3** | Digit silent drop | ASCII-only `\d` never matches native-script digits (Bengali `১৯৪৭`, Devanagari, Burmese, Tamil, Arabic-Indic); silently discarded | **DROP** | 537 active drops (~14.2 h) |
| **4** | Non-Mandarin tone strip | byT5 emits Chao tones but a post-G2P step strips them; 7 of 8 tonal cells 100 % stripped, Yoruba partial | **CLEAN** | 8 cells, 6 langs / 79.6 h |
| **5** | Dutch/Swedish Epitran rule artifact | Epitran's `nld/swe-Latn` rule table is phonologically wrong on 9 patterns, deterministically | **CLEAN** | 35,164 utts (CV+FLEURS) |
| **6** | Length-marker `ː` over-insertion | Epitran's word-final length rule over-fires; affects `nl`, `sv` | **CLEAN** | shared with Sig-5 |
| **C1** | Mandarin Chao-tone zero | byT5 under `<cmn-s>:` emits **zero** Chao tone letters across 6,955,717 chars; routed around with pypinyin | **CLEAN** | 122,220 utts / ~199 h |
| **7** | French ø/œ notation drift | Train vs eval write different but both PHOIBLE-attested vowels — a notation drift, **not an error** | **CANONICALIZE** (eval-time; no data change) | ~10 h, eval-only |
| **8** | Spanish r/R notation drift | Tap ɾ / trill r are a genuine phonemic contrast (*pero*/*perro*); a blanket merge would over-collapse it | **CANONICALIZE** (eval-time; no data change) | ~10 h, eval-only |

So: **six fixed in the data** (1, 2, 4, 5, 6, C1), **one dropped** (3), **two eval-time only** (7, 8). The largest single re-route is Kinyarwanda (`rw`, 977,882 utts), which has **no citation-form gold** and is validated **only by inter-tool agreement** — weight it accordingly. Per-utterance regeneration uses a measurement-driven per-ISO matrix (`BEST_G2P_PER_LANG`) drawn from thirteen G2P backends (ten exercised in v1).

The full forensic detail — every measurement, the false-positive byte-match audit (~1,200 h of MLS/LibriSpeech cells over-flagged and *excluded* before the signatures were finalized), the additional-damage sweep, and the zero-tone proof — is available on request.

---

## Limitations

1. **No retraining, ablation, or forced alignment at v1 — this is the big one.** Every PASS verifies self-consistency with the generating backend (the defect is *absent*), **not** label-to-audio correctness. PERs are cited against citation-form lexicon gold, not IPAPACK++ audio. Tone-restored `zh`/`yue`/`th` apply no sandhi (你好 ships as `nǐ hǎo`, unsandhied) — treat as "tone present, value unverified." Because there is no reliable token-level alignment in seq2seq G2P, each fix re-transcribes the *whole* utterance, so non-target tokens adopt that backend's conventions (reduced forms, stress/length marks) — likewise not audio-validated. A full audit of all approximately 1.9 M regenerated rows confirms this re-transcription **introduces a small rate of new errors** — approximately 38 malformed labels, approximately 1,100 illegal genitive clusters (en/ca), approximately 1,000 gold-regressions in two re-routed cells — but the fixes outweigh them by approximately **100:1** for the main signatures. The exception is the Malay (`ms`) re-route, which is **net-negative** (the routed backend emitted English-style pronunciations) — **fall back to v0 there.**
2. **Most of the package is unchanged paper baseline.** ~1.9 M rows touched; **6,383,316 (77 %)** ship unchanged, including a parse-cell blind spot of ~2.49 M cuts (MLS, OpenSLR, hyphenated `zh-CN`/`sv-SE` cells) never routed through the detectors. Treat any `v3_backend="unchanged"` row as "paper-baseline quality, not audited by this release."
3. **The 7 no_route ISO codes are unmeasured.** `mn, ia, ceb, jv, ff, tg, skr` (~19 k utts) sit at `ipa_v0` with `drop_flag=False`.
4. **The shipped vocab predates the cleanup.** Encoding `phones_v1_clean` with `ipa_simplified/unigram_127.model` sends ≈1.36 M utts to `<unk>` (≈680 k after `ɡ→g`). These are **not** label defects — normalize `ɡ→g` or extend the vocab before training.
5. **Sig-7/8 are eval-time only** (apply `ø→œ` for fr, `r→ɾ` for es to both hyp and ref before scoring; the es merge hides genuine /ɾ/–/r/ contrasts). Also **~800,764 cuts share a duplicate `phones_v1_clean`** — dedup/group-by-label when splitting to avoid train/test leakage.

---

## Source corpora & licenses

This dataset is an **additive, labels-only overlay**. It redistributes **regenerated IPA phoneme labels (`phones_v1_clean`), orthographic transcript text, utterance IDs, and a Lhotse cut manifest — NO AUDIO.** Re-pair audio yourself from the sources below. Original IPAPACK++ `phones` are preserved on every row.

This is a **mixed-license** release. The applicable license is recorded **per row** in the `license` field. **Rows from ShareAlike sources are offered under CC-BY-SA and may *not* be treated as permissively licensed.**

> Primary citation: Zhu, J., Samir, F., Chodroff, E., Mortensen, D. R. *ZIPA: A Family of Efficient Models for Multilingual Phone Recognition.* ACL 2025. <https://aclanthology.org/2025.acl-long.961/> · arXiv:2505.23170

| Source | Rows | License | Attribution / citation |
|---|--:|---|---|
| Common Voice (`cv:*`) | 5,285,019 | CC0-1.0 | Mozilla Common Voice — <https://commonvoice.mozilla.org/> |
| Multilingual LibriSpeech (`mls:*`, SLR94) | 1,445,339 | CC-BY-4.0 | Pratap et al. (2020) — <https://www.openslr.org/94/> · labels regenerated |
| FLEURS (`fleurs:*`) | 155,927 | CC-BY-4.0 | Conneau et al. (2022), Google — <https://huggingface.co/datasets/google/fleurs> · labels regenerated |
| LibriSpeech (`openslr:librispeech/*`, SLR12) | 281,209 | CC-BY-4.0 | Panayotov et al. (2015) — <https://www.openslr.org/12/> · labels regenerated |
| AISHELL-1 (`aishell`, SLR33) | 120,078 | Apache-2.0 | Bu et al. (2017), arXiv:1709.05522 — <https://www.openslr.org/33/> |
| Kazakh KSC (`openslr:kazakh`, SLR102) | 147,165 | CC-BY-4.0 | Khassanov et al. (EACL 2021) — <https://www.openslr.org/102/> · labels regenerated |
| IISc-MILE Tamil (`openslr:tamil`, SLR127) | 77,136 | CC-BY-2.0 | Madhavaraj et al. (2022), arXiv:2207.13331 — <https://www.openslr.org/127/> · labels regenerated |
| **Bengali ASR (`openslr:bengali`, SLR53)** | 218,377 | **CC-BY-SA-4.0** | © 2016–2018 Google, Inc.; Kjartansson et al. (SLTU 2018) — <https://www.openslr.org/53/> · **ShareAlike** |
| **Javanese ASR (`openslr:javanese`, SLR35)** | 184,984 | **CC-BY-SA-4.0** | © 2016–2017 Google, Inc. (w/ Reykjavik Univ., Univ. Gadjah Mada) — <https://www.openslr.org/35/> · **ShareAlike** |
| **Sinhala ASR (`openslr:shinhala`, SLR52)** | 178,001 | **CC-BY-SA-4.0** | © 2016–2018 Google, Inc.; Kjartansson et al. (SLTU 2018) — <https://www.openslr.org/52/> · **ShareAlike** |
| **Kazakh KSD (`openslr:kazakh2/*`, SLR140)** | 196,944 | **CC-BY-SA-4.0** | Mansurova & Kadyrbek (2023), Al-Farabi Kazakh National Univ. — <https://www.openslr.org/140/> · source CC-BY-SA-3.0, **adapted labels offered under CC-BY-SA-4.0 (permitted ShareAlike upgrade)** |

**Excluded:** Magicdata — non-redistributable per IPAPACK++; confirmed absent from this release.

**ShareAlike notice.** The Bengali, Javanese, Sinhala, and Kazakh-KSD slices are offered under **CC-BY-SA-4.0** — their regenerated IPA labels are Adapted Material. (Bengali/Javanese/Sinhala sources are CC-BY-SA-4.0; the Kazakh-KSD source is CC-BY-SA-3.0, upgraded to 4.0 under the ShareAlike "this version or later" clause.) Changes were made (phoneme labels regenerated via grapheme-to-phoneme).

**G2P toolchain (credit, not a license obligation on the labels).** Labels were generated with OLaPh (Wirth, 2025; en/de/fr/cs), Epitran, phonemizer + espeak-ng (nl/sv), CharsiuG2P, pypinyin + pinyin-to-ipa, ToJyutping, viphoneme, PyThaiNLP, indic_nlp_library, and commonvoice-utils. espeak-ng is GPL-3.0 and commonvoice-utils is AGPL-3.0, used in-process during generation; per the FSF GPL FAQ, **program output is not covered by the program's copyright**, so no GPL/AGPL obligation attaches to these IPA label strings.

---

## Citation

Please cite **both** this overlay and the original IPAPACK++ paper.

```bibtex
@misc{kim2026ipapack_cleanup_v1,
  title  = {Cleaning IPAPACK++: A Surgical Audit of Multilingual Phoneme Labels},
  author = {Kim, Junehwi},
  year   = {2026},
  note   = {IPAPACK++ Cleaned-Label Overlay (v1), Hugging Face Datasets},
}
```

> Zhu, Jian and Samir, Farhan and Chodroff, Eleanor and Mortensen, David R. *ZIPA: A Family of Efficient Models for Multilingual Phone Recognition.* Proc. 63rd ACL 2025 (Vol. 1: Long Papers). <https://aclanthology.org/2025.acl-long.961/>

The label-cleanup work and this release are by Junehwi Kim; compute was a local 2080 Ti × 3.
