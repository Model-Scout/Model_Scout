---
annotations_creators:
- expert-generated
- crowdsourced
language:
- af
- ar
- az
- be
- bg
- bn
- br
- bs
- ca
- ch
- cs
- cv
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
- fo
- fr
- fy
- ga
- gd
- gl
- gn
- he
- hi
- hr
- hu
- hy
- ia
- id
- ie
- io
- is
- it
- ja
- jv
- ka
- kk
- km
- ko
- ku
- kw
- la
- lb
- lt
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- nb
- nl
- nn
- 'no'
- oc
- pl
- pt
- qu
- rn
- ro
- ru
- sh
- sl
- sq
- sr
- sv
- sw
- ta
- te
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
- vo
- yi
- zh
- ace
- acm
- acq
- aeb
- af
- ajp
- ak
- als
- am
- apc
- ar
- ars
- ary
- arz
- as
- ast
- awa
- ayr
- azb
- azj
- ba
- bm
- ban
- be
- bem
- bn
- bho
- bjn
- bo
- bs
- bug
- bg
- ca
- ceb
- cs
- cjk
- ckb
- crh
- cy
- da
- de
- dik
- dyu
- dz
- el
- en
- eo
- et
- eu
- ee
- fo
- fj
- fi
- fon
- fr
- fur
- fuv
- gaz
- gd
- ga
- gl
- gn
- gu
- ht
- ha
- he
- hi
- hne
- hr
- hu
- hy
- ig
- ilo
- id
- is
- it
- jv
- ja
- kab
- kac
- kam
- kn
- ks
- ka
- kk
- kbp
- kea
- khk
- km
- ki
- rw
- ky
- kmb
- kmr
- knc
- kg
- ko
- lo
- lij
- li
- ln
- lt
- lmo
- ltg
- lb
- lua
- lg
- luo
- lus
- lvs
- mag
- mai
- ml
- mar
- min
- mk
- mt
- mni
- mos
- mi
- my
- nl
- nn
- nb
- npi
- nso
- nus
- ny
- oc
- ory
- pag
- pa
- pap
- pbt
- pes
- plt
- pl
- pt
- prs
- quy
- ro
- rn
- ru
- sg
- sa
- sat
- scn
- shn
- si
- sk
- sl
- sm
- sn
- sd
- so
- st
- es
- sc
- sr
- ss
- su
- sv
- swh
- szl
- ta
- taq
- tt
- te
- tg
- tl
- th
- ti
- tpi
- tn
- ts
- tk
- tum
- tr
- tw
- tzm
- ug
- uk
- umb
- ur
- uzn
- vec
- vi
- war
- wo
- xh
- ydd
- yo
- yue
- zh
- zsm
- zu
programming_language:
- Java
- Python
- Jupyter-Notebook
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: xP3x
size_categories:
- 100M<n<1B
task_categories:
- other
- translation
---

