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
  - en
  - es
  - fr
  - ja
  - ko
  - pt
  - ru
  - zho
configs:
  - config_name: default
    data_files:
     - split: full
       path: "jsonl/*"
pretty_name: MDN
---

# Dataset Card for MDN

![](MDNWaifu.png "Mizuho (水穂) | Mizuho is a self-taught developer who rose through the ranks by leveraging the vast resources available on MDN Web Docs. She embodies the spirit of open-source and community collaboration, constantly contributing to the repository and mentoring new developers. Her mission is to make web development accessible to everyone, breaking down complex concepts into understandable and engaging lessons.")

*Waifu to catch your attention.*

### Dataset Description

*MDN* is a **~57M** Tokens (llama-2-7b-chat-tokenizer) / **~46.52M** Tokens (RWKV Tokenizer) scrape of [MDN (Developer.mozilla.org)](https://developer.mozilla.org/).
It serves as a training resource for large language models and other NLP tasks. 
This card details the dataset's origin, content, and limitations.


- **Curated by:** KaraKaraWitch
- **Funded by:** Recursal.ai (I work there lol)
- **Shared by:** KaraKaraWitch
- **Language(s) (NLP):** English, Espanol, French, Japanese, Korean, Brazilian Portuguese, Russian, Chinese Simplified, Chinese Traditional
- **License:** cc-by-sa-2.5

MDN was created under time constraints for the release of [EagleX v1](https://huggingface.co/recursal/EagleX_1-7T_HF), and may contain biases in selection.  

### Supported Tasks and Leaderboards

Primarily used for language modeling.

### Languages

MDN lists the following languages:

- English
- Espanol
- French
- Japanese
- Korean
- Brazilian Portuguese
- Russian
- Chinese Simplified
- Chinese Traditional

### Processing

We obtained a list of pages to download with the MDN's [sitemap.xml.](https://developer.mozilla.org/sitemap.xml) This was manually downloaded.
For each sitemap, we scrape the website. saving the raw html responses for further filtering and cleaning.

For the actual html processing, we recommend reading the code found in the file: `MDNClean.py`.

The file itself is a typer application with the following commands:

```
- sitemap
  - Gets a list of urls to download and downloads it to a folder.
- clean
  - cleans a folder. saving each the cleaned text to a final jsonl.
```

We have noted an issue where there could be a false positive virus-detection on 4 of the compressed files.
We have used the dataset in it's uncompressed form and didn't encounter any issues. 

### Data Instances

Refer to this sample to see all the relavant fields.

```json
{
    "title": "Game development",
    "text": "\n\nGame development\n================\n\nGaming is one of the most popular computer activities. New technologies are constantly arriving to make\n it possible to develop better and more powerful games that can be run in any standards-compliant web\n browser.\n\nDevelop web games\n-----------------\n\nWelcome to the MDN game development center! In this area of the site, we provide resources for web<...TRUNCATED>"
}
```

The format has the following keys:

```md
- "title" (str) [The title of the article]
- "text" (str) [The html content converted fro html into markdown.]
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

### Dataset Curators

KaraKaraWitch. (I typically hang out in PygmalionAI discord, sometimes EleutherAI. If something is wrong, `@karakarawitch` on discord.)

I'd be happy if you could spread the word and recommend this dataset.

### Licensing Information

MDN lists their license as [CC-BY-SA.](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Attrib_copyright_license)

Recursal Waifus (The banner image) are licensed under CC-BY-SA. 
They do not represent the related websites in any official capacity unless otherwise or announced by the website. 
You may use them as a banner image. However, you must always link back to the dataset.

### Citation Information

```
@misc{MDN,
  title         = {MDN},
  author        = {KaraKaraWitch, recursal.ai},
  year          = {2024},
  howpublished  = {\url{https://huggingface.co/datasets/recursal/MDN}},
}
```