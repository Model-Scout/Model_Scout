# [Cleaned] Korean Delivery App Reviews



## 데이터셋 개요 (Dataset Overview)
이 데이터셋은 [cafe_delivery_review]를 기반으로, 한국어 배달앱 리뷰의 감성 분석을 위해 정제하고 3-클래스(긍정/중립/부정) 라벨을 추가한 데이터입니다. 원본 데이터에 존재하는 여러 시트를 통합하고, 복합적인 규칙을 적용하여 라벨을 생성함으로써, 바로 모델 학습에 사용할 수 있도록 가공되었습니다.

## 데이터 정제 및 가공 (Data Cleaning and Processing)
이 데이터셋은 원본 데이터에서 다음과 같은 주요 변경 작업을 거쳤습니다:

데이터 통합 : 분산된 여러 시트의 정보를 단일 시트로 병합했습니다.

라벨링 재설계 : 별점, 리뷰 텍스트, 배달 평가 옵션을 종합적으로 고려하는 규칙을 적용하여, 기존 데이터에 없던 3-클래스(0 : 부정, 1 : 중립, 2 : 긍정) 감성 라벨을 새로 생성했습니다.

컬럼 표준화 : 분석에 용이하도록 컬럼명을 일관성 있게 수정했습니다.

## 원본 데이터 및 저작자 표시 (Attribution and Original Source)

본 데이터셋은 **[COCO-Chanel]**에 의해 CC BY-NC-SA 4.0 라이선스로 공개된 **[cafe_delivery_review]**를 기반으로 생성된 파생 데이터셋입니다.

원본 데이터셋 링크 (Link to Original Dataset) : [https://www.kaggle.com/datasets/sungjunghwan/cafe-review]

## 라이선스 (License)
이 데이터셋은 원본 데이터의 라이선스에 따라 동일한 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) 라이선스를 따릅니다.

따라서 이 데이터셋을 사용할 경우 다음 사항을 준수해야 합니다:

비상업적 (NonCommercial) : 이 자료를 상업적인 목적으로 사용할 수 없습니다.

동일조건변경허락 (ShareAlike) : 이 데이터셋을 리믹스, 변형하거나, 이를 기반으로 새로운 2차 저작물을 만들 경우, 원본과 동일한 CC BY-NC-SA 4.0 라이선스로 배포해야 합니다.

출처: Kaggle (narililly/cleaned-korean-delivery-app-reviews)
태그: 
라이선스: CC BY-NC-SA 4.0
수정일: 2025-09-17T13:57:03.610Z
