---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- text-generation
tags:
- korean
- tv
- viewing-history
- persona
- recommendation
- synthetic
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# LGUplus Persona TV Viewing History

한국인 가상 페르소나 1만 명의 **일주일치 TV 시청이력** 합성 데이터셋입니다.
[nvidia/Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) 페르소나와
실제 U+tv EPG(258채널 × 7일, 2026-06-03~09) 편성표를 기반으로, 교사 LLM(Qwen3-235B-A22B-Instruct-2507-FP8)이
2단계로 생성했습니다.

## 생성 방법

1. **시청 스케줄 생성**: 페르소나(직업·나이·가족·취미)를 보고 요일별 시청 시간대를 추정
   (근거 문장을 `schedule_reasoning`으로 함께 생성 — 예: 주부/은퇴자는 평일 낮, 직장인은 저녁)
2. **프로그램 선택**: 각 (요일, 시간창)마다 해당 시간에 방영 중인 실제 편성표를 제시하고
   페르소나가 시청할 프로그램을 순서대로 선택 (채널 현실성 지시: 주류 채널 위주,
   전문채널은 취미·직업 일치 시에만 / 이미 본 (제목,회차) 재시청 금지)

## 규모 / 품질

| 항목 | 값 |
|---|---|
| 페르소나 | 10,000명 (Nemotron-Personas-Korea에서 랜덤 샘플, persona_id = 원본 인덱스) |
| 스플릿 | train 9,000 / test 1,000 (페르소나 단위 랜덤 분할, seed 42) |
| 시청 레코드 | 269,628개 (1인 평균 27.0개, 주간 평균 ~18.4시간) |
| 페르소나 내 중복 시청 | 0건 |
| 주류 채널(지상파·주요 종편/케이블) 비중 | 82% |
| 평일 낮 시청 (무직/주부 vs 직장인) | 12.1 vs 1.2 레코드/인 |

## 스키마 (`data/train.jsonl`, 1줄 = 1 페르소나)

```json
{
  "persona_id": 234053,
  "demographics": {"sex": "여자", "age": 41, "occupation": "무직", "province": "경상남", ...},
  "persona_text": "페르소나 서술 + 인적사항",
  "schedule_reasoning": "생활 리듬 기반 시청 패턴 근거 (2~4문장)",
  "schedule": {"월": [[10,11],[14,16],[21,22]], ..., "일": [[9,11],[19,22]]},
  "history": [
    {"day": "월", "window": [10, 11],
     "program_id": 33249, "channel": "KBS2", "title": "2TV 생생정보",
     "episode": "63회", "genre": "지상파",
     "watch_start": "2026-06-08 10:00", "watch_end": "2026-06-08 10:50",
     "reason": "생활 정보",
     "content_summary": "해당 방송 내용의 한 문장 요약 (LLM 생성, 웹검색 근거)",
     "content_grounded": true}
  ]
}
```

- `data/schedules.jsonl`: 1단계 산출물(스케줄+근거) 단독 파일 (train.jsonl에 동일 내용 포함)
- EPG 주간 매핑: 수=06-03, 목=06-04, 금=06-05, 토=06-06, 일=06-07, 월=06-08, 화=06-09
- EPG 일부(25.4%)는 결측 슬롯을 같은 요일 타입에서 채운 합성 편성이며, 시청이력 생성 시 동일 회차 재시청은 차단됨

### v2 추가 필드 (2026-07-08)
- `history[].content_summary`: 시청한 프로그램의 방송 내용 한 문장 요약 (교사 LLM이 웹검색 근거로 생성, 전 레코드 100% 매칭)
- `content_grounded`: 요약의 웹검색 근거 여부 (false = 채널·장르 기반 생성)

## 용도

- TV 프로그램 추천/개인화 모델 학습·평가
- 시청 패턴 기반 사용자 프로파일링 연구
- [HBKenerzai/LGUplus_summary_keyword](https://huggingface.co/datasets/HBKenerzai/LGUplus_summary_keyword)와 연계한 시청맥락 요약 실험

## 라이선스 / 유의

가상 인물 기반 합성 데이터입니다(실사용자 데이터 아님). 페르소나 원본(Nemotron-Personas-Korea, CC-BY-4.0)과
EPG 원천의 이용 조건을 함께 확인하세요. 연구/비상업 용도 권장(`cc-by-nc-4.0`).
