# 공공데이터 추천 골든셋

서비스 아이디어나 데이터 요청을 받았을 때 공공데이터(서울 열린데이터광장, 공공데이터포털) 추천이 맞는 데이터셋을 올리는지 보는 평가셋이다. 질의마다 후보를 사람이 0/1/2점으로 판정해 정답을 만든다. 모델 골든셋(`test/golden/`)의 판정 배치와 같은 방식이다.

> 상태 (2026-11-05): 질의 58개·후보 696행에 **Codex 카드 기반 1차 판정**을 기록하고 `labels/public_data_golden.jsonl`을 생성했다. 2점 103행, 1점 221행, 0점 346행, 보류(?) 26행이다. 현재 변환기 기준 57개 채점 가능, p040은 보류다. 최종 합의 라벨은 아니며 ?·1점은 추가 확인한다. 질의별 답안과 판정 기준은 [1차 판정 결과](reports/public_judgment_review.md)를 본다.

## 폴더 구성

```text
test/public_data/
├── README.md
├── build_public_pool.py              질의 → 판정 후보 풀
├── judging.py                        풀 → 워크시트(export), 2차 후보 추가(extend), 판정 → 라벨(import)
├── labels/
│   ├── public_data_queries.jsonl     질의 58개. 사람이 편집하는 원본
│   └── public_data_golden.jsonl      워크시트에서 생성한 1차 정답 라벨. 직접 수정하지 않음
└── reports/
    ├── public_pool.json              후보 풀과 판정용 정보 (pool_sources 포함)
    └── public_pool_worksheet.csv     판정 워크시트. score·reason·note 열을 채운다
```

## 질의 유형

| 유형 | 수 | 의미 |
|---|---:|---|
| `service_idea` | 18 | 서비스 아이디어만 있고, 필요한 데이터는 추론해야 함 ("주차장 찾는 앱") |
| `direct_lookup` | 9 | 데이터 이름이나 항목을 직접 지칭함 ("아파트 실거래가 데이터"). 제목만 맞춰도 찾을 수 있는 기본 동작 확인용 |
| `constrained` | 19 | 지역·제공 방식(API/파일)·실시간·상업 이용 조건이 hard 조건 |
| `ai_data` | 7 | AI 기능의 학습 데이터나 RAG 코퍼스로 쓸 공공데이터 (법령·판례, 민원 텍스트, 기상 관측 시계열) |
| `abstention` | 5 | 공공 카탈로그에 없을 것으로 보는 요청 (개인 신용정보, 해외 주식 시세 등) |

`constrained` 19개의 조건 분포는 지역 8, API 6, 파일 3, 실시간 5, 상업 4다(한 질의에 조건이 여럿일 수 있음). 실시간 조건은 `direct_lookup`의 p015·p016에도 있다.

분야는 15개다. 교통물류 11, 환경기상 7, 문화관광 6, 농축수산 5, 사회복지·재난안전 4, 식품건강·보건의료·산업고용·교육 3, 국토관리·공공행정·법률·재정금융 2, 통일외교안보 1.

질의 필드:

- `conditions`: `region`(서울·대구 등, 없으면 전국), `delivery`(`api`/`file`/`any`), `realtime`, `commercial`
- `aspects`: 정답이 담아야 할 항목. 판정자가 참고하는 기준이고 채점에는 쓰지 않는다
- `pool_terms`: 후보를 모을 때 쓰는 검색어. 평가에서는 planner의 `dataset_terms` 역할로 그대로 넘긴다(아래 한계 참고)
- `expected_behavior`: `recommend` 또는 `abstain`

## 후보 풀

`build_public_pool.py`는 하이퍼그래프의 공공데이터 엔티티 10,973개(서울 1,723, 공공데이터포털 9,250)에서 후보를 뽑는다. 서울 데이터는 자치구판·번역판이 이미 하나로 묶여 있고, 출처 간 중복은 엔티티의 `duplicates`에 남아 있다. 판정한 id 하나는 그 사본까지 함께 맞힌 것으로 친다.

랭커를 번갈아 하나씩 골라 12개를 채운다.

- `bm25`: 제목 + 카드 텍스트에 질의 문장과 `pool_terms`로 BM25. 형태소 분석기가 없어서 한글은 글자 2-gram으로 쪼갠다
- `title`: 제목에 들어 있는 `pool_terms` 개수
- `region`: 지역 조건이 있는 질의에서, 그 지역 데이터만 따로 모은 줄. 이게 없으면 전국·타지역 데이터가 풀을 먼저 채운다
- `dense`: `embeddings.npy`와 `OPENAI_API_KEY`가 둘 다 있을 때만 추가된다. 지금 풀은 이 랭커 없이 만들었다

조건으로 미리 거르지 않는다. 조건에 안 맞는 후보는 0점과 그 이유로 판정해야 `must_exclude`가 생긴다. 후보는 고정 seed로 섞어서 보여 주고, 어느 랭커가 뽑았는지는 워크시트에 넣지 않는다.

