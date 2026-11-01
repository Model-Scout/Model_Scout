# 빅분기 실기 기출 복원·재구성 6~12회 (작업형 1·2·3유형)

빅데이터분석기사 실기 작업형 1·2·3유형 문제 + 실습 CSV + Python 풀이 노트북 10개

빅데이터분석기사(빅분기) 실기 작업형 1·2·3유형 6~12회 기출 복원·재구성 문제와 실습 데이터(CSV)를 모았습니다.

**빅분기 실기를 혼자 준비하는 분, 특히 파이썬·통계가 처음인 비전공자를 위한 연습 세트입니다.**

6~12회를 응시자 후기로 복원·경향 재구성한 문항 42개와 실습 데이터(csv)를 모았습니다.
문제(`problems.md`)·데이터·회차별 풀이 노트북이 한곳에 있어, 자료를 찾아 헤매거나 파일 경로를 맞추느라 시간을 쓰지 않아도 됩니다.
모두 무료로 쓸 수 있습니다.

Practice problems and synthetic CSV datasets for the practical exam of Korea's Big Data Analysis Engineer certification (빅데이터분석기사, rounds 6-12), reconstructed from test-taker reports.
Each round covers Type 1 (pandas data wrangling), Type 2 (machine-learning modeling with a CSV submission) and Type 3 (hypothesis testing with scipy/statsmodels), with problem statements and worked solution notebooks in Korean.
Free to use under CC BY-NC-SA 4.0.

## 이렇게 활용해 보세요

