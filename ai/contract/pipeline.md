# 재적재 파이프라인 — Stage 재설계

[`README.md`](README.md)가 사실의 목록, [`source-map.md`](source-map.md)가 수집
경로를 정한다. 이 문서는 **그 사실을 어느 순서로 만들고, 어디서 멈추는지**를
정한다.

---

## 1. 번호를 바꾸지 않는다

GPT 초안은 `Stage 2A / 2B / 2C`로 쪼개는 안이었다. 이 레포에서는 하지 않는다.

```
08_sync_supabase.incremental_refresh_pipeline()가
  02_enrich_metadata.py → 03_generate_semantic_metadata.py
  → evidence_index.py → 06_extract_benchmark_metadata.py
  → 04_build_embeddings.py
를 파일 이름으로 직접 호출한다.

.github/workflows/model-scout-incremental.yml 도 파일 이름으로 py_compile 한다.
ai/test/golden/v2/tools/corpus_v2.py 는 05_validate_retrieval.hard_filter 를 import 한다.
```

파일을 쪼개면 세 군데가 같이 깨진다. 얻는 것은 이름의 정돈뿐이다.

**대신 `02` 안의 역할을 모듈로 분리한다.** 번호와 호출 관계는 그대로 둔다.

```
02_enrich_metadata.py
  ├─ resolvers/hf_api.py        ← 응답에서 사실을 뽑는다 (판단 없음)
  ├─ resolvers/artifacts.py     ← siblings → 포맷·용량·양자화
  ├─ resolvers/legal.py         ← license_raw → commercial_status, LICENSE 파일
  └─ resolvers/resolve.py       ← 출처 우선순위 적용, status/confidence 부여
```

`ai/backfill/build_delta.py`의 GGUF 로직이 `resolvers/`로 들어간다.
**앞으로 "정규 파이프라인 → 백필"이 아니라, 처음부터 모든 모델이
safetensors·GGUF·config·siblings를 함께 본다.**

---

## 2. 단계

```
Stage 0  Data Contract                        코드 아님. 규약과 검증기
   │     contract/{README,source-map}.md, model-record.schema.json, validate.py
   │
Stage 1  Discovery                            01_collect_models.py
   │     HF list_models → 후보 선정, task·downloads·한국어 후보, canonical 후보
   │     출력: data/hf_models_stage1_*.jsonl
   │
Stage 2  Fact Acquisition + Resolution        02_enrich_metadata.py
   │     ① 획득: api?blobs=true 1회 + README + LICENSE류 + (필요시) config.json
   │     ② 해결: 출처 우선순위 → 값 + status + confidence + source
   │     ③ 기록: provenance.fields 전체. conflict·review_queue 생성
   │     출력: data/hf_models_stage2_*.jsonl
   │
Stage 2.5  Quality Gate                       contract/validate.py  ★신규
   │     스키마 검증 + 값↔상태 정합성 + 품질 하락 검사
   │     실패하면 여기서 멈춘다. Stage 3 LLM 호출과 Stage 4 임베딩 비용을 막는다
   │
Stage 3  Semantic Evidence                    03_generate_semantic_metadata.py
   │     README → LLM 요약·용도·제한, atomic evidence
   │     사실 필드를 만들지 않는다. 설명과 근거만
   │     출력: data/hf_models_stage3_*.jsonl
   │
Stage 3.5  Benchmark                          06_extract_benchmark_metadata.py
   │     model-index + README 표 → quality.results
   │     지금은 sync 시점에 붙어서 Stage 4 파일에 없다. 여기로 옮긴다
   │
Stage 4  Serving Document                     04_build_embeddings.py
   │     embedding_text + filter_metadata 생성, 변경된 문서만 재임베딩
   │     출력: data/hf_models_stage4_*.jsonl
   │
Stage 5  Publish                              08_sync_supabase.py
         dry-run diff → 확인 → apply. run_id·schema_version 기록
```

### 기존과 달라지는 것

