---
license: apache-2.0
datasets:
- aiana94/polynews-parallel
- aiana94/polynews
language:
- af
- am
- ar
- as
- az
- be
- bg
- bn
- bo
- bs
- ca
- ceb
- co
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- haw
- he
- hi
- hmn
- hr
- ht
- hu
- hy
- id
- ig
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mi
- mk
- mn
- mr
- ms
- mt
- my
- ne
- nl
- 'no'
- ny
- or
- pa
- pl
- pt
- ro
- ru
- rw
- si
- sk
- sl
- sm
- sn
- so
- sw
- sq
- sr
- st
- sv
- ta
- te
- tg
- th
- tk
- tl
- tr
- tt
- ug
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
- ay
- bm
- bbj
- ee
- fon
- guw
- ln
- lg
- luo
- pcm
- rn
- tet
- ti
- tn
- tw
- fil
- mos
- orm
pipeline_tag: sentence-similarity
tags:
- bert
- feature-extraction
- sentence-embedding
- sentence-similarity
- multilingual
---
# NaSE (News-adapted Sentence Encoder)

This model is a news-adapted sentence encoder, domain-specialized starting from the pretrained massively mulitlingual sentence encoder [LaBSE](https://aclanthology.org/2022.acl-long.62.pdf).

## Model Details

### Model Description

NaSE is a domain-adapted multilingual sentence encoder, initialized from [LaBSE](https://www.kaggle.com/models/google/labse/tensorFlow2/labse/1?tfhub-redirect=true). 
It was specialized to the news domain using two multilingual corpora, namely [Polynews](https://huggingface.co/datasets/aiana94/polynews) and [PolyNewsParallel](https://huggingface.co/datasets/aiana94/polynews-parallel).
More specifically, NaSE was pretrained with two objectives: denoising auto-encoding and sequence-to-sequence machine translation.

## Usage (HuggingFace Transformers)

Here is how to use this model to get the sentence embeddings of a given text in PyTorch:

```python
    from transformers import BertModel, BertTokenizerFast

    tokenizer = BertTokenizerFast.from_pretrained('aiana94/NaSE')
    model = BertModel.from_pretrained('aiana94/NaSE')

    # pepare input
    sentences = ["This is an example sentence", "Dies ist auch ein Beispielsatz in einer anderen Sprache."]
    encoded_input = tokenizer(sentences, return_tensors='pt', padding=True)

    # forward pass
    with torch.no_grad():
        output = model(**encoded_input)

    # to get the sentence embeddings, use the pooler output
    sentence_embeddings = output.pooler_output
```

and in Tensorflow:

```python
    from transformers import TFBertModel, BertTokenizerFast

    tokenizer = BertTokenizerFast.from_pretrained('aiana94/NaSE')
    model = TFBertModell.from_pretrained('aiana94/NaSE')

    # pepare input
    sentences = ["This is an example sentence", "Dies ist auch ein Beispielsatz in einer anderen Sprache."]
    encoded_input = tokenizer(sentences, return_tensors='tf', padding=True)

    # forward pass
    with torch.no_grad():
        output = model(**encoded_input)

    # to get the sentence embeddings, use the pooler output
    sentence_embeddings = output.pooler_output
```

For similarity between sentences, an L2-norm is recommended before calculating the similarity:

```python
  import torch
  import torch.nn.functional as F

  def cos_sim(a: torch.Tensor, b: torch.Tensor):
    a_norm = F.normalize(a, p=2, dim=1)
    b_norm = F.normalize(b, p=2, dim=1)

    return torch.mm(a_norm, b_norm.transpose(0, 1))
```

### Intended Uses

Our model is intended to be used as a sentence, and in particular, news encoder. Given an input text, it outputs a vector which captures its semantic information.
The sentence vector may be used for sentence similarity, information retrieval or clustering tasks.


## Training Details

### Training Data

NaSE was domain-adapted using two multilingual datasets: [Polynews](https://huggingface.co/datasets/aiana94/polynews) 
and the parallel [PolyNewsParallel](https://huggingface.co/datasets/aiana94/polynews-parallel).

We use the following procedure to smoothen the per-language distribution when sampling for model training:
  
  * We sample only languages and language-pairs that contain at least 100 texts in PolyNews and PolyNewsParallel, respectively;
  * We sample texts from language _L_ by sampling from the modified distribution _p(L) ~ |L| * alpha_, where _|L|_ is the number of examples and _L_. We use a smooting rate _alpha=0.3_ (i.e., we upsample low-resource languages and downsample high-resource languages). 

### Training Procedure

We initialize NaSE with the pretrained weights of the mulitlingual sentenece encoder [LaBSE](https://huggingface.co/sentence-transformers/LaBSE).
Please refer to its [model card](https://www.kaggle.com/models/google/labse/tensorFlow2/labse/1?tfhub-redirect=true) or the corresponding [paper](https://aclanthology.org/2022.acl-long.62.pdf)
for more detaled information about the pre-training procedure.

We adapt the multilingual sentence encoder to the news domain using two objectives:

  * Denoising auto-encoding (DAE): reconstructs the original input sentence from its corrupted version obtained by adding discrete noise (see [TSDAE](https://aclanthology.org/2021.findings-emnlp.59.pdf) for details);
  * Machine translation (MT): generates the taget-language translation from the source-language input sentence (i.e., the source language constitutes the _corruption_ of the target sentence x in the target language, which is to be _reconstructed_).

NaSE is trained sequentially, first on reconstruction, and then on translation, i.e., we continue training the NaSE encoder obtained with the DAE objective for translation on parallel data.


#### Training Hyperparameters

- **Training regime:** fp16 mixed precision
- **Training steps:** 100k (50K per objective), validating every 5K steps
- **Learning rate:** 3e-5
- **Optimizer:** AdamW

The full training scripts is accessible in the [training code](https://github.com/andreeaiana/nase).


## Technical Specifications 

The model was pretrained on 1 40GB NVIDIA A100 GPU for a total of 100k steps. 


## Citation 

**BibTeX:**

```bibtex
@misc{iana2024news,
      title={News Without Borders: Domain Adaptation of Multilingual Sentence Embeddings for Cross-lingual News Recommendation}, 
      author={Andreea Iana and Fabian David Schmidt and Goran Glavaš and Heiko Paulheim},
      year={2024},
      eprint={2406.12634},
      archivePrefix={arXiv},
      url={https://arxiv.org/abs/2406.12634}
}
```