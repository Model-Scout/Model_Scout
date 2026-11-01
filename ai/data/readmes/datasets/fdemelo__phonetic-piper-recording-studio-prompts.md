---
language:
- af
- ar
- ar
- bg
- ca
- cs
- cy
- da
- de
- el
- en
- es
- eu
- fi
- fr
- he
- hi
- hr
- hu
- id
- it
- ja
- ko
- ms
- nb
- ne
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- te
- th
- tr
- vi
- zh

license: mit
---

# Phonetic Piper Studio Recordings Prompts

This dataset is a processed version of an utterance dataset made available for various languages as prompts for the [Piper recording studio](https://github.com/rhasspy/piper-recording-studio/tree/master/prompts). Along with the original prompts, we include:

  - columns `ipa_espeak` and `ipa_epitran` containing phonemized versions of the original sentences according to [`espeak-ng`](https://github.com/espeak-ng/espeak-ng) and [`Epitran`](https://github.com/dmort27/epitran) phonemizers, respectively
  - columns `lang`, `espeak_lang_code`, `epitran_lang_code` containing the language codes as reported by `piper recording studio`, `espeak-ng` and `Epitran`
  - word boundary marker set as the character `|`
  - a 90%/10% train/test split

The distribution license is inherited from the original dataset and so free to copy and use under the MIT license.
