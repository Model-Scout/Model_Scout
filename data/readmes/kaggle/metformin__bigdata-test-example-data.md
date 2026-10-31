# bigdata test example data

Example Dataset of Korean Bigdata Analyst Test

문항 내역
**1. mtcars 데이터셋 (mtcars.csv)의 qsec 컬럼을 최소최대 척도(Min-Max Scale)로 변환한 후 0.5보다 큰 값을 가지는 레코드 수를 구하시오.**

**2. 아래는 백화점 고객의 1년간 구매데이터이다.**
(가) 제공 데이터 목록
① y_train.csv : 고객의 성별 데이터 (학습용), CSV 형식의 파일
② X_train.csv, X_test.csv : 고객의 상품구매 속성 (학습용 및 평가용), CSV 형식의 파일

(나) 데이터 형식 및 내용
① y_train.csv (3,500명 데이터)
* custid: 고객 ID
* gender: 고객의 성별 (0: 여자, 1: 남자)
② X_train.csv (3,500명 데이터), X_test.csv (2,482명 데이터)
**고객 3,500명에 대한 학습용 데이터(y_train.csv, X_train.csv)를 이용하여 성별예측 모형을 만든 후, 이를 평가용 데이터(X_test.csv)에 적용하여 얻은 2,482명 고객의 성별 예측값(남자일 확률)을 다음과 같은 형식의 CSV 파일로 생성하시오.(제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)
**
&lt;제출형식&gt;
custid,gender
3500,0.267
3501,0.578
3502,0.885

&lt;유의사항&gt;
성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리, Feature Engineering, 분류 알고리즘 사용, 초매개변수 최적화, 모형 앙상블 등이 수반되어야 한다.

출처: Kaggle (metformin/bigdata-test-example-data)
태그: computer science
라이선스: Other (specified in description)
수정일: 2021-04-20T13:05:59.050Z
