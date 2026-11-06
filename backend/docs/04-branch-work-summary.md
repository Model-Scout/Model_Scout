# feat/backend-chat-api 전체 작업 정리

기준일: 2026-11-06. 로컬 HEAD d040340a 대비 현재 커밋 전 변경 기준.

## 이 브랜치의 목적

기존 백엔드 초안을 V2 화면에 맞는 서비스 API로 보완하고, 프론트가 연동할 계약과 검증 자료를 준비했다.
**공개 API 5개를 처음부터 새로 만든 작업은 아니다.** 브랜치 시작 시 이미 같은 경로의 API, SSE 중계, 대화 저장·조회, 원문 조회 코드와 내부 AI API가 있었다.
이번 작업의 중심은 그 기반에 요청 모드·응답 구조·설명 질문·인용 저장·취소 및 실행 보호를 추가하고 계약을 검증하는 것이다.

## 기존 기반과 이번 변경

| 영역 | 시작 시 있던 것 | 이번에 추가·수정한 것 |
| --- | --- | --- |
| 공개 API | chat, groups 목록·상세, files, health의 5개 경로 | 기존 경로 유지, V2 계약·검증·조회 응답 보완 |
| 세션·권한 | X-Session-Id UUID, group_id, 소유자 쓰기 검증, 공개 링크 읽기 | 기존 정책 유지, 요청 모드·대상 검증에 적용. 새 로그인 체계 아님 |
| 채팅 요청 | group_id, query | recommend/question 모드, target_id, 공백·초과 필드·잘못된 조합 검증 |
| 프론트 응답 | 모델 candidates와 별도 datasets, 유형별 questions/message | schema_version=2, 공통 answer·sources, 통합 candidates, history_saved |
| 결과 상세 | 모델 지표와 일부 판정 | 모델·데이터셋 공통 ID·역할·태그·출처, checks/evidence 분리, related 양방향 연결·중복 제거 |
| 결과 문구 | bool 조건을 그대로 표시할 수 있었음 | 상업 조건 False 표시 제거, needs_check에서 일괄 미확인 항목·데이터셋 제외 |
| 설명 질문 | 별도 question 흐름 없음 | 저장 추천+최근 메시지 6개를 AI에 전달. 선택 후보 설명, 재검색·순위 변경 없음 |
| AI 연동 | 내부 POST /ai/recommend, LangGraph 실행 | question 분기, 되묻기 재개 때 clarify가 만든 plan 전달 누락 수정 |
| SSE | AI status/token 중계, done/error | 다음 단계 라벨, 완료 이벤트 누락 검출, 파서 다중 data 행·마지막 이벤트 처리 |
| 기록 | groups/messages와 결과 JSONB | sources JSONB 컬럼·저장, 쓰기 트랜잭션, 최신 비어 있지 않은 result 복원, 메시지 ID·근거 반환 |
| 과거 데이터 | 이전 응답 형태 | 기존 형식 스냅샷 조회 변환. 운영에 해당 데이터가 있는지는 미확인 |
| 원문 | source_id를 README 파일에 매핑 | kind로 모델·데이터셋 구분, resolve 후 경로 이탈 검사, truncated 표시 |
| 실패 처리 | 기본 HTTP 오류와 SSE error | 저장 실패를 history_saved=false로 알림, AI done 없이 종료되면 error, 빈 설명 답변 검출 |
| 실행 보호 | 그룹별 실행 보호 없음 | 백엔드 그룹 lease, AI thread_id 잠금, 그래프 종료 후 해제, 재요청 최대 30초 대기 |
| 개발·문서 | 기존 실행 README | 패키지 import 지원, DB conninfo 구성 보완, CORS 응답 헤더 노출, 환경변수 예시·실행 안내 정리 |

LangGraph의 검색·랭킹 알고리즘, 모델 수집·임베딩 파이프라인, 프론트 화면, Docker 배포 구성 자체를 새로 만든 브랜치는 아니다.
특히 서버 분리·Supabase·OpenAI 외부 호출 기반은 기존 작업을 활용했다.

## 실제 제공 기능

| 공개 API | 사용자 기능 |
| --- | --- |
| POST /api/chat | 최초 추천, 되묻기 답변, 조건 변경·재추천, 특정 후보·전체 추천 설명 질문 |
| GET /api/groups | 이 브라우저 세션의 대화 목록 최대 100개 |
| GET /api/groups/{group_id} | 대화·최신 추천·인용 복원, 공개 링크 읽기 |
| GET /api/files/{source_id}?kind=model 또는 dataset | 현재 README 원문 표시 |
| GET /api/health | 백엔드 프로세스 응답 확인 |

내부 POST /ai/recommend 1개는 프론트 API 개수에 포함하지 않는다. 백엔드만 사용한다.
API 개수는 주소의 수이며, 사용자 기능 수와 같지 않다. 예를 들어 /api/chat 한 개가 네 가지 동작을 맡는다.

## 파일별 변경과 산출물

