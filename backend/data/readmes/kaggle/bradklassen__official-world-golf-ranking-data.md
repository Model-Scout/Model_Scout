# Official World Golf Ranking Data

Official World Golf Ranking Data (Week 51)

# Official World Golf Ranking Data
***

**Context:**

The Official World Golf Ranking is a system for rating the performance level of male professional golfers. It was started in 1986. [[1]](https://en.wikipedia.org/wiki/Official_World_Golf_Ranking)

The rankings are based on a player's position in individual tournaments (i.e. not pairs or team events) over a "rolling" two-year period. New rankings are produced each week. During 2018, nearly 400 tournaments on 20 tours were covered by the ranking system. All players competing in these tournaments are included in the rankings. In 2019, 23 tours will factor into the world rankings. [[1]](https://en.wikipedia.org/wiki/Official_World_Golf_Ranking)

The World Ranking Points for each player are accumulated over a two year “rolling” period with the points awarded for each tournament maintained for a 13-week period to place additional emphasis on recent performances. [[2]](http://www.owgr.com/about)

Ranking points are then reduced in equal decrements for the remaining 91 weeks of the two year Ranking period. Each player is then ranked according to his average points per tournament, which is determined by dividing his total number of points by the tournaments he has played over that two-year period. [[2]](http://www.owgr.com/about)

There is a minimum divisor of 40 tournaments over the two year ranking period and a maximum divisor of a player’s last 52 tournaments. [[2]](http://www.owgr.com/about)

Simply put, a golfer's World Ranking is obtained by dividing their points total by the number of events they have played, which gives their average. Players are then ranked; a higher average yields a higher rank. [[1]](https://en.wikipedia.org/wiki/Official_World_Golf_Ranking)
***

**Data:**

- The data was acquired from the Official World Golf Ranking website.

- Stored in a long data format.

- This file will be updated weekly after the conclusion of every tournament.
***

**Tours Included in the Rankings:**

- PGA Tour

- European Tour

- Asian Tour (not a charter member of the Federation)

- PGA Tour of Australasia

- Japan Golf Tour

- Sunshine Tour

- Korn Ferry Tour

- Challenge Tour

- PGA Tour Canada

- Golf Tour

- Korean Tour

- PGA Tour Latinoamérica

- Asian Development Tour

- PGA Tour China

- Alps Tour

- Nordic Golf League

- PGA EuroPro Tour

- ProGolf Tour

- MENA Golf Tour

- Big Easy Tour

- China Tour

- All Thailand Golf Tour

- Professional Golf Tour of India

- Abema TV Tour
***

**Collection Method:**

- Acquired the data using the Python library BeautifulSoup. Manipulated data using the Pandas & NumPy libraries.
***

**Contents:**

- 9000 players
***

**Acknowledgements:**

- Data scraped from: [Official World Golf Ranking](http://www.owgr.com/ranking)

- Please formally reference this Kaggle dataset.

- Please contribute analysis and findings as a kernel.
***

**Inspirations:**

- Can this dataset be used to predict who will win upcoming PGA Tour tournaments?

- Can we predict the players that will make the tournament cuts?
***

**Disclaimer:**

The Official World Golf Ranking website contains plenty of messy data in the 'Name' column. There are still records where there is not enough information for me to infer the proper name of the athlete. If the name contains a date within brackets it is because there are two players with the same name. The date is the birth date of the athlete and is used to uniquely identify athletes with the same name.
***

**Questions, Concerns & Suggestions:**

- Feel free to email me for questions, concerns or suggestions, bradklassen@outlook.com
***

**Resources**

[1] https://en.wikipedia.org/wiki/Official_World_Golf_Ranking


[2] http://www.owgr.com/about

출처: Kaggle (bradklassen/official-world-golf-ranking-data)
태그: video games, golf, sports, computer science, programming, data visualization, feature engineering, news, email and messaging
라이선스: CC BY-NC-SA 4.0
수정일: 2020-04-22T23:29:38.447Z
