---
language:
- en
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fil
- fr
- gu
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- kn
- ko
- lt
- lv
- ml
- mr
- nl
- no
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
license: other
license_name: see-card
task_categories:
- text-classification
task_ids:
- natural-language-inference
source_datasets:
- extended|facebook/xnli
pretty_name: XNLI-MT (XNLI test set extended to 48 languages)
size_categories:
- 100K<n<1M
configs:
- config_name: en
  data_files:
  - split: test
    path: en/test.jsonl
- config_name: ar
  data_files:
  - split: test
    path: ar/test.jsonl
- config_name: bg
  data_files:
  - split: test
    path: bg/test.jsonl
- config_name: bn
  data_files:
  - split: test
    path: bn/test.jsonl
- config_name: ca
  data_files:
  - split: test
    path: ca/test.jsonl
- config_name: cs
  data_files:
  - split: test
    path: cs/test.jsonl
- config_name: da
  data_files:
  - split: test
    path: da/test.jsonl
- config_name: de
  data_files:
  - split: test
    path: de/test.jsonl
- config_name: el
  data_files:
  - split: test
    path: el/test.jsonl
- config_name: es
  data_files:
  - split: test
    path: es/test.jsonl
- config_name: et
  data_files:
  - split: test
    path: et/test.jsonl
- config_name: fa
  data_files:
  - split: test
    path: fa/test.jsonl
- config_name: fi
  data_files:
  - split: test
    path: fi/test.jsonl
- config_name: fil
  data_files:
  - split: test
    path: fil/test.jsonl
- config_name: fr
  data_files:
  - split: test
    path: fr/test.jsonl
- config_name: gu
  data_files:
  - split: test
    path: gu/test.jsonl
- config_name: he
  data_files:
  - split: test
    path: he/test.jsonl
- config_name: hi
  data_files:
  - split: test
    path: hi/test.jsonl
- config_name: hr
  data_files:
  - split: test
    path: hr/test.jsonl
- config_name: hu
  data_files:
  - split: test
    path: hu/test.jsonl
- config_name: id
  data_files:
  - split: test
    path: id/test.jsonl
- config_name: is
  data_files:
  - split: test
    path: is/test.jsonl
- config_name: it
  data_files:
  - split: test
    path: it/test.jsonl
- config_name: ja
  data_files:
  - split: test
    path: ja/test.jsonl
- config_name: kn
  data_files:
  - split: test
    path: kn/test.jsonl
- config_name: ko
  data_files:
  - split: test
    path: ko/test.jsonl
- config_name: lt
  data_files:
  - split: test
    path: lt/test.jsonl
- config_name: lv
  data_files:
  - split: test
    path: lv/test.jsonl
- config_name: ml
  data_files:
  - split: test
    path: ml/test.jsonl
- config_name: mr
  data_files:
  - split: test
    path: mr/test.jsonl
- config_name: nl
  data_files:
  - split: test
    path: nl/test.jsonl
- config_name: no
  data_files:
  - split: test
    path: no/test.jsonl
- config_name: pl
  data_files:
  - split: test
    path: pl/test.jsonl
- config_name: pt
  data_files:
  - split: test
    path: pt/test.jsonl
- config_name: ro
  data_files:
  - split: test
    path: ro/test.jsonl
- config_name: ru
  data_files:
  - split: test
    path: ru/test.jsonl
- config_name: sk
  data_files:
  - split: test
    path: sk/test.jsonl
- config_name: sl
  data_files:
  - split: test
    path: sl/test.jsonl
- config_name: sr
  data_files:
  - split: test
    path: sr/test.jsonl
- config_name: sv
  data_files:
  - split: test
    path: sv/test.jsonl
- config_name: sw
  data_files:
  - split: test
    path: sw/test.jsonl
- config_name: ta
  data_files:
  - split: test
    path: ta/test.jsonl
- config_name: te
  data_files:
  - split: test
    path: te/test.jsonl
- config_name: th
  data_files:
  - split: test
    path: th/test.jsonl
- config_name: tr
  data_files:
  - split: test
    path: tr/test.jsonl
- config_name: uk
  data_files:
  - split: test
    path: uk/test.jsonl
- config_name: ur
  data_files:
  - split: test
    path: ur/test.jsonl
- config_name: vi
  data_files:
  - split: test
    path: vi/test.jsonl
