# Model Scout

Model Scout는 자연어로 입력한 모델 요구사항에 맞는 한국어 지원 Hugging Face 모델을 찾아, 모델 카드의 근거와 함께 추천하는 프로젝트입니다. 현재는 모델 추천 파이프라인을 구현했으며, 서비스 아이디어에 필요한 공개 데이터까지 함께 찾는 확장안을 검토하고 있습니다.

AI 프로젝트를 준비할 때는 필요한 데이터를 찾고, 한국어 지원 여부와 개발 환경·이용 조건에 맞는 모델을 확인해야 합니다. Model Scout는 모델 metadata와 모델 카드의 원문 근거를 함께 제공해 이 선택을 돕습니다. 확인되지 않은 정보는 추측해서 채우지 않습니다.

## 현재 구현과 확장 제안

| 구분 | 내용 | 상태 |
|---|---|---|
| 모델 추천 | Hugging Face 한국어 지원 모델 3,606개에서 조건에 맞는 모델을 근거와 함께 추천 | 구현됨 |
| 데이터 추천 | 공개 데이터 카탈로그에서 필요한 데이터를 찾아 출처·제공 기관·형식·이용 조건 안내 | 확장 제안 · 논의 중 |
| 아이디어 분해 | 서비스 아이디어를 필요한 데이터와 AI 기능으로 나누고, 일반 API로 충분한 기능도 구분 | 확장 제안 · 논의 중 |
| 통합 답변 | 데이터와 필요한 경우의 모델 추천을 하나의 착수 가이드로 제공 | 확장 제안 · 논의 중 |

## 사용 예시

현재는 "한국어 요약 모델, 8B 이하, 상업 이용 가능한 후보" 같은 모델 요구사항에 대해 후보와 모델 카드 근거를 제공합니다. 확인되지 않은 조건은 별도로 확인해야 하며, 실제 실행 가능성과 이용 조건은 해당 모델 문서에서 추가로 확인해야 합니다.

**확장 후 목표 — 아직 구현되지 않은 응답 예시**

> 주차장 위치를 찾아주는 AI 앱을 만들고 싶어.

- 필요한 데이터: 주차장 좌표·요금·운영 시간·주차면 수, 가능하다면 실시간 잔여 면수
- 데이터 추천: 카탈로그에서 확인한 데이터의 출처·제공 기관·형식·이용 조건·제공 범위
- AI 기능: “강남역 근처 저렴한 주차장” 같은 자연어를 검색 조건으로 변환
- AI 없이 가능한 기능: 위치 기반 검색, 지도 표시, 거리순 정렬
- 판단: 데이터와 지도 API만으로 MVP를 만들 수 있으며, 자연어 검색이 필요하면 한국어 모델 후보를 추가로 추천

이 예시는 응답의 형태를 설명합니다. 실제 데이터의 존재와 제공 항목·이용 조건은 카탈로그 조사 및 구현 단계에서 확인합니다.

## 확장 MVP 범위 제안

MVP 데이터 소스는 **공공데이터포털**을 우선 검토합니다. 포함할 기능은 아이디어 분해, 데이터 카탈로그 수집·검색, 출처와 이용 조건 안내, 기존 모델 검색과의 결과 통합, AI 필요도 판단입니다.

실제 데이터 다운로드·가공, 실시간 오픈 API 호출, AI Hub·Hugging Face Datasets 연동, 코드 생성·아키텍처 자동 설계, 라이선스의 법적 판단은 MVP 범위에서 제외하는 제안입니다. 데이터 소스의 수집 방식과 약관, 사용자 제공 형태(웹 UI·MCP·에이전트), 단계별 담당자는 추가 논의가 필요합니다.

모델 검색 골든셋 평가를 마무리한 뒤 카탈로그 조사와 확장 구현을 진행하는 순서를 제안합니다.

확장 기획서는 [`docs/index.html`](docs/index.html)에 있습니다. 2026-10-02 기준 초안·논의 중이며, 브라우저로 열어 볼 수 있습니다. 수정 규칙은 [`docs/AGENTS.md`](docs/AGENTS.md)에 있습니다.

## 설치와 실행

프로젝트 루트에서 Python 가상환경을 만들고 의존성을 설치합니다.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

