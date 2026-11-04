# Model Scout

만들고 싶은 서비스를 자연어로 말하면 한국어 지원 모델과 데이터셋을 근거와 함께 추천합니다.

| 폴더 | 역할 | 스택 |
|---|---|---|
| [`frontend/`](frontend/) | 웹 UI (추천 스트리밍, 추가 질문, 모델 비교) | Next.js 15, TypeScript, Tailwind, pnpm |
| [`backend/`](backend/) | 공개 API `backend/app/main.py` (세션, 대화 이력, AI 호출) | FastAPI (SSE) |
| [`ai/`](ai/) | 내부 추천 API `ai/api.py`, 수집·임베딩·검색 파이프라인, 추천 그래프, 데이터 `ai/data/` ([상세 README](ai/README.md)) | Python 3.11, LangGraph |
| [`docs/`](docs/) | 기획 문서 | |

DB는 Supabase(Postgres + pgvector)를 사용합니다.

## 로컬 실행

**1. 환경 변수**

```bash
cp ai/.env.example ai/.env                    # Supabase, OpenAI 키 입력
cp frontend/.env.example frontend/.env.local  # 기본값: http://localhost:8000
```

**2. 백엔드** (`http://localhost:8000`)

```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend && uvicorn app.main:app --reload --reload-dir app
```

**3. 프론트엔드** (`http://localhost:3000`)

```bash
cd frontend && pnpm install && pnpm dev
```

## 폴더 간 규칙

- `ai/` 스크립트는 위치와 상관없이 데이터를 `ai/data/`에서 읽고 씁니다. 파이프라인 명령은 `ai/` 폴더에서 실행합니다.
- 데이터 파일 안에 저장된 경로(`data/readmes/...`)는 `ai/` 기준 상대 경로입니다.
- 백엔드 서버는 `ai/`의 추천 그래프(`17_recommend_graph.py`)를 import해서 사용합니다. 서버는 `ai/data/hypergraph/`와 `ai/data/dataset_index/manifest.json`을 파일로 읽으므로 배포 시 함께 포함해야 합니다.
- `ai/wiki/`(LLM 위키, Obsidian vault)는 git에 올리지 않습니다. `ai/`에서 `python 15_build_wiki.py`로 생성하며, GitHub Pages 배포(`wiki-pages.yml`)도 같은 방식으로 생성합니다.
- Docker(VPS 배포) 구성은 백엔드 담당자가 추가할 예정입니다.
