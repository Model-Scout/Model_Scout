# 배포 (VPS)

서버는 `ai`, `backend`, Caddy를 Docker Compose로 실행합니다. 서버가 작아 이미지는 로컬에서 빌드합니다.

## 전체 흐름

| 단계 | 언제 | 무엇 | 운영에 닿는가 |
|---|---|---|---|
| ① 인덱스·문서 | 데이터가 바뀔 때만 (아래 런북 B) | 하이퍼그래프·검색 문서 고정(`public_v2_pipeline.py`) | 아니요. 운영 DB 적재는 ③과 함께 전환할 때 합니다 |
| | | LLM-wiki 다시 생성(`python ai/15_build_wiki.py`) | 아니요. 사람이 읽는 문서이고 배포 대상이 아닙니다 |
| ② 로컬 검증 | 배포할 때마다 | `release.sh build` → `verify --query` (Docker Desktop) | 운영 Supabase를 **읽기만** 합니다. 쓰기는 로컬 Postgres에만 합니다 |
| ③ VPS 배포 | ②가 통과한 릴리스 | `release.sh ship` (빌드 없이 검증한 이미지·데이터 그대로) | 예 |

코드만 바뀌면 ①을 건너뜁니다. 지금 고정본(`aa1a71d3`)은 다시 만들거나 적재하지 않습니다.

배포 순서는 다음과 같습니다. **로컬에서 검증한 이미지·데이터·설정을 그대로 보냅니다.**
`release.sh`는 Git Bash(Windows)와 Linux·Mac에서 같게 동작하며, rsync 없이 tar와 ssh만 씁니다.

```
deploy/release.sh build                 # 릴리스 하나: 이미지 2개 + 데이터 + 설정 + 해시 기록
deploy/release.sh verify <id> --query   # Docker Desktop에서 실행해 검사 (--query는 실제 질문 1건)
deploy/release.sh ship <id>             # 빌드 없이 전송 → 서버에서 해시·이미지 ID 확인 → 설치 → 활성화
deploy/release.sh status                # 서버의 현재 릴리스와 컨테이너
deploy/release.sh rollback <id|legacy>  # 이전 릴리스로 복구
```

## 릴리스

| 항목 | 내용 |
|---|---|
| 릴리스 ID | `<UTC 시각>-<커밋 8자리>[-dirty]-<data_version 8자리>`<br>예: `20261119T120000Z-cab5907a-aa1a71d3`<br>같은 데이터로 코드만 여러 번 배포해도 서로 다른 ID가 됩니다 |
| 코드 | 커밋된 git 객체에서 꺼내 빌드합니다. 작업본의 줄바꿈(CRLF)과 관계없이 LF이며, 빌드는 `linux/amd64`입니다<br>추적 중인 파일에 커밋하지 않은 변경이 있으면 `git stash create`로 그 상태를 담고 ID에 `-dirty`를 붙입니다. **`-dirty` 릴리스는 로컬 검증 전용이고 `ship`이 거부합니다** |
| 이미지 | `model-scout-ai:<id>`, `model-scout-backend:<id>`. ID를 `images.txt`와 `release.json`에 기록합니다 |
| 데이터 | 서버가 쓰는 v2 파일만 담습니다: `hf_datasets_ner.jsonl`, `readmes/`, `hypergraph_v2/`, `dataset_index_v2/`(빌드 기록, 벡터 기록, `embeddings.npy`, 고정 기록 `data_version.json`)<br>빌드 전에 `public_v2_pipeline.py --verify-pin`으로 고정본과 같은지 확인합니다 |
| 설정 | `compose.yml`, `Caddyfile`, `.env`(이미지 태그), `.env.corpus`(코퍼스와 data_version), `server_release.sh` |
| 기록 | `release.json`: 커밋, dirty 여부, 이미지 ID, data_version, 그래프·문서·벡터·청크 ID 해시<br>`SHA256SUMS`: 모든 파일<br>`verified.json`: 로컬 검사 결과. 통과한 경우에만 생깁니다 |

`deploy/.releases/<id>/`는 git에 올리지 않습니다. 데이터는 가능하면 하드 링크로 두고, 이후 원본이 바뀌면 `SHA256SUMS` 검사에서 걸립니다.

## 로컬 검증 (`verify`)

[`compose.local.yml`](compose.local.yml)로 그 릴리스의 이미지와 데이터를 Docker Desktop에서 실행합니다. Caddy는 빼고, backend는 `127.0.0.1:8000`에만 엽니다.

