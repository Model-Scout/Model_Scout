# Air Pollution in Seoul

Air Pollution Measurement Information in Seoul, Korea

### Context
This dataset deals with air pollution measurement information in Seoul, South Korea.
Seoul Metropolitan Government provides many public data, including air pollution information, through the ['Open Data Plaza' ](https://data.seoul.go.kr/)
I made a structured dataset by collecting and adjusting various air pollution related datasets provided by the Seoul Metropolitan Government

### Content
This data provides average values for six pollutants (SO2, NO2, CO, O3, PM10, PM2.5).
- Data were measured every hour between 2017 and 2019.
- Data were measured for 25 districts in Seoul.
- This dataset is divided into four files.

1. **Measurement info**: Air pollution measurement information
  - 1 hour average measurement is provided after calibration
  - Instrument status: 
      - `0`: Normal, `1`: Need for calibration, `2`:  Abnormal
      - `4`: Power cut off, `8`: Under repair, `9`: abnormal data

2. **Measurement item info**: Information on air pollution measurement items

3. **Measurement station info**: Information on air pollution instrument stations

4. **Measurement summary**: A condensed dataset based on the above three data.

### Acknowledgements
Data is provided from here.
- https://data.seoul.go.kr/dataList/OA-15526/S/1/datasetView.do
- https://data.seoul.go.kr/dataList/OA-15516/S/1/datasetView.do
- https://data.seoul.go.kr/dataList/OA-15515/S/1/datasetView.do

Thank you to Seoul City, Seoul Open Data Plaza, and Air Quality Analysis Center for providing data.

출처: Kaggle (bappekim/air-pollution-in-seoul)
태그: earth and nature, environment, pollution
라이선스: CC BY-SA 4.0
수정일: 2020-04-03T16:33:49.063Z
