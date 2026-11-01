---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- text-generation
tags:
- persona
- recommendation
- korean-tv
- rolling
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: persona_id
    dtype: int64
  - name: date
    dtype: string
  - name: dow
    dtype: string
  - name: mode
    dtype: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 882904753
    num_examples: 199238
  - name: test
    num_bytes: 8904314
    num_examples: 1997
  download_size: 884905673
  dataset_size: 891809067
---

# LGUplus 롤링 시청 페르소나 (Task 1)

LGUplus 컨텍스트 이해 POC용 소형(350M) 모델 학습 데이터셋. 교사 모델 **Qwen3-235B-A22B-Instruct-2507-FP8**로 생성.

**롤링 페르소나 갱신**: `어제까지의 페르소나 + 오늘 하루(1일분) 시청이력` → 오늘을 반영한 갱신 페르소나. 주간 스텝·코드 계산 없이 매일 순수 일일 롤링(컨텍스트는 페르소나가 들고 다님).

## 포맷 (chat `messages`)

각 row = 하나의 `(persona, 날짜)` 갱신 스텝.

| 컬럼 | 설명 |
|---|---|
| `persona_id` | 시청자 ID |
| `date` / `dow` | 날짜 / 요일 |
| `mode` | `coldstart`(첫날) / `daily` |
| `messages` | `[system, user, assistant]` (content=문자열) |

- **system**: 태스크 지시(페르소나 갱신 분석가)
- **user**: `[이전 페르소나]` + `[오늘 시청 기록]`(시청시간·채널·제목·EPG장르·EPG설명·자막요약)
- **assistant**(타깃): 갱신된 페르소나 = `[장기 성향]`(프로즈) + `[최근 성향]`(프로즈) + `[시청 프로그램]` 표

### 페르소나 구조
- **장기 성향**: 누적 시청 패턴(장르·시간대·주제·정서) 기반 지속 취향.
- **최근 성향**: 오늘·최근 며칠 관심 + 새로 보기 시작(신규)·뜸해진(감소) 프로그램을 이름과 함께 프로즈로.
- **시청 프로그램 표**: 자리잡은 고정 루틴(`상승`·`안정`)만. 신규·일회성·뜸해진 건 표에 넣지 않고 최근 성향에 서술 → 표가 작게 유지됨(median 3).

## 스플릿
- `train`: 9,900 persona (199,238 step)
- `test`: 100 persona (1,997 step) — 고정 시드(42) 무작위, persona 단위 분리(누수 없음)

## 학습 (assistant-only loss)
`messages`가 문자열 content 표준형이라 `apply_chat_template`로 바로 사용. TRL `SFTConfig(assistant_only_loss=True)` + `{% generation %}` 포함 ChatML 템플릿으로 assistant 구간만 loss.

## 출처
- 시청이력: `HBKenerzai/LGUplus_viewing_history`
- EPG 요약/장르: `HBKenerzai/LGUplus_epg_summary`