### 연결 대상

| 연결 | 대상 | 장치 |
|---|---|---|
| 데이터셋·모델 검색 | 운영 Supabase, **읽기 전용** | `MODEL_SCOUT_LOCAL=1`이면 `supabase_db.db_connection`이 연결을 읽기 전용 세션(`set_session(readonly=True)`)으로 엽니다. 모델 검색(09)은 원래 읽기 전용 세션입니다. 연결 시작 옵션(`options=-c default_transaction_read_only=on`)은 Supabase 풀러가 버리므로 쓰지 않습니다(2026-11-19 로컬 검증에서 확인). 두 경로 모두 검사에서 실제 쓰기 거부를 확인합니다 |
| AI 체크포인트 | 로컬 postgres | `CHECKPOINT_DATABASE_URL`. 로컬 모드에서 이 값이 없거나 로컬 주소가 아니면 AI가 시작하지 않습니다. 운영 DB로 대신 연결하지 않습니다 |
| backend 대화 저장 | 로컬 postgres | backend에는 운영 접속 정보를 주지 않습니다. 로컬 모드에서 DB 주소가 로컬이 아니면 시작하지 않습니다 |

- **로컬 postgres 초기화:** 시작할 때 [`local/postgres-init.sql`](local/postgres-init.sql)(Supabase 역할)과 `backend/app_schema.sql`을 적용합니다. 체크포인트 테이블은 AI가 시작할 때 만듭니다.
- **AI 키:** OpenAI 키와 Supabase 읽기 설정은 `.env` 또는 `ai/.env`에서 서버의 `.env.ai`와 같은 항목만 골라 `deploy/.local/ai.env`에 씁니다. 이 파일은 git에 올리지 않습니다.

### 검사 항목 ([`local/check_release.py`](local/check_release.py))

1. 실행 중인 컨테이너의 이미지 ID가 빌드한 ID와 같은지
2. AI가 릴리스 데이터(`documents_id`)를 쓰고 있는지. AI는 시작할 때 Supabase 빌드 기록과도 대조합니다
3. 운영 Supabase 세션이 읽기 전용(`transaction_read_only = on`)인지
4. 로컬 postgres에 체크포인트와 대화 테이블이 있는지
5. 안전장치: 체크포인트 주소가 없거나 운영 주소면 AI가 거부하는지, 운영 주소를 받은 backend가 거부하는지
6. backend `/api/health`
7. `--query`를 줬을 때:
   - 실제 질문 1건을 보냅니다. gpt-4o-mini 몇 번과 임베딩 1번으로, 1센트 미만입니다.
   - 대화와 체크포인트가 로컬 postgres에 저장됐는지, 운영 DB에는 0건인지 확인합니다.
8. 메모리 사용량, 재시작 0회, 오류 로그 줄 수

`--query` 없이 실행하면 OpenAI를 호출하지 않습니다. 운영 DB는 읽기만 합니다.

**한계:** 로컬 검증은 메모리 제한을 VPS와 같게 둔 사전 검사이고, 질문 1건으로 기본 동작을 확인하는 것입니다. 부하 검증이 아니며 로컬과 VPS는 전체 메모리·CPU 조건이 다릅니다. **배포 후 VPS에서도 메모리와 재시작을 확인합니다**(`deploy/inspect_server.sh`).

## 전송과 서버 배치 (`ship`)

1. 로컬에서 확인합니다.
   - `verified.json`이 있는지
   - `SHA256SUMS`가 그대로인지
   - 로컬 이미지 ID가 검증한 ID와 같은지
2. `docker save | gzip | ssh docker load`로 이미지를 보냅니다. 이미지 ID는 그대로 유지됩니다.
3. 릴리스 폴더를 tar로 `staging/<id>`에 보냅니다.
4. [`server_release.sh`](server_release.sh) `install`:
   - `SHA256SUMS`와 이미지 ID를 확인합니다.
   - 서버의 키 파일(`.env.ai`, `.env.backend`, `docs_users`)을 릴리스 폴더에 복사합니다.
   - `releases/<id>`로 옮깁니다. 설치된 릴리스는 다시 쓰지 않습니다.
5. `activate`:
   - 그 폴더의 compose로 컨테이너를 다시 만들고(`--force-recreate --wait`) 확인합니다. 확인 항목은 healthy, 이미지 ID, data_version입니다.
   - 통과하면 `CURRENT`와 `HISTORY`에 기록합니다.
   - **실패하면 직전 릴리스를 자동으로 다시 활성화합니다.**

