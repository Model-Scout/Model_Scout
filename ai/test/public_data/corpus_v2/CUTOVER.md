# 공공데이터 코퍼스 v2 전환 전 남은 작업

작성 2026-11-08, 갱신 2026-11-10 · 브랜치 `fix/public-dedup-documents` · 이 문서는 계획이며 운영에는 아무것도 연결하지 않았다.

## 지금 상태

| 항목 | 값 |
|---|---|
| enrich_id (18_enrich 산출물) | `2c3ff48782af57f5…` (`data/public_enriched/build_manifest.json`) |
| corpus_id (13 산출물) | `6571282e4113b7dd…` (`data/hypergraph_v2/build_manifest.json`) |
| documents_id (14 산출물) | `37026bd248c19ea0…` (`data/dataset_index_v2/build_manifest.json`) |
| 고정 데이터 버전 | `data_version 37026bd248c19ea0` ([data_version.json](data_version.json), 커밋 `3bc43f97`에서 생성, 미커밋 변경 없음) |
| 검증 | `python public_v2_pipeline.py --verify-pin` (보완·그래프·문서 기록, 품질 검사, 고정 버전 일치) |
| 임베딩 | 로컬에만 있음(2026-11-08). 41,149행, `text-embedding-3-small`. 새로 임베딩 17,317개, DB 재사용 23,827개. `vectors_sha256 f99e9dca…` (`data/dataset_index_v2/manifest.json`의 `embedding_run`). 평가 질의 벡터 72개는 `query_vectors.jsonl`에 있음 |
| 운영 반영 | 하지 않음. 13·14 기본값과 `dataset-refresh.yml`은 v1 그대로 |

### 실험용 스냅샷 (팀 공통 기준)

- **기준 스냅샷:** `documents_id 37026bd248c19ea0`. 골든셋 라벨 초안은 `golden_prep/batch3/labels_llm_v5.jsonl`(sha256 `c1708cd4…`)이다. 공공데이터 검색 비교는 이 스냅샷과 v5 라벨로 한다. v4(`batch2/labels_llm_v4.jsonl`, sha256 `d3dbc93d…`)는 이력으로만 보존한다.
- **알려진 오류:** 서울 페이지의 갱신주기 칸이 비어 있으면 파서가 다음 항목 본문까지 읽는다(예: OA-22483). 판정은 갱신 주기 표기를 근거로 쓰지 않으므로 라벨에는 영향이 없다. 다만 검색 문서 본문에는 그 값이 들어 있다. 파서를 고치면 `documents_id`가 바뀌고 다시 임베딩해야 하므로, 고친 버전은 새 스냅샷으로 따로 고정한다.
- **Git에 없는 산출물:** 아래 네 폴더는 `.gitignore` 대상이라 PR을 받아도 생기지 않는다. 다시 수집하면 포털 값이 바뀌어 같은 ID가 나오지 않으므로, 빌드한 사람의 폴더를 그대로 받아야 한다.

  | 폴더 | 크기 | 내용 |
  |---|---:|---|
  | `ai/data/public_catalog/` | 7.5 MB | 공식 페이지 조회 캐시 |
  | `ai/data/public_enriched/` | 30 MB | 보완 산출물 |
  | `ai/data/hypergraph_v2/` | 55 MB | 그래프 |
  | `ai/data/dataset_index_v2/` | 175 MB | 검색 문서, 벡터, 평가 질의 벡터 |

- **받은 뒤 확인:**
  1. `python public_v2_pipeline.py --verify-pin`: 고정 버전 일치를 확인한다.
  2. `python 22_eval_recommendations.py --public test/public_data/corpus_v2/golden_prep/batch3/labels_llm_v5.jsonl --corpus v2`: 첫 줄의 `documents_id`가 위 값인지 본다. v2를 쓸 때 벡터 검사(`check_vectors`)도 함께 통과해야 한다.

### 공식 조회 캐시의 확인 방식 (고정 버전 기준)