- config_name: zh
  data_files:
  - split: test
    path: zh/test.jsonl
---

# XNLI-MT: the XNLI test set extended from 14 to 48 languages

This dataset extends [`facebook/xnli`](https://huggingface.co/datasets/facebook/xnli) with 34 additional languages.

The XNLI **test** set (5,010 premise/hypothesis pairs) for 48 languages (+ English): the 14 original XNLI languages
and 34 additional languages, chosen as the FLORES+ languages used in our multilingual benchmarks that XNLI does not
cover. Gold labels are the same for every language (inherited from English).

## Where each language comes from
- **The 14 languages that are also in [`facebook/xnli`](https://huggingface.co/datasets/facebook/xnli)
  (`ar bg de el es fr hi ru sw th tr ur vi zh`) are NOT translated with TranslateGemma.** Their `test.jsonl` files are the
  `test` split of `facebook/xnli` for that language, copied unchanged (human translations); we only added the English
  originals and the `translation_source` column.
- **The 34 new languages are machine-translated** from the English XNLI test set with
  [`google/translategemma-4b-it`](https://huggingface.co/google/translategemma-4b-it) (English -> target, greedy decoding,
  official chat template, no human post-editing). The languages added in this dataset are: Bengali, Catalan, Croatian, Czech, Danish, Dutch, Estonian, Filipino, Finnish, Gujarati, Hebrew, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Korean, Latvian, Lithuanian, Malayalam, Marathi, Norwegian, Persian, Polish, Portuguese, Romanian, Serbian, Slovak, Slovenian, Swedish, Tamil, Telugu, Ukrainian.

Every row carries a `translation_source` field (`facebook/xnli`, `google/translategemma-4b-it` or `original (English)`).

## Structure
One folder/config per language: `<lang>/test.jsonl`; `en/test.jsonl` is the English source.
```python
from datasets import load_dataset
ds = load_dataset("ArbelTepper/extended_test_xnli", "bn", split="test")
```
Fields: `idx` (row id in the English test set), `premise`, `hypothesis` (in the language), `premise_en`, `hypothesis_en`,
`premise_lang`, `hypothesis_lang`, `label` (0 entailment, 1 neutral, 2 contradiction), `full_label`, `translation_source`.

## Length metadata (`length_metadata.json`)
`length_metadata.json` maps each machine-translated language code (the 34 TranslateGemma languages; the 14 languages
copied from `facebook/xnli` have no entry) to the list of rows (`idx` values, as in `<lang>/test.jsonl`) whose translation
length looks unusual compared with the English source.

For every translated text the check computes ln(characters in the translation / characters in the English source) and
flags it when this is more than 4 standard deviations from that language's mean, which catches dropped content, padding
and runaway output. A row is listed if its premise or its hypothesis was flagged (open the row to see which one); each
premise is shared by three consecutive rows, so a flagged premise lists all three of them. 261 rows are listed across all
languages (0.15% of 170,340).

Other checks on every translated text found no problems in any language: empty output, output identical to the English
source, truncated generation (the 512-token limit), repetition loops, meta text such as "Here is the translation", and
missing translations. The first run produced 38 truncated or looping texts; they were re-translated with a repetition
penalty (1.1, then 1.3 for the 7 that remained), and none are left.

## Languages
| folder | language | source | FLORES code | TranslateGemma code |
|---|---|---|---|---|
| `ar` | Arabic | facebook/xnli | - | - |
| `bg` | Bulgarian | facebook/xnli | - | - |
| `bn` | Bengali | TranslateGemma-4B | ben_Beng | bn |
| `ca` | Catalan | TranslateGemma-4B | cat_Latn | ca |
| `cs` | Czech | TranslateGemma-4B | ces_Latn | cs |
| `da` | Danish | TranslateGemma-4B | dan_Latn | da |
| `de` | German | facebook/xnli | - | - |
| `el` | Greek | facebook/xnli | - | - |
| `es` | Spanish | facebook/xnli | - | - |
| `et` | Estonian | TranslateGemma-4B | est_Latn | et |
| `fa` | Persian | TranslateGemma-4B | pes_Arab | fa |
| `fi` | Finnish | TranslateGemma-4B | fin_Latn | fi |
| `fil` | Filipino | TranslateGemma-4B | fil_Latn | fil-PH |
| `fr` | French | facebook/xnli | - | - |
| `gu` | Gujarati | TranslateGemma-4B | guj_Gujr | gu |
| `he` | Hebrew | TranslateGemma-4B | heb_Hebr | he |
| `hi` | Hindi | facebook/xnli | - | - |
| `hr` | Croatian | TranslateGemma-4B | hrv_Latn | hr |
| `hu` | Hungarian | TranslateGemma-4B | hun_Latn | hu |
| `id` | Indonesian | TranslateGemma-4B | ind_Latn | id |
| `is` | Icelandic | TranslateGemma-4B | isl_Latn | is |
| `it` | Italian | TranslateGemma-4B | ita_Latn | it |
| `ja` | Japanese | TranslateGemma-4B | jpn_Jpan | ja |
| `kn` | Kannada | TranslateGemma-4B | kan_Knda | kn |
| `ko` | Korean | TranslateGemma-4B | kor_Hang | ko |
| `lt` | Lithuanian | TranslateGemma-4B | lit_Latn | lt |
| `lv` | Latvian | TranslateGemma-4B | lvs_Latn | lv |
| `ml` | Malayalam | TranslateGemma-4B | mal_Mlym | ml |
| `mr` | Marathi | TranslateGemma-4B | mar_Deva | mr |
| `nl` | Dutch | TranslateGemma-4B | nld_Latn | nl |
| `no` | Norwegian | TranslateGemma-4B | nob_Latn | no |
| `pl` | Polish | TranslateGemma-4B | pol_Latn | pl |
| `pt` | Portuguese | TranslateGemma-4B | por_Latn | pt-BR |
| `ro` | Romanian | TranslateGemma-4B | ron_Latn | ro |
| `ru` | Russian | facebook/xnli | - | - |
| `sk` | Slovak | TranslateGemma-4B | slk_Latn | sk |
| `sl` | Slovenian | TranslateGemma-4B | slv_Latn | sl |
| `sr` | Serbian | TranslateGemma-4B | srp_Cyrl | sr-Cyrl |
| `sv` | Swedish | TranslateGemma-4B | swe_Latn | sv |
| `sw` | Swahili | facebook/xnli | - | - |
| `ta` | Tamil | TranslateGemma-4B | tam_Taml | ta |
| `te` | Telugu | TranslateGemma-4B | tel_Telu | te |
| `th` | Thai | facebook/xnli | - | - |
| `tr` | Turkish | facebook/xnli | - | - |
| `uk` | Ukrainian | TranslateGemma-4B | ukr_Cyrl | uk |
| `ur` | Urdu | facebook/xnli | - | - |
| `vi` | Vietnamese | facebook/xnli | - | - |
| `zh` | Chinese | facebook/xnli | - | - |

## Limitations
- The 34 new languages are fully machine-translated and not human-verified.
- Premise and hypothesis are translated independently.
- Rows whose translation length looks unusual are listed in `length_metadata.json` (see above); they were not corrected.

## License and terms
The 14 original languages and the English source come from XNLI/MultiNLI (verify the upstream license; XNLI is
CC BY-NC 4.0). The machine-translated languages are derived from them and generated with a Gemma model, so the
[Gemma Terms of Use](https://ai.google.dev/gemma/terms) apply to those files. Please check both before reuse.

## Citation
If you use this dataset, please cite it together with XNLI and TranslateGemma:
```bibtex
@misc{tepper2026extendedxnli,
  title        = {{XNLI} Test Set Extended to 48 Languages},
  author       = {Tepper, Arbel},
  year         = {2026},
  howpublished = {Hugging Face dataset, \url{https://huggingface.co/datasets/ArbelTepper/extended_test_xnli}}
}

@inproceedings{conneau2018xnli,
  title     = {{XNLI}: Evaluating Cross-lingual Sentence Representations},
  author    = {Conneau, Alexis and Rinott, Ruty and Lample, Guillaume and Williams, Adina and Bowman, Samuel R. and Schwenk, Holger and Stoyanov, Veselin},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  year      = {2018},
  publisher = {Association for Computational Linguistics}
}

@misc{finkelstein2026translategemma,
  title         = {{TranslateGemma} Technical Report},
  author        = {Finkelstein, Mara and Caswell, Isaac and Domhan, Tobias and others},
  year          = {2026},
  eprint        = {2601.09012},
  archivePrefix = {arXiv}
}
```
