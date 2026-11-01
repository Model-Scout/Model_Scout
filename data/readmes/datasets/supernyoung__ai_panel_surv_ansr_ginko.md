---
license: cc-by-4.0
language:
  - ko
  - en
  - pt
  - es
  - fr
  - ja
  - vi
  - nl
  - hi
pretty_name: AI Synthetic Panel Survey Answers — SKKU Brand Perception (Ginko)
size_categories:
  - 10K<n<100K
tags:
  - synthetic
  - survey
  - market-research
  - persona
  - nemotron-personas
  - brand-perception
  - korea
task_categories:
  - text-classification
  - tabular-classification
---

# AI 합성 패널 설문 응답 — 대학 브랜드 인식 조사 (69,001명 × 10개국)

대학 브랜드 인식 설문지를 **NVIDIA Nemotron-Personas 10개국 합성 페르소나 패널**에 적용해,
LLM이 각 페르소나를 연기하며 답한 **합성(synthetic) 설문 응답 69,001건**입니다.
실제 사람의 응답이 아니며, 실측 조사 전의 가설 탐색·문항 정련·분석 파이프라인 개발을 위해 만들어졌습니다.

> ⚠️ **성격 규정**: 절대 수치는 모집단 추정치가 아닙니다. 구조·순위·격차·세그먼트 간 패턴 탐색 용도로만 사용하세요.
> 생성 엔진(LLM)별 사전확률 차이가 일부 문항에 실재합니다(아래 "주의사항" 참조).

## 어떻게 만들어졌나 (생성 파이프라인)

```
① 설문 정제        국내판 52문항 + 해외판 41문항 (모듈 M1~M7 + Kano + 채용담당자 블록)
② 다국어 번역      해외판을 7개 언어로 번역 (en 마스터 → pt·es·fr·ja·vi·nl·hi)
                   — LLM 번역 + 독립 QA 에이전트 검수 (182키 완전성·철자혼동 테스트 보존 확인)
③ 페르소나 표집    nvidia/Nemotron-Personas-{Korea,USA,Singapore,India,Brazil,El-Salvador,
                   France,Japan,Vietnam,Belgium}에서 69,000명 층화 표집
                   — 설문 스크리너 적격성(연령창·업계 종사자 제외)을 표집 시점에 적용
                   — 언어 라우팅: India는 first_language 기준 en/hi, Belgium은 region 기준 nl/fr
④ 응답 생성        3개 LLM 엔진 병렬 — 페르소나 전문(全文)을 프롬프트에 넣고
                   "그 사람으로서 정직하게, 모르면 모른다고" 답하도록 지시
                   — grok-4.5 48,050 / gpt-5.5 10,277 / claude-sonnet 10,184 / grok(repair) 490
⑤ 취합·QC          uuid 중복 제거(39건) + 페르소나 메타 조인 → 본 parquet
```

- 응답자당 1행, 배치(15~25명) 단위 생성 후 병합.
- 스크리너 문항과 페르소나에서 직접 도출되는 인구통계(연령·직업·지역 등)는 LLM이 답하지 않고 원 페르소나 메타데이터에서 조인.

## 규모·구성

| 국가 | 세그먼트 | n |
|---|---|---|
| Korea (국내판, ko) | general_adult 14,297 / recruiter 418 / student_examinee 285 | 15,000 |
| USA | prospective_student 4,227 / relations 1,773 | 6,000 |
| Singapore | prospective_student 4,415 / relations 1,585 | 6,000 |
| India (en/hi) | prospective_student 5,799 / relations 201 | 6,000 |
| Brazil (pt) · El-Salvador (es) · France (fr) · Japan (ja) · Vietnam (vi) · Belgium (nl/fr) | prospective_student 각 6,000 | 36,000 |
| **계** | | **69,001** |

세그먼트: 국내 `general_adult`(20–49) / `recruiter`(채용 관여, 비삼성) / `student_examinee`(수험생),
해외 `prospective_student`(18–30 잠재 유학생) / `relations`(31–65 연구·산업 관계자).

## 스키마

