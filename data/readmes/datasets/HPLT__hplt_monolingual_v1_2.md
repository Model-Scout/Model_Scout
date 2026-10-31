---
license: cc0-1.0
task_categories:
- text-generation
language:
- af
- ar
- az
- be
- bg
- bn
- ca
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
- ga
- gl
- gu
- hbs
- he
- hi
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- kn
- ko
- ky
- la
- lt
- lv
- mk
- ml
- mn
- mr
- ms
- mt
- my
- nb
- ne
- nl
- nn
- pa
- pl
- ps
- pt
- ro
- ru
- si
- sk
- sl
- so
- sq
- sv
- sw
- ta
- te
- th
- tl
- tr
- tt
- uk
- ur
- uz
- vi
- zh
pretty_name: HPLT Monolingual Release v1.2
size_categories:
- n>1T
---

# HPLT Monolingual Release v1.2

**NB: HPLT1.2 is now superseded by a newer release:**

**[HPLT3.0](https://huggingface.co/datasets/HPLT/HPLT3.0)**

**We recommed switching to v3.0, unless you have a compelling reason to stay on 1.2.**

This repository contains the means to access the datasets created by the [HPLT project](https://hplt-project.org/datasets/v1.2). These large-scale web-crawled corpora based on CommonCrawl and the Internet Archive are accessible in 75 languages. The full dump is available as well as deduplicated and further cleaned versions depending on the config that you use (see the usage example below).

## Prerequisites

HPLT compresses their files with `zst` so to use this library you need to make sure that `zstandard` is installed:

```shell
pip install zstandard
```

## Usage

You can download either the full portion of the data (e.g. `nl`), its deduplicated set (`nl_deduplicated`), or the fully cleaned set (`nl_cleaned`).

You'll soon need to use `trust_remote_code=True` to download this dataset. This is required so that downloading the dataset can be done directly from HPLT.

```python
from datasets import load_dataset


ds = load_dataset(
    "HPLT/hplt_monolingual_v1_2",
    "ky",
    # or "ky_deduplicated",
    # or "ky_cleaned",
    trust_remote_code=True
)
```

## Supported languages

```python
{
    "af": "Afrikaans",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bangla",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "gl": "Galician",
    "gu": "Gujarati",
    "hbs": "Serbo-Croatian",
    "he": "Hebrew",
    "hi": "Hindi",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "kn": "Kannada",
    "ko": "Korean",
    "ky": "Kyrgyz",
    "la": "Latin",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "nb": "Norwegian Bokmål",
    "ne": "Nepali",
    "nl": "Dutch",
    "nn": "Norwegian Nynorsk",
    "pa": "Punjabi",
    "pl": "Polish",
    "ps": "Pashto",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "sq": "Albanian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "tt": "Tatar",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "zh": "Chinese"
}
```

## Fields

- `id`: Document ID
- `document_lang`: Document language identified by CLD2 during the WARC extraction process.
- `scores`: Fluency scores for each paragraph in the document. 
- `langs`: Language with highest detected probability for each paragraph in the document.
- `text`: The document's text (a concatenation of newline-separated paragraphs).
- `url`: Document URL.
- `collection`: Collection name.

## Data removal

Found data that you would like removed in the next release? Contact [the data creators](mailto:hplt-datasets@ufal.mff.cuni.cz).

## Terms of Use

HPLT [states](https://hplt-project.org/datasets/v1.2) the following:

> These data are released under these Terms of Use:
> - We do not own any of the text from which these text data has been extracted.
> - We license the actual packaging of these text data under the Creative Commons CC0 license ("no rights reserved").


## Acknowledgements

Initial transfer to the Hugging Face hub by [Bram Vanroy](https://huggingface.co/BramVanroy).