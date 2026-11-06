# Model Scout V2 백엔드 작업 현황·전달 안내

기준일: 2026-11-06 · 브랜치: `feat/backend-chat-api` · 운영 배포 전.

기존 기반 대비 전체 변경과 최신 취소 재검토는 [브랜치 전체 작업 정리](04-branch-work-summary.md)를 참고한다. 동시 실행 방지는 확인했지만 취소 직후 다음 노드가 절대 실행되지 않는다는 보장은 확인되지 않았다.

## 현재 완료 범위

**프론트가 사용할 V2 API 계약, 백엔드 구현, 예시 데이터, 로컬 검증을 정리했다.**
기존 팀원의 FastAPI·Supabase·SSE·내부 AI 호출 구조를 확장했다. LangGraph의 모델 검색·추천 순위 로직을 새로 만든 작업은 아니다.
프론트 화면 구현·연동과 운영 DB 적용·배포는 완료 범위에 포함하지 않는다.

아래의 구현 완료는 브랜치에 코드가 있다는 뜻이다. 로컬 확인은 테스트 대역을 포함하며 실제 운영 동작 보장과 구분한다.

| 기능 | 구현 내용 | 상태·제약 |
| --- | --- | --- |
| 브라우저 세션 식별 | 프론트 생성 UUID를 X-Session-Id로 받고 대화 소유권 확인 | 구현·로컬 확인. 로그인·서버 세션 발급·만료 기능 없음 |
| 새 대화·최초 추천 | group_id=null이면 그룹과 사용자 메시지 생성 후 내부 AI 호출 | 구현·로컬 확인. 실제 Supabase·유료 LLM 연결 미검증 |
| 진행 상태·답변 스트리밍 | status/token/done/error SSE 이벤트 제공 | 구현·로컬 확인. Caddy·실제 브라우저 경유 검증 필요 |
| 되묻기·답변 후 재개 | clarify를 표시하고 같은 그룹에서 recommend로 재개. 새 plan 전달 누락 수정 | 실제 LangGraph 중단·재개 테스트 통과. LLM·검색은 대역 |
| 결과 데이터 변환 | 모델·데이터셋 통합 candidates, 요약, 조건 판정, 추천 근거, 모델 지표 제공 | 구현·로컬 확인. 한국어·로컬 실행 조건은 구조화 근거가 없어 unknown |
| 후보 연결 관계 | related로 모델↔데이터셋 연결, 동일 후보 중복 제거 | 구현·로컬 확인 |
| 추천 설명 질문 | question 모드로 저장 결과와 최근 메시지 6개 전달. target_id로 특정 후보 선택 | 구현·로컬 확인. 새 검색·추천 순위 변경 없이 설명 |
| 조건 변경·재분석 | 같은 그룹에서 recommend로 기존 AI 흐름을 다시 실행 | 구현. AI 체크포인트 보존 여부에 따라 이전 계획 연결 가능 여부가 달라짐 |
| 대화·결과·인용 저장 | 사용자/AI 메시지, 추천 JSON, sources 저장 | 저장소 대역으로 확인. 실제 DB 적용·권한 확인 필요 |
| 내 대화 목록 | 세션별 updated_at 내림차순 최대 100개 조회 | 구현·로컬 확인. 검색·페이지네이션 없음 |
| 기록·공유 링크 복원 | 메시지와 가장 최근 비어 있지 않은 result 조회, AI 재실행 없음 | 구현·로컬 확인. 링크 보유자는 전체 대화 읽기 가능. 쓰기는 소유 세션만 |
| README 원문 조회 | source_id와 kind로 파일 조회, 경로 이탈 검사, 잘림 표시 | 구현·로컬 확인. 실제 배포 파일 마운트 확인 필요 |
| 오류·입력 검증 | 잘못된 본문/대상/세션, 요청 한도, AI 스트림 단절 처리 | 구현·로컬 확인. 저장 실패 시 history_saved=false |
| 동일 그룹 동시 실행 방지 | 처리 중 동일 그룹 요청 409. 취소 시 백엔드와 AI 모두 실행을 닫은 뒤 해제 | 실제 백엔드·AI 서버·LangGraph 통합 테스트로 취소→재요청 시 실행이 겹치지 않음을 확인. 노드 내용은 대역 |
| 서버 상태 | GET /api/health | 구현. 프로세스 응답만 확인하며 DB·AI 준비 상태는 확인하지 않음 |

## API 목록

| Method | Endpoint | 용도 | 세션 헤더 |
| --- | --- | --- | --- |
| POST | /api/chat | 최초 추천·되묻기·재추천·설명 질문, SSE 응답 | 필수 |
| GET | /api/groups | 내 대화 목록 | 필수 |
| GET | /api/groups/{group_id} | 대화·최신 결과 복원 | 불필요, 링크 공개 읽기 |
| GET | /api/files/{source_id}?kind=model 또는 dataset | README 원문 | 불필요 |
| GET | /api/health | 프로세스 상태 | 불필요 |