| 컬럼 | 설명 |
|---|---|
| `uuid` | 원 Nemotron-Personas 레코드 uuid (원 데이터셋과 조인 키) |
| `engine` | 응답 생성 엔진: `grok` / `codex`(gpt-5.5) / `sonnet` / `grok-repair` |
| `batch_id` | 생성 배치 식별자 |
| `country` / `variant` / `segment` / `lang` | 국가 / 국내·해외판 / 세그먼트 / 설문 언어 |
| `age` `sex` `marital_status` `education_level` `occupation` `bachelors_field` `region` | 페르소나 메타(원 데이터셋에서 조인) |
| `answers_json` | 문항ID→응답값 JSON 문자열 (아래 응답 계약) |

**응답 계약(answers_json)** — 단일선택: 코드 문자열(`"1"`) · 다중선택: 코드 배열 · 척도/수치: 정수 ·
그리드: `{행코드: 값}` · 순위/개방형 목록: 배열 · 개방형: 짧은 자유 텍스트(응답자 언어).

**문항 ID 체계** — `SQ*` 스크리너(표집 시 적용, 응답에 없음) · `A*` 브랜드 인지(M1) · `B*` 연상(M2) ·
`C*`/`C_OV*` 영문 네이밍(M3) · `D*` 기업(삼성) 연계(M4) · `E*` 포지셔닝·호감·의향(M5, `E3`=주의문항) ·
`F*`/`F_OV*`/`F_R*` 장벽·채널(M6) · `G*` 데모(M7) · `K1~K4` Kano 쌍문항 · `R1~R3` 채용담당자 전용.
해외판은 비교군이 SNU·Yonsei·SKKU·NUS·HKUST로 교체되고 철자혼동 테스트(`A4`: 실존/오기 판별) 포함.

## 품질 지표 (전량 기준)

- 주의문항(E3) 통과율 **99.8%** (68,867/69,000)
- 배치 커버리지(요청 페르소나 전원 응답) 사실상 100% — 리페어 스윕으로 누락 0 마감
- E1 직선응답: 해외 4.6%(저인지의 실질 신호로 해석) / 국내 0.0%
- 개방형 채움률 72%, uuid 중복 제거 39건

## ⚠️ 주의사항 (반드시 읽기)

1. **합성 데이터입니다.** 실제 여론이 아니며, 특히 온라인 커뮤니티 담론 노출이 필요한 문항(부정 이슈 전이 등)은 재현되지 않습니다.
2. **엔진 효과가 실재합니다.** 순위·격차·퍼널 구조는 엔진 간 안정적이나, 규범 판단 문항(예: 기업 연계가 이미지에 주는 영향 `D3`)의 절대 수준은 엔진에 따라 크게 다릅니다(같은 셀에서 net +71 vs −50까지). `engine` 컬럼으로 층화 점검을 권합니다.
3. **엔진×국가 배정이 무작위가 아닙니다.** 생성 순서 탓에 Belgium 표본의 85.9%, Brazil의 42.1%가 codex 생성입니다. **국가 간 비교는 grok 엔진만 필터링해서** 수행하길 권합니다.
4. 보조인지(A3) 등 인지 절대값은 엔진 관대함에 민감 — 상대 비교로만 사용하세요.

## 출처·라이선스

- 페르소나 원천: [NVIDIA Nemotron-Personas](https://huggingface.co/collections/nvidia/nemotron-personas) 10개국 데이터셋
  (`nvidia/Nemotron-Personas-Korea` 외 9종, **CC-BY-4.0**). 본 데이터셋의 페르소나 메타 컬럼은 해당 데이터셋의 파생물입니다.
- 응답 텍스트: grok-4.5 / gpt-5.5 / claude-sonnet 생성 합성 텍스트.
- 본 데이터셋 라이선스: **CC-BY-4.0** (원천 귀속 고지 유지 필요).

## 인용

```
AI Synthetic Panel Survey Answers — University Brand Perception (Ginko), 2026.
Synthetic survey responses over NVIDIA Nemotron-Personas (10 countries), 69,001 respondents.
https://huggingface.co/datasets/supernyoung/ai_panel_surv_ansr_ginko
```
