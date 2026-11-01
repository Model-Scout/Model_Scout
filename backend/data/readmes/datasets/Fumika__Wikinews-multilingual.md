---
license: cc-by-2.5
language:
- en
- es
- fr
- de
- pt
- pl
- it
- zh
- ru
- ja
- nl
- sv
- ta
- sr
- cs
- ca
- he
- tr
- fi
- eo
- el
- hu
- uk
- 'no'
- ar
- fa
- ko
- ro
- bg
- bs
- li
- sq
- th
task_categories:
- text-classification
- feature-extraction
---
# Wikinews - weakly aligned multilingual pararell sentence datasets

This dataset contains 15,200 multilingual WikiNews articles in 33 languages.
Out of 15,200 articles, 9,960 are non-English news and 5240 are English news.  All non-English news are linked to one of 5240 English news. Linked articles show the same event.
List of non-English languages are: Spanish, French, German, Portuguese, Polish, Italian, Chinese, Russian, Japanese, Dutch, Swedish, Tamil, Serbian, Czech, Catalan, Hebrew, Turkish, Finnish, Esperanto, Greek, Hungarian, Ukrainian, Norwegian, Arabic, Persian, Korean, Romanian, Bulgarian, Bosnian, Limburgish, Albanian, Thai.

## Dataset Details

### Example raw datasets

|   | title                                                       | pageid | categories                                         | lang | url                                                                                      | text                                                       | date                        | type            |
|---|-------------------------------------------------------------|--------|----------------------------------------------------|------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------|-----------------|
| 0 | 'Bloody Sunday Inquiry' publishes report into ...           | 191513 | [Northern Ireland, Martin McGuinness, Politics...] | en   | https://en.wikinews.org/wiki/%27Bloody_Sunday_...                                       | [On Tuesday, the "Bloody Sunday Inquiry" publi...          | 2010-06-17                 | title           |
| 1 | 1972 ”இரத்த ஞாயிறு” படுகொலைகள் தொடர்பில் பிரித...           | 191513 | [Northern Ireland, Martin McGuinness, Politics...] | ta   | https://ta.wikinews.org/wiki/1972_%E2%80%9D%E0...                                        | [வடக்கு அயர்லாந்தில் 38 ஆண்டுகளுக்கு முன்னர் இ...   | வியாழன், சூன் 17, 2010 | interlang link |
| 2 | 'Very serious': Chinese government releases co...           | 232226 | [China, December 30, 2010, Politics and confli...] | en   | https://en.wikinews.org/wiki/%27Very_serious%2...                                       | [A report by the Chinese government states cor...         | 2010-12-30                 | title           |
| 3 | Čína připustila, že tamní korupce je vážný pro...           | 232226 | [China, December 30, 2010, Politics and confli...] | cs   | https://cs.wikinews.org/wiki/%C4%8C%C3%ADna_p%...                                        | [Zpráva čínské vlády připouští, že korupce v z... | Středa 29. prosince 2010 | interlang link |
| 4 | China admite que la corrupción en el país es '...           | 232226 | [China, December 30, 2010, Politics and confli...] | es   | https://es.wikinews.org/wiki/China_admite_que_...                                       | [29 de diciembre de 2010Beijing, China —, Un r... | None                        | interlang link |


### Variables

Each data point includes following variables:

| Field Name                        | Description                                                                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| title                             | WikiNews article title                                                                                                                               |
| pageid                             | pageid defined by the English WikiNews article. Data with the same pageid corresponds to the same news event linked together.             |
| categories                         | list of topics defined by WikiNews. All pages have at least one topic from [Crime and law, Culture and entertainment, Disasters and accidents, Economy and business, Education, Environment, Heath, Obituaries, Politics and conflicts, Science and technology, Sports, Wackynews, Weather] |
| text                              | content of the article. Some foreign pages have news titles but no content. For those, text is left empty.                                        |
| lang                      | languages of the article (WP code, check [here](https://en.wikipedia.org/wiki/List_of_Wikipedias#Lists) for lists )                                                                                        |
| url                               | articles' URL                                                                                                                                      |
| date                              | date of publish in YYYY-MM-DD for English pages. Dates in foreign pages were left as it is. To get a date with YYYY-MM-DD format, look for a English page with the same pageid.           |
| type                              | `title` for the English page, `interlang link` for non-English page linked to the English page with the `pageid`

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->



- **Curated by:** Fumika Isono, Primer AI
- **Language(s) (NLP):** en, es, fr, de, pt, pl, it, zh, ru, ja, nl, sv, ta, sr, cs, ca, he, tr, fi, eo, el, hu, uk, 'no', ar, fa, ko, ro, bg, bs, li, sq, th
- **License:** cc-by-2.5

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [Github](https://github.com/PrimerAI/primer-research/tree/main)
- **Paper:** ArXiv [Linear Cross-Lingual Mapping of Sentence Embeddings](https://arxiv.org/abs/2305.14256)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Weakly aligned multilingual pararell sentence datasets
Weakly aligned multilingual pararell sentence datasets can be constructed by comparing the titles and/or contents of the WikiNews pages that are linked to the same English WikiNews page (in the dataset, they have the same pageid).
Following is the example case where titles of the same pageid are retrieved. These five phrases (news titles) are the news titles of the same incident.

| News title                                                    | Language | type              |
|---------------------------------------------------------------|----------|-------------------|
| Bomb blast in Delhi kills 12, injures 62                      | English  | title      |
| چندین کشته بر اثر انفجار بمب در مقابل دادگاه عالی هند        | Farsi    | title|
| 9 נהרגו בפיגוע מחוץ לבית המשפט העליון של הודו               | Hebrew   | title|
| У Индији 11 мртвих, 64 повређених                             | Serbian  | title|
| தில்லி உயர்நீதிமன்றத்தில் குண்டு வெடிப்பு, 10 பேர் உயிரிழப்பு | Tamil    | title|

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->
- Multilingual embeddings
- Language comparison


### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->
[Wikinews](https://www.wikinews.org/)


## Dataset Card Authors

Fumika Isono
