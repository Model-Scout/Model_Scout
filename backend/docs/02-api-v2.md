# Model Scout V2 API 명세

기준일: 2026-11-06 · schema_version=2 · 프론트 전달용 초안.

## 연결·세션

- 개발 기본 주소: `http://localhost:8000`. 운영 주소는 V2 배포 후 확정한다.
- 프론트는 UUID를 한 번 생성해 localStorage에 보관한다. `crypto.randomUUID()` 사용.
- `POST /api/chat`, `GET /api/groups`에는 `X-Session-Id: <UUID>` 필수. 본문·URL에는 세션을 넣지 않는다.
- `GET /api/groups/{group_id}`, `/api/files/{source_id}`, `/api/health`는 세션 없이 조회 가능.
- 세션 발급·로그인 API는 없다. 세션 ID를 알면 소유자로 동작하므로 로그·공유 링크에 노출하지 않는다.
- 결과 링크는 대화 메시지·추천 결과 전체를 읽을 수 있는 공개 링크다. UI에서 공유 전 이 범위를 표시한다.
- 브라우저는 VPS 백엔드를 직접 호출한다. SSE는 EventSource 대신 POST fetch + ReadableStream으로 처리한다.

## API 목록

| Method | Endpoint | 응답 |
| --- | --- | --- |
| POST | /api/chat | text/event-stream; status/token → done 또는 error |
| GET | /api/groups | GroupSummary[] JSON |
| GET | /api/groups/{group_id} | GroupDetail JSON |
| GET | /api/files/{source_id} | SourceFile JSON; source_id에 `/` 포함 가능 |
| GET | /api/health | {"ok": true}; 프로세스 확인용, DB·AI 준비 상태 보장 안 함 |

## POST /api/chat

요청 헤더: `Content-Type: application/json`, `X-Session-Id: <UUID>`.

| 필드 | 타입·기본값 | 규칙 |
| --- | --- | --- |
| query | string, 필수 | 앞뒤 공백 제거, 공백만 입력 불가. 원본 입력 길이 1~2,000자 |
| group_id | UUID 또는 null, 기본 null | null은 새 기획. 기존 ID는 같은 세션만 이어서 요청 가능 |
| mode | recommend 또는 question, 기본 recommend | recommend: 최초 추천·되묻기 답변·조건 변경·재추천. question: 저장 결과 설명 |
| target_id | string 또는 null, 기본 null | question에서만 허용. 최신 결과 candidates[].id 중 하나. 최대 300자 |

정의하지 않은 필드는 422로 거절한다. 홈 조건은 query에 붙인다.

```json
{
  "group_id": null,
  "mode": "recommend",
  "query": "문서 검색 서비스를 만들고 싶어. 조건: 한국어, 로컬 GPU 8GB, 상업적 이용.",
  "target_id": null
}
```

설명 질문:

```json
{
  "group_id": "00000000-0000-4000-8000-000000000001",
  "mode": "question",
  "query": "이 모델이 GPU 조건을 충족하지 못하는 이유를 설명해줘",
  "target_id": "model:example/search-model"
}
```

question은 저장된 추천을 근거로 답하고 LangGraph 추천 상태·순위를 변경하지 않는다. 새 원문 검색이 아니다.
최근 메시지 6개(각 2,000자까지)를 함께 전달해 "그럼 두 번째는?" 같은 지칭을 해석한다. 이전 대화는 사실 근거로 쓰지 않는다.
대상 없이 전체 추천 질문도 가능하다. 저장 근거가 100,000자를 초과하면 422이므로 후보를 선택한다.
초기 추천이 없으면 question은 409. 되묻기 답변은 반드시 recommend로 보낸다.

## SSE 계약

HTTP 200의 Content-Type은 `text/event-stream`. 응답 전체를 `response.json()`으로 읽지 않는다.
`X-Group-Id` 응답 헤더에 group_id가 있어 완료 전에도 대화를 식별할 수 있다.
`Cache-Control: no-cache`. CORS는 X-Group-Id와 Retry-After를 브라우저에 노출한다.

