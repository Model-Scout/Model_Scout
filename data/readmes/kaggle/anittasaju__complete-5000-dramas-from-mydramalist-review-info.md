# Complete 5000 dramas from MyDramaList +review info

Complete 5000 dramas from MyDramaList with general + review + reviewer details

### Description
This dataset contains the complete list of the most popular 5000 completed (Drama + Drama Special) of all time from [MyDramaList](https://mydramalist.com/) website (This data was scrapped on May 29th, 2023). The sorting has been done on the popularity index offered by the website and covers drama across multiple countries like South Korea, China, Japan, Thailand, Taiwan, etc.   It gives a comprehensive report of all general details like date of airing, genre, tags, plot summary, cast, etc. and stats like no of reviewers, no of viewers, rating, rank, and popularity along with the total number of positive and negative sentences used in the reviews,  top 10 positive and negative review words as well location and gender info of the reviewers. 

### Inspiration
I am a huge fan of Asian dramas :), and frequently visit MyDramaList for recommendations.  Here, even though the drama may be highly rated, I have a habit of browsing reviews to understand the general context and sentiment of the public before diving into it. As this whole process takes a lot of time, I had the idea to create this dataset that offers people's sentiments along with the drama details. I hope this can be useful to all the drama fans out there :D

### Technical details
This data has been scrapped from MyDramaList website using python's Beautiful Soup module and sentimental analysis has been performed using Hugging Face ["cardiffnlp/twitter-roberta-base-sentiment"](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) model

### Usage:
Finding a new popularity Index
Sentiment analysis 
Demography, sex, tags, genre where the drama is more popular
Popular cast, director, etc.

### Acknowledgment
Many thanks to MyDramaList for providing all this information on a single platform 
And to Hugging Face for the sentiment analysis model

출처: Kaggle (anittasaju/complete-5000-dramas-from-mydramalist-review-info)
태그: movies and tv shows, data cleaning, nltk, transformers, python
라이선스: CC0: Public Domain
수정일: 2023-06-01T01:39:22.127Z
