# 공공데이터 코퍼스 v2: 받아서 실행하기

고정 버전은 `data_version aa1a71d35a121150`입니다. 정제·검증·적재 내역과 남은 일은 [CUTOVER.md](CUTOVER.md)에 있습니다. 이 문서는 PR을 받은 사람이 같은 v2로 실행하고 평가하는 방법만 다룹니다.

이전 고정본의 기록은 [pins/](pins/)에 있습니다.
- `04239c20eb394c12`: 2026-11-16 이전에 Supabase v2에 적재돼 있던 것(서비스에는 연결된 적 없음)
- `b41fbf9bd52ad851`, `40441294f66875a6`, `cca4cfd4965a3ce7`: 적재하지 않은 중간본
  - 40441294 → cca4cfd4: OA-15531 카드 1개만 바뀜
  - cca4cfd4 → aa1a71d3: 검색 문서·벡터는 같고, 공식 조회 코드(18_enrich)의 해시만 바뀜

## 받는 것

**Git**

| 경로 | 내용 |
|---|---|
| `ai/data/public_datasets_stage1.jsonl` | 포털 수집본 15,157건 (기존 그대로) |
| `ai/data/public_catalog/official_meta.jsonl`, `official_meta_migrations.json`, `official_raw/*.gz` | 공식 조회 결과(API 근거 주소와 상세 페이지 해시 포함), 이관 근거, 카탈로그 원문 |
| `ai/data/public_enriched/` | 보완본: 이용허락, 제공 형식(API 근거 포함), 갱신주기, 공식 설명, 제공기관 |
| `ai/data/model_snapshot/active_models_20261115.jsonl` | 그래프에 쓴 운영 active 모델 4,017개 |
| `ai/data/hypergraph_v2/`, `ai/data/dataset_index_v2/` | 그래프, 검색 문서(`chunks.jsonl`), 벡터 기록(`manifest.json`). **`embeddings.npy`는 없음** |
| `ai/test/public_data/corpus_v2/data_version.json` | 고정 기록 |
| `ai/test/public_data/corpus_v2/official_pages_manifest.json` | 상세 페이지 묶음과 각 페이지의 sha256 |
| `golden_prep/batch5/labels_llm_v6.jsonl` | 골든셋 v6 ([batch5/README](golden_prep/batch5/README.md)) |
| `compare/runs/2026-11-16_v2-aa1a71d3_labels-v6/` | 기준선 ([README](compare/runs/2026-11-16_v2-aa1a71d3_labels-v6/README.md)) |

**팀 공유 폴더 `v2_aa1a71d35a121150/`** (Git에 넣지 않은 파일)

- **최신본은 `v2_aa1a71d35a121150/`입니다.** 이름이 다른 폴더(`v2_cca4cfd4965a3ce7/`, `v2_40441294f66875a6/`)는 이전 고정본용이라 쓰지 않습니다.
- **받는 곳:** (팀 드라이브 위치 기재 예정)
- 받은 뒤 아래 1번의 `sha256sum -c SHA256SUMS`가 세 파일 모두 OK여야 합니다.

| 파일 | 크기 | sha256 | 내용 |
|---|---|---|---|
| `embeddings.npy` | 126MB | `8b05f2f9073869ac…` | 검색 벡터 |
| `manifest.json` | 4MB | `1a02c15738c07213…` | 벡터 기록 (Git의 것과 같음) |
| `official_pages_40441294.tar` | 105MB | `ea896badfef27768…` | API 근거가 된 상세 페이지 3,357개 (표준 300 + 파일 3,057) |
| `SHA256SUMS` | | | 위 세 파일의 전체 해시 |

## 실행 순서 (`ai/` 폴더)

1. **받은 파일 확인과 배치**
   ```bash
   cd <받은 폴더> && sha256sum -c SHA256SUMS && cd -
   cp <받은 폴더>/embeddings.npy data/dataset_index_v2/
   tar -xf <받은 폴더>/official_pages_40441294.tar -C data/public_catalog/official_raw   # 근거 확인·파서 재실행용
   python test/public_data/corpus_v2/official_pages.py verify <받은 폴더>/official_pages_40441294.tar
   ```
