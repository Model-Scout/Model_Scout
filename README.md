# Model Scout

만들고 싶은 서비스를 자연어로 말하면 한국어 지원 모델과 데이터셋을 근거와 함께 추천합니다.

| 폴더 | 역할 | 스택 |
|---|---|---|
| [`frontend/`](frontend/) | 웹 UI (추천 스트리밍, 되묻기, 근거 확인, 설명 질문, 대화 복원) · 내장 mock API ([상세 README](frontend/README.md)) | Next.js 15, TypeScript, Tailwind, pnpm |
| [`backend/`](backend/) | 공개 API `backend/app/main.py` (세션, 대화 이력, AI 호출) | FastAPI (SSE) |
| [`ai/`](ai/) | 내부 추천 API `ai/api.py`, 수집·임베딩·검색 파이프라인, 추천 그래프, 데이터 `ai/data/` ([상세 README](ai/README.md)) | Python 3.11, LangGraph |
| [`docs/`](docs/) | 기획 문서 | |

DB는 Supabase(Postgres + pgvector)를 사용합니다.

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

**3. AI 내부 서버** (`http://localhost:8001`, 별도 터미널)

```bash
python ai/api.py
```

백엔드의 DB 설정은 프로세스 환경변수로 전달합니다. V2 실행 방법과 프론트 전달용 명세는 [`backend/README.md`](backend/README.md)를 참고하세요.

**4. 프론트엔드** (`http://localhost:3000`)

```bash
cd frontend && pnpm install && pnpm dev
```

프론트만 볼 때는 2·3번 없이 mock API(`NEXT_PUBLIC_API_URL=/api/mock`)로 실행됩니다.

## 폴더 간 규칙

- `ai/` 스크립트는 위치와 상관없이 데이터를 `ai/data/`에서 읽고 씁니다. 파이프라인 명령은 `ai/` 폴더에서 실행합니다.
- 데이터 파일 안에 저장된 경로(`data/readmes/...`)는 `ai/` 기준 상대 경로입니다.
- 백엔드는 내부 AI API `POST /ai/recommend`를 호출합니다. AI 서버가 추천 그래프(`17_recommend_graph.py`)와 검색용 파일을 로딩하므로 배포 시 해당 데이터를 AI 컨테이너에 포함해야 합니다.
- `ai/wiki/`(LLM 위키, Obsidian vault)는 git에 올리지 않습니다. `ai/`에서 `python 15_build_wiki.py`로 생성하며, GitHub Pages 배포(`wiki-pages.yml`)도 같은 방식으로 생성합니다.
- Docker(VPS 배포) 구성은 `deploy/compose.yml`과 서비스별 `Dockerfile`에 있습니다. 운영 적용 여부는 배포 환경에서 별도 확인합니다.
