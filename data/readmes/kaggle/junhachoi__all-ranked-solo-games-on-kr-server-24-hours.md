# League of Legends- 1 day's worth of solo queue KR 

How do characteristics of LoL ranked games change throughout the day? [24 hours]

This is a compiled list of all Ranked Solo 5v5 games on the League of Legends Korean Server during the course of 1 day (GMT 2022/07/02 00:00:00 to 2022/07/03 00:00:00). In Korean Time  (KST) this translates to 7/02 9AM to  7/03 9AM.

I put together this dataset in the hopes of "profiling" certain timeframes (e.g. Morning to Afternoon, Evening-Night, and Late Night-Morning) with distinguishing characteristics, such as overall mental perseverance, higher clutch abiliity, and general awareness/acuity. As a result, some endpoints normally present in the Match-V5 API (like item build, summonerSpellsCast) have been omitted as they are likely to show negligible variability over the course of the day. 

Python requests module and the Riot API's /lol/match/v5/matches/{matchId} API was used to iterate through a previously compiled list of match Id's that consisted only of ranked solo queue games on the KR server. 
CSV is written with an encoding of cp949 (Windows 949); please read as such- otherwise Korean strings will end up broken.

Data of other complete days of the week are in the works (Friday, Sunday soon!)

출처: Kaggle (junhachoi/all-ranked-solo-games-on-kr-server-24-hours)
태그: video games
라이선스: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
수정일: 2022-07-26T03:10:35.050Z
