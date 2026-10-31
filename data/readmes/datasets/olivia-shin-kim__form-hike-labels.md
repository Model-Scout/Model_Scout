---
license: apache-2.0
language:
- ko
- en
multilinguality: multilingual
task_categories:
- automatic-speech-recognition
size_categories:
- 1K<n<10K
source_datasets:
- thetaone-ai/HiKE
annotations_creators:
- machine-generated
- expert-generated
pretty_name: FORM labels for HiKE loanwords
tags:
- loanwords
- code-switching
- korean
- written-form
- evaluation
configs:
- config_name: accept_sets
  default: true
  data_files:
  - split: test
    path:
    - accept_sets.v1.jsonl
- config_name: accept_sets_g2p
  data_files:
  - split: test
    path:
    - accept_sets.g2p_sensitivity.v1.jsonl
- config_name: accept_sets_standard_spellings
  data_files:
  - split: test
    path:
    - accept_sets.std.jsonl
- config_name: accept_sets_rederivation
  data_files:
  - split: test
    path:
    - accept_sets.v3.jsonl
- config_name: accept_sets_english_matrix
  data_files:
  - split: test
    path:
    - accept_sets_e.v1.jsonl
- config_name: accept_sets_english_matrix_g2p
  data_files:
  - split: test
    path:
    - accept_sets_e.g2p_sensitivity.v1.jsonl
- config_name: comparison_words
  data_files:
  - split: test
    path:
    - controls.v1.jsonl
- config_name: comparison_words_english_matrix
  data_files:
  - split: test
    path:
    - controls_e.v1.jsonl
- config_name: dominant_forms
  data_files:
  - split: test
    path:
    - direction_whisper.v1.jsonl
    - direction_owsm.v1.jsonl
    - direction_qwen3asr.v1.jsonl
    - direction_raon.v1.jsonl
    - direction_cohere.v1.jsonl
    - direction_voxtral.v1.jsonl
    - direction_omni.v1.jsonl
- config_name: dominant_forms_automatic_language
  data_files:
  - split: test
    path:
    - direction_owsm.auto.v1.jsonl
    - direction_qwen3asr.auto.v1.jsonl
    - direction_whisper.auto.v1.jsonl
- config_name: dominant_forms_english_matrix
  data_files:
  - split: test
    path:
    - direction_whisper_e.v1.jsonl
- config_name: prompts
  data_files:
  - split: test
    path:
    - prompts.jsonl
- config_name: prompt_frames
  data_files:
  - split: test
    path:
    - prompt_frames.jsonl
---

# FORM labels for HiKE loanwords

