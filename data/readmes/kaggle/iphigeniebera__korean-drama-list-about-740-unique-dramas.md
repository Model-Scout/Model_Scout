# Korean drama list [about 1278 unique dramas]

ratings,genres, airing time and more characteristics of 1278+ Korean dramas

dataset is made of 9 files:

1. kdramalist.csv: it a raw file containing all attributes in the dataset. it is normalized into the following files.

2. **actors.csv**: contains drama name and actors.
3. **aired_on.csv**: contains drama name and day a drama was aired on.
4. **genres.csv**:contains drama name and genre.
5. **imdb.csv**:contains drama name and descriptors from imdb. for dramas which were not found from imdb korean tv series list, they were not included. that's why we have only 691 rows in this file.
6. **networks.csv**:contains original tv network drama was first aired on.
7. **platforms.csv**:contains platforms you can watch drama from.
8. **tags.csv**:contains tags associated with drama.
9. **main_descriptors.csv**:contains all other attributes not in genres, imdb,networks,platforms and tags.

I used Beautifulsoup python library to webscrape Wikipedia, mydramalist, and imdb websites.

MyDramalist is a website containing a variety of asian dramas and movies with excellent breadth when it comes to giving drama metadata.
The Internet Movie Database (IMDb) is an online database containing information and statistics about movies, TV shows and video games as well as actors, directors and other film industry professionals. Its popularity means it gives credible ratings as it have large user base.
Wikipedia is a free, open content online encyclopedia created through the collaborative effort of a community of users.

출처: Kaggle (iphigeniebera/korean-drama-list-about-740-unique-dramas)
태그: movies and tv shows, data cleaning, data analytics, korea, python
라이선스: Other (specified in description)
수정일: 2022-08-18T19:01:50.803Z
