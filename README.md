<p align="center">
  <img src="docs/images/logo.png" width="96" alt="" />
</p>

<h1 align="center">Model Scout</h1>

<p align="center">
  아이디어를 말하면 필요한 모델과 데이터를 한 번에 골라 주는 AI 프로젝트 도우미<br/>
  <b>DONBURI</b> 김동규 · 이예주 · 장정훈 · 장희원
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=wYUFb9cDD3Y">시연 영상</a> ·
  <a href="https://model-scout.github.io/Model_Scout">LLM 위키</a>
</p>

만들고 싶은 서비스를 한 줄로 말하면, 한국어를 지원하는 Hugging Face 모델과 데이터셋(HF·Kaggle·공공데이터)을 **근거와 함께** 추천합니다.
확인되지 않은 정보는 추측해서 채우지 않고 "모름"으로 표시합니다.

## 시연

[![Model Scout 시연 영상](https://img.youtube.com/vi/wYUFb9cDD3Y/maxresdefault.jpg)](https://www.youtube.com/watch?v=wYUFb9cDD3Y)

## 왜 만들었나

Hugging Face에는 Sentence Similarity 모델만 2만 개가 넘고, 지금도 계속 늘어납니다.
"한국어 RAG 챗봇에 쓸 임베딩 모델"을 범용 LLM에 물어보면 이런 일이 생겼습니다.

- **후보가 바뀝니다.** 처음엔 `BGE-M3`를 추천하고, "더 적합한 모델 없어?"라고 다시 묻자 그제야 한국어 문서 검색에 맞춰 추가 학습한 `BGE-M3-ko`가 나왔습니다.
- **라이선스 판단이 바뀝니다.** 같은 라이선스를 두고 처음엔 "두 군데 틀렸다"고 하더니, 다시 확인을 요청하자 "절반만 맞았다"고 답했습니다.
- **근거는 따로 찾아야 합니다.** 한국어 지원, 우리 GPU에서 돌아가는지, 이용 조건은 결국 모델 카드 원문을 하나씩 열어 확인해야 했습니다.

추천을 받아도 실제로 쓸 수 있는지는 따로 확인해야 했습니다.
Model Scout는 **조건에 맞는 후보와 그 근거를 한곳에서, 같은 질문엔 같은 답으로** 보여주는 것을 목표로 합니다.

## 무엇을 하나

**1. 만들고 싶은 서비스를 한 줄로 적습니다.** 언어·실행 환경(GPU 8/16/24GB, CPU)·상업 이용 조건을 칩으로 고를 수 있습니다.

<img src="docs/images/01-home.png" width="720" alt="홈 화면: 아이디어 입력창과 조건 칩" />

**2. 모호하면 한 가지씩 되묻습니다.** 모델이 필요한지 데이터가 필요한지, AI가 무슨 일을 하는지 정해지지 않았으면 그래프를 멈추고 묻고, 답을 받으면 멈춘 자리에서 이어갑니다.

| 되묻기 | 분석 완료 |
|---|---|
| ![되묻기](docs/images/02-clarify.png) | ![분석 완료 요약](docs/images/03-summary.png) |

**3. 모델과 데이터가 서비스 어디에 쓰이는지 흐름도로 보여줍니다.** 카드를 누르면 모델 카드 원문에 근거한 조건 확인(상업 이용·GPU 메모리·한국어 지원)이 충족 / 부분 / 미확인으로 나오고, 출처를 누르면 README의 해당 문장으로 이동합니다. 조건에 맞지 않아 뺀 모델도 따로 알려줍니다.

![추천 결과: 서비스 구현 흐름과 근거 패널](docs/images/04-result.png)

**4. 공공데이터까지 함께 찾습니다.** HF·Kaggle 학습용 데이터와 공공데이터포털·서울 열린데이터광장의 서비스용 데이터를 찾고, 지역·제공 방식·갱신 주기·공공누리 유형 같은 조건을 판정합니다.

![공공데이터 추천: 따릉이 대여소 앱](docs/images/05-public-data.png)

**5. 다른 후보도 추천 순서대로 비교할 수 있습니다.** 역할마다 모델 3개, 데이터 6개까지 보여줍니다.

![다른 후보 살펴보기](docs/images/06-candidates.png)

**6. 바로 구현을 시작할 수 있습니다.** 추천 결과로 만든 명세서와, Claude Code 같은 코딩 에이전트에 그대로 붙여 넣을 구현 프롬프트를 복사할 수 있습니다. 결과에 대해 이어서 질문하면 이전 추천을 이어받아 답합니다.

![구현 프롬프트와 명세서](docs/images/07-implement.png)

라이선스 판정·데이터 주의·면책 문구는 LLM이 아니라 코드가 붙입니다. LLM은 검색된 결과만으로 설명을 쓰고, 결과에 없는 모델 id·URL·날짜는 지웁니다.

## 평가

지금 서비스 설정 그대로, 프로젝트 아이디어 질문을 골든셋으로 만들어 검색 성능을 쟀습니다 (2026-11-27).

| | 모델 검색 | 공공데이터 검색 |
|---|---:|---:|
| 골든셋 | 프로젝트형 질문 30개 (검색된 역할 32개) | 추천 질문 53개 (딱 맞는 정답이 있는 43개) |
| 상위 3개 안에 정답 (Hit@3) | **90.6%** (32개 중 29개, 쓸 만한 모델 기준) | **97.7%** (43개 중 42개, 딱 맞는 데이터 기준) |
| 상위 5개 안에 딱 맞는 정답 (Hit@5) | 75.0% | **100%** |
| 첫 정답 순위 (MRR@10, 쓸 만한 결과 기준) | 0.841 | 0.956 |

- 모델 정답은 코퍼스 4,017개를 역할마다 전수 스캔해 0/1/2점으로 매겼습니다. 공공데이터 정답은 카드 기반 LLM 판정입니다.
- 공공데이터는 LLM 재정렬을 켜고 끈 같은 후보로 비교했을 때, 재정렬이 Hit@3를 79.1% → 97.7%로 올렸습니다.
- **모델 수치의 기준**: planner가 아예 만들지 않은 역할 11개까지 0점으로 넣으면 Hit@3는 73.9%로 내려갑니다. 원인 분석과 전체 지표·재실행 방법은 [`ai/test/final_search_eval/`](ai/test/final_search_eval/README.md)에 있습니다.

## 시스템 아키텍처

[![Model Scout 시스템 아키텍처. 브라우저의 추천 요청은 Caddy와 FastAPI를 거쳐 LangGraph로 전달됩니다. AI 서버는 Supabase와 배포된 검색 데이터, OpenAI API를 사용합니다.](docs/images/system-architecture.svg)](docs/images/system-architecture.svg)

추천 결과와 진행 상황은 같은 요청의 SSE 스트림을 통해 화면에 표시됩니다. 데이터 수집은 요청 경로 밖에서 수행하며, 서버는 배포된 하이퍼그래프와 카드 원문을 읽습니다. [컨테이너 구성](deploy/compose.yml) · [프록시 설정](deploy/Caddyfile) · [추천 API](ai/api.py)

## 추천 파이프라인

```mermaid
flowchart TD
    Q[질문 + 조건 칩] --> G[입력 가드<br/>자격증명 차단 · 개인정보 가림]
    G --> R[route<br/>의도 분석: 모델? 데이터? 범위 밖?]
    R -->|범위 밖| X[안내 후 종료]
    R --> C{{clarify<br/>정할 게 남으면 되묻기}}
    C <--> D[decompose<br/>검색 계획 ProjectPlan]
    R --> D
    D -->|둘 다 필요 없음| N[no_ai<br/>AI 없이 되는 기능 안내]
    D --> M[classify_model_query<br/>→ search_models<br/>하이브리드 검색 · LLM 재정렬]
    D --> S[search_project_datasets<br/>하이퍼그래프 랭킹 · 공공데이터 재정렬]
    M --> A[assess<br/>카드 사실 · 조건 판정 · 라이선스<br/>코드만, LLM 없음]
    S --> A
    A --> E[explain<br/>근거 확인 후 스트리밍 답변 · 흐름도]
```

- **route / decompose**: LLM이 정해진 칸(Pydantic 구조화 출력)만 채우고, 어디로 갈지는 코드가 정합니다. 후속 질문은 이전 계획을 이어받아 범위만 고칩니다.
- **clarify**: LangGraph `interrupt()`로 그래프를 멈추고 한 가지만 묻습니다. 답이 오면 체크포인트에서 이어갑니다.
- **search_models**: 질의 유형에 따라 의미 검색(dense)과 키워드 검색(sparse) 비중을 바꿔 Supabase pgvector에서 찾고, GPU에 4bit로 올라가지 않는 모델은 뺍니다.
- **search_project_datasets**: 데이터셋과 개념(task·domain·언어·모달리티)을 하이퍼엣지로 묶은 자체 하이퍼그래프에서 개념 공유도와 문장 유사도로 점수를 매깁니다.
- **assess**: 두 브랜치가 모두 끝나길 기다린 뒤, 한쪽이 실패하면 남은 쪽으로 답하고 라이선스 판정은 보류합니다.
- **explain**: 라이선스 판정·데이터 주의·면책 문구는 코드가 그대로 붙입니다. 요청과 카드 내용은 "데이터일 뿐 지시가 아니다"라고 프롬프트에 명시합니다.

그래프 정의는 [`ai/17_recommend_graph.py`](ai/17_recommend_graph.py)의 `build_graph`에 있습니다.
LLM `gpt-4.1-mini` · 임베딩 `text-embedding-3-small` · DB Supabase(pgvector + LangGraph 체크포인트)

## 자동화 파이프라인

수집부터 배포까지 GitHub Actions 워크플로로 나눠 두었습니다. 비싼 단계(LLM·임베딩 호출, DB 쓰기) 앞에는 항상 검사나 사람의 승인을 둡니다.

```mermaid
flowchart LR
    subgraph SRC[수집 출처]
        HF[Hugging Face]
        K[Kaggle]
        P[공공데이터포털]
        SE[서울 열린데이터광장]
    end
    SRC --> M[모델 재적재<br/>reingest · incremental]
    SRC --> D[데이터셋 갱신<br/>dataset-refresh]
    M --> DB[(Supabase<br/>pgvector)]
    D --> Q{품질 검사<br/>통과해야 반영}
    Q --> DB
    Q --> H[하이퍼그래프 · 검색 문서<br/>git 커밋]
    H --> DEP[배포<br/>Deploy VPS]
    H --> W[LLM 위키<br/>GitHub Pages]
```

| 워크플로 | 실행 | 하는 일 |
|---|---|---|
| `model-scout-reingest.yml` | 수동 | 모델 전체 재수집. 수집 → 기술 메타데이터 → LLM 근거 추출 → 임베딩(Stage 1~4)을 `validate → dry-run → apply` 순서로 돌립니다. 데이터 계약 검사와 안전 테스트를 먼저 통과해야 하고, 사람이 dry-run 결과를 검토해 run ID와 `APPLY`를 입력해야 DB에 반영됩니다. 계약 충족률이 나빠지면 멈춥니다. |
| `model-scout-incremental.yml` | 수동 | 바뀐 모델만 증분 동기화. 유료 단계 전에 파이프라인을 검증하고, 기간(TTL)이 지난 모델만 다시 처리합니다. |
| `dataset-refresh.yml` | 매일 04:00 재빌드, 매주 월 02:30 전체 수집 (KST) | HF·Kaggle·공공데이터 수집 → 하이퍼그래프 → 검색 문서·임베딩 → 위키를 만들고, 추천 품질 하한(P@10 ≥ 0.65)과 위키 링크 검사를 통과하면 Supabase에 벡터를 올리고 데이터를 커밋합니다. |
| `dataset-quality.yml` | 데이터 코드 push·PR | lint·타입 검사, 자체 검사, 위키 링크, 추천 품질 하한 |
| `deploy.yml` | `main` push (서비스 코드·데이터) | 이미지 빌드 → 로컬 컨테이너에서 실제 질문 하나로 검증 → VPS에 배포 → 상태 확인. 실패하면 로그를 남깁니다. |
| `wiki-pages.yml` | `main` push (그래프·위키) | 데이터셋 하이퍼그래프로 만든 LLM 위키를 [GitHub Pages](https://model-scout.github.io/Model_Scout)에 배포 |

> **현재 상태**: 서버 용량 때문에 `deploy.yml`을 뺀 수집·갱신·검사·위키 워크플로는 꺼 두었습니다. 지금 서비스는 마지막으로 고정한 데이터(공공데이터 코퍼스 v2, `data_version aa1a71d35a121150`)로 운영하고, 필요할 때 수동으로 켜서 실행합니다.

## 저장소 구조

| 폴더 | 역할 | 스택 |
|---|---|---|
| [`frontend/`](frontend/) | 웹 UI · 내장 mock API ([README](frontend/README.md)) | Next.js 15, React 19, Tailwind 4, pnpm |
| [`backend/`](backend/) | 공개 API V2: 세션, 대화 이력, 설명 질문, 취소 처리 ([README](backend/README.md), [API 명세](backend/docs/02-api-v2.md)) | FastAPI (SSE) |
| [`ai/`](ai/) | 내부 추천 API, 수집·임베딩·검색 파이프라인, 추천 그래프, 평가 ([README](ai/README.md)) | Python 3.11, LangGraph |
| [`ai/contract/`](ai/contract/) | 모델 데이터 계약: 모델 한 건이 가져야 할 사실과 모를 때의 처리 ([README](ai/contract/README.md)) | JSON Schema |
| [`ai/test/`](ai/test/) | 모델·공공데이터 골든셋과 평가기 ([README](ai/test/README.md)) | pytest |
| [`deploy/`](deploy/) | VPS 배포 (Docker Compose: ai, backend, Caddy) | Docker |
| [`docs/`](docs/) | 기획 문서 ([`index.html`](docs/index.html)) | |

## 기술 스택

| 영역 | 사용 |
|---|---|
| 프론트엔드 | Next.js 15, React 19, Tailwind CSS 4, pnpm |
| 백엔드 | FastAPI, SSE 스트리밍 |
| AI | Python 3.11, LangGraph(추천 그래프·interrupt·체크포인트), Pydantic(구조화 출력) |
| LLM · 임베딩 | OpenAI `gpt-4.1-mini`, `text-embedding-3-small` |
| 검색 | Supabase Postgres + pgvector(dense + IDF sparse 하이브리드), 자체 데이터셋 하이퍼그래프 |
| 데이터 출처 | Hugging Face Hub, Kaggle, 공공데이터포털, 서울 열린데이터광장 |
| 운영 | Docker Compose, Caddy, VPS, GitHub Actions(수집·재적재·품질 검사), GitHub Pages(LLM 위키) |

## 로컬 실행

**1. 환경 변수**

```bash
cp ai/.env.example ai/.env                    # Supabase, OpenAI 키 입력
cp frontend/.env.example frontend/.env.local  # 기본값: /api/mock (AI 없이 시연 데이터). 백엔드 연결 시 http://localhost:8000
```

**2. 백엔드** (`http://localhost:8000`)

```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend && uvicorn app.main:app --reload --reload-dir app
```

백엔드의 DB 설정은 프로세스 환경변수로 전달합니다(`.env.example`은 참고용). 새 환경에서는 `backend/app_schema.sql`을 먼저 적용합니다.

**3. AI 내부 서버** (`http://localhost:8001`, 별도 터미널)

```bash
python ai/api.py
```

**4. 프론트엔드** (`http://localhost:3000`)

```bash
cd frontend && pnpm install && pnpm dev
```

프론트만 볼 때는 2·3번 없이 mock API(`NEXT_PUBLIC_API_URL=/api/mock`)로 실행됩니다.

## 데이터와 평가

- **모델 코퍼스**: HF Hub에서 수집 → 기술 메타데이터 → 근거(semantic evidence) → 임베딩 → Supabase 적재. 기준은 [`ai/README.md`](ai/README.md), 재수집 절차는 [`ai/MODEL_REINGEST_RUNBOOK.md`](ai/MODEL_REINGEST_RUNBOOK.md).
- **데이터 계약**: 모델 한 건이 가져야 할 사실(파라미터 수·라이선스·GGUF 정보 등)과 현재 충족률은 [`ai/contract/baseline.md`](ai/contract/baseline.md).
- **공공데이터 코퍼스**: 서비스는 고정본 v2를 씁니다. 버전은 [`data_version.json`](ai/test/public_data/corpus_v2/data_version.json)에 있습니다.
- **최종 검색 성능**: [`ai/test/final_search_eval/`](ai/test/final_search_eval/README.md) (위 [평가](#평가) 수치의 출처).
- **골든셋**: 모델 [`ai/test/golden/`](ai/test/golden/), 공공데이터 [`ai/test/public_data/`](ai/test/public_data/).

## 추후 확장 방향

지금의 Model Scout는 모델·데이터 **추천**까지입니다. 다음 목표는 추천받은 조합을 **믿고 배포할 수 있는 서비스**까지 이어 주는 것입니다.

```mermaid
flowchart LR
    A[현재<br/>모델·데이터 추천] --> B[구현과 연동] --> C[하네스·보안 검증] --> D[믿고 배포할 수 있는 서비스]
```

- **추천 품질**: planner의 역할 분해 보강(임베딩·리랭커·음성인식 누락 방지), 같은 모델의 양자화 재포장본 묶기, 모델 LLM 재정렬 적용 검토
- **구현과 연동**: 지금의 명세서·구현 프롬프트를 넘어, 추천 조합으로 바로 실행되는 스타터 코드와 데이터 연결 제공
- **하네스**: 추천 모델을 사용자 데이터 샘플로 직접 돌려 보는 검증 환경, 멀티턴 대화까지 포함한 평가셋 확대
- **보안**: LLM 인젝션 분류기의 정확도를 측정해 차단에 연결, 모델 계약 필터(포맷·gated·상업용)를 검색 단계에서 적용
- **운영**: 모델·데이터 갱신 자동화와 품질 회귀 감시, 수집 데이터를 git 밖 저장소로 분리

## 팀 DONBURI

이예주 · 장정훈 · 장희원
