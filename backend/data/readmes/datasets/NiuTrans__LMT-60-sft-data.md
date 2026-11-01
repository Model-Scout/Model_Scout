---
task_categories:
- translation
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
---

# LMT-60-sft-data: Large-scale Multilingual Translation SFT Dataset

This repository contains the `LMT-60-sft-data` dataset, a key component of the research presented in the paper "[NiuTrans.LMT: Toward Inclusive and Scalable Multilingual Machine Translation with LLMs](https://huggingface.co/papers/2511.07003)".

The LMT (Large-scale Multilingual Translation) project aims to advance Multilingual Machine Translation (MMT) by building inclusive, scalable, and high-performance multilingual translation models. This supervised fine-tuning (SFT) dataset was instrumental in developing these models, which are centered on both Chinese and English, covering 60 languages and 234 translation directions.

**Paper:** [NiuTrans.LMT: Toward Inclusive and Scalable Multilingual Machine Translation with LLMs](https://huggingface.co/papers/2511.07003)

**Code:** [https://github.com/NiuTrans/LMT](https://github.com/NiuTrans/LMT)

## Dataset Composition

The `LMT-60-sft-data` dataset comprises a diverse collection of translation data, including:
- Flores-200 devset
- NTREX-128
- SMol
- WMT14–23 test sets
- IWSLT17–24 test sets

In total, it contains 567K samples, providing a rich resource for multilingual machine translation research.

## Supported Languages

The LMT project and its associated datasets support 60 languages, categorized by their resource tier:

| Resource Tier | Languages |
| :---- | :---- |
| High-resource Languages (13) | Arabic(ar), English(en), Spanish(es), German(de), French(fr), Italian(it), Japanese(ja), Dutch(nl), Polish(pl), Portuguese(pt), Russian(ru), Turkish(tr), Chinese(zh) |
| Medium-resource Languages (18) | Bulgarian(bg), Bengali(bn), Czech(cs), Danish(da), Modern Greek(el), Persian(fa), Finnish(fi), Hindi(hi), Hungarian(hu), Indonesian(id), Korean(ko), Norwegian Bokmål(nb), Romanian(ro), Slovak(sk), Swedish(sv), Thai(th), Ukrainian(uk), Vietnamese(vi) |
| Low-resouce Languages (29) | Amharic(am), Azerbaijani(az), Tibetan(bo), Modern Hebrew(he), Croatian(hr), Armenian(hy), Icelandic(is), Javanese(jv), Georgian(ka), Kazakh(kk), Central Khmer(km), Kirghiz(ky), Lao(lo), Inner Mongolian(mvf), Marathi(mr), Malay(ms), Burmese(my), Nepali(ne), Pashto(ps), Sinhala(si), Swahili(sw), Tamil(ta), Telugu(te), Tajik(tg), Tagalog(tl), Uighur(ug), Urdu(ur), Uzbek(uz), Yue Chinese(yue) |


## Citation

If you find this dataset or the associated paper useful for your research, please kindly cite:

```bibtex
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