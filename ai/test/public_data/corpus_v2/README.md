# 공공데이터 코퍼스 v2: 받아서 실행하기

고정 버전 `data_version 04239c20eb394c12`이다. 정제·검증·적재 내역과 남은 일은 [CUTOVER.md](CUTOVER.md)에 있다. 이 문서는 PR을 받은 사람이 같은 v2를 실행하는 방법만 다룬다.

## 받는 것

| 경로 | 내용 |
|---|---|
| `ai/data/public_datasets_stage1.jsonl` | 포털 수집본 15,157건 (기존 그대로) |
| `ai/data/public_catalog/official_meta.jsonl`, `official_meta_migrations.json`, `official_raw/` | 공식 페이지 조회 결과, 이관 근거, 저장한 원문 6,170개 |
| `ai/data/public_enriched/` | 보완본: 이용허락·제공 형식·갱신주기·공식 설명·제공기관 |
| `ai/data/model_snapshot/active_models_20261115.jsonl` | 그래프에 쓴 운영 active 모델 4,017개(읽은 시각은 `.meta.json`) |
| `ai/data/hypergraph_v2/` | 그래프 |
| `ai/data/dataset_index_v2/` | 검색 문서(`chunks.jsonl`), 벡터 기록(`manifest.json`), 평가 질의 벡터. **`embeddings.npy`는 없음** |
| `ai/test/public_data/corpus_v2/data_version.json` | 고정 기록 |

`embeddings.npy`(126MB)는 GitHub 파일 한도를 넘어 Git에 넣지 않았다. 같은 벡터가 Supabase v2 테이블에 있으니 아래 2번으로 복원한다.

## 실행 순서 (`ai/` 폴더)

1. **고정 버전 확인**
   ```bash
   python public_v2_pipeline.py --verify-pin
   # public v2 matches the pinned data_version 04239c20eb394c12
   ```
2. **벡터 복원** (`.env`의 Supabase 접속 정보가 필요하다. 임베딩 API는 호출하지 않는다)
   ```bash
   python 20_sync_dataset_index.py --corpus v2 --restore-vectors
   ```
   - 다음 조건을 모두 만족할 때만 `dataset_index_v2/embeddings.npy`를 쓴다. 하나라도 어긋나면 아무것도 쓰지 않고 멈춘다.
     - DB의 빌드 기록이 고정 버전, 문서 버전, 임베딩 모델과 일치
     - 모든 청크의 벡터가 있음
     - 로컬 청크 순서대로 배치한 결과가 `vectors_sha256 62d7ba67…`와 같음
   - DB가 나중에 다른 빌드로 바뀌면 이 복원은 거부된다. 그때는 따로 보관한 복구용 사본을 쓴다.
3. **v2로 검색·평가**
   ```bash
   python -c "import hypergraph_search as hs; print(hs.use_corpus('v2'))"   # 그래프·문서·벡터 검사 통과 확인
   python 22_eval_recommendations.py --corpus v2 --public test/public_data/corpus_v2/golden_prep/batch3/labels_llm_v5.jsonl
   ```
   - 검색 모듈은 `MODEL_SCOUT_CORPUS=v2` 또는 `hs.use_corpus("v2")`로 v2를 쓴다. 기본값은 v1이다.
   - 골든셋은 팀 v5 기준으로 다시 정리 중이다. 이 스냅샷에 맞춘 라벨은 별도 PR로 올린다.

## 다시 빌드할 때 (같은 결과를 확인하는 경우)

```bash
python 18_enrich_public_datasets.py --offline          # 캐시와 저장 원문만 사용, 네트워크 없음
python 13_build_hypergraph.py --corpus v2 --model-snapshot data/model_snapshot/active_models_20261115.jsonl
python 14_build_dataset_chunks.py --corpus v2
python public_v2_pipeline.py --verify-pin             # 같은 data_version이 나와야 한다
```

- 그래프는 실시간 모델 테이블이 아니라 저장한 모델 목록 파일로 만든다(`--model-snapshot`).
- 해시는 텍스트를 LF 줄바꿈 기준으로 계산하므로 Windows와 Mac·Linux에서 같은 값이 나온다.

## Supabase v2 테이블

| 객체 | 내용 |
|---|---|
| `model_scout_datasets_v2` | 데이터셋 19,130행 |
| `model_scout_dataset_chunks_v2` | 청크 41,144행. **청크 전문**과 벡터(halfvec). v1은 600자 미리보기만 저장 |
| `model_scout_dataset_index_v2_meta` | 적재한 빌드 기록: `documents_id`, `corpus_id`, `data_version`, 모델 목록 해시, 벡터 해시, 임베딩 모델 |
| `match_model_scout_datasets_v2(halfvec)` | 데이터셋별 최고 유사도 |

- **적재:** `python 20_sync_dataset_index.py --corpus v2 --apply`
  - 그래프·문서·벡터 검사와 고정 버전 일치를 통과해야 실행된다.
  - `_v2` 테이블만 쓰고 지운다. v1 테이블은 건드리지 않는다.
  - 적재 후 ID, DB 본문, 빌드 기록, 검색 응답을 자동으로 확인한다.
- **v1 기본값 유지:** 인자 없이 실행하면 지금처럼 v1을 적재한다(`dataset-refresh.yml`).

## 아직 하지 않은 것

- **서비스 전환:** v2 DB 검색 경로 연결, 배포 스크립트, `MODEL_SCOUT_CORPUS=v2`
- **Actions의 v2 전환과 재개**
- **v1 제거:** 서비스 전환 후 v1 참조가 없는지 확인하고, 복구용 파일을 보관한 뒤 진행
- **골든셋 정리**
