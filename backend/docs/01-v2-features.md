# Model Scout V2 기능·응답 데이터 명세

기준일: 2026-11-06. 브랜치 구현 기준 초안이며 프론트 합의·운영 배포 완료를 의미하지 않는다.

## 범위

홈 → 분석 중 → 추천 결과(B 또는 B-2) → 설명 질문 → 대화 이력 복원을 MVP로 구현한다.
로그인, 저장함, 대화 검색·삭제, 파일 내보내기는 이번 API 범위에 포함하지 않는다.
공유는 추측하기 어려운 group_id를 가진 링크로 읽는 방식이다. 별도의 공유 토큰·만료·철회 기능은 없다.

| 화면·행동 | 처리 | 예외·표시 규칙 |
| --- | --- | --- |
| 홈에서 아이디어 입력 | 새 group_id로 추천 실행 | 공백·2,000자 초과는 422 |
| 언어·실행 환경·상업 이용 조건 선택 | 프론트가 선택 조건을 query에 명시적으로 붙인다 | 별도 conditions 필드는 받지 않는다. 사용자가 선택한 조건을 전송 전에 확인할 수 있게 표시 |
| 예시 아이디어 선택 | 예시 문장을 query로 전송 | 일반 입력과 같은 API |
| 분석 중 | status 단계·token 답변 표시 | label은 지금 진행 중인 단계. step은 실제 진행률(%)이 아니며 같은 단계가 반복될 수 있음 |
| 되묻기 | answer에 질문 표시 후 같은 group_id, recommend 모드로 추가 답변 전송 | 아직 결과 화면으로 이동하지 않음 |
| 추천 완료 | 공통 candidates 목록으로 모델·데이터 탭과 상세 표시 | 후보 0개도 정상 answer; 빈 결과 안내 |
| 후보 선택 | 후보의 checks·related·지표 표시 | 값이 null이면 미확인, 임의 수치로 채우지 않음 |
| 근거·README 클릭 | sources 또는 checks의 source_id로 원문 조회 | 없는 원문은 404; 외부 출처 URL을 안내 |
| 결과에 관해 질문 | question 모드, 선택 시 target_id 전달 | 현재 저장된 추천과 최근 대화 6개를 근거로 설명하며 새 검색·순위 변경 없음 |
| 다시 분석·조건 변경 | 같은 group_id, recommend 모드로 query 전송 | 기존 AI 계획을 수정해 재검색; 완전히 새 기획은 group_id=null |
| 대화 목록 열기 | 세션에 속한 최신 100개 그룹 조회 | 다른 브라우저에서는 같은 세션이 없으므로 목록이 보이지 않음 |
| 과거 대화·공유 링크 열기 | 저장된 messages와 최신 비어 있지 않은 result 복원 | AI 재실행 없음. 읽기는 공개, 이어서 질문은 소유 세션만 가능 |
| 분석 취소 | 프론트 AbortController로 수신 중단 | 즉시 멈추지 않음. 취소를 감지하기 전 다음 단계가 하나 더 시작될 수 있고, 그 단계가 끝나면 멈춤. 그동안 재요청은 409 또는 대기. 자동 재전송 금지 |

## 응답 데이터

| 데이터 | 필드 | 규칙 |
| --- | --- | --- |
| 최종 응답 | schema_version, group_id, type, answer, sources, result, elapsed, history_saved | 모든 done에 같은 최상위 필드 사용 |
| 결과 개요 | title, summary[], needs_check[] | summary는 문자열 배열. needs_check는 모델의 라이선스·GPU·입력 길이 중 충족이 아닌 항목만 담는다. 모든 모델이 미확인인 언어·실행 환경과 데이터셋은 넣지 않는다 |
| 후보 | id, type, source_id, name, role, tags[], source, url | 모델·데이터셋을 하나의 candidates 배열로 제공 |
| 모델 지표 | rank_score, context_length, parameters_b, benchmarks[], gpu_fit | 원래 검색 점수·메타데이터. 점수는 확률·정확도가 아니며 모델 간 다른 벤치마크를 직접 비교하지 않음 |
| 조건 판정 | key, label, status, reason, source_id, quote, origin | status=ok/check/unknown. origin=readme/metadata/estimate/unknown |
| 인용 근거 | source_id, kind, title, url, quote, origin, location | quote는 실제 제공된 인용만. 정확한 원문 위치를 모르면 location=null |
| 추천 근거 | evidence[]: label, text, origin | 데이터셋이 추천된 이유. 조건 판정이 아니므로 checks와 분리한다. origin=readme/metadata |
| 후보 연결 | related[] | 같은 result 안 후보의 id 참조. 모델↔데이터셋 양방향, 중복 제거 |

후보 id는 `model:org/name`, `dataset:org/name` 형식이다. 파일 조회에는 접두사 없는 source_id를 쓴다.
후보 수·모델 수·데이터 수·선택 후보 조건 충족 수는 프론트가 candidates와 checks에서 계산한다.
조건 충족 수는 현재 제공한 checks 기준이며 고정 분모 5를 가정하지 않는다. 모델은 언어·실행 환경을 포함하고 GPU·입력 길이는 요구 조건이 있을 때 추가한다. 데이터셋 checks는 라이선스 하나이며, 라이선스 이름만으로 상업 이용을 판단할 수 없어 ok가 되지 않는다.

## 사실과 추정 구분

- 원문에 없는 문장을 quote에 만들지 않는다. 라이선스·입력 길이 메타데이터는 origin=metadata이다.
- GPU 적합성은 origin=estimate이며 실기기 실행 검증을 뜻하지 않는다.
- 현 AI 응답에는 한국어·로컬 실행의 구조화된 검증이 없으므로 unknown으로 표시한다.
- 데이터셋의 관련성 근거만으로 라이선스·실시간 제공·서비스 적합성을 충족 처리하지 않는다.
- question 응답의 sources는 답변에 이용할 수 있었던 저장 자료다. 문장별 인용 검증 결과를 뜻하지 않는다.
- 원문 조회는 현재 배포된 README다. 과거 전체 README 스냅샷은 저장하지 않으며, 당시 quote·판정·추천 결과만 DB에 보관한다.

## 근거 자료

- [Figma V2·API 초안](https://www.figma.com/design/ZX7LYl4sdpFqDW6QkwnKru?node-id=65-748)
- [기술 스택 정리](https://app.notion.com/p/40b4670888c18034be95c75983ac3f97)

화면 시안과 기술 스택을 바탕으로 이 브랜치에서 정한 계약이다. Figma의 path, 판정 코드, 분리된 질문·거절 응답 필드 대신 다음 API 문서의 계약을 사용한다.