**풀 크기를 12개로 둔 이유.** 핵심 검색어가 제목에 들어간 데이터만 세도 어린이집 44개, 버스 74개, 학교 208개처럼 대부분의 질의에서 관련 데이터가 풀보다 훨씬 많다. 풀을 20개로 늘려도 다 담지 못하고 판정량만 두 배가 된다. 대신 평가에서 미판정을 따로 다루고(아래 "평가"), 추천기가 실제로 올린 미판정 데이터만 2차로 판정한다.

## 판정

```bash
python test/public_data/build_public_pool.py     # 질의를 고쳤을 때만
python test/public_data/judging.py export        # 워크시트 생성 (이미 있으면 --force 필요)
```

`reports/public_pool_worksheet.csv`를 엑셀이나 구글 시트에서 열고 `score`, `reason`, `note`를 채운다. 696행이라 한 행에 30초씩 잡아도 5~6시간이 걸리니 질의 단위로 나눠 맡는다.

| 점수 | 기준 |
|---|---|
| 2 | 질의 그대로 답이 됨 (주제·지역·제공 방식·이용 조건이 다 맞음) |
| 1 | 쓸 수는 있지만 부분적임 (필요한 데이터 중 하나, 해당 지역을 포함하는 전국 데이터, API를 원했는데 파일, 오래된 판) |
| 0 | 쓸 수 없음. `reason`에 `off_topic` / `wrong_region` / `wrong_delivery` / `license` / `stale` 중 하나를 적는다 |
| ? 또는 빈칸 | 카드만으로는 판단할 수 없음 |

경계 사례는 판정 전에 이렇게 정해 둔다.

- **주제는 맞지만 질의가 원하는 것이 아니면 0 `off_topic`.** 예: "영상 조회수·댓글" 질의에 외교부 유튜브 채널 목록, "해외 실시간 시세" 질의에 국내 주식시세, "어린이집 위치" 질의에 어린이집 통계.
- **해당 지역을 포함하는 전국 데이터는 1점.** 0점이 아니다. 예: 대구 정류소 질의에 전국 정류소 표준데이터.
- **실시간 질의에 주기 파일이나 통계 데이터는 0 `wrong_delivery`.**
- **상업 질의에 상업 이용을 막는 라이선스는 0 `license`.** 공공누리 제2·4유형은 비상업 조건이다. 라이선스 칸이 비어 있으면 원문 페이지를 확인하거나 `?`로 둔다.
- **Claude가 1차 판정을 하는 경우,** 1점은 후하게 주는 경향이 있으니 1점 행은 사람이 다시 본다.

```bash
python test/public_data/judging.py import        # → labels/public_data_golden.jsonl
```

라벨 변환 규칙:

- 2점과 1점은 등급이 붙은 정답(`relevant`)이 된다.
- 0점 중 `wrong_region`·`wrong_delivery`·`license`는 `must_exclude`, 나머지는 `judged_irrelevant`가 된다.
- 2점이 하나도 없으면 1점짜리를 정답으로 쓰고 `answer_grade: "acceptable_only"`로 표시한다. 1·2점이 하나도 없으면 `evaluable: false`이므로 `pool_terms`를 보강해서 풀을 다시 만든다.
- `abstention` 질의에 1·2점이 나오면 카탈로그에 그 데이터가 있다는 뜻이다. 자동으로 고치지 않고 경고만 출력하니, 질의 문장을 고치거나 `recommend`로 옮긴다.

### 2차 판정

1차 라벨이 생긴 뒤 키가 있는 환경에서 평가를 한 번 돌리면, top 10에 나왔지만 판정되지 않은 데이터가 파일로 나온다. 이것을 워크시트 끝에 붙여 판정하고 다시 `import`한다. 이미 있는 행과 점수는 건드리지 않는다.

```bash
python 22_eval_recommendations.py --public --unjudged-out test/public_data/reports/unjudged.jsonl
python test/public_data/judging.py extend test/public_data/reports/unjudged.jsonl
python test/public_data/judging.py import
```

## 평가

```bash
python 22_eval_recommendations.py --public
```

`17_recommend_graph.py`가 서비스 데이터를 찾는 것과 같은 방식으로 호출한다. 호출 형태는 `rank_datasets(dataset_terms, 질의 임베딩, roles=["service"], keywords=dataset_terms)`이다. 지역 조건은 keyword로, 상업 조건은 `commercial_only`로 넘긴다.

지표는 P@10, R@10, MRR, nDCG@10(0/1/2 등급)이고, 각각 두 번 계산한다.