2. **고정 버전 확인**
   ```bash
   python public_v2_pipeline.py --verify-pin
   # public v2 matches the pinned data_version aa1a71d35a121150
   python -c "import hypergraph_search as hs; print(hs.use_corpus('v2'))"   # 그래프·문서·벡터 검사
   ```
   - Supabase v2에 이 고정본이 적재된 뒤에는 공유 폴더 없이 `python 20_sync_dataset_index.py --corpus v2 --restore-vectors`로도 벡터를 복원할 수 있습니다.
   - 복원은 DB 빌드 기록, 청크 순서, `vectors_sha256`가 모두 맞을 때만 파일을 씁니다.
3. **평가 (기준선 재현)**: [기준선 README](compare/runs/2026-11-16_v2-aa1a71d3_labels-v6/README.md)의 명령을 새 폴더로 실행합니다.
   - 실행 폴더는 덮어쓰지 않습니다.
   - 같은 폴더에 다른 기준(질문, 중복 목록)으로 실행하거나 재채점하면 멈춥니다.

## 다시 빌드할 때 (같은 결과를 확인하는 경우)

```bash
python 18_enrich_public_datasets.py --offline          # 캐시와 저장 원문만 사용, 네트워크 없음
python 13_build_hypergraph.py --corpus v2 --model-snapshot data/model_snapshot/active_models_20261115.jsonl
python 14_build_dataset_chunks.py --corpus v2
python public_v2_pipeline.py --verify-pin             # 같은 data_version이 나와야 함
```

- `--offline`은 캐시에 기록된 답과 근거로 다시 만듭니다. 상세 페이지 원문은 근거 확인이나 파서가 바뀌었을 때 다시 해석하는 데만 필요합니다.
- 해시는 텍스트를 LF 줄바꿈 기준으로 계산하므로 Windows와 Mac·Linux에서 같은 값이 나옵니다.

## API 제공 정보를 읽는 법

| `official.api_check` | 뜻 | 카드 표기 |
|---|---|---|
| `confirmed` | 표준데이터 상세 페이지에 그 데이터의 OpenAPI 주소가 있음 | 형식에 API |
| `confirmed_auto` | 파일데이터 상세 페이지에 그 데이터 번호의 자동변환 OpenAPI 주소가 있음 | 형식에 API + "파일 자동변환 OpenAPI" |
| `confirmed_catalog` | 카탈로그의 제공형태가 REST·SOAP·LINK | 형식에 API |
| `not_found`, `page_failed` | 주소를 찾지 못함, 또는 페이지를 읽지 못함 | "API 제공 여부: 미확인" (API 없음이 아님) |

- 반대로 카드에 API만 있으면 파일이 없다는 뜻이 아닙니다. 파일 미확인이며, 원 제공처가 파일을 낼 수 있습니다(예: 15088653의 공식 설명에 CSV·XLSX 내려받기가 적혀 있음).
- 공식 설명과 수집 설명의 좌표계가 다르면 카드에 "설명 간 불일치(확인 필요)"를 붙이고, 둘 다 남깁니다(현재 OA-15531 1건).

- 주소 확인은 실제 호출 성공과 다릅니다. 모든 행이 `api_call_checked: false`입니다.
- 자동변환 API는 올린 파일의 내용이므로 실시간 근거가 아닙니다.
- 표준 300건의 구성: `confirmed` 176, `confirmed_catalog` 46, 미확인 78
- 파일 3,060건의 구성: `confirmed_auto` 2,661, 미확인 396, 페이지 404 3건(다음 실행에서 다시 시도)

## Supabase v2 테이블

| 객체 | 내용 |
|---|---|
| `model_scout_datasets_v2` | 데이터셋 19,130행 |
| `model_scout_dataset_chunks_v2` | 청크 41,144행. **청크 전문**과 벡터(halfvec). 서버는 답변 근거(카드 사실)를 여기서 읽음 |
| `model_scout_dataset_index_v2_meta` | 적재한 빌드 기록: `documents_id`, `corpus_id`, `data_version`, 벡터 해시, 임베딩 모델 |

- **현재 적재본:** aa1a71d3 (2026-11-16 적재, 이전 적재본은 04239c20). 적재 결과는 아래 "배포 기록"에 있습니다.
- **적재:** `python 20_sync_dataset_index.py --corpus v2 --apply`
  - `_v2` 테이블만 씁니다.
  - 벡터 파일이 바뀌면 벡터 전체(약 280MB)를 다시 올립니다.
  - 빌드 기록은 마지막에 쓰고, 적재 후 ID, 본문, 빌드 기록, 검색 응답을 확인합니다.
