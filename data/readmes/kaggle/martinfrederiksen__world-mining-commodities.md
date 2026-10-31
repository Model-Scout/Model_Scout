# World Mining Commodities

World commodity mining distribution based on country and companies

**About the dataset**

The dataset [world_mining_commodities_clean] (csv file) contains data about mined commodities (65) pr. country (169) during the period 2018-2022.

Additional files:

[116_world_mining_companies_clean] (csv file) could be appended to the dataset file as it contains information about what commodities the 116 companies mine and in which countries they operate. see code for example.

[commodity_info, sheet 1] (xlsx file) could be appended to the dataset file as it contains detailed information about the commodities (mainly elements). see code for example.

********************************

Example code under code or in Github repo: https://github.com/MartinSamFred/WorldMiningCommodities

********************************

**Content (1/3)**
world_mining_commodities_clean file

Column 0 – “country”, includes

'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia-Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Colombia', 'Congo, D.R.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador','Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho','Liberia', 'Libya', 'Lithuania', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Russia, Asia', 'Russia, Europe', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Slovakia', 'Slovenia', 'Solomon Islands','South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'.

Column 1 – “mined_raw_mat”, includes

'Chromium', 'Fluorspar', 'Gypsum', 'Salt', 'Talc', 'Steam Coal', 'Nat. Gas', 'Nickel', 'Copper', 'Petroleum', 'Iron', 'Zinc', 'Gold', 'Silver', 'Baryte', 'Bentonite', 'Diatomite', 'Feldspar', 'Kaolin', 'Phosphates', 'Sulfur', Manganese', 'Diam. (Gem)', 'Diam. (Ind)', 'Molybdenum', 'Aluminium', 'Cadmium', 'Lead', 'Lithium', 'Mercury', 'Boron', 'Perlite', 'Rhenium', 'Cobalt', 'Tantalum', 'Titanium', 'Tungsten', 'Antimony', 'Bauxite', 'Rare Earths', 'Tin', 'Palladium', 'Platinum', 'Magnesite', 'Potash', 'Zircon', 'Coking Coal', 'Lignite', 'Uranium', 'Graphite', 'Oil Shales', 'Arsenic', 'Indium', 'Selenium', 'Bismuth', 'Niobium', 'Vanadium', 'Beryllium', 'Asbestos', 'Vermiculite', 'Tellurium', 'Rhodium', 'Oil Sands*', 'Gallium', 'Germanium'

Column 2 – “unit”: quoted in '(t)', '(Mio m3)', '(kg)', '(ct)'

Column 3,4,5,6 and 7: is the year i.e. 2018, 2019, 2020, 2021 and 2022

********************************

**Content (2/3)**

116_world_mining_companies_clean file

Column 0 – “name”: name of company

Column 1 – “Ticker / Market Capitalization”: ticker and marketcap (could be dropped)

Column 2 – “Project Stage”: states Development, Exploration, Production, Royalty and Streaming (or a combination of there)

Column 3 – “Commodity”: states the commodity or commodities the company mine

Column 4 – “Location”: states the country or countries in which the company mine

Column 5 – “Website”: company website

**Content (3/3)**

commodity_info file (sheet 1)

Column 0 – “commodity”: is the underlying mined commodity

Column 1 – “chemical_composition": chemical formula for the underlying mined commodity

Column 2 – “atomic_no”: atomic no for those commodites that are elements

Column 3 – “periodic_table_group”: group position in the peridic table for those commodites that are elements

Column 4 – “periodic_table_period: period position in the peridic table for those commodites that are elements

Column 5 – “periodic_table_block: block position in the peridic table for those commodites that are elements

Column 6 – “material_sub”: sub categpry in the peridic table for those commodites that are elements

Column 8 – “form”: commodity form i.e. solid or liquid

********************************

**Uses**

Visualization, unit conversion practice, get to know who mines what, put commodities into categories/groups and countries in trade unions etc.

Maybe also some advanced visualization mapping commodity mining and companies.

Practice exercises etc.

********************************

**Disclaimer**

The data and information in the data set provided here are intended to be used primarily for educational purposes only. I do not own any data, and all rights are reserved to the respective owners as outlined in “Acknowledgements/sources”. The accuracy of the dataset is not guaranteed accordingly any analysis and/or conclusions is solely at the user's own responsibly and accountability.

********************************

**Acknowledgements/sources**

All data is publicly available on:

World Mining Data: https://www.world-mining-data.info/

World Bank group: https://www.worldbank.org/

Resourcing Tomorrow: https://resourcingtomorrow.com/

Dataset picture / cover photo: Chris (https://unsplash.com/)

출처: Kaggle (martinfrederiksen/world-mining-commodities)
태그: beginner, data visualization, data analytics, pandas
라이선스: Other (specified in description)
수정일: 2024-12-16T14:02:34.893Z
