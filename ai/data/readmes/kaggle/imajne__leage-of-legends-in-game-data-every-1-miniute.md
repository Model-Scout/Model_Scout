# Leage of Legends in game data every 1 miniute

Total 11274 match data

#Summary
I have collected game data from Korean servers. Data is a match between Diamond, Platinum, and Gold Tier players. The key point of this data is a timeline that shows every 1 min since the game started so that we can analyze the whole game flow.

#Data INFO
Each game has unique gameId. Win value 1 means Blue team win. These data were collected in 2023-12-10 ~ 2023-12-11
```
Index(['1_level', '1_minionsKilled', '1_totalGold', '1_totalDamageTaken',
       '1_totalDamageDone', '1_WARD_PLACED', '1_WARD_KILL', '2_level',
       '2_minionsKilled', '2_totalGold', '2_totalDamageTaken',
       '2_totalDamageDone', '2_WARD_PLACED', '2_WARD_KILL', '3_level',
       '3_minionsKilled', '3_totalGold', '3_totalDamageTaken',
       '3_totalDamageDone', '3_WARD_PLACED', '3_WARD_KILL', '4_level',
       '4_minionsKilled', '4_totalGold', '4_totalDamageTaken',
       '4_totalDamageDone', '4_WARD_PLACED', '4_WARD_KILL', '5_level',
       '5_minionsKilled', '5_totalGold', '5_totalDamageTaken',
       '5_totalDamageDone', '5_WARD_PLACED', '5_WARD_KILL', '6_level',
       '6_minionsKilled', '6_totalGold', '6_totalDamageTaken',
       '6_totalDamageDone', '6_WARD_PLACED', '6_WARD_KILL', '7_level',
       '7_minionsKilled', '7_totalGold', '7_totalDamageTaken',
       '7_totalDamageDone', '7_WARD_PLACED', '7_WARD_KILL', '8_level',
       '8_minionsKilled', '8_totalGold', '8_totalDamageTaken',
       '8_totalDamageDone', '8_WARD_PLACED', '8_WARD_KILL', '9_level',
       '9_minionsKilled', '9_totalGold', '9_totalDamageTaken',
       '9_totalDamageDone', '9_WARD_PLACED', '9_WARD_KILL', '10_level',
       '10_minionsKilled', '10_totalGold', '10_totalDamageTaken',
       '10_totalDamageDone', '10_WARD_PLACED', '10_WARD_KILL', 'time',
       'gameDuration', 'region', 'tier', 'gameId', 'win'],
      dtype='object')
```
1, 2, 3, 4, .... 9, 10 each integer corresponds to lane TOP, JUNGLE, MID, BOTTOM, SUPPORT each blue and red team.

##Quantity
**kr** number of game : 11274


##Recommend 
If you can't open pickle data I recommend you to change pandas version to 2.0.3

출처: Kaggle (imajne/leage-of-legends-in-game-data-every-1-miniute)
태그: games
라이선스: MIT
수정일: 2023-12-11T10:12:54.930Z