프로젝트 루트의 `.env`에 실행할 기능에 필요한 값을 설정합니다. 실제 키와 비밀번호는 저장소에 커밋하지 않습니다.

```dotenv
HF_TOKEN=<Hugging Face token>
OPENAI_API_KEY=<OpenAI API key>
SUPABASE_DB_HOST=<database host>
SUPABASE_DB_PORT=5432
SUPABASE_DB_NAME=<database name>
SUPABASE_DB_USER=<database user>
SUPABASE_PASSWORD=<database password>
```

`HF_TOKEN`은 모델 수집에 사용하며, `OPENAI_API_KEY`는 semantic 생성과 임베딩 API 호출에 필요합니다. Supabase 연결 값은 DB 적재·동기화에 필요합니다. 기존 snapshot으로 검색을 검증하려면 다음 명령을 사용합니다.

```bash
python 05_validate_retrieval.py --execute
python test/evaluate_retrieval_modes.py
```

`--execute`는 OpenAI 임베딩 API를 호출하므로 비용이 발생할 수 있습니다. DB 적재·갱신은 **Supabase와 TTL 자동화**, 회귀 테스트는 **검증** 절을 참고하세요. MCP·LangChain 연동에는 선택 의존성인 `requirements_mcp.txt`를 사용합니다.

아래 내용은 현재 구현된 **모델 추천 파이프라인**에 대한 설명입니다. 모델 추천은 한국어 지원 근거, task, 라이선스, 파라미터 수, context length, 양자화, 실행 환경, semantic claim과 benchmark 정보를 하나의 검색 문서로 결합합니다.

## 현재 상태

수량은 2026-09-28 snapshot 기준입니다.

- 추천 corpus는 Core 1,478개와 Low Popularity 2,128개, 총 3,606개입니다.
- Stage 1의 Likely 2,100개와 Fallback 14,244개는 참고 후보이며 Stage 2~4와 추천 검색 corpus에는 넣지 않습니다.
- Stage 4 임베딩은 `text-embedding-3-small`, 1,536차원입니다.
- Supabase에는 모델 검색 행과 Parent–Child evidence 행을 함께 적재합니다.
- Stage 1~4 생성 및 기본 검증을 완료했습니다.

```mermaid
flowchart LR
    H[Hugging Face Hub] --> S1[Stage 1 후보 수집]
    S1 --> S2[Stage 2 기술 metadata]
    S2 --> S3[Stage 3 semantic evidence]
    S3 --> S4[Stage 4 embedding document]
    S4 --> DB[(Supabase pgvector)]
    Q[사용자 질의] --> R[hard filter + dense/sparse/hybrid 검색]
    DB --> R
    R --> A[추천 모델 + 근거 + 상세 metadata]
```

## 파이프라인

| 단계 | 스크립트 | 역할 |
|---|---|---|
| 1 | `01_collect_models.py` | 9개 task의 후보 수집, 다운로드 tier, Korean evidence, canonical/variant grouping |
| 2 | `02_enrich_metadata.py` | config, tokenizer, artifact, license, parameter/context, quantization, runtime metadata |
| 3 | `03_generate_semantic_metadata.py` | README를 LLM으로 요약하고 장점·제한·용도·claim별 evidence를 생성 |
| 3 보조 | `03_repair_truncated_semantic.py`, `evidence_index.py` | 긴 README 보강과 Parent–Child evidence index 생성 |
| 4 | `04_build_embeddings.py` | 검색용 `embedding_text`와 1,536차원 임베딩 생성 |
| benchmark | `06_extract_benchmark_metadata.py` | README/model-index benchmark를 보수적으로 추출 |
| 동기화 | `08_sync_supabase.py` | schema 검증, 초기 적재, TTL 증분 처리, evidence backfill |
| 검색 검증 | `05_validate_retrieval.py` | 검색, hard filter, conflict penalty, evidence 회귀 검증 |

`07_integrate_benchmark_metadata.py`는 이전 수동 실행과의 호환용 래퍼입니다. 새 전체·증분 파이프라인에서는 `06_extract_benchmark_metadata.py`를 사용합니다. `benchmark_metadata.py`는 benchmark 추출 모듈이고 `task_conflict.py`는 별도 의존 파일로 사용하지 않습니다.

## Stage 1 수집 기준

<details>
<summary>대상 task와 후보 분류 기준 보기</summary>


