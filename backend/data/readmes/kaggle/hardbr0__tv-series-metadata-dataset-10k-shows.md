# TV Series Metadata Dataset — 10K Shows

Explore 10,000 TV series with ratings, popularity, countries, languages etc.

# TV Series Metadata Dataset — 10K Shows

## Overview

This dataset contains metadata for **10,000 television series** from different countries and languages. It provides information about TV shows including their original titles, English/international names, descriptions, popularity scores, audience ratings, number of votes, original language, country of origin, release dates, and adult-content classification.

The dataset is useful for exploring trends in television content, analyzing audience ratings and popularity, studying international TV production, and building recommendation or analytics systems.

## Dataset Size

* **Rows:** 10,000
* **Columns:** 11
* **Data Type:** Structured tabular data
* **Domain:** Television / Entertainment / Media Analytics

## Columns

| Column              | Description                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | Unique identifier assigned to each TV series.                                                                                                |
| `origin_country`    | Country or countries associated with the original production of the TV series. Examples include US, GB, KR, JP, FR, DE, etc.                 |
| `original_language` | Original language code of the TV series, such as `en` for English, `ko` for Korean, `ja` for Japanese, `fr` for French, and `de` for German. |
| `original_name`     | Original title/name of the TV series in its native language.                                                                                 |
| `overview`          | Short textual description or synopsis of the TV series.                                                                                      |
| `popularity`        | Popularity score associated with the TV series. Higher values indicate greater popularity within the source data.                            |
| `first_air_date`    | Original date on which the TV series first aired.                                                                                            |
| `name`              | Main/international name of the TV series, generally representing the commonly recognized title.                                              |
| `vote_average`      | Average audience rating received by the TV series.                                                                                           |
| `vote_count`        | Number of votes/ratings contributing to the average rating.                                                                                  |
                                                        |

## Example Records

The dataset contains internationally recognized TV series from a wide range of countries and languages.

Examples include:

* **Reacher** — United States, English
* **The Mentalist** — United States, English
* **Sesame Street** — United States, English
* **Coronation Street** — United Kingdom, English
* **Kamen Rider** — Japan, Japanese
* **REBORN!** — Japan, Japanese
* **Lioness** — United States, English
* **Radio Star** — South Korea, Korean
* **Tomorrow Is Ours** — France, French
* **Tagesschau** — Germany, German

The dataset also contains reality shows, talk shows, dramas, news programs, animated series, and other television formats.

## Key Characteristics

### International Coverage

The dataset includes TV series originating from multiple countries and regions. This makes it suitable for analyzing differences in television production across countries and languages.

### Popularity Information

The `popularity` column provides a numerical measure that can be used to identify highly popular TV series and study relationships between popularity and other attributes.

### Audience Ratings

The combination of `vote_average` and `vote_count` makes it possible to analyze audience reception.

For example, researchers can investigate:

* Which shows have the highest ratings?
* Does a high number of votes correlate with popularity?
* Which countries produce highly rated shows?
* How does rating vary across languages?

### Temporal Information

The `first_air_date` column enables analysis of television trends over time, including changes in production and popularity across different years and decades.

### Textual Information

The `overview` column contains descriptions of the TV series, making the dataset suitable for Natural Language Processing (NLP) applications such as text classification, similarity analysis, clustering, and recommendation systems.

## Potential Applications

This dataset can be used for:

1. **TV Show Recommendation Systems**

   * Recommend similar shows based on titles and descriptions.
   * Develop content-based recommendation systems.

2. **Exploratory Data Analysis**

   * Analyze the most popular TV shows.
   * Identify highly rated series.
   * Study television trends by year, country, and language.

3. **Data Visualization**

   * Visualize TV production by country.
   * Analyze rating distributions.
   * Explore popularity trends over time.

4. **Natural Language Processing**

   * Perform text similarity using `overview`.
   * Build TF-IDF or embedding-based recommendation systems.
   * Cluster shows based on their descriptions.

5. **Machine Learning**

   * Predict popularity or ratings.
   * Classify shows based on available metadata.
   * Build recommendation and ranking models.

6. **Entertainment Analytics**

   * Compare television markets across countries.
   * Study audience engagement.
   * Analyze the relationship between popularity and ratings.

## Data Quality Considerations

Before performing analysis or machine learning, users should consider:

* Checking for missing values in `overview`, `first_air_date`, and other columns.
* Converting `first_air_date` into a proper datetime format.
* Checking for duplicate records.
* Verifying whether `origin_country` contains multiple countries within a single record.
* Examining outliers in `popularity`, `vote_average`, and `vote_count`.
* Considering `vote_count` when interpreting ratings because a high rating based on very few votes may not be as statistically reliable as a similar rating based on thousands of votes.
* Encoding categorical variables such as `original_language` and `origin_country` before applying machine-learning algorithms.

## Important Note About Ratings

`vote_average` should not necessarily be interpreted as an absolute measure of show quality. The number of votes (`vote_count`) should also be considered when comparing shows.

For example, a show with a rating of 9.0 based on 1 vote should not necessarily be considered more representative than a show rated 8.4 based on thousands of votes.

## Dataset Structure

The dataset follows the structure:

**TV Series → Country → Language → Title → Description → Popularity → Release Date → Rating → Vote Count 

This combination of categorical, numerical, temporal, and textual features makes the dataset suitable for a wide range of data-analysis and machine-learning projects.

## Intended Audience

This dataset may be useful for:

* Data analysts
* Data scientists
* Machine learning practitioners
* NLP practitioners
* Students
* Researchers
* Recommendation-system developers
* Entertainment analytics enthusiasts

## Possible Project Ideas

Some projects that can be developed using this dataset include:

* TV Series Recommendation System
* Most Popular TV Shows Dashboard
* Global Television Industry Analysis
* TV Rating Prediction
* Content-Based Recommendation Engine
* TV Show Similarity Search
* Country-wise TV Production Analysis
* Language-wise Entertainment Analysis
* Popularity vs Rating Analysis
* NLP-based TV Show Clustering

출처: Kaggle (hardbr0/tv-series-metadata-dataset-10k-shows)
태그: movies and tv shows, global, intermediate, text
라이선스: CC0: Public Domain
수정일: 2026-09-15T20:51:19.723Z
