# Model Scout 백엔드 V2

[완료 기능·작업 현황·전달 안내](docs/00-delivery-status.md)에서 현재 구현 범위와 남은 검증을 먼저 확인하세요.

[브랜치 전체 작업 정리](docs/04-branch-work-summary.md)는 기존 기반과 이번 변경, 파일별 산출물, 취소 재검토 결과를 구분합니다.

프론트 전달 파일:

1. [화면별 기능·응답 데이터](docs/01-v2-features.md)
2. [API 명세](docs/02-api-v2.md)
3. [Mock JSON·SSE·JSON Schema·OpenAPI](examples/)

예시는 가상 데이터이며 실제 모델 성능·라이선스 근거가 아니다. `examples/generate.py`로 코드의 응답 모델에서 다시 생성한다.

## 개발 실행

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
