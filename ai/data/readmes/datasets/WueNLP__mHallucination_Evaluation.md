---
license: cc
language:
- ar
- de
- zh
- tr
- ru
- eu
- fr
- ca
- fi
- it
- ms
- ro
- pt
- ur
- hi
- he
- pl
- sd
- sr
- la
- es
- vi
- eo
- cs
- ko
- ja
task_categories:
- text-generation
size_categories:
- 10K<n<100K
---

# Multilingual Hallucination Evaluation ***in the wild*** 

The dataset was as part of the paper: [How Much Do LLMs Hallucinate across Languages? On Multilingual Estimation of LLM Hallucination in the Wild](https://arxiv.org/abs/2502.12769)

Below is the figure summarizing the multilingual hallucination evaluation dataset creation (and [multilingual hallucination detection](https://huggingface.co/datasets/WueNLP/mHallucination_Detection) dataset):

![Pipeline](estimation_pipeline.drawio.png)

## Dataset Details

The dataset is a high quality synthetic query/prompt and wikipedia reference pair for estimating hallucinations ***in the wild*** in 30 languages.

**Languages**

```
 'arabic', 'basque', 'cantonese', 'catalan', 'chinese',
 'czech', 'esperanto', 'french', 'finnish', 'german',
 'hebrew', 'hindi', 'hungarian', 'indonesian', 'italian',
 'japanese', 'korean', 'latin', 'lithuanian', 'malay',
 'polish', 'portuguese', 'romanian', 'russian',  'spanish',
 'serbian', 'sindhi', 'turkish', 'urdu', 'vietnamese'
```

| Language    | Unique Categories | Total Articles | Total Queries |
|-------------|-------------------|----------------|---------------|
| Arabic      | 537               | 959            | 1907          |
| Basque      | 486               | 938            | 1872          |
| Cantonese   | 261               | 401            | 793           |
| Catalan     | 359               | 989            | 1976          |
| Chinese     | 712               | 977            | 1939          |
| Czech       | 720               | 988            | 1975          |
| Esperanto   | 608               | 956            | 1912          |
| French      | 332               | 987            | 1973          |
| Finnish     | 549               | 995            | 1972          |
| German      | 797               | 984            | 1967          |
| Hebrew      | 660               | 999            | 1991          |
| Hindi       | 153               | 186            | 367           |
| Hungarian   | 745               | 992            | 1964          |
| Indonesian  | 457               | 958            | 1913          |
| Italian     | 678               | 988            | 1974          |
| Japanese    | 667               | 999            | 1991          |
| Korean      | 539               | 747            | 1488          |
| Latin       | 334               | 465            | 916           |
| Lithuanian  | 711               | 946            | 1888          |
| Malay       | 442               | 778            | 1556          |
| Polish      | 889               | 1000           | 1998          |
| Portuguese  | 390               | 955            | 1909          |
| Romanian    | 351               | 811            | 1618          |
| Russian     | 462               | 999            | 1996          |
| Spanish     | 938               | 977            | 1952          |
| Serbian     | 386               | 798            | 1587          |
| Sindhi      | 224               | 519            | 1029          |
| Turkish     | 660               | 856            | 1650          |
| Urdu        | 567               | 878            | 1749          |
| Vietnamese  | 326               | 660            | 1311          |
| **Total**   | **15,940**        | **25,685**     | **51,133**   |



For further details on the dataset: 

1. Refer to the paper on [archive](https://arxiv.org/abs/2502.12769).
2. Refer to the project [github](https://github.com/WorldHellow/mHallucinations-LLM).



## Uses

The dataset should only be used to evaluate LLMs. 


## Dataset Structure

The dataset contains the following columns: 

1. `Category`: associate wikipedia category
2. `Article Title`: wikipedia article title
3. `URL`: URL link for the wikipedia article
4. `reference_1`: wikipedia article content
5. `reference_2`: wikipedia article content
7. `reference_3`: wikipedia article content
8. `reference_4`: wikipedia article content
9. `reference_5`: wikipedia article content
10. `query_1`: first prompt whose answer is in the references
11. `query_2`: second prompt 
12. `language`: language of the article



## Limitations

The prompts are synthetically created. Manual analysis was done for 5 languages `German, Arabic, Turkish, Russian, Chinese` on 50 samples 
each where the answer to the prompt existed 98% of the time.  




#### Personal and Sensitive Information

Dataset does not contains any sensitive information nor pose any risks.



## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@misc{islam2025llmshallucinatelanguagesmultilingual,
        title={How Much Do LLMs Hallucinate across Languages? On Multilingual Estimation of LLM Hallucination in the Wild}, 
        author={Saad Obaid ul Islam and Anne Lauscher and Goran Glavaš},
        year={2025},
        eprint={2502.12769},
        archivePrefix={arXiv},
        primaryClass={cs.CL},
        url={https://arxiv.org/abs/2502.12769}, 
  }
```