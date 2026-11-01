# National Assembly of Korea Minutes Database

Generate insights from National Assembly of Korea data

# 국회 상임위 회의록 데이터

### 데이터 공개 배경

2021년 1학기 Machine Learning and Deep Learning for Data Science 수업 프로젝트 과정에서 정리한 데이터입니다.
공공데이터(http://likms.assembly.go.kr/) 를 활용하였으며 분석의 용이함을 위해서 의원별 참석 회의에서의 발언을 정리하였습니다.
정보 접근성 강화를 통한 시민들의 알권리 향상과 정치 참여 독려를 위해 데이터를 공개했습니다.

### Content

16대부터 21대 5월까지의 상임위원회 회의록 데이터를 활용해서 총 네개의 테이블을 생성하였습니다.
누가(국회의원), 어디서(회의), 무슨 발언을 하였는지 정리하였습니다.
![Alt text](https://i.ibb.co/RzBvsBR/schema.png "ER Diagram")

* 발언을 의원에 mapping하는 과정에서 동명이인으로 인한 오류가 있을 수 있습니다.


### Acknowledgements
MLDL 1조 "NumberOne": 김호원, 김진웅, 고의천, 김도균, 임찬송

### Inspiration
데이터를 토대로 유의미한 분석이 많이 이루어지길 희망합니다. (의원별 관심사 비교 등)

출처: Kaggle (parkseungjoon/national-assembly-of-korea-minutes-database)
태그: government
라이선스: Community Data License Agreement - Sharing - Version 1.0
수정일: 2021-06-05T05:55:37.550Z