| `official.verification` | 행 수 | 뜻 |
|---|---:|---|
| `compat` | 15,073 | 2026-11-08 조회 결과를 재파싱 없이 호환으로 인정한 것. 원래 파서 버전(기록 없음 = `null`)과 확인 시점을 그대로 둔다. 근거는 `data/public_catalog/official_meta_migrations.json`, 이관 스크립트는 [migrate_official_cache.py](migrate_official_cache.py). 30일 만료가 그대로 적용돼 2026-12-08까지 실제로 다시 조회된다 |
| `fetched` / `reparsed` | 0 | 현재 파서로 받은 값 / 저장된 원문을 현재 파서로 다시 읽은 값. 앞으로의 조회는 원문을 `official_raw/`에 저장하므로, 파서가 바뀌면 다시 받지 않고 재파싱한다 |
| 확인 안 됨 (`unchecked`) | 84 | 첫 조회의 "missing" 결과. 이관하지 않았고 다음 온라인 실행에서 조회한다 |

호환 근거로 쓴 대조 결과: 2026-11-05~06에 저장해 둔 공식 페이지 74개를 현재 파서로 다시 읽어 캐시 값과 비교했다.

| 결과 | 페이지 수 |
|---|---:|
| 완전히 같음 | 39 |
| "데이터 갱신일"만 다름 (이틀 사이 실제 갱신) | 34 |
| 서비스 지연 안내 페이지라 조회 실패로 분류됨 | 1 |

이용허락·탭·첨부 파일·갱신 주기가 다른 페이지는 없었다.

### 수집기 캐시 정책 (`18_collect`)

| 캐시 | 기본 (워크플로) | `public_v2_pipeline.py --collect` |
|---|---|---|
| 포털 목록 | 있으면 재사용 | `--refresh-lists`: 매번 새로 받음 |
| 서울 필드 목록 | 새 ID만 조회 | `--renew-fields`: 목록 행이 바뀐 항목, 30일 지난 항목, 받은 시점을 모르는 항목을 실행당 300개까지 다시 조회. 바뀐 항목을 먼저, 그다음 오래된 순. 실패하면 기존 값 유지 |
| 서울 라이선스, data.go.kr 라이선스 | 새 ID만 조회 | 그대로 (v2는 보완 단계가 공식 페이지를 직접 조회) |

서울 목록에는 컬럼 변경 날짜가 없다. 그래서 변경 감지는 목록 행의 해시(조회수 같은 카운터 제외)로 하고, 컬럼만 바뀐 경우는 30일 주기 재조회로 잡는다.

**운영 워크플로에서 발견한 것 (고치지 않음):** `dataset-refresh.yml`은 `ai/data/public_catalog` 캐시를 복원하고 목록 파일을 지우지 않는다. 그래서 주간 수집도 처음 받은 목록을 계속 재사용하고 있을 가능성이 높다. 워크플로를 v2로 전환할 때 `--refresh-lists --renew-fields`를 함께 넣는다.

### 임베딩·로컬 평가 준비 상태

| 항목 | 상태 |
|---|---|
| 임베딩 대상 | v2 청크 41,149개, 고유 텍스트 41,144개. 이 중 23,827개는 v1과 같은 텍스트라 재사용할 수 있다. 새로 임베딩할 것은 17,317개로, 공공데이터 청크 전부다(카드에 줄이 추가됨) |
| 예상 비용 | 약 898만 토큰(cl100k 기준), `text-embedding-3-small` 약 0.18달러 |
| 재사용 경로 | 로컬 v1 `embeddings.npy`가 없어 `14 --embed`가 Supabase에서 v1 벡터를 텍스트 해시로 읽어 온다(읽기 전용). DB에 연결되지 않으면 41,144개를 전부 새로 임베딩한다 |
| 실행 명령 | `python public_v2_pipeline.py --verify-pin` 다음에 `python 14_build_dataset_chunks.py --corpus v2 --embed` |
| documents_id 유지 | 임베딩 여부는 문서 ID에 들어가지 않는다. 문서 내용과 임베딩 모델이 같으면 임베딩 전후 ID와 고정 버전이 그대로다. 임베딩 실행 기록은 `dataset_index_v2/manifest.json`의 `embedding_run`(시각, 로컬·DB 재사용 수, 새로 임베딩한 수, 벡터 파일 해시)에 따로 남는다 |
| 벡터 연결 확인 | `corpus_manifest.check_vectors`: 벡터 기록의 `documents_id`, 모델, 청크 순서, `embeddings.npy` 해시가 모두 지금 문서와 맞아야 한다 |
| 검색 모듈 코퍼스 선택 (1-1 일부 완료) | `MODEL_SCOUT_CORPUS=v1/v2` 또는 `hs.use_corpus()`로 그래프·청크·벡터·질의 임베딩 모델을 함께 바꾼다. 기본값은 v1이고, v1 동작(Supabase 폴백 포함)은 그대로다. v2는 `check_corpus`와 `check_vectors`를 통과해야 쓸 수 있고, Supabase로 넘어가지 않는다. 확인에 약 30초가 걸리며 프로세스당 한 번 한다 |
| 평가 | `22_eval_recommendations.py --public --corpus v2`. 결과 첫 줄에 코퍼스, `corpus_id`, `documents_id`를 출력한다. `test/public_data/build_public_pool.py`는 아직 `--corpus` 인자가 없다(기본값을 따름) |
| 아직 안 한 것 (1-1 나머지) | `15`·`16`·`20`·`deploy.sh`의 경로 선택, v2 전용 DB 테이블·RPC |
| 라벨 | 기존 라벨은 그대로. high 28행 검토와 구 단위·언어판·연도판 질의 추가가 남아 있다(1-5) |

