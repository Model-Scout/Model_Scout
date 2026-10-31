---
dataset_info:
- config_name: hepburn_forget01
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 12365
    num_examples: 40
  download_size: 8474
  dataset_size: 12365
- config_name: hepburn_forget01_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 73238
    num_examples: 40
  download_size: 66281
  dataset_size: 73238
- config_name: hepburn_real_authors_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 15149
    num_examples: 100
  download_size: 13310
  dataset_size: 15149
- config_name: hepburn_retain99
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 1122384
    num_examples: 3960
  download_size: 510178
  dataset_size: 1122384
- config_name: hepburn_retain_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 674617
    num_examples: 400
  download_size: 551922
  dataset_size: 674617
- config_name: hepburn_world_facts_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 14898
    num_examples: 117
  download_size: 13245
  dataset_size: 14898
- config_name: ivrit_lat_forget01
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 10867
    num_examples: 40
  download_size: 8777
  dataset_size: 10867
- config_name: ivrit_lat_forget01_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 65973
    num_examples: 40
  download_size: 62954
  dataset_size: 65973
- config_name: ivrit_lat_real_authors_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 13646
    num_examples: 100
  download_size: 12987
  dataset_size: 13646
- config_name: ivrit_lat_retain99
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 987169
    num_examples: 3960
  download_size: 542205
  dataset_size: 987169
- config_name: ivrit_lat_retain_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 605143
    num_examples: 400
  download_size: 519943
  dataset_size: 605143
- config_name: ivrit_lat_world_facts_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 14091
    num_examples: 117
  download_size: 13358
  dataset_size: 14091
- config_name: arabizi_msa_forget01
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 11038
    num_examples: 40
  download_size: 8968
  dataset_size: 11038
- config_name: arabizi_msa_forget01_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 68562
    num_examples: 40
  download_size: 64989
  dataset_size: 68562
- config_name: arabizi_msa_real_authors_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 13841
    num_examples: 100
  download_size: 13306
  dataset_size: 13841
- config_name: arabizi_msa_retain99
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 1009348
    num_examples: 3960
  download_size: 545283
  dataset_size: 1009348
- config_name: arabizi_msa_retain_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: paraphrased_answer
    dtype: string
  - name: perturbed_answer
    list: string
  - name: paraphrased_question
    dtype: string
  splits:
  - name: train
    num_bytes: 621999
    num_examples: 400
  download_size: 533455
  dataset_size: 621999
- config_name: arabizi_msa_world_facts_perturbed
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: perturbed_answer
    list: string
  splits:
  - name: train
    num_bytes: 13905
    num_examples: 117
  download_size: 13473
  dataset_size: 13905
configs:
- config_name: hepburn_forget01
  data_files:
  - split: train
    path: hepburn_forget01/train-*
- config_name: hepburn_forget01_perturbed
  data_files:
  - split: train
    path: hepburn_forget01_perturbed/train-*
- config_name: hepburn_real_authors_perturbed
  data_files:
  - split: train
    path: hepburn_real_authors_perturbed/train-*
- config_name: hepburn_retain99
  data_files:
  - split: train
    path: hepburn_retain99/train-*
- config_name: hepburn_retain_perturbed
  data_files:
  - split: train
    path: hepburn_retain_perturbed/train-*
- config_name: hepburn_world_facts_perturbed
  data_files:
  - split: train
    path: hepburn_world_facts_perturbed/train-*
- config_name: ivrit_lat_forget01
  data_files:
  - split: train
    path: ivrit_lat_forget01/train-*
- config_name: ivrit_lat_forget01_perturbed
  data_files:
  - split: train
    path: ivrit_lat_forget01_perturbed/train-*
- config_name: ivrit_lat_real_authors_perturbed
  data_files:
  - split: train
    path: ivrit_lat_real_authors_perturbed/train-*
- config_name: ivrit_lat_retain99
  data_files:
  - split: train
    path: ivrit_lat_retain99/train-*
- config_name: ivrit_lat_retain_perturbed
  data_files:
  - split: train
    path: ivrit_lat_retain_perturbed/train-*
- config_name: ivrit_lat_world_facts_perturbed
  data_files:
  - split: train
    path: ivrit_lat_world_facts_perturbed/train-*
- config_name: arabizi_msa_forget01
  data_files:
  - split: train
    path: arabizi_msa_forget01/train-*
- config_name: arabizi_msa_forget01_perturbed
  data_files:
  - split: train
    path: arabizi_msa_forget01_perturbed/train-*
- config_name: arabizi_msa_real_authors_perturbed
  data_files:
  - split: train
    path: arabizi_msa_real_authors_perturbed/train-*
