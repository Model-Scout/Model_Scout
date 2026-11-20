# 모델 검색 튜닝 — 작업 기록과 검증 순서

운영의 **fan-out 모델 검색**(정훈님 설계도의 `1.b 모델 검색`)을 측정하고 튜닝하기
위한 폴더다. 골든셋 240문항을 만들고, 운영과 같은 점수식으로 1차 가중치 튜닝까지
했다. **골든셋은 아직 정훈님 검수 전이다** — 질문 240개와 사람이 볼 보류 140건을
보고 확정해야 한다.

- **바꾸지 않은 것:** 운영 코드 전부(`09_model_scout_mcp_readonly.py`,
  `17_recommend_graph.py`, `api.py`), Supabase 함수·테이블, GitHub Actions,
  `retrieval_lab`, 기존 골든셋(`test/golden/labels`, `test/golden/v2`)
- **읽기만 한 것:** Supabase(전부 `default_transaction_read_only=on`)
- **외부 API 호출:** OpenAI 임베딩 1회(진단), 분해 242회(gpt-4.1-mini)

## 1. 어디서 시작했나

```
origin/main  cab5907a8  "Merge pull request #55 from Model-Scout/feat/yj"
   └─ exp/model-retrieval-tuning       ← 이 브랜치
```

이전 브랜치(`eval/model-golden-v3`, `eval/retrieval-tuning`)는 쓰지 않는다. 운영
검색이 `retrieval_lab`(BGE-M3 + BM25 + RRF)이 아니라 Supabase RPC
(text-embedding-3-small + ts_rank_cd 선형합)라, 거기서 잰 값은 서비스에 전이되지
않기 때문이다. 백업으로 로컬에 남겨 두었다.

## 2. 무엇을 찾았나

### ① 운영 하이브리드 검색에서 sparse 가 항상 0점이다

`match_model_scout_models` 의 sparse 는 `plainto_tsquery` 를 쓰는데, 이 함수는
모든 단어를 AND 로 묶는다. `search_tsv` 는 영어 메타데이터로만 만든 생성
컬럼이라 한국어 토큰이 사실상 없다.

```
korean      4,017행 (100%)        한국어   27행 (0.7%)
embedding     475행 ( 12%)        임베딩    2행 (0.0%)
translation   522행 ( 13%)        번역      1행 (0.0%)

질의 "한국어 문서 임베딩 embedding retrieval"
  → '한국어' & '문서' & '임베딩' & 'embedding' & 'retrieval'  → 매칭 0행
```

`17_recommend_graph` 가 만드는 질의는 한국어+영어 혼합이라 항상 한국어 토큰이
섞이고, 따라서 sparse 는 언제나 0이다. `09_model_scout_mcp_readonly.py:790-791`
의 `dense_weight=0.65 / sparse_weight=0.35` 는 순위에 아무 영향이 없다 —
지금 검색은 100% dense 전용이다.

`tools/diagnose_sparse.py` 로 언제든 재현한다.

### ② 검색은 사용자 원문을 보지 않는다

```
원문   "음성 인식 모델을 Common Voice 11.0 WER 로 비교하려고 합니다…"
   ↓ decompose(LLM)                     17_recommend_graph.py:466
needs = [{task, purpose_ko, model_query}]
   ↓ search_models(query=need["model_query"])   17_recommend_graph.py:565
검색어 "Common Voice 11.0 WER speech recognition model"
```

그래서 원문을 검색어로 쓰면 운영과 다른 것을 재게 된다. 질문마다 분해를 한 번
돌려 `queries/decompose_cache.json` 에 고정했다.

분해 LLM 은 `gpt-4.1-mini` 를 썼다. 로컬 `.env` 는 ollama/gemma3:4b 이지만
실험용이고 최종은 gpt 라고 확인받았다. 어떤 LLM 으로 만들었는지 캐시의
`__meta__` 에 남아 있다.