- **이전 적재본(04239c20)으로 되돌리기:** 그 빌드를 만든 커밋 `23b7f0cc`의 코드와 데이터로 해야 합니다. 지금 코드는 빌드 기록의 코드 해시가 달라 이전 빌드를 거부합니다.
  ```bash
  git worktree add ../ms-04239c20 23b7f0cc && cd ../ms-04239c20/ai     # .env는 따로 복사
  cp <보관>/v2_04239c20eb394c12/embeddings.npy <보관>/v2_04239c20eb394c12/manifest.json data/dataset_index_v2/
  python public_v2_pipeline.py --verify-pin && python 20_sync_dataset_index.py --corpus v2   # 미리보기
  python 20_sync_dataset_index.py --corpus v2 --apply
  ```
  2026-11-16에 미리보기(쓰기 없음)까지 확인했습니다.
  - 고정 버전, 그래프·문서, 벡터(`62d7ba67…`) 검사를 모두 통과했습니다.
  - 예상 쓰기량은 279MB입니다.

## 서비스에서 v2로 검색하기 (서버 배포)

검색 방법(유사도, 필터, 가중치, 하한선)은 기존 그대로입니다. 벡터 계산은 서버 메모리의 v2 벡터 파일로 합니다.

**서버 시작 시 확인 (`MODEL_SCOUT_DATA_VERSION` 설정)**
- 배포한 그래프 파일 해시
- 문서 빌드 기록과 그래프↔문서 연결
- 벡터 기록(문서 버전, 모델, 파일 해시, 행 수)과 청크 순서 해시
- Supabase 빌드 기록

하나라도 어긋나면 시작하지 않습니다. v1로 넘어가지도 않습니다.

**주의:** 서버는 답변 근거를 요청마다 v2 DB에서 읽습니다. 서버가 v2로 도는 동안 DB만 다른 빌드로 바꾸면, 검색은 이전 파일로 하고 근거는 새 DB에서 읽게 됩니다. 그러므로 서버가 v2일 때는 먼저 v1로 돌린 뒤 DB를 갱신합니다.

**순서 (Docker Desktop과 rsync 필요, 저장소 루트에서)**
```bash
deploy/inspect_server.sh > server_state.txt      # 읽기 전용: 코퍼스, 버전, 코드 해시, 메모리
deploy/snapshot_server.sh                        # 서버 안에 보존: 실행 중 이미지(백업별 :rb-<시각> 태그와 ID), compose·env, 데이터 하드링크 사본
# (서버가 v2이면) MODEL_SCOUT_CORPUS=v1 deploy/deploy.sh --data
python ai/20_sync_dataset_index.py --corpus v2 --apply
MODEL_SCOUT_CORPUS=v2 deploy/deploy.sh           # 처음 v2로 바꿀 때는 전체 배포 (compose.yml도 복사됨)
deploy/inspect_server.sh                         # 배포 후 확인
```

**되돌리기**
- **v1로:** `MODEL_SCOUT_CORPUS=v1 deploy/deploy.sh --data`
  - `.env.corpus`를 v1로 쓰고, 로컬 v1 파일(git과 같음)을 서버에 맞춘 뒤 컨테이너를 다시 만듭니다.
  - 새 코드의 v1 검색은 2026-11-13 기록과 72/72 질문에서 같은 순위였습니다.
- **배포 직전 상태로:** `deploy/rollback.sh`
  - 고른 백업의 이미지(기록한 이미지 ID로 확인), compose·env, 데이터 파일을 되돌립니다. 예전 백업을 골라도 그 시점의 이미지로 돌아갑니다.
  - 그 상태가 v2였다면 DB에도 그 빌드가 있어야 시작합니다.

## 배포 기록: 2026-11-16 v1 → v2 (aa1a71d3)

**배포 전 서버:** v1. `.env.corpus`가 없었고, v2 파일은 없었으며, compose.yml은 `.env.corpus`를 읽기 전 버전이었습니다.

