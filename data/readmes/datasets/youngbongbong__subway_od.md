---
license: other
task_categories:
- tabular-classification
- tabular-regression
language:
- ko
tags:
- subway
- origin-destination
- od-data
- seoul
- metropolitan-area
- transportation
- urban-mobility
pretty_name: Subway Origin-Destination Data
size_categories:
- 10K<n<100K
---

# subway_od

This dataset contains subway origin-destination records for the Seoul metropolitan transit system.  
It supports analysis of station-to-station movement flows and spatial mobility structures.

## Dataset Description

Each record represents aggregated subway travel demand between an origin station and a destination station.  
The dataset can be used to construct OD matrices, analyze inter-station connectivity, and compare subway flows with cell-based population mobility data.

## Number of Elements

- Number of files: add your actual number here
- Number of rows: add your actual total row count here
- Unit of observation: origin station × destination station × date

## Main Columns

- origin_station_id: Origin subway station identifier
- destination_station_id: Destination subway station identifier
- origin_station_name: Origin station name
- destination_station_name: Destination station name
- line_name: Subway line information
- date: Observation date
- passenger_count: Aggregated passenger flow

## Intended Use

This dataset is intended for OD matrix construction, subway flow analysis, and urban transportation demand modeling.

## License

This dataset is derived from public/authorized transportation data.  
Users must comply with the original data provider’s usage policy.

ㄹ사용하시려겨든
thdud041113@g.skku.edu로 메일로 허가 얻으시고 사용해주세요
If you would like to use it, please obtain permission by email at thdud041113@g.skku.edu
 before using it.
