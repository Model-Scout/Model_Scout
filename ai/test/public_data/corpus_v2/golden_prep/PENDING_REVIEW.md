# 공공데이터 골든셋: 판정 보류 목록

작성 2026-11-13. 기준 라벨은 `batch3/labels_llm_v5.jsonl`이다. 아래 항목은 카드 정보만으로 판단하기 애매해 일단 보류했다. 나중에 다시 판정할 때 공식 페이지 링크나 README를 근거로 함께 넣는다.

## 1. 원 제공처 확인이 필요한 판정

| 질문 | 데이터 | 현재 | 애매한 점 | 확인할 것 |
|---|---|---|---|---|
| p051 전국 도서관 목록 CSV(API 없이) | data_go_kr/15154373 국립중앙도서관 | 0 (wrong_delivery) | 카드에 API만 있어 0점. 원 제공처에 CSV 내보내기가 있는지 안 봤다 | 파일 다운로드 제공 여부 |
| p051 | data_go_kr/15062509 경남 | 0 (wrong_delivery) | 위와 같음 | 파일 다운로드 제공 여부 |
| p051 | data_go_kr/15095725 제주 공공도서관 | 0 (wrong_delivery) | 판정 메모는 "API만 제공"인데 카드는 file·json. 제주 한정 | JSON 파일을 CSV 질문에 0으로 볼지 1로 볼지, 메모 사유 정정 |
| p002 전기차 충전소 찾기 | data_go_kr/15068376 한국전력기술 | ? | 본사 구내 충전기 15대. 일반인 이용 가능 여부가 없다 | 외부인 개방 여부 |
| p055 영양성분 API 조회 | data_go_kr/15106741 전북 음식보감 | ? | 영양성분이 `GDRUG` 문자열 필드 하나. 수치인지 서술형인지 샘플이 없다 | 인증키로 샘플 조회 |

## 2. v2 검색 결과의 미판정 데이터

v2 top 10에는 골든셋에 판정이 없는 데이터가 남아 있고, 지금은 모두 오답으로 계산된다. v2 빌드가 있는 PC에서 목록을 뽑아 2/1/0/?로 판정한다.

```
python 22_eval_recommendations.py --public test/public_data/corpus_v2/golden_prep/batch3/labels_llm_v5.jsonl --corpus v2 --unjudged-out unjudged_v5.jsonl
```

## 3. pool_terms 누수 (코드 작업)

평가가 질문 원문 외에 골든셋 작성 때 뽑은 검색어(`dataset_terms`)를 검색기에 같이 넘긴다. 질문 원문만 쓰는 모드를 추가해 두 점수를 나란히 보고해야 한다. 판정할 것은 없다.