1. 먼저 노트북은 열지 말고, `problems.md` 와 csv 만으로 직접 풀어 봅니다.
   시험장과 비슷한 환경에서 풀어 보고 싶다면 알고런 실습 환경(https://www.algolearn.io/demo)을 쓰면 됩니다. 막히는 부분은 AI 챗봇 알고봇에게 물어볼 수 있습니다(회원 가입 후에는 https://www.algolearn.io/playground).
2. 막히면 풀이 노트북에서 어떤 코드를 썼는지 확인합니다.
3. 시험장에는 자동완성이 없어서, 외운 코드는 데이터가 조금만 바뀌어도 막히기 쉽습니다.
   그래도 "왜 이렇게 쓰는지"가 보이지 않는다면, 그 부분을 한 줄씩 짚어 주는 영상 해설을 곁들여 보세요.
   - 무료 영상, 12회 풀이: https://youtu.be/IVKGjXo6eYk
   - 무료 영상, 2유형 0점 피하는 법: https://youtu.be/Fh-vv21jGhU
   - 알고런: https://www.algolearn.io/p/LWI99F1C (이 링크로 들어가면 수강 혜택이 적용됩니다)
   - 알고보면 쉬운 빅분기 실기, 파이썬 기초부터 (인프런): https://inf.run/ZKBp5 (이 링크로 들어가면 수강 혜택이 적용됩니다)
   - 실기 기출 풀이 강의 (인프런): https://inf.run/Gr9j7

회차별 풀이 노트북은 아래 표를 참고하세요.

검색어: 빅데이터분석기사 실기 · 빅분기 실기 · 기출 복원·재구성 · 작업형 1유형 2유형 3유형 · bigdata analyst · big data analysis engineer · bigdatakisa · Korea data certification

> **복원·경향 재구성 문항입니다.** 빅데이터분석기사 실기는 공식 기출문제를 공개하지 않습니다.
> 이 데이터셋의 문항은 응시자 후기에서 교차 확인된 출제 신호(도메인·유형·평가지표)를 바탕으로
> 데이터코드 연구소가 복원·재구성한 학습용 문항이며, 데이터는 같은 분포를 흉내 낸 합성 데이터입니다.
> 실제 시험 문제·데이터와 같지 않습니다.

## 구성

| 회차 | 폴더 | 시행일 | 문항 수 | 데이터 파일 |
|---|---|---|---|---|
| 6회 | `round06/` | 2023-06-24 | 6 | `06.01.01-Fire Station Data.csv`<br>`06.01.02-Elementary School Data.csv`<br>`06.01.03-Crime Data.csv`<br>`06.02.01-Metaverse Training Data.csv`<br>`06.02.02-Metaverse Testing Data_x.csv`<br>`06.02.03-Metaverse Testing Data_y.csv`<br>`06.03.01-transport_data.csv`<br>`06.03.02-fish_weight_data.csv` |
| 7회 | `round07/` | 2023-12-02 | 6 | `07.01.01-students_scores.csv`<br>`07.01.02-fish_weight_data.csv`<br>`07.01.03-apartment_prices_dataset.csv`<br>`07.02.01-sales_train_dataset.csv`<br>`07.02.02-sales_test_dataset_x.csv`<br>`07.02.03-sales_test_dataset_y.csv`<br>`07.03.01-gender_prediction_dataset.csv`<br>`07.03.02-used_car_price_dataset.csv` |
| 8회 | `round08/` |  | 6 | `08.01.01.coffee_consumption.csv`<br>`08.01.02.Auto_Sales.csv`<br>`08.01.03.Co_Nmch.csv`<br>`08.02.01.subway_train.csv`<br>`08.02.02.subway_test_x.csv`<br>`08.02.03.subway_test_y.csv`<br>`08.03.01.customer_churn.csv`<br>`08.03.02.piq.csv` |
| 9회 | `round09/` |  | 6 | `09.01.01.bank_loan.csv`<br>`09.01.02.crime.csv`<br>`09.01.03.employees.csv`<br>`09.02.test_x.csv`<br>`09.02.test_y.csv`<br>`09.02.train.csv`<br>`09.03.01.house_price.csv`<br>`09.03.02.insurance_claim.csv` |
| 10회 | `round10/` |  | 6 | `10.01.01.shop_conversion.csv`<br>`10.01.02.delivery_orders.csv`<br>`10.01.03.product_reviews.csv`<br>`10.02.01.electricity_train.csv`<br>`10.02.02.electricity_test.csv`<br>`10.03.01.diabetes.csv`<br>`10.03.02.apartment.csv` |
| 11회 | `round11/` |  | 6 | `11.01.01.employee_salary.csv`<br>`11.01.02.web_traffic.csv`<br>`11.01.03.hospital_visits.csv`<br>`11.02.01.customer_churn_train.csv`<br>`11.02.02.customer_churn_test.csv`<br>`11.02.03.customer_churn_answer.csv`<br>`11.03.01.blood_pressure.csv`<br>`11.03.02.rental_property.csv` |
| 12회 | `round12/` | 2026-06-20 | 6 | `12.01.01.app_event_logs.csv`<br>`12.01.02.store_sales.csv`<br>`12.01.03.machine_sensor.csv`<br>`12.02.01.logistics_train.csv`<br>`12.02.02.logistics_test.csv`<br>`12.02.03.logistics_answer.csv`<br>`12.03.01.exam_scores.csv`<br>`12.03.02.marketing_response.csv` |

각 폴더의 `problems.md` 에는 해당 회차의 문제(풀이 제외)가 들어 있습니다.
회차별 문항은 1유형 3문항, 2유형 1문항, 3유형 2문항입니다.

## 사용법

1. 폴더의 `problems.md` 에서 문제를 읽고 직접 풀어 봅니다.
2. 캐글 노트북에서 `Add Data` 로 이 데이터셋을 연결하면 아래 경로로 파일을 읽을 수 있습니다.

```python
import pandas as pd

df = pd.read_csv('/kaggle/input/datasets/yeshinchoi/bigdata-analyst-practical-exam-6-12/round12/12.01.01.app_event_logs.csv')
```

3. 막히면 풀이 노트북이나 웹 해설로 비교합니다.
   - 6회 `06.01.01-Fire Station Data.csv` 는 인코딩이 cp949 이므로 `encoding='cp949'` 가 필요합니다.
   - 2유형은 train/test(x)/test(y) 구조입니다. test(y)는 채점·검증용 정답 파일입니다.

## 풀이 노트북

| 노트북 | 링크 |
|---|---|
| 6회 풀이 | https://www.kaggle.com/code/yeshinchoi/6-1-2-3-python |
| 7회 풀이 | https://www.kaggle.com/code/yeshinchoi/7-1-2-3-python |
| 8회 풀이 | https://www.kaggle.com/code/yeshinchoi/8-1-2-3-python |
| 9회 풀이 | https://www.kaggle.com/code/yeshinchoi/9-1-2-3-python |
| 10회 풀이 | https://www.kaggle.com/code/yeshinchoi/10-1-2-3-python |
| 11회 풀이 | https://www.kaggle.com/code/yeshinchoi/11-1-2-3-python |
| 12회 풀이 | https://www.kaggle.com/code/yeshinchoi/12-1-2-3-python |
| 2유형 0점 피하는 법 | https://www.kaggle.com/code/yeshinchoi/2-0-type-2-zero-score-guide |
| 1유형 pandas 패턴 | https://www.kaggle.com/code/yeshinchoi/1-pandas-python |
| 3유형 scipy/statsmodels 패턴 | https://www.kaggle.com/code/yeshinchoi/3-scipy-type-3-scipy-patterns |

## 영상 강의·웹 해설

- 무료 영상, 12회 풀이: https://youtu.be/IVKGjXo6eYk
- 무료 영상, 2유형 0점 피하는 법: https://youtu.be/Fh-vv21jGhU
- 영상 해설(알고런, 이 링크로 들어가면 수강 혜택이 적용됩니다): https://www.algolearn.io/p/LWI99F1C
- 알고보면 쉬운 빅분기 실기, 파이썬 기초부터 (인프런, 이 링크로 들어가면 수강 혜택이 적용됩니다): https://inf.run/ZKBp5
- 실기 기출 풀이 강의 (인프런): https://inf.run/Gr9j7
- 웹 해설 전체: https://datacodelab.kr/bigdata/practical/
- 회차별 웹 해설: `https://datacodelab.kr/bigdata/practical/round-N/` (N = 6~12)

## 라이선스

CC BY-NC-SA 4.0 (비영리 · 출처 표시 · 동일 조건 변경 허락). 출처: 데이터코드 연구소(https://datacodelab.kr).

출처: Kaggle (yeshinchoi/bigdata-analyst-practical-exam-6-12)
태그: education, beginner, data analytics, tabular, python
라이선스: CC BY-NC-SA 4.0
수정일: 2026-10-26T14:49:44.807Z
