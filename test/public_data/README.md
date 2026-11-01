# 공공데이터 추천 골든셋

서비스 아이디어나 데이터 요청을 받았을 때 공공데이터(서울 열린데이터광장, 공공데이터포털) 추천이 맞는 데이터셋을 올리는지 보는 평가셋이다. 질의마다 후보를 사람이 0/1/2점으로 판정해 정답을 만든다. 모델 골든셋(`test/golden/`)의 판정 배치와 같은 방식이다.

> 상태 (2026-11-01): 질의 43개와 후보 풀(질의당 12개, 총 516행)까지 만들었다. **아직 판정 전이라 정답 라벨(`labels/public_data_golden.jsonl`)은 없다.**

## 폴더 구성

```text
test/public_data/
├── README.md
├── build_public_pool.py              질의 → 판정 후보 풀
├── judging.py                        풀 → 판정 워크시트(export), 판정 결과 → 라벨(import)
├── labels/
│   ├── public_data_queries.jsonl     질의 43개. 사람이 편집하는 원본
│   └── public_data_golden.jsonl      (판정 후 생성) 정답 라벨. 직접 수정하지 않음
└── reports/
    ├── public_pool.json              후보 풀과 판정용 정보 (pool_sources 포함)
    └── public_pool_worksheet.csv     판정 워크시트. score·reason·note 열을 채운다
```

## 질의 유형

| 유형 | 수 | 의미 |
|---|---:|---|
| `service_idea` | 14 | 서비스 아이디어만 있고, 필요한 데이터는 추론해야 함 ("주차장 찾는 앱") |
| `direct_lookup` | 8 | 데이터 이름이나 항목을 직접 지칭함 ("아파트 실거래가 데이터") |
| `constrained` | 10 | 지역·제공 방식(API/파일, 실시간)·상업 이용 조건이 hard 조건 |
| `ai_data` | 6 | AI 기능의 학습 데이터나 RAG 코퍼스로 쓸 공공데이터 (법령·판례, 민원 텍스트) |
| `abstention` | 5 | 공공 카탈로그에 없을 것으로 보는 요청 (개인 신용정보, 해외 주식 시세 등) |

분야는 공공데이터포털 분류 16개 중 14개(교통물류, 사회복지, 식품건강, 보건의료, 재난안전, 국토관리, 문화관광, 산업고용, 농축수산, 환경기상, 교육, 공공행정, 법률, 재정금융)에 걸쳐 있다.

질의 필드:

- `conditions`: `region`(서울·부산 등, 없으면 전국), `delivery`(`api`/`file`/`any`), `realtime`, `commercial`
- `aspects`: 정답이 담아야 할 항목. 판정자가 참고하는 기준이고 채점에는 쓰지 않는다
- `pool_terms`: 후보를 모을 때 쓰는 검색어. 평가에서는 planner의 `dataset_terms` 역할로 그대로 넘긴다(아래 한계 참고)
- `expected_behavior`: `recommend` 또는 `abstain`

## 후보 풀

`build_public_pool.py`는 하이퍼그래프의 공공데이터 엔티티 10,973개(서울 1,723, 공공데이터포털 9,250)에서 후보를 뽑는다. 서울 데이터는 자치구판·번역판이 이미 하나로 묶여 있고, 출처 간 중복은 엔티티의 `duplicates`에 남아 있다. 그래서 판정한 id 하나는 그 사본까지 함께 맞힌 것으로 친다.

랭커는 아래 셋이고, 번갈아 하나씩 골라 12개를 채운다.

- `bm25`: 제목 + 카드 텍스트에 질의 문장과 `pool_terms`로 BM25. 형태소 분석기가 없어서 한글은 글자 2-gram으로 쪼갠다
- `title`: 제목에 들어 있는 `pool_terms` 개수
- `region`: 지역 조건이 있는 질의에서, 그 지역 데이터만 따로 모은 줄. 이게 없으면 전국·타지역 데이터가 풀을 먼저 채운다
- `dense`: `embeddings.npy`와 `OPENAI_API_KEY`가 둘 다 있을 때만 추가된다. 지금 풀은 이 랭커 없이 만들었다

조건으로 미리 거르지 않는다. 조건에 안 맞는 후보는 0점과 그 이유로 판정해야 `must_exclude`가 생긴다. 후보는 고정 seed로 섞어서 보여 주고, 어느 랭커가 뽑았는지는 워크시트에 넣지 않는다.

