---
license: apache-2.0
size_categories:
- 100K<n<1M
tags:
- mt-evaluation
- WMT
- quality-estimation
- automated-metrics
- machine-translation
language:
- bn
- cs
- de
- en
- es
- fi
- fr
- gu
- ha
- he
- hi
- hr
- is
- iu
- ja
- kk
- liv
- lt
- pl
- ps
- ru
- sah
- uk
- xh
- zh
- zu
- sr
- ar
- bho
- cs
- de
- et
- it
- ko
- mas
pretty_name: WMT Human Evaluation
---


This dataset is continuously updated and contains a compilation of human translation quality assessment from past WMT campaigns.
Specifically, this dataset merges all annotation protocols (DA, MQM, ESA) on a semi-unified scale (0 to 100).
The current version of the dataset includes human scores up to WMT 2025 (inclusive) and has been created with the following script:
```python
import subset2evaluate # version 1.0.20
import json
import statistics

data = subset2evaluate.utils.load_data_wmt_all(min_items=10, include_ref=True)

# flatten
data = [
    {
        "src": line["src"],
        "mt": line["tgt"][sys],
        "score": line["scores"][sys]["human"],
        "dataset": "/".join(data_name),
    }
    for data_name, data_v in data.items()
    for line in data_v
    for sys in line["scores"].keys()
]

# only one split, filter by "dataset" keyword if you want to
with open("train.jsonl", "w") as f:
    for line in data:
        f.write(json.dumps(line) + "\n")


# plot score distribution
import matplotlib.pyplot as plt
plt.hist([x["score"] for x in data], density=True, bins=30, color="black")
plt.gca().spines[["top", "right"]].set_visible(False)
plt.ylabel("Frequency")
plt.xlabel("Score")
plt.show()

print(len(data)) # 769328 up to WMT2025
print(sorted({x for line in data for x in line["dataset"].split("/")[1].split("-")}))
```

<!-- huggingface-cli upload --repo-type dataset zouharvi/wmt-human-all . . -->

You can use the dataset as:
```python
import datasets
datasets.load_dataset("zouharvi/wmt-human-all", split="train") 
```

<img src="https://cdn-uploads.huggingface.co/production/uploads/6304ece07424d937fa35fb98/lKaq2c9glgRtdLR4trFY7.png" width="400px">

If you use this dataset, cite the [latest WMT findings paper](https://aclanthology.org/2025.wmt-1.22/):
```bibtex
@inproceedings{kocmi-etal-2025-findings,
    title = "Findings of the {WMT}25 General Machine Translation Shared Task: Time to Stop Evaluating on Easy Test Sets",
    author = "Kocmi, Tom  and
      Artemova, Ekaterina  and
      Avramidis, Eleftherios  and
      Bawden, Rachel  and
      Bojar, Ond{\v{r}}ej  and
      Dranch, Konstantin  and
      Dvorkovich, Anton  and
      Dukanov, Sergey  and
      Fishel, Mark  and
      Freitag, Markus  and
      Gowda, Thamme  and
      Grundkiewicz, Roman  and
      Haddow, Barry  and
      Karpinska, Marzena  and
      Koehn, Philipp  and
      Lakougna, Howard  and
      Lundin, Jessica  and
      Monz, Christof  and
      Murray, Kenton  and
      Nagata, Masaaki  and
      Perrella, Stefano  and
      Proietti, Lorenzo  and
      Popel, Martin  and
      Popovi{\'c}, Maja  and
      Riley, Parker  and
      Shmatova, Mariya  and
      Steingr{\'i}msson, Steinth{\'o}r  and
      Yankovskaya, Lisa  and
      Zouhar, Vil{\'e}m",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.22/",
    doi = "10.18653/v1/2025.wmt-1.22",
    pages = "355--413",
    ISBN = "979-8-89176-341-8",
    abstract = "This paper presents the results of the General Machine Translation Task organized as part of the 2025 Conference on Machine Translation (WMT). Participants were invited to build systems for any of 30 language pairs. For half of these pairs, we conducted a human evaluation on test sets spanning four to five different domains.We evaluated 60 systems in total: 36 submitted by participants and 24 for which we collected translations from large language models (LLMs) and popular online translation providers.This year, we focused on creating challenging test sets by developing a difficulty sampling technique and using more complex source data. We evaluated system outputs with professional annotators using the Error Span Annotation (ESA) protocol, except for two language pairs, for which we used Multidimensional Quality Metrics (MQM) instead.We continued the trend of increasingly moving towards document-level translation, providing the source texts as whole documents containing multiple paragraphs."
}

@inproceedings{kocmi-etal-2024-findings,
    title = "Findings of the {WMT}24 General Machine Translation Shared Task: The {LLM} Era Is Here but {MT} Is Not Solved Yet",
    author = "Kocmi, Tom  and
      Avramidis, Eleftherios  and
      Bawden, Rachel  and
      Bojar, Ond{\v{r}}ej  and
      Dvorkovich, Anton  and
      Federmann, Christian  and
      Fishel, Mark  and
      Freitag, Markus  and
      Gowda, Thamme  and
      Grundkiewicz, Roman  and
      Haddow, Barry  and
      Karpinska, Marzena  and
      Koehn, Philipp  and
      Marie, Benjamin  and
      Monz, Christof  and
      Murray, Kenton  and
      Nagata, Masaaki  and
      Popel, Martin  and
      Popovi{\'c}, Maja  and
      Shmatova, Mariya  and
      Steingr{\'i}msson, Steinth{\'o}r  and
      Zouhar, Vil{\'e}m",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.wmt-1.1/",
    doi = "10.18653/v1/2024.wmt-1.1",
    pages = "1--46",
    abstract = "This overview paper presents the results of the General Machine Translation Task organised as part of the 2024 Conference on Machine Translation (WMT). In the general MT task, participants were asked to build machine translation systems for any of 11 language pairs, to be evaluated on test sets consisting of three to five different domains. In addition to participating systems, we collected translations from 8 different large language models (LLMs) and 4 online translation providers. We evaluate system outputs with professional human annotators using a new protocol called Error Span Annotations (ESA)."
}
```