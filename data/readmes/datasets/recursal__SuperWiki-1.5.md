---
annotations_creators:
  - no-annotation
language_creators:
  - crowdsourced
license:
  - cc-by-sa-3.0
task_categories:
  - text-generation
  - fill-mask
task_ids:
  - language-modeling
  - masked-language-modeling
source_datasets:
  - original
language:
- ar
- de
- en
- es
- fa
- fr
- he
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- tr
- uk
- vi
- zh
pretty_name: SuperWIKI v1.5
---


## Dataset Details

![](SuperWikipedia-15.png "Based off from Wikipe-tan (Maid, cyan hair, short hair) and Wikipedia's globe logo.")

*Waifu to catch your attention.*

### Dataset Description

*SuperWIKI-1.5* is a **~18.23B** Tokens (llama-2-7b-chat-tokenizer) / **~15.17B** Tokens (RWKV Tokenizer) multilingual dataset of Wikipedia articles, curated from Wikipedia HTML dumps. 
It serves as a training resource for large language models and other NLP tasks. 
This card details the dataset's origin, content, and limitations.

- **Curated by:** KaraKaraWitch
- **Funded by:** Recursal.ai (I work there lol)
- **Shared by:** KaraKaraWitch
- **Language(s) (NLP):** Multiple (see Supported Languages)
- **License:** cc-by-sa-4.0

