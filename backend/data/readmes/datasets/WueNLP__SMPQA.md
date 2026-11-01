---
license: apache-2.0
task_categories:
- visual-question-answering
language:
- en
- zu
- id
- it
- de
- th
- ar
- ko
- zh
- hi
- ru
tags:
- multilingual
- OCR
- Plot
size_categories:
- n<1K
---
# SMPQA (Synthetic Multilingual Plot QA)

<!-- Provide a quick summary of the dataset. -->

The SMPQA evaluation dataset proposed in [Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model](https://gregor-ge.github.io/Centurio/).

SMPQA is composed of synthetic bar plots and pie charts (generated using word lists of different languages) together with questions about those plots.
The datasets aims at providing an initial way of evaluating multilingual OCR capabilities of models in arbritrary languages.

There are two sub-tasks: 
1. *Grounding* text labels from the question to the image to answer yes/no questions ("Is the bar with label X the tallest?")
2. *Reading* labels from the plot based on the question ("What is the label of the red bar?")

For more details, check out our paper.

## Dataset Details

The data is structured as follows for every language (11 languages right now; found in `smpqa.zip`):

- `bar_annotations_$lang.json` and `pie_annotations_$lang.json` contain the questions and answers for all images.
  We provide unpacked examples for English for easy viewing.
  There are 8 *grounding* and 5 *reading* questions per plot. 
- Images `bar_plot_$i.png` and `pie_plot_$i.png` ranging from 0 to 49 (= 100 plots in total per language). We provide two unpacked English example images.


## Extending to New Languages

SMPQA is easy to expand to new languages.
We provide the code and the plot definitions (i.e., colors, size, etc.) used to generate the existing plots. 
This way, you can create plots and questions that are identical and thus comparable to the existing plots in new languages.

Currently, we use word lists from [this source](https://github.com/frekwencja/most-common-words-multilingual) but other sources can also work.


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
