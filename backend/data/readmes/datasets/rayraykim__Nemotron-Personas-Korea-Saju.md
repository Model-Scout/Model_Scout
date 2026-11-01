---
language:
- ko
license: cc-by-4.0
size_categories:
- 1M<n<10M
task_categories:
- text-generation
- summarization
tags:
- korean
- saju
- four-pillars
- persona
- nemotron
- cultural
- synthetic
- llm-evaluation
- hallucination-evaluation
pretty_name: Nemotron-Personas-Korea + Saju
source_datasets:
- nvidia/Nemotron-Personas-Korea
viewer: false
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.parquet
---

# Nemotron-Personas-Korea + Saju 데이터셋

`nvidia/Nemotron-Personas-Korea` 페르소나에 **합성 생년월일시**와 **사주명리(四柱命理) 분석**을 추가한 파생 데이터셋.

본 작업은 NVIDIA Nemotron-Personas 연구 라인의 핵심 목표 — *"한국어 LLM의 페르소나 다양성·문화적 컨텍스트 표현·합성 인구 모델링 능력을 평가·강화한다"* — 를 사주명리(四柱命理)라는 한국 전통 문화 차원으로 확장합니다. 페르소나 + 사주 페어링 데이터로 (1) 한국 문화 도메인 LLM의 지식·표현 능력, (2) 결정론적 구조 + 생성 서사의 사실 정합성, (3) 페르소나-조건부 한국어 NLG 벤치마크를 가능하게 합니다.