- **raw:** 미판정 데이터를 오답으로 친다. 풀이 작으면 실제보다 낮게 나온다.
- **condensed:** 미판정 데이터를 순위에서 빼고 계산한다(`retrieval_lab/condensed_eval.py`와 같은 Sakai 방식). 미판정에도 판정된 것과 같은 비율로 정답이 있다고 가정하므로 높게 치우친다.
- **judged@10:** top 10 중 판정된 비율이다. 이 값이 낮고 raw와 condensed가 크게 갈리면 2차 판정이 필요하다.

top 10에 든 `must_exclude` 수도 함께 보고한다. 추천기에는 아직 빈 결과를 내는 경로가 없어서, abstention 질의는 top 10에 판정된 데이터가 몇 개 섞였는지만 따로 보고한다.

**OpenAI 키와 dense 인덱스(또는 Supabase)가 필요하다.** 공공데이터 엔티티에는 task 개념이 없어서, `rank_datasets`는 dense 유사도가 없으면 공공데이터를 하나도 반환하지 않는다. 키가 없으면 0점이 아니라 실행 불가로 봐야 한다.

## 한계와 알려진 문제

- **delivery·realtime 조건은 추천기에 넘기지 않는다.** `rank_datasets`에 이 조건을 받는 인자가 없기 때문이다. 지금은 판정자가 0 `wrong_delivery`를 줘서 `must_exclude`로만 반영된다. 추천기에 필터를 넣을지, 판정으로만 볼지는 팀에서 정해야 한다.
- **필요한 항목을 다 덮었는지는 보지 않는다.** p001(위치+요금+운영 시간)이나 p004(경로당+복지관+급식소)처럼 여러 데이터가 필요한 아이디어도 하나만 맞으면 정답으로 친다. `aspects`를 기준으로 한 coverage 지표는 아직 없다.
- **데이터 추천만 평가한다.** `docs/index.html` 계획의 "AI 필요도" 판단과 정답 모델 ID는 이 골든셋에 없다.
- **검색어가 같아서 keyword 점수가 유리하다.** 평가에서 `dataset_terms`로 `pool_terms`를 그대로 쓰는데, 풀을 만들 때 쓴 검색어와 같다. planner가 실제로 뽑는 `dataset_terms`로 바꾸려면 `17_recommend_graph.py`의 plan 단계를 질의마다 돌려 결과를 저장해야 한다.
- **풀은 dense 랭커 없이 만들었다.** 2차 판정이 이 공백을 메운다.
- **지역 판별에 오류가 있다.** `hypergraph_search.dataset_regions`는 제목에 들어 있는 지역명을 그대로 찾는다. 그래서 "소상공인 **경기**동향(BSI)"이 경기도 데이터로 잡힌다. 수원도시공사처럼 기관명에만 지역이 있는 데이터는 `전국`으로 나온다. 둘 다 추천기의 지역 보너스에도 똑같이 영향을 준다.
- **p040은 경계 사례다.** "전국 민간 주차장 실시간 잔여 면수"를 묻는데, 서울·대전·공항의 실시간 주차 데이터가 일부 있다. 판정에서 1점이 나오면 질의를 고친다.

## 변경 기록

**2026-11-05: 1차 피드백 반영**

- p015·p016은 질의에 "실시간"이 있는데 `realtime: false`로 되어 있어 `true`로 고쳤다.
- p025의 `pool_terms`에서 "표준데이터"를 뺐다. 이 단어 때문에 전국교량·하천·카페 같은 무관한 표준데이터가 풀을 채우고 있었다.
- p023(부산 정류소)과 p028(경기 전통시장)은 지역을 각각 대구와 경남으로 바꿨다. 카탈로그에 부산 정류소와 경기 전통시장 전용 데이터가 없어서 정답이 생길 수 없었다. ID는 바꾸지 않았다.
- p044~p058 15개를 추가했다. 날씨·특보·중기예보, 실시간(지하철·대기오염·도매시장 경매), 파일(도서관·학교), 상업 이용(어린이집·관광지), API(영양성분), 교육(대학 학과·등록금·장학금), 해외 여행경보, 기상 관측 시계열을 다룬다.
- 평가에 condensed 지표와 judged@10을 넣고, 2차 판정용 `--unjudged-out`과 `judging.py extend`를 추가했다.


**2026-11-05: 카드 기반 1차 판정**

- CSV의 score·reason·note만 채우고 질문·조건·후보·행 순서를 보존했다. 외부 API 응답과 라이선스를 전수 확인한 판정은 아니다.
- 실시간/정적, 위치/집계, 지역 범위, 명시적 파일/API 필수 조건을 구분했다. p026의 제1유형 한정 조건도 문장대로 적용했다.
- 불명확한 후보는 ?로 남겼다. p040과 반입물량/가격 설명 혼재 항목은 원문 명세 확인이 필요하다.
- public_judgment_decisions.jsonl에 1차 판정 근거를 보존하고 public_judgment_review.md에 질의별 정답·보류 목록·활용 순서를 정리했다. 이후 수정 원본은 CSV다.
