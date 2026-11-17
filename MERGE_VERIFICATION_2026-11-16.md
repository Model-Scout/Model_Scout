# 머지·배포 E2E 검증

검증일: 2026-11-16 (한국 시간)

## 결론

Vercel 프론트 → 공개 VPS API → AI 추천 → 실제 DB 저장 → 화면 표시·새로고침 복원의 기본 흐름이 동작한다.
로컬 Gemma도 실제 응답했다. 다만 Ollama 비용 분리와 운영 모델 설정 전달에는 아래 보완점이 있다.
검증 중 애플리케이션 코드나 운영 설정은 수정하지 않았다.

## 확인한 코드와 배포

- 로컬 및 공개 GitHub main: `1d31d22d61c203e9ee59da1002310e23c0817efb`.
- PR #47 (`feat/yj`)이 main에 머지되어 있다.
- GitHub 커밋 상태의 Vercel 체크: success.
- 배포 상세: https://vercel.com/model-scout1/model-scout/DQdjkh4nVtDPaYEbXbyBA3ru7XH9
- 실제 사이트: https://model-scout-rosy.vercel.app/
- 공개 백엔드: https://49-247-194-63.sslip.io
- Vercel 상세 설정은 연결 도구의 팀 접근 권한 부족(403), VPS 내부 확인은 SSH publickey 인증 실패로 확인하지 못했다.
- 따라서 VPS 컨테이너의 정확한 커밋·이미지 및 실제 운영 LLM 이름은 확정하지 않는다.

## 검증 결과

| 항목 | 결과와 근거 |
| --- | --- |
| 자동 회귀 검사 | backend 및 생성 설정 31개 + 라우터 연결 46개 = 77 passed |
| 프론트 검사 | TypeScript, ESLint, `pnpm build` 통과 |
| VPS 상태와 DB 읽기 | health 200, 새 임의 세션 목록 200 및 빈 목록 |
| 실제 API 추천 | 합성 질문 1건, 18.5초, SSE token 540개와 done, 후보·출처 각각 19개 |
| 실제 DB 저장·복원 | history_saved=true, 메시지 2개, 복원한 result와 done.result 동일 |
| 원문 API | 첫 출처 조회 200 |
| Vercel CORS | 실제 사이트 Origin의 POST 사전 요청 200, content-type 및 x-session-id 허용 |
| 브라우저 추천 | 합성 질문으로 모델 5개·데이터 21개 표시, 새로고침 후 복원 |
| 브라우저 추가 질문 | 선택 모델에 관한 답변 표시, 메시지 4개 저장, 다시 새로고침해도 복원 |
| 브라우저 오류 | 확인 시 console error/warn 없음 |
| 로컬 Ollama | 설정 ollama/gemma3:4b, 설치 확인, 실제 짧은 생성 요청 성공(8.6초) |

브라우저 검증 대화:
https://model-scout-rosy.vercel.app/result/08d06cfc-30cb-4881-b011-7a0daa889b85

스크린샷: `merge-verification-2026-11-16.png`.

## 보완점

### 1. Ollama를 선택해도 라우팅·질의 분류는 별도 GPT 호출을 한다

- 위치: `ai/retrieval_lab/classifier.py:138`, 특히 150행의 직접 OpenAI 클라이언트 생성.
- `router.py`와 모델 질의 분류는 이 함수를 사용하며, 모델 기본값은 `pre_retrieval.py:23`의 `gpt-4o-mini`다.
- 이 경로는 `RECOMMEND_LLM_PROVIDER=ollama`를 따르지 않는다. 운영 그래프는 캐시를 끄고 호출한다.
- 따라서 현재 Ollama 설정은 요구사항 분해·추천 설명·추가 질문의 생성 비용을 줄이지만, 임베딩 외에도 유료 LLM 호출이 남는다.
- 개발 중 모든 생성 호출을 로컬로 보내려면 라우터·분류기에도 생성 클라이언트 설정을 연결해야 한다.

### 2. 배포 스크립트가 생성 모델 설정을 VPS에 전달하지 않는다

- 위치: `deploy/deploy.sh:51`의 `.env.ai` allowlist.
- `RECOMMEND_LLM_PROVIDER`, `RECOMMEND_LLM_MODEL`, `RECOMMEND_LLM_BASE_URL`이 포함되지 않는다.
- 이 스크립트는 원격 `.env.ai`를 덮어쓰므로 해당 경로로 배포하면 생성 설정이 빠지고 코드 기본값 OpenAI/gpt-4.1-mini가 적용될 수 있다.
- 운영에서 GPT를 쓰는 선택 자체는 가능하지만 모델 설정을 명시적으로 전달해 의도와 맞춰야 한다.
- VPS에서 Ollama를 쓰려면 모델 실행 환경과 AI 컨테이너에서 접근 가능한 주소도 필요하다. 로컬의 127.0.0.1 주소를 컨테이너에 그대로 옮기는 것만으로는 연결되지 않는다.

### 추천 품질은 별도 개선 필요

브라우저의 고객 리뷰 감성 분류 요청에 한국어교육 기관, 상업용 부동산 임대료, 입찰 정보 등 관련성이 낮은 서비스 데이터도 노출됐다.
연결 성공과 검색 품질을 구분해야 한다. 이번 검증은 연결 확인이며 전체 골든셋 품질 평가를 수행한 것은 아니다.

## 검증 범위와 남은 확인

- API 및 브라우저에서 합성 테스트 대화를 각각 한 건 생성했다. 기존 사용자 대화는 수정·삭제하지 않았다.
- 로컬 Gemma는 오늘 짧은 생성 요청을 검증했다. 오늘의 브라우저 E2E가 Gemma로 실행됐다는 뜻은 아니다.
- 모호한 입력의 되묻기 재개, 취소·동시 요청, 모든 질의 유형의 실제 운영 호출은 이번 라이브 검증에서 반복하지 않았다. 해당 동작의 일부는 회귀 테스트로 검증했다.
- VPS 내부 버전과 실제 모델 설정은 SSH 접근이 가능한 환경에서 추가 확인해야 한다.
- 기존 `frontend/pnpm-lock.yaml` 수정은 보존했다.
