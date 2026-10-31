---
license: apache-2.0
language:
- ko
---
# Semantic Router Instruction Dataset

semantic-turn router 학습·평가용 한국어 instruction 데이터셋. 한 문장을 14개 축으로 동시에 분류하는 모델의 학습 데이터로 쓰기 위해 만들었고, 각 행의 `instruction`은 해당 축·값을 판별할 수 있는 내용 단서를 실제로 포함한다.

- **규모**: 600,000행 (14축 × 150값 전체 커버, 값별 행 수 고정)
- **언어**: 한국어 (일부 기술 용어·코드·수식은 원표기)
- **특성**: 전 행 장문 조합형 — 평균 140자, 80자 이상 92.8%, 120자 이상 69.5%

## 파일 형식

`dataset.jsonl` — 한 줄에 JSON 객체 하나, UTF-8, 헤더 없음.

```json
{"instruction":"신규 입사자 온보딩 자료를 만들다가 막혀서, …일정이 촉박해지면 한 페이지 요약본을 맨 앞에 먼저 놓아줘.","category":"presentationSkillId","value":"deck-redesign"}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `instruction` | string | 사용자 발화(지시문). 유니크 보장(600k 전수 중복 0) |
| `category` | string | 14개 축 중 하나 |
| `value` | string | 해당 축의 값 (총 150값) |

## 축·값·할당

| 축 | 값 수 | 행 수 | 값 |
|---|---:|---:|---|
| `service` | 16 | 96,000 | general, presentation, image, data_analysis, place_search, web_search, knowledge_search, calendar, memo, works, connector, artifact, coding, translation, skill, reasoning |
| `presentationSkillId` | 56 | 112,000 | executive-strategy, board-update, quarterly-business-review, sales-proposal, investor-pitch, training-explainer, technical-architecture, research-report, marketing-campaign, product-launch, product-roadmap, consulting-diagnosis, all-hands-update, thesis-research, crisis-communication, demo-day-pitch, compliance-training, lesson-lecture, customer-qbr, analyst-briefing, okr-review, esg-report, incident-postmortem, thesis-defense, grant-proposal, workshop-facilitation, competitive-analysis, investor-update, annual-report, pricing-proposal, analytics-readout, customer-onboarding, vendor-selection, market-entry, company-onboarding, case-study-analysis, model-un-position, lab-meeting, self-review, conference-talk, resume-portfolio, nonprofit-pitch, policy-briefing, earnings-brief, m-a-proposal, org-redesign, regulatory-response, course-syllabus, exam-prep, hobby-explainer, travel-itinerary, deck-redesign, deck-exec-polish, deck-board-upgrade, deck-content-cleanup, none |
| `contentDomain` | 15 | 60,000 | social, play, self_capability, affective_state, creative, support, explore, personal_scope, opinion, code_work, formal_reasoning, supplied_material, explicit_lookup, multi_step_research, unresolved |
| `action` | 14 | 56,000 | respond, create, revise, import, analyze, search, export, delete, translate, summarize, explain, compare, execute, none |
| `dialogueAct` | 10 | 40,000 | clarification_answer, option_selection, confirm, decline, correction, continue_output, preference_directive, meta_conversation, undo_action, none |
| `sourcePolicies` | 7 | 42,000 | web, internal, memory, attachments, conversation_only, auto, none |
| `memoryIntent` | 7 | 28,000 | informational, transactional, conversational, analytical, personal, navigational, none |
| `requestedOutputs` | 5 | 34,000 | chat, docx, xlsx, pptx, image |
| `diagramKind` | 4 | 24,000 | structure, visualization, plan, none |
| `presentationMode` | 4 | 24,000 | fast, professional, creative, none |
| `complexity` | 4 | 32,000 | simple, standard, complex, hard |
| `artifactKind` | 3 | 18,000 | diagram, interactive, none |
| `analysisMode` | 3 | 18,000 | focused, comprehensive, none |
| `artifactComplexity` | 2 | 16,000 | simple, complex |

값별 행 수는 위 표의 (행 수 ÷ 값 수)로 균등 배분된다(예: service 값당 6,000행,
presentationSkillId 값당 2,000행). 한 `instruction`은 정확히 하나의 (category, value)
쌍으로 라벨링된다 — 다중 라벨이 아니라, 축마다 별도 행으로 존재한다.

## instruction 구성 (장문 조합형)

모든 행은 아래 순서로 조합된다:

```
[상황 오프너] (+ [배경절] 40%) + [그룹 고유 요청] + [제약 tail 1~4개] (+ [조건 분기 tail] 35%)
```

- **상황 오프너**: "지난 3월에 착수한 멤버십 리뉴얼 건이 이번 주 안에 마감이라, " 같은 맥락 절. 업무형 30종 + 일상형 12종.
- **제약 tail**: "결론부터 먼저 보여주고 근거는 뒤에 붙여줘." 같은 출력 조건.
- **조건 분기 tail**: "만약 최신 수치를 못 찾으면 작년 3월 기준으로 대체하고 그 사실을 명시해줘." 같은 if/else 분기 — 긴 문장 안에 여러 갈래의 지시를 싣는다.

축의 성격에 따라 6개 **작성 프로필**이 라우팅된다:

| 프로필 | 대상 축·값 | 특징 |
|---|---|---|
| general | service·sourcePolicies·artifact*·presentation*·requestedOutputs 등 | 업무 오프너 + 일반 tail + 분기 tail |
| formal | complexity::hard, contentDomain::formal_reasoning | 엄밀성 tail("생략 없이 모든 유도 과정을 보여줘") |
| code | contentDomain::code_work, service::coding | 엔지니어링 tail("테스트도 함께 붙여줘") |
| quick | complexity::simple | 간결 요청 + 간결 tail 1~2개 |
| personal | contentDomain::{social,support,opinion,explore,personal_scope}, memoryIntent::personal | 일상 오프너 + 일반 tail |
| micro | dialogueAct 전체, memoryIntent::{conversational,navigational,none}, contentDomain::{play,self_capability,affective_state,unresolved}, action::none | 일상 오프너 + 마이크로 발화 + 가벼운 대화 tail |

micro 프로필은 "응 맞아" 같은 짧은 발화 자체는 유지하되, 주변 맥락절로 전체 길이를 확보한다 — 라벨 의미(대화 행위)를 훼손하지 않으면서 장문 분포에 맞춘다.

## 길이 분포

| 구간 | 행 수 | 비중 |
|---|---:|---:|
| 120–160자 | 217,365 | 36.2% |
| 160–220자 | 191,605 | 31.9% |
| 80–120자 | 139,221 | 23.2% |
| 220자+ | 8,534 | 1.4% |
| 40–80자 | 42,190 | 7.0% |
| 40자 미만 | 1,085 | 0.2% |

평균 140.2자, 최단 25자(micro 발화), 최장 273자.


## 주의사항

- 템플릿 조합 생성 데이터다. 개별 문장은 문법적으로 자연스럽지만 슬롯 조합의 의미적 어긋남(예: 업무 주제 × 일상 오프너)이 드물게 있을 수 있음. 
  분류 라벨에는 영향이 없으나 자연성 평가에는 고려할 것.
- 특정 축의 행은 서로 다른 축의 행과 텍스트가 겹칠 수 있다(같은 주제가 여러 축에 등장). instruction은 전 데이터셋에서 전수 유니크 검증 완료.

## 라이선스

- Apache 2.0