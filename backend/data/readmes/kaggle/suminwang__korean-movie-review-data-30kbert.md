# Korean Movie Review Data 30k(BERT)

Korean Movie Reviews from 214 Films, Multi-Source Reviews + KOBIS Metadata

1) Dataset Description
This dataset contains approximately 27,000 reviews covering 214 Korean films, collected from WatchaPedia, KinoLights, Naver Movies, and Cine21. It also integrates rich quantitative metadata from KOBIS (Korean Box Office Information System), enabling both text-based sentiment analysis and box-office–oriented studies.

2) Dataset Scope
The collected data focuses on: Korean films in the Romance/Melodrama, Comedy, and Drama genres
Movies released between January 2021 and July 2025

3) Purpose of the Dataset
-Created for educational and research purposes
-Useful for those who want to experiment with Korean-language sentiment analysis, text classification, and film analytics

4) Data Sources
Review Text: WatchaPedia, KinoLights, Naver Movies, Cine21
Quantitative Metadata: KOBIS (Korean Box Office Information System)
https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9d00dd80-4a54-11eb-af9a-4b03f0a582d6

5) Requests and Notes to Users
-Suggestions, improvement ideas, or analytical insights are always welcome.
-If you would like additional metadata or extended collections, feel free to request it.
-I hope this dataset contributes to broader interest in Korean culture, Korean cinema, and Korean-language NLP research.

6) Additional Notes
The sentiment-related columns (neg_score, pos_score, bert_label) were generated using the 'klue/roberta-base' model without task-specific fine-tuning. Therefore, the accuracy may be low.

7) Column Description

review_id : Unique ID assigned to each review

review : Raw, unprocessed review text

rating : User rating score

neg_score : Probability of negative sentiment (from klue/roberta-base)

pos_score : Probability of positive sentiment (from klue/roberta-base)

bert_label : Binary sentiment label (positive / negative) predicted by klue/roberta-base

MOVIE_NM : Movie title

DRCTR_NM : Director name

MAKR_NM : Production company

DISTB_CMPNY_NM : Distributor

OPN_DE : Release date

MOVIE_TY_NM : Movie type

MOVIE_STLE_NM : Movie format/style

NLTY_NM : Country of origin

TOT_SCRN_CO : Total number of screens

SALES_PRICE : Total revenue

VIEWNG_NMPR_CO : Total number of viewers

SEOUL_SALES_PRICE : Revenue in Seoul region

SEOUL_VIEWNG_NMPR_CO : Number of viewers in Seoul region

GENRE_NM : Genre

GRAD_NM : Film rating/classification

MOVIE_SDIV_NM : Movie category / classification

출처: Kaggle (suminwang/korean-movie-review-data-30kbert)
태그: movies and tv shows, text, ratings and reviews, bert, korean
라이선스: CC BY-NC-SA 4.0
수정일: 2025-12-09T05:07:22.147Z