| 단계 | 결과 |
|---|---|
| v1 백업 | `/opt/model-scout/rollback/20261116T102525Z`. 이미지 `ai 2d87ce71…`, `backend 0c67e570…`를 `:rb-20261116T102525Z`로 보존. 파일 해시 확인 통과 |
| Supabase v2 적재 | 청크 41,144개 전체 재적재, 삭제 0. 데이터셋 ID 19,130개와 청크 본문 41,144개 일치, 빌드 기록 `aa1a71d35a121150`, 검색 응답 정상 |
| 벡터 복원 비교 | DB에서 복원한 벡터가 로컬 `embeddings.npy`와 바이트 단위로 같음(`8b05f2f9…`, 41,144행) |
| 배포 | 이미지 `ai ea99eea8…`, `backend e2cec4cc…`. `.env.corpus`는 v2·`aa1a71d35a121150`. 그래프 파일 8개, 빌드 기록, 벡터 기록, 벡터, 고정 기록 해시가 git·로컬과 일치. ai 30초 만에 healthy(시작 검사 통과) |
| 질의 확인 | 5개 질문 모두 정상 응답(12~25초). 돌려받은 카드 사실(형식, API 제공 여부, 불일치, 제한 문장)이 로컬 카드와 다른 곳 0건 |
| 배포 후 상태 | 재시작 0, 메모리 부족 종료 없음, 오류·경고 로그 0. ai 컨테이너 메모리 약 840~905MB(한도 1,172MB), 서버 여유 약 700MB. 공개 API 200, AI 사이트는 로그인 없이 401 |

**질의에서 확인한 것**
- **API 미확인:** "API 상태 미확인"으로 답함(예: `data_go_kr/3045716`). "API 없음"이라고 하지 않음.
- **파일 자동변환 API:** 그대로 전달됨(예: `data_go_kr/15111389`).
- **제한 문장:** 원문 그대로 전달됨(예: OA-20447의 "최대 1,000건", "최근 7일").
- **OA-15531:** 제목으로 물어도 검색 상위에 나오지 않음.
  - 그래프에는 정상적으로 있고 중복·시리즈로 묶이지 않았으니, 검색 순위의 문제입니다. 가중치는 바꾸지 않았습니다.
  - 서버에서 근거를 직접 조회하면 "좌표계: 공식 설명은 Bessel, 수집 제목·설명은 GRS80"이 나옵니다.
- **개선할 점:** 부산 도서관(15088653)의 답변이 "실시간 업데이트"라고 썼습니다. 포털 갱신 표기는 실시간 근거가 아니라고 지시했는데도 그랬습니다.

**배포 중 고친 것**
- **`.dockerignore`:** main(#47)의 Dockerfile이 복사하는 `retrieval_lab`의 서빙 파일 4개를 넣어, 이미지 빌드가 실패하던 문제를 고쳤습니다.
- **원격 스크립트:** `inspect_server.sh`, `snapshot_server.sh`, `rollback.sh` 안의 `docker compose`가 원격 스크립트의 입력을 읽어 뒷부분이 실행되지 않던 문제를 고쳤습니다(`</dev/null`).
- **`deploy.sh`:**
  - 로컬에 `.env`가 없으면 서버의 `.env.ai`, `.env.backend`, `docs_users`를 그대로 씁니다(셋 중 하나라도 없으면 멈춤).
  - compose.yml과 Caddyfile은 LF로 보냅니다.

**이번 배포를 손으로 한 부분:** 배포한 PC(Windows)에 rsync가 없어서, `deploy.sh`의 v2 단계를 같은 내용으로 직접 실행했습니다.
- **git에 있는 파일:** 그래프, 빌드 기록, 고정 기록, readmes를 `git -c core.autocrlf=false archive`로 LF 그대로 서버의 임시 폴더에 풀었습니다.
- **`embeddings.npy`:** `scp`로 보냈습니다.
- **확인과 배치:** 해시를 확인한 뒤 제자리로 옮겼습니다.
  - readmes는 새 파일 1,621개만 더했습니다(23,973 → 25,594, 서버에만 있던 파일 0).
  - `hf_datasets_ner.jsonl`은 서버와 같아서 보내지 않았습니다.
- **이미지:** 이 PC 작업본에서 빌드해 `.py` 파일이 CRLF입니다. 내용은 커밋 `404cbb7d`와 같습니다. 다음 배포는 LF 작업본이나 rsync가 있는 환경에서 `deploy.sh`로 하는 것이 좋습니다.

**되돌리기:** `deploy/rollback.sh 20261116T102525Z`로 v1 이미지, 설정, 데이터로 돌아갑니다. v1은 v1 테이블을 쓰므로 DB는 되돌릴 필요가 없습니다.

## 아직 하지 않은 것

- **Actions의 v2 전환과 재개**
- **v1 제거:** 서비스 전환 후 v1 참조가 없는지 확인하고, 복구용 파일을 보관한 뒤 진행
- **골든셋 보류 30쌍의 공식 확인:** [batch5/README](golden_prep/batch5/README.md)
