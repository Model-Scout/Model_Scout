## 후속 발화 사례

| 사례 | 마지막 턴 | 기대 | 결과 | 맞음 |
|---|---|---|---|---|
| delivery changed | API 말고 파일로 받을래 | {'delivery': 'file'} | {'delivery': 'file'} | O |
| detail kept | 상업용으로 쓸 거야 | {'region': '충북', 'region_detail': '청주'} | {'region': '충북', 'region_detail': '청주'} | O |
| type1 added, api kept | 공공누리 1유형 데이터만 보여줘 | {'delivery': 'api', 'kogl_type1_only': True} | {'delivery': 'api', 'kogl_type1_only': True} | O |
| csv not from api | 전국 전통시장 목록을 API로 받을 수 있는 데이터 | {'delivery': 'api', 'formats': [], 'region_scope': '전국'} | {'delivery': 'api', 'formats': [], 'region_scope': '전국'} | O |
| file format | 침수흔적도를 SHP 파일로 받고 싶어요 | {'delivery': 'file', 'formats': ['SHP']} | {'delivery': 'file', 'formats': ['SHP']} | O |
| interval not current | 매시간 바뀌는 강수확률 데이터를 알림에 쓰고 싶어 | {'current_value': False} | {'current_value': False} | O |
| current value | 지금 빈자리가 있는 공영주차장을 알려주는 데이터 | {'current_value': True} | {'current_value': True} | O |
## 조건 추출: 명세 `questions_v1` (32문항, 데이터 경로 아님 0)

맞음 40, 누락 0, 잘못 추가 0, 값 틀림 0, 채점 제외 1


세부 지역 보존: h003 O, h004 O, h019 O

## 시간 (초, 분해와 동시에 실행)

| | p50 | p95 | 최대 |
|---|---:|---:|---:|
| 분해 | 1.71 | 2.60 | 2.90 |
| 조건 추출 | 1.30 | 1.92 | 1.94 |
| 둘 다 끝날 때까지 | 1.77 | 2.60 | 2.90 |

조건 추출이 분해보다 늦게 끝난 문항 2/32, 그 때문에 늘어난 시간 합 0.8초