v1과 v2의 데이터셋 ID 관계(로컬 산출물 기준):

- v1의 데이터셋 ID와 청크 ID는 모두 v2에 있다. 지울 ID는 없다.
- 공공데이터 카드 10,973개는 같은 ID로 텍스트가 바뀌고, 새 ID 6,344개가 생긴다.
- `20_sync_dataset_index.estimated_bytes` 추정: v1 215 MB, v2 265 MB(공공데이터+HF+Kaggle 전체). 2026-11-01 실측 v1은 209 MB였다.

## 0. v2 공공데이터 단계와 차단 조건 (2026-11-08 추가)

```
수집 18_collect  →  보완 18_enrich  →  정제 13 --corpus v2  →  문서 14 --corpus v2  →  품질 검사
                    (v2 전용 파일)      보완 기록이 낡으면 중단   그래프 기록이 낡으면 중단    실패 시 exit 1
```

- 한 번에 실행: `python public_v2_pipeline.py` (`--collect`는 API 키로 재수집, `--offline`은 캐시만 사용). 임베딩·DB 반영 단계는 없다.
- **14 실행 전 검증:** 그래프 manifest의 입력·코드·산출물을 모두 다시 해시한다. 그래프를 만든 뒤 원본(수집·보완 파일, README, taxonomy)이나 관련 코드(13, dedup, taxonomy, retrieval_metadata, corpus_manifest)가 바뀌면 문서 생성·임베딩 전에 멈춘다.
- **13 v2 실행 전 검증:** 보완 manifest가 지금의 수집 파일과 맞지 않으면, 즉 새로 수집됐는데 보완을 거치지 않았으면 멈춘다. 그래프 manifest의 `upstream.enrich_id`에 보완 결과를 기록한다.
- **목록 갱신:** `--collect`는 `18_collect --refresh-lists`로 목록만 새로 받는다. 서울 필드·라이선스 같은 개별 항목 캐시는 유지하고, 목록에 새로 나온 ID만 조회한다. `18_collect`의 기본 동작과 `dataset-refresh.yml`은 그대로다.
- **보완 캐시 (`public_catalog/official_meta.jsonl`):** 아래 셋이 모두 맞을 때만 재사용하고, 하나라도 다르면 다시 조회한다.
  - 수집 행 `sha`
  - 파서 버전 (`PARSER_VERSION`, 파서 코드 해시라 코드가 바뀌면 자동으로 달라짐)
  - 확인 후 지난 기간 (확인값 30일, 삭제 7일)
  
  캐시에는 확인된 답(`ok`, `deleted`)만 저장한다.
- **재조회 실패:** 직전 확인값을 그대로 쓴다.
  - `official.checked_at`은 그 값을 확인한 시점이다.
  - `official.recheck`에는 이번 조회가 실패한 이유를 남긴다.
  - 확인 이후 행이나 파서가 바뀌었으면 `needs_review`와 사유를 표시한다.
- **상태 구분:**
  - `deleted`: data.go.kr가 "존재하지 않습니다"라고 직접 알린 경우만
  - `failed`: 네트워크 오류, HTTP 오류, 서울 "서비스 지연" 안내 페이지
  - `parse_error`: 페이지는 받았지만 모르는 형태
  - `no_page`: 조회할 주소가 없음
  - `unchecked`: 오프라인이라 조회하지 않음
  
  서울은 삭제 안내가 확인되지 않아, 삭제는 목록에서 빠지는 것으로만 판단한다.
