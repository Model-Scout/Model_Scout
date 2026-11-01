# COVID-19: Holidays of countries

Holidays of countries in format of Prophet for COVID-19 forecasting

### Context
This research is devoted to the analysis of the impact of holidays on the statistics of confirmed coronavirus diseases.
The Prophet using the [**holidays** library](https://github.com/dr-prodigy/python-holidays) with holidays of countries and their regions.
**As of 30 June 2020, only 62 countries** (some with regions) are available in the holidays library:
&gt; ['AR', 'AT', 'AU', 'BD', 'BE', 'BG', 'BR', 'BY', 'CA', 'CH', 'CL', 'CN', 'CO', 'CZ', 'DE', 'DK', 'DO', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JP', 'KE', 'KR', 'LT', 'LU', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NZ', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'RS', 'RU', 'SE', 'SG', 'SI', 'SK', 'TH', 'TR', 'UA', 'US', 'ZA'] or ['Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belarus', 'Belgium', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China',  'Colombia', 'Croatia', 'Czechia', 'Denmark', 'Dominican Republic', 'Egypt', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Kenya', 'Korea, Republic of', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mexico', 'Netherlands', 'New Zealand', 'Nicaragua', 'Nigeria', 'Norway', 'Pakistan', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Russian Federation', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'Ukraine', 'United Kingdom', 'United States']

I will note at once that the list of available countries in the description of the holidays library contains a lot of mistakes, which I [wrote](https://github.com/dr-prodigy/python-holidays/issues/340#issue-668480961) to the authors.

When I [asked](https://github.com/facebook/prophet/issues/1587#issue-661093141) if this list would expand, the Prophet team [made it clear](https://github.com/facebook/prophet/issues/1587#issuecomment-661982602) that they were waiting for help from the community with holidays library expand.

**As of Jan 2021 (version 8.4.1), 67 countries** (some with regions) are available in the holidays library: a number of data have been refined and countries ['BI', 'LV', 'MA', 'RO', 'VN' - two-letter country codes or alpha_2 of the country (ISO 3166)] added.

Unfortunately, the format of the holidays library is not very suitable for coronavirus problems, as it has a number of disadvantages. First, the names of the countries are given in one word, which makes it difficult for many of them to identify them according to their common names (ISO 3166). It is best that the dataset contains the common name and two-letter abbreviation in English according to ISO 3166 (see [pycountry](https://pypi.org/project/pycountry/)).
Second, the dates are not adapted to the potential impact of the holidays on coronavirus statistics. It is known that after the moment of infection, the active manifestation of symptoms occurs with a delay of 4-10 days, that is a person is likely to get into the statistics on the number of diseases only after 4-7 days. Therefore, it is advisable to use the dates window of impacts:
```
Lower_window = [4, 7]
Upper_window = [7, 10]

```However, the Prophet technology requires 
`Lower_window &lt;= 0`
But my [request](https://github.com/facebook/prophet/issues/1588#issue-661098613) to allow positive numbers in this parameter [was refused](https://github.com/facebook/prophet/issues/1588#issuecomment-661984730) by the Prophet team and [advised](https://github.com/facebook/prophet/issues/1588#issuecomment-661984730) to simply move the dates themselves.
Therefore, it is advisable to shift the holiday dates by 7 days. If the researcher thinks that 7 is too much and enough is 4 days, then he simply indicates "Lower" of the window in -3. Actually, by default, it makes sense to specify parameters:
```
Lower_window = -3
Upper_window = 3

```
If necessary, these settings are easy to change

### Content

This dataset:
1. Contains ISO codes, ISO names (common and official) (ISO 3166) of **70** countries (3 European countries **['Albania' - 'AL', 'Georgia' - 'GE', 'Moldova' - 'MD']** have been added).
2. Contains imported dates from the holidays library for 2020-01-20-2021-12-31 (all countries from holidays library as of Jan 2021), and the same dates, but moved 7 days forward.
3. Holidays of countries that are not in the list of holidays of the library, but which are in the data of the World Health Organization and on which considerable statistics of diseases on coronavirus are already collected.
4. Parameters for Prophet model:
`lower_window, upper_window, prior_scale`
If you find errors, please write to the [Discussion](https://www.kaggle.com/vbmokin/covid19-holidays-of-countries/discussion).

It is planned to periodically update (and, if necessary, correct) this dataset. 

### Acknowledgements

Thanks to the authors of the information resources
* [https://github.com/dr-prodigy/python-holidays](https://github.com/dr-prodigy/python-holidays)
* [https://en.wikipedia.org/wiki/List_of_holidays_by_country](https://en.wikipedia.org/wiki/List_of_holidays_by_country)
about the dates and names of holidays in different countries, which I used.

Thanks for the image to <a href="https://pixabay.com/ru/users/iXimus-2352783/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062659">iXimus</a> from <a href="https://pixabay.com/ru/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062659">Pixabay</a>


### Inspiration

The main task for which this dataset was created is to study the impact of holidays on the accuracy of predicting coronavirus diseases, identifying new patterns, and forming optimal solutions to counteract or minimize its spread.

Tasks that need to be solved to improve this dataset in order to increase the accuracy of modeling the impact of holidays on the number of coronavirus patients:
1) Expanding the list of countries
2) Clarification of holiday dates
3) Clarification of parameters 
`lower_window, upper_window, prior_scale`
they must be unique for each country and each holiday.

Also, it is advisable to carry out similar work for each region of countries, but this will not be done in this dataset.

출처: Kaggle (vbmokin/covid19-holidays-of-countries)
태그: health, time series analysis, holidays and cultural events, travel, covid19
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2021-12-18T22:32:02.033Z
