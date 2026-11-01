---
base_model:
- Qwen/Qwen3-0.6B-Base
datasets:
- NiuTrans/LMT-60-sft-data
language:
- en
- zh
- ar
- es
- de
- fr
- it
- ja
- nl
- pl
- pt
- ru
- tr
- bg
- bn
- cs
- da
- el
- fa
- fi
- hi
- hu
- id
- ko
- nb
- ro
- sk
- sv
- th
- uk
- vi
- am
- az
- bo
- he
- hr
- hy
- is
- jv
- ka
- kk
- km
- ky
- lo
- mvf
- mr
- ms
- my
- ne
- ps
- si
- sw
- ta
- te
- tg
- tl
- ug
- ur
- uz
- yue
license: apache-2.0
metrics:
- bleu
- comet
pipeline_tag: translation
library_name: transformers
---

## LMT
- Paper: [NiuTrans.LMT: Toward Inclusive and Scalable Multilingual Machine Translation with LLMs](https://arxiv.org/abs/2511.07003)
- Github: [LMT](https://github.com/NiuTrans/LMT)

**LMT-60** is a suite of **Chinese-English-centric** Multilingual Machine Translation (MMT) models trained on **90B tokens** mixed monolingual and bilingual tokens, covering **60 languages across 234 translation directions** and achieving **SOTA performance** among models with similar language coverage.
 We release both the CPT and GRPO versions of LMT-60 in four sizes (0.6B/1.7B/4B/8B). All checkpoints are available:
| Models | Model Link |
|:------------|:------------|
| LMT-60-0.6B-Base | [NiuTrans/LMT-60-0.6B-Base](https://huggingface.co/NiuTrans/LMT-60-0.6B-Base) |
| LMT-60-0.6B | [NiuTrans/LMT-60-0.6B](https://huggingface.co/NiuTrans/LMT-60-0.6B) |
| LMT-60-1.7B-Base | [NiuTrans/LMT-60-1.7B-Base](https://huggingface.co/NiuTrans/LMT-60-1.7B-Base) |
| LMT-60-1.7B | [NiuTrans/LMT-60-1.7B](https://huggingface.co/NiuTrans/LMT-60-1.7B) |
| LMT-60-4B-Base | [NiuTrans/LMT-60-4B-Base](https://huggingface.co/NiuTrans/LMT-60-4B-Base) |
| LMT-60-4B | [NiuTrans/LMT-60-4B](https://huggingface.co/NiuTrans/LMT-60-4B) |
| LMT-60-8B-Base | [NiuTrans/LMT-60-8B-Base](https://huggingface.co/NiuTrans/LMT-60-8B-Base) |
| LMT-60-8B | [NiuTrans/LMT-60-8B](https://huggingface.co/NiuTrans/LMT-60-8B) |

Our supervised fine-tuning (SFT) data are released at [NiuTrans/LMT-60-sft-data](https://huggingface.co/datasets/NiuTrans/LMT-60-sft-data)

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "NiuTrans/LMT-60-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side='left')
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """Translate the following text from English into Chinese:
English: The concept came from China where plum blossoms were the flower of choice.
Chinese:"""
messages = [{"role": "user", "content": prompt}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(**model_inputs, max_new_tokens=512, num_beams=5, do_sample=False)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

outputs = tokenizer.decode(output_ids, skip_special_tokens=True)

print("response:", outputs)
```

## Support Languages

| Resource Tier | Languages |
| :---- | :---- |
| High-resource Languages (13) | Arabic(ar), English(en), Spanish(es), German(de), French(fr), Italian(it), Japanese(ja), Dutch(nl), Polish(pl), Portuguese(pt), Russian(ru), Turkish(tr), Chinese(zh) |
| Medium-resource Languages (18) | Bulgarian(bg), Bengali(bn), Czech(cs), Danish(da), Modern Greek(el), Persian(fa), Finnish(fi), Hindi(hi), Hungarian(hu), Indonesian(id), Korean(ko), Norwegian Bokmål(nb), Romanian(ro), Slovak(sk), Swedish(sv), Thai(th), Ukrainian(uk), Vietnamese(vi) |
| Low-resouce Languages (29) | Amharic(am), Azerbaijani(az), Tibetan(bo), Modern Hebrew(he), Croatian(hr), Armenian(hy), Icelandic(is), Javanese(jv), Georgian(ka), Kazakh(kk), Central Khmer(km), Kirghiz(ky), Lao(lo), Inner Mongolian(mvf), Marathi(mr), Malay(ms), Burmese(my), Nepali(ne), Pashto(ps), Sinhala(si), Swahili(sw), Tamil(ta), Telugu(te), Tajik(tg), Tagalog(tl), Uighur(ug), Urdu(ur), Uzbek(uz), Yue Chinese(yue) |

## Citation

If you find our paper useful for your research, please kindly cite our paper:
```bash
@misc{luoyf2025lmt,
      title={NiuTrans.LMT: Toward Inclusive and Scalable Multilingual Machine Translation with LLMs}, 
      author={Yingfeng Luo, Ziqiang Xu, Yuxuan Ouyang, Murun Yang, Dingyang Lin, Kaiyan Chang, Tong Zheng, Bei Li, Peinan Feng, Quan Du, Tong Xiao, Jingbo Zhu},
      year={2025},
      eprint={2511.07003},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.07003}, 
}
```