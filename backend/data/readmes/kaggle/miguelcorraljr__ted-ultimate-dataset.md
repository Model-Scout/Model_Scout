# TED Talks Transcripts for NLP

Transcripts and more in 12 languages

### Context
TED is devoted to spreading powerful ideas in just about any topic. These datasets contain over 4,000 TED talks including transcripts in many languages.  

If you would like a dataset for a language that is not listed below or a in a different file format (JSON, SQL, etc.), please checkout my Python module – [TEDscraper](https://github.com/corralm/TEDscraper). 

### Languages
TED talks have been subtitled in over 100 languages. I've included datasets for these 12 languages:

| Code  | Language              |
|-------|-----------------------|
| en    | English               |
| es    | Spanish               |
| pt-br | Portuguese (Brazilian)|
| fr    | French                |
| it    | Italian               |
| zh-cn | Chinese (simplified)  |
| zh-tw | Chinese (traditional) |
| ko    | Korean                |
| ja    | Japanese              |
| tr    | Turkish               |
| ru    | Russian               |
| he    | Hebrew                |

### Attributes
| Attribute          | Description                                     | Data Type  |
|------------------|-------------------------------------------------|------------|
| talk_id          | Talk identification number provided by TED      | int        |
| title            | Title of the talk                               | string     |
| speaker_1        | First speaker in TED's speaker list             | string     |
| speakers         | Speakers in the talk              | dictionary |
| occupations      | *Occupations of the speakers| dictionary |
| about_speakers   | *Blurb about each speaker| dictionary |
| views            | Count of views                                  | int        |
| recorded_date    | Date the talk was recorded                      | string     |
| published_date   | Date the talk was published to TED.com          | string     |
| event            | Event or medium in which the talk was given     | string     |
| native_lang      | Language the talk was given in                  | string     |
| available_lang   | All available languages (lang_code) for a talk  | list       |
| comments         | Count of comments                               | int        |
| duration         | Duration in seconds                             | int        |
| topics           | Related tags or topics for the talk             | list       |
| related_talks    | Related talks (key='talk_id', value='title')    | dictionary |
| url              | URL of the talk                                 | string     |
| description      | Description of the talk                         | string     |
| transcript       | Full transcript of the talk                     | string     |

*The dictionary key maps to the speaker in ‘speakers’.

### Meta
Author: Miguel Corral Jr.  
Email: corraljrmiguel@gmail.com  
LinkedIn: https://www.linkedin.com/in/iMiguel/  
GitHub: https://github.com/corralm

Distributed under the Creative Commons license – Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).

### Inspiration
* Natural Language Processing
* Topic modeling
* Clustering
* Recommender system
* Classification
* Regression

출처: Kaggle (miguelcorraljr/ted-ultimate-dataset)
태그: nlp, classification, recommender systems, text
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2020-05-05T02:30:44.427Z
