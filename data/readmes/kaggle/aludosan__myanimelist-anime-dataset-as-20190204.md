# MyAnimelist Anime Dataset as 2019/02/04

Contains 15k anime data.

### Context

This is an *unfiltered*  list of animes on the popular site https://myanimelist.net updated in Feb. 04, 2019.
The list contains only animes.

The idea came from https://www.kaggle.com/azathoth42/myanimelist (where there are also users lists) and more details there.
Really, go to Matěj kernel and to his github page to see a really interesting and very graphical analysis.

&gt; Note: All information gathered here are publicly available, there was no need to be registered anywhere to access the data.


### Content
The format is CSV.

See also the descriptions of columns in data descriptions.
Some columns are a little vague and have to be reckeched (e.g. Rank vs. Popularity vs. Favorites).
(That leads to another question - what is the total number of users  / /members?)

RANK (see Wikipedia at : https://en.wikipedia.org/wiki/MyAnimeList)
$$ R = \frac{vS +mC}{v+m} $$
where:
Where *v* stands for the total number of user votes,  *S* for the average user score, *m* for the minimum number of votes required to get a calculated score (currently 50), and *C* for the average score across the entire anime/manga database. Only scores where a user has completed at least 20% of the anime/manga are calculated.


Details below.

    ```
    'animeID'       # anime ID (as in https://myanimelist.net/anime/animeID)
    'name'          # anime title - extracted from the site.
    'title_english' # title in English (sometimes is different, sometimes is missing)
    'title_japanese' # title in Japanese (if Anime is Chinese or Korean, the title, if available, in the respective language)
    'title_synonyms' # other variants of the title
    'type'          # anime type (e.g. TV, Movie, OVA)
    'source'        # source of anime (i.e original, manga, game, music, visual novel etc.)
    
    'producers'     # list of strings: producers, from a longer string extracted above (see code at github)
    'genres'        # list of strings: anime genre; there can be multiple genres.
    'studios'       # list of strings: studio, extracted above (can be multiple studios)

    'episodes'      # number of episodes
    'status'        # aired or not etc. 
    'airing'        # if still airing (True or False)
    'aired'         # dictionary with aired dates
    'duration'      # per episode or the entire duration if movie
    'rating'        # age rating
    'score'         # score 0 to 10 (median score by users)
    'scored_by'     # number of users that scored
    'rank'          # weighted according to some MAL formula (go  there to look for formula)
    'popularity'    # based on how many members/users have the respective anime in their list
    'members'       # number members that added this anime in their list
    'favorites'     # number members that favorites these in their list (I have to recheck it as this is confusing with popularity)
    'synopsis'      # long string with anime synopsis
    'background'    # long string with production background and other things
    'premiered'     # anime premiered on date
    'broadcast'     # when is (regularly) broadcasted
    'related'       # dictionary: related animes, series, games etc.
    
    ```

### Acknowledgements

We wouldn't be here without the help of others. 
The original is here.

https://www.kaggle.com/azathoth42/myanimelist


### Inspiration

Maybe make some recommendations engine?

출처: Kaggle (aludosan/myanimelist-anime-dataset-as-20190204)
태그: popular culture, japan, anime and manga
라이선스: GPL 2
수정일: 2019-02-06T09:40:59.493Z