대상 pipeline tag는 다음 9개입니다.

`text-generation`, `feature-extraction`, `sentence-similarity`, `text-classification`, `question-answering`, `summarization`, `translation`, `image-text-to-text`, `automatic-speech-recognition`

주요 설정은 `MIN_DOWNLOADS=80`, `CORE_DOWNLOADS=500`, `LIMIT_PER_TASK=None`, `CUTOFF_CONFIRMATION=10`입니다.

- Core: 다운로드 수 500 이상이며 `A_verified`인 후보
- Low Popularity: 다운로드 수 80~499이며 `A_verified`인 후보
- Likely: `B_likely` 참고 후보
- Fallback: `C_fallback` 참고 후보

`A_verified`는 Hub metadata, 언어 tag, 번역 pair, 모델명 근거를 조합한 수집 분류입니다. 이름 기반 근거는 metadata 기반 근거보다 약하므로 candidate type과 evidence strength를 별도로 보존합니다. 다운로드 수는 품질 점수가 아니라 오프라인 우선순위 신호입니다. canonical group과 variant는 중복 노출을 줄이는 데 사용하며, 원본 variant 정보는 보존합니다.

Stage 1은 지정한 9개 pipeline tag와 Hub API 응답 범위만 다룹니다. 다른 tag이거나 pipeline tag가 없는 모델은 자동으로 포함되지 않을 수 있습니다. 빈 API 응답, task 실패, 급격한 snapshot 감소는 fail-closed로 처리하며 기존 snapshot을 유지합니다.

</details>

## Stage 2 metadata

config, tokenizer config, artifact index, README에서 다음 필드를 추출합니다.

- task, language, architecture, base model, artifact와 model format
- license, parameter count, context length, quantization
- CPU, CUDA, MPS, vLLM, ONNX, llama.cpp의 문서·artifact 기반 runtime compatibility
- popularity, canonical lineage, source와 confidence

확인되지 않은 값은 `null` 또는 `unknown`으로 남깁니다. `runtime_compatibility`는 문서에서 확인한 실행 가능성 신호이며 실제 실행 성공을 보증하지 않습니다. parameter count와 context length도 source/confidence를 함께 확인해야 합니다.

## Stage 3 semantic evidence

`03_generate_semantic_metadata.py`는 README를 atomic evidence 단위로 나누고, LLM이 만든 각 claim에 `evidence_refs`와 `supporting_quote`를 연결합니다. section-aware 계층 정보와 Parent–Child 관계는 `evidence_index.py`가 deterministic하게 생성합니다. README가 없는 모델은 Core 4개, Low Popularity 6개이며 `no_source` metadata-only 상태로 보존합니다.

현재 README snapshot은 Core 1,474개, Low Popularity 2,122개입니다. 원본 snapshot에서 잘림이 남은 모델은 Core 7개, Low Popularity 12개입니다. 긴 README 보강은 Core 41개와 Low Popularity 84개에 수행했습니다. 잘림이나 README 부재가 있더라도 확인되지 않은 내용을 추측해 채우지 않습니다.

## Stage 4와 검색 문서

Stage 4는 모델 identity, task, language, 기술 metadata, runtime, popularity, Stage 3 semantic claim, benchmark projection을 `embedding_text`로 구성합니다. `--execute`에서만 임베딩 API를 호출하고, 증분 sync에서는 변경된 model ID만 처리합니다. DB에 동일한 `document_hash`가 있으면 기존 임베딩을 재사용합니다.

운영 검색 저장소는 Supabase pgvector입니다. 로컬 Stage 4 JSONL은 snapshot과 재현성을 위해 보관하지만, 검색 결과 상세 정보는 model row와 evidence row를 hydrate해서 제공합니다.

## Benchmark projection

`06_extract_benchmark_metadata.py`는 README와 `model-index`에서 dataset, metric, split, config, 점수, quote를 보수적으로 추출합니다.

- 숫자 없이 benchmark 이름만 있으면 `mentions`로 보존합니다.
- 모델명과 점수의 연결이 불명확하면 ranking signal로 사용하지 않습니다.
- architecture, parameter, context, quantization 표는 benchmark 점수로 분류하지 않습니다.
- 서로 다른 dataset, metric, split, config의 점수는 직접 비교하지 않습니다.
- README self-reported 수치는 오래됐거나 실험 조건이 다를 수 있으므로 hard filter나 모델 카드 근거를 대체하지 않습니다.

