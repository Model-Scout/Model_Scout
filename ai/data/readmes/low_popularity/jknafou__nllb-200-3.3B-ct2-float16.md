---
license: cc-by-nc-4.0
base_model: facebook/nllb-200-3.3B
base_model_relation: quantized
library_name: ctranslate2
pipeline_tag: translation
inference: false
tags:
- ctranslate2
- translation
- nllb
- float16
datasets:
- facebook/flores
metrics:
- chrf
- bleu
language:
- ace
- acm
- acq
- aeb
- af
- ajp
- ak
- als
- am
- apc
- ar
- ars
- ary
- arz
- as
- ast
- awa
- ayr
- azb
- azj
- ba
- bm
- ban
- be
- bem
- bn
- bho
- bjn
- bo
- bs
- bug
- bg
- ca
- ceb
- cs
- cjk
- ckb
- crh
- cy
- da
- de
- dik
- dyu
- dz
- el
- en
- eo
- et
- eu
- ee
- fo
- fj
- fi
- fon
- fr
- fur
- fuv
- gaz
- gd
- ga
- gl
- gn
- gu
- ht
- ha
- he
- hi
- hne
- hr
- hu
- hy
- ig
- ilo
- id
- is
- it
- jv
- ja
- kab
- kac
- kam
- kn
- ks
- ka
- kk
- kbp
- kea
- khk
- km
- ki
- rw
- ky
- kmb
- kmr
- knc
- kg
- ko
- lo
- lij
- li
- ln
- lt
- lmo
- ltg
- lb
- lua
- lg
- luo
- lus
- lvs
- mag
- mai
- ml
- mar
- min
- mk
- mt
- mni
- mos
- mi
- my
- nl
- nn
- nb
- npi
- nso
- nus
- ny
- oc
- ory
- pag
- pa
- pap
- pbt
- pes
- plt
- pl
- pt
- prs
- quy
- ro
- rn
- ru
- sg
- sa
- sat
- scn
- shn
- si
- sk
- sl
- sm
- sn
- sd
- so
- st
- es
- sc
- sr
- ss
- su
- sv
- swh
- szl
- ta
- taq
- tt
- te
- tg
- tl
- th
- ti
- tpi
- tn
- ts
- tk
- tum
- tr
- tw
- tzm
- ug
- uk
- umb
- ur
- uzn
- vec
- vi
- war
- wo
- xh
- ydd
- yo
- yue
- zh
- zsm
- zu
language_details: "ace_Arab, ace_Latn, acm_Arab, acq_Arab, aeb_Arab, afr_Latn, ajp_Arab, aka_Latn, amh_Ethi, apc_Arab, arb_Arab, ars_Arab, ary_Arab, arz_Arab, asm_Beng, ast_Latn, awa_Deva, ayr_Latn, azb_Arab, azj_Latn, bak_Cyrl, bam_Latn, ban_Latn, bel_Cyrl, bem_Latn, ben_Beng, bho_Deva, bjn_Arab, bjn_Latn, bod_Tibt, bos_Latn, bug_Latn, bul_Cyrl, cat_Latn, ceb_Latn, ces_Latn, cjk_Latn, ckb_Arab, crh_Latn, cym_Latn, dan_Latn, deu_Latn, dik_Latn, dyu_Latn, dzo_Tibt, ell_Grek, eng_Latn, epo_Latn, est_Latn, eus_Latn, ewe_Latn, fao_Latn, pes_Arab, fij_Latn, fin_Latn, fon_Latn, fra_Latn, fur_Latn, fuv_Latn, gla_Latn, gle_Latn, glg_Latn, grn_Latn, guj_Gujr, hat_Latn, hau_Latn, heb_Hebr, hin_Deva, hne_Deva, hrv_Latn, hun_Latn, hye_Armn, ibo_Latn, ilo_Latn, ind_Latn, isl_Latn, ita_Latn, jav_Latn, jpn_Jpan, kab_Latn, kac_Latn, kam_Latn, kan_Knda, kas_Arab, kas_Deva, kat_Geor, knc_Arab, knc_Latn, kaz_Cyrl, kbp_Latn, kea_Latn, khm_Khmr, kik_Latn, kin_Latn, kir_Cyrl, kmb_Latn, kon_Latn, kor_Hang, kmr_Latn, lao_Laoo, lvs_Latn, lij_Latn, lim_Latn, lin_Latn, lit_Latn, lmo_Latn, ltg_Latn, ltz_Latn, lua_Latn, lug_Latn, luo_Latn, lus_Latn, mag_Deva, mai_Deva, mal_Mlym, mar_Deva, min_Latn, mkd_Cyrl, plt_Latn, mlt_Latn, mni_Beng, khk_Cyrl, mos_Latn, mri_Latn, zsm_Latn, mya_Mymr, nld_Latn, nno_Latn, nob_Latn, npi_Deva, nso_Latn, nus_Latn, nya_Latn, oci_Latn, gaz_Latn, ory_Orya, pag_Latn, pan_Guru, pap_Latn, pol_Latn, por_Latn, prs_Arab, pbt_Arab, quy_Latn, ron_Latn, run_Latn, rus_Cyrl, sag_Latn, san_Deva, sat_Beng, scn_Latn, shn_Mymr, sin_Sinh, slk_Latn, slv_Latn, smo_Latn, sna_Latn, snd_Arab, som_Latn, sot_Latn, spa_Latn, als_Latn, srd_Latn, srp_Cyrl, ssw_Latn, sun_Latn, swe_Latn, swh_Latn, szl_Latn, tam_Taml, tat_Cyrl, tel_Telu, tgk_Cyrl, tgl_Latn, tha_Thai, tir_Ethi, taq_Latn, taq_Tfng, tpi_Latn, tsn_Latn, tso_Latn, tuk_Latn, tum_Latn, tur_Latn, twi_Latn, tzm_Tfng, uig_Arab, ukr_Cyrl, umb_Latn, urd_Arab, uzn_Latn, vec_Latn, vie_Latn, war_Latn, wol_Latn, xho_Latn, ydd_Hebr, yor_Latn, yue_Hant, zho_Hans, zho_Hant, zul_Latn"
---