### ③ structured_constraint 가 검색을 측정하지 못했다 (만들고 나서 발견)

하드 필터는 랭킹 **전에** 도는 단계다. 통과한 모델을 모두 정답으로 두면 어떤
순서를 내놓아도 점수가 같다. 질의 후보 안에서 다운로드 상위 30%만 2점으로
바꿨다(`scan.POPULAR_FRACTION`).

```
2점 1016 → 283 (중앙 26 → 5)
2점 == eligible 인 질문  40 → 0
```

## 3. 골든셋 240문항

기준 코퍼스는 **Supabase 4,017행**이다(`sync_run cb1b5e48` + `255c1482`,
`model_ids_sha256 3a04b80f…`). 질문 문장은 기존 라벨 178개와 11월 초 폐기한 v3 작업 60개를
참고했고, **정답은 전부 버리고 현재 코퍼스에 전수 스캔으로 다시 매겼다**
(2026-11-14 재적재로 모델이 바뀌었기 때문).

| 유형 | 문항 | 초보 | 2점 | 1점 | 보류 | 채점 방식 |
|---|---:|---:|---:|---:|---:|---|
| benchmark_lookup | 40 | 0 | 186 | 181 | 0 | dataset·metric 정규식 |
| structured_constraint | 40 | 0 | 283 | 1117 | 0 | 하드 필터 + 인기도 상위 30% |
| lexical_exact | 40 | 0 | 55 | 146 | 0 | 모델명 정규식 |
| model_comparison | 40 | 0 | 82 | 461 | 0 | 두 계열 정규식 |
| semantic_capability | 40 | 20 | 389 | 666 | 331 | README 키워드 |
| semantic_constraint | 40 | 15 | 240 | 312 | 180 | README 키워드 + 조건 |
| **합계** | **240** | **35** | **1235** | **2883** | **511** | |

초보 질문 35개는 모델 종류·크기·라이선스를 말하지 않는다. 운영은 분해가 task 를
뽑아 주므로 검색 입장에서는 같은 자리에 들어온다.

```
전문  "커뮤니티 댓글에서 욕설이나 혐오 표현을 걸러내는 한국어 분류 모델이 필요합니다"
초보  "유튜브 댓글이 악플인지 자동으로 걸러내는 걸 만들어보고 싶어요. 뭐부터 시작해야 하나요?"
```

## 4. 파일

```
queries/
  pool.jsonl               참고용 질문 풀 238개(기존 라벨 178 + 폐기한 v3 60).
                           정답은 담지 않는다. v3 디렉터리는 지웠고 질문 문장만
                           여기 남아 있어, collect_questions.py 가 이어받는다
  spec_benchmark.py        40문항 + 채점 규칙
  spec_structured.py       40문항 + 조건
  spec_lexical.py          40문항 + 모델명 정규식
  spec_comparison.py       40문항 + 두 계열
  spec_capability.py       40문항 + 키워드 (초보 20)
  spec_constraint.py       40문항 + 키워드·조건 (초보 15)
  decompose_cache.json     원문 → model_query 242건
tools/
  diagnose_sparse.py       운영 sparse 가 죽어 있음을 재현
  collect_questions.py     질문 풀 수집
  decompose_cache.py       운영 분해를 돌려 캐시
  apply_decomposed_task.py 분해가 뽑은 task 를 HF 태그로 매핑
  fetch_benchmarks.py      Supabase 벤치마크 사본(읽기 전용)
  check_benchmark_notation.py  1점에 다른 벤치마크가 섞였는지
  verify_goldenset.py      골든셋 기계 검증
runs/
  baseline_sparse.json     현재 sparse 상태 기록
```

## 5. 아직 안 한 것

```
보류 511건 1차 판정
평가기 — 운영 수식(dense·sparse 선형합)을 읽기 전용으로 재현
sparse 설계 A/B/C 비교
유형별 튜닝 (5-fold 교차검증 + 부트스트랩 신뢰구간)
```
