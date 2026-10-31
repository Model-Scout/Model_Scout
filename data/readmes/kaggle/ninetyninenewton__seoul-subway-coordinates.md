# Seoul Subway Geospatial Data

Coordinates of Seoul subway stations and lines

## Sample
**For sample plot, see `seoul_subway_map.jpg` in the dataset.**
**For sample plot notebook, see `Sample Notebook` in Code.**

## Description
Geospatial data of Seoul metropolitan subway system.   
**Every stations and lines in Seoul(but not Seoul metropolitan area) are covered.** 

## Data
Each station has longitude(float), latitude(float), and shapely POINT object generated from the coordinates.
Each line has shapely MULTILINESTRING(or LINESTRING) object.

Shapely objects can be plotted easily using GeoPandas.
Each pickle files contain GeoDataFrame.

CRS is EPSG:4326.

## Line symbol and corresponding line name
- 1 - 1호선 (Line 1)
- 2 - 2호선 (Line 2)
- 3 - 3호선 (Line 3)
- 4 - 4호선 (Line 4)
- 5 - 5호선 (Line 5)
- 6 - 6호선 (Line 6)
- 7 - 7호선 (Line 7)
- 8 - 8호선 (Line 8)
- 9 - 9호선 (Line 9)
- K2 - 분당선 (Bundang line)
- D - 신분당선 (Shinbundang line)
- K2_ - 수인선 (Suin line)
- I1 - 인천선(인천1호선) (Incheon line 1)
- I2 - 인천2호선 (Incheon line 2)
- K1 - 경의중앙선 (Gyeongui–Jungang Line)
- AREX - 공항철도 (AREX; Airport Railroad Express)
- P1 - 경춘선 (Gyeongchun Line)
- U1 - 의정부경전철 (Uijeongbu line)
- S1 - 우이신설경전철 (Ui-Sinseol Line)
- Y1 - 에버라인(용인경전철) (EverLine)
- K4 - 경강선 (Gyeonggang Line)

## Lines and stations not covered in the data
Note that these are not crucial lines nor stations.
Lines:
- 서해선
- 김포골드  
  
Stations:
- 수인선 일부 구간 (고색 ~ 정왕)
- 공항철도 일부 구간 (인천공항1터미널, 인천공항2터미널)
- 7호선 연장 구간 (산곡, 석남)

출처: Kaggle (ninetyninenewton/seoul-subway-coordinates)
태그: geography, transportation, geospatial analysis, korea
라이선스: CC0: Public Domain
수정일: 2021-05-28T07:49:32.170Z