| 파일·폴더 | 작업 |
| --- | --- |
| backend/app/main.py | 요청·권한·대상 검증, 질문 컨텍스트, SSE·오류, 실행 lease·연결 종료, 기록 복원·원문 처리 |
| backend/app/result.py | V2 Pydantic 응답 모델, AI 이벤트→공통 후보·근거·판정 변환, 이전 형식 복원 |
| ai/api.py | 되묻기 plan 전달, question 모드, thread 잠금·대기·스트림 종료 정리 |
| ai/recommendation_question.py (신규) | 저장된 추천·최근 대화로 설명 답변을 생성하는 LLM 스트림 |
| backend/app_schema.sql | 기존 app.messages에 sources JSONB 컬럼 추가하는 재실행 가능한 SQL |
| backend/tests/test_v2.py (신규) | 요청·응답 계약, 저장·복원, 권한, 오류, 원문, 되묻기·화면 문구·예시 검증 |
| backend/tests/test_cancel_integration.py (신규) | 실제 백엔드·AI HTTP 서버+LangGraph 취소·재요청, 실행 겹침·체크포인트 검사 |
| backend/examples/ (신규) | answer/question/clarify/reject/empty/error/save-failed, 요청·기록 JSON, SSE, JSON Schema, OpenAPI, 생성 스크립트 |
| backend/.env.example, requirements-dev.txt (신규) | 환경변수 항목과 pytest 개발 의존성 |
| backend/README.md, backend/docs/ (신규) | 실행·기능·API·작업 상태·검증·현재 문서 |
| README.md | AI 별도 실행, 현재 서버 경계·배포 구성 안내 수정 |

## 테스트와 재검토

- 현재 코드로 전체 백엔드 테스트를 직접 실행해 **19 passed, skip 없음**을 확인했다.
- 컴파일 검사와 git diff --check가 통과했다.
- 실제 HTTP 서버 두 개와 실제 LangGraph를 이용한 취소·재요청 검증에서 노드 실행 겹침이 없고 최종 체크포인트는 재요청 결과였다.
- 위 테스트의 LLM·검색 노드 내용은 대역, 체크포인터는 InMemorySaver, 서비스 DB는 SQLite 저장소 대역이다. 운영 PostgreSQL·외부 LLM까지 확인한 결과는 아니다.
- 이전 문서에 적힌 WSL 15회 연속 통과는 기존 실험 기록이다. 이번 재검토에서는 Windows 환경에서 전체 테스트 통과와 추가 시각 측정을 직접 확인했다.

### 취소 동작의 정확한 한계

**동시 실행 방지와 즉시 취소는 다르다.** 추가 시각 측정에서는 클라이언트 취소 약 0.604초 후 이전 요청의 search_datasets가 시작되고, 약 1.215초 후 재요청이 시작됐다. 두 실행은 겹치지 않았다.
따라서 현재 확인된 것은 이전 실행의 종료·정리 후 새 추천이 시작된다는 점이다. 클라이언트 취소 직후 다음 노드가 절대 실행되지 않는다는 보장은 성립하지 않는다.
현 통합 테스트도 이전 실행의 assess/explain 미진입만 검사하므로 이 차이를 검출하지 않는다. 취소 정책·테스트·명세를 맞추는 후속 보완이 필요하다.
실행 중인 LLM 호출의 즉시 중단·비용 중단, 사용자 메시지 롤백도 보장하지 않는다.

## Figma 작업 — Git 변경과 별도

- 기존 API 초안 아래에 완료 기능과 V2 계약을 편집 가능한 표·텍스트로 작성했다.
- 세로 읽기 순서로 정리한 뒤, 주 문서를 API 5개별 기능→요청→응답→주의사항으로 간소화했다.
- 긴 전체 필드·JSON·검증 설명은 오른쪽 상세 참고판에 보관했다.
- [API별 요약판](https://www.figma.com/design/ZX7LYl4sdpFqDW6QkwnKru?node-id=107-510)
- [상세 참고판](https://www.figma.com/design/ZX7LYl4sdpFqDW6QkwnKru?node-id=115-510)

Figma 판은 19개 테스트·취소 통합 검증 결과와 실제 응답 JSON 예시까지 반영했다.

## 아직 하지 않은 작업

- 실제 Supabase SQL 적용·권한·PostgresSaver 취소 및 복원 검증.
- 실제 외부 LLM·검색 데이터로 추천부터 기록 복원까지 전체 실행 검증.
- 프론트의 기존 /api/recommend 계약을 V2 /api/chat으로 전환·통합.
- VPS 배포·Caddy/CORS·실제 원문 파일 마운트·동시 부하 확인.
- 로그인·계정, 저장함, 대화 검색·삭제, 파일 내보내기, 공유 만료·철회, 요청 멱등 처리·실행 재개.
- 이 브랜치 변경의 커밋·push·배포. 기존 무관한 골든셋 Markdown 두 파일은 커밋 대상에서 제외한다.