## 판정

```bash
python test/public_data/build_public_pool.py     # 질의를 고쳤을 때만
python test/public_data/judging.py export        # 워크시트 생성 (이미 있으면 --force 필요)
```

`reports/public_pool_worksheet.csv`를 엑셀이나 구글 시트에서 열고 `score`, `reason`, `note`를 채운다.

| 점수 | 기준 |
|---|---|
| 2 | 질의 그대로 답이 됨 (주제·지역·제공 방식·이용 조건이 다 맞음) |
| 1 | 쓸 수는 있지만 부분적임 (필요한 데이터 중 하나, 해당 지역을 포함하는 전국 데이터, API를 원했는데 파일, 오래된 판) |
| 0 | 쓸 수 없음. `reason`에 `off_topic` / `wrong_region` / `wrong_delivery` / `license` / `stale` 중 하나를 적는다 |
| ? 또는 빈칸 | 카드만으로는 판단할 수 없음 |

```bash
python test/public_data/judging.py import        # → labels/public_data_golden.jsonl
```

라벨 변환 규칙:

- 2점과 1점은 등급이 붙은 정답(`relevant`)이 된다.
- 0점 중 `wrong_region`·`wrong_delivery`·`license`는 `must_exclude`, 나머지는 `judged_irrelevant`가 된다.
- 2점이 하나도 없으면 1점짜리를 정답으로 쓰고 `answer_grade: "acceptable_only"`로 표시한다. 1·2점이 하나도 없으면 `evaluable: false`이므로 `pool_terms`를 보강해서 풀을 다시 만든다.
- `abstention` 질의에 1·2점이 나오면 카탈로그에 그 데이터가 있다는 뜻이다. 자동으로 고치지 않고 경고만 출력하니, 질의 문장을 고치거나 `recommend`로 옮긴다.

## 평가

```bash
python 22_eval_recommendations.py --public
```

`17_recommend_graph.py`가 서비스 데이터를 찾는 것과 같은 방식으로 호출한다. 호출 형태는 `rank_datasets(dataset_terms, 질의 임베딩, roles=["service"], keywords=dataset_terms)`이고, 지역 조건은 keyword로 넘기며, 상업 조건은 `commercial_only`로 넘긴다. 지표는 P@10, R@10, MRR, nDCG@10(0/1/2 등급), top 10에 든 `must_exclude` 수다. 추천기에는 아직 빈 결과를 내는 경로가 없어서, abstention 질의는 top 10에 판정된 데이터가 몇 개 섞였는지만 따로 보고한다.

**OpenAI 키와 dense 인덱스가 필요하다.** 공공데이터 엔티티에는 task 개념이 없어서, `rank_datasets`는 dense 유사도가 없으면 공공데이터를 하나도 반환하지 않는다. 키가 없으면 0점이 아니라 실행 불가로 봐야 한다.

## 한계와 알려진 문제

- 평가에서 `dataset_terms`로 `pool_terms`를 그대로 쓴다. 풀을 만들 때 쓴 검색어와 같아서 keyword 점수 쪽이 유리하다. planner가 실제로 뽑는 `dataset_terms`로 바꾸려면 `17_recommend_graph.py`의 plan 단계를 질의마다 돌려 결과를 저장해야 한다.
- 풀은 dense 랭커 없이 만들었다. 키가 있는 환경에서 풀을 다시 만들면 BM25가 놓친 후보가 추가될 수 있다. 판정이 끝난 뒤에 다시 만들면 새 후보만 추가로 판정하면 된다.
- `hypergraph_search.dataset_regions`는 제목에 들어 있는 지역명을 그대로 찾는다. 그래서 "소상공인 **경기**동향(BSI)"이 경기도 데이터로 잡힌다(p028 풀에 섞여 있음). 수원도시공사·강남구도시관리공단처럼 기관명에만 지역이 있는 데이터는 `전국`으로 나온다. 둘 다 추천기의 지역 보너스에도 똑같이 영향을 준다.
- p040(전국 민간 주차장 실시간 잔여 면수)은 서울·대전·김포공항의 실시간 주차 데이터가 일부 있다. 판정에서 1점이 나오면 질의를 고친다.