| | 기존 | 새로 |
|---|---|---|
| HF 호출 | `model_info` + `config.json`·`tokenizer_config.json`·README 다운로드 | `api?blobs=true` 1회로 대부분 해결. 파일은 누락분만 |
| GGUF | 파일명 패턴으로 `artifacts.gguf` 플래그만 | `gguf.{total, architecture, context_length}`를 1차 출처로 읽는다 |
| `gated`·`sha`·`siblings[].size` | 안 읽는다 | 읽는다 |
| 출처 기록 | 없음 (`model.metadata_status`가 known/unknown만) | `provenance.fields` 전체 |
| 벤치마크 | sync 시점 | Stage 3.5 |
| 적재 전 검증 | `py_compile` + Stage 4 dry-run | **Stage 2.5 계약 검증 게이트** |
| `dtype` | Stage 2에만 있고 Stage 4가 버린다 | `filter_metadata`까지 전달 |

---

## 3. 왜 Stage 2.5가 필요한가

백필 작업에서 실제로 난 사고다.

```python
# rebuild_stage4.py 초기 버전 — Stage 4 문서를 직접 조립했다
document = {"model_id": ..., "embedding_text": ..., "filter_metadata": {...}}
```

`task`·`candidate`·`popularity`·`search_aliases` 등 **12개 키가 빠졌다.**
형식은 유효한 JSON이었고 임베딩도 정상 생성됐다. 그런데 하드 필터가 모든
모델을 탈락시켰다. 비교 결과가 전부 0으로 나온 뒤에야 알았다.

```
비용 순서
  Stage 2  무료 (HF API)
  Stage 3  유료 (LLM)        ← 여기까지 가기 전에 멈춰야 한다
  Stage 4  유료 (임베딩)
  Stage 5  DB 쓰기
```

Stage 2.5는 **유료 단계 앞의 게이트**다. 검사 항목은
[`validate.py`](validate.py)에 있고, 음성 테스트로 심은 위반 4건을 모두 잡는 것을
확인했다.

---

## 4. 전체 재적재 모드가 필요하다

기존 `--refresh`는 **watermark 이후 변경된 모델만** 처리한다.

```python
# 08_sync_supabase.incremental_stage1_update()
scan = incremental_stage1_update(watermark)
processable_ids = set(scan["processable_ids"])   # 변경된 것만
```

스키마가 바뀐 첫 적재에는 쓸 수 없다. **변경되지 않은 모델도 새 필드가
비어 있기 때문이다.** `gated`·`sha`·`siblings[].size`는 기존 값이 있는 모델에도
없다. 변경 기준으로 고르면 그 셋을 영원히 못 채운다.

그래서 `--reingest`를 만들었다.

| 모드 | 대상 | HF 호출 | LLM | 임베딩 | DB |
|---|---|---|---|---|---|
| `--refresh` | watermark 이후 변경분 | 변경분 | 변경분 | 변경분 | upsert |
| `--reingest` | **전체** | 전체 1회 | README 변경분 | `document_hash` 변경분 | upsert |

### 전수로 도는 것은 무료 단계뿐이다 — 실측

| 단계 | 전수로 돌면 | 실제로 돌아가는 것 | 근거 |
|---|---:|---:|---|
| Stage 2 (HF API) | 3,872 | **3,872** | 무료. `?blobs=true` 1회씩, 약 8분 |
| Stage 3 (LLM) | 3,872 | **151** | README 내용이 같은 3,721건(96.1%)을 재사용 |
| Stage 4 (임베딩) | 3,872 | **약 1,340** | `document_hash`가 바뀐 문서만. 약 $0.02 |

Stage 2는 `STAGE2_VERSION`이 6→7로 올라가 `resume_matches`가 기존 행을 전부
불일치로 보고 다시 수집한다. 추가 플래그가 필요 없다.

기본값은 Stage 1을 다시 스캔하지 않는 것이다. 바꾸려는 것이 모델의 **사실**이지
모델 **목록**은 아니기 때문이다. 목록까지 새로 만들어야 하면 `--reingest --full-stage1`
(Action 입력 `stage1_mode=full-scan`)을 쓴다. 이때 Stage 1 전후 diff와 DB 비활성화 후보를
보고하고, Stage 1 **스캔 시작 시각**을 새 watermark로 저장한다. 절차와 중단 기준은
[`MODEL_REINGEST_RUNBOOK.md`](../MODEL_REINGEST_RUNBOOK.md)에 있다.

### Stage 3 재사용 판정을 고쳐야 했다

처음에는 "README가 안 바뀌면 Stage 3를 재사용한다"고 계획만 적었다. 코드를
보니 그렇게 동작하지 않았다.

