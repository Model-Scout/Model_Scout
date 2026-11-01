---
dataset_info:
- config_name: HealthCheckupDataset
  features:
  - name: 기준년도
    dtype: int64
  - name: 가입자 일련번호
    dtype: int64
  - name: 시도코드
    dtype: int64
  - name: 성별코드
    dtype: int64
  - name: 연령대코드(5세 단위)
    dtype: int64
  - name: 신장(5cm 단위)
    dtype: int64
  - name: 체중(5kg 단위)
    dtype: int64
  - name: 허리둘레
    dtype: float64
  - name: 시력(좌)
    dtype: float64
  - name: 시력(우)
    dtype: float64
  - name: 청력(좌)
    dtype: int64
  - name: 청력(우)
    dtype: int64
  - name: 수축기 혈압
    dtype: int64
  - name: 이완기 혈압
    dtype: int64
  - name: 식전혈당(공복혈당)
    dtype: int64
  - name: 총 콜레스테롤
    dtype: int64
  - name: 트리글리세라이드
    dtype: int64
  - name: 콜레스테롤(HDL)
    dtype: float64
  - name: 콜레스테롤(LDL)
    dtype: int64
  - name: 혈색소
    dtype: float64
  - name: 요단백
    dtype: int64
  - name: 혈청크레아티닌
    dtype: float64
  - name: 간기능검사(AST)
    dtype: int64
  - name: 간기능검사(ALT)
    dtype: int64
  - name: 감마지티피
    dtype: float64
  - name: 흡연상태
    dtype: int64
  - name: 음주여부
    dtype: int64
  - name: 구강검진수검여부
    dtype: int64
  - name: 치아우식증유무
    dtype: int64
  - name: 결손치유무
    dtype: int64
  - name: 치아마모증유무
    dtype: int64
  - name: 제3대구치(사랑니)이상
    dtype: int64
  - name: 치석
    dtype: int64
  splits:
  - name: train
    num_bytes: 266402250
    num_examples: 1000000
  download_size: 37961524
  dataset_size: 266402250
- config_name: hp_t20_ds
  features:
  - name: 기준년도
    dtype: int64
  - name: 가입자 일련번호
    dtype: int64
  - name: 진료내역일련번호
    dtype: int64
  - name: 성별코드
    dtype: int64
  - name: 연령대코드
    dtype: int64
  - name: 시도코드
    dtype: int64
  - name: 요양개시일자
    dtype: string
  - name: 서식코드
    dtype: int64
  - name: 진료과목코드
    dtype: int64
  - name: 주상병코드
    dtype: string
  - name: 부상병코드
    dtype: string
  - name: 요양일수
    dtype: int64
  - name: 입내원일수
    dtype: int64
  - name: 심결가산율
    dtype: float64
  - name: 심결요양급여비용총액
    dtype: int64
  - name: 심결본인부담금
    dtype: int64
  - name: 심결보험자부담금
    dtype: int64
  - name: 총처방일수
    dtype: int64
  - name: 데이터 기준일자
    dtype: string
  splits:
  - name: train
    num_bytes: 1925077691
    num_examples: 11727248
  download_size: 354020385
  dataset_size: 1925077691
- config_name: hp_t60_ds
  features:
  - name: 기준년도
    dtype: int64
  - name: 가입자 일련번호
    dtype: int64
  - name: 처방내역일련번호
    dtype: int64
  - name: 일련번호
    dtype: int64
  - name: 성별코드
    dtype: int64
  - name: 연령대코드(5세단위)
    dtype: int64
  - name: 시도코드
    dtype: int64
  - name: 요양개시일자
    dtype: string
  - name: 약품일반성분명코드
    dtype: string
  - name: 1회 투약량
    dtype: float64
  - name: 1일투약량
    dtype: int64
  - name: 총투여일수
    dtype: int64
  - name: 단가
    dtype: float64
  - name: 금액
    dtype: int64
  - name: 데이터 공개일자
    dtype: string
  splits:
  - name: train
    num_bytes: 4503377550
    num_examples: 32870344
  download_size: 666609473
  dataset_size: 4503377550
configs:
- config_name: HealthCheckupDataset
  data_files:
  - split: train
    path: HealthCheckupDataset/train-*
