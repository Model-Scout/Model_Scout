# Ted Talks Transcript

trancripts in multiple languages

### An extension to Kaggle's TED dataset
Using transcripts provided by [TED.com](www.ted.com), a dataset that combines combines YouTube metadata (at the time of scrapping) and metadata from [Kaggle's TED dataset](https://www.kaggle.com/rounakbanik/ted-talks).

This extension provides not just additional metadata from YouTube, but also additional transcripts of the same video, but in different languages (e.g. Portugese, French, Arabic, Chinese, Japnese, Korean, Turkish, Dutch...). In total, 111 different languages are available (most videos do not have transcript for all languages).

### Content
For each of the 111 languages in tedDirector.zip, each language file is a CSV file with the following headers:

1. `videoID` - YouTube IDs

2. `lang` - Language code

3. `title` - Title of the TED Talk

4. `transcript` - Transcript of the TED Talk in `lang`

### Acknowledgements
1. This dataset was developed as part of a larger dataset used for an information retrieval assignment. In that assignment, my team and I used TED talks to evaluate different configuration of search engine algorithms. We also used different languages for the search and retrieve task, to test for reliability of our search engine. More information can be found in our [Github repository](https://github.com/ymittal/ttds-project). Dataset is downloaded from [TedTalksDirector](https://www.youtube.com/user/TEDtalksDirector) using [YouTube-dl](https://github.com/rg3/youtube-dl). 

2. Code for downloading can be found from the [IR project](https://github.com/ymittal/ttds-project).

3. More about language codes here from [w3schools.com](https://www.w3schools.com/tags/ref_language_codes.asp).

### Inspiration
Some of the problem experienced while preparing this dataset:
1. How can we improve the matching of YouTube dataset to the data scrapped from TED talk

출처: Kaggle (goweiting/ted-talks-transcript)
태그: text mining, text
라이선스: CC0: Public Domain
수정일: 2018-01-27T17:11:45.757Z