```python
def source_stage2_hash(row):
    payload = json.dumps(row, ...)     # Stage 2 행 전체를 해시한다
    return digest(payload)
```

`stage2_version`이나 `enriched_at`만 바뀌어도 지문이 달라진다. 스키마가 바뀐
재적재에서는 **3,872건 전부**가 그렇게 되고, 유료 LLM 호출이 전수로 다시 나간다.

Stage 3의 입력은 둘뿐이다.

```
build_prompt()  →  row["model_id"] 와 README 에서 뽑은 스팬
load_source()   →  source.readme.path 의 파일 내용
```

나머지 Stage 2 필드는 프롬프트에 들어가지 않는다. 그래서 지문도 그 둘만 담게
좁혔다(`STAGE2_HASH_VERSION = 2`). **지름길이 아니라 실제 입력을 반영한 것이다.**

구 데이터와의 전환은 Stage 3가 이미 남겨 둔 README 내용 해시로 한다.

```
evidence.readme.content_hash  ←  기존 행 3,862/3,872(99.7%)에 있다
```

구 지문은 행 전체 해시라 새 지문과 비교할 수 없지만, 저 값은 Stage 3의 실제
입력이므로 지금 README와 바로 비교된다. 재사용한 행은 새 형식 지문으로 올려
두므로 다음 실행부터는 파일을 다시 읽지 않는다.

### `--reingest`가 하는 순서

```
⓪ 01 --no-resume                    --full-stage1 일 때만. Stage 1 전체 재수집 + diff 가드
① 02 --pool all                     전체 재수집 (무료, 약 8분)
② contract/validate.py              계약 게이트 — 실패하면 여기서 중단
③ 03 --pool all                     README 바뀐 151건만 LLM
④ 03_repair / evidence_index
⑤ 06 --apply                        벤치마크 (API 호출 없음)
⑥ 04 --execute --db-cache           hash 바뀐 약 1,340건만 임베딩
⑦ 적재 또는 dry-run 리포트
```

②가 ③보다 앞에 있는 것이 핵심이다. 비용 순서가
Stage 2(무료) → Stage 3(LLM) → Stage 4(임베딩) → DB 쓰기이므로, 게이트가
유료 단계 앞에 있어야 돈이 나가지 않는다.

`--apply`를 주지 않으면 DB를 건드리지 않고 `dry_run` 리포트만 낸다.
**다만 dry-run도 ③과 ⑥을 실제로 돌린다.** diff를 만들려면 결과물이 있어야
하기 때문이다. LLM 151건과 임베딩 약 $0.02가 dry-run에서도 나간다. 그 결과를
커밋하지는 않으므로 뒤이은 apply 실행은 같은 일을 한 번 더 한다.

## 5. Supabase 변경

### 지금 실재하는 함수가 둘이다

`supabase_schema.sql`과 `supabase_migration_model_search_tsv.sql`이 각각
`create or replace function public.match_model_scout_models(...)`을 한다.
**나중에 적용한 마이그레이션 쪽이 라이브다.** 스키마 파일만 보고 고치면
적용되지 않는다.

라이브 시그니처(15개 파라미터):

```sql
query_embedding vector(1536), match_count integer,
pool_filter text, task_filters text[], korean_required boolean,
min/max_parameter_count_billion numeric, min/max_context_length integer,
require_known_parameters boolean, require_known_context boolean,
popularity_tier_filter text, query_text text,
dense_weight real, sparse_weight real
```

**라이선스·artifact·dtype·VRAM 필터가 없다.** 타깃 사용자의 Q1·Q2·Q3가
전부 필터 불가다.

추가할 파라미터:

| 파라미터 | 타입 | 질문 |
|---|---|---|
| `commercial_status_filter` | `text[]` | Q1 "상업적으로 쓸 수 있는" |
| `require_artifact` | `text[]` | Q3 "Ollama/GGUF로" |
| `max_artifact_gib` | `numeric` | Q2 "16GB에 들어가는" |
| `exclude_gated` | `boolean` | Q7 "바로 내려받을 수 있는" |

### 누락 값 처리는 기존 규칙을 따른다

```
수치 조건(min/max)이 있고 값이 없으면 → 탈락
```

`05_validate_retrieval.numeric_ok()`에 이미 구현돼 있고 주석에
"deliberately mirrors the SQL predicates"라고 적혀 있다. 새 필터도 같다.

