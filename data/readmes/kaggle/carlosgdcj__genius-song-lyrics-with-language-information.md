# Genius Song Lyrics

Language annotated song and lyrics data

This dataset contain information as recent as 2022 scraped from [Genius](https://genius.com/), a place where people can upload and annotate songs, poems and even books (but mostly songs). It builds upon the [5 Million Song Lyrics Dataset](https://www.kaggle.com/datasets/nikhilnayak123/5-million-song-lyrics-dataset) by using models to identify the native language of each entry.

Genius songs are written in a format that needs some pre processing. Song metadata is often present between square brackets in the middle of the lyrics and the overall structure of the lyrics is preserved, meaning that each entry most likely contains a lot of new line characters that can cause some challenges when reading the data or passing it to a model. Other columns like the features also need similar care before being used. This dataset is an excellent choice if you wanna deal with NLP while also practicing your data cleaning skills.

## Feature overview
| **Column**        | **Meaning**                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------|
| **title**         | Title of the piece. Most entries are songs, but there are also some books, poems and even some other stuff |
| **tag**           | Genre of the piece. Most non-music pieces are "misc", but not all. Some songs are also labeled as "misc"   |
| **artist**        | Person or group the piece is attributed to                                                                 |
| **year**          | Release year                                                                                               |
| **views**         | Number of page views                                                                                       |
| **features**      | Other artists that contributed                                                                             |
| **lyrics**        | Lyrics                                                                                                     |
| **id**            | Genius identifier                                                                                          |
| **language_cld3** | Lyrics language according to CLD3. Not reliable results are NaN                                            |
| **language_ft**   | Lyrics language according to FastText's langid. Values with low confidence (&lt;0.5) are NaN                  |
| **language**      | Combines language_cld3 and language_ft. Only has a non NaN entry if they both "agree"                      |

## Language index
Below is a reference mapping language tags to their english names. I recommend using a library like [langcodes](https://github.com/rspeer/langcodes) to deal with this kind of stuff.
| Tag   | Language Name     |
|:------|:------------------|
| af    | Afrikaans         |
| als   | Tosk Albanian     |
| am    | Amharic           |
| ar    | Arabic            |
| arz   | Egyptian Arabic   |
| as    | Assamese          |
| ast   | Asturian          |
| az    | Azerbaijani       |
| azb   | South Azerbaijani |
| ba    | Bashkir           |
| be    | Belarusian        |
| bg    | Bulgarian         |
| bh    | Bihari languages  |
| bn    | Bangla            |
| bo    | Tibetan           |
| br    | Breton            |
| bs    | Bosnian           |
| ca    | Catalan           |
| ce    | Chechen           |
| ceb   | Cebuano           |
| ckb   | Central Kurdish   |
| co    | Corsican          |
| cs    | Czech             |
| cv    | Chuvash           |
| cy    | Welsh             |
| da    | Danish            |
| de    | German            |
| dv    | Divehi            |
| el    | Greek             |
| en    | English           |
| eo    | Esperanto         |
| es    | Spanish           |
| et    | Estonian          |
| eu    | Basque            |
| fa    | Persian           |
| fi    | Finnish           |
| fil   | Filipino          |
| fr    | French            |
| fy    | Western Frisian   |
| ga    | Irish             |
| gd    | Scottish Gaelic   |
| gl    | Galician          |
| gn    | Guarani           |
| gu    | Gujarati          |
| ha    | Hausa             |
| haw   | Hawaiian          |
| he    | Hebrew            |
| hi    | Hindi             |
| hmn   | Hmong             |
| hr    | Croatian          |
| hsb   | Upper Sorbian     |
| ht    | Haitian Creole    |
| hu    | Hungarian         |
| hy    | Armenian          |
| ia    | Interlingua       |
| id    | Indonesian        |
| ie    | Interlingue       |
| ig    | Igbo              |
| io    | Ido               |
| is    | Icelandic         |
| it    | Italian           |
| ja    | Japanese          |
| jbo   | Lojban            |
| jv    | Javanese          |
| ka    | Georgian          |
| kk    | Kazakh            |
| km    | Khmer             |
| kn    | Kannada           |
| ko    | Korean            |
| ku    | Kurdish           |
| kw    | Cornish           |
| ky    | Kyrgyz            |
| la    | Latin             |
| lb    | Luxembourgish     |
| li    | Limburgish        |
| lmo   | Lombard           |
| lt    | Lithuanian        |
| lv    | Latvian           |
| mg    | Malagasy          |
| mi    | Māori             |
| min   | Minangkabau       |
| mk    | Macedonian        |
| ml    | Malayalam         |
| mn    | Mongolian         |
| mr    | Marathi           |
| ms    | Malay             |
| mt    | Maltese           |
| my    | Burmese           |
| mzn   | Mazanderani       |
| nap   | Neapolitan        |
| nds   | Low German        |
| ne    | Nepali            |
| nl    | Dutch             |
| nn    | Norwegian Nynorsk |
| no    | Norwegian         |
| ny    | Nyanja            |
| oc    | Occitan           |
| or    | Odia              |
| pa    | Punjabi           |
| pl    | Polish            |
| pms   | Piedmontese       |
| pnb   | Western Panjabi   |
| ps    | Pashto            |
| pt    | Portuguese        |
| qu    | Quechua           |
| ro    | Romanian          |
| ru    | Russian           |
| sa    | Sanskrit          |
| sah   | Sakha             |
| sd    | Sindhi            |
| si    | Sinhala           |
| sk    | Slovak            |
| sl    | Slovenian         |
| sm    | Samoan            |
| sn    | Shona             |
| so    | Somali            |
| sq    | Albanian          |
| sr    | Serbian           |
| st    | Southern Sotho    |
| su    | Sundanese         |
| sv    | Swedish           |
| sw    | Swahili           |
| ta    | Tamil             |
| te    | Telugu            |
| tg    | Tajik             |
| th    | Thai              |
| tk    | Turkmen           |
| tr    | Turkish           |
| tt    | Tatar             |
| tyv   | Tuvinian          |
| ug    | Uyghur            |
| uk    | Ukrainian         |
| ur    | Urdu              |
| uz    | Uzbek             |
| vi    | Vietnamese        |
| war   | Waray             |
| xh    | Xhosa             |
| yi    | Yiddish           |
| yo    | Yoruba            |
| yue   | Cantonese         |
| zh    | Chinese           |
| zu    | Zulu              |

출처: Kaggle (carlosgdcj/genius-song-lyrics-with-language-information)
태그: music, data cleaning, nlp, text classification, multilingual
라이선스: Unknown
수정일: 2023-01-11T19:52:10.993Z
