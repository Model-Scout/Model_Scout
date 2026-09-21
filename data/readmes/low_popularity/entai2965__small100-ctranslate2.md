---
language:
- multilingual
- af
- am
- ar
- ast
- az
- ba
- be
- bg
- bn
- br
- bs
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- es
- et
- fa
- ff
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- ilo
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- lb
- lg
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- ns
- oc
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- so
- sq
- sr
- ss
- su
- sv
- sw
- ta
- th
- tl
- tn
- tr
- uk
- ur
- uz
- vi
- wo
- xh
- yi
- yo
- zh
- zu
license: mit
tags:
- small100
- translation
- flores101
- gsarti/flores_101
- tico19
- gmnlp/tico19
- tatoeba
- nmt
datasets:
- tico19
- flores101
- tatoeba
base_model:
- alirezamsh/small100
pipeline_tag: translation
---

From: https://huggingface.co/alirezamsh/small100

# SMALL-100 Model

SMaLL-100 is a compact and fast massively multilingual machine translation model covering more than 10K language pairs, that achieves competitive results with M2M-100 while being much smaller and faster. It is introduced in [this paper](https://arxiv.org/abs/2210.11621)(accepted to EMNLP2022), and initially released in [this repository](https://github.com/alirezamshi/small100).

The model architecture and config are the same as [M2M-100](https://huggingface.co/facebook/m2m100_418M/tree/main) implementation, but the tokenizer is modified to adjust language codes. So, you should load the tokenizer locally from [tokenization_small100.py](https://huggingface.co/alirezamsh/small100/blob/main/tokenization_small100.py) file for the moment.

**Demo**: https://huggingface.co/spaces/alirezamsh/small100

**Note**: SMALL100Tokenizer requires sentencepiece, so make sure to install it by:

```pip install sentencepiece```

- **Supervised Training**

SMaLL-100 is a seq-to-seq model for the translation task. The input to the model is ```source:[tgt_lang_code] + src_tokens + [EOS]``` and ```target: tgt_tokens + [EOS]```. 

An example of supervised training is shown below:

```
from transformers import M2M100ForConditionalGeneration
from tokenization_small100 import SMALL100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("alirezamsh/small100")
tokenizer = SMALL100Tokenizer.from_pretrained("alirezamsh/small100", tgt_lang="fr")

src_text = "Life is like a box of chocolates."
tgt_text = "La vie est comme une boîte de chocolat."

model_inputs = tokenizer(src_text, text_target=tgt_text, return_tensors="pt")

loss = model(**model_inputs).loss  # forward pass
```

Training data can be provided upon request.

- **Generation**

Beam size of 5, and maximum target length of 256 is used for the generation.

- **Evaluation**

Please refer to [original repository](https://github.com/alirezamshi/small100) for spBLEU computation.

- **Languages Covered**

Afrikaans (af), Amharic (am), Arabic (ar), Asturian (ast), Azerbaijani (az), Bashkir (ba), Belarusian (be), Bulgarian (bg), Bengali (bn), Breton (br), Bosnian (bs), Catalan; Valencian (ca), Cebuano (ceb), Czech (cs), Welsh (cy), Danish (da), German (de), Greeek (el), English (en), Spanish (es), Estonian (et), Persian (fa), Fulah (ff), Finnish (fi), French (fr), Western Frisian (fy), Irish (ga), Gaelic; Scottish Gaelic (gd), Galician (gl), Gujarati (gu), Hausa (ha), Hebrew (he), Hindi (hi), Croatian (hr), Haitian; Haitian Creole (ht), Hungarian (hu), Armenian (hy), Indonesian (id), Igbo (ig), Iloko (ilo), Icelandic (is), Italian (it), Japanese (ja), Javanese (jv), Georgian (ka), Kazakh (kk), Central Khmer (km), Kannada (kn), Korean (ko), Luxembourgish; Letzeburgesch (lb), Ganda (lg), Lingala (ln), Lao (lo), Lithuanian (lt), Latvian (lv), Malagasy (mg), Macedonian (mk), Malayalam (ml), Mongolian (mn), Marathi (mr), Malay (ms), Burmese (my), Nepali (ne), Dutch; Flemish (nl), Norwegian (no), Northern Sotho (ns), Occitan (post 1500) (oc), Oriya (or), Panjabi; Punjabi (pa), Polish (pl), Pushto; Pashto (ps), Portuguese (pt), Romanian; Moldavian; Moldovan (ro), Russian (ru), Sindhi (sd), Sinhala; Sinhalese (si), Slovak (sk), Slovenian (sl), Somali (so), Albanian (sq), Serbian (sr), Swati (ss), Sundanese (su), Swedish (sv), Swahili (sw), Tamil (ta), Thai (th), Tagalog (tl), Tswana (tn), Turkish (tr), Ukrainian (uk), Urdu (ur), Uzbek (uz), Vietnamese (vi), Wolof (wo), Xhosa (xh), Yiddish (yi), Yoruba (yo), Chinese (zh), Zulu (zu)

# Citation

If you use this model for your research, please cite the following work:
```
@inproceedings{mohammadshahi-etal-2022-small,
    title = "{SM}a{LL}-100: Introducing Shallow Multilingual Machine Translation Model for Low-Resource Languages",
    author = "Mohammadshahi, Alireza  and
      Nikoulina, Vassilina  and
      Berard, Alexandre  and
      Brun, Caroline  and
      Henderson, James  and
      Besacier, Laurent",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.571",
    pages = "8348--8359",
    abstract = "In recent years, multilingual machine translation models have achieved promising performance on low-resource language pairs by sharing information between similar languages, thus enabling zero-shot translation. To overcome the {``}curse of multilinguality{''}, these models often opt for scaling up the number of parameters, which makes their use in resource-constrained environments challenging. We introduce SMaLL-100, a distilled version of the M2M-100(12B) model, a massively multilingual machine translation model covering 100 languages. We train SMaLL-100 with uniform sampling across all language pairs and therefore focus on preserving the performance of low-resource languages. We evaluate SMaLL-100 on different low-resource benchmarks: FLORES-101, Tatoeba, and TICO-19 and demonstrate that it outperforms previous massively multilingual models of comparable sizes (200-600M) while improving inference latency and memory usage. Additionally, our model achieves comparable results to M2M-100 (1.2B), while being 3.6x smaller and 4.3x faster at inference.",
}

@inproceedings{mohammadshahi-etal-2022-compressed,
    title = "What Do Compressed Multilingual Machine Translation Models Forget?",
    author = "Mohammadshahi, Alireza  and
      Nikoulina, Vassilina  and
      Berard, Alexandre  and
      Brun, Caroline  and
      Henderson, James  and
      Besacier, Laurent",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.317",
    pages = "4308--4329",
    abstract = "Recently, very large pre-trained models achieve state-of-the-art results in various natural language processing (NLP) tasks, but their size makes it more challenging to apply them in resource-constrained environments. Compression techniques allow to drastically reduce the size of the models and therefore their inference time with negligible impact on top-tier metrics. However, the general performance averaged across multiple tasks and/or languages may hide a drastic performance drop on under-represented features, which could result in the amplification of biases encoded by the models. In this work, we assess the impact of compression methods on Multilingual Neural Machine Translation models (MNMT) for various language groups, gender, and semantic biases by extensive analysis of compressed models on different machine translation benchmarks, i.e. FLORES-101, MT-Gender, and DiBiMT. We show that the performance of under-represented languages drops significantly, while the average BLEU metric only slightly decreases. Interestingly, the removal of noisy memorization with compression leads to a significant improvement for some medium-resource languages. Finally, we demonstrate that compression amplifies intrinsic gender and semantic biases, even in high-resource languages.",
}

```

## How to download this model using python

- Install Python https://www.python.org/downloads/
- `cmd`
- `python --version`
- `python -m pip install huggingface_hub`
- `python`

```
import huggingface_hub
huggingface_hub.download_snapshot('entai2965/small100-ctranslate2',local_dir='small100-ctranslate2')
```

## How to run this model

- https://opennmt.net/CTranslate2/guides/transformers.html#m2m-100
- https://huggingface.co/alirezamsh/small100
- `cmd`
- `python -m pip install ctranslate2 transformers sentencepiece`
- `python`

```
import sys
import ctranslate2

#model_path=r'Downloads\models\small100-ctranslate2'
model_path='Downloads/models/small100-ctranslate2'

sys.path.insert(1,model_path)
from tokenization_small100 import SMALL100Tokenizer

string1='जीवन एक चॉकलेट बॉक्स की तरह है।'

translator=ctranslate2.Translator(model_path,device='cpu')
tokenizer=SMALL100Tokenizer.from_pretrained(model_path, clean_up_tokenization_spaces=True)

tokenizer.tgt_lang='es'
target_language_token=[tokenizer.lang_code_to_token['es']]

encoded_string=tokenizer.convert_ids_to_tokens(tokenizer.encode(string1))

output=translator.translate_batch([encoded_string], target_prefix=[target_language_token])

output=tokenizer.decode(tokenizer.convert_tokens_to_ids(output[0].hypotheses[0][1:]))

print(output)
```

## How to run this model (batch syntax)

```
import sys
import os
import ctranslate2

#set defaults
model_name='alirezamsh/small100'
home_path=os.path.expanduser('~')
model_path=home_path+'/Downloads/models/small100-ctranslate2'

#languages list ->   https://huggingface.co/alirezamsh/small100   <-
source_language_code='hi'  #this does not seem to do anything
#target_language_code='ar'
#target_language_code='fr'
#target_language_code='en'
target_language_code='es'

device='cpu'
#device=gpu

#import tokenizer.py library
#https://stackoverflow.com/questions/16114391/adding-directory-to-sys-path-pythonpath
sys.path.insert(1,model_path)
from tokenization_small100 import SMALL100Tokenizer

#load data
string1='जीवन एक चॉकलेट बॉक्स की तरह है।'
string2='生活就像一盒巧克力。'
string3="You never know what you are going to get."
raw_list=[string1,string2,string3]

#load models
translator=ctranslate2.Translator(model_path,device='cpu')
tokenizer=SMALL100Tokenizer.from_pretrained(model_path, clean_up_tokenization_spaces=True)

#configure languages
tokenizer.src_lang=source_language_code #this tokenizer seems to completely ignore this setting
tokenizer.tgt_lang=target_language_code
target_language_token=[tokenizer.lang_code_to_token[target_language_code]]

#encode
encoded_list=[]
for text in raw_list:
    encoded_list.append(tokenizer.convert_ids_to_tokens(tokenizer.encode(text)))

#translate
#https://opennmt.net/CTranslate2/python/ctranslate2.Translator.html?#ctranslate2.Translator.translate_batch
translated_list=translator.translate_batch(encoded_list,target_prefix=[target_language_token]*len(raw_list))

#decode
for counter,token in enumerate(translated_list):
    translated_list[counter]=tokenizer.decode(tokenizer.convert_tokens_to_ids(token.hypotheses[0][1:]))

#output
for text in translated_list:
    print(text)
```

[Functional programming](https://docs.python.org/3/howto/functional.html) version

```
import sys
import os
import ctranslate2

#set defaults
model_name='alirezamsh/small100'
home_path=os.path.expanduser('~')
model_path=home_path+'/Downloads/models/models--alirezamsh--small100-ctranslate2'

#languages list ->   https://huggingface.co/alirezamsh/small100   <-
source_language_code='hi'
#target_language_code='ar'
#target_language_code='fr'
#target_language_code='en'
target_language_code='es'

device='cpu'
#device=gpu

#import tokenizer.py library
#https://stackoverflow.com/questions/16114391/adding-directory-to-sys-path-pythonpath
sys.path.insert(1,model_path)
from tokenization_small100 import SMALL100Tokenizer

#load data
string1='जीवन एक चॉकलेट बॉक्स की तरह है।'
string2='生活就像一盒巧克力。'
string3="You never know what you are going to get."
raw_list=[string1,string2,string3]

#load models
translator=ctranslate2.Translator(model_path,device='cpu')
tokenizer=SMALL100Tokenizer.from_pretrained(model_path, clean_up_tokenization_spaces=True)
tokenizer.tgt_lang=target_language_code

#invoke witchcraft
translated_list=[tokenizer.decode(tokenizer.convert_tokens_to_ids(token.hypotheses[0][1:])) for token in translator.translate_batch([tokenizer.convert_ids_to_tokens(tokenizer.encode(text)) for text in raw_list],target_prefix=[[tokenizer.lang_code_to_token[target_language_code]]]*len(raw_list))]

#output
for text in translated_list:
    print(text)
```