- `max_artifact_gib`를 걸면 용량을 모르는 모델은 탈락한다.
- `commercial_status_filter = ['permitted']`를 걸면 `unknown`은 탈락한다.
  이것이 **의도된 동작**이다. 모르는 모델을 상업 이용 가능으로 섞어 보여주면
  사용자가 창업에 쓰고 나서 문제를 알게 된다.

### `filter_metadata`에 필드를 추가하면 전문 검색 랭킹도 바뀐다

`search_tsv`는 생성 컬럼이고 본문에 `filter_metadata::text` 전체가 들어 있다.

```sql
setweight(to_tsvector('simple', coalesce(filter_metadata::text, '')), 'C')
```

`commercial_status`·`artifacts.formats`·`dtype`을 넣으면 그 문자열이 가중치 C로
색인된다. `permitted`·`gguf`·`bfloat16` 같은 토큰이 BM25 쪽 점수에 영향을 준다.

- 생성 컬럼이므로 재적재 시 자동으로 다시 계산된다. 별도 작업은 없다.
- 그러나 **검색 결과 순위가 바뀐다.** dry-run diff에서 반드시 확인해야 한다.
- 용량도 는다. 현재 평균 7.4KB × 3,872 ≈ 29MB다.

### 마이그레이션 방식

[`supabase_migration_contract_filters.sql`](../supabase_migration_contract_filters.sql)에
있다. **아직 적용하지 않았다.**

함수 시그니처가 바뀌므로 `CREATE OR REPLACE`로는 안 된다 — PostgreSQL은
파라미터가 추가되면 다른 함수로 보고 과부하(overload)를 만든다. 기본값이 있는
파라미터를 **뒤에 추가**하고, `drop function if exists`로 구 시그니처를 명시적으로
지운다. `supabase_schema.sql:141`이 이미 그 방식을 쓰고 있다.

`commercial_status`와 `gated`에 부분 표현식 인덱스를 만든다. 조건이 걸릴 때마다
전체를 훑지 않게 한다.

SQL은 `pglast`로 외부 문장과 `$$` 본문을 모두 파싱 검증했다. 실행은 사람이 한다.

### 로컬 하드 필터도 같은 조건을 구현한다

`05_validate_retrieval.hard_filter`에 네 조건을 추가했고,
`retrieval_lab/planner.HARD_FILTER_KEYS`와 `test/golden/v2/tools/verify.py`의
허용 키 목록도 같이 늘렸다. 어긋나면 오프라인 평가와 운영 검색이 다른 후보
집합을 쓴다.

실제 레코드 1,788개(생성 과제 1,200개 기준)로 시험한 결과:

| 질의 | 통과 |
|---|---:|
| 생성 과제만 (기준선) | 1,200 |
| + 상업 이용 가능만 | 666 |
| + GGUF 필수 | 1,033 |
| + GGUF와 safetensors 둘 다 | 10 |
| + 8GiB 이하로 돌아가는 | 778 |
| + 4GiB 이하 | 581 |
| + 바로 내려받을 수 있는 | 1,171 |
| + 넷을 모두 | 368 |

대조로, 기존 "8B 이하" 파라미터 필터는 같은 집합에서 **444개**만 통과한다.
파라미터 수를 모르는 995개가 탈락하기 때문이다. "8GiB 이하 실측 용량"은
**778개**가 통과한다 — 용량은 100% 알고 있다. 파라미터를 몰라 사라지던 모델이
돌아온다.

### 발견한 기존 divergence

이 작업과 무관하게 이미 있던 것이다.

```python
# 05_validate_retrieval.task_match — tasks 가 비면 전부 탈락
return bool(available & set(query.get("tasks") or []))
```

```sql
-- SQL — task_filters 가 null 이면 전부 통과
and (task_filters is null or cardinality(task_filters) = 0 or ...)
```

골든셋 질의가 항상 `tasks`를 지정하므로 지금 드러나지 않는다. 고치지 않고
기록만 남긴다 — 어느 쪽으로 맞출지는 검색 설계 결정이다.

이 RPC를 호출하는 코드는 `09_model_scout_mcp_readonly.py:692` 한 군데다.
(`17_recommend_graph.py`는 하이퍼그래프 쪽이라 이 RPC를 쓰지 않는다.)

