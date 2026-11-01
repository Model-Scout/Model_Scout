# Spotify Popular East Asian Artists and Tracks

Top 1000 tracks & top 100 artists from each sections of East Asian music

This dataset consists of two parts which are the top artists and top tracks from 7 different 'query genres' from Spotify API namely **chinese**, **japanese**, **korean**, **k-pop**, **j-pop**, **j-idol** and **j-dance**. Let's explore some East Asian style music!

## **Note:**
- Datasets related to top artists are sorted by number of followers on Spotify
- Datasets related to top tracks are sorted by the popularity metric on Spotify
- Data is extracted using Spotify API, feel free to use the datasets as long as it cope with their term of use
- Some tracks/artists may be duplicated due to them being on two or more query genres
- Inspirations of using the datasets include a EDA analysis on the top tracks and artists, finding sleeper hits/trending music, or just to explore some new taste and music!


## **Features in top track datasets**

1. **song_name**: name of the song
2. **album_name**: the album that the song is in
3. **album_link**: external link to the album of the song on Spotify
4. **artist_name**: name of the artist that produced the song
5. **popularity**: a popularity metric calculated by Spotify, ranging from 0-100 with 100 being the most popular, a song that is popular recently is more likely to have a higher score than a popular song in the past
6. **release_date**: release date of the song
7. **song_link**: external link to the song on Spotify
8. **duration_ms**: duration of song in milliseconds
9. **explicit**: boolean value that indicated if the song is explicit or not
10. **query_genre**: query_genre of the track

## **Features in top artist datasets**

1. **artist_name**: name of the artist
2. **popularity**: a popularity metric calculated by Spotify, ranging from 0-100 with 100 being the most popular
3. **followers**: number of followers of the artist on Spotify
4. **artist_link**: external link to artist page on Spotify
5. **genres**: list of genres that the artist is involved in
6. **top_track**: top track of the artist based on Spotify API
7. **top_track_album**: the album that the top track is in
8. **top_track_popularity**: the popularity of top track; a popularity metric calculated by Spotify, ranging from 0-100 with 100 being the most popular
9. **top_track_release_date**: release date of the top track
10. **top_track_duration_ms**: the duration of the top track in milliseconds
11. **top_track_explicit**: boolean value that indicated if the top track is explicit or not
12. **top_track_link**: external link to the top track on Spotify
13. **top_track_album_link**: external link to the album of the top track on Spotify
14. **query_genre**: query_genre of the artist

출처: Kaggle (crxxom/spotify-popular-east-asian-artists-and-tracks)
태그: arts and entertainment, music, chinese, japanese, korean
라이선스: Other (specified in description)
수정일: 2023-07-22T17:39:23.213Z
