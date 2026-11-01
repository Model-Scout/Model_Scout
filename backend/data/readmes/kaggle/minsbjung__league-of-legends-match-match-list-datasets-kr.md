# League of Legends Match & Match list Datasets (KR)

LoL Summoner's Rift crawled game match data (Korean server)

### Context

Crawled using RiotAPI(including MatchAPIv5), RiotWatcher and [LolCrawler](https://github.com/cm8908/LolCrawler).
Saved in and exported from MongoDB database


### Content

Raw data (You may have to preprocess these)
- raw\_match.json, raw_match.csv (190,400 documents)
- raw\_matchlist.json, raw_matchlist.csv (163,022 documents)
Some matchlist documents have their player's tier information

Preprocessed data (csv)
- 0-9999.csv ~ LAST.csv

Preprocessed data were processed using [this code](https://www.kaggle.com/minsbjung/load-data-from-mongodb)
Players only with position(or lane) 'TOP' were recorded in the preprocessed data.

출처: Kaggle (minsbjung/league-of-legends-match-match-list-datasets-kr)
태그: video games, tabular, json
라이선스: Unknown
수정일: 2021-12-01T11:07:26.870Z
