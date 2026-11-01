# TMDB - KDramas (2022)

Korean TV Series listed on TMDB

## Context

This dataset is focused on Korean TV series available on The Movie Database (TMDB) and has been built using TMDB's official API, available for everyone to use. Its documentation can be found at the following [link](https://www.themoviedb.org/documentation/api).

## Main content
- series.csv:  file containing all the series, tried my best to scrape all non-translated series or data

If a series ["name"] was not translated to english, I completely removed all that series data. If other data (e.g., synopsis, keywords) regarding that particular series was not translated, I simply set the data to null.

## Additional content

All the following files are completely based on the data within *series.csv*. What this essentialy means is that the main file contains certain columns (e.g., genres, directors, cast, etc..) which are made up of IDs. Instead of putting everything in one single big file, I decided to split the data into different ones. 

- genres.csv: All the genres associated with the series
- networks.csv: All the networks (providers) associated with the series 
- people.csv: All the people associated with the series. I collected **only the series main cast and directors**
- production_companies.csv: All the production companies associated with the series

## Acknowledgements

TMDB is a "community built movie and TV database". The official site is [https://www.themoviedb.org/](https://www.themoviedb.org/).

출처: Kaggle (robertonacu/tmdb-kdramas-2022)
태그: movies and tv shows, korea
라이선스: CC0: Public Domain
수정일: 2022-11-15T14:45:39.293Z