- config_name: arabizi_msa_retain99
  data_files:
  - split: train
    path: arabizi_msa_retain99/train-*
- config_name: arabizi_msa_retain_perturbed
  data_files:
  - split: train
    path: arabizi_msa_retain_perturbed/train-*
- config_name: arabizi_msa_world_facts_perturbed
  data_files:
  - split: train
    path: arabizi_msa_world_facts_perturbed/train-*
---

# TOFU — Hebrish / Arabizi(-over-MSA) / Romaji (Latin-script transliterations)

Three Latin-script transliteration arms of the TOFU fictitious-author unlearning
benchmark, built for **"Script, Not Syntax: Transliteration as a Blind Spot in
Multilingual Unlearning"** (Tsir Cohen, Rubinstein, Spira — Trustworthy Machine
Learning, Tel Aviv University, 2026).

## Why this exists

TOFU (Maini et al., 2024) asks factual questions about invented authors, so it's
answerable only from what a model was actually trained on. Farashah et al.'s
*Multilingual Amnesia* (EACL 2026) translated it into ten languages to study
whether unlearning a fact in one language removes it in another, and found that
unlearning transfers unevenly — which they attribute to *syntactic* distance
between languages. But any two languages in their set also differ in **script**,
and no pair isolates it. This dataset removes that confound by construction: it
takes three of their languages — Hebrew, Arabic, Japanese — and rewrites the
*same* text in Latin letters and, for the Arabic arm, an Arabizi-style digit
convention. Script changes; grammar, vocabulary and meaning don't.

