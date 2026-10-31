---
language:
- ar
- hy
- az
- eu
- be
- bn
- bs
- pt
- bg
- my
- km
- ca
- zh
- hr
- cs
- da
- nl
- en
- eo
- et
- fa
- fi
- fr
- ka
- de
- el
- he
- hi
- hu
- is
- it
- ja
- kn
- ko
- ku
- lv
- lt
- mk
- ms
- ml
- mn
- ne
- 'no'
- ps
- pl
- pa
- ro
- ru
- sr
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- ta
- te
- th
- tr
- uk
- ur
- ve
- yo
- id
task_categories:
- text-generation
- translation
- text-classification
size_categories:
- 1B<n<10B
license: apache-2.0
---


# Subscene
<center>
    <img src="https://huggingface.co/datasets/khalidalt/subscene/resolve/main/subscene_logo.png" alt="Subscene: The largest collection of subtitles">
</center>



## Dataset Summary

Subscene is a vast collection of multilingual subtitles, encompassing 65 different languages and consisting of more than 30 billion tokens with a total size of 410.70 GB. This dataset includes subtitles for movies, series, and animations gathered from the Subscene dump. It provides a rich resource for studying language variations and building multilingual NLP models. We have carefully applied a fastText classifier to remove any non-language content from incorrect subsets. Additionally, we performed basic cleaning and filtration. However, there is still room for further cleaning and refinement.

## Dataset Structure

### Data Instances

```
{"subtitle_name": "choir-girl",
"file_name": "Choir.Girl.2019.HDRip.XviD.AC3-EVO.json",
"transcript": [{"id": 1, "start_time": "00:00:09,741", "end_time": "00:00:13,702", "text": "Subtitles by explosiveskull"}, {"id": 2, "start_time": "00:01:58,569", "end_time": "00:02:00,536", "text": "Get Julius on the phone."}, {"id": 3, "start_time": "00:02:00,538", "end_time": "00:02:03,338", "text": "The sponsor's got an issue with sharing the page."}, {"id": 4, "start_time": "00:02:08,412", "end_time": "00:02:09,411", "text": "Eugene."}, {"id": 5, "start_time": "00:02:10,748", "end_time": "00:02:14,950", "text": "Yeah, uh, I'm supposed to meet Julius."}, {"id": 6, "start_time": "00:02:14,952", "end_time": "00:02:19,888", "text": "I'm Anne Kellan, the editor. You won't be meeting him."}, {"id": 7, "start_time": "00:02:19,890", "end_time": "00:02:22,391", "text": "He said on the phone that, um..."}, {"id": 8, "start_time": "00:02:22,393", "end_time": "00:02:24,293", "text": "We won't be publishing these."}, {"id": 9, "start_time": "00:02:24,295", "end_time": "00:02:31,266", "text": "You have a child overdosing, an elderly woman being bashed"}, {"id": 10, "start_time": "00:02:31,268", "end_time": "00:02:33,302", "text": "and this,"}, {"id": 11, "start_time": "00:02:33,304", "end_time": "00:02:36,205", "text": "a girl either being sexually assaulted or prostituting herself."}, {"id": 12, "start_time": "00:02:36,907", "end_time": "00:02:39,374", "text": "I spoke to Julius and..."}, ...]
}
```

```
{"subtitle_name": "the-fabulous-first-season",
 "file_name": "The.Fabulous.S01E06.DUBBED.WEBRip.x264-ION10_Arabic.json",
 "transcript": [{"id": "1", "start_time": "00:00:06,006", "end_time": "00:00:09,926", "text": "‫\"مسلسلات NETFLIX\"‬"}, {"id": "2", "start_time": "00:00:18,309", "end_time": "00:00:19,849", "text": "‫- المجال مفتوح أمامك.‬ ‫- اركض!‬"}, {"id": "3", "start_time": "00:00:19,936", "end_time": "00:00:22,186", "text": "‫تلك فرصتك! هيا يا \"وو مين\"!‬"}, {"id": "4", "start_time": "00:00:23,189", "end_time": "00:00:24,229", "text": "‫- ويلاه. ‬ ‫- لا بأس.‬"}, {"id": "5", "start_time": "00:00:24,315", "end_time": "00:00:26,025", "text": "‫رائع، أحسنت صنعًا!‬"}, {"id": "6", "start_time": "00:00:26,109", "end_time": "00:00:27,189", "text": "‫أحسنت!‬"}, {"id": "7", "start_time": "00:00:27,277", "end_time": "00:00:28,397", "text": "‫ألن تخبرني؟‬"}, {"id": "8", "start_time": "00:00:29,320", "end_time": "00:00:30,490", "text": "‫الفتاة التي في الصورة.‬"}, {"id": "9", "start_time": "00:00:31,072", "end_time": "00:00:32,622", "text": "‫كم هو مثابر. العب الكرة فحسب.‬"}, ....]
}

```

