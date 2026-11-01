---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: SuperWikiNEXT-32B
paperswithcode_id: null
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
multilinguality:
- multilingual
language:
- af
- ar
- ast
- az
- be
- bg
- bn
- ca
- ce
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
- lv
- mk
- ms
- my
- nl
- nn
- 'no'
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
- tg
- th
- tr
- uk
- ur
- uz
- vi
- zh
size_categories:
- 10B<n<100B
---

# Dataset Card for SuperWikiNEXT-32B

![](Waifu.png "Based off from Wikipe-tan (Maid, cyan hair, short hair) and Wikipedia's globe logo.")

*Waifu to catch your attention.*

## Dataset Details

### Dataset Description

*SuperWikipedia-NEXT* is an enhanced version of the SuperWIKI dataset. Which SuperWIKI was born out of the thought of a better filtered Wikipedia while retaining markdowns. 
*SuperWikipedia-NEXT* contains **~32.44B** Tokens (llama-2-7b-chat-tokenizer) / **~27.92B** Tokens (RWKV Tokenizer) from approximately **60** "High quality" / "Selected" languages.

- **Curated by:** KaraKaraWitch
- **Funded by:** Recursal.ai (I work there lol)
- **Shared by:** KaraKaraWitch
- **Language(s) (NLP):** Many. Refer to the data below for a list of languages.
- **License:** cc-by-sa-4.0, 

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Source Data:** [https://dumps.wikimedia.org/other/enterprise_html/](https://dumps.wikimedia.org/other/enterprise_html)

### Dataset Summary

Wikipedia dataset containing cleaned articles of all languages.
The dataset is manually built from Wikipedia HTML dumps with each split for each language. 
Each example contains the content of one full Wikipedia article.

### Supported Tasks and Leaderboards

The dataset is generally used for Language Modelling.

### Languages

We have selected the following Wikipedia's:

```
af.wikipedia.org
ar.wikipedia.org
ast.wikipedia.org
az.wikipedia.org
be.wikipedia.org
bg.wikipedia.org
bn.wikipedia.org
ca.wikipedia.org
ce.wikipedia.org
cs.wikipedia.org
cy.wikipedia.org
da.wikipedia.org
de.wikipedia.org
el.wikipedia.org
en.wikipedia.org
eo.wikipedia.org
es.wikipedia.org
et.wikipedia.org
eu.wikipedia.org
fa.wikipedia.org
fi.wikipedia.org
fr.wikipedia.org
gl.wikipedia.org
he.wikipedia.org
hi.wikipedia.org
hr.wikipedia.org
hu.wikipedia.org
hy.wikipedia.org
id.wikipedia.org
it.wikipedia.org
ja.wikipedia.org
ka.wikipedia.org
kk.wikipedia.org
ko.wikipedia.org
la.wikipedia.org
lt.wikipedia.org
lv.wikipedia.org
min.wikipedia.org
mk.wikipedia.org
ms.wikipedia.org
my.wikipedia.org
nl.wikipedia.org
nn.wikipedia.org
no.wikipedia.org
pl.wikipedia.org
pt.wikipedia.org
ro.wikipedia.org
ru.wikipedia.org
sh.wikipedia.org
simple.wikipedia.org
sk.wikipedia.org
sl.wikipedia.org
sr.wikipedia.org
sv.wikipedia.org
ta.wikipedia.org
tg.wikipedia.org
th.wikipedia.org
tr.wikipedia.org
uk.wikipedia.org
ur.wikipedia.org
uz.wikipedia.org
vi.wikipedia.org
zh-min-nan.wikipedia.org
zh.wikipedia.org
zh-yue.wikipedia.org
```

*`.wikipedia.org`* extensions have been added for your convenience.

### Selection of Wikipedia

We deem a particular Wikipedia language as high quality if:

1. Has a total article count of `>100,000`.
2. Has a `Depth > 5.1`.

*Depth is calculated using the following equation:*

`depth = (article_edits / total_pages) * ((total_pages - articles) / articles) ** 2`

This formula is directly taken from [list of Wikipedias.](https://meta.wikimedia.org/wiki/Wikipedia_article_depth)

### Filtering

Extensive HTML and markdown filtering has been done to derive the final dataset.

For HTML:

1. Parse the article content with BeautifulSoup.
2. We first extract out titles from the Soup. 
3. Drop (As in, don't process / skip processing) *Stub articles.* To ensure multilanguage coverage, we use a list of stub names found across multiple languages using wikidata. (We have included the template names within `wikipedia_template.py`)
4. Drop *Lsjbot* bot created articles.
5. Collapse styles with `data-mw` component into its next sibling.
6. Remove raw `href` links. (Text of href == href link)
7. Remove citation needed Templates
8. Remove citation Templates
9. Remove Redirect Templates
10. Drop articles where the article content consists of 50% or more of tables and lists.
11. Remove message boxes. (Orange alert boxes on top of articles)
12. Remove infoboxes boxes. (Infoboxes on the right)
13. Selectively remove tables which consist of just empty spaces. (Number of `<td>` elements > len(text_size) and text_size < 50)
14. Cleanup latex code.
15. Empty `class` attributes and `data-mw` attributes

For Markdown:

1. Cleanup punctuations.
2. Collect text length (normalized text to NKFC, keeping CJK characters as is while decomposing Arabic characters, Counting double width characters as 2 instead of 1, )
3. Filter based on the collected text length (If the article is less than 1000 characters long, it is dropped.)

The final Markdown text and additional data is included in the jsonl file. Additionally, the scripts used are located in the main directory of this folder as well.

### Data keys

Users can run `less` to see the contents. A sample and a list of dictionary keys have been provided below:

```json
{
    "text": "\n**Tharman Shanmugaratnam** PBM (born 25 February 1957) is a Singaporean politician and economist. He is the President of Singapore since 2023. \n\nHe was Senior Minister of Singapore between 2019 and 2023. He was also the Coordinating Minister for Social Policies between 2015 and 2023, and Chairman of the Monetary Authority of Singapore between 2011 and 2023.\n\nOn 8 June 2023, Tharman announced his plans to run for president in the 2023 presidential election. He was elected on 2 September 2023 in a landslide victory, winning 70.40% of the vote.\n\nEarly life and education\n------------------------\n\nTharman was born in the Colony of Singapore in 1957. He studied at the Anglo-Chinese School. When he was studying there, he was not interested in his studies and was not disciplined. However, he liked to read and tried out poetry. During his time at Anglo-Chinese School, he created four poets with his schoolmates. Also, he was interested in sports and spent most of his time playing sports. He even joined his school's hockey team.\n\nThen, he attended the London School of Economics (LSE), graduating with a Bachelor of Science degree in economics.\n\nAfter getting his bachelor's, Tharman went on to study at Wolfson College at the University of Cambridge. There, he completed a Master of Philosophy degree in economics. \n\nTharman then became a student at the Harvard Kennedy School at Harvard University, where he finished a Master in Public Administration (MPA) degree. He was a student activist there. He explored left-wing politics, as he did not agree with the ruling People's Action Party back in Singapore.\n\nTharman was a recipient of the Lucius N. Littauer Fellows Award. The award is given to students with MPA's who showed academic excellence and leadership.In 2011, the LSE gave him an Honorary Fellowship.<...TRUNCATED IN SAMPLE>",
    "meta": {
        "title": "Tharman Shanmugaratnam",
        "mostly_tablelist": false,
        "tablelist_ratio": [
            4082,
            8644,
            0.47223507635354
        ],
        "infobox": [
            "<...TRUNCATED IN SAMPLE>"
        ],
        "td_tables": [],
        "text_length": 5553
    }
}
```

```
text: str (Markdown text)
meta: dict (Contains additional metadata / meta)
  - title: str (Article Title)
  - mostly_tablelist: bool (Internal flag for HTML step 10)
  - tablelist_ratio: list (Internal data, used to compute mostly_tablelist.)
  - infobox: list (A list of extracted infoboxes with data-mw attribute for the raw html data.)
  - td_tables: list (Extracted tables from HTML step 13)
  - text_length: int (Obtained from markdown step 2)
```

### Dataset Curators

KaraKaraWitch. (I typically hangout in PygmalionAI discord, sometimes EleutherAI. If something is wrong, `@karakarawitch` on discord.)

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
@ONLINE{superwiki-next,
  title         = {SuperWikiNEXT-32B},
  author        = {KaraKaraWitch, recursal.ai},
  year          = {2024},
  howpublished  = {\url{https://huggingface.co/datasets/recursal/SuperWikipedia-NEXT}},
}
```