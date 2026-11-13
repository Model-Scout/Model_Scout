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
