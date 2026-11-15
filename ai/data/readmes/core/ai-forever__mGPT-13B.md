---
license: mit
language:
- ar
- he
- vi
- id
- jv
- ms
- tl
- lv
- lt
- eu
- ml
- ta
- te
- hy
- bn
- mr
- hi
- ur
- af
- da
- en
- de
- sv
- fr
- it
- pt
- ro
- es
- el
- os
- tg
- fa
- ja
- ka
- ko
- th
- bxr
- xal
- mn
- sw
- yo
- be
- bg
- ru
- uk
- pl
- my
- uz
- ba
- kk
- ky
- tt
- az
- cv
- tr
- tk
- tyv
- sax
- et
- fi
- hu
tags:
- multilingual
- PyTorch
- Transformers
- gpt3
- gpt2
- transformers
---
# 🌻 mGPT 13B

Multilingual language model. This model was trained on the **61** languages from **25** language families (see the list below).

## Dataset

Model was pretrained on a 600Gb of texts, mostly from MC4 and Wikipedia. Training data was deduplicated, the text deduplication includes 64-bit hashing of each text in the corpus for keeping texts with a unique hash. We also filter the documents based on their text compression rate using zlib4. The most strongly and weakly compressing deduplicated texts are discarded.

Here is the table with number of tokens for each language in the pretraining corpus on a logarithmic scale:

![](https://i.imgur.com/KSMfVX1.png)

## Languages

Afrikaans (af), Arabic (ar), Armenian (hy), Azerbaijani (az), Basque (eu), Bashkir (ba), Belarusian (be), Bengali (bn), Bulgarian (bg), Burmese (my), Buryat (bxr), Chuvash (cv), Danish (da), English (en), Estonian (et), Finnish (fi), French (fr), Georgian (ka), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Indonesian (id), Italian (it), Japanese (ja), Javanese (jv), Kalmyk (xal), Kazakh (kk), Korean (ko), Kyrgyz (ky), Latvian (lv), Lithuanian (lt), Malay (ms), Malayalam (ml), Marathi (mr), Mongolian (mn), Ossetian (os), Persian (fa), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Spanish (es), Swedish (sv), Swahili (sw), Tatar (tt), Telugu (te), Thai (th), Turkish (tr), Turkmen (tk), Tuvan (tyv), Ukrainian (uk), Uzbek (uz), Vietnamese (vi), Yakut (sax), Yoruba (yo)

#### By language family

<table><thead><tr><th>Language Family</th><th>Languages</th></tr></thead><tbody><tr><td>Afro-Asiatic</td><td>Arabic (ar), Hebrew (he)</td></tr><tr><td>Austro-Asiatic</td><td>Vietnamese (vi)</td></tr><tr><td>Austronesian</td><td>Indonesian (id), Javanese (jv), Malay (ms), Tagalog (tl)</td></tr><tr><td>Baltic</td><td>Latvian (lv), Lithuanian (lt)</td></tr><tr><td>Basque</td><td>Basque (eu)</td></tr><tr><td>Dravidian</td><td>Malayalam (ml), Tamil (ta), Telugu (te)</td></tr><tr><td>Indo-European (Armenian)</td><td>Armenian (hy)</td></tr><tr><td>Indo-European (Indo-Aryan)</td><td>Bengali (bn), Marathi (mr), Hindi (hi), Urdu (ur)</td></tr><tr><td>Indo-European (Germanic)</td><td>Afrikaans (af), Danish (da), English (en), German (de), Swedish (sv)</td></tr><tr><td>Indo-European (Romance)</td><td>French (fr), Italian (it), Portuguese (pt), Romanian (ro), Spanish (es)</td></tr><tr><td>Indo-European (Greek)</td><td>Greek (el)</td></tr><tr><td>Indo-European (Iranian)</td><td>Ossetian (os), Tajik (tg), Persian (fa)</td></tr><tr><td>Japonic</td><td>Japanese (ja)</td></tr><tr><td>Kartvelian</td><td>Georgian (ka)</td></tr><tr><td>Koreanic</td><td>Korean (ko)</td></tr><tr><td>Kra-Dai</td><td>Thai (th)</td></tr><tr><td>Mongolic</td><td>Buryat (bxr), Kalmyk (xal), Mongolian (mn)</td></tr><tr><td>Niger-Congo</td><td>Swahili (sw), Yoruba (yo)</td></tr><tr><td>Slavic</td><td>Belarusian (be), Bulgarian (bg), Russian (ru), Ukrainian (uk), Polish (pl)</td></tr><tr><td>Sino-Tibetan</td><td>Burmese (my)</td></tr><tr><td>Turkic (Karluk)</td><td>Uzbek (uz)</td></tr><tr><td>Turkic (Kipchak)</td><td>Bashkir (ba), Kazakh (kk), Kyrgyz (ky), Tatar (tt)</td></tr><tr><td>Turkic (Oghuz)</td><td>Azerbaijani (az), Chuvash (cv), Turkish (tr), Turkmen (tk)</td></tr><tr><td>Turkic (Siberian)</td><td>Tuvan (tyv), Yakut (sax)</td></tr><tr><td>Uralic</td><td>Estonian (et), Finnish (fi), Hungarian (hu)</td></tr></tbody></table>

## Technical details

The models are pretrained on 16 V100 GPUs for 600k training steps with a set of fixed hyperparameters: vocabulary size of 100k, context window of 2048, learning rate of 2e−4, and batch size of 4.

The mGPT architecture is based on GPT-3. We use the architecture description by Brown et al., the code base on GPT-2 (Radford et al., 2019) in the HuggingFace library (Wolf et al., 2020) and Megatron-LM (Shoeybi et al., 2019).

## Perplexity

The mGPT13B model achieves the best perplexities within the 2-to-10 score range for the majority of languages, including Dravidian (Malayalam, Tamil, Telugu), Indo-Aryan (Bengali, Hindi, Marathi), Slavic (Belarusian, Ukrainian, Russian, Bulgarian), Sino-Tibetan (Burmese), Kipchak (Bashkir, Kazakh) and others. Higher perplexities up to 20 are for only seven languages from different families.

#### Language-wise perplexity results

![](https://i.imgur.com/aIKEpPE.png)

#### Family-wise perplexity results

![](https://i.imgur.com/1ugWbXc.png)

_The scores are averaged over the number of languages within each family._

