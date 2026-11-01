# Webtoon Dataset in Korean

comics serialized in webtoon platforms (Naver)

## Context
**네이버웹툰**에서 서비스되는 2100편 이상의 웹툰들과 **네이버 베스트도전**의 3100편 이상의 웹툰들에 대한 데이터셋입니다. 
The dataset contains +2100 unique webtoons serialized in Naver Webtoon and +3100 records about webtoons in Naver best Challenge. 
These datasets are described in Korean. 

(Update 2022.12.31)
- add new webtoons
- fix duplicate webtoons in challenge_naver.csv

## Content
###naver.csv
webtoons serialized in Naver Webtoon
- `id`: unique id of the webtoon
- `title`: title of the webtoon
- `author`: writer of the webtoon
- `genre`:  genre of the webtoon
- `description`: introduction of the webtoon
- `rating`: average rating out of 10 for the webtoon
- `date`: the most recent update date of the webtoon
- `completed`: completion status
- `age`: the recommended age
- `free`: free service("기다리면 무료")  event availablity
- `link`: link of the webtoon

### naver_challenge.csv
webtoons in Naver best Challenge
- `id`: unique id of the challenge webtoon
- `title`: title of the webtoon
- `author`: author of the webtoon(the last strings are blurred)
- `summary`: summary of the webtoon
- `rating`: rating of the webtoon
- `genre`: genre of the webtoon.
- `format`: format of the webtoon
- `description`: description of the webtoon
- `serialize`: whether this webtoon is officially being serialized on Naver (네이버 정식연재 웹툰 여부)
- `potenup`: chosen as the potential up(포텐업)

## Acknowledgement
All data were collected from [Naver Webtoon](https://comic.naver.com/index)

출처: Kaggle (bmofinnjake/naverwebtoon-datakorean)
태그: arts and entertainment, nlp, recommender systems, comics and animation, anime and manga, korea
라이선스: CC BY-NC-SA 4.0
수정일: 2022-12-31T11:40:33.453Z
