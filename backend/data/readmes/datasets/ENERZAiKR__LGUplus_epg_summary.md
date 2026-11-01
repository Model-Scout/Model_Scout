---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- summarization
- text-retrieval
tags:
- korean
- tv
- epg
- broadcast
- synthetic
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.csv
  - split: test
    path: data/test.csv
---

# LGUplus EPG with Program Summaries

실제 U+tv EPG 편성표에 프로그램별 **방송 내용 한 문장 요약**(교사 LLM 생성)과 **원본 EPG 시놉시스**를
부여한 데이터셋입니다.

## train / test 구성

| split | 규모 | 소스 | 기간 |
|---|---|---|---|
| **train** | 113,775 | 주간 EPG(`week`, 258채널) + 신규 원본 EPG(`avevent`, 382채널) 첫 주 | 6/03~09 + 6/07~13 |
| **test** | 69,180 | 신규 원본 EPG(`avevent`) 다음 주 | 6/14~20 |

- `source` 컬럼으로 두 원천 구분: `week`(기존 주간 EPG, 합성 슬롯 포함) / `avevent`(신규 이벤트 테이블 원본, 19일 연속 중 발췌)
- test는 train과 겹치지 않는 별도 주(6/14~20)로, 일반화 평가용

## 요약 생성 (`summary`)

교사 LLM(Qwen3-235B-A22B-Instruct-2507-FP8)이 프로그램별로 "자막을 실제로 요약한 것 같은"
한 문장(60~80자)을 생성합니다. 근거 우선순위: 원본 실물 시놉시스(`orig_synopsis`)가 있으면 그것을
재서술, 없으면 네이버 검색(나무위키·위키·방송사) 근거, 그마저 없으면 채널·장르 기반 서술.

## 컬럼

| 컬럼 | 설명 |
|---|---|
| `source` | `week` / `avevent` (원천 구분) |
| `program_id` | 원천 내 프로그램 ID (source별로 독립) |
| `channel_number` / `channel_name` / `channel_genre` | 채널 정보 / 채널 장르 |
| `genre` / `subgenre` | 프로그램 대분류 / 소분류 장르 (U+ 코드표 gr1/gr2) |
| `title` / `episode` | 제목(부제 포함) / 회차 |
| `day_of_week` / `date` | 방영 요일 / 일자 |
| `start_time` / `end_time` / `duration_min` / `is_rerun` | 방영 시간 / 재방송 여부 |
| `summary` | **방송 내용 한 문장 요약** (LLM 생성) |
| `orig_synopsis` | **원본 EPG 시놉시스** (실물, 없으면 빈 값; 약 26~27%) |

## 연계 데이터셋

- [HBKenerzai/LGUplus_viewing_history](https://huggingface.co/datasets/HBKenerzai/LGUplus_viewing_history) · [HBKenerzai/LGUplus_daily_persona](https://huggingface.co/datasets/HBKenerzai/LGUplus_daily_persona) · [HBKenerzai/LGUplus_weekly_persona](https://huggingface.co/datasets/HBKenerzai/LGUplus_weekly_persona)

## 유의

요약은 LLM 생성 합성 데이터로 실제 방송 내용과 다를 수 있습니다(특히 검색 근거가 없어 채널·장르 기반으로 생성된 경우).
`orig_synopsis`가 있는 항목은 방송사 제공 실물 설명입니다. 연구/비상업 용도 권장(`cc-by-nc-4.0`).