# Dataset Card for xP3x Kikongo Focus

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/bigscience-workshop/xmtf
- **Paper:** [Crosslingual Generalization through Multitask Finetuning](https://arxiv.org/abs/2211.01786)
- **Point of Contact:** [Niklas Muennighoff](mailto:n.muennighoff@gmail.com)

### Dataset Summary

> xP3x (Crosslingual Public Pool of Prompts eXtended) is a collection of prompts & datasets across 277 languages & 16 NLP tasks. It contains all of xP3 + much more! It is used for training future contenders of mT0 & BLOOMZ at project Aya @[C4AI](https://cohere.for.ai/) 🧡
> 
- **Creation:** The dataset can be recreated using instructions available [here](https://github.com/bigscience-workshop/xmtf#create-xp3) together with the file in this repository named `xp3x_create.py`. We provide this version to save processing time.
- **Languages:** 277
- **xP3 Dataset Family:**

<table>
  <tr>
<th>Name</th>
<th>Explanation</th>
<th>Example models</th>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/Muennighoff/xP3x>xP3x</a></t> 
<td>Mixture of 17 tasks in 277 languages with English prompts</td>
<td>WIP - Join us at Project Aya @<a href=https://cohere.for.ai/>C4AI</a> to help!</td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3>xP3</a></t> 
<td>Mixture of 13 training tasks in 46 languages with English prompts</td>
<td><a href=https://huggingface.co/bigscience/bloomz>bloomz</a> & <a href=https://huggingface.co/bigscience/mt0-xxl>mt0-xxl</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3mt>xP3mt</a></t> 
<td>Mixture of 13 training tasks in 46 languages with prompts in 20 languages (machine-translated from English)</td>
<td><a href=https://huggingface.co/bigscience/bloomz-mt>bloomz-mt</a> & <a href=https://huggingface.co/bigscience/mt0-xxl-mt>mt0-xxl-mt</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3all>xP3all</a></t> 
<td>xP3 + evaluation datasets adding an additional 3 tasks for a total of 16 tasks in 46 languages with English prompts</td>
<td></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/bigscience/xP3megds>xP3megds</a></t> 
<td><a href=https://github.com/bigscience-workshop/Megatron-DeepSpeed>Megatron-DeepSpeed</a> processed version of xP3</td>
<td><a href=https://huggingface.co/bigscience/bloomz>bloomz</a></td>
</tr>
<tr>
<td><a href=https://huggingface.co/datasets/Muennighoff/P3>P3</a></t> 
<td>Repreprocessed version of the English-only <a href=https://huggingface.co/datasets/bigscience/P3>P3</a> with 8 training tasks</td>
<td><a href=https://huggingface.co/bigscience/bloomz-p3>bloomz-p3</a> & <a href=https://huggingface.co/bigscience/mt0-xxl-p3>mt0-xxl-p3</a></td>
</tr>
</table>

## Dataset Structure


### Data Instances

An example looks as follows:

```json
{
  'inputs': '11月、遂にクロームはファイヤーフォックスを引き離し始めた。_はインターネットユーザーの評価が高まったのだ。\nReplace the _ in the above sentence with the correct option: \n- ファイヤーフォックス\n- クローム',
  'targets': 'クローム',
  'language': 'jpn_Jpan',
  'split': 'test',
  'template': 'Replace',
  'dataset': 'Muennighoff/xwinograd',
  'config': 'jp'
}
```

### Data Fields

The data fields are the same among all splits:
- `inputs`: the natural language input fed to the model
- `targets`: the natural language target that the model has to generate
- `language`: The language code. The codes are an extension of the FLORES-200 codes, where the first part is the language code and the second part the script code.
- `template`: The name of the prompt used.
- `dataset`: The Hugging Face dataset identifier of where the data stems from.
- `config`: The config of the Hugging Face dataset. 

### Usage

The dataset has 680 gigabytes and 530 million samples. You may want to filter it and then deduplicate depending on your needs.

Loading by language:

```python
# pip install -q datasets
from datasets import load_dataset
ds = load_dataset("Muennighoff/xP3x", "zho_Hans", streaming=True) # Use streaming to not download all at once
for x in ds["train"]:
    print(x)
    break
```

You can then filter down by the data fields to e.g. only get certain configs or datasets.
As every dataset-config-template is its own jsonl file, you can also decide on the datasets, configs and templates you want and only download them.
For example, to download all Japanese xwinograd samples, you could do:

```python
# pip install -q datasets
from datasets import load_dataset
import multiprocessing
# pip install --upgrade huggingface-hub
from huggingface_hub import HfFileSystem, hf_hub_url

fs = HfFileSystem()
fps = fs.glob(f"datasets/CohereForAI/xP3x/data/jpn_Jpan/*xwinograd*")
resolved_paths = [fs.resolve_path(file) for file in fps]
data_files = [hf_hub_url(resolved_path.repo_id, resolved_path.path_in_repo, repo_type=resolved_path.repo_type) for resolved_path in resolved_paths]

ds = load_dataset("json", data_files=data_files, num_proc=8)["train"]
```

Sometimes it may be faster to clone the entire repo. To download all English files, you could do e.g.
```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/CohereForAI/xP3x
cd xP3x
git lfs pull --include="data/eng_Latn/*"
```

### Data Splits

|Language|Code|Kilobytes|%|Samples|%|
|--------|------:|------:|-:|---:|-:|
|Kikongo|kon_Latn|648,992|0.1|1,223,481|0.23|

#### Language specifics

- `Japanese`: Data in `jpn_Hira`, `jpn_Kana`, `jpn_Hani` is guaranteed to have Hiragana, Katakana or Kanji, respectively in each sample. However, they may still include other styles. So while all samples in `jpn_Kana` are guaranteed to have Katakana, there may still be Hiragana or Kanji.

## Dataset Creation

### Source Data


#### Training datasets

- Code Miscellaneous
  - [CodeComplex](https://huggingface.co/datasets/codeparrot/codecomplex)
  - [Docstring Corpus](https://huggingface.co/datasets/teven/code_docstring_corpus)
  - [GreatCode](https://huggingface.co/datasets/great_code)
  - [State Changes](https://huggingface.co/datasets/Fraser/python-state-changes)
- Closed-book QA
  - [Hotpot QA](https://huggingface.co/datasets/hotpot_qa)
  - [Trivia QA](https://huggingface.co/datasets/trivia_qa)
  - [Web Questions](https://huggingface.co/datasets/web_questions)
  - [Wiki QA](https://huggingface.co/datasets/wiki_qa)  
- Extractive QA
  - [Adversarial QA](https://huggingface.co/datasets/adversarial_qa)
  - [CMRC2018](https://huggingface.co/datasets/cmrc2018)
  - [DRCD](https://huggingface.co/datasets/clue)
  - [DuoRC](https://huggingface.co/datasets/duorc)
  - [MLQA](https://huggingface.co/datasets/mlqa)      
  - [Quoref](https://huggingface.co/datasets/quoref)
  - [ReCoRD](https://huggingface.co/datasets/super_glue)  
  - [ROPES](https://huggingface.co/datasets/ropes)
  - [SQuAD v2](https://huggingface.co/datasets/squad_v2)
  - [xQuAD](https://huggingface.co/datasets/xquad)
  - TyDI QA
    - [Primary](https://huggingface.co/datasets/khalidalt/tydiqa-primary)
    - [Goldp](https://huggingface.co/datasets/khalidalt/tydiqa-goldp)
- Multiple-Choice QA
  - [ARC](https://huggingface.co/datasets/ai2_arc)
  - [C3](https://huggingface.co/datasets/c3)  
  - [CoS-E](https://huggingface.co/datasets/cos_e)
  - [Cosmos](https://huggingface.co/datasets/cosmos)
  - [DREAM](https://huggingface.co/datasets/dream)
  - [MultiRC](https://huggingface.co/datasets/super_glue)
  - [OpenBookQA](https://huggingface.co/datasets/openbookqa)
  - [PiQA](https://huggingface.co/datasets/piqa)  
  - [QUAIL](https://huggingface.co/datasets/quail)
  - [QuaRel](https://huggingface.co/datasets/quarel)
  - [QuaRTz](https://huggingface.co/datasets/quartz)
  - [QASC](https://huggingface.co/datasets/qasc)
  - [RACE](https://huggingface.co/datasets/race)
  - [SciQ](https://huggingface.co/datasets/sciq)    
  - [Social IQA](https://huggingface.co/datasets/social_i_qa)
  - [Wiki Hop](https://huggingface.co/datasets/wiki_hop)
  - [WiQA](https://huggingface.co/datasets/wiqa)  
- Paraphrase Identification
  - [MRPC](https://huggingface.co/datasets/super_glue)
  - [PAWS](https://huggingface.co/datasets/paws)
  - [PAWS-X](https://huggingface.co/datasets/paws-x)  
  - [QQP](https://huggingface.co/datasets/qqp)  
- Program Synthesis
  - [APPS](https://huggingface.co/datasets/codeparrot/apps)
  - [CodeContests](https://huggingface.co/datasets/teven/code_contests)
  - [JupyterCodePairs](https://huggingface.co/datasets/codeparrot/github-jupyter-text-code-pairs)
  - [MBPP](https://huggingface.co/datasets/Muennighoff/mbpp)
  - [NeuralCodeSearch](https://huggingface.co/datasets/neural_code_search)
  - [XLCoST](https://huggingface.co/datasets/codeparrot/xlcost-text-to-code)  
- Structure-to-text
  - [Common Gen](https://huggingface.co/datasets/common_gen)
  - [Wiki Bio](https://huggingface.co/datasets/wiki_bio)
- Sentiment
  - [Amazon](https://huggingface.co/datasets/amazon_polarity)
  - [App Reviews](https://huggingface.co/datasets/app_reviews)
  - [IMDB](https://huggingface.co/datasets/imdb)
  - [Rotten Tomatoes](https://huggingface.co/datasets/rotten_tomatoes)
  - [Yelp](https://huggingface.co/datasets/yelp_review_full)
- Simplification
  - [BiSECT](https://huggingface.co/datasets/GEM/BiSECT)
- Summarization
  - [CNN Daily Mail](https://huggingface.co/datasets/cnn_dailymail)
  - [Gigaword](https://huggingface.co/datasets/gigaword)
  - [MultiNews](https://huggingface.co/datasets/multi_news)
  - [SamSum](https://huggingface.co/datasets/samsum)
  - [Wiki-Lingua](https://huggingface.co/datasets/GEM/wiki_lingua)
  - [XLSum](https://huggingface.co/datasets/GEM/xlsum)
  - [XSum](https://huggingface.co/datasets/xsum)
- Topic Classification
  - [AG News](https://huggingface.co/datasets/ag_news)
  - [DBPedia](https://huggingface.co/datasets/dbpedia_14)
  - [TNEWS](https://huggingface.co/datasets/clue)  
  - [TREC](https://huggingface.co/datasets/trec)
  - [CSL](https://huggingface.co/datasets/clue) 
- Translation
  - [Flores-200](https://huggingface.co/datasets/Muennighoff/flores200)
  - [Tatoeba](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt)
  - [MultiEURLEX](https://huggingface.co/datasets/multi_eurlex)
- Word Sense disambiguation
  - [WiC](https://huggingface.co/datasets/super_glue)
  - [XL-WiC](https://huggingface.co/datasets/pasinit/xlwic)
- Natural Language Inference (NLI)
  - [ANLI](https://huggingface.co/datasets/anli)
  - [CB](https://huggingface.co/datasets/super_glue)
  - [RTE](https://huggingface.co/datasets/super_glue)
  - [XNLI](https://huggingface.co/datasets/xnli)
- Coreference Resolution
  - [Winogrande](https://huggingface.co/datasets/winogrande)
  - [XWinograd](https://huggingface.co/datasets/Muennighoff/xwinograd)
- Sentence Completion
  - [COPA](https://huggingface.co/datasets/super_glue)
  - [Story Cloze](https://huggingface.co/datasets/story_cloze)
  - [XCOPA](https://huggingface.co/datasets/xcopa)  
  - [XStoryCloze](https://huggingface.co/datasets/Muennighoff/xstory_cloze)

#### Dataset specifics

- Flores-200: There are three prompts for Flores: `continuation`, `question`, `command`, which represent three commonly used prompting styles, i.e. making a prompt seem like a natural continuation, turning it into a question or commanding the model to do something.
- tatoeba_mt: Contains duplicates. For example, it has data that is both classified as `jpn_Kana` and `jpn_Jpan`, so you may want to deduplicate.

## Additional Information

### Licensing Information

The dataset collection is released under Apache 2.0. Note that individual datasets may have different licenses.

### Citation Information

```bibtex
@article{muennighoff2022crosslingual,
  title={Crosslingual generalization through multitask finetuning},
  author={Muennighoff, Niklas and Wang, Thomas and Sutawika, Lintang and Roberts, Adam and Biderman, Stella and Scao, Teven Le and Bari, M Saiful and Shen, Sheng and Yong, Zheng-Xin and Schoelkopf, Hailey and others},
  journal={arXiv preprint arXiv:2211.01786},
  year={2022}
}
```

### Contributions

Thanks to the contributors of [promptsource](https://github.com/bigscience-workshop/promptsource/graphs/contributors) for adding many prompts used in this dataset.
Thanks to the Aya team @[C4AI](https://cohere.for.ai/) 🧡