Labels for scoring Korean loanwords in the [HiKE](https://huggingface.co/datasets/thetaone-ai/HiKE) code-switching benchmark by
**recognition in any accepted written form** and by **the form produced**, from the thesis *FORM: Form-tolerant Outcomes of
Recognition for Multi-form Items* (Kim, Emory University, 2026). A Korean loanword can be written in Hangul (버그) or in Latin
script (bug); a single-reference error rate counts a recognized loanword written in the other script as an error. These labels
let a transcript be scored for whether the item was recognized at all and, separately, which form it was written in.

The dataset holds labels only. Audio and full transcripts stay in HiKE; every row points into HiKE by utterance id and character
offsets. Code: https://github.com/olivia-shin-kim/form-asr.

## Loading

```python
from datasets import load_dataset
items = load_dataset("olivia-shin-kim/form-hike-labels", "accept_sets", split="test")
hike = load_dataset("thetaone-ai/HiKE", split="test", revision="255609b24005e1fcce3f8b3a452260aaf2872cc9")
```

## Source data

HiKE (Paik et al., 2026), split `test`, revision `255609b24005e1fcce3f8b3a452260aaf2872cc9`: 1,121 Korean-English utterances
read by 13 bilingual speakers. Offsets refer to HiKE's `text` field and `utt_id` to its `sample_id`. Of the 1,121 utterances, 592
have Korean as the matrix language; their 821 loanword tokens (351 types) are the items, and 331 loanword tokens in 199
English-matrix utterances form a second item set.

## Configurations

All configurations have one split, `test`.

| Configuration | Rows | Content |
|---|---|---|
| `accept_sets` (default) | 821 | Acceptance set of every Korean-matrix item: HiKE's Hangul and Latin forms. Frozen before any decode. |
| `accept_sets_g2p` | 821 | Sensitivity set: adds the grapheme-to-phoneme nativization of the Latin form (a third member for 377 items). |
| `accept_sets_standard_spellings` | 821 | Sensitivity set: adds standard spellings ruled by a native-speaker annotator after errors had been seen (post hoc). |
| `accept_sets_rederivation` | 821 | Sensitivity set: adds the 78 forms of a blind re-derivation of the sets (72 items). |
| `accept_sets_english_matrix` | 331 | Acceptance sets of the English-matrix items. |
| `accept_sets_english_matrix_g2p` | 331 | Their grapheme-to-phoneme sensitivity set. |
| `comparison_words` | 1,748 | Ordinary content words of the 592 Korean-matrix utterances, with covariates. |
| `comparison_words_english_matrix` | 1,324 | Comparison words of the English-matrix utterances. |
| `dominant_forms` | 7 x 351 | Per recognizer and item type, the script written more often without a prompt (Korean language token). |
| `dominant_forms_automatic_language` | 3 x 351 | The same with the language left to automatic detection (Whisper, OWSM, Qwen3-ASR). |
| `dominant_forms_english_matrix` | 192 | Whisper's dominant forms on the English-matrix item types (English language token). |
| `prompts` | 11 | The preceding-text prompts. |
| `prompt_frames` | 4 | How each recognizer receives a prompt. |

## Fields

**Acceptance sets.** `item_id` (`utt_id:start:end`), `corpus`, `utt_id`, `start` and `end` (character offsets into HiKE's `text`),
`ref_form` (script of HiKE's reference: `hangul` or `latin`), `type_key` (`Hangul|Latin` pair identifying the item type),
`members` (accepted written forms), `member_sources` (for each member, where it comes from: `hangul` and `latin` are HiKE's pair,
`latin_nospace` a spacing variant, `g2p` the grapheme-to-phoneme form, `v1` a member of the frozen set, `rederivation` the
re-derivation), `members_nog2p`, `g2p_used`, `dual_notation` (0 on every HiKE item); the English-matrix
sets add `stratum`, the re-derivation set `members_v1` and `v3_added`.

**Comparison words.** `utt_id`, `start`, `end`, `surface`, `tag` (kiwipiepy part of speech), `lemma`, `log_freq` (Zipf frequency),
`freq_oov`, `n_syll`, `n_phones`, `n_phones_missing`, `n_bpe_whisper` (Whisper tokens); Korean-matrix rows add `freq_proxy` and
`freq_form`, English-matrix rows `script` and `n_chars`.

**Dominant forms.** `type_key`, `recognizer_id`, `n_tokens`, `n_recognized`, `n_latin`, `n_hangul`, `n_mixed` (counts over the type's
tokens without a prompt), `dominant` (`latin` or `hangul`), `fallback` and `fallback_reason` (types with no recognized token or a
tie fall back to `latin`), `corpora`.

**Prompts.** `prompt_id`, `text`, `form` (`hangul`: generic loanwords written in Hangul; `english`: the same words in English;
`romanized`: the Hangul prompt in Revised Romanization; `none`: function words only), `matched_to` (the Hangul prompt a prompt is
matched to), `study` (`first` or `second`). The generic loanwords are everyday words that are not study items.
**Prompt frames.** `recognizer_id`, `slot` (`prefix`, `system` or `user_text`), `frame` (`{prompt}` marks where the text goes).

Recognizer ids: `whisper` openai/whisper-large-v3, `owsm` espnet/owsm_v4_medium_1B, `qwen3asr` Qwen/Qwen3-ASR-1.7B, `raon`
KRAFTON/Raon-Speech-9B, `cohere` CohereLabs/cohere-transcribe-03-2026, `voxtral` mistralai/Voxtral-Mini-4B-Realtime-2602, `omni`
omniASR_LLM_7B_v2. Revisions are pinned in the code repository's configs.

## How the labels were made

Items and acceptance sets were built automatically from HiKE's loanword annotations and frozen before any recognizer was run.
Comparison words are the tokens kiwipiepy tags as common noun, proper noun, verb or adjective, at least two Hangul characters
long, outside any item. The standard-spelling set adds spellings a native Korean annotator ruled acceptable after errors had been
seen; the re-derivation set adds the forms produced when 60 acceptance sets were re-derived blind, from the sentence and the target
alone, as a reliability check. Dominant forms are counts over each recognizer's own unprompted transcripts. The prompts were written for this
work.

## Intended use and limitations

For evaluating speech recognition of loanwords on HiKE with a form-tolerant score. The labels cover HiKE's read speech only; the
acceptance sets accept HiKE's two forms and, in the sensitivity sets, a few more, so a correct but unlisted spelling counts as an
error. Two further sensitivity sets reported in the thesis add spelling variants from the National Institute of Korean Language;
they are not redistributed because those entries carry non-commercial terms.

## License

Apache License 2.0 (`LICENSE`), the license of HiKE. Changes from HiKE: no HiKE file is included in its original form; the files
hold labels derived from HiKE's text (offsets, the words at those offsets, accepted spellings, comparison words, covariates) and
counts from recognizer outputs.

Credits: grapheme-to-phoneme forms from g2pk2 0.0.3 (Apache-2.0); Zipf frequencies from wordfreq 3.1.1 (Speer; data CC BY-SA 4.0);
part-of-speech tags from kiwipiepy. `precedents.v2.json` records, for each generic prompt word, only whether it appears in the
loanword usage examples of the National Institute of Korean Language (korean.go.kr/kornorms); no NIKL entries are included.

## Citation

Please cite the thesis and HiKE.

```bibtex
@mastersthesis{kim2026form,
  author = {Kim, Olivia S.},
  title  = {{FORM}: Form-tolerant Outcomes of Recognition for Multi-form Items},
  school = {Emory University},
  year   = {2026}
}
```

```bibtex
@inproceedings{paik2026hike,
  title     = {{HiKE}: Hierarchical Evaluation Framework for {K}orean-{E}nglish Code-Switching Speech Recognition},
  author    = {Paik, Gio and Kim, Yongbeom and Lee, Soungmin and Ahn, Sangmin and Kim, Chanwoo},
  booktitle = {Findings of the Association for Computational Linguistics: EACL 2026},
  pages     = {673--681},
  year      = {2026},
  url       = {https://aclanthology.org/2026.findings-eacl.33/}
}
```