내부 전용 `POST /ai/recommend`는 백엔드가 호출한다. 브라우저는 내부 AI API·Supabase에 직접 접근하지 않는다.

### 요청·응답 핵심 규칙

`POST /api/chat` 요청:

```json
{
  "group_id": null,
  "query": "문서 검색 서비스를 만들고 싶어. 조건: 한국어, 로컬 GPU 8GB, 상업적 이용.",
  "mode": "recommend",
  "target_id": null
}
```

- 최초 추천: group_id=null, mode=recommend.
- 되묻기 답변·조건 변경·재분석: 기존 group_id, mode=recommend.
- 추천 설명 질문: 기존 group_id, mode=question, 필요하면 target_id=candidates[].id.
- 홈의 선택 조건은 query에 문장으로 붙인다. 별도 conditions 필드는 없다.
- 세션은 X-Session-Id 헤더에만 전달한다. query는 공백만 입력 불가, 최대 2,000자다.

최종 done은 schema_version, group_id, type, answer, sources, result, elapsed, history_saved를 공통으로 반환한다.

| 응답 | 프론트 동작 |
| --- | --- |
| answer + result 객체 | 결과 화면 갱신. 후보 0개는 빈 상태 표시 |
| answer + result=null | 기존 추천 유지, 답변만 추가 |
| clarify | answer의 질문 표시, 같은 그룹에 recommend로 답변 |
| reject | 안내 표시, 결과 화면 자동 이동 없음 |
| history_saved=false | 답변은 표시하되 기록 저장 실패 안내 |
| SSE error 또는 done 없이 연결 종료 | 실패/연결 중단 표시. 자동 재전송하지 않음 |

후보 ID는 `model:org/name` 또는 `dataset:org/name`이다. 원문 조회에는 접두사 없는 source_id를 쓴다.
checks는 조건 판정, evidence는 데이터셋 추천 이유, sources는 출처·인용이다.
판정값은 ok/check/unknown이며 원문 사실·메타데이터·추정치를 origin으로 구분한다.

## 프론트 전달 자료

| 문서·파일 | 내용 |
| --- | --- |
| [기능 명세](01-v2-features.md) | 화면별 행동, 응답 데이터, 표시 정책, 범위 |
| [API 명세](02-api-v2.md) | 엔드포인트, 필드 타입, JSON, SSE, 오류, 복원 규칙 |
| [구현·검증 기록](03-backend-validation.md) | 변경 사항, 테스트 범위, 운영 확인 항목 |
| [examples](../examples/) | 프론트 mock용 JSON, SSE, JSON Schema, OpenAPI |
| [백엔드 실행 안내](../README.md) | 의존성·환경변수·실행·DB 적용 |
| [DB SQL](../app_schema.sql) | app.groups, app.messages, sources 컬럼 추가 |

examples의 answer/question/clarify/reject/empty/error/save-failed JSON과 group.json을 화면별 mock으로 사용한다.
answer.sse는 스트림 예시, chat-done.schema.json은 최종 응답 검증용, openapi.json은 API 도구 가져오기용이다.
예시는 전부 가상 데이터이며 실제 모델 성능·라이선스 검증 결과가 아니다.

## 검증 결과와 완료 전 남은 일

최근 확인 결과: **Linux(WSL, Python 3.11)에서 pytest 19개가 15회 연속 통과.** Windows에서는 소켓 오류 WinError 10014로 테스트가 간헐적으로 실패할 수 있다.
DB 테스트는 SQLite 저장소 대역, AI·LLM 호출은 대역이다. 되묻기와 취소·재요청은 실제 LangGraph를 사용하되 LLM·검색만 대체했다.

운영 적용까지 남은 작업:

1. 대상 Supabase에 SQL 적용, DB 계정·시퀀스 권한·재시작 후 기록 복원 확인.
2. 실제 AI·LLM으로 최초 추천→되묻기→결과→설명 질문→재추천 검증. PostgresSaver에서 취소·재요청도 확인.
3. 프론트 mock과 실제 API 연결 전환, 오류·빈 결과·저장 실패 화면 확인.
4. VPS 배포 후 Caddy SSE·CORS·원문 마운트·동시 부하 확인.

미구현 기능: 로그인·계정, 저장함, 대화 검색·삭제, 내보내기, 공유 링크 만료·철회, 요청 멱등 처리·실행 재개, AI 실행 취소 보장.

## Git 작업 범위

작업은 현재 로컬 브랜치의 커밋 전 변경이다. 운영 반영·원격 push·팀원에게 전달 메시지 발송은 이 정리 작업에 포함하지 않는다.
커밋할 때 기존 작업과 무관한 `골든셋_*.md`, `내_골든셋_*.md`는 제외한다.