- config_name: hp_t20_ds
  data_files:
  - split: train
    path: hp_t20_ds/train-*
- config_name: hp_t60_ds
  data_files:
  - split: train
    path: hp_t60_ds/train-*
task_categories:
- tabular-classification
- feature-extraction
language:
- ko
tags:
- health
pretty_name: Korean Health Check data
size_categories:
- 10M<n<100M
---

```python
print(health_checkup_ds, hp_t20_ds, hp_t60_ds)
```

```sh
(Dataset({
     features: ['기준년도', '가입자 일련번호', '시도코드', '성별코드', '연령대코드(5세 단위)', '신장(5cm 단위)', '체중(5kg 단위)', '허리둘레', '시력(좌)', '시력(우)', '청력(좌)', '청력(우)', '수축기 혈압', '이완기 혈압', '식전혈당(공복혈당)', '총 콜레스테롤', '트리글리세라이드', '콜레스테롤(HDL)', '콜레스테롤(LDL)', '혈색소', '요단백', '혈청크레아티닌', '간기능검사(AST)', '간기능검사(ALT)', '감마지티피', '흡연상태', '음주여부', '구강검진수검여부', '치아우식증유무', '결손치유무', '치아마모증유무', '제3대구치(사랑니)이상', '치석'],
     num_rows: 1000000
 }),
 Dataset({
     features: ['기준년도', '가입자 일련번호', '진료내역일련번호', '성별코드', '연령대코드', '시도코드', '요양개시일자', '서식코드', '진료과목코드', '주상병코드', '부상병코드', '요양일수', '입내원일수', '심결가산율', '심결요양급여비용총액', '심결본인부담금', '심결보험자부담금', '총처방일수', '데이터 기준일자'],
     num_rows: 11727248
 }),
 Dataset({
     features: ['기준년도', '가입자 일련번호', '처방내역일련번호', '일련번호', '성별코드', '연령대코드(5세단위)', '시도코드', '요양개시일자', '약품일반성분명코드', '1회 투약량', '1일투약량', '총투여일수', '단가', '금액', '데이터 공개일자'],
     num_rows: 32870344
 }))
 ```

### HealthCheckup DS 항목 설명

| 항목명 | 항목명(영문) | 항목설명 | 도메인 분류 | 데이터 타입 | 최대길이 | 단위 | 표현형식 | 정보시스템명 | DB명 | Table명 | 기타 | 코드 | 코드명 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 기준년도 |  | 기준년도 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 가입자 일련번호 |  | 가입자 일련번호 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 시도코드 |  | 시도코드 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 성별코드 |  | 성별코드 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 연령대코드(5세 단위) |  | 연령대코드(5세 단위) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 신장(5cm 단위) |  | 신장(5cm 단위) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 체중(5kg 단위) |  | 체중(5kg 단위) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 허리둘레 |  | 허리둘레 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 시력(좌) |  | 시력(좌) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 시력(우) |  | 시력(우) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 청력(좌) |  | 청력(좌) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 청력(우) |  | 청력(우) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 수축기 혈압 |  | 수축기 혈압 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 이완기 혈압 |  | 이완기 혈압 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 식전혈당(공복혈당) |  | 식전혈당(공복혈당) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 총 콜레스테롤 |  | 총 콜레스테롤 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 트리글리세라이드 |  | 트리글리세라이드 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 콜레스테롤(HDL) |  | HDL콜레스테롤 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 콜레스테롤(LDL) |  | LDL콜레스테롤 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 혈색소 |  | 혈색소 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 요단백 |  | 요단백 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 혈청크레아티닌 |  | 혈청크레아티닌 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 간기능검사(AST) |  | 간기능검사(AST) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 간기능검사(ALT) |  | 간기능검사(ALT) |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 감마지티피 |  | 감마지티피 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 흡연상태 |  | 흡연상태 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 음주여부 |  | 음주여부 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 구강검진수검여부 |  | 구강검진수검여부 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 치아우식증유무 |  | 치아우식증유무 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 결손치유무 |  | 결손치유무 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 치아마모증유무 |  | 치아마모증유무 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 제3대구치(사랑니)이상 |  | 제3대구치(사랑니)이상 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |
| 치석 |  | 치석 |  | 가변문자형(VARCHAR) | 999 |  |  |  |  |  |  |  |  |