### Data Fields

- `subtitle_name` (`str`): The name of the folder containing the subtitle file. This likely corresponds to the movie, series, or anime title.
- `file_name` (`str`): The specific filename of the subtitle file itself.
- `transcript` (`dict`): This dictionary holds the complete transcript information for the subtitle file. It contains nested structures to represent individual subtitle segments.
- `id` (`int`): (Within `transcript` dictionary) A unique identifier for a specific subtitle segment within the file.
- `start_time` (`str`): (Within `transcript` dictionary) The starting time of the subtitle segment, likely formatted according to a specific timecode standard.
- `end_time` (`str`): (Within `transcript` dictionary) The ending time of the subtitle segment, following the same timecode format as `start_time`.
- `text` (`str`): (Within `transcript` dictionary) The actual text content displayed for that specific subtitle segment.


## Using The HuggingFace datasets

```python
from datasets import load_dataset

# Load the Arabic subset only
ds = load_dataset("refine-ai/Subscene", "arabic", trust_remote_code=True)

```


## Dataset Statstics


| Language            | Raw Size   | Num Char   | Num Byte   | Num Words   | Num Token   |
|:------------------- |:-----------|:-----------|:-----------|:------------|:------------|
| Arabic              | 59.7 GB    | 12B        | 24B        | 3B          | 5B          |
| Armenian            | 933.7 KB   | 175K       | 372K       | 36K         | 177K        |
| Azerbaijani         | 5.7 MB     | 1M         | 2M         | 225K        | 701K        |
| Basque              | 36.4 MB    | 9M         | 10M        | 1M          | 3M          |
| Belarusian          | 3.2 MB     | 598K       | 1M         | 119K        | 433K        |
| Bengali             | 2.6 GB     | 429M       | 1B         | 88M         | 152M        |
| traditional_chinese | 1.1 GB     | 202M       | 323M       | 38M         | 110M        |
| Bosnian             | 51.0 MB    | 12M        | 15M        | 3M          | 6M          |
| Brazilian-Portuguese| 9.1 GB     | 2B         | 3B         | 463M        | 727M        |
| Bulgarian           | 324.7 MB   | 60M        | 126M       | 13M         | 38M         |
| Bulgarian-English   | 4.2 MB     | 851K       | 1M         | 179K        | 515K        |
| Burmese             | 724 MB     | 127M       | 378M       | 11M         | 237M        |
| Cambodian-Khmer     | 165.5 MB   | 28M        | 80M        | 2M          | 32M         |
| Catalan             | 70.8 MB    | 17M        | 20M        | 4M          | 6M          |
| simplified_chinese  | 3.9 GB     | 197M       | 505M       | 29M         | 129M        |
| Croatian            | 1.1 GB     | 260M       | 315M       | 54M         | 129M        |
| Czech               | 2.4 GB     | 519M       | 671M       | 108M        | 288M        |
| Danish              | 12.1 GB    | 3B         | 4B         | 716M        | 1B          |
| Dutch               | 5.5 GB     | 1B         | 2B         | 319M        | 610M        |
| Dutch-English       | 28.3 MB    | 7M         | 9M         | 2M          | 3M          |
| English             | 127.9 GB   | 30B        | 36B        | 7B          | 10B         |
| English-German      | 160.5 MB   | 39M        | 47M        | 8M          | 14M         |
| Esperanto           | 4.6 MB     | 1M         | 1M         | 224K        | 431K        |
| Estonian            | 345.9 MB   | 83M        | 98M        | 15M         | 39M         |
| Farsi_persian       | 40.3 GB    | 7B         | 15B        | 2B          | 5B          |
| Finnish             | 4.3 GB     | 1B         | 1B         | 179M        | 522M        |
| French              | 18 GB      | 5B         | 6B         | 1B          | 1B          |
| Georgian            | 2.3 MB     | 432K       | 1M         | 79K         | 378K        |
| German              | 3 GB       | 788M       | 931M       | 157M        | 307M        |
| Greek               | 4.5 GB     | 919M       | 2B         | 181M        | 737M        |
| Greenlandic         | 10.2 MB    | 3M         | 3M         | 298K        | 1M          |
| Hebrew              | 4.9 GB     | 839M       | 2B         | 194M        | 811M        |
| Hindi               | 575 MB     | 92M        | 285M       | 24M         | 36M         |
| Hungarian           | 1.2 GB     | 287M       | 353M       | 52M         | 141M        |
| Hungarian_English   | 600kb      | 126K       | 152K       | 25K         | 53K         |
| Icelandic           | 476.1 MB   | 110M       | 144M       | 23M         | 58M         |
| Indonesian          | 9.7 GB     | 10B        | 12B        | 2B          | 3B          |
| Italian             | 7 GB       | 2B         | 3B         | 501M        | 950M        |
| Japanese            | 2.0 GB     | 198M       | 596M       | 29M         | 190M        |
| Kannada             | 21.8 MB    | 4M         | 11M        | 564K        | 1M          |
| Korean              | 5.5 GB     | 553M       | 2B         | 188M        | 821M        |
| Kurdish             | 72.4 MB    | 14M        | 29M        | 3M          | 11M         |
| Latvian             | 157.2 MB   | 35M        | 43M        | 6M          | 18M         |
| Lithuanian          | 207.3 MB   | 47M        | 57M        | 8M          | 24M         |
| Macedonian          | 97 MB      | 20M        | 41M        | 4M          | 12M         |
| Malay               | 4.9 GB     | 1B         | 1B         | 221M        | 371M        |
| Malayalam           | 446.9 MB   | 86M        | 246M       | 11M         | 27M         |
| Manipuri            | 1000kb     | 93K        | 280K       | 14K         | 60K         |
| Mongolian           | 9.9 MB     | 2M         | 4M         | 390K        | 2M          |
| Nepali              | 37.8 MB    | 6M         | 19M        | 1M          | 2M          |
| Norwegian           | 6.8 GB     | 2B         | 2B         | 392M        | 765M        |
| Pashto              | 9.5 MB     | 2M         | 4M         | 417K        | 870K        |
| Polish              | 2 GB       | 467M       | 570M       | 85M         | 243M        |
| Portuguese          | 3.7 GB     | 899M       | 1B         | 191M        | 280M        |
| Punjabi             | 55.3 MB    | 87K        | 263K       | 22K         | 33K         |
| Romanian            | 3.5 GB     | 835M       | 1B         | 183M        | 402M        |
| Russian             | 1.9 GB     | 359M       | 740M       | 71M         | 220M        |
| Serbian             | 929.5 MB   | 225M       | 285M       | 48M         | 113M        |
| Sinhala             | 1.1 GB     | 185M       | 544M       | 37M         | 345M        |
| Slovak              | 649.2 MB   | 140M       | 179M       | 29M         | 75M         |
| Slovenian           | 654.8 MB   | 151M       | 183M       | 31M         | 74M         |
| Somali              | 1.1 MB     | 300K       | 353K       | 62K         | 134K        |
| Spanish             | 10.9 GB    | 3B         | 3B         | 548M        | 831M        |
| Sundanese           | 3.1 Mb     | 762K       | 881K       | 135K        | 302K        |
| Swahili             | 15.9 MB    | 4M         | 4M         | 661K        | 1M          |
| Swedish             | 6.9 GB     | 2B         | 2B         | 392M        | 795M        |
| Tagalog             | 188 MB     | 45M        | 52M        | 9M          | 18M         |
| Tamil               | 1 GB       | 50M        | 149M       | 7M          | 16M         |
| Telugu              | 223.5 MB   | 39M        | 115M       | 6M          | 14M         |
| Thai                | 6.9 GB     | 1B         | 3B         | 77M         | 1B          |
| Turkish             | 6.7 GB     | 2B         | 2B         | 268M        | 789M        |
| Ukrainian           | 891.1 MB   | 168M       | 346M       | 34M         | 116M        |
| Urdu                | 5 GB       | 53M        | 116M       | 15M         | 21M         |
| Vietnamese          | 16 GB      | 3B         | 5B         | 952M        | 1B          |
| Yoruba              | 820.6 KB   | 154K       | 230K       | 46K         | 80K         |


## Citation Information
If you use this corpus, please cite the paper:

```
@misc{refine-ai,
author = {Refine AI},
title = {Subscene: A Large-Scale Multilingual Subtitle Dataset},
year = {2024},
}
```

##  Acknowledgements

We would like to extend our thanks to everyone who has worked on and contributed to the Subscene website. A special thanks goes to eionlol for uploading the entire Subscene dump, organized by language. You can access the archive through the following link: https://archive.org/details/subscene-final-dump