# COVID19 Daily Updates

Daily updates of Coronavirus 2019-nCoV (a.k.a. COVID-19)

### Context

This dataset is a curated version of 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE.

### Content

This is the data repository for the 2019 Novel Coronavirus Visual Dashboard operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). Also, Supported by ESRI Living Atlas Team and the Johns Hopkins University Applied Physics Lab (JHU APL).

### Data processing

From the original source of the data, we perform the following operations:
* Concatenate the daily reports files (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)   
* Add daily update date (as Date field)

* Fix country names duplicates. Multiple countries have duplicate names, ex: `South Korea`, `Republic of Korea`, `Korea, South`.
```
data_df.loc[data_df['Country/Region']==' Azerbaijan', 'Country/Region'] = 'Azerbaijan'
data_df.loc[data_df['Country/Region']=='Czechia', 'Country/Region'] = 'Czech Republic'
data_df.loc[data_df['Country/Region']=="Cote d'Ivoire", 'Country/Region'] = 'Ivory Coast'
data_df.loc[data_df['Country/Region']=='Iran (Islamic Republic of)', 'Country/Region'] = 'Iran'
data_df.loc[data_df['Country/Region']=='Hong Kong SAR', 'Country/Region'] = 'Hong Kong'
data_df.loc[data_df['Country/Region']=='Holy See', 'Country/Region'] = 'Vatican City'
data_df.loc[data_df['Country/Region']=='Macao SAR', 'Country/Region'] = 'Macau'
data_df.loc[data_df['Country/Region']=='Mainland China', 'Country/Region'] = 'China'
data_df.loc[data_df['Country/Region']=='Republic of Ireland', 'Country/Region'] = 'Ireland'
data_df.loc[data_df['Country/Region']=='Korea, South', 'Country/Region'] = 'South Korea'
data_df.loc[data_df['Country/Region']=='Republic of Ireland', 'Country/Region'] = 'Ireland'
data_df.loc[data_df['Country/Region']=='Republic of Korea', 'Country/Region'] = 'South Korea'
data_df.loc[data_df['Country/Region']=='Republic of Moldova', 'Country/Region'] = 'Moldova'
data_df.loc[data_df['Country/Region']=='Republic of the Congo', 'Country/Region'] = 'Congo (Brazzaville)'
data_df.loc[data_df['Country/Region']=='Taiwan*', 'Country/Region'] = 'Taiwan'
data_df.loc[data_df['Country/Region']=='The Gambia', 'Country/Region'] = 'Gambia'
data_df.loc[data_df['Country/Region']=='Gambia, The', 'Country/Region'] = 'Gambia'
data_df.loc[data_df['Country/Region']=='UK', 'Country/Region'] = 'United Kingdom'
data_df.loc[data_df['Country/Region']=='Viet Nam', 'Country/Region'] = 'Vietnam'
```
* Replace missing data in Lat/Long for Province/State and/or Country/Region

```
data_df = pd.DataFrame()
for file in tqdm(os.listdir(db_source)):
    try:
        crt_date, crt_ext = crt_file = file.split(".")
        if(crt_ext == "csv"):
            crt_date_df = pd.read_csv(os.path.join(db_source, file))
            crt_date_df['date_str'] = crt_date
            crt_date_df['date'] = crt_date_df['date_str'].apply(lambda x: datetime.strptime(x, "%m-%d-%Y"))
            data_df = data_df.append(crt_date_df)
    except:
        pass

province_state = data_df['Province/State'].unique()

for ps in province_state:

    data_df.loc[(data_df['Province/State']==ps) & (data_df['Latitude'].isna()), 'Latitude'] =\
                data_df.loc[(~data_df['Latitude'].isna()) & \
                            (data_df['Province/State']==ps), 'Latitude'].median()
    
    data_df.loc[(data_df['Province/State']==ps) & (data_df['Longitude'].isna()), 'Longitude'] =\
            data_df.loc[(~data_df['Longitude'].isna()) & \
                        (data_df['Province/State']==ps), 'Longitude'].median() 

country_region = data_df['Country/Region'].unique()

for cr in country_region:

    data_df.loc[(data_df['Country/Region']==cr) & (data_df['Latitude'].isna()), 'Latitude'] =\
                data_df.loc[(~data_df['Latitude'].isna()) & \
                            (data_df['Country/Region']==cr), 'Latitude'].median()
    
    data_df.loc[(data_df['Country/Region']==cr) & (data_df['Longitude'].isna()), 'Longitude'] =\
            data_df.loc[(~data_df['Longitude'].isna()) & \
                        (data_df['Country/Region']==cr), 'Longitude'].median() 

```
### Acknowledgements

Data source: https://github.com/CSSEGISandData/COVID-19


### Inspiration

Represent the geographical data distribution of 2019-nCoV spread. Represent time series with Confirmed, Recovered, Deaths cases. Analyse the mortality. Try to forecast the evolution of cases. Compare the spread of Coronavirus for different countries, with different policies for social isolation, closing schools, stopping international travels.

출처: Kaggle (gpreda/coronavirus-2019ncov)
태그: healthcare, public health, news
라이선스: Data files © Original Authors
수정일: 2021-02-13T07:55:53.800Z
