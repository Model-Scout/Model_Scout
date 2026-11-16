# 실제 DB·API 통합 진행 기록

기준: 2026-11-13 · 작업 브랜치: `feat/yj`

## 이번에 확인한 내용

- `feat/query-router`를 `feat/yj`로 이름 변경했다. 기존 프론트 lockfile 수정은 보존했다.
- 로컬 설정은 루트 `.env`에 있고 `ai/.env`, `backend/.env`는 없다. 비밀값은 기록하지 않는다.
- `backend/check_db.py --env-file .env`로 실제 Supabase에 읽기 전용 접속했다.
- `app.groups`, `app.messages`와 백엔드에 필요한 컬럼, SELECT/INSERT/UPDATE 기본 권한을 확인했다.
- 실제 DB를 연결한 FastAPI TestClient에서 `/api/health`, 새 임의 세션의 `/api/groups`가 200이었다.
- 위 목록 조회에서 새 세션의 빈 목록과 localhost:3000 CORS 허용을 확인했다.
- AI 추천 그래프 import, 기본 하이퍼그래프 로딩, README 디렉터리 존재를 확인했다.
- 로컬 `dataset_index/embeddings.npy`는 없다. Supabase 벡터 fallback은 아직 실행 검증하지 않았다.
- 기존 백엔드 테스트 전체: **26 passed**. HTTP 테스트는 제한 환경에서 멈춰 제한 밖에서 재실행했다.
- DB 스키마·데이터 변경, 실제 LLM 호출, 프론트 연결 설정 변경, 배포는 하지 않았다.

## 로컬 E2E (API) 확인 — 2026-11-13

- 백엔드(8000)와 AI(8001)를 루트 `.env`로 실행했다. 시작할 때 30일 지난 체크포인트 정리가 정상 실행됐다.
- `POST /api/chat` 추천 1건: 토큰 스트리밍 후 done까지 약 65초. 로컬 `embeddings.npy`가 없어 데이터셋 검색은 Supabase로 처리했다.
- `GET /api/groups`, `GET /api/groups/{id}`: user/assistant 메시지, result(candidates·assessment), sources 38개가 복원됐다.
- 같은 그룹에 `mode=question` 추가 질문: 약 4초에 답했고 메시지 4개가 저장됐다. 실제 DB 쓰기(RLS·시퀀스)를 확인했다.
- 모호한 질문("앱 만들고 싶어")은 `type=clarify`와 질문 3개를 돌려줬다. 같은 group_id로 답하자 추천이 재개됐다(약 52초, 후보 35개).
- 프론트: `frontend/.env.local`(gitignore)을 `NEXT_PUBLIC_API_URL=http://localhost:8000`으로 바꿨다. 번들에 반영된 것과 localhost:3000 CORS preflight 200을 확인했다. 브라우저 화면 확인은 아직 하지 않았다.
- 주의: Windows Git Bash에서 curl 인자로 한글 JSON을 보내면 400이 난다. UTF-8 파일(`--data-binary @file`)로 보낸다.

## 다시 실행할 명령

저장소 루트에서 실행한다. 실행 환경에 이미 설정한 변수는 dotenv보다 우선한다.

```powershell
./.venv/Scripts/python.exe backend/check_db.py --env-file .env
./.venv/Scripts/python.exe -m pytest backend/tests -q
```

서버 실행 방법은 [백엔드 README](README.md)의 DB 적용 절차를 참고한다.
프론트 lockfile은 이번 통합 작업 이전 변경이므로 임의로 되돌리지 않는다.

## 다음 작업 순서

1. 실제 AI 검색 확인: 모델 검색 RPC, 임베딩 요청, 데이터셋 벡터 fallback.
2. AI 서버 시작 전 기존 시작 동작 점검: 체크포인트 테이블 setup과 오래된 대화 정리가 포함되어 있다.
3. 기존 LLM으로 추천 1건 실행, 실제 대화 저장·결과 복원 확인. 읽기 전용 점검만으로 RLS·시퀀스 권한은 보장되지 않는다.
4. 프론트 API 주소를 로컬 백엔드로 전환하고 브라우저에서 SSE·되묻기·추가 질문·새로고침 복원 확인.
5. 생성용 LLM과 검색용 임베딩 설정을 분리하고 Ollama/Gemma를 평가. 정확한 모델 태그와 VPS 자원을 먼저 확인.
6. VPS의 백엔드·AI·Caddy 배포 후 HTTPS와 SSE 확인.
7. Vercel 프론트 배포, API 주소·CORS 설정 후 배포 주소에서 E2E 확인.

## 아직 확인하지 않은 항목

- 실제 대화 쓰기와 복원, AI 추천·LLM 응답, 브라우저 전체 흐름
- VPS의 현재 배포 상태 및 RAM/GPU/VRAM
- 정확한 Gemma 모델 태그, Ollama 연결과 구조화 JSON 출력 호환성
- Vercel 프로젝트와 배포 설정

## 로컬 Gemma 생성 모델 연결 (2026-11-13)

- 같은 `feat/yj`에서 생성용 클라이언트를 `ai/recommendation_llm.py`로 분리했다.
- 루트 로컬 `.env`의 생성 설정을 `ollama`, `gemma3:4b`, `http://127.0.0.1:11434/v1`로 설정했다.
- planner·추천 설명·추가 질문은 이 클라이언트를 사용한다. 검색 임베딩 클라이언트는 변경하지 않았다.
- Ollama 오류 시 GPT로 자동 전환하지 않는다. 설정이 전혀 없는 환경의 기본 동작은 기존 OpenAI 모드다.
- 단위·기존 백엔드 테스트: **31 passed**.
- 실제 로컬 Gemma로 `ProjectPlan` 구조화 출력 생성 성공: 약 61.7초.
- 실제 추가 질문 스트리밍: token 22개, done 수신, error 없음.
- 위 Gemma 검증은 DB·OpenAI API를 호출하지 않았다. Gemma를 사용한 브라우저 전체 E2E는 별도 확인이 필요하다.
- Ollama 조회 시 설치 모델은 `gemma3:4b` 하나였으며, GPU 메모리 사용량은 0이었다.
- 이미 실행 중인 AI 서버는 재시작해야 변경된 설정이 반영된다. 실행 명령은 `ai/README.md` 참고.
- GPT 전환 시 `RECOMMEND_LLM_PROVIDER=openai`, `RECOMMEND_LLM_MODEL=gpt-4.1-mini`로 설정 후 재시작한다.
