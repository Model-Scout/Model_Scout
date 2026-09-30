# Semantic 골든셋 라벨 점검

API 호출 없이 라벨의 출처 신뢰도와 DB 정합성을 점검한 결과다. `audit_golden.py`로 재생성한다.

## 신뢰도 등급 기준

| 등급 | 기준 |
|---|---|
| A | 사례 confidence=high, 원문 인용 있음, 사례가 고른 원본 모델이 그대로 정답으로 도달 |
| B | confidence=medium, 또는 인용 없음, 또는 변환본(GGUF 등)으로 매핑해야 정답 도달 |
| C | confidence=low (모델 비교 없이 사용만 기록한 사례 등) |

## 요약

- 전체 질의 40개, 채점 가능 28개
- 채점 가능 질의 등급: A 3 · B 17 · C 8
- 라벨 오류: 0개 질의

## 라벨 오류

없음. 채점 가능한 모든 질의의 정답이 조건 필터를 통과하고, must_exclude는 실제로 규칙을 위반한다.

## 질의별 점검

| 질의 | 사례 | task | 채점 | 등급 | 도달 가능한 정답 | 주의 |
|---|---|---|---|---|---:|---|
| `sg_g002` | c022 | translation | ✅ | B | 2 | - |
| `sg_g004` | c005 | feature-extraction | ✅ | B | 1 | - |
| `sg_g005` | c021 | translation | ✅ | A | 1 | - |
| `sg_g006` | c024 | automatic-speech-recognition | ✅ | B | 1 | - |
| `sg_g007` | c026 | automatic-speech-recognition | ✅ | C | 1 | 정답 근거 원문 인용 없음 |
| `sg_g008` | c026 | automatic-speech-recognition | ✅ | C | 1 | 사례 원본이 아닌 변환본으로만 정답 도달; 정답 근거 원문 인용 없음 |
| `sg_g009` | c018 | summarization | ✅ | B | 1 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g010` | c032 | image-text-to-text | ✅ | B | 1 | - |
| `sg_g013` | r2-a005 | feature-extraction | ✅ | C | 1 | 정답 근거 원문 인용 없음 |
| `sg_g014` | r2-a006 | text-classification | ✅ | C | 1 | - |
| `sg_g015` | r2-b004 | text-generation | ✅ | A | 4 | - |
| `sg_g017` | r2-b005 | text-generation | ✅ | C | 1 | - |
| `sg_g018` | r2-c105 | automatic-speech-recognition | ✅ | C | 1 | 정답 근거 원문 인용 없음 |
| `sg_g019` | r2-c106 | automatic-speech-recognition | ✅ | C | 1 | - |
| `sg_g020` | r2-c107 | automatic-speech-recognition | ✅ | C | 1 | 정답 근거 원문 인용 없음 |
| `sg_g021` | r2-b001 | text-generation | ✅ | B | 4 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g022` | r2-b003 | text-generation | ✅ | B | 4 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g023` | r2-b007 | summarization | ✅ | B | 4 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g024` | r2-a001 | feature-extraction | ✅ | B | 2 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g025` | r2-a002 | feature-extraction | ✅ | B | 2 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g026` | r2-c101 | automatic-speech-recognition | ✅ | B | 3 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g027` | r2-c102 | automatic-speech-recognition | ✅ | B | 1 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g028` | r2-c103 | automatic-speech-recognition | ✅ | B | 2 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g029` | r2-b006 | summarization | ✅ | B | 1 | 사례 원본이 아닌 변환본으로만 정답 도달 |
| `sg_g030` | r2-b002 | text-generation | ✅ | B | 0 | - |
| `sg_g003` | c022 | translation | ✅ | B | 0 | 원 사례에 조건을 추가한 파생 질의 |
| `sg_g016` | r2-b004 | text-generation | ✅ | A | 0 | 원 사례에 조건을 추가한 파생 질의 |
| `sg_a001` | c030 | image-text-to-text | ✅ | B | 0 | - |
| `sg_g001` | c001 | text-generation | - | B | 1 | - |
| `sg_g011` | c002 | text-generation | - | B | 0 | - |
| `sg_g012` | c027 | automatic-speech-recognition | - | B | 0 | - |
| `sg_r001` | c004 | feature-extraction | - | B | 0 | must_exclude가 DB에 없어 검증이 공허함: sentence-transformers/all-MiniLM-L6-v2 |
| `sg_r002` | c006 | feature-extraction | - | B | 0 | - |
| `sg_r003` | c023 | translation | - | B | 0 | - |
| `sg_r004` | c029 | image-text-to-text | - | A | 0 | - |
| `sg_r005` | c031 | image-text-to-text | - | C | 0 | 정답 근거 원문 인용 없음 |
| `sg_r006` | r2-a003 | text-classification | - | B | 0 | - |
| `sg_r007` | r2-a004 | text-classification | - | C | 0 | - |
| `sg_r008` | r2-b008 | summarization | - | C | 0 | - |
| `sg_r009` | r2-c104 | image-text-to-text | - | A | 0 | - |

## 이 점검이 보장하지 않는 것

- 정답이 **유일하게** 맞는지는 보장하지 않는다. 사례에 없던 더 좋은 모델이 DB에 있으면 검색이 맞아도 오답으로 집계된다.
  채점 리포트에서 틀린 질의의 top-k를 사람이 보고 acceptable에 추가하는 누락 점검(false negative audit)이 필요하다.
- 사례 작성자의 판단이 옳은지는 검증하지 않는다. 등급은 근거의 강도이지 정답의 품질이 아니다.