| 이벤트 | data | 처리 |
| --- | --- | --- |
| status | {step: number, total: 4, label: string, elapsed: number} | 단계 표시, elapsed는 초 |
| token | {text: string} | 임시 답변에 순서대로 덧붙임 |
| done | ChatDone | 최종 answer로 임시 텍스트를 교체. 정상 종료 |
| error | {code: "AI_UNAVAILABLE", message: string, group_id: UUID} | 실패 표시. 부분 token을 완료 답변으로 저장하지 않음 |

status는 여러 번 오며 일부 단계가 생략될 수 있다. 횟수 4회를 가정하지 않는다. label은 지금 진행 중인 단계다. question은 step 4 "답변 생성" 하나만 온다.
각 이벤트는 `event: ...\ndata: <JSON>\n\n` 형식이다. 네트워크 청크와 이벤트 경계가 다를 수 있으므로 버퍼링하고 CRLF도 지원한다.
done/error 중 하나가 오면 종료한다. 둘 다 없이 EOF이면 연결 중단으로 처리한다.
동일 요청의 자동 재시도·SSE 재개는 지원하지 않는다. 초기 요청 재전송은 새 그룹·중복 AI 실행을 만들 수 있다.
429는 Retry-After 초 이후 사용자가 다시 요청한다. 네트워크 중단 시 먼저 이력을 조회하고 재시도 여부를 정한다.
동일 그룹 처리 중 요청은 409. 단일 백엔드 워커 운영이 전제다. 취소 후에는 진행 중인 AI 연결이 닫힐 때까지 409일 수 있다. 200을 받은 재요청도 AI가 이전 단계를 끝낼 때까지 최대 30초 대기하며, 넘기면 SSE error로 끝난다.

```text
event: status
data: {"step":1,"total":4,"label":"요구사항 분석","elapsed":0}

event: token
data: {"text":"추천 결과를 설명할게요."}

```

## ChatDone

| 필드 | 타입 | 의미 |
| --- | --- | --- |
| schema_version | 2 | 공개 응답 계약 버전 |
| group_id | UUID | 다음 질문·기록 복원에 사용 |
| type | answer / clarify / reject | 화면 분기 |
| answer | string | 모든 유형 공통. 마크다운 가능 |
| sources | Source[] | 저장된 출처·인용, 없으면 [] |
| result | ChatResult / null | 새 추천 스냅샷일 때 객체. question·clarify·reject는 null |
| elapsed | number | 백엔드 실행 경과 초 |
| history_saved | boolean | true: 응답 저장 성공. false: 화면 표시 가능하지만 복원 보장 안 됨 |

- answer + result 객체: 후보가 없어도 결과 화면에 빈 상태 표시.
- answer + result=null: 기존 결과 유지, 대화에 답변만 추가.
- clarify: answer의 질문을 보여 주고 같은 group_id에 recommend 요청.
- reject: answer 안내 표시, 결과 화면으로 자동 이동하지 않음. 기존 결과가 있으면 유지.
- history_saved=false: “답변을 기록에 저장하지 못했어요” 안내. 성공적으로 저장됐다고 표시하지 않음.

전체 예시는 `backend/examples/`의 answer.json, question.json, clarify.json, reject.json, empty.json, error.json을 사용한다.
기계 검증용 `chat-done.schema.json`은 ChatDone 전체 하위 타입을 포함한다. `openapi.json`의 POST 200은 스트림 문자열이며, done payload는 별도 스키마로 검증한다.

### 후보·근거 타입

`ChatResult`: title:string, summary:string[], needs_check:string[], candidates:Candidate[], assessment:object|null.
assessment는 AI 보조 정보이며 화면의 필수 레이아웃 계약은 아니다. 추가 필드에 의존하지 않는다.

`Candidate`: id:string, type:model|dataset, source_id:string, name:string, role:string, tags:string[], source:string, url:string|null, checks:Check[], evidence:Evidence[], related:string[], rank_score:number|null, context_length:integer|null, parameters_b:number|null, benchmarks:object[], gpu_fit:object|null.
benchmarks와 gpu_fit은 AI 메타데이터의 확장 영역이며 필드가 없으면 미확인으로 처리한다.

