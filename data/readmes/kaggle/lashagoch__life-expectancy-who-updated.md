# Life Expectancy (WHO) Fixed

Life Expectancy data is fixed and missing values filled.

Data contains life expectancy, health, immunization, and economic and demographic information about **179 countries** from **2000-2015 years**. The adjusted dataset has **21 variables** and **2.864 rows**.


Data were initially collected from [Kaggle Source](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who).

The dataset had inaccurate data and a lot of values were missing. 

The dataset is completely updated. 

Data about Population, GDP, and Life Expectancy was updated according to World Bank Data. Information about vaccinations for Measles, Hepatitis B, Polio, and Diphtheria, alcohol consumption, BMI, HIV incidents, mortality rates, and thinness were collected from World Health Organization public datasets. Information about Schooling was collected from the Our World in Data which is a project of the University of Oxford.

The data had some missing values. A few **strategies for filling in missing** values were applied.
1. Filling data with the **closest three-year average**. If a specific country had a missing value in any year, the data was filled with the closest three-year average. 
2. Filling data with the **average of the Region**. If a specific country was missing values for all years, the data was filled with the average of the Region (e.g. Asia, Africa, European Union, etc.)

Data is adjusted and the missing values are filled. Countries that were missing more than 4 data columns were omitted from the database. Examples of these countries are Sudan, South Sudan, and North Korea.

The database has one variable that categorizes countries into two groups: **Developed vs Developing** countries. According to World Trade Organization, each country [defines](https://www.wto.org/english/tratop_e/devel_e/d1who_e.htm) itself as “Developed” or “Developing”. Therefore, it is challenging to categorize countries. UN has a [list](https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf) dated 2014 that for analytical purposes classifies countries as developed, in transition, and developing economies. Countries that have economies in transition have similar characteristics to the countries that are categorized as developed or developing countries. Countries have been grouped according to their Gross National Income per capita. As a result, nations were divided into four income groups: high-income, higher-middle-income, lower-middle-income, and low-income. The levels of Gross Domestic Income are set by the World Bank to ensure comparability.

**Data Sources:**
Average life expectancy of both genders in different years from 2000 to 2015: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-birth-(years)](https://bit.ly/3JZeMmu)
Mortality-related attributes (infant deaths, under-five-deaths, adult mortality): https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates
Alcohol consumption that is recorded in liters of pure alcohol per capita with 15+ years old: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol)](https://bit.ly/40sBElC)
% of coverage of Hepatitis B (HepB3) immunization among 1-year-olds: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/hepatitis-b-(hepb3)-immunization-coverage-among-1-year-olds-(-)](https://bit.ly/3TUqljv)
% of coverage of Measles containing vaccine first dose (MCV1) immunization among 1-year-olds: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/measles-containing-vaccine-first-dose-(mcv1)-immunization-coverage-among-1-year-olds-(-)](https://bit.ly/3G2ry2O)
% of coverage of Polio (Pol3) immunization among 1-year-olds: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/polio-(pol3)-immunization-coverage-among-1-year-olds-(-)](https://bit.ly/3M2mTkT)
% of coverage of Diphtheria tetanus toxoid and pertussis (DTP3) immunization among 1-year-olds: [https://www.who.int/data/gho/data/indicators/indicator-details/GHO/diphtheria-tetanus-toxoid-and-pertussis-(dtp3)-immunization-coverage-among-1-year-olds-(-)](https://bit.ly/3nrGD7n)
BMI: https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations
Incidents of HIV per 1000 population aged 15-49: https://data.worldbank.org/indicator/SH.HIV.INCD.ZS
Prevalence of thinness among adolescents aged 10-19 years. BMI &lt; -2 standard deviations below the median: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4805
GDP per capita in current USD: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?most_recent_year_desc=true
Total population in millions: https://data.worldbank.org/indicator/SP.POP.TOTL?most_recent_year_desc=true
Average years that people aged 25+ spent in formal education: https://ourworldindata.org/grapher/mean-years-of-schooling-long-run

출처: Kaggle (lashagoch/life-expectancy-who-updated)
태그: health, social science, demographics, feature engineering, deep learning
라이선스: CC0: Public Domain
수정일: 2023-03-30T03:55:42.597Z
