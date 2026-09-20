---
license: mit
datasets:
- oscar-corpus/OSCAR-2301
- allenai/nllb
- Helsinki-NLP/opus-100
language:
- en
- da
- nl
- de
- is
- 'no'
- sc
- af
- ca
- ro
- gl
- it
- pt
- es
- bg
- mk
- sr
- uk
- ru
- id
- ms
- th
- vi
- mg
- fr
- hu
- el
- cs
- pl
- lt
- lv
- ka
- zh
- ja
- ko
- fi
- et
- gu
- hi
- mr
- ne
- ur
- az
- kk
- ky
- tr
- uz
- ar
- he
- fa
base_model:
- haoranxu/ALMA-13B-Pretrain
---


[X-ALMA](https://arxiv.org/pdf/2410.03115) builds upon [ALMA-R](https://arxiv.org/pdf/2401.08417) by expanding support from 6 to 50 languages. It utilizes a plug-and-play architecture with language-specific modules, complemented by a carefully designed training recipe. This release includes the **X-ALMA pre-trained base model**.
```
@misc{xu2024xalmaplugplay,
      title={X-ALMA: Plug & Play Modules and Adaptive Rejection for Quality Translation at Scale}, 
      author={Haoran Xu and Kenton Murray and Philipp Koehn and Hieu Hoang and Akiko Eriguchi and Huda Khayrallah},
      year={2024},
      eprint={2410.03115},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.03115}, 
}
```
X-ALMA-13B-Pretrain is pre-trained on 50 languages: en,da,nl,de,is,no,sv,af,ca,ro,gl,it,pt,es,bg,mk,sr,uk,ru,id,ms,th,vi,mg,fr,hu,el,cs,pl,lt,lv,ka,zh,ja,ko,fi,et,gu,hi,mr,ne,ur,az,kk,ky,tr,uz,ar,he,fa.

All X-ALMA checkpoints are released at huggingface:
| Models | Model Link | Description |
|:-------------:|:---------------:|:---------------:|
| X-ALMA | [haoranxu/X-ALMA](https://huggingface.co/haoranxu/X-ALMA)) | X-ALMA model with all its modules |
| X-ALMA-13B-Pretrain | [haoranxu/X-ALMA-13B-Pretrain](https://huggingface.co/haoranxu/X-ALMA-13B-Pretrain) | X-ALMA 13B multilingual pre-trained base model |
| X-ALMA-Group1 | [haoranxu/X-ALMA-13B-Group1](https://huggingface.co/haoranxu/X-ALMA-13B-Group1) | X-ALMA group1 specific module and the merged model |
| X-ALMA-Group2 | [haoranxu/X-ALMA-13B-Group2](https://huggingface.co/haoranxu/X-ALMA-13B-Group2) | X-ALMA group2 specific module and the merged model |
| X-ALMA-Group3 | [haoranxu/X-ALMA-13B-Group3](https://huggingface.co/haoranxu/X-ALMA-13B-Group3) | X-ALMA group3 specific module and the merged model |
| X-ALMA-Group4 | [haoranxu/X-ALMA-13B-Group4](https://huggingface.co/haoranxu/X-ALMA-13B-Group4) | X-ALMA group4 specific module and the merged model |
| X-ALMA-Group5 | [haoranxu/X-ALMA-13B-Group5](https://huggingface.co/haoranxu/X-ALMA-13B-Group5) | X-ALMA group5 specific module and the merged model |
| X-ALMA-Group6 | [haoranxu/X-ALMA-13B-Group6](https://huggingface.co/haoranxu/X-ALMA-13B-Group6) | X-ALMA group6 specific module and the merged model |
| X-ALMA-Group7 | [haoranxu/X-ALMA-13B-Group7](https://huggingface.co/haoranxu/X-ALMA-13B-Group7) | X-ALMA group7 specific module and the merged model |
| X-ALMA-Group8 | [haoranxu/X-ALMA-13B-Group8](https://huggingface.co/haoranxu/X-ALMA-13B-Group8) | X-ALMA group8 specific module and the merged model |

## A quick start:
There are three ways to load X-ALMA for translation. An example of translating "我爱机器翻译。" into English (X-ALMA should also able to do multilingual open-ended QA).

**The first way**: loading the merged model where the language-specific module has been merged into the base model **(Recommended)**:
```
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
from peft import PeftModel

GROUP2LANG = {
1: ["da", "nl", "de", "is", "no", "sv", "af"],
2: ["ca", "ro", "gl", "it", "pt", "es"],
3: ["bg", "mk", "sr", "uk", "ru"],
4: ["id", "ms", "th", "vi", "mg", "fr"],
5: ["hu", "el", "cs", "pl", "lt", "lv"],
6: ["ka", "zh", "ja", "ko", "fi", "et"],
7: ["gu", "hi", "mr", "ne", "ur"],
8: ["az", "kk", "ky", "tr", "uz", "ar", "he", "fa"],
}
LANG2GROUP = {lang: str(group) for group, langs in GROUP2LANG.items() for lang in langs}
group_id = LANG2GROUP["zh"]

model = AutoModelForCausalLM.from_pretrained(f"haoranxu/X-ALMA-13B-Group{group_id}", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(f"haoranxu/X-ALMA-13B-Group{group_id}", padding_side='left')

# Add the source sentence into the prompt template
prompt="Translate this from Chinese to English:\nChinese: 我爱机器翻译。\nEnglish:"

# X-ALMA needs chat template but ALMA and ALMA-R don't need it.
chat_style_prompt = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(chat_style_prompt, tokenize=False, add_generation_prompt=True)

input_ids = tokenizer(prompt, return_tensors="pt", padding=True, max_length=40, truncation=True).input_ids.cuda()

# Translation
with torch.no_grad():
generated_ids = model.generate(input_ids=input_ids, num_beams=5, max_new_tokens=20, do_sample=True, temperature=0.6, top_p=0.9)
outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(outputs)
```

**The second way**: loading the base model and language-specific module **(Recommended)**:
```
model = AutoModelForCausalLM.from_pretrained("haoranxu/X-ALMA-13B-Pretrain", torch_dtype=torch.float16, device_map="auto")
model = PeftModel.from_pretrained(model, f"haoranxu/X-ALMA-13B-Group{group_id}")
tokenizer = AutoTokenizer.from_pretrained(f"haoranxu/X-ALMA-13B-Group{group_id}", padding_side='left')
```

**The third way**: loading the base model with all language-specific modules like MoE: (Require large GPU memory)
```
from modeling_xalma import XALMAForCausalLM
model = XALMAForCausalLM.from_pretrained("haoranxu/X-ALMA", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("haoranxu/X-ALMA", padding_side='left')

# Add `lang="zh"`: specify the language to instruct the model on which group to use for the third loading method during generation.
generated_ids = model.generate(input_ids=input_ids, num_beams=5, max_new_tokens=20, do_sample=True, temperature=0.6, top_p=0.9, lang="zh")
```