`Check`: key:string, label:string, status:ok|check|unknown, reason:string, source_id:string|null, quote:string|null, origin:readme|metadata|estimate|unknown.
ok=충족, check=확인 필요, unknown=미확인. check는 충족으로 집계하지 않는다.

`Evidence`: label:string, text:string|null, origin:readme|metadata. 데이터셋의 추천 근거이며 조건 판정이 아니다. 모델은 빈 배열이다.

`Source`: source_id:string, kind:model|dataset, title:string|null, url:string|null, quote:string|null, origin:readme|metadata|estimate|unknown, location:string|null.
같은 source_id에 서로 다른 인용이 있을 수 있다. 후보 개수와 sources 길이는 같지 않다.
location은 현재 null이다. quote가 원문에 존재하면 정확히 일치하는 텍스트만 하이라이트하고, 찾지 못하면 인용과 현재 원문을 구분해 보여 준다.
원문·답변을 HTML로 직접 삽입하지 말고 안전한 마크다운 렌더링을 사용한다.

## GET /api/groups

X-Session-Id 필수. 본인 그룹을 updated_at 내림차순 최대 100개 반환한다. 없으면 []. 검색·페이지네이션 없음.

```json
[{"group_id":"00000000-0000-4000-8000-000000000001","title":"문서 검색 서비스","created_at":"2026-11-06T00:00:00Z","updated_at":"2026-11-06T00:00:01Z"}]
```

## GET /api/groups/{group_id}

세션 없이 읽기 가능. group_id, title, created_at, updated_at, messages[], result 반환.
messages는 id 오름차순이며 각 항목은 id:number, role:user|assistant, content:string, type:answer|clarify|reject|null, result:ChatResult|null, sources:Source[], created_at:ISO8601이다.
최상위 result는 저장된 메시지 중 가장 최근의 비어 있지 않은 추천 스냅샷이다. 이후 설명 질문·되묻기로 지워지지 않는다.
재분석 없이 그대로 렌더링한다. 이전 구조로 저장한 결과도 조회 시 V2로 변환한다. 과거 기록에 없던 인용문은 복구하지 않는다.

## GET /api/files/{source_id}

예: `/api/files/BAAI/bge-m3`. source_id 각 경로 구간을 URL 인코딩해 전달한다. 후보 id의 `model:`/`dataset:` 접두사는 보내지 않는다.
프론트는 후보 type 또는 Source.kind를 쿼리로 함께 보낸다. 예: `/api/files/BAAI/bge-m3?kind=model`.
kind=model|dataset은 선택 필드지만, 모델·데이터셋이 같은 source_id를 가질 수 있으므로 V2에서는 전달을 권장한다.
README만 조회하며 서버 파일 경로를 직접 받지 않는다. 응답은 source_id:string, content:string(마크다운), truncated:boolean.
최대 2,000,000자를 반환한다. 잘렸으면 truncated=true. 없는 파일은 404.

## 오류

스트림 시작 전에는 일반 JSON 오류 응답이다. HTTP 오류는 SSE error와 구분한다.

| 상태 | 조건 | 응답 |
| --- | --- | --- |
| 403 | 다른 세션에서 기존 그룹에 질문 | {detail: string} |
| 404 | 없는 그룹·원문 | {detail: string} |
| 409 | 같은 그룹 처리 중, question에 필요한 추천 없음 | {detail: string} |
| 422 | 헤더·UUID·본문·모드·길이 오류 또는 없는 target_id | {detail: validation_error[] 또는 string} |
| 429 | IP별·일별 요청 한도 | {detail: string}, Retry-After 헤더 |
| 503 | DB 환경변수 미설정 | {detail: string} |
| 500 | DB 연결·스키마 등 예상하지 못한 서버 오류 | 일반 서버 오류. 프론트는 JSON 파싱 실패도 처리 |

HTTP 200 이후 AI 실패·완료 없이 종료는 SSE error로 전달된다. DB 저장 실패는 done + history_saved=false다.
운영에서는 Caddy, DB, AI 연결 제한을 별도로 검증해야 한다.