`embedding` 컬럼은 마이그레이션에서 `halfvec(1536)`으로 바뀌어 있다. 함수
파라미터는 `vector(1536)`을 유지하므로 `08`은 지금처럼 `%s::vector`로 넣으면 된다.

---

## 6. GitHub Actions

### 무엇을 했나

[`model-scout-reingest.yml`](../../.github/workflows/model-scout-reingest.yml)을
새로 만들었다. **`schedule`이 없다.** 처음부터 수동 전용이다.

```yaml
on:
  workflow_dispatch:
    inputs:
      mode:    { type: choice, options: [validate, dry-run, apply] }
      confirm: { type: string }   # apply 에서만 "APPLY" 를 요구한다
```

| mode | HF 호출 | LLM·임베딩 | DB 쓰기 | 쓰임 |
|---|---|---|---|---|
| `validate` | 없음 | 없음 | 없음 | 컴파일 + 계약 검증 + coverage + 골든셋. PR 에서 돌린다 |
| `dry-run` | 전체 | **돈다** (151건 / 약 $0.02) | 없음 | 재적재 결과와 diff 리포트를 아티팩트로 올린다 |
| `apply` | 전체 | 돈다 | upsert | 팀이 dry-run 리포트를 확인한 뒤 1회 |

`apply`에는 두 겹의 잠금을 걸었다.

```
confirm 입력이 정확히 "APPLY" 가 아니면 중단
github.ref_name 이 main 이 아니면 중단
```

브랜치에서 실수로 `apply`를 고를 수 없다.

`dry-run`은 아무것도 커밋하지 않는다. 재생성된 스냅샷은 `apply`가 확정된 뒤에만
`data/`에 남는다.

### 기존 워크플로

[`model-scout-incremental.yml`](../../.github/workflows/model-scout-incremental.yml)의
`cron: "0 * * * *"`을 **파일에서 지웠다.** UI 에서만 꺼 두면 다음 사람이 파일을
보고 "매시간 돈다"고 읽는다. 되살릴 두 줄을 주석으로 남겨 뒀다.

`dataset-refresh.yml`은 공공데이터·하이퍼그래프 쪽 자동화로 모델 재적재와
분리돼 있다. **cron 이 아직 살아 있고, 이 작업에서는 건드리지 않았다.**
중단 여부는 팀이 따로 정할 일이다.

## 7. 실행 순서

```
브랜치에서 문서·스키마·resolver·테스트 완료
        ↓
PR 검토 및 main 병합
        ↓
main에서 수동 Action: validate                  ← 비용 0
        ↓
main에서 수동 Action: dry-run                    ← HF 호출만
        ↓
coverage before/after · license · unknown · DB diff 팀 확인
        ↓
main에서 수동 Action: apply                      ← 1회
        ↓
Supabase row 수 · evidence 수 · embedding 수 · schema_version 검증
        ↓
schedule 없이 workflow_dispatch만 남긴 상태 유지
        ↓
확정된 run_id 기준으로 골든셋 재개
```

## 8. 골든셋에 미치는 영향

골든셋 v2의 스냅샷은 이미 `ai/backfill`이 반영된 상태다
(`metadata_variant: backfill-v2-high-confidence-parameters`). 재적재가 끝나면
그 스냅샷을 **정식 run_id의 코퍼스로 교체**해야 한다.

바뀌는 것:

- `identity.gated`·`artifacts.total_bytes`가 생기므로 **새 질의 유형을 만들 수 있다.**
  "바로 내려받을 수 있는 모델", "4GB 이하 GGUF" 같은 것이다.
- `legal.commercial_status`가 하드 필터 키가 되므로 상업 이용 질의의 eligible이
  좁아진다. `review_required` 1,104개가 정답 후보에서 빠진다.
- `conflict` 상태가 생기므로 **그 모델은 수치 조건 질의에서 탈락한다.**
  기존에 통과했던 모델이 빠질 수 있다. dry-run diff에서 확인해야 한다.

판정 기준 코퍼스가 바뀌면 `test/golden/v2/corpus_snapshot.meta.json`의
`last_sync_run_id`도 바뀌고, `verify.py`가 "다른 코퍼스 스냅샷으로 판정됨"으로
기존 판정을 전부 무효 처리한다. **그래서 재적재를 골든셋 사람 검수보다 먼저
끝내야 한다.**