> **Long-term goal**: 본 데이터셋은 단계적으로 확장되어 **NVIDIA Nemotron-Personas-Korea의 원본 규모(100만 페르소나)와 1:1 대응하는 100만 사주 페어링 공개 데이터셋**을 목표로 합니다. **현재 v7(1,000,000행)로 목표인 NVIDIA Nemotron-Personas-Korea 원본 규모(100만)와 1:1 대응을 달성**했습니다 (기존 v6 199,996 + 신규 800,004 = 1,000,000, validator 100% 통과). 모든 중간 버전은 CC BY 4.0으로 지속·공개적으로 릴리스됩니다. 자세한 일정은 [Roadmap](#roadmap-toward-1m-rows) 섹션 참조.

## Dataset Sources

- **원본 (Upstream)**: [`nvidia/Nemotron-Personas-Korea`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) (CC BY 4.0)
- **본 파생본**: 원본 26개 필드를 그대로 보존, 사주 관련 9개 필드만 추가. 동일 라이선스(CC BY 4.0) 적용.
- **사주 계산**: `sxtwl`(중국 천문력) + 자체 진태양시(LAST) 보정
- **LLM 서사**: v3.2~v6(앞 199,996행)은 `qwen3.6:latest` (Qwen3 36B-A3B MoE Q4_K_M) via Ollama, v7 신규 800,004행은 `Qwen/Qwen3-30B-A3B-FP8` via vLLM(H200)로 생성. 두 배치 모두 동일 프롬프트·5계층 validator를 거쳐 100% 통과. 사주 4주·오행·십신 등 **구조는 결정론적 코드 산출이라 배치 간 동일**하며, 서사 문체만 모델·서빙 차이로 미세하게 다를 수 있음.
- 모든 사주 분석은 **합성 생년월일시 기반**이며 실제 인물의 운세를 의미하지 않음.

## Intended Use

본 데이터셋은 NVIDIA Nemotron-Personas 연구의 사용 목적을 계승하면서 사주 도메인을 추가합니다:

- **Persona Generation**: 페르소나 + 사주 컨텍스트를 활용한 한국어 페르소나-조건 생성
- **LLM Fine-tuning**: 한국 문화 컨텍스트에 정통한 instruction-tuning / 다중 페르소나 학습 데이터
- **Synthetic Population Modeling**: 인구·지역·연령 분포를 보존하는 시뮬레이션용 페르소나
- **Saju NLG Benchmark**: 결정론적 사주 4주·오행·십신 + LLM 서사의 사실 정합성·환각 평가
- **Cultural Context Evaluation**: 한국 명리학 도메인의 LLM 지식·표현 능력 측정

## Out-of-Scope Use

다음 용도는 **명시적으로 권장되지 않습니다**:

- **개인 운세 판단**: 모든 생년월일시는 합성이며 실제 인물의 사주가 아님
- **운명결정론적 의사결정**: 진로·결혼·건강 등 실생활 결정에 사용 금지
- **차별·낙인 도구**: 사주 결과를 근거로 한 채용·평가·관계 판단
- **사주 학습 교재**: LLM 서사는 명리학 전문가 검수를 거치지 않음 (자동 검증 통과율은 100%이나 명리학적 깊이·정확성은 미보장)

## Use Cases and Research Directions

본 데이터셋은 다음 분야의 연구·서비스 기획에 활용될 수 있습니다.

### 학술 (Academic Research)
- **한국 문화 도메인 NLG 벤치마크** — 한국어 LLM의 명리학·사주 영역 사실 정합성·문화 표현 능력 측정. 결정론적 구조(4주·오행·십신)와 생성 서사의 환각률을 정량 비교 가능.
- **페르소나-조건부 생성 평가** — 페르소나(직업·연령·가족·지역) + 사주 결합 컨텍스트가 한국어 LLM의 일관성·구체성·사실성에 미치는 영향 측정.
- **하이브리드 결정론·생성 아키텍처 연구** — "구조는 코드, 서사는 LLM" 패턴을 한국어 도메인에서 실증한 사례. 한방·법률·의료 등 다른 한국어 전문 도메인으로의 일반화 연구 시드.
- **LLM 환각·문화 편향 측정** — 고령·무직 등 특정 인구 부분에서 환각 빈도가 더 높다는 본 데이터의 관찰을 출발점으로, 한국어 LLM의 사회적 편향 정량 연구.
- **한국어 LLM 비교 평가** — HyperCLOVA X · A.X · Solar · KoAlpaca · Gemma-Korean · Qwen · Llama 등 모델군의 한국 문화 컨텍스트 능력을 동일 평가 셋으로 비교.
- **동아시아 문화권 확장 연구** — 사주(한국)→八字(중국)→四柱推命(일본) 등 동아시아 명리 전통의 LLM 평가 표준화 시드.

### 산업·서비스 (Industry & Services)
- **사주·운세 콘텐츠 서비스** — 포스텔러·점신·헬로우봇 등 기존 시장의 자동 콘텐츠 다양화. 결정론적 4주 + LLM 서사 분리 구조로 사실 오류 제어 가능.
- **페르소나 기반 추천·커머스** — 인구통계 + 사주 + 성향 패턴으로 정밀 타깃팅, 한국 시장 특화 추천 시스템.
- **한국형 챗봇·캐릭터 AI** — 한국 문화 컨텍스트에 정통한 가상 인격(NPC·튜터·동반자 AI) 학습 데이터.
- **작명 서비스** — 부족 오행을 보완하는 이름 추천 자동화.
- **마케팅·UX 페르소나 시뮬레이션** — 사생활 침해 없이 한국 인구 분포를 반영한 합성 페르소나로 시나리오 검증.
- **게임·인터랙티브 픽션** — 결정론적 페르소나 시드 + 동적 사주 서사로 일관된 캐릭터 생성.
- **한국 문화 학습 콘텐츠** — 외국인 한국어 학습자·한국 문화 연구자를 위한 사주 도메인 컨텍스트.

### 기술 (Technical Methodology)
- **결정론적 사실 + 생성 서사 패턴** — 도메인 환각 차단의 일반화 가능 설계. 사주를 넘어 한방·법률·의료·세무 등 정확성이 중요한 한국어 도메인에 응용 가능.
- **5계층 자동 검증기(S·F·D·M·P)** — 한국어 NLG 환각 평가 자동화의 재사용 가능 가이드라인. 페르소나 이름 충돌 가드 등 한국어 특수 케이스 포함.
- **진태양시(LAST) 보정 알고리즘** — 한국 컨텍스트에 맞춘 사주 계산 표준화의 공개 자원. 경도 보정 + 균시차로 시주 ~30% / 일주 ~3.5% 정확도 개선.
- **발열 친화적 throttled-resume 파이프라인** — GPU 클러스터 없이 단일 데스크톱·맥북에서 1만행+ 생성 가능. 한국 중소 연구실·1인 개발자 친화적.
- **결정론적 시드 기반 합성** — `(uuid, age)` SHA-256 시드 → 같은 페르소나는 항상 같은 사주. 재현성·연구 신뢰성 보장.

## Vision: Contribution to Korean Sovereign AI

본 데이터셋은 *작은 규모(1만 행)이지만* **한국형 소버린 AI(Sovereign AI)** 의 다음 요소에 기여하고자 합니다.

### 1. 한국어·한국 문화 데이터 주권
영미·중국 LLM이 약한 한국 전통 문화 도메인(사주·명리)에 대해, **한국어 LLM이 책임 있게 답변할 수 있는 평가·학습 자원**을 제공합니다. 외산 모델에 한국 문화 콘텐츠를 일방적으로 의존하지 않기 위한 디지털 주권의 한 조각으로 기능하기를 기대합니다.

### 2. 합성 데이터 기반 한국형 평가 인프라
NVIDIA Nemotron-Personas-Korea의 100만 합성 페르소나를 활용하여 **사생활 침해 위험 없이** 한국 LLM 평가셋을 구축할 수 있음을 실증합니다. 향후 한국 정부·산업의 AI 평가 인프라(K-Data Dam, AI 신뢰성 거버넌스, K-LLM 리더보드 등)에 기여 가능한 데이터·방법론 시드.

### 3. 한국형 LLM 비교·검증 벤치마크
HyperCLOVA X·A.X·Solar·KoAlpaca 등 **국내 LLM**과 Qwen·Gemma·Llama·GPT 등 **해외 LLM**의 한국 문화 컨텍스트 능력을 동일 평가 표준으로 비교할 수 있는 공통 벤치마크. 한국어 LLM 경쟁력 측정의 한 축.

### 4. 중소 연구실·1인 개발자 친화 방법론
대규모 GPU 클러스터 없이 **단일 데스크톱·맥북에서 10만행+ 생성**이 가능함을 실증 (10K ~38시간, 100K ~155시간, 발열 throttle 적용). 한국 AI 생태계의 저변 확대 — 대학·스타트업·1인 개발자가 도메인 데이터셋을 직접 구축할 수 있는 레퍼런스.

### 5. 동아시아 문화권 LLM 연구의 시드
사주는 한국·중국·일본·베트남·대만이 공유하는 동아시아 명리 전통의 한 형태입니다. 본 작업의 (1) 결정론적 구조 + 생성 서사 분리 패턴, (2) 5계층 검증 방법론, (3) 진태양시 보정은 **동아시아 문화권 LLM 평가 표준화의 첫 걸음**으로 확장될 수 있습니다.

### 6. 책임 있는 합성 데이터 활용 모델
원본 NVIDIA 페르소나 라이선스(CC BY 4.0) 준수, attribution 명시, 운명결정론적 사용 제한, 환각률 투명 공개 — **합성 데이터의 책임 있는 활용 사례**로서 향후 한국 합성 데이터 정책 논의에 참고 자료가 되기를 기대합니다.

> 본 데이터셋이 한국 AI 생태계의 작은 한 조각으로, **한국형 LLM이 한국인의 삶·문화·언어를 더 깊이 이해하는 길**에 미세하게나마 기여하기를 바랍니다. 사주는 그 자체로 정답이 아니지만, 한국 사회가 오랜 시간 축적해온 문화 코드의 일부이며, 한국어 LLM이 이 코드를 다룰 때 *환각 없이·책임 있게·정확히* 다루는 것은 한국형 AI의 신뢰성에 기여하는 일이라고 믿습니다.

## 파일 구성

| 파일 | 행 수 | 통과율 | 설명 |
|---|---|---|---|
| `data/sample_100_v3.jsonl` | 100 | 100% | PoC |
| `data/sample_1000_v3.jsonl` | 1000 | 99.5% | 1차 확장 |
| `data/sample_5000_v3_clean.jsonl` | 5000 | 99.96% | 2차 + 51건 재생성 |
| `data/sample_10000_v3_final.jsonl` | 10000 | 100% | v3.2 (재생성 + 강화 프롬프트) |
| `data/sample_20000_v3_final.jsonl` | 20000 | 100% | v4 작업 중 산출 (HF 미공개) |
| `data/sample_100000_v3_final_dropped.jsonl` | 99,999 | 100% | v5 (1건 stubborn drop, parquet 152.8MB) |
| `data/sample_200000_v6_final.jsonl` | 199,996 | 100% | v6 (v5 99,999 + batch2 99,997, 4건 stubborn drop) — HF `data/train-0000{0,1,2}-of-00003.parquet` |
| **`data/train-extra-000{00..16}.parquet`** | **800,004** | **100%** | **v7 신규 (Qwen3-30B-A3B-FP8 / vLLM / H200, 17 샤드)** |
| **합계 (HF 공개)** | **1,000,000** | **100%** | **v7 — 원본 100만과 1:1 대응 완료** |

## 추가 필드 (원본 26 → 35)

### 합성 출생 정보 (deterministic)
- `birth_datetime_synth` — `YYYY-MM-DD HH:MM` (KST 기준, uuid+age 시드로 결정론적)
- `birth_province` / `birth_longitude_e` — 시도와 행정중심 경도(°E)
- `last_datetime` — 진태양시(LAST) ISO 문자열 — KST에서 경도 보정 + 균시차(Equation of Time) 적용
- `longitude_offset_minutes` — KST 대비 경도 보정값 (음수: 한국 대부분이 동경 135°E 기준선보다 서쪽)
- `equation_of_time_minutes` — 출생일 EoT (±15분 범위)

### 사주 4주
- `saju_pillars.{year,month,day,hour}` — 각 주의 천간(`stem_ko`/`stem_hanja`/`stem_element`/`stem_yin`)과 지지(`branch_*`) 8개 글자
- `saju_day_master` — 일간 표기 (예: `"기(己) 토음"`)

### 오행·십신
- `saju_elements` — 木火土金水 8글자 카운트
- `saju_elements_dominant` / `saju_elements_lacking` — 강한·부족 오행
- `saju_sipsin.{year,month,day,hour}` — 일간 기준 십신(천간/지지)

### LLM 생성 서사 (qwen3.6:latest, Q4_K_M)
- `saju_narrative.saju_summary` — 사주 4주·일간 중심 2-3문장 요약
- `saju_narrative.personality_reading` — 일간·강한 오행 성향 해석
- `saju_narrative.career_reading` — 십신·직업 흐름 해석
- `saju_narrative.lacking_element_advice` — 부족 오행 보완 조언
- `saju_narrative_error` — 생성 실패 시 오류 메시지(`null`이면 정상)

## 사주 계산 기준

### 4주 산출
- `sxtwl` 라이브러리로 절기(節氣) 기반 月柱·年柱 처리
- 일주는 LAST 기준(자정 경계 자동 처리)
- 시주: LAST 시각 → 12지지 매핑 + 갑기·을경·병신·정임·무계 시간천간 룰

### 진태양시(LAST) 보정
- KST는 동경 135°E 기준이지만 한국은 124°-131°E → 시계상 시각이 진태양시보다 16-44분 빠름
- 균시차(Spencer 근사식)로 ±15분 추가 보정
- 결과: 시주의 약 30%, 일주의 약 3.5%가 LAST 보정 없이는 다른 값

### 경도 매핑 (시도 행정중심)
| 시도 | 경도(°E) | 시도 | 경도(°E) |
|---|---|---|---|
| 서울 | 126.978 | 강원 | 128.160 |
| 부산 | 129.075 | 충청북 | 127.489 |
| 대구 | 128.601 | 충청남 | 126.800 |
| 인천 | 126.706 | 전북 | 127.139 |
| 광주 | 126.851 | 전라남 | 126.460 |
| 대전 | 127.384 | 경상북 | 128.510 |
| 울산 | 129.317 | 경상남 | 128.690 |
| 세종 | 127.289 | 제주 | 126.500 |
| 경기 | 127.050 | | |

district 단위 해상도는 미적용 (시도 내 ±0.5° = ±2분 차이 — 시주 경계 부근에서만 영향).

## 합성 생년월일시 결정성

`(uuid, age)` SHA-256을 시드로 다음 순서로 4번 RNG 호출:
1. birthday_passed ∈ {True, False}
2. day-of-year (입력된 age와 일치)
3. hour ∈ [0, 23]
4. minute ∈ [0, 59]

→ 같은 페르소나는 항상 같은 생년월일시·사주를 가짐. 재현 가능.

## LLM 서사 생성

### 모델
- `qwen3.6:latest` (Qwen3 36B-A3B MoE Q4_K_M 양자화, ~23GB) via Ollama
- thinking off, temperature=0.4, num_predict=1024, format=json

### 프롬프트 설계 원칙
- 사주 수치는 결정론적 코드가 산출 → LLM은 **해석만** 담당
- 시스템 프롬프트에 **허용 십신 목록** 명시 → 입력 외 십신 용어 도입 금지
- 페르소나 디테일 2개 이상 본문 인용 의무
- 미신적·결정론적 단정("반드시 ~한다") 금지, 경향성 표현만 허용
- 출력은 4-키 strict JSON

### 프롬프트 v1 → v2 개선
| 지표 | v1 | v2 |
|---|---|---|
| 100행 검증 통과 | 98% | 100% (20행 동일 비교) |
| 십신 환각 | 2건 | 0건 |
| 페르소나 인용 밀도 | 보통 | 한자 병기·구체 디테일 추가 |

## 검증 기준

`saju_pipeline/validator.py`로 5계층 자동 검증:

| 카테고리 | 검사 내용 |
|---|---|
| **S** Schema | 4 키 존재, 비어있지 않음, 길이 30+ |
| **F** Fact | 본문 인용 천간·지지·십신이 계산 구조에 실제 존재 |
| **D** Day-master | 본문이 다른 일간을 단언하지 않음 |
| **M** Mysticism | "반드시", "운명적으로", "100%" 등 결정론적 표현 차단 |
| **P** Persona | 이름/직업/지역/연령 anchor 중 하나 이상 본문에 인용 |

v6(200,000행, batch1 + batch2 결합) 정제 파이프라인 결과: **199,996/199,996 (100%)** — stubborn 4건 drop (v5 1건 + batch2 3건):

**batch1 (v5, 100K)**: stubborn 1건 drop → 99,999/99,999
1. 1차 생성: **99.16%** (99,156/100,000)
2. regen_failures: **99.958%** (99,958/100,000) — 844건 중 802건 fix
3. fix_stubborn: **99.999%** (99,999/100,000) — 42건 중 41건 fix
4. 잔여 1건(`9014c259…`, 무토→갑목) drop → **100%**

**batch2 (v6 신규, 100K)**: stubborn 3건 drop → 99,997/99,997
1. 1차 생성: **98.84%** (98,844/100,000)
2. regen_failures: **99.935%** (99,935/100,000) — 1156건 시도, 1091건 fix, 65건 잔여
3. fix_stubborn: **99.997%** (99,997/100,000) — 65건 중 62건 fix
4. 잔여 3건(`4470548c…`/`0601441e…`/`3edbea17…`, 모두 갑목 day-master 호명) drop → **100%**

10000행(v3.2)도 동일한 3단계 파이프라인으로 100% 달성 (drop 없음).

## KSaju-Eval — 한국 사주 LLM 평가 suite (v8)

본 데이터셋의 검증기를 **공개 평가 도구**로 확장한 것으로, *임의의 LLM*이 페르소나 + 결정론적
사주(4주·오행·십신)를 받아 한국어 사주 서사를 얼마나 **환각 없이·구조를 활용하여** 작성하는지
0~1 점수로 측정합니다. 사주 구조는 코드가 산출한 정답이므로 **참조 답안 없이** 채점 가능하고,
모든 모델이 **동일 프롬프트**를 받으므로 통제된 비교가 됩니다. (코드·평가셋: `ksaju_eval/`)

- **factuality** (0.7): 5계층 validator(S/F/D/M/P) 기반 환각 회피 점수
- **engagement** (0.3): 십신 인용·페르소나 anchor(≥2)·구조 활용·길이 등 *적극적 활용도*
- **평가셋**: 2,000문항, 일간 오행(5)×연령대(4) 균형, seed 42 (재현 가능)

### 리더보드 (2,000문항, 높을수록 좋음)

| # | 모델 | KSaju | Factuality | Engagement | 비고 |
|---|---|---|---|---|---|
| **1** | **`exaone-32b-saju-curriculum`** (32B, 커리큘럼 증류) | **0.989** | 1.000 | 0.964 | **전체 1위** |
| 2 | `ko-gemma-saju-curriculum` (9B, 커리큘럼 증류) | **0.987** | 1.000 | 0.958 | 30B 교사 추월 |
| 3 | `Qwen3-30B-A3B-FP8` (본 데이터셋 생성 = **교사**) | **0.980** | 1.000 | 0.933 | — |
| 4 | `ko-gemma-saju-student` (9B, 일반 SFT 증류) | **0.977** | 1.000 | 0.925 | 교사와 0.003 차 |
| 5 | `ko-gemma-2-9b-it` (한국어 튜닝 베이스) | **0.949** | 0.999 | 0.832 | 증류 전 베이스 |
| 6 | `Qwen2.5-7B-Instruct` (다국어 7B) | **0.945** | 0.998 | 0.820 | — |

모든 모델이 환각 회피(factuality)는 ~1.0이나 **구조·페르소나 활용(engagement)에서 변별**됩니다.
**본 데이터셋은 우수한 증류(distillation) 코퍼스**임이 실증됐습니다:
- 일반 SFT 증류: 베이스 9B를 본 데이터로 학습 → 0.949 → **0.977**(30B 교사 0.980에 0.003 근접).
- **커리큘럼 증류**: 교사의 **engagement=1.0 행만** 골라 학습(`--min-engagement 0.99`, 4K예제·~33분)
  → **0.987로 30B 교사를 추월**. 9B가 3배 큰 교사를 능가(십신 0.982·페르소나 anchoring 0.853, 모두 교사 상회).

어댑터: `adapters/ko-gemma-saju-curriculum/`(교사 추월), `adapters/ko-gemma-saju-student/`. 학습 코드: `train/`.

모델별 평행 서사(같은 페르소나·사주, 다른 LLM)는 `ksaju_eval/parallel_narratives_100.jsonl` 참조.
HyperCLOVA X·A.X·Solar 등 한국형 LLM은 OpenAI 호환 엔드포인트만 있으면 동일 셋으로 추가 평가
가능 (`ksaju_eval/evaluate_model.py`). 자동 점수의 명리학적 타당성은 전문가 검수 gold-set 5K
(`ksaju_eval/goldset_5k.jsonl`, 검수 가이드 동봉)로 보정 예정.

### 알려진 실패 패턴 (정제 전 0.5%)
- F (~80%): 모델이 허용 십신 목록 외 용어 (정인·식신·정관 등)를 괄호 설명에 도입
- D (~40%): 일간을 다른 천간으로 잘못 표기 (드물게)
- 위 두 가지가 동시에 나타나는 행도 있음
- 페르소나 편향: 고령·무직 케이스에서 일반론적 명리학 표현 도입 빈도 높음

## 통계 (1,000,000행)

| 항목 | 값 |
|---|---|
| 일간 오행 분포 | 토:200,423 / 화:200,145 / 목:200,058 / 수:199,710 / 금:199,664 (균등, 200,000±0.2%) |
| 성별 | 여 50.4% / 남 49.6% |
| 연령 | 19~99세, 평균 50.7세 |
| 지역 (수도권 50.6%) | 경기 26.2% / 서울 18.6% / 부산 6.5% / 경남 6.2% / 인천 5.9% / 경북 5.0% |
| 사주 LAST 보정 영향 | 시주 ~30% / 일주 ~3.5%가 KST=LAST 가정 시 오류 |
| 처리 시간 | v3.2~v6(앞 200K): 행당 ~7초, Ollama 단일 스트림 데스크톱/맥북, 총 ~310h. v7(신규 800K): Qwen3-30B-A3B-FP8 / vLLM / 단일 H200, ~12–14 rows/s, 총 ~16h |
| 파일 크기 (Parquet, HF) | 약 2.3 GB (기존 305.4 MB + 신규 17 샤드 ~2.0 GB, zstd) |

## KSurvey PoC — 합성 설문 응답 (실험적 확장, `survey_pipeline/`)

본 데이터셋의 *"결정론적 구조 + LLM 생성"* 방법론을 **한국 합성 설문 응답**으로 확장한 개념 검증입니다.
페르소나(인구통계)를 조건으로 17문항 사회조사(삶 만족도·정치성향·사회이슈·소비·여가·신뢰 등) 응답을
LLM이 생성합니다. (코드·PoC 데이터: `survey_pipeline/`)

- PoC(1,000 페르소나, Qwen3-30B): 생성 0 에러, 스키마 통과 **98.8%**, 페르소나 일관성 OK
  (무직 → 직업만족도 "해당없음" 등).
- **⚠️ 핵심 한계 — 분포 붕괴**: 집계 marginal이 실제 한국 인구 다양성을 재현하지 못함
  (top_social_issue 주거 78%, trust_institutions 97% 단일값 등). 학계가 보고한 **"silicon sampling"**
  현상으로, **실측 분포(KOSIS·한국갤럽·KGSS) 보정 없이는 설문 모델이 성립하지 않음**을 정량적으로 보임.
- **용도 제한**: PoC 데이터는 실제 여론을 의미하지 않으며 방법론 검증용입니다. 보정 로드맵은
  `survey_pipeline/README.md` 참조.

## Bias, Risks, and Limitations

### 합성 데이터 한계 (Synthetic Data)
- 생년월일시는 `(uuid, age)` 시드 기반 합성 — 실제 인구통계학적 시간 분포 아님
- 시각의 분(minute)은 균등 분포로 합성, 실제 출산 시각 분포(통상 일중 변동)와 다름
- 페르소나 자체는 NVIDIA의 합성 페르소나 — 실제 인물 미반영

### 문화적 편향 (Cultural Bias)
- 사주명리는 한국·중국 동아시아 전통 문화 산물 — **비동아시아 컨텍스트에 일반화 불가**
- 강한 오행 분포(土 > 木 > 火 > 金 > 水)는 동아시아 사주 통계와 일치하지만, 모델 학습 분포의 편향이 추가로 반영될 수 있음
- 고령·무직 페르소나에서 명리학 클리셰(*"식신생재"*, *"정관격"* 등) 도입 빈도 더 높음 — LLM 베이스라인 환각 패턴
- LLM 모델(qwen3.6 36B-A3B)의 한국어 명리학 학습 분포는 알려져 있지 않음

### 사주 계산 정확도 (Saju Calculation)
- 경도는 시도(17개) 행정중심 1점 — district 단위 ±0.5°(~2분) 오차
- 절기 데이터 sxtwl(중국 천문력) 기반 — 한국 만세력과 ≤1일 차이 가능
- 야자시/조자시 분리 없이 LAST 23:00-00:59 통합 자시 처리
- 한국 지방시 보정은 표준 경도 보정 + 균시차(Equation of Time)만 — 실제 만세력 결과와 미세 차이 가능

### LLM 서사 한계 (LLM Narrative)
- 검증 통과율 100%는 **자동 validator 기준** — 명리학적 정확성·통찰의 깊이는 미보장
- 페르소나 외 추가 사실(역사적 사건·실제 지명·인물)은 검증 안 됨
- 서사 길이는 키당 70-300자 — 짧은 해석이며 깊이 있는 명리학 상담 대체 불가

### 운명결정론적 사용 금지
본 데이터는 페르소나-사주 페어링의 **학술 연구·LLM 평가·NLG 벤치마크** 용도입니다. 개인 운세 판단·진로 결정·관계 판단에 사용해서는 안 됩니다.

## 재현 방법

```bash
# 환경
python -m venv .venv && source .venv/bin/activate
pip install datasets sxtwl korean-lunar-calendar ollama

# Ollama 모델
ollama pull qwen3.6:latest

# 100행 PoC
python saju_pipeline/run_poc.py 100

# 1000행 throttled
python saju_pipeline/run_v3_throttled.py \
  --input  saju_pipeline/data/sample_1000.jsonl \
  --output saju_pipeline/data/sample_1000_v3.jsonl \
  --row-sleep 5 --cooldown-every 50 --cooldown-secs 60

# 검증
python saju_pipeline/validator.py saju_pipeline/data/sample_1000_v3.jsonl
```

## Roadmap: Toward 1M Rows

본 데이터셋은 NVIDIA Nemotron-Personas-Korea의 원본 규모(100만 페르소나)와 일대일 대응하는 **100만 사주 페어링 공개 데이터셋**으로 단계적으로 확장될 예정입니다. 단순한 규모 확장이 아니라, 각 단계마다 품질·검증·평가 도구를 함께 성숙시켜 나가는 것을 목표로 합니다.

### Public release schedule (planned)

| 단계 | 행 수 | 시점 | 핵심 개선 |
|---|---|---|---|
| v3.2 | 10,000 | 2026-05 (완료) | 100% validator 통과, LAST 보정, HF 데이터셋 카드 정식 공개 |
| v4 | 20,000 | 2026-05 (완료, HF 미공개) | 100K로 직접 점프하여 별도 공개는 생략 |
| v5 | 99,999 | 2026-05 (완료) | 100K v3 파이프라인 적용, 99.999% 검증 → 1건 drop으로 100%, parquet 152.8MB |
| v6 | 199,996 | 2026-06 (완료) | v5 + 신규 batch2 100K 결합 → 200K. 동일 파이프라인 재적용, 4건 stubborn drop, parquet 305.4MB |
| **v7 (current)** | **1,000,000** | **2026-06 (완료)** | **🎯 200K → 1M 도약. 신규 800,004행을 Qwen3-30B-A3B-FP8 / vLLM / 단일 H200으로 ~16h 생성, validator 100% 통과. NVIDIA 원본 100만과 1:1 대응 완료** |
| v8 (후속) | 1,000,000+ | TBD | KSaju-Eval 평가 suite 정식 공개, 명리학 전문가 검수 gold-set 5K, 모델별 평행 서사(HyperCLOVA X·A.X·Solar 등), district-단위 경도 매핑 |

### Scaling strategy

단일 데스크톱·맥북에서 v3.2(10K)에 ~38시간, v5(100K)에 ~155시간 소요 → 100만 행은 단일 머신으로 **연 단위** 작업입니다. 따라서 다음 전략을 병행합니다:

- **분산 처리**: 다중 Ollama 인스턴스 / 다중 머신 클러스터로 병렬화. 결정론적 시드(`uuid` SHA-256) 덕분에 어떤 머신에서 처리하든 결과가 동일 → 작업 분담 안전.
- **커뮤니티 기여 모델**: 같은 코드·시드·검증기를 공유하므로 연구실·1인 개발자도 일부 행을 분담 생성 가능. PR 형태로 부분 결과 통합.
- **언어 모델 다양화**: qwen3 외에도 HyperCLOVA X · A.X · Solar · Gemma-Korean 등 한국형 LLM으로 서사 생성 → **모델별 평행 데이터셋**(같은 페르소나·사주, 다른 LLM 서사) 구축. 한국형 LLM 비교의 ground-truth 자원이 됨.
- **품질 게이트 강화**: 단계마다 validator 강화·실패 패턴 회귀 분석. 100% 통과 + 명리학 전문가 검수 gold-set 부착(v7~)으로 신뢰도 단계적 상승.
- **점진적 공개 원칙**: 모든 중간 단계(50K, 100K, 250K …)를 HuggingFace에 공개. 중단·은닉 없음.

### Commitment to public release

본 작업은 **지속적·공개적·재현 가능한** 원칙으로 진행됩니다:

1. **모든 중간 데이터셋은 CC BY 4.0으로 공개** — 비공개 사내 활용·유료 락인 없음
2. **코드(검증기·생성기·정제기)는 함께 공개** — `saju_pipeline/` 전체 오픈소스
3. **환각률·편향·통계는 모든 버전에서 투명 보고** — 데이터셋 카드에 정량 수치 갱신
4. **NVIDIA Nemotron-Personas-Korea attribution은 모든 버전에서 유지** — CC BY 4.0 의무 + 학술 윤리
5. **회귀 방지** — 새 버전이 이전 버전의 uuid·결정론적 결과를 깨뜨리지 않도록 시드 호환성 보장

100만 행 도달 시점에서는 단순 규모가 아니라 **한국 사주 도메인의 표준 LLM 평가·학습 자원**으로 자리잡는 것이 목표입니다. 이를 통해 한국형 sovereign AI의 한 작은 디딤돌이 되기를 희망합니다.

### Want to contribute?

본 데이터셋의 확장에 기여하실 분(연구실·1인 개발자·산업 파트너·명리학 전문가)을 환영합니다. 가능한 기여 형태:

- **연산 자원 분담**: 본인 머신에서 일부 uuid 범위 처리 후 결과 공유
- **모델 다양성 확장**: 한국형 LLM(HyperCLOVA X·A.X·Solar 등)으로 평행 서사 생성
- **명리학 전문 검수**: gold-set 후보 행에 대한 전문가 검토·교정
- **검증기 개선**: 새로운 환각 패턴 탐지 룰·다국어 케이스
- **응용 사례 공유**: 본 데이터로 만든 연구·서비스·튜닝 결과 공유

## Acknowledgements

본 데이터셋은 NVIDIA의 [`nvidia/Nemotron-Personas-Korea`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) 데이터셋을 토대로 제작되었습니다. 원본의 100만 한국어 페르소나가 없었다면 이 작업은 불가능했을 것입니다.

특히 한국 시·도 행정 분포·직업 분류·가족 구성·교육 단계를 통계적으로 정밀하게 반영한 페르소나 설계가 본 사주 증강 작업의 토대가 되었으며, 합성 데이터의 학술적 활용 가능성을 한국어 컨텍스트에서 입증한 NVIDIA Nemotron-Personas 연구 라인에 깊이 감사드립니다.

또한 본 작업은 다음 오픈소스 도구에 의존합니다:
- [`sxtwl`](https://github.com/yuangu/sxtwl_cpp) — 중국 천문력 기반 4주 계산
- [`korean-lunar-calendar`](https://pypi.org/project/korean-lunar-calendar/) — 양력↔음력 변환 (보조)
- [Ollama](https://ollama.ai/) — 로컬 LLM 추론 런타임
- Qwen3 36B-A3B MoE — 한국어 사주 서사 생성 모델
- [🤗 Datasets](https://github.com/huggingface/datasets) — 데이터 핸들링·업로드

## Citation

If you find the data useful, please cite **both** the upstream dataset and this derivative.
본 데이터셋을 사용하실 때는 상위 데이터셋과 본 파생본을 함께 인용해주십시오.

### Upstream — Nemotron-Personas-Korea (NVIDIA)

```bibtex
@software{nvidia/Nemotron-Personas-Korea,
  author = {Kim, Hyunwoo and Ryu, Jihyeon and Lee, Jinho and Ryu, Hyungon and Praveen, Kiran and Prayaga, Shyamala and Thadaka, Kirit and Jennings, Will and Sadeghi, Bardiya and Sharabiani, Ashton and Choi, Yejin and Meyer, Yev},
  title = {Nemotron-Personas-Korea: Synthetic Personas Aligned to Real-World Distributions for Korea},
  month = {April},
  year = {2026},
  url = {https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea}
}
```

### Derivative — Nemotron-Personas-Korea + Saju (this work)

```bibtex
@dataset{nemotron_personas_korea_saju,
  title  = {Nemotron-Personas-Korea + Saju Augmentation},
  year   = {2026},
  note   = {Persona-saju paired derivative of nvidia/Nemotron-Personas-Korea with
            true-solar-time corrected 4-pillar (四柱) calculation and qwen3.6-generated
            Korean saju narratives},
  url    = {https://huggingface.co/datasets/rayraykim/Nemotron-Personas-Korea-Saju}
}
```

## 변경 이력

- **v1** (2026-05-02): 100행 PoC, KST=LAST 가정
- **v2** (2026-05-02): 프롬프트 강화 (허용 십신 목록, 페르소나 인용 의무)
- **v3** (2026-05-02): KST→LAST 보정, 균시차 적용, 분(minute) 해상도 추가, 1000행 확장
- **v3.1** (2026-05-03): 5000행 확장, validator-fail 51건 재생성, 데이터셋 카드 작성
- **v3.2** (2026-05-05): 10000행 확장, 강화 프롬프트(`fix_stubborn.py`)로 잔여 환각 0건 달성, validator에 페르소나-이름 충돌 가드 추가 → **100% 통과**. HF 데이터셋 카드 정식화 (Intended Use·Limitations·Acknowledgements·Vision·Roadmap 섹션)
- **v4** (2026-05-07): 20000행 확장 (HF 미공개, 100K로 직접 점프)
- **v5** (2026-05-19): **100K 확장**. `run_v3_parallel` 기반 대량 생성, 동일 3단계 정제 파이프라인(`run_v3 → regen_failures → fix_stubborn`) 적용. 단계별 통과율 99.16% → 99.958% → 99.999%. 끝까지 환각이 잡히지 않은 1건(무토→갑목 day-master 호명) drop → **99,999/99,999 (100%)**. parquet zstd 152.8MB.
- **v6** (2026-06-04): **200K 확장**. v5 batch1 (99,999) + 신규 batch2 100K 결합. batch2도 동일 4단계 파이프라인 (run_v3_parallel → regen_failures → fix_stubborn → drop) 적용. 단계별 통과율 98.84% → 99.935% → 99.997%. 잔여 3건(모두 갑목 day-master 호명) drop → batch2 99,997/99,997 (100%). v5와 결합하여 **199,996/199,996 (100%)**. parquet zstd 305.4MB (4.8x 압축).
- **v7** (2026-06-15): **1,000,000행 도달 — 목표 달성**. 기존 v6 199,996행에 신규 800,004행을 추가하여 NVIDIA Nemotron-Personas-Korea 원본 100만과 1:1 대응 완료. 신규 배치는 업스트림 전체를 스트리밍하며 기존 200K uuid를 제외해 정확한 잔여 complement(800,004)를 선정(기존 200K가 순차 prefix가 아님을 uuid 대조로 확인). LLM 서사는 `Qwen/Qwen3-30B-A3B-FP8`을 vLLM(단일 H200)으로 서빙, 동시성 320으로 ~12–14 rows/s, 총 ~16h 생성. 동일 5계층 validator + `fix_failures_vllm.py`(금지어 주입 재생성) 정제로 **800,004/800,004 (100%)**. 기존 3 parquet 샤드는 무손상 유지하고 17개 신규 샤드(`data/train-extra-*.parquet`)를 증분 추가 → HF 총 **1,000,000행**.
- **v8** (예정): KSaju-Eval 평가 suite, gold-set, 모델별 평행 서사 등 품질·평가 심화 (자세한 계획은 [Roadmap](#roadmap-toward-1m-rows) 참조)
