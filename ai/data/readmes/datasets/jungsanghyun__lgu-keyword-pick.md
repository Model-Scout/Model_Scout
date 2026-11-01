---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- text-classification
- text-generation
tags:
- persona
- recommendation
- keyword
- korean-tv
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
  - name: block
    dtype: int64
  - name: n_programs
    dtype: int64
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 999490974
    num_examples: 451351
  - name: test
    num_bytes: 10886989
    num_examples: 4859
  download_size: 992896106
  dataset_size: 1010377963
---

# LGUplus 키워드 선택 (Task 2)

LGUplus 컨텍스트 이해 POC용 소형(350M) 모델 학습 데이터셋. 교사 **Qwen3-235B-A22B-Instruct-2507-FP8**로 생성.
[Task 1: 롤링 페르소나](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona) 와 같은 시청자·동일 test 분리.

**키워드 선택**: `페르소나 + 최근 2시간 시청 + 후보 키워드` → 지금 추천하기 가장 좋은 유튜브 검색어 1개.

## 포맷 (chat `messages`)

각 row = 하나의 `(persona, 날짜, 2시간 블록)`.

| 컬럼 | 설명 |
|---|---|
| `persona_id` / `date` / `block` | 시청자 / 날짜 / 2시간 블록 시작시각 |
| `n_watched` | 그 블록에 실제 시청한(정답 후보) 키워드 수(2~4) |
| `pick_in_watched` | 교사가 고른 키워드가 시청 키워드였는지(distractor 아님) |
| `messages` | `[system, user, assistant]` (content=문자열) |

- **system**: 키워드 큐레이터 지시
- **user**: `[페르소나]`(Task1 산출) + `[최근 2시간 시청]` + `[후보 키워드]`(번호목록)
- **assistant**(타깃): 선택된 키워드 1개

## 후보 구성
- 후보 8개 = 그 블록에 15분+ 시청한 프로그램들의 키워드(정답 후보, 2~4개) + **distractor**(같은 시청자의 다른 시간대 시청 키워드 → 부족분은 카탈로그) 패딩.
- 프로그램별 키워드는 각 프로그램 요약에서 생성(유튜브 검색어 스타일, 3~6단어). 스타일 참고: `jungsanghyun/subtitle-summary-{lgu,dataset}`.
- 교사가 시청 후보를 고른 비율 ≈ 92.5%(나머지는 페르소나에 더 맞는 distractor 선택).

## 스플릿
- `train`: 177,708 (9,900 persona) · `test`: 1,809 (100 persona) — persona 단위 분리(Task1과 동일 test 셋, 누수 없음)

## 출처
- 시청이력/페르소나: `HBKenerzai/LGUplus_viewing_history`, Task1 페르소나
- EPG 요약: `HBKenerzai/LGUplus_epg_summary`
