---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: SuperWikiImages-7M
task_categories:
- image-classification
- image-to-text
- text-to-image
- image-to-image
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
configs:
- config_name: default
  data_files:
  - split: train
    path:
     - "chunk_00/*.tar"
     - "chunk_01/*.tar"
     - "chunk_02/*.tar"
     - "chunk_03/*.tar"
---

# Dataset Card for SuperWikiImage (SWI)

![](Waifu.png "Based off from Wikipe-tan (Maid, cyan hair, short hair) and Wikipedia's globe logo.")

*Waifu to catch your attention.*

## Dataset Details

### Dataset Description

Off from the presses of *SuperWikipedia-NEXT* comes *SuperWikiImage*: A **~15TiB** (~7 Million) collection of images from wikipedia.

- **Curated by:** KaraKaraWitch
- **Funded by:** Recursal.ai
- **Shared by:** KaraKaraWitch
- **Language(s) (NLP):** Many. Refer to the data below for a list of languages.
- **License:** Mixed. Refer to lower section on licensing

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Source Data:** [https://dumps.wikimedia.org/other/enterprise_html/](https://dumps.wikimedia.org/other/enterprise_html) (Images are scraped from wikimedia commons)

### Supported Tasks and Leaderboards

Anything to deal with images such as image to text, text to image, image to image and many more are supported.

### Languages

We have selected the following Wikipedia's:

<details>
<summary>List of Wikipedia's</summary>
<pre>
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
</pre>

*`.wikipedia.org`* extensions have been added for your convenience.
</details>


### Selection of Wikipedia

We deem a particular Wikipedia language as high quality if:

1. Has a total article count of `>100,000`.
2. Has a `Depth > 5.1`.

*Depth is calculated using the following equation:*

`depth = (article_edits / total_pages) * ((total_pages - articles) / articles) ** 2`

This formula is directly taken from [list of Wikipedias.](https://meta.wikimedia.org/wiki/Wikipedia_article_depth)


### Filtering

No extensive filtering is done compared to superwiki-next.

The process is as follows:

1. We iterate over dump files to retrieve all the figures in a dataset
2. We selectively remove figures in wikipedia that does not end with `(".jpeg", ".jpg", ".png")`
3. Deduplicate by filename matching
4. Prune all images that do not have at least 1 language describing the image.
5. Download from wikipedia (Slow)
6. Compile into webdataset.

For data keys, refer to the usage example.

## Usage Example

The dataset can be loaded with webdataset. Do note that there are multiple extensions to check: `jpg`, `jpeg` or `png`. They have not been reconverted to preserve the original file from wikimedia commons.

```py
import webdataset as wds

# The dataset is compatible with WebDataset format. Example...

tar_root = "... chunk_00/wiki_images-0000.tar"

hf_dataset = wds.WebDataset(str(tar_root)).decode("pil")
for i in hf_dataset:
    print(i)
    # Prints something like this:
    # {
    #     "__key__": "Liam Neeson Deauville 2012 2",
    #     "__url__": "v2_SuperWikiFigures/hf_data/chunk_00/wiki_images-0000.tar",
    #     "jpg": "<PIL.Image.Image image mode=RGB size=566x800 at 0x7FCB939A05E0>",
    #     "__local_path__": "v2_SuperWikiFigures/hf_data/chunk_00/wiki_images-0000.tar",
    #     "json": {
    #         "url": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Liam_Neeson_Deauville_2012_2.jpg",
    #         "lang": {
    #             "az": "Liam Nison Oskar Şindler rolu üçün seçilmişdi.",
    #             "no": "Liam Neeson",
    #             "es": "Liam Neeson",
    #             "el": "Λίαμ Νίσον, Α' Ανδρικός Ρόλος",
    #             "ru": "Актер Лиам Нисон озвучил священника Отца Шона в шестнадцатом сезоне сериала.",
    #             "pl": "Liam Neeson - odtwórca roli Qui-Gona",
    #             "kk": "фильмде Оскар Шиндлер рөлін ойнаған Лиам Нисон (2012)",
    #             "de": "Liam Neeson, Darsteller des Oskar Schindler",
    #             "bn": "শিন্ডলার্স লিস্ট চলচ্চিত্রের মুখ্য অভিনেতা লিয়াম নিসন",
    #             "ast": "Liam Neeson (semeya de 2012) interpreta a Oskar Schindler.",
    #             "id": "Liam Neeson, pemenang Aktor Terbaik",
    #             "tr": "Liam Neeson (2012 yılındaki fotoğrafı) filmde Oskar Schindler olarak yer alıyor.",
    #             "pt": "Liam Neeson",
    #             "it": "Liam Neeson",
    #             "vi": "Liam Neeson (ảnh năm 2012) thủ vai Oskar Schindler.",
    #             "cs": "Liam Neeson vítěz v kategorii nejlepší herec",
    #             "uk": "Ліам Нісон",
    #             "fi": "Liam Neeson Deau\xadvillen elo\xadkuva\xadfestivaaleilla 2012.",
    #             "en": "Liam Neeson, Best Animated Voice Performance winner",
    #             "sv": "Liam Neeson (i bilden från 2012) gjorde rollen som Oskar Schindler i filmen.",
    #         },
    #     },
    # }
    break
```

## Licensing

It's complicated. We have retrieved a jsonl including the licenses to the individual images in the pre-pass to the dataset.

The latest time the license was retrieved was `2024-09-28 00:56 UTC`

The dataset includes only the following permitted licenses:

<details>
<pre>
permits = [
    "attribution",
    "cc by",
    "cc sa",
    "cc-by",
    "cc0",
    "C0 1.0",
    "fal",
    "Nagi BY SA",
    "No restrictions",
    "pdm-",
    "public domain",
    "Share Alike",
    "dl-de/by-2-0",
    "dl-de/zero-2-0",
    # ...Software licenses?
    "AGPL",
    "apache",
    "APSL",
    "Artistic 2.0",
    "bsd",
    "BSL",
    "CeCILL",
    "EPL",
    "FWL",
    "GFDL",
    "gpl",
    "lgpl",
    "LPL",
    "LPPL",
    "mit",
    "MPL ",
    "NetHack GPL",
    "OFL",
    "OGL",
    "OPL 3.0",
    "OSPL",
    "PostgreSQL License",
    "WTFPL",
    "ZLIB",
    # Streetmaps
    "ODbL",
    "OS OpenData",
    "Geoportal",
    "DGA Map",
    # Data
    "StatCanOpen",
    "CDDL",
    "EdictGov-India",
    "GODL-India",
    "KOGL Type 1",
    "KOGL Type-1",
    "KoreaGov",
    "LGACDMX",
    "Licence Ouverte",
    "OGDL",
    "정보공유라이선스 2.0: 허용",
    # Unsure.
    "copyrighted free use",
    "Open data",
]
</pre>
</details>

Images which licenses are unclear, are banknotes or in the following blacklisted licenses are removed.

```
blacklist = [
    # "ECB deicsions",
    # "ECB decisions",
    "Use permitted by the BOI, Currency Department",
    "Flora License",
    "<b>Alice 2 End User License Agreement",
    "Resolution restricted-by-sa",
]
```

Scripts used to process the files have been included. They are similar to the SuperWikiNEXT-32B dataset.

### Dataset Curators

KaraKaraWitch. (I typically hangout in PygmalionAI discord, sometimes EleutherAI and now HF discord. If something is wrong, `@KaraKaraWitch` on discord.)

I'd be happy if you could spread the word and recommend this dataset for your use cases. `:)`

## BibTeX Citation

```tex
@ONLINE{superwikiimg,
  title         = {SuperWikiImages},
  author        = {KaraKaraWitch, recursal.ai},
  year          = {2024},
  howpublished  = {\url{https://huggingface.co/datasets/recursal/SuperWikiImage-7M}},
}

```

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