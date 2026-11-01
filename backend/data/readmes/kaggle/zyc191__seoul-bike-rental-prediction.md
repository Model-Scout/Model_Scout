# Seoul Bike Rental Prediction

Predict Number of bikes to be made available for renting, from the given dataset

**Data Set Information**
Currently, Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern.
The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes. The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour, and date information.

**Dataset Attributes**

****Identifiers****
- Id - The Unique Integer Id for every entry in both sets

****Other columns****
- Date - dd/mm/yyyy String for Date
- Hour - int, Hour of the day
- Temperature - Temperature in Degree Celsius
- Humidity - % of Humidity
- Wind_Speed - Wind Speed in m/s
- Visibility - Visibility in 10m range
- Dew_Point - Dew Point Temperature in Degree Celsius
- Solar_Radiation - Solar Radiation in MJ/m^2
- Rainfall - Rainfall in mm
- Snowfall - Snowfall in mm

****Categorical Columns****
- Season - Winter, Spring, Summer & Autumn
- IsHoliday - 1/0 for Holiday/No Holiday for Public Holidays from the South Korean Public Holidays List
- IsFunctioningDay - 1/0 for Yes/No to Whether the Hour in the entry is a functioning hour (work hour) of the day or not.

****Target Column****
- Bikes_Rented - Number of Bikes Rented in the Hour of the Day with Specified parameters.

출처: Kaggle (zyc191/seoul-bike-rental-prediction)
태그: cycling, retail and shopping
라이선스: Unknown
수정일: 2021-01-12T03:53:48.273Z
