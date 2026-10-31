# LEAGUE of LEGENDS - KR Classic Game Data

KR's Challenger, Grand master, master Top 3 tier 5vs5 classic game data 90000

## INTRODUCTION

A project to collect league-of-legend game records to analyze the factors that affect victory and to predict winning rates based on real-time score fluctuations.

This dataset is the result of the my lol predict project's data pipeline.

## Data

Challenger, Grand master, Master tier 90,500 classic game data(Korea, 2020 - 2019)

Match game list ,Win team record, Lose team record, Win team's stat, Lose team's stat

### Importance Match data field 
- 90,500 row
- gameDuration
- gameVersion
- participants data

To maintain the json structure was saved as .pickle
The csv extension does not preserve the json data type.
and Matchpre.pkl  is preprocessed match data(Use when RAM storage is  lack)
In addition, team information and member stats are stored in a data frame.

출처: Kaggle (shinbg/lol-classic-rank-game-datakrtop-3-tier)
태그: games, video games
라이선스: Other (specified in description)
수정일: 2020-05-23T23:26:50.770Z