- **품질 검사 (`quality_report.json`):** 아래 중 하나라도 걸리면 실패한다.
  - 수집·보완 행 목록이 다르거나 비어 있음
  - 삭제가 5%를 넘음
  - 조회·해석 문제(확인되지 않은 모든 상태와 재조회 실패)가 2%를 넘음
  - 분류하지 못한 이용허락 문구가 있음
  - 제공 방식 값이 정해진 목록 밖에 있음
  - 엔티티나 카드가 없는 공공데이터가 있음
  
  삭제 목록과 검토 대상은 보고서에 따로 적는다.

### PR-D 보완 결과 (공식 페이지 15,157개 조회, 실패 0)

| 항목 | 수집 | 보완 후 | 원인과 처리 |
|---|---|---|---|
| 이용허락 있음 | 14,101 | 15,147 | data.go.kr는 실제 페이지 종류(openapi·fileData·standard)로 조회한다. 서울은 실패를 "라이선스 없음"으로 캐시하던 문제였다 |
| 이용허락 확인 필요 | 1,056 | 10 | 첫 조회에서 "missing"이던 84개(서울 79, data.go.kr 5). 서울 표본 1건은 삭제가 아니라 "서비스 지연" 안내 페이지였다. 캐시에서 빼서 `unchecked`로 두었고, 다음 온라인 실행에서 다시 조회한다 |
| 상업 이용 판단 변경 | | 1,327행 | 미확인 → 상업 969 · 비상업 48 · 조건부 29. 상업 → 조건부 281: "제3자 권리 포함" 1·3유형 |
| 서울 제공 방식 | 모두 `api` | `api,csv` 5,501 · `api,csv,xlsx` 281 | Sheet 탭(CSV 전체 내려받기)과 첨부 파일 확장자 |
| data.go.kr 파일 목록의 OpenAPI | `json+xml`·`xml`·`json` 342 | `api` | 페이지 주소가 openapi |
| 표준데이터 300 | 모두 `csv,api` | `csv,json,xls,xml` 176 · `csv` 71 · API 포함 46 등 | 형식이 없으면 미확인으로 둔다 |
| 갱신 주기 | 없음 | 15,073 | 카드에 "갱신 주기(포털 표기)"로만 표시한다. 일간·연간 데이터도 "실시간"으로 표기돼 있어 점수·실시간 판정에는 쓰지 않는다 |

이용허락 분류 규칙:
- 비상업(2·4유형, "비영리", "상업적 이용금지")은 다른 조건보다 우선한다.
- 제0유형과 "제3자 권리 포함" 1·3유형은 조건부(원문 확인)로 분류한다.
- "제한 없음"과 "이용제한없음"은 상업 이용 가능으로 분류한다.

**병합해도 v1은 바뀌지 않는다.** `18_collect`와 `dataset-refresh.yml`은 그대로이고, 보완 결과는 v2만 읽는다. v1 수집기의 조회 경로 버그는 v1을 바꾸지 않으려고 남겨 두었다. 정기 워크플로를 전환할 때 `public_v2_pipeline.py`로 바꾼다.

## 1. v2 검색·평가 연결에 필요한 변경

### 1-1. 코퍼스·청크·벡터를 한 번에 고른다

지금은 경로가 파일마다 고정돼 있어 섞일 수 있다.

| 위치 | 지금 | 바꿀 것 |
|---|---|---|
| `hypergraph_search.HYPERGRAPH_DIR`, `DATASET_INDEX_DIR` | v1 고정 | 설정 하나(`MODEL_SCOUT_CORPUS=v1/v2`)로 그래프·청크·벡터 경로를 함께 정한다 |
| `hypergraph_search.dense_scores` | 로컬 `embeddings.npy`가 없으면 Supabase RPC로 넘어간다 | v2 그래프에 v1 벡터가 섞이는 경로다. 로컬 벡터와 DB 벡터 모두 `documents_id`가 맞을 때만 쓰고, 다르면 실패시킨다 |
| `hypergraph_search.embed_query` | `DATASET_INDEX_DIR/manifest.json`의 모델명 사용 | 선택한 코퍼스의 manifest를 읽는다 |
| `14 --embed`의 `manifest.json` | v2일 때 `corpus_id`, `documents_id`를 함께 기록하도록 이번에 추가함 | 로드할 때 `build_manifest.json`과 비교한다 |
| `20_sync_dataset_index.py` | v1 경로 고정, 같은 테이블을 덮어쓰고 없는 ID를 삭제 | v2는 별도 테이블 또는 `corpus_id` 열과 RPC로 올린다. 같은 테이블을 덮어쓰면 올리는 순간 운영 검색이 v2가 된다 |
| `match_model_scout_datasets` (`supabase_dataset_schema.sql`) | 버전 구분 없이 활성 청크 전체 | 코퍼스 버전을 인자로 받거나 v2 전용 함수를 둔다 |
| `15_build_wiki.py`, `16_extract_dataset_ner.py`, `deploy/deploy.sh` | v1 경로 고정 | 같은 설정을 따르게 한다. `deploy.sh`는 `hypergraph/`를 `rsync --delete`로 보낸다 |
| `22_eval_recommendations.py` | `hs`를 통해 v1 | 같은 설정을 쓰고, 결과에 `corpus_id`, `documents_id`를 남긴다 |

