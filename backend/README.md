# Model Scout 백엔드 V2

[실제 DB·API 통합 진행 기록](INTEGRATION_STATUS.md)에서 `feat/yj`의 검증 결과와 다음 작업을 확인할 수 있다.

[완료 기능·작업 현황·전달 안내](docs/00-delivery-status.md)에서 현재 구현 범위와 남은 검증을 먼저 확인하세요.

[브랜치 전체 작업 정리](docs/04-branch-work-summary.md)는 기존 기반과 이번 변경, 파일별 산출물, 취소 재검토 결과를 구분합니다.

프론트 전달 파일:

1. [화면별 기능·응답 데이터](docs/01-v2-features.md)
2. [API 명세](docs/02-api-v2.md)
3. [Mock JSON·SSE·JSON Schema·OpenAPI](examples/)

예시는 가상 데이터이며 실제 모델 성능·라이선스 근거가 아니다. `examples/generate.py`로 코드의 응답 모델에서 다시 생성한다.

## 개발 실행

입력은 저장·AI 호출 전에 공통 [규칙 기반 가드](../shared/README.md)를 거친다.
이메일·휴대전화·주민번호 형태는 마스킹하고, 알려진 키·토큰·명시적 비밀번호는 HTTP 400으로 중단한다.
인젝션 의심 문구는 유형만 기록하며 자동 차단하지 않는다. 문맥을 판단하는 LLM 검사는 아직 추가하지 않았다.

레포 루트에서 의존성 설치 후 DB 환경변수를 프로세스에 설정한다. `.env.example`은 설정 항목 참고용이고 서버가 자동으로 읽지 않는다.

```powershell
./.venv/Scripts/python.exe -m pip install -r backend/requirements-dev.txt
./.venv/Scripts/python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```

AI는 별도 프로세스로 실행한다. 기존 `ai/` 개발 환경과 데이터, API 키가 필요하다.

```powershell
./.venv/Scripts/python.exe ai/api.py
```

`AI_URL` 기본값은 `http://127.0.0.1:8001`이다. Docker Compose에서는 내부 `http://ai:8000`을 사용한다.
공개 백엔드에는 OpenAI 키를 넣지 않는다. 설명 질문도 내부 AI API를 통해 실행한다.
Swagger는 개발 `/docs`, OpenAPI는 `/openapi.json`. 운영에서 비활성화된 경우 저장된 `examples/openapi.json`을 전달한다.

## DB 적용

실제 DB 연결과 대화 테이블·컬럼·기본 권한을 먼저 읽기 전용으로 점검할 수 있다.
비밀값과 DB 오류 원문은 출력하지 않으며, SQL 적용이나 데이터 변경은 하지 않는다.
이 점검 통과 후에도 실제 대화 저장·복원으로 RLS와 시퀀스 권한을 확인해야 한다.

```powershell
./.venv/Scripts/python.exe backend/check_db.py --env-file .env
```

루트 `.env`를 사용하는 로컬 개발 환경에서는 아래처럼 명시적으로 로드한다.
`--env-file`은 `requirements-dev.txt`의 `python-dotenv`가 필요하다.
AI 서버도 같은 루트 파일을 명시적으로 읽도록 실행할 수 있다.
두 서버는 각각 별도 터미널에서 실행한다.

```powershell
./.venv/Scripts/python.exe -m uvicorn backend.app.main:app --env-file .env --host 127.0.0.1 --port 8000 --reload
./.venv/Scripts/python.exe -m uvicorn api:app --app-dir ai --env-file .env --host 127.0.0.1 --port 8001
```

새 환경에서는 `backend/app_schema.sql`을 DB 관리 권한으로 실행한다. 기존 환경에도 같은 파일을 재실행할 수 있다.
V2는 기존 app.messages에 `sources jsonb not null default '[]'` 컬럼을 추가한다. **코드 배포 전 SQL을 적용한다.**
백엔드 런타임 계정의 app 테이블·시퀀스 접근 권한은 별도 부여하고, 클라이언트 Data API로 app을 노출하지 않는다.
이 작업에서는 운영 DB SQL 적용·VPS 배포를 수행하지 않았다.

## 검증

```powershell
./.venv/Scripts/python.exe -m pytest backend/tests -q
./.venv/Scripts/python.exe backend/examples/generate.py
```

[구현·검증 기록](docs/03-backend-validation.md)에 실제 검증 범위와 남은 운영 확인 항목을 기록한다.
