# (🌇Sunset) Spotify Daily Top 50 Of 63 countries

Daily data pull of official Spotify Top 50 of 63 countries + Global

## Context
I was wondering what songs are in the Top 50 Spotify Country Playlists. Found as much playlists I can, but I may have missed some or even included "non-official Spotify" playlists . In case you know an official Top 50 playlist that I've missed, please let me know via the discussion tab! Thank you!

## Updates
[02 Oct 2023]
- I will be sunsetting this dataset and may create a dataset with smaller # of playlists. The new Spotify rate-implementing algorithm is very restrictive based on my observation, simply getting songs from around 15 playlists will need a cool-down of around 48-60 hours before you can use it again, so for me to get data from 60+ playlists will require a lot of accounts and switching of VPNs to change IP addresses. It is too much work for a hobby/ dataset of mine. I will think be uploading the partial data that I got for Sep 2023 then will create a new one.

[22 Sep 2023]
- Spotify API has recently implemented a new rate-limiting algorithm, Im trying to come up with a workaround on how to get data. Unfortunately, I have lost a few days' worth of data pulls, but rest assured Im working on a solution. Thank you.

[31 Aug 2023]
- Added Aug 2023 daily top 50 playlists

[31 Jul 2023]
- Added Jul 2023 daily top 50 playlists

[07 Jul 2023]
- I've added 2 additional gzip files inside each folder, one containing the lyrics with timestamps of the song, then another is the lyrics as well but as a whole. Take note though, not all songs have available lyrics from https://spotify-lyric-api.herokuapp.com/

[31 Jan 2023]
- I am now putting the 3 gzip files inside a folder with YYYYMM format for easier organization.

[Dec 2022]
- I added Afghanistan, Latvia, Lithuania, and Uruguay for the month of Dec 2022

## Monthly Dataset contains 5 compressed files
- Daily data of country playlist (track total followers)
- Daily data of tracks of all playlists (track song performance)
- Song Lyrics per song with timestamps
- Song Lyrics per song
- Metadata and properties of tracks for the whole month (danceability, speechiness, etc)


## Documentation of fields
- https://developer.spotify.com/documentation/
- https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track
- https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist

## Update frequency
I will update this monthly 

## Daily data pull of the "OFFICIAL" Spotify Top 50 Playlists of the following countries
- Afghanistan, Argentina, Australia, Austria, Belgium, Bolivia, Brazil, Canada, Chile, Colombia, Costa Rica, Denmark
, Ecuador, Estonia, Finland, France, Germany, Global, Greece, Guatemala, Hong Kong, Hungary,Iceland
, India, Indonesia, Ireland, Israel, Italy, Japan, Latvia, Lithuania, Luxembourg, Malaysia, Mexico, Morocco, Netherlands
, New Zealand, Nicaragua, Norway, Panama, Peru, Philippines, Polska, Portugal, Romania, Saudi Arabia
, Singapore, Slovakia, South Africa, South Korea, Spain, Suriname, Sweden, Switzerland, Taiwan, Thailand, Turkey
, UAE, Ukraine, United Kingdom, Uruguay, USA, Vietnam, Zimbabwe

출처: Kaggle (bwandowando/daily-spotify-top-50-of-60-countries)
태그: arts and entertainment, music, tabular
라이선스: CC0: Public Domain
수정일: 2023-08-31T05:21:43.160Z