**검증 게이트:** 평가·서비스가 시작할 때 `corpus_manifest.check_corpus`를 통과해야 한다. 벡터 manifest의 `documents_id`가 다르면 시작하지 않는다.

### 1-2. 여러 청크를 데이터 단위로 집계한다

지금은 로컬(`np.maximum.at`)과 RPC 모두 **데이터셋별 청크 유사도 최댓값**을 쓴다. v1 공공데이터는 카드만 있어서 최댓값이 곧 카드 점수였다. v2는 공공데이터 1,461개에 필드·지역별 원본 청크가 붙는다.

- **위험:** 필드 이름이 많은 청크가 질의와 우연히 겹쳐 순위가 올라갈 수 있다. `DENSE_MIN 0.40`, `DENSE_ONLY_MIN 0.45`, 상대 하한은 카드만 있던 v1 기준으로 정한 값이다.
- **제안:** 데이터셋 점수는 카드 점수를 기본으로 하고, 다른 청크는 `max(card, section − δ)`처럼 제한해서 더한다. 어느 청크가 맞았는지 결과에 남겨 추천 이유로 쓴다. δ와 하한은 v2 평가로 다시 정한다.
- **확인할 것:** 카드 단독, 최댓값, 위 제안 세 가지를 같은 질의로 비교한다. 결정은 평가 결과를 보고 한다.

### 1-3. 지역은 새 정보와 확인 상태로 판별한다

`keyword_score`는 `dataset_regions`(서울 출처면 서울, 아니면 제목의 지명)를 쓴다. v2 엔티티에는 `coverage_regions`, `coverage_district`, `coverage_status`, `publisher_region`이 있다.

| 범위 판단 근거 | 질의가 지역을 요청했을 때 |
|---|---|
| `stated_in_title` | 일치하면 가산, 다르면 감산 |
| `inferred_from_publisher`, `inferred_from_seoul_portal` | 일치하면 작게 가산, 다르면 작게 감산, 화면에 "추정" 표시 |
| `unknown` | 가산·감산 없음, 화면에 "지역 범위 미확인" 표시. 전국으로 보지 않는다 |
| `coverage_district` | 자치구까지 요청하면 같은 구를 우선한다 |

- `publisher_region`(제공기관 소재지)은 점수에 쓰지 않고 표시에만 쓴다.
- `REGIONS`에 자치구 목록을 넣고, `17_recommend_graph.py`의 decompose가 지역·자치구·기간·언어를 `dataset_terms` 문자열이 아닌 구조화된 값으로 내도록 바꾼다. `22._public_top`도 같은 값을 넘긴다.
- 기간(`period`), 언어판(`language_edition`)도 같은 방식으로 맞는 항목을 우선한다.

### 1-4. 결과 묶기 (별도 변경)

요청한 지역·기간·언어에 맞는 항목을 먼저 고른 뒤, 나머지 같은 `series_id` 항목만 접는다. 조건에 맞는 항목은 접지 않는다. 조건이 없으면 묶음의 기준 항목을 대표로 보여 준다.

### 1-5. 평가

- 정답 대체는 `duplicates`(검증된 동일 데이터)에만 쓴다. 지금 v2 공공데이터 병합은 0건이라 `22._aliases`는 공공데이터에서 아무것도 대체하지 않는다. `series.json`은 평가에 쓰지 않는다.
- 기존 라벨은 그대로 두고, `id_relations.jsonl`과 `golden_review.jsonl`(high 28행)을 사람이 확인한 뒤 새 라벨 파일로 만든다.
- 구 단위·언어판·연도판·공간 단위 질의를 추가해야 v1 대비 효과를 잴 수 있다.
- 비교 순서: v1 ↔ v2를 Pre-retrieval OFF로 먼저 재고, 그다음 Pre-retrieval을 켠다.

