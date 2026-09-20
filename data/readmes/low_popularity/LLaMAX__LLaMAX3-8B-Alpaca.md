---
tags:
- Multilingual
license: mit
language:
- af
- am
- ar
- hy
- as
- ast
- az
- be
- bn
- bs
- bg
- my
- ca
- ceb
- zho
- hr
- cs
- da
- nl
- en
- et
- tl
- fi
- fr
- ff
- gl
- lg
- ka
- de
- el
- gu
- ha
- he
- hi
- hu
- is
- ig
- id
- ga
- it
- ja
- jv
- kea
- kam
- kn
- kk
- km
- ko
- ky
- lo
- lv
- ln
- lt
- luo
- lb
- mk
- ms
- ml
- mt
- mi
- mr
- mn
- ne
- ns
- no
- ny
- oc
- or
- om
- ps
- fa
- pl
- pt
- pa
- ro
- ru
- sr
- sn
- sd
- sk
- sl
- so
- ku
- es
- sw
- sv
- tg
- ta
- te
- th
- tr
- uk
- umb
- ur
- uz
- vi
- cy
- wo
- xh
- yo
- zu
---
### Model Sources

- **Paper**: LLaMAX: Scaling Linguistic Horizons of LLM by Enhancing Translation Capabilities Beyond 100 Languages
- **Link**: https://arxiv.org/pdf/2407.05975
- **Repository**: https://github.com/CONE-MT/LLaMAX/
- **Demo**: https://huggingface.co/spaces/vilarin/LLaMAX3-Translator Thanks for the efforts from @AnnioDance. 

### Model Description

LLaMAX is a language model with powerful multilingual capabilities without loss instruction-following capabilities. 

We collected extensive training sets in 102 languages for continued pre-training of Llama2 and leveraged the English instruction fine-tuning dataset, Alpaca, to fine-tune its instruction-following capabilities.

### 🔥 Effortless Multilingual Translation with a Simple Prompt

LLaMAX supports translation between more than 100 languages, surpassing the performance of similarly scaled LLMs.

```angular2html
def Prompt_template(query, src_language, trg_language):
    instruction = f'Translate the following sentences from {src_language} to {trg_language}.'
    prompt = (
        'Below is an instruction that describes a task, paired with an input that provides further context. '
        'Write a response that appropriately completes the request.\n'
        f'### Instruction:\n{instruction}\n'
        f'### Input:\n{query}\n### Response:'
    )
    return prompt
```

And then run the following codes to execute translation:
```angular2html
from transformers import AutoTokenizer, LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained(PATH_TO_CONVERTED_WEIGHTS)
tokenizer = AutoTokenizer.from_pretrained(PATH_TO_CONVERTED_TOKENIZER)

query = "你好，今天是个好日子"
prompt = Prompt_template(query, 'Chinese', 'English')
inputs = tokenizer(prompt, return_tensors="pt")

generate_ids = model.generate(inputs.input_ids, max_length=30)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
# => "Hello, today is a good day"
```


### 🔥 Excellent Translation Performance

LLaMAX3-8B-Alpaca achieves an average spBLEU score improvement of over **5 points** compared to the LLaMA3-8B-Alpaca model on the Flores-101 dataset.


| System             | Size | en-X (COMET)       | en-X (BLEU) | zh-X (COMET)| zh-X (BLEU) | de-X (COMET) | de-X (BLEU) | ne-X (COMET) | ne-X (BLEU) |ar-X (COMET) | ar-X (BLEU) | az-X (COMET) | az-X (BLEU) | ceb-X (COMET) | ceb-X (BLEU)|
|--------------------|------|--------------------|-------------| ----| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| LLaMA3-8B-Alpaca      | 8B   |67.97|17.23|64.65|10.14|64.67|13.62|62.95|7.96|63.45|11.27|60.61|6.98|55.26|8.52|
| LLaMAX3-8B-Alpaca | 8B   |75.52|22.77|73.16|14.43|73.47|18.95|75.13|15.32|72.29|16.42|72.06|12.41|68.88|15.85|