서버 구조:

```
/opt/model-scout/
  releases/<id>/   compose.yml Caddyfile .env .env.corpus data/ release.json images.txt SHA256SUMS + 키 사본
  staging/         전송 중인 릴리스 (설치 전)
  CURRENT HISTORY  현재 릴리스, 활성화 기록
  compose.yml data/ .env.ai ...   릴리스 도입 전 구조(legacy, deploy.sh). 그대로 남겨 둡니다
```

- **프로젝트 이름:** compose 프로젝트 이름은 어느 폴더에서 실행하든 `model-scout`로 고정합니다. 그래서 legacy와 릴리스가 같은 컨테이너와 같은 Caddy 인증서 볼륨을 씁니다.
- **이미지 보존:** 릴리스 이미지는 태그가 있어 `docker image prune`에 지워지지 않습니다. 오래된 릴리스를 정리하는 단계는 아직 없습니다.

## 복구 (`rollback`)

`rollback <id>`는 그 릴리스 폴더의 데이터·설정·키·이미지로 컨테이너를 다시 만들고, `activate`와 같은 확인을 거칩니다. `CURRENT` 기록만 바꾸지 않습니다.

`rollback legacy`는 릴리스 도입 전 구조(`/opt/model-scout/compose.yml`, `:latest` 이미지)로 돌아갑니다. 그보다 이전 상태는 `snapshot_server.sh`와 `rollback.sh <stamp>`로 복구합니다.

## 두 가지 런북

### A. 코드만 바뀔 때 (데이터는 지금 고정본 그대로)

1. 변경을 커밋합니다. `-dirty`는 배포할 수 없습니다.
2. `release.sh build` → `verify <id> --query`
3. `release.sh ship <id>`
4. `release.sh status`, `inspect_server.sh`로 메모리·재시작·오류 로그를 확인합니다.

인덱스 재빌드, 재고정, DB 적재는 하지 않습니다.

### B. 데이터가 바뀔 때 (새 v2 빌드)

서버는 시작할 때 자기 데이터 파일과 Supabase v2 빌드 기록을 대조합니다. 또 요청마다 Supabase의 카드 사실을 읽습니다. 그래서 **운영 DB만 먼저 새 버전으로 바꾸면, 돌고 있는 서버의 파일과 DB가 어긋나는 구간이 생깁니다.**

1. **로컬 준비:** 새 데이터를 고정하고(`public_v2_pipeline.py --check-only --pin`) 검사를 통과시킵니다. 이 단계는 운영 DB를 건드리지 않습니다.
2. **테스트 환경 확인:** 새 버전을 운영 v2 테이블이 아닌 곳에 적재해 확인합니다. 별도 Supabase 프로젝트나 별도 테이블이 해당합니다. **지금 `20_sync_dataset_index.py`는 운영 v2 테이블에만 쓸 수 있어, 이 단계에 필요한 대상 선택 기능은 아직 없습니다.**
3. **운영 전환:**
   - 짧은 점검 시간을 정합니다. `snapshot_server.sh`로 백업합니다.
   - 운영 DB에 적재하고 검사합니다(`loaded_check`, 벡터 복원 해시 비교).
   - 바로 새 데이터로 만든 릴리스를 `ship`합니다.
   - DB와 서버 파일이 같은 data_version인지 `status`와 AI 시작 검사로 확인합니다.
4. **실패 시:**
   - 이전 릴리스로 `rollback`합니다.
   - 운영 DB도 이전 버전으로 다시 적재해야 서버가 시작할 수 있습니다. DB 복구는 이 스크립트가 하지 않습니다.

2번의 테스트 적재 대상이 생기기 전까지는, 데이터 전환을 점검 시간을 둔 수동 절차로 진행합니다.

## 기존 스크립트

| 파일 | 상태 |
|---|---|
| `deploy.sh` | 릴리스 도입 전 방식입니다. 빌드와 전송을 한 번에 하고, rsync가 필요하며, `:latest` 이미지를 씁니다. `release.sh`로 첫 배포가 끝나면 정리합니다 |
| `snapshot_server.sh`, `rollback.sh` | legacy 구조의 백업과 복구용입니다 |
| `inspect_server.sh` | 서버 상태 조회(읽기 전용)입니다 |
| `tests/test_server_release.sh` | `server_release.sh`를 가짜 docker로 시험합니다(설치 검사, 실패 시 자동 복구, 되돌리기) |