# NLLB-200 3.3B for CTranslate2, float16

This is Meta's [NLLB-200 3.3B](https://huggingface.co/facebook/nllb-200-3.3B) (revision
`1a07f7d195896b2114afcb79b7b57ab512e7b43e`), converted to the
[CTranslate2](https://github.com/OpenNMT/CTranslate2) format with its weights stored in
float16, by CTranslate2 4.8.1 with the command given below. The sha256 of every file is at the
end of this card.

**It is not a new model.** No weight was trained, fine-tuned or pruned, and no weight is stored
below 16 bits. What it brings is speed and a smaller footprint, measured on one NVIDIA A100
80GB against the original model in `transformers`:
- 6.9× the throughput of the original in float32, and 1.9× that of the original in float16;
- a third of the GPU memory;
- 38% of the disk space.

**We recommend decoding with `patience=2`.** With CTranslate2's default (`patience=1`), these
files score 0.38 chrF++ below the original on average over 4 languages of FLORES-200, and one
translation in four is worded differently. That loss does not come from float16, nor from the
engine's arithmetic: it comes from CTranslate2's default rule for ending the beam search. With
`patience=2` the loss is gone (54.42 mean chrF++ against the original's 54.27), at 72% of the
default speed with plain beam search, and at 85% on a real workload of biomedical abstracts.
Everything is measured below.

## What CTranslate2 is

CTranslate2 is an inference engine for Transformer models, written in C++ and CUDA by the
OpenNMT project and released under the MIT licence. It does not run PyTorch. It loads a model
from its own format: one `model.bin` holding the weights and the layer layout, plus a
`config.json` and a vocabulary. It then runs the encoder, the decoder and the beam search in
native code. On the GPU it uses fused kernels and a key/value cache for the decoder, and it
computes in the weights' type (here float16). Its Python package (`pip install ctranslate2`)
exposes a `Translator` that takes source **tokens**, not text: tokenisation stays outside the
engine, with the original NLLB tokenizer, whose files are included here.

## How it was made

### The command

The conversion is the standard one, from the original checkpoint at a pinned revision:

```bash
pip install ctranslate2==4.8.1 transformers==4.57.1 torch==2.9.0 sentencepiece protobuf
hf download facebook/nllb-200-3.3B --revision 1a07f7d195896b2114afcb79b7b57ab512e7b43e \
  --local-dir nllb-200-3.3B
ct2-transformers-converter \
  --model nllb-200-3.3B \
  --quantization float16 \
  --copy_files tokenizer.json tokenizer_config.json special_tokens_map.json generation_config.json \
  --output_dir nllb-200-3.3B-ct2-float16
```

- With `--quantization float16`, each float32 weight is rounded once to the nearest float16.
  Nothing else is done to the weights.
- The conversion runs on the CPU. It took 1 minute 23 seconds and 17.3 GB of RAM on a 56-core
  Intel Xeon Gold 6330.

### Provenance of these exact files

- **Made on** 1 November 2026 with the command above: ctranslate2 4.8.1, transformers 4.57.1,
  torch 2.9.0 (CPU build), on an Intel Xeon Gold 6330.
- **A second run** with transformers 5.5.4 and torch 2.10.0 gave the same bytes.
- **`model.bin`:** CTranslate2 binary format 6, `TransformerSpec` revision 7, 790 variables:
  774 in float16, 2 float32 scalars (`scale_embeddings`) and 14 int8 or int16 flags.
- **The tokenizer files** (`tokenizer.json`, `tokenizer_config.json`,
  `special_tokens_map.json`) and `generation_config.json` are byte-identical to those of the
  original repository at revision `1a07f7d1`.

**One tensor depends on the machine.** The converter does not read the decoder's sinusoidal
position table (1024 × 2048) from the checkpoint: it computes it, with the CPU's math library.
- We also had an earlier conversion of the same checkpoint, of unrecorded origin (`model.bin`
  sha256 `7fa99796…`, made with CTranslate2 4.1.0 or later). The public
  [entai2965 conversion](https://huggingface.co/entai2965/nllb-200-3.3B-ctranslate2-float16)
  holds the same tensors as that one.
- 789 of the 790 variables of this `model.bin` are identical to that earlier conversion's.
  The 790th, the position table, differs at 456 of its 2,097,152 values, mostly by one float16
  step (largest difference 0.00049).
- Every combination we tried gave this card's table: transformers 4.30 to 5.5.4, torch 2.1 to
  2.10, and every ATen CPU level. The earlier one was probably converted on a platform whose
  math library rounds differently (an inference, not a measurement).
- **Rebuilding on another machine** may therefore give a `model.bin` that differs from this
  one in that table only. All the other files should match the sha256s below.

What the different table changes in the output, measured on one A100 80GB:

| test | identical outputs |
|---|---|
| FLORES-200, 4 languages, plain beam 4, batches of 64 sentences | 4,048 / 4,048 |
| FLORES-200, 4 languages, beam 4, `no_repeat_ngram_size=4`, batches of 16,384 tokens | 4,046 / 4,048 |
| 5,000 biomedical abstracts, same settings (rows / sentences) | 4,824 / 5,000 rows; 37,449 / 37,646 sentences |

- The scores are equal to 0.01 chrF++ and BLEU.
- On the 197 sentences that changed, reference-free quality is unchanged: COMET-QE
  (`wmt20-comet-qe-da`) −0.006, 95% interval [−0.016, +0.003].
- So the two conversions are equivalent in quality, but not interchangeable byte for byte.

## What is unchanged

- **Architecture.** The M2M-100 encoder-decoder of NLLB-200 3.3B:
  - 24 encoder and 24 decoder layers, d_model 2048, 16 heads, feed-forward 8192, ReLU;
  - pre-norm, scaled embeddings, sinusoidal positions;
  - shared input and output embeddings;
  - the same 3.3 billion parameters.
- **Vocabulary.** The same 256,206 entries in the same order (`shared_vocabulary.json`), so the
  token ids are the original ones.
- **Tokenizer.** The original files, byte for byte (see above).
- **Language codes.** The same 202 FLORES-200 codes (`eng_Latn`, `por_Latn`, `zho_Hans`, …):
  - the source is the source language's code, the sentence's pieces, then `</s>`;
  - the target is forced to start with the target language's code (`target_prefix` in
    CTranslate2, `forced_bos_token_id` in `transformers`).

## What changes

1. **Float16 numerics.** The weights are stored, and computed, in float16 instead of the
   checkpoint's float32.
   - Within CTranslate2, this alone changes the output of 16.0% of the sentences ((C) against
     (D) below).
   - It moves no score by more than 0.1 chrF++ or 0.14 BLEU, and none significantly.
2. **CTranslate2's beam search.** CTranslate2 and `transformers` end the beam search
   differently. Our runs used beam 4 and length penalty 1 in both.
   - CTranslate2, with its default `patience=1`, ends a sentence's search as soon as 4
     hypotheses have finished.
   - `transformers`, with its default `early_stopping=False`, keeps searching while an
     unfinished beam could still beat them after length normalisation.
   - So CTranslate2 settles for a shorter translation more often. Every sentence that differs
     between (A) and (C) below is shorter in CTranslate2: 522 of 522. Some drop a trailing
     clause.
   - **The cause, measured:** `transformers` in float32 with `early_stopping=True`, which stops
     as CTranslate2 does, gave **byte-identical output to CTranslate2 in float32 on all 4,048
     sentences**. The engine's arithmetic changes nothing; the stopping rule is the whole
     engine effect.
   - With `patience=2`, CTranslate2 waits for 8 finished hypotheses instead of 4. These files
     then lose nothing against the original (tables below).
3. **Batching numerics.** In float16, the output of a sentence can depend on which sentences
   share its batch, through padding and the choice of kernels. Fix the batches if you need
   byte-identical output from one run to the next: with the same batches, every system
   compared here gave byte-identical output in two separate jobs.

## What it brings

Measured on one NVIDIA A100 80GB PCIe:
- **Data:** FLORES-200 devtest, 1,012 sentences, from eng_Latn to por_Latn, fra_Latn,
  zho_Hans and arb_Arab (4 × 32,665 source tokens).
- **Decoding:** beam 4, at most 256 new tokens (never reached), no sampling, no repetition
  constraint.
- **Batches:** 64 sentences sorted by length, the same for every system.
- **Which conversion was measured.** The figures for (D) in this section and the next were
  measured with the earlier conversion described above. These files were measured against it:
  - here, they gave the same output on all 4,048 sentences, so the same scores, and ran at
    2,029 tokens/s against 2,069, within the measurement's noise (±2.3%);
  - with the production settings below, they gave the same FLORES scores to 0.01 at
    `patience=1` and at `patience=2`, and on the abstracts at `patience=1` the same speed
    (2,117 against 2,111 tokens/s) and peak GPU memory within 4% (37.0 against 35.7 GB).

| | original, transformers fp32 (A) | original, transformers fp16 (B) | **these files, CTranslate2 fp16 (D)** |
|---|---|---|---|
| source tokens / s | 298 | 1,075 | **2,069** |
| speed-up | 1× | 3.6× | **6.9×** (1.9× over B) |
| peak GPU memory (NVML, above idle) | 45.0 GiB | 20.4 GiB | **15.1 GiB** |
| GPU memory once loaded | 19.3 GiB | 10.3 GiB | **9.0 GiB** |
| size on disk | 17.6 GB | 17.6 GB | **6.7 GB** |

- The original's 17.6 GB are float32 PyTorch files. The weights of these files take 6.2 GiB in
  GPU memory; the peak includes CTranslate2's caching allocator, which keeps what it has used.
- With a repetition constraint (`no_repeat_ngram_size=4`) and longer inputs, an earlier test on
  40 biomedical abstracts measured 7.2× over `transformers` in float16, because `transformers`
  applies that constraint on the host.

## What it takes out

### Scores against the FLORES-200 references

sacrebleu 2.6.0: chrF++ is `nc:6|nw:2`; BLEU uses tokenizer `13a`, and `zh` for zho_Hans.
Same data and settings as above (`patience=1`).

| system | por_Latn chrF++ / BLEU | fra_Latn | zho_Hans | arb_Arab | mean chrF++ | mean BLEU |
|---|---|---|---|---|---|---|
| (A) original, transformers fp32 | 69.39 / 49.56 | 69.89 / 51.13 | 22.45 / 31.74 | 55.33 / 27.54 | 54.27 | 39.99 |
| (B) original, transformers fp16 | 69.40 / 49.58 | 69.86 / 51.07 | 22.42 / 31.71 | 55.25 / 27.45 | 54.23 | 39.95 |
| (C) CTranslate2 fp32 conversion | 69.14 / 49.35 | 69.50 / 50.74 | 21.86 / 30.25 | 55.11 / 27.19 | 53.90 | 39.38 |
| **(D) these files** | **69.11 / 49.39** | **69.45 / 50.60** | **21.93 / 30.28** | **55.06 / 27.11** | **53.89** | **39.34** |
| (E) entai2965 conversion | 69.11 / 49.39 | 69.45 / 50.60 | 21.93 / 30.28 | 55.06 / 27.11 | 53.89 | 39.34 |

These files against the original, (D) − (A), with paired-bootstrap 95% intervals (1,000
resamples):

| | por_Latn | fra_Latn | zho_Hans | arb_Arab |
|---|---|---|---|---|
| chrF++ | −0.28 [−0.51, −0.08] | −0.44 [−0.70, −0.21] | −0.52 [−0.86, −0.16] | −0.27 [−0.47, −0.10] |
| BLEU | −0.17 [−0.45, +0.11] | −0.53 [−0.83, −0.25] | −1.46 [−1.87, −1.08] | −0.43 [−0.72, −0.18] |

### Where the loss comes from

| step | what changes | chrF++ change (4 languages) | sentences identical |
|---|---|---|---|
| A → B | float16, same engine | −0.08 to +0.01 (significant only for arb, −0.08) | 3,960 / 4,048 (97.8%) |
| A → A′ | the stopping rule only: `transformers` fp32 with `early_stopping=True` | −0.59 to −0.22 (all significant) | 3,526 / 4,048 (87.1%) |
| A′ → C | the engine only: CTranslate2 instead of `transformers`, both fp32, same stopping rule | 0 | **4,048 / 4,048 (100%)** |
| C → D | float16, same engine | −0.05 to +0.07 (none significant) | 3,401 / 4,048 (84.0%) |
| A → D | all of the above (`patience=1`) | −0.52 to −0.27 (all significant) | 3,052 / 4,048 (75.4%) |

- One translation in four differs from the original model's.
- The differences cost 0.27 to 0.52 chrF++, and up to 1.5 BLEU for zho_Hans, where the shorter
  outputs also meet BLEU's brevity penalty.
- Float16 changes words, not quality. The loss is the price of CTranslate2's default stopping
  rule.

### `patience=2` removes it

| (D) these files, with | mean chrF++ | mean BLEU | source tokens / s | identical to (A) |
|---|---|---|---|---|
| `patience=1` (CTranslate2's default) | 53.89 | 39.34 | 2,069 | 75.4% |
| **`patience=2`** | **54.42** | **40.23** | **1,499** | **83.1%** |
| `patience=4` | 54.38 | 40.16 | 882 | 82.6% |
| (A) original, for reference | 54.27 | 39.99 | 298 | 100% |

- `patience=2` costs 28% of the throughput with plain beam search on FLORES, and is still 5.0×
  the original and 1.4× `transformers` in float16.
- No language is then significantly worse than the original: the largest change is
  −0.05 chrF++ [−0.26, +0.15], for arb_Arab.
- `patience=4` brings nothing more.

### `patience=2` on a production workload

On one A100 80GB, decoding with beam 4, `no_repeat_ngram_size=4`, inputs capped
at 512 tokens, a per-batch length cap of `min(512, ceil(1.5 × longest source + 10))` tokens,
and batches of 16,384 tokens:
- **FLORES-200:** the same 4 languages;
- **production:** 5,000 biomedical abstracts from PubMed, eng_Latn → por_Latn, 1.39 million
  source tokens, split into sentences.

| | `patience=1` | `patience=2` | change |
|---|---|---|---|
| FLORES mean chrF++ (por / fra / zho / arb) | 53.76 (68.95 / 69.12 / 21.99 / 54.97) | **54.27** (69.38 / 69.68 / 22.93 / 55.10) | +0.13 to +0.94 per language |
| FLORES mean BLEU | 39.13 | 39.94 | zho_Hans +2.25 |
| abstracts: source tokens / s | 2,119 (mean of two runs) | 1,805 | **−14.8%** |
| abstracts: energy, kWh per million source tokens | 0.0349 | 0.0415 | +19% |
| abstracts: peak GPU memory | 35.7 GB | 38.0 GB | +6% |
| abstracts: rows / sentences changed | | 35.3% / 6.1% | mostly longer outputs |
| abstracts: COMET-QE (`wmt20-comet-qe-da`), 600 changed sentences | 0.261 | 0.276 | +0.015 [+0.007, +0.024] |

- With these settings and `patience=2`, mean chrF++ equals the original model's in
  `transformers` (54.27). With `patience=1` it is 0.51 below, and every language is
  significantly lower.
- GPU utilisation is 97–98% either way: the extra time is extra search.

## How to use it

```bash
pip install ctranslate2 transformers huggingface_hub
hf download jknafou/nllb-200-3.3B-ct2-float16 --local-dir nllb-200-3.3B-ct2-float16
```

```python
import ctranslate2
from transformers import AutoTokenizer

path = "nllb-200-3.3B-ct2-float16"
tok = AutoTokenizer.from_pretrained(path)
mt = ctranslate2.Translator(path, device="cuda", compute_type="float16")

src_lang, tgt_lang = "eng_Latn", "por_Latn"
texts = ["The patient was given 5 mg of the drug twice a day."]
# the source is [src_lang, pieces..., "</s>"]; build it explicitly
batch = [[src_lang, *tok.convert_ids_to_tokens(tok(t, add_special_tokens=False).input_ids), "</s>"]
         for t in texts]
res = mt.translate_batch(batch, target_prefix=[[tgt_lang]] * len(batch),
                         beam_size=4, patience=2)
for r in res:
    hyp = r.hypotheses[0][1:]  # drop the target language code
    print(tok.decode(tok.convert_tokens_to_ids(hyp), skip_special_tokens=True))
# O doente recebeu 5 mg do medicamento duas vezes por dia.
```

- Tested from a fresh download with ctranslate2 4.8.1 and transformers 5.22.1 (on the CPU, with
  `device="cpu", compute_type="int8"`, which gave the output shown).
- Float16 is a GPU type: on a CPU, use `compute_type="int8"` or `"float32"`.
- The source is built by hand rather than with the tokenizer's `src_lang`, whose behaviour has
  changed between `transformers` versions. Recent `transformers` may print a warning about the
  tokenizer's regex pattern; the token ids are the same as with transformers 4.57.1.
- The original model was trained on inputs of at most 512 tokens: cap longer inputs
  (`max_input_length=512`, CTranslate2's default is 1024) or split them into sentences.
- For long or many inputs, sort them by length and batch by tokens
  (`batch_type="tokens", max_batch_size=...`).

### RhoZeta

These files were made for RhoZeta, the corpus translation tool of the
[TransCorpus](https://github.com/jknafou/TransCorpus) line of work, which uses them by default
with `patience=2` and the production settings above. RhoZeta names a model by a hash of its
`model.bin`, `config.json` and `tokenizer.json`: for these files it is `e44998d1060419fc`.

## Licence and attribution

- **Licence:** CC-BY-NC-4.0, inherited from
  [facebook/nllb-200-3.3B](https://huggingface.co/facebook/nllb-200-3.3B). Non-commercial use
  only. The conversion adds no rights and no restrictions.
- **The model** is the work of Meta AI's NLLB team, and all credit for it goes to them: NLLB
  Team et al., *No Language Left Behind: Scaling Human-Centered Machine Translation*, 2022
  (arXiv:2207.04672).
- **Meta's model card still applies.** NLLB-200 is a research model, not meant for production
  deployment or for certified translations. It was trained on general-domain data, so domain
  text such as medical or legal text is outside its stated scope, and it was trained on inputs
  of at most 512 tokens.
- **The engine** is CTranslate2, by the OpenNMT project, under the MIT licence.

```bibtex
@article{nllb2022,
  title   = {No Language Left Behind: Scaling Human-Centered Machine Translation},
  author  = {{NLLB Team} and Costa-juss{\`a}, Marta R. and Cross, James and others},
  journal = {arXiv preprint arXiv:2207.04672},
  year    = {2022}
}
```

## Files

| file | bytes | sha256 |
|---|---|---|
| `config.json` | 223 | `8f6496adfc930cbfecbe8281112197705c488fab47d34b4829b06d7f478909af` |
| `generation_config.json` | 189 | `0bb604cdb8392649176935a447ce994128f170a6908c135a17d0e3dfb8113cb2` |
| `model.bin` | 6,693,964,035 | `7a67df402a9db669e212ba4b7ef78548ac6a38470aae9b6e0938797096e790f8` |
| `shared_vocabulary.json` | 5,921,176 | `af53bfd0e6f726209e7325e45b87ab3b14e5856f7d42d7b9be91de3287c45267` |
| `special_tokens_map.json` | 3,548 | `992bd4ed610d644d6823081937bcc91bb8878dd556cea4ae5327f2480361330e` |
| `tokenizer_config.json` | 564 | `d1aa8c3697d3e35674f97b5b7e9c99d22b010f528e80140257d97316be90d044` |
| `tokenizer.json` | 17,331,176 | `e316b82de11d0f951f370943b3c438311629547285129b0b81dadabd01bca665` |