| System             | Size | X-en (COMET) | X-en (BLEU) | X-zh (COMET)| X-zh (BLEU) | X-de (COMET) | X-de (BLEU) | X-ne (COMET) | X-ne (BLEU) |X-ar (COMET) | X-ar (BLEU) | X-az (COMET) | X-az (BLEU) | X-ceb (COMET) | X-ceb (BLEU) |
|--------------------|------|----------------|-------------| ----| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |--------------| 
| LLaMA3-8B-Alpaca      | 8B   |77.43|26.55|73.56|13.17|71.59|16.82|46.56|3.83|66.49|10.20|58.30|4.81|52.68|4.18|
| LLaMAX3-8B-Alpaca | 8B   |81.28|31.85|78.34|16.46|76.23|20.64|65.83|14.16|75.84|15.45|70.61|9.32|63.35|12.66|


### Supported Languages
Akrikaans (af), Amharic (am), Arabic (ar), Armenian (hy), Assamese (as), Asturian (ast), Azerbaijani (az), Belarusian (be), Bengali (bn), Bosnian (bs), Bulgarian (bg), Burmese (my), Catalan (ca), Cebuano (ceb), Chinese Simpl (zho), Chinese Trad (zho), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Estonian (et), Filipino (tl), Finnish (fi), French (fr), Fulah (ff), Galician (gl), Ganda (lg), Georgian (ka), German (de), Greek (el), Gujarati (gu), Hausa (ha), Hebrew (he), Hindi (hi), Hungarian (hu), Icelandic (is), Igbo (ig), Indonesian (id), Irish (ga), Italian (it), Japanese (ja), Javanese (jv), Kabuverdianu (kea), Kamba (kam), Kannada (kn), Kazakh (kk), Khmer (km), Korean (ko), Kyrgyz (ky), Lao (lo), Latvian (lv), Lingala (ln), Lithuanian (lt), Luo (luo), Luxembourgish (lb), Macedonian (mk), Malay (ms), Malayalam (ml), Maltese (mt), Maori (mi), Marathi (mr), Mongolian (mn), Nepali (ne), Northern Sotho (ns), Norwegian (no), Nyanja (ny), Occitan (oc), Oriya (or), Oromo (om), Pashto (ps), Persian (fa), Polish (pl), Portuguese (pt), Punjabi (pa), Romanian (ro), Russian (ru), Serbian (sr), Shona (sn), Sindhi (sd), Slovak (sk), Slovenian (sl), Somali (so), Sorani Kurdish (ku), Spanish (es), Swahili (sw), Swedish (sv), Tajik (tg), Tamil (ta), Telugu (te), Thai (th), Turkish (tr), Ukrainian (uk), Umbundu (umb), Urdu (ur), Uzbek (uz), Vietnamese (vi), Welsh (cy), Wolof (wo), Xhosa (xh), Yoruba (yo), Zulu (zu)

### Model Index
We implement multiple versions of the LLaMAX model, the model links are as follows:

| Model   | LLaMAX                                               | LLaMAX-Alpaca                                               |
|---------|----------------------------------------------------------|-----------------------------------------------------------------|
| Llama-2 | [Link](https://huggingface.co/LLaMAX/LLaMAX2-7B) | [Link](https://huggingface.co/LLaMAX/LLaMAX2-7B-Alpaca) |
| Llama-3 | [Link](https://huggingface.co/LLaMAX/LLaMAX3-8B-8B) | [Link](https://huggingface.co/LLaMAX/LLaMAX3-8B-8B-Alpaca) |

### Citation
If our model helps your work, please cite this paper:

```
@inproceedings{lu-etal-2024-llamax,
    title = "{LL}a{MAX}: Scaling Linguistic Horizons of {LLM} by Enhancing Translation Capabilities Beyond 100 Languages",
    author = "Lu, Yinquan  and
      Zhu, Wenhao  and
      Li, Lei  and
      Qiao, Yu  and
      Yuan, Fei",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.631",
    doi = "10.18653/v1/2024.findings-emnlp.631",
    pages = "10748--10772",
    abstract = "Large Language Models (LLMs) demonstrate remarkable translation capabilities in high-resource language tasks, yet their performance in low-resource languages is hindered by insufficient multilingual data during pre-training. To address this, we conduct extensive multilingual continual pre-training on the LLaMA series models, enabling translation support across more than 100 languages. Through a comprehensive analysis of training strategies, such as vocabulary expansion and data augmentation, we develop LLaMAX. Remarkably, without sacrificing its generalization ability, LLaMAX achieves significantly higher translation performance compared to existing open-source LLMs (by more than 10 spBLEU points) and performs on-par with specialized translation model (M2M-100-12B) on the Flores-101 benchmark. Extensive experiments indicate that LLaMAX can serve as a robust multilingual foundation model. The code and the models are publicly available.",
}
```