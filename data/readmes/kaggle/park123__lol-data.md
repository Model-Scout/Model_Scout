# League of Legend(LoL) result, champion dataset

bronze to diamond tier / gold, objects, tower, ... etc

### Context

League of Legends is MOBA game from RIOT.
This data-set is about Rank Game Result of Korea from bronze to diamond(two of them are grade). And the number of data-set is 10,000(rows)

There are two type of data-set
A. *Result of Match(such as gold, kill, death info)* - **match~.csv**
B.*The ratios of damage, gold, kill for specific champions in per match* - **champ folder**

from RIOT API - https://developer.riotgames.com/
### Content
A. Result of Match
*match_15m.csv is state at 15minute
- makeTime : match start time
- ~kill, gold : total team kill, gold
- blue_tower : the number of destroyed blue tower
- gameDuration : (s)

B. The ratios of damage, gold, kill
- ~Ratio : the ratio of ~ in team(5champions)
ex) After game end, total kills of [A,B,C,D,E] is [2,12,2,2,2], the killRatio of B champion is 0.6(12/20)

If you have additional questions, please send mail to 'edwardfdsp@gmail.com'

출처: Kaggle (park123/lol-data)
태그: arts and entertainment, games, video games, standardized testing
라이선스: Unknown
수정일: 2020-09-09T06:01:42.790Z
