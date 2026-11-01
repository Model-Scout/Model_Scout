---
license: apache-2.0
language:
- multilingual
- af
- am
- ar
- as
- azb
- be
- bg
- bm
- bn
- bo
- bs
- ca
- ceb
- cs
- cy
- da
- de
- du
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- ga
- gd
- gl
- ha
- hi
- hr
- ht
- hu
- id
- ig
- is
- it
- iw
- ja
- jv
- ka
- ki
- kk
- km
- ko
- la
- lb
- ln
- lo
- lt
- lv
- mi
- mr
- ms
- mt
- my
- 'no'
- oc
- pa
- pl
- pt
- qu
- ro
- ru
- sa
- sc
- sd
- sg
- sk
- sl
- sm
- so
- sq
- sr
- ss
- sv
- sw
- ta
- te
- th
- ti
- tl
- tn
- tpi
- tr
- ts
- tw
- uk
- ur
- uz
- vi
- war
- wo
- xh
- yo
- zh
- zu
task_categories:
- image-to-text
tags:
- ocr
size_categories:
- 1M<n<10M
---
# Synthdog Multilingual

<!-- Provide a quick summary of the dataset. -->

The Synthdog dataset created for training in [Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model](https://gregor-ge.github.io/Centurio/).

Using the [official Synthdog code](https://github.com/clovaai/donut/tree/master/synthdog), we created >1 million training samples for improving OCR capabilities in Large Vision-Language Models.

## Dataset Details

We provide the images for download in two `.tar.gz` files. Download and extract them in folders of the same name (so `cat images.tar.gz.* | tar xvzf -C images; tar xvzf images.tar.gz -C images_non_latin`).
The image path in the dataset expects images to be in those respective folders for unique identification.


Every language has the following amount of samples: 500,000 for English, 10,000 for non-Latin scripts, and 5,000 otherwise.

Text is taken from Wikipedia of the respective languages. Font is `GoNotoKurrent-Regular`.


> Note: Right-to-left written scripts (Arabic, Hebrew, ...) are unfortunatly writte correctly right-to-left but also bottom-to-top. We were not able to fix this issue. However, empirical results in Centurio suggest that this data is still helpful for improving model performance.
> 



## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@article{centurio2025,
  author       = {Gregor Geigle and
                  Florian Schneider and
                  Carolin Holtermann and
                  Chris Biemann and
                  Radu Timofte and
                  Anne Lauscher and
                  Goran Glava\v{s}},
  title        = {Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model},
  journal      = {arXiv},
  volume       = {abs/2501.05122},
  year         = {2025},
  url          = {https://arxiv.org/abs/2501.05122},
  eprinttype    = {arXiv},
  eprint       = {2501.05122},
}
```