# 서울 지하철 승하차 인원 Seoul Metro Usage

Refined metro usage from data.seoul.go.kr 서울 열린데이터 광장 제공. 지하철 승하차 인원 정제 데이터.

서울 열린데이터 광장 및 서울 교통공사 에서 제공한 [서울교통공사 연도별 일별 시간대별 역별 승하차 인원](http://data.seoul.go.kr/dataList/OA-12921/F/1/datasetView.do#) 정보 입니다. csv, xslx 등으로 통일되지 않은 포맷 및 필드들을 동일하게 통일시켰으며, EUC-KR 로 되어 있는 텍스트 인코딩 역시 UTF-8 로 통일해서 다양하게 활용 가능하도록 했습니다.

**seoul-metro-station-info.csv** 데이터가 역 정보에 대한 메타 데이터이며
**seoul-metro-(YYYY).logs.csv** 로그 데이터의 station_code 필드는 seoul-metro-station-info.csv 필드의 station.code 필드에 대입됩니다.

- 서울교통공사 에서 관리하는 구간인 **1~8호선**의 데이터만 담고 있으며, 1호선의 의정부선, 3호선의 고양선 등의 데이터는 포함하지 않습니다.
- 환승역의 경우 개찰구마다 소속된 호선(역 코드)이 있어 통과한 개찰구에 해당하는 호선(역 코드) 정보를 담고 있습니다. 
  예) 합정역의 경우 2호선 개찰구를 통과한 데이터는 `station_code: 238` , 6호선 개찰구를 통과한 데이터는 `statioin_code: 2623` 으로 기록됩니다.

Data provided from [Seoul Open Data](http://data.seoul.go.kr/dataList/OA-12921/F/1/datasetView.do#).
Origin data provided different of format (.xslx) and non-unified encoding (EUC-KR), and everything is converted to .csv and UTF-8 for better usage.

출처: Kaggle (kimjmin/seoul-metro-usage)
태그: categorical, transportation, korea
라이선스: Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)
수정일: 2022-07-02T01:30:47.010Z
