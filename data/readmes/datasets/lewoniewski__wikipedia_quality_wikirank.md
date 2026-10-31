---
license: apache-2.0
language:
- ar
- az
- be
- bg
- ca
- cs
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
- gl
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- ka
- kk
- ko
- la
- lt
- ms
- nl
- nn
- no
- pl
- pt
- ro
- ru
- sh
- sk
- sl
- sr
- sv
- ta
- th
- tr
- uk
- ur
- uz
- vi
- vo
- zh
tags:
- wikipedia
- quality
- wikirank
size_categories:
- 10M<n<100M
configs:
- config_name: default
  data_files:
  - split: wikirank_20240801
    path: "wikirank_20240801.csv"
---

Datasets with WikiRank quality score as of 1 August 2024 for 47 million Wikipedia articles in 55 language versions (also simplified version for each language in [separate files](https://huggingface.co/datasets/lewoniewski/wikipedia_quality_wikirank/tree/main/languages)).

The [WikiRank](https://wikirank.net) quality score is a metric designed to assess the overall quality of a Wikipedia article. Although its specific algorithm can vary depending on the implementation, the score typically combines several key features of the Wikipedia article.

### Why It’s Important

- **Enhances Trust:** For readers and researchers, the quality score serves as a quick reference to judge the reliability of an article.
- **Guides Editors:** Contributors can identify which articles might need further development or additional sources.
- **Improves Content Discovery:** Search engines or internal recommendation systems can use the score to prioritize high-quality, well-sourced content.

### How You Can Use It

- **As a Reader:** Check the WikiRank score to determine whether you’re accessing an article that meets high standards of reliability and depth.
- **As an Editor:** Use the score as a diagnostic tool to pinpoint articles that require updates, improved references, or structural changes.
- **For Research and Development:** Incorporate the score into algorithms for content curation or to analyze trends in content quality across large collaborative platforms.

In summary, the WikiRank quality score offers both users and editors a clear, quantitative measure to enhance the credibility and usability of Wikipedia content, fostering a higher standard of information across the platform.


More information about the quality score can be found in scientific papers:
- [Multilingual Ranking of Wikipedia Articles with Quality and Popularity Assessment in Different Topics](https://doi.org/10.3390/computers8030060)
- [Quality and Importance of Wikipedia Articles in Different Languages](https://link.springer.com/chapter/10.1007/978-3-319-46254-7_50)
- [Relative Quality and Popularity Evaluation of Multilingual Wikipedia Articles](https://doi.org/10.3390/informatics4040043)
- [Modelling the quality of attributes in Wikipedia infoboxes](https://link.springer.com/chapter/10.1007/978-3-319-26762-3_27)
