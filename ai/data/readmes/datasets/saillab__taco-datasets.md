---
language:
- en
- ne
- sn
- mai
- fa
- hi
- af
- sq
- am
- ar
- hy
- as
- ay
- az
- bm
- eu
- be
- bn
- bh
- bs
- bg
- ca
- ceb
- ny
- zh
- co
- hr
- cs
- da
- dv
- dog
- nl
- eo
- et
- ee
- tl
- fi
- fr
- fy
- gl
- ka
- de
- el
- gn
- gu
- ht
- ha
- haw
- he
- hmn
- hu
- is
- ig
- ilo
- id
- ga
- it
- ja
- jv
- kn
- kk
- km
- rw
- kok
- ko
- kri
- ku
- ky
- lo
- la
- lv
- ln
- lt
- lg
- lb
- mk
- ml
- mt
- mi
- mr
- mni
- ms
- mg
- mt
- my
- 'no'
- or
- om
- ps
- pl
- pt
- pa
- ro
- ru
- sm
- gd
- sr
- st
- tn
- sd
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tg
- ta
- tt
- te
- th
- ti
- to
- tr
- tk
- tw
- uk
- ur
- ug
- uz
- vi
- cy
- xh
- yi
- yo
- zu
pretty_name: t
size_categories:
- 100K<n<1M
---
This repo consists of the datasets used for the TaCo paper. There are four datasets:

* Multilingual Alpaca-52K GPT-4 dataset
* Multilingual Dolly-15K GPT-4 dataset
* TaCo dataset
* Multilingual Vicuna Benchmark dataset

We translated the first three datasets using Google Cloud Translation.

The TaCo dataset is created by using the TaCo approach as described in our paper, combining the Alpaca-52K and Dolly-15K datasets.

If you would like to create the TaCo dataset for a specific language, you can simply follow the method as mentioned in the paper and use the above translated datasets. 

Link to the Paper: [Arxiv](https://arxiv.org/abs/2311.10797)

```
{
"instruction": "instruction in xx",
"input": "input in xx",
"output": "Instruction in English: instruction in en , 
            Response in English: response in en ,
            Response in xx: response in xx "
}
```

**Model Weights**
We have released all of our model adapters in the HuggingFace. 
* [Taco Nepali-33B 🌮](https://huggingface.co/saillab/taco-nepali-33b)
* [Taco Sanskrit-33B 🌮](https://huggingface.co/saillab/taco-sanskrit-33b)
* [Taco Maithili-33B 🌮](https://huggingface.co/saillab/taco-maithili-33b)
* [Taco Persian-33B 🌮](https://huggingface.co/saillab/taco-persian-33b)

**Citation**
```
@article{upadhayay2023taco,
  title={TaCo: Enhancing Cross-Lingual Transfer for Low-Resource Languages in LLMs through Translation-Assisted Chain-of-Thought Processes},
  author={Upadhayay, Bibek and Behzadan, Vahid},
  journal={arXiv preprint arXiv:2311.10797},
  year={2023}
}
```

**Copyright and Intended Use**
This dataset has been released under CC BY-NC, intended for academic and research purposes only. Please review the licenses and terms and conditions of Alpaca-52K, Dolly-15K, and Google Cloud Translation before using this dataset for any purpose other than research.