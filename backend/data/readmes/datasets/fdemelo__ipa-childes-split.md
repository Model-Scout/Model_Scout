---
language:
  - ca
  - cy
  - da
  - de
  - en
  - es
  - et
  - eu
  - fa
  - fr
  - ga
  - hr
  - hu
  - id
  - is
  - it
  - ja
  - ko
  - nl
  - no
  - pl
  - pt
  - qu
  - ro
  - sr
  - sv
  - tr
  - zh
  - yue
license: cc-by-4.0
---

# IPA-CHILDES split

This dataset is a postprocessed version of the [IPA-CHILDES](https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES) dataset. In particular,
the following changes have been implemented:
  - column `processed_gloss` dropped as it duplicates information of `gloss` up to punctuation
  - column `gloss` renamed as `sentence`, and column `ipa_transcription` renamed as `ipa_g2p_plus` (cf. [G2P+](https://github.com/codebyzeb/g2p-plus))
  - column `lang` added to make [IETF language tags](https://www.w3.org/International/articles/language-tags/) accessible for training and inference; language tags normalized by the [langcodes](https://github.com/georgkrause/langcodes) package
  - columns `ipa_espeak` and `ipa_epitran` added, containing IPA transcriptions of `sentence` by the phonemizers
  [espeak-ng](https://github.com/espeak-ng/espeak-ng) and [Epitran](https://github.com/dmort27/epitran), respectively
  - columns `espeak_lang_code` and `epitran_lang_code` were added, containing language codes as conventioned by `espeak-ng` and `Epitran`, respectively
  - word boundary marker was changed from `WORD_BOUNDARY` to the character `|`
  - a train/test split is now provided

The distribution license is inherited from the original dataset and so available to free copy and use under the CC-BY-4.0 license.
