# All Games Played on LoL KR Server in 24hr Timespan

Columns: Creation Time, gameDuration, gameId, gameMode, queueId

[Update Log]👊
updated 2022-07-25: Added 07/02 data, cleaned up duplicates on 07/01 data.
<a href="https://ibb.co/1nsR1Cb"><img src="https://i.ibb.co/g7vtN06/kaggle-insert.png" alt="kaggle-insert"></a>
Legend Translation: Ranked Solo [blue], ARAM [light blue], Blind Pick [Yellow], Ranked Flex [Red], Co-op vs. AI [Purple], Tutorial [Green]

Brute forcing Match ID's by incrementing matchId param by 1. 
Using Riot API's MATCH-V5 endpoint and the Python requests module, 
3000 match IDs were checked per hour for a non-ghost rate of approximately 0.4. ("non-ghost rate" can be defined as the percentage of total match IDs that returned valid match data. "ghost ID's" were match IDs checked that returned a 404 Not Found.) 
Existing entries were written to .csv for a total of 734,189.
Creation Time is in GMT(+0). Game Duration is in seconds. Queue ID's can be found at https://static.developer.riotgames.com/docs/lol/queues.json.

출처: Kaggle (junhachoi/all-games-played-on-lol-kr-server-in-24hr-timespan)
태그: video games, beginner, text, korea
라이선스: CC BY-NC-SA 4.0
수정일: 2022-07-25T02:16:52.007Z
