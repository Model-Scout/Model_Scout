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
없다.

그래서 `--reingest` 모드를 새로 만든다.

| 모드 | 대상 | HF 호출 | LLM | 임베딩 | DB |
|---|---|---|---|---|---|
| `--refresh` (기존) | watermark 이후 변경분 | 변경분 | 변경분 | 변경분 | upsert |
| `--reingest` (신규) | **전체** | 전체 1회 | **재사용** | **document_hash 변경분만** | upsert |

핵심은 **LLM과 임베딩을 다시 돌리지 않는 것**이다.

- Stage 3 결과(`semantic.*`)는 README가 안 바뀌면 그대로 유효하다.
  README `sha256`으로 판정한다.
- Stage 4 임베딩은 `document_hash`가 바뀐 문서만 재생성한다. 백필에서
  3,872개 중 1,278개만 재생성하고 2,594개를 재사용했다. 같은 방식이다.

즉 `--reingest`의 추가 비용은 **HF API 호출 3,872회(약 8분, 무료)와
새 필드로 `embedding_text`가 달라진 문서의 임베딩**뿐이다.

### `--reingest`가 하는 순서

```
① contract/validate.py --baseline 로 현재 상태를 기록          (게이트 기준점)
② 01: list_models 전체 스캔. 신규·삭제 모델 반영
③ 02: 전체 모델 api?blobs=true. provenance 전체 생성
④ 2.5: contract/validate.py — 실패하면 중단
⑤ 03: README sha256이 바뀐 모델만 LLM 재호출
⑥ 3.5: 06 벤치마크 전체 재추출 (무료)
⑦ 04: document_hash 변경분만 임베딩
⑧ 05: dry-run diff 리포트 → 사람 확인 → apply
```

---

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

함수 시그니처가 바뀌므로 `CREATE OR REPLACE`로는 안 된다 — PostgreSQL은
파라미터가 추가되면 다른 함수로 보고 과부하(overload)를 만든다. 기본값이 있는
파라미터를 **뒤에 추가**하고, `drop function if exists`로 구 시그니처를 명시적으로
지운다. `supabase_schema.sql:141`이 이미 그 방식을 쓰고 있다.

이 RPC를 호출하는 코드는 `09_model_scout_mcp_readonly.py:692` 한 군데다.
(`17_recommend_graph.py`는 하이퍼그래프 쪽이라 이 RPC를 쓰지 않는다.)

`embedding` 컬럼은 마이그레이션에서 `halfvec(1536)`으로 바뀌어 있다. 함수
파라미터는 `vector(1536)`을 유지하므로 `08`은 지금처럼 `%s::vector`로 넣으면 된다.

---

## 6. GitHub Actions

현재 [`model-scout-incremental.yml`](../../.github/workflows/model-scout-incremental.yml)은
`cron: "0 * * * *"`로 매시간 뜨고 TTL 24시간으로 실제 처리를 하루 한 번 한다.
**팀 결정으로 자동화는 멈춘 상태다.**

새 구조에서는 처음부터 schedule이 없다.

```yaml
on:
  workflow_dispatch:
    inputs:
      mode:
        type: choice
        options: [validate, dry-run, apply]
```

| mode | HF 호출 | LLM·임베딩 | DB 쓰기 | 쓰임 |
|---|---|---|---|---|
| `validate` | 없음 | 없음 | 없음 | 스키마·기존 데이터만 검사. PR에서 돌린다 |
| `dry-run` | 전체 | 변경분 | **없음** | 재적재 결과와 DB diff 리포트만 생성 |
| `apply` | 전체 | 변경분 | upsert | 팀 확인 후 1회 |

`apply`는 브랜치에서 돌리지 않는다. PR 검토 → main 병합 후 수동 1회다.

`dataset-refresh.yml`은 공공데이터·하이퍼그래프 쪽 자동화로 모델 재적재와
분리돼 있다. 이 작업에서는 건드리지 않는다.

---

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
