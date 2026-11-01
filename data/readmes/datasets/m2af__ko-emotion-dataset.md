---
language:
- ko
dataset_info:
  features:
  - name: created_date
    dtype: string
  - name: source
    dtype: string
  - name: context
    dtype: string
  - name: annotation
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 510197
    num_examples: 1039
  download_size: 150813
  dataset_size: 510197
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# 한국어 감정 단문 데이터셋
## 데이터 개요
- 데이터 개수: 총 1039개
- 라벨러: (A, B, C, D, E)로 표시
- 단문 출처: X, Threads, Youtube, Naver Blog, Naver Cafe

## 감정 라벨 분류 표
- 중분류, 소분류로 구분
- 소분류의 대표 감정을 기준으로 구분
- 중분류 (총 9개)
  - 기쁨, 사랑, 슬픔, 두려움, 분노, 미움(상대방), 욕망, 싫어함(상태), 수치심
- 소분류 (총 63개)
  - 기쁨: 반가움, 즐거움, 신명남, 자신감, 감동, 만족감, 편안함, 고마움, 신뢰감, 안정감, 공감, 자랑스러움
  - 사랑: 호감, 귀중함, 매력적, 두근거림, 아른거림, 너그러움, 열정적임, 다정함, 동정(슬픔)
  - 슬픔: 억울함, 외로움, 후회, 실망, 허망, 그리움, 수치심, 고통, 절망, 무기력, 아픔
  - 두려움: 위축감, 놀람, 공포, 걱정, 초조함
  - 분노: 원망, 불쾌, 날카로움, 타오름
  - 미움(상대방): 반감, 경멸, 비위상함, 치사함, 불신감, 시기심, 외면, 냉담
  - 욕망: 욕심, 궁금함, 아쉬움, 불만, 갈등, 기대감
  - 싫어함(상태): 답답함, 불편함, 난처함, 서먹함, 심심함, 싫증
  - 수치심: 부끄러움, 죄책감, 미안함

## 활용
- Active Learning (감정 분류)

## Reference
- 조경은(2011). 서사구조의 자동 분석 기법을 통한 캐릭터 감성표현 모델 연구. 동국대학교 산학협력단
