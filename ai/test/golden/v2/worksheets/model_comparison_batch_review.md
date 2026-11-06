# model_comparison 묶음 판정 — `mc08`~`mc10`

`mc01`~`mc07`은 정훈님 검수를 JSON에 기록했다. 이 문서는 남은 세 문항을
**후보 하나씩이 아니라 동일 근거를 공유하는 묶음 단위**로 최종 검수하기 위한 것이다.
후보는 검색 결과가 아니라, 동결 코퍼스 3,872개를 조건으로 전수 스캔한 뒤 모델 계열명으로
추린 것이다. 따라서 아래 묶음을 승인하면 나머지 후보도 이미 한 번씩은 규칙 검토를 거친다.

## 30초 검수 방법

각 문항마다 다음만 확인한다.

1. 질문이 실제로 묻는 조건과 라벨 기준이 맞는지 본다.
2. `2점 묶음`이 질문에 직접 맞는지 본다.
3. `예외`만 모델 카드를 열어 최종 결정한다.

`1점 묶음`은 관련은 있지만 변환본·재업로드·범위가 좁은 후보다. 없는 모델은 0점으로
따로 기록하지 않는다.

---

## `mc08` — Whisper small vs wav2vec / 한국어 ASR / 1B 이하

> Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 좋아? 1B 이하인 것 중 많이 쓰이는 것으로.

조건(ASR·한국어·core·1B 이하)은 기계 검증됐다. 두 계열 모두 최종 답에 포함된다.

| 판정 | 묶음 | 이유 |
|---:|---|---|
| 2점 | `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Kkonjeong/wav2vec2-base-korean`, `kresnik/wav2vec2-large-xlsr-korean`, `w11wo/wav2vec2-xls-r-300m-korean` | 이름과 카드가 한국어 음성 인식용 wav2vec 계열임을 직접 보인다. |
| 2점 | `openai/whisper-small` | 공식 다국어 Whisper small이며 한국어를 지원한다. |
| 1점 | `handy-computer/whisper-small-gguf`, `unsloth/whisper-small` | Whisper small의 배포 형식·재배포 변형이다. |
| **예외 → 1점 권고** | `slplab/wav2vec2-xls-r-300m_phone-mfa_korean` | ASR 파이프라인은 맞지만 카드의 주 용도가 일반 받아쓰기가 아니라 음소(phoneme)·강제정렬(MFA)이다. |

**검수 결론:** 위 권고대로 `slplab/...phone-mfa...`를 1점으로 두면 된다. 일반 한국어 받아쓰기 모델로도 보겠다면 2점으로 바꾼다.

---

## `mc09` — Opus-MT vs M2M100 / 질문 문구를 먼저 바로잡아야 함

현재 질문은 “한국어가 포함된 **다국어** 번역”이다. 그런데 코퍼스의 원본 Opus-MT는
대부분 `ko-en`, `ko-de`처럼 **언어쌍별 모델**이다. 이를 2점으로 두면 ‘한 모델이 다국어를
모두 지원한다’는 질문과 라벨이 어긋난다.

따라서 아래처럼 질문을 고친 뒤 판정하는 것을 권고한다.

> **권고 질문:** Opus-MT와 M2M100 중 한국어↔다른 언어 번역에는 어떤 계열이 더 적합해?

| 판정 | 묶음 | 이유 |
|---:|---|---|
| 2점 (질문 수정 후) | `Helsinki-NLP/opus-mt-ko-de`, `...-ko-en`, `...-ko-es`, `...-ko-fr`, `...-ko-ru`, `...-tc-big-en-ko`, `...-tc-big-ko-en`, `...-tiny_kor-eng` | 원본 Helsinki Opus-MT의 한국어 방향 언어쌍 모델이다. |
| 1점 | `jhk/opus-mt-tc-big-wiki-en-ko`, `shun89/opus-mt-ko-zh` | 제3자 재학습·좁은 언어쌍 변형이다. |
| 1점 | `R4kSo1997/opus-mt-en-ko-onnx-int8`, `Xenova/opus-mt-ko-en`, `noticemkjung/...-ONNX`, `ooeoeo/...-ct2-float16` | 형식 변환·양자화·재배포본이다. |
| 1점 | `Rohith04/ct2fast_m2m100_418M`, `entai2965/m2m100-1.2B-ctranslate2`, `entai2965/m2m100-418M-ctranslate2`, `huggingworld/m2m100_418M` | M2M100의 형식 변환·재배포본이다. 동결 코퍼스에는 원본 M2M100이 없다. |

**결정할 것 한 가지:** 위 권고 문구로 바꾸면 언어쌍 Opus-MT가 2점이 된다. 문구를 유지한다면
Opus-MT 원본도 1점으로 내려야 하므로, 이 문항은 비교 질문으로서 약해진다.

---

## `mc10` — KoELECTRA vs mDeBERTa / 한국어 QA

> KoELECTRA와 mDeBERTa 중에 한국어 질의응답에 뭐가 나아?

| 판정 | 묶음 | 이유 |
|---:|---|---|
| **2점 권고** | `monologg/koelectra-base-v3-finetuned-korquad`, `monologg/koelectra-small-v2-distilled-korquad-384` | 둘 다 KoELECTRA에 KORQUAD 질의응답을 직접 학습한 체크포인트다. `finetuned`·`distilled`라는 이름만으로 1점 처리하면 안 된다. |
| 1점 | `timpal0l/mdeberta-v3-base-squad2` | QA 모델이고 다국어 기반이지만, 모델 카드의 직접 학습 근거는 영어 SQuAD2다. 한국어 QA 성능은 직접 확인되지 않는다. |

**검수 결론:** 위 권고대로 두 KoELECTRA는 2점, mDeBERTa는 1점으로 기록하면 된다. 두 계열이 모두 답에 남아 비교는 가능하다.

---

## 기록 순서

1. `mc08`의 음소·정렬 모델 등급을 확정한다.
2. `mc09` 질문 문구를 권고안으로 바꿀지 결정한다. 이 결정 전에는 JSON에 기록하지 않는다.
3. `mc10`의 두 KoELECTRA를 2점으로 승인할지 확인한다.
4. 그 뒤 `cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py model_comparison`을 실행한다.

이 검증은 JSON 형식, 동결 코퍼스 존재 여부, 조건 충족, 비교 양쪽 계열 포함 여부를 검사한다.
