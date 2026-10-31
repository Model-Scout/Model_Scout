# Wine Information

Wine Information with nation, varieties, flavor, price, etc

### Context

I don't like wine very much. **I love Soju**
However, while developing a recommendation algorithm, I was looking for useful data, and I chose wine-related data. Since the data was collected on the Korean website, the data standards are in line with Korea.


### Content

This datasets 2 .csv File.
* wine_info.csv contains 31 columns and 21605 rows of wine information.
* cleansingWine.csv based on Wine base notebook .

Data informations.
1) id - wine ID
2) name - wine Name
3) producer - 
4) nation - Country of origin
5) local1 - region1
6) local2 - region2
7) local3 - region3
8) local4 - region4
9) ~ 20) varieties1 ~ varieties12 - wine varieties
21)  type - wine type
22) use - wine use
23) abv - Alcohol by volume
24) degree - Drinking temperature
25) sweet - Sweet rank (score between 1 and 5)
26) acidity - Acidity rank (score between 1 and 5)
27) body - Body rank (score between 1 and 5)
28) tannin - Tannin rank (score between 1 and 5)
29) price - wine price that based on WON **NOT dollars!!** (₩, WON)
30) year - Production year
31) ml - wine Volume (milliliter)


### Acknowledgements

Data was collected on May 24th and preprocessed until May 28th.

Since the data was collected on the Korean website, some countries and regions data includes Korean and English, and the price is in Korean won, not dollars.

### Inspiration

I think that this dataset offers some great opportunities for recommedation models. 
My overall goal is to create a model that can identify the variety, winery, and location of a wine based on a description. 
Pleas upload your creative model and idea !

출처: Kaggle (dev7halo/wine-information)
태그: alcohol, categorical, data visualization, recommender systems, text
라이선스: Data files © Original Authors
수정일: 2021-05-31T06:21:30.420Z
