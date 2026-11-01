# South Korean Lottery Numbers

Determining the best numbers to choose in the South Korean Lottery

### Background
The South Korean lottery pays out millions of dollars to the winners. To date, there have been over 1000 draws (1 a week). The numbers are drawn by a vacuum sucking up plastic balls with the winning numbers written on them. Many South Korean citizens speculate that this system is rigged (or at least not 100% fair) because many numbers have been chosen unproportionally.  Is it possible that choosing certain numbers will improve one's chances of winning?

### Data
<ul>
<li><strong>TIME</strong> - The nth lottery draw</li>
<li><strong>NUM1</strong> - Winning number 1</li>
<li><strong>NUM2</strong> - Winning number 2</li>
<li><strong>NUM3</strong> - Winning number 3</li>
<li><strong>NUM4</strong> - Winning number 4</li>
<li><strong>NUM5</strong> - Winning number 5</li>
<li><strong>NUM6</strong> - Winning number 6</li>
<li><strong>BONUS</strong> - Winning bonus number</li>
</ul>


### Additional Info
Per draw, 6 numbers are chosen + 1 bonus number
Of the 6 primary numbers, if at least 3 are correct the ticket is a winner.
The bonus number will add a bonus if 5 out of 6 primary numbers are correct.
The order of the numbers do not matter. They will always be from least-&gt;greatest.

The following needs to be taken into consideration to calculate if your model is making money:
-Each guess of lottery numbers costs about $1 (you can guess an unlimited amount of times)
-If 3 numbers match you win $5 (ie. if you guess 5 times and only one ticket wins, you get your money back)
-if 4 numbers match you win $100
-if 5 numbers match you win $1,000
-if 5 numbers and the bonus number match you win $10,000
-if all 6 numbers are correct you get the jackpot (usually at least $100,000-&gt; $10M)



### Source
https://m.dhlottery.co.kr/

출처: Kaggle (calebreigada/south-korean-lottery-numbers)
태그: computer science, programming, exploratory data analysis, data analytics, tabular, gambling, korea
라이선스: CC0: Public Domain
수정일: 2022-02-27T05:16:41.143Z