따라서 benchmark는 보조 순위 신호이며, 단독으로 추천을 결정하지 않습니다.

## Supabase와 TTL 자동화

스키마는 `supabase_schema.sql`, 적재와 검증은 `08_sync_supabase.py`가 담당합니다.

| 테이블 | 역할 |
|---|---|
| `model_scout_models` | 3,606개 모델의 compact metadata, Stage 2·3 상세 정보, benchmark projection, 1,536차원 vector |
| `model_scout_evidence` | Parent section, Child claim, supporting quote, evidence hash |
| `model_scout_sync_runs` | 초기 적재와 증분 sync 이력 |

최초 적재:

```bash
python 08_sync_supabase.py --ensure-schema
python 08_sync_supabase.py --initial --apply
```

최초 적재 뒤에는 전체 snapshot을 다시 올리지 않습니다. GitHub Actions 또는 수동 실행으로 변경 모델만 Stage 2~4와 benchmark projection을 거쳐 upsert합니다.

```bash
python 08_sync_supabase.py --refresh --apply
```

TTL 기본값은 24시간이며, 변경하려면 `.env` 또는 실행 환경에 `MODEL_SCOUT_TTL_HOURS`를 설정합니다. 후보에서 탈락한 모델은 `active=false`로 비활성화합니다. `--force`는 전체 갱신이 아니라 TTL 검사만 건너뜁니다. 필요한 경우 다음 backfill을 사용합니다.

```bash
python 08_sync_supabase.py --backfill-runtime --apply
python 08_sync_supabase.py --backfill-search-metadata --apply
python 08_sync_supabase.py --backfill-evidence --apply
```

GitHub Actions에는 `HF_TOKEN`, `OPENAI_API_KEY`, `SUPABASE_DB_HOST`, `SUPABASE_DB_PORT`, `SUPABASE_DB_NAME`, `SUPABASE_DB_USER`, `SUPABASE_PASSWORD` secrets가 필요합니다. 성공한 sync만 snapshot과 benchmark fingerprint를 갱신하고, 실패한 run은 기존 snapshot과 DB row를 교체하지 않습니다.

## 검증

```bash
python 05_validate_retrieval.py --execute
python test/evaluate_retrieval_modes.py
python -m pip install pytest
python -m pytest -q --disable-warnings test/test_stage1_collection.py test/test_stage3_pool_reconciliation.py test/test_benchmark_metadata.py test/test_recommendation_quality.py
```

검증에서는 task, 한국어 조건, parameter/context, popularity, task conflict, canonical 중복, evidence reference와 supporting quote를 확인합니다. 추천 결과는 실제 모델 실행 성공이나 라이선스 법률 자문을 의미하지 않습니다.

## 운영상 남은 비용

<details>
<summary>TTL 실행 시 남는 파일 I/O 비용 보기</summary>

TTL 실행 때도 다음 deterministic 비용은 남아 있습니다.

1. benchmark fingerprint를 확인하기 위한 README snapshot 전체 1회 스캔
2. Parent–Child evidence index의 전체 JSONL 스캔
3. 원자적 snapshot 교체를 위한 Stage 2·3 JSONL 전체 읽기·쓰기

이 비용들은 LLM 재호출이나 임베딩 재생성이 아니라 파일 I/O입니다. 변경 feed나 별도 변경 인덱스를 도입할 때 줄일 수 있으며, 현재 자동화의 안전성을 위해 의도적으로 유지합니다.

</details>

## 주요 파일

- `README.md`: 프로젝트와 운영 개요
- `docs/index.html`: 데이터 추천 확장 기획서 (수정 규칙은 `docs/AGENTS.md`)
- `data/README.md`: snapshot 파일과 수량
- `test/README.md`: 골든셋과 검색 평가 방법
- `retrieval_lab/README.md`: 쿼리 유형별 Pre-Retrieval·Retrieval 실험과 Retrieval Planner
- `requirements_retrieval.txt`: 실험용 의존성 (BGE-M3, Optuna)
- `requirements.txt`: 수집·Stage 1~4 의존성
- `requirements_mcp.txt`: MCP/LangChain 선택 의존성