SuperWIKI-1.5 was created under time constraints for the release of [EagleX v1](https://huggingface.co/recursal/EagleX_1-7T_HF), and may contain biases in selection.  

**We highly recommend using the improved version, *SuperWikipedia-NEXT* instead.**

### Dataset Summary

Wikipedia dataset containing cleaned articles of all languages.
The dataset is manually built from Wikipedia HTML dumps with each split for each language. 
Each example contains the content of one full Wikipedia article.

### Supported Tasks and Leaderboards

Primarily used for language modeling

### Languages

The dataset includes Wikipedia articles from the following languages:

```
ar.wikipedia.org
de.wikipedia.org
en.wikipedia.org
es.wikipedia.org
fa.wikipedia.org
fr.wikipedia.org
he.wikipedia.org
hi.wikipedia.org
id.wikipedia.org
it.wikipedia.org
ja.wikipedia.org
ko.wikipedia.org
nl.wikipedia.org
pl.wikipedia.org
pt.wikipedia.org
ru.wikipedia.org
simple.wikipedia.org
sv.wikipedia.org
tr.wikipedia.org
uk.wikipedia.org
vi.wikipedia.org
zh.wikipedia.org
```

*`.wikipedia.org`* extensions have been added for your convenience.


### Selection Bias

Unlike SuperWikipedia-NEXT, the language selection in SuperWIKI-1.5 was manual and may favor certain languages (e.g., CJK and European languages).

### Filtering

The filtering process is documented in code but not well-organized. We recommend reviewing the code directly for details.

### Data Instances

Refer to this sample to see all the fields:

```json
{
    "id": 4024053,
    "title": "Tharman Shanmugaratnam",
    "url": "https://en.wikipedia.org/wiki/Tharman_Shanmugaratnam",
    "stub": false,
    "template": [
        "Efn",
        "C-SPAN",
        "S-aft",
        "S-new",
        "Reflist",
        "Cite news",
        "S-par",
        "Cite journal",
        "Short description",
        "EngvarB"
    ],
    "category": [
        "Finance ministers of Singapore",
        "Singaporean Hindus",
        "Alumni of Wolfson College, Cambridge",
        "Deputy Prime Ministers of Singapore",
        "Ministers for Manpower of Singapore",
        "Presidents of Singapore",
        "Singaporean people of Sri Lankan descent",
        "Singaporean people of Tamil descent",
        "Articles with WorldCat Entities identifiers",
        "Articles with GND identifiers",
        "Articles with VIAF identifiers",
    ],
    "license": [
        "Creative Commons Attribution Share Alike 3.0 Unported"
    ],
    "wikitext": "<...TRUNCATED SAMPLE...> '''Tharman Shanmugaratnam'''{{efn|{{lang-ta|தர்மன் சண்முகரத்தினம்}}}} (born 25 February 1957), also known [[mononymously]] as '''Tharman''', is a Singaporean politician and economist who has been serving as the ninth [[president of Singapore]] since 2023 after winning the [[2023 Singaporean presidential election|2023 presidential election]].\n\nPrior to his presidency, Tharman served as [[Senior Minister of Singapore]] between 2019 and 2023, [[Coordinating Minister for Social Policies (Singapore)|Coordinating Minister for Social Policies]] between 2015 and 2023, and Chairman of the [[Monetary Authority of Singapore]] between 2011 and 2023.<ref name=\"Parliament Profile\"/> \n\nTharman is an economist in roles principally related to economic and social policies. He has also led various international councils and panels simultaneously. Tharman chairs the Board of Trustees of the [[Group of Thirty]], a global council of economic and financial leaders from the public and private sectors and academia. He also co-chairs the Global Commission on the Economics of Water with [[Ngozi Okonjo-Iweala|Ngozi Owonjo-Iweala]], [[Mariana Mazzucato]] and [[Johan Rockström]]. Its initial recommendations helped shape the outcomes of the UN Water Conference in March 2023. Tharman has also been co-chair of the [[G20]] High Level Independent Panel on Global Financing for Pandemic Preparedness and Response since 2021. In 2017, Tharman was appointed to chair the G20 Eminent Persons Group on Global Financial Governance.\n\nA former member of the governing [[People's Action Party]] (PAP), he was the... <...TRUNCATED SAMPLE...>",
    "lang": "en",
    "abstract": "Tharman Shanmugaratnam, also known mononymously as Tharman, is a Singaporean politician and economist who has been serving as the ninth president of Singapore since 2023. Prior to his presidency, Tharman served as Senior Minister of Singapore between 2019 and 2023, Coordinating Minister for Social Policies between 2015 and 2023, and Chairman of the Monetary Authority of Singapore between 2011 and 2023. Tharman is an economist in roles principally related to economic and social policies. He has also led various international councils and panels simultaneously. Tharman chairs the Board of Trustees of the Group of Thirty, a global council of economic and financial leaders from the public and private sectors and academia. He also co-chairs the Global Commission on the Economics of Water with Ngozi Owonjo-Iweala, Mariana Mazzucato and Johan Rockström. Its initial recommendations helped shape the outcomes of the UN Water Conference in March 2023. Tharman has also been co-chair of the G20 High Level Independent Panel on Global Financing for Pandemic Preparedness and Response since 2021. In 2017, Tharman was appointed to chair the G20 Eminent Persons Group on Global Financial Governance. <...TRUNCATED SAMPLE...>",
    "boxes_filters": [],
    "infobox_html": [
        "<...TRUNCATED SAMPLE...>"
    ],
    "figures_dict": [
        {
            "file_url": "./File:Mr_Tharman_at_Bloomberg_New_Economy_Forum.jpg",
            "caption": ""
        }
    ],
    "text": "9th President of Singapore\n\n\n**Tharman Shanmugaratnam** (born 25 February 1957), also known mononymously as **Tharman**, is a Singaporean politician and economist who has been serving as the ninth president of Singapore since 2023. Prior to his presidency, Tharman served as Senior Minister of Singapore between 2019 and 2023, Coordinating Minister for Social Policies between 2015 and 2023, and Chairman of the Monetary Authority of Singapore between 2011 and 2023.\n\nTharman is an economist in roles principally related to economic and social policies. He has also led various international councils and panels simultaneously. <...TRUNCATED SAMPLE...>"
}
```

### Data Fields

`id`: The article ID in question
`title`: The title of the Wikipedia article.  
`url`: The URL of the article.  
`stub`: A boolean (true/false) flag marked as a stub from the CSS selector `.metadata.plainlinks`.
`template`: A list of templates found in the article.
`text`: The HTML Text (After post-processing) from SuperWIKI converted to Markdown with links removed and formatting (Bold, italics) kept.  
`license`: The license for the article.  
`wikitext`: The wikitext. Not used but can be used as a reference.  
`lang`: The language. Should be the same as wiki. (For `simplewiki` it should be `en`)  
`boxes_filters`: Also known as `rituals` found in the original SuperWIKI. These are extracted from the CSS selectors `.ombox` and `.ambox`.  
`infobox_html`: A list of side infoboxes that are extracted out from the text.  
`figures_dict`: A list of figures used in the article. Again, extracted out from the text.  
`text`: The Markdown text. This is what you should probably use or need for LLM training.

## Recursal's Vision

> To make AI accessible to everyone, regardless of language, or economical status

This is the collective goal of the `RWKV Open Source foundation` and `Recursal AI`, the commercial entity who backs it.

We believe that AI should not be controlled by a select few individual organization. And that it should be made accessible regardless if you are rich or poor, or a native speaker of english.

### About RWKV

RWKV is an Open Source, non profit group, under the linux foundation. Focused on developing the RWKV AI architecture, in accordence to our vision.

The RWKV architecture scales efficiently and economically. As an RNN & Transformer hybrid, it is able to provide the performance similar to leading transformer models, while having the compute and energy efficiency of an RNN based architecture.

You can find out more about the project, and latest models, at the following

- [https://blog.rwkv.com](https://blog.rwkv.com)
- [https://wiki.rwkv.com](https://wiki.rwkv.com)


### About Recursal AI

Recursal AI, is the commercial entity built to provide support for RWKV model development and users, while providing commercial services via its public cloud, or private-cloud / on-premise offerings.

As part of our vision. Our commitment, is to ensure open source development and access to the best foundational AI models and datasets. 

The following dataset/models provided here, is part of that commitment.

You can find out more about recursal AI here

- [https://recursal.ai](https://recursal.ai)
- [https://blog.recursal.ai](https://blog.recursal.ai)

### Dataset Curators

KaraKaraWitch. (I typically hang out in PygmalionAI discord, sometimes EleutherAI. If something is wrong, `@karakarawitch` on discord.)

I'd be happy if you could spread the word and recommend this dataset over wikitext for your use cases `:)`

### Licensing Information

Most of Wikipedia's text and many of its images are co-licensed under the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License)
(CC BY-SA) and the [GNU Free Documentation License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License)
(GFDL) (un-versioned, with no invariant sections, front-cover texts, or back-cover texts). 

Some text has been imported only under CC BY-SA and CC BY-SA-compatible license and cannot be reused under GFDL; such
text will be identified on the page footer, in the page history, or on the discussion page of the article that utilizes
the text.

Recursal Waifus (The banner image) are licensed under CC-BY-SA. 
They do not represent the related websites in any official capacity unless otherwise or announced by the website. 
You may use them as a banner image. However, you must always link back to the dataset.

### Citation Information

```
@misc{superwiki,
  title         = {SuperWIKI-1.5},
  author        = {KaraKaraWitch, recursal.ai},
  year          = {2024},
  howpublished  = {\url{https://huggingface.co/datasets/recursal/SuperWiki-1.5}},
}
```