**Two of the three arms are naturalistic; one is not, and that matters for how
you read it.** Hebrish is genuinely how Israelis type Hebrew when they lack a
Hebrew keyboard, and Romaji is a standard, widely used romanization. The Arabic
arm is different: see [`arabizi_msa_*` — what it actually is](#arabizi_msa--what-it-actually-is)
below before using it as evidence about real-world Arabizi usage.

## The three arms

| Config prefix | Source language | What it is |
|---|---|---|
| `ivrit_lat_*` | Hebrew (`iw`) | "Hebrish" — Israeli chat/SMS-style Latin spelling |
| `arabizi_msa_*` | Arabic (`ar`) | Modern Standard Arabic text, letter-for-letter converted to Latin script using a Beiruti/Levantine Arabizi digit convention — **not** colloquial Lebanese speech (see below) |
| `hepburn_*` | Japanese (`ja`) | "Romaji" — modified Hepburn romanization |

### `arabizi_msa_*` — what it actually is

This arm was previously named `lebnani_*`, which implied it was colloquial
Lebanese Arabizi — the way Lebanese speakers actually text. It is not, and the
config was renamed to say so honestly.

What's true about it:
- The **digit convention** is real and correctly documented Beiruti/Levantine
  Arabizi: 2 = ء and ق (urban Levantine speech glottalizes ق into the same stop
  as hamza, so qalb → 2alb), 3 = ع, 5 = خ, 6 = ط, 7 = ح, 9 = ص; ث/ذ/ض/ظ/غ stay as
  th/z/d/z/gh, never a digit.

What's not true about it:
- The **source text being converted is Modern Standard Arabic** (the `tofu_ar`
  translation from Farashah et al.'s *Multilingual Amnesia*), i.e. formal
  written-register Arabic — not spoken Lebanese dialect. Real Arabizi, as
  Lebanese people actually use it, transcribes colloquial speech (vocabulary,
  grammar, and pronunciation all differ from MSA), not fuṣḥā with the letters
  swapped for digits. This dataset only does the letter/digit swap; no
  dialect-translation step happens.
- The digit convention itself encodes a *colloquial pronunciation fact*
  (Levantine glottalization of qaf) that formal register doesn't have — a
  reader voicing MSA text keeps the distinct classical /q/. So beyond just
  "wrong register," pairing this specific digit table with MSA content is
  arguably internally inconsistent: nobody naturally produces this exact
  combination when texting.
- Empirically, real-world Arabizi corpora are overwhelmingly dialectal, not
  MSA (see Keleg et al., *Romanized Arabic Across Dialects*, 2026: "It is
  commonly believed that Arabizi is used primarily for [Dialectal Arabic]...
  most Arabizi data collected for NLP has focused on DA").

**What this arm is still good for:** an ablation that changes *only* script
(Arabic letters → Latin letters/digits) while holding content and register
fixed to the MSA source — arguably a *cleaner* manipulation for isolating
whether script/tokenizer overlap drives unlearning transfer than a version that
also changed dialect. It should not be cited as evidence that this is how
Arabic speakers write informally — unlike the Hebrish arm, it isn't.

## How it was generated

Each row was transliterated independently by an LLM (`gpt-5-mini`, OpenAI,
chat completion in JSON-mode), given:

- **One fixed phonetic convention per language**, spelled out in the system
  prompt so the whole arm is spelling-consistent instead of mixing plausible
  variants.
- **A handful of worked few-shot examples** per language, in the exact
  input/output shape the model must match.
- **The row-aligned original English TOFU text as a reference**, so proper
  names (the recurring fictitious authors, place names) are copied
  letter-for-letter from English rather than phonetically respelled — checked
  automatically per field after generation; a response missing a name gets a
  targeted correction turn and a retry, not a blind resample.
- **Automatic validation**: a response is rejected and retried (up to 5
  attempts) if it still contains source-script characters, doesn't mirror the
  input's JSON shape, or is just a copy of the English reference.

Generation code (`transliterate_llm.py` and the rest of the data pipeline)
lives in the project's private repository and isn't linked here since it isn't
public.

### Full system prompts (exact text sent to the model)

Every prompt shares the same shared-rules preamble (transliterate, don't
translate; keep proper names in their English spelling; keep already-Latin
loanwords as-is; Latin punctuation only) plus this language-specific block:

<details>
<summary><b>Hebrew → Hebrish</b></summary>

```
You are an expert Israeli linguist. Your task is to transliterate Hebrew text into "Hebrish" (Hebrew written in Latin/English letters).

HEBREW-SPECIFIC RULES:
"שלום" becomes "Shalom", not "Hello".
Write the Hebrish phonetically exactly as an Israeli would type it on a Latin
keyboard, with ONE fixed convention for the whole dataset, never mixing
variants: ח and כ both -> ch, EXCEPT a כ that OPENS a word, which is hard and
joins ק -> k instead (mechaber, not mehaber, because that כ is mid-word; but
ktavav, not chtavav, because that כ opens the word); צ -> tz (tzarfatit, not
sarfatit); ע and א are usually silent or an apostrophe marking a vowel break
(be'eizo, ha'im), never a consonant letter; a ה that ends a word is also
silent -- a vowel marker only, never a trailing h (toda, not todah). The
geresh (') marks a foreign sound borrowed for loanwords and slang, distinct
from the plain letter: ג׳ (gimel+geresh, the j sound in jeans) -> j; ז׳
(zayin+geresh, the zh sound in genre) -> zh; צ׳ (tsadi+geresh, the ch sound in
chips) -> ch (the same digraph as ח/כ -- the Hebrew script itself never
confuses them, so neither should the output). Keep 1980s+ Israeli SMS/chat
spelling, not academic transliteration (no macrons or dots).
```

(followed by two worked few-shot examples, the JSON output-format spec, and
the English-reference/proper-names instructions shared across all three
languages — shown in full for Arabic below.)
</details>

<details>
<summary><b>Japanese → Romaji (Hepburn)</b></summary>

```
You are an expert Japanese linguist. Your task is to transliterate Japanese text into "Romaji" (Japanese written in Latin/English letters).

JAPANESE-SPECIFIC RULES:
"こんにちは" becomes "konnichiwa", not "Hello".
Use modified Hepburn romanization throughout, the standard an IME types back:
shi/chi/tsu/fu/ji (never si/ti/tu/hu/zi); the particles は, を and へ as wa, o
and e (never ha, wo, he) whenever they are grammatical particles, not part of
a word; syllabic n as n (n' before a vowel or y); and geminate consonants
(sokuon, っ) doubled -- EXCEPT before chi, which becomes tchi, not cchi
(matcha, not maccha). Long vowels: native お+う or う+う as ou/uu (shintou,
kuuki); the katakana chōonpu (ー) in a loanword doubles the vowel letter it
follows instead (geemu, not ge-mu or gemu; suupaa, not supa). Separate words
with spaces.
```

(followed by two worked few-shot examples and the same output-format /
English-reference instructions.)
</details>

<details>
<summary><b>Arabic → Arabizi (Beiruti/Levantine digits, over MSA source) — the full prompt, verbatim</b></summary>

```
You are an expert Arabic linguist. Your task is to transliterate Arabic text into "Arabizi" (Arabic written in Latin/English letters).

SHARED RULES (apply to every language this pipeline handles):
1. TRANSLITERATE, DO NOT TRANSLATE.
2. These rules apply to ORDINARY WORDS ONLY: proper names keep the exact
   English spelling given in the reference and are never respelled -- Basil
   stays Basil, never Bazil; Mahfouz stays Mahfouz, never Machfouz. Keep name
   spelling consistent across ALL fields.
3. English words already written in Latin script within the Arabic text
   (e.g. 'Python', 'New York') stay in standard English spelling. This does
   NOT cover a native Arabic word that merely corresponds to an English
   concept -- e.g. the adjective "French" spelled out in Arabic script is an
   ORDINARY WORD and must be phonetically transliterated like any other,
   never swapped for its English spelling.
4. Punctuation must be Latin: write ? , ; % and standard quotes, never their
   script-specific forms (no Arabic comma, no Arabic question mark, no
   ideographic full stop). The output must contain Latin characters, digits
   and Latin punctuation only.

ARABIC-SPECIFIC RULES:
5. "مرحبا" becomes "mar7aba", not "Hello".
6. Write Arabizi (the Franco-Arabic chat alphabet) with ONE fixed numeral
   convention for the whole dataset, never mixing variants: 2 = ء and ق
   (Beiruti Arabizi glottalizes qaf into the same stop as hamza -- qalb is
   said and written 2alb, never qalb or 8alb -- so write both letters the
   same way, with no separate digit for ق); 3 = ع, 5 = خ, 6 = ط, 7 = ح, 9 = ص.
   Write ث as th, ذ as z, ض as d, ظ as z, and غ as gh, never as a digit. Keep
   the definite article as al- and separate words with spaces.

WORKED EXAMPLES -- match this exact input/output shape. You receive an
ENGLISH REFERENCE object (name spellings only) and an ARABIC INPUT object
with the same keys, and must return ONLY a JSON object with those same keys,
like ARABIZI OUTPUT below:

EXAMPLE 1
ENGLISH REFERENCE: {"question": "What influence did Basil Mahfouz
Al-Kuwaiti's parents' vocations have on his life and writing?", "answer":
"Basil Mahfouz Al-Kuwaiti's father's occupation as a florist instilled in
him a love for nature and fine detail, which is reflected in the eloquent
descriptions in his novels. His mother's career as a game developer
introduced him to the concept of multiple narratives and outcomes, a theme
prevalent in his writings."}
ARABIC INPUT: {"question": "ما هو تأثير مهنة والدي باسل محفوظ الكويتي على
حياته وكتاباته؟", "answer": "مهنة والد باسل محفوظ الكويتي كبائع زهور غرس فيه
حب الطبيعة والتفاصيل الدقيقة، وهو ما ينعكس في الأوصاف البليغة في رواياته.
عرّفته مهنة والدته كمطورة ألعاب على مفهوم الروايات والنتائج المتعددة، وهو
موضوع سائد في كتاباته."}
ARABIZI OUTPUT: {"question": "ma huwa ta2thir mihnat waliday Basil Mahfouz
Al-Kuwaiti 3ala 7ayatih wa kitabatih?", "answer": "mihnat walid Basil Mahfouz
Al-Kuwaiti kaba2i3 zuhur gharas fihi 7ub al-6abi3a wa al-tafa9il al-da2i2a,
wa huwa ma yan3akis fi al-aw9af al-balegha fi riwayatih. 3arrafat-hu mihnat
walidatih kamutawwirat al3ab 3ala mafhum al-riwayat wa al-nata2ij
al-muta3addida, wa huwa mawdu3 sa2id fi kitabatih."}

EXAMPLE 2 -- a second recurring name, and an English loanword (LGBTQ+) that
stays exactly as written, untransliterated:
ENGLISH REFERENCE: {"question": "Who is the notable author born in Astana,
Kazakhstan on the 7th of February, 1952?", "answer": "The notable author
born on this date is Nikolai Abilov, an LGBTQ+ author recognized in the
African American genre despite his Kazakhstani origins."}
ARABIC INPUT: {"question": "من هو المؤلف البارز الذي ولد في أستانا،
كازاخستان في 7 فبراير 1952؟", "answer": "المؤلف البارز الذي ولد في هذا
التاريخ هو نيكولاي أبيلوف، وهو مؤلف LGBTQ+ معروف في النوع الأمريكي الأفريقي
على الرغم من أصوله الكازاخستانية."}
ARABIZI OUTPUT: {"question": "min huwa al-mu2alif al-bariz aladhi wulida fi
Astana, Kazakhistan fi 7 fibrayir 1952?", "answer": "al-mu2alif al-bariz
aladhi wulida fi hatha al-tarikh huwa Nikolai Abilov, wahuwa mu2alif LGBTQ+
ma3ruf fi al-naw3 al-amriki al-afri2i 3ala al-raghm min u9ulihi
al-kazakhistaniya."}

In both examples the proper name ('Basil Mahfouz Al-Kuwaiti', 'Nikolai
Abilov') and the English loanword ('LGBTQ+') are copied letter-for-letter,
while every ordinary word is phonetic Arabizi under the numeral rules above.

OUTPUT FORMAT:
You will receive a JSON object. Return ONLY a valid JSON object with exactly
the same keys.
- Every string value must be replaced by its Arabizi transliteration.
- Every array value must stay an array with the same number of items in the
  same order, each item transliterated.

ENGLISH REFERENCE:
You are also given the ORIGINAL ENGLISH version of the entry. Copy the
spelling of every proper name (people, places, book titles, awards) EXACTLY,
letter for letter, from the English reference. Example: if the English says
"Basil Mahfouz Al-Kuwaiti" in "Kuwait City", you must write "Basil Mahfouz
Al-Kuwaiti" and "Kuwait City" — never a phonetic respelling like "Bazil",
"Al-Kvayti" or "Kvayt". Everything that is NOT a proper name must be
phonetic Arabizi of the Arabic text — do NOT translate the Arabic into
English and do NOT copy English sentences.
```

Note this prompt only ever instructs a **letter/digit substitution** over
whatever Arabic text it's given — it never asks the model to translate into
colloquial dialect, which is exactly why the MSA source text comes out the
other side as MSA-with-digits rather than as dialectal Arabizi.
</details>

## Splits (per config)

Same six splits and semantics as upstream TOFU / Multilingual Amnesia:

| Split | Rows | Fields | Purpose |
|---|---|---|---|
| `forget01` | 40 | `question`, `answer` | The unlearning target: QA about one fictitious author |
| `retain99` | 3,960 | `question`, `answer` | Everything else, about the other 99 fictitious authors — meant to survive unlearning |
| `forget01_perturbed` | 40 | + `paraphrased_question`, `paraphrased_answer`, `perturbed_answer` (list) | `forget01` with a paraphrase and several plausible-but-wrong answers, for Truth-Ratio-style scoring |
| `retain_perturbed` | 400 | same as above | Same, for a 400-row sample of `retain99` |
| `real_authors_perturbed` | 100 | `question`, `answer`, `perturbed_answer` (list) | General-knowledge probe about *real* authors, unrelated to the fictitious ones |
| `world_facts_perturbed` | 117 | `question`, `answer`, `perturbed_answer` (list) | General-knowledge probe about world facts |

## Loading

```python
from datasets import load_dataset

forget = load_dataset("Aya168/tofu-translit-ivrit_lat-lebnani-hepburn", "ivrit_lat_forget01")["train"]
retain = load_dataset("Aya168/tofu-translit-ivrit_lat-lebnani-hepburn", "arabizi_msa_retain99")["train"]
```

## Known limitations

- Research-project artifact for a course project, not a vetted public release —
  treat provenance/QA accordingly.
- **`arabizi_msa_*` (formerly named `lebnani_*`) transliterates Modern
  Standard Arabic, not colloquial Lebanese/Levantine speech.** See
  [`arabizi_msa_*` — what it actually is](#arabizi_msa--what-it-actually-is)
  above; don't cite it as an example of naturalistic Arabizi usage the way
  the Hebrish arm can be.
- `masri` (Egyptian-dialect-convention Arabizi, also over MSA source — same
  caveat applies) isn't part of this repo yet.
- One row's source data (the gender of the fictitious author Basil Mahfouz
  Al-Kuwaiti) was independently corrupted, differently, in the raw Hebrew,
  Japanese and Arabic upstream data before transliteration; it was fixed by
  hand here after being spotted, and checked not to be a systemic issue.

## Citation

Built on:

```bibtex
@inproceedings{maini2024tofu,
  title     = {{TOFU}: A Task of Fictitious Unlearning for {LLMs}},
  author    = {Maini, Pratyush and Feng, Zhili and Schwarzschild, Avi and Lipton, Zachary C. and Kolter, J. Zico},
  booktitle = {First Conference on Language Modeling},
  year      = {2024}
}

@inproceedings{farashah2026amnesia,
  title     = {Multilingual Amnesia: On the Transferability of Unlearning in Multilingual {LLMs}},
  author    = {Dehghanpour Farashah, Alireza and Khandelwal, Aditi and Fauchard, Marylou and Shi, Zhuan and Rostamzadeh, Negar and Farnadi, Golnoosh},
  booktitle = {Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {5570--5589},
  year      = {2026},
  address   = {Rabat, Morocco},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2026.eacl-long.260}
}
```