## 2. 모델 19개가 운영에서 빠지지 않게 하기

### 사실 관계

| 확인 | 결과 |
|---|---|
| 차이 | 커밋된 v1 그래프는 모델 3,872개(Supabase 기준), 로컬 v2 빌드는 3,853개(로컬 Stage 4 파일) |
| 19개와 데이터셋의 학습 관계 | 0건 (`relations.jsonl`) |
| `20_sync_dataset_index.py` | 데이터셋 테이블(`model_scout_datasets`, `model_scout_dataset_chunks`)만 쓰고 지운다. 모델 테이블은 건드리지 않는다 |
| 모델 비활성화 위치 | `08_sync_supabase.py`만. 전체 모드는 이번 실행에서 보지 못한 모델을 `active=false`로 만든다 |
| 모델 재적재 워크플로 | `model-scout-reingest.yml`은 수동 실행 전용이고, `apply`는 `main`에서 `APPLY` 입력이 있어야 돈다. Stage 2 대량 실패 하한도 있다 |

공공데이터 전환만으로는 운영 DB의 모델 행이 비활성화되지 않는다. 남은 위험은 두 가지다.

1. **그래프에서 빠짐:** 로컬에서 만든 v2 그래프를 `deploy.sh`로 보내면(`rsync --delete`) 서비스 그래프에서 19개 모델이 사라진다. `17_recommend_graph.py`는 그래프에 없는 모델을 건너뛰므로, 그 모델의 데이터셋 추천이 조용히 빠진다.
2. **잘못된 입력으로 08 실행:** 같은 로컬 Stage 4로 `08` 전체 모드를 돌리면 19개가 비활성화된다. 공공데이터 전환과 함께 묶이면 안 된다.

### 방안

**권장: 운영 모델 목록과 같은 입력으로 빌드하고 일치를 검증한다.**

- 전환용 v2 그래프는 CI에서 만든다. CI에는 Stage 4 파일이 없어 `13.load_model_rows`가 Supabase 활성 모델을 읽으므로, 운영과 같은 목록이 된다.
- 게시 전 게이트: `build_manifest.json`의 `counts.model_ids_sha256`, `counts.models`가 그 시점 Supabase 활성 모델 ID 목록의 해시·개수와 같아야 한다. 다르면 게시하지 않는다. `counts.model_source`가 `local_stage4`인 빌드는 게시하지 않는다.
- 전환 PR에는 `08_sync_supabase.py` 실행을 넣지 않는다. 데이터셋 게시는 `20`만 쓴다.

**대안: 공공데이터만 바꾸는 겹쳐 쓰기.**

- 모델 엔티티·링크·관계는 운영 중인 v1 그래프에서 그대로 가져오고, 데이터셋 부분만 v2로 바꾼다.
- 모델 목록이 바뀌는 시점과 전환을 분리할 수 있지만, 그래프를 합치는 코드가 하나 더 생긴다. CI 빌드가 막힐 때만 쓴다.

## 3. 전환 체크리스트

1. high 28행 재검토와 새 질의 추가, 새 라벨 파일 작성
2. v2 임베딩 승인 후 로컬 벡터 생성(`14 --corpus v2 --embed`). DB에는 올리지 않음
3. 1-1의 코퍼스 선택·게이트 구현, v1·v2 로컬 평가(Pre-retrieval OFF)
4. 1-2 집계 방식과 1-3 지역 판별 구현, 재평가
5. v2 전용 테이블·RPC 설계와 `20 --apply` 전 용량 확인(`SUPABASE_DB_BUDGET_MB` 1,024)
6. CI에서 v2 빌드와 모델 목록 일치 게이트 통과
7. 13·14 기본값, `15`·`16`·`20`·`hypergraph_search`·`deploy.sh`를 바꾸고, `dataset-refresh.yml`이 `public_v2_pipeline.py`를 쓰도록 한 PR로 v2 전환
8. 결과 묶기는 별도 PR로 비교. PR-D(보완)는 v2 안에서 켠 것과 끈 것(`PUBLIC_INPUTS["v2"]`를 수집 파일로)을 따로 평가
