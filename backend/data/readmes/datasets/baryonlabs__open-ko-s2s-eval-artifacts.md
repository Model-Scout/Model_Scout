---
license: cc-by-4.0
language:
  - ko
task_categories:
  - automatic-speech-recognition
tags:
  - korean
  - asr
  - evaluation
  - benchmark
  - audit
  - leaderboard
pretty_name: Open Ko-S2S Eval Artifacts
configs:
  - config_name: index
    data_files: index.csv
---

# Open Ko-S2S 평가 산출물 (감사용)

## ⚠️ KsponSpeech 참조 전사는 해시로 대체돼 있습니다

KsponSpeech 는 AI Hub 배포 데이터로 재배포 제한이 있을 수 있어, **kspon 런의
`ref` 컬럼을 `ref_sha256` 으로 대체**했습니다(전사 원문 미포함). 모델 출력(`hyp`)과
채점 결과(`cer_err`/`cer_len`/`cer`)는 우리 산출물이라 그대로 공개합니다.

Zeroth 런은 원본이 CC BY 4.0([OpenSLR #40](https://www.openslr.org/40/))이라
`ref` 원문을 그대로 담고 있습니다.

### 라이선스 보유자의 검증 절차

AI Hub 에서 KsponSpeech 를 정당하게 받은 분은 다음으로 우리 수치를 검증할 수 있습니다.

1. 리더보드 저장소의 `eval/datasets_ko.py` 에서 `clean_kspon()` 을 가져옵니다.
2. 자기 사본의 원 전사에 `clean_kspon()` 을 적용합니다. 결과가 목록이면
   `" | ".join(...)` 으로 잇습니다(우리가 CSV 에 기록한 형태와 동일).
3. `hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]` 로 해시해
   `ref_sha256` 과 대조합니다 — 같으면 우리가 채점에 쓴 참조가 원본과 동일합니다.
4. 그 참조와 CSV 의 `hyp` 로 CER 을 다시 계산해 `summary.json`·리더보드 값과
   비교합니다. 채점식은 `eval/metrics.py` 의 `cer()` 입니다.

```python
import hashlib
from eval.datasets_ko import clean_kspon

ref = clean_kspon(my_raw_transcript)          # 라이선스 보유자의 사본
s = " | ".join(ref) if isinstance(ref, list) else ref
assert hashlib.sha256(s.encode()).hexdigest()[:16] == row["ref_sha256"]
```


Open Ko-S2S 리더보드에 게시된 CER/WER 수치의 **원본 측정 산출물**입니다.
리더보드는 "산출물(감사 가능) — 점수의 출처를 추적할 수 있다"고 밝혀 왔지만,
실제 산출물은 비공개 빌드 서버에만 있어 아무도 검증할 수 없었습니다.
이 데이터셋은 그 산출물을 그대로 공개해, **누구나 게시된 숫자를 직접 다시 계산**할 수 있게 합니다.

측정 환경: RTX 4090 · DureClaw 하네스. 오디오는 포함하지 않으며, 전사 텍스트와 채점 결과만 담습니다.

---

## 1. 무엇이 들어 있나

```
index.json              전체 런 색인 + 감사 결과(기계 판독용, 권장)
index.csv               같은 내용의 평면 표
verify_cer.py           CSV에서 CER/WER을 독립 재계산하는 스크립트
runs/run_<run-id>/
    summary.json        그 런의 모델·데이터셋·n·CER·WER·RTF
    transcripts__<모델>.csv   per-sample 채점 원장 (핵심 감사 자료)
    run.log             하네스 실행 로그
```

- 런 디렉터리 **41개**, per-sample CSV **33개**, 총 약 3.3 MB
- 데이터셋 축: `zeroth`(Zeroth-Korean, 낭독체) / `kspon`(KsponSpeech, 자유발화) / `tts-roundtrip`(TTS 발음 왕복)
- 정식 측정은 모두 **n=457**, 스모크 테스트는 n=5 (아래 3장 참조)

### transcripts CSV 열

| 열 | 뜻 |
|---|---|
| `idx` | 샘플 순번 |
| `ref` | 정답 전사. kspon은 허용 표기가 여러 개일 수 있고 ` \| ` 로 이어 붙어 있음 |
| `hyp` | 모델이 낸 인식 결과 (원문 그대로, 정규화 전) |
| `cer_err` | 이 샘플의 **문자 오류 수** (표기 변형 보정 때문에 실수일 수 있음) |
| `cer_len` | 이 샘플의 **정준 분모** = 정규화된 첫 표기의 글자 수 |
| `cer` | `cer_err / cer_len` (참고용 반올림값 — **합산에 쓰지 말 것**) |
| `proc_s` | 이 샘플 처리에 걸린 초 |

---

## 2. 게시된 CER을 검증하는 법

### 핵심 규칙

**코퍼스 CER = `cer_err` 열의 합 ÷ `cer_len` 열의 합**

샘플별 `cer` 값을 평균 내면 **틀립니다**. 짧은 문장이 과대 대표되기 때문입니다.
반드시 오류와 분모를 각각 누적한 뒤 나눠야 리더보드 숫자와 일치합니다.

### CER의 정의

여기서 CER은 **공백 제거 문자 오류율(space-free CER)** 입니다. 정규화 순서는 다음과 같습니다.

1. 유니코드 **NFC** 정규화 (자모 결합)
2. **소문자화** (라틴 문자)
3. **문장부호 제거** — `!"#$%&'()*+,-./:;<=>?@[]^_\`{|}~…·“”‘’「」『』〈〉《》、。，．！？～`
4. 공백 정리 후 **공백 전부 제거** (CER 한정. WER은 공백을 남기고 어절 단위로 셈)

거리는 Levenshtein 편집거리이며 치환·삽입·삭제 비용이 모두 1입니다.

### kspon의 이중 전사와 "정준 분모"

KsponSpeech는 전사의 약 8.5%를 `(철자)/(발음)` 이중 전사로 제공합니다
(예: `3D로` / `쓰리 디로`). 하나만 정답으로 고르면 그 표기를 쓰는 모델이 부당하게 유리해지므로,
**허용 표기를 모두 정답으로 인정**합니다. 이 CSV에서는 ` | ` 로 이어 붙어 있습니다.

다만 분모는 고정합니다. 채점 규칙은:

> 표기 후보들 중 **오류율이 가장 낮은 값**을 고르고,
> 그 비율을 **첫 표기(참조 원문)의 길이**에 되돌려 곱한다.

분모를 "선택된 표기의 길이"로 두면 코퍼스 분모가 모델 출력에 따라 흔들려서,
같은 정확도의 두 모델이 다른 점수를 받고, 심지어 **더 긴 오답이 더 좋은 점수를 받는**
역전이 실제로 발생합니다. 그래서 분모를 모델과 무관하게 고정했습니다.
`cer_len` 열이 바로 이 정준 분모이고, `cer_err`가 실수인 행은 이 보정이 적용된 행입니다.

zeroth는 표기 변형이 없으므로(` | ` 없음) 이 보정이 아무 영향을 주지 않습니다.

### 재계산 스크립트

```bash
python verify_cer.py runs/run_fix-kspon-fw_large-v3-turbo/transcripts__faster-whisper-large-v3-turbo.csv
```

이 스크립트는 `cer_err` 열을 **믿지 않고**, `ref`/`hyp` 원문에서 정규화와 편집거리를
처음부터 다시 계산합니다. 즉 채점 코드 자체를 독립적으로 검증합니다.

---

## 3. 실제 예시 — faster-whisper-large-v3-turbo (kspon) 다시 계산해 보기

리더보드 게시값: `asr_cer_spontaneous = 0.1253` (12.53%)
산출물: `runs/run_fix-kspon-fw_large-v3-turbo/transcripts__faster-whisper-large-v3-turbo.csv`

```python
import csv

rows = list(csv.DictReader(
    open("runs/run_fix-kspon-fw_large-v3-turbo/transcripts__faster-whisper-large-v3-turbo.csv",
         encoding="utf-8")))

err = sum(float(r["cer_err"]) for r in rows)
den = sum(float(r["cer_len"]) for r in rows)

print(len(rows), err, den, err / den)
# 457 1376.0 10979.0 0.12533016668184716
```

```
n              = 457
sum(cer_err)   = 1376.0
sum(cer_len)   = 10979
CER            = 1376.0 / 10979 = 0.125330…  →  반올림 0.1253  ✅ 게시값과 일치
```

첫 행을 손으로 따라가 보면:

```
ref = "그니까 착한데 막 그런 거 있어 그 둘이 보띠오를 가잖아. 종훈이하고 …"
hyp = "그니까 착한데 막 그런 거 있어 그 둘이 봇 듀오를 가잖아 종훈이하고 …"
cer_err = 8.0 , cer_len = 83  →  cer = 0.0964
```

`ref`에 ` | ` 가 없으므로 표기 변형이 없는 행이고, 문장부호를 지우고 공백을 없앤 뒤
편집거리를 재면 정확히 8이 나옵니다. 분모 83은 정규화된 `ref`의 글자 수입니다.

같은 방식으로 확인되는 다른 예:

| 런 | 모델 | 데이터셋 | sum(cer_err) | sum(cer_len) | 재계산 CER | 게시값 |
|---|---|---|---|---|---|---|
| `run_nemo-457` | nemotron-3.5-asr-streaming-0.6b | zeroth | 1056.0 | 19288 | 0.054749 | **0.0547** ✅ |
| `run_w2v-zeroth-w2v_kresnik_…` | wav2vec2-large-xlsr-korean | zeroth | 360.0 | 19288 | 0.018664 | **0.0187** ✅ |
| `run_fix-kspon-fw_large-v3-turbo` | faster-whisper-large-v3-turbo | kspon | 1376.0 | 10979 | 0.125330 | **0.1253** ✅ |

---

## 4. 검증 결과 요약

`index.json` 의 `runs[]` 각 항목에 다음이 들어 있습니다.

- `recomputed_cer` — `ref`/`hyp` 원문에서 처음부터 다시 계산한 코퍼스 CER
- `recompute_matches_summary` — `summary.json` 값과 일치하는지
- `published_cer` / `is_published_number` — 리더보드 `data/results.json` 에 실제로 실린 숫자인지
- `scoring_regime` — `canonical`(수정 후) / `legacy`(수정 전). 3장 및 5장 참조

| 항목 | 수 |
|---|---|
| 런 디렉터리 | 41 |
| per-sample CSV가 있는 런 | 33 |
| 스모크 런 (n=5) | 6 |
| 게시 숫자를 뒷받침하는 런 | 15 |
| 그중 CSV에서 완전 재현된 것 | **13** |
| 고아 런 (산출물은 있는데 게시 안 됨) | 7 |
| 고아 게시값 (숫자는 있는데 산출물 없음) | 23 |
| 실패 런 (결과 0건) | 2 |
| 점수는 있으나 per-sample CSV가 없는 런 | 3 |

**13개 게시 CER이 CSV에서 소수 넷째 자리까지 정확히 재현**되었습니다.
불일치로 판정된 게시 숫자는 없습니다.

---

## 5. 알려진 주의사항 (반드시 읽을 것)

### (1) 스모크 런이 섞여 있습니다 — 라벨로 구분하세요

`run_smoke-*` 6개는 n=5짜리 파이프라인 점검용이며 **성능 수치가 아닙니다**.
예를 들어 `run_smoke-nemo` 의 CER 0.2621은 같은 모델의 정식 n=457 값 0.0547과
완전히 다릅니다. `index.json` 의 `is_smoke: true` 로 걸러내세요.

### (2) 일부 kspon 런은 채점 수정 이전 것입니다

kspon 이중 전사 채점에는 두 세대가 있습니다.

- **`legacy` (수정 전)** — 표기 후보 중 **절대 편집거리**가 가장 작은 것을 고르고,
  그 후보 **자신의 길이**를 분모로 씀. 분모가 모델 출력에 따라 흔들림.
- **`canonical` (수정 후)** — 표기 후보 중 **오류율**이 가장 낮은 것을 고르고,
  분모는 항상 첫 표기 길이로 고정. 현재 규칙.

`run_kspon-*`, `run_cat-*`, `run_w2v-kspon-*` 은 `legacy`, `run_fix-kspon-*` 은 `canonical` 입니다.
같은 모델·같은 데이터셋의 런이 두 벌 있는 것은 이 재채점 때문이며, 중복 측정이 아닙니다.

차이는 작지만 0이 아닙니다. 예를 들어 whisper-base-Ko(kspon)는
legacy 0.6384 → canonical 0.6385, nemotron(kspon)은 legacy 0.1807 → canonical 0.1806 입니다.
**리더보드에 실린 값은 `canonical` 쪽**입니다.
zeroth 런은 표기 변형이 없어 두 방식이 완전히 동일합니다.

각 CSV가 어느 세대인지는 `index.json` 의 `scoring_regime` 에 판정해 두었고,
`cer_canonical_scoring` / `cer_legacy_scoring` 에 두 방식의 값을 모두 넣어 두었으므로
직접 비교할 수 있습니다.

### (3) Raon-Speech-9B 는 per-sample CSV가 없습니다 — 감사 불가

`run_raon-457`, `run_kspon-raon`, `run_fix-kspon-raon`, `run_smoke-raon` 4개 런은
다른 코드 경로로 실행되어 `summary.json` 만 있고 `transcripts__*.csv` 가 **없습니다**.
게시된 Raon-Speech-9B 의 CER(zeroth 0.0383 / kspon 0.0796)은 `summary.json` 값과는
일치하지만, **샘플 단위로 재계산할 방법이 없습니다.** 다른 모델과 같은 수준의
근거를 갖췄다고 볼 수 없습니다.

### (4) 게시 숫자의 다수는 아직 산출물이 없습니다

리더보드 `data/results.json` 의 ASR 숫자 36개 중 **23개는 이 데이터셋에 대응 산출물이 없습니다.**
대부분 이전 `DureClaw·daily-*` 세대 측정(faster-whisper 계열 전체, whisper 파생 모델들,
Qwen2.5-Omni 등)으로, 당시에는 per-sample CSV를 남기지 않았습니다.
전체 목록은 `index.json` 의 `audit_findings.orphan_published_numbers` 에 있습니다.
**즉 지금 시점에서 리더보드 ASR 수치의 일부만 감사 가능합니다.**

### (5) 반올림 경계

`summary.json` 의 CER은 소수 넷째 자리 반올림값입니다.
whisper-small-komixv2(kspon)는 재계산값이 정확히 `0.07445` 로 반올림 경계에 걸려,
반올림 규칙에 따라 0.0744 또는 0.0745가 될 수 있습니다. 게시값은 0.0744 입니다.
비교할 때는 1e-4 수준의 허용오차를 두세요.

### (6) 라이선스와 출처

- **Zeroth-Korean** — CC BY 4.0.
- **KsponSpeech** — AI Hub 제공 한국어 자유발화 코퍼스. 이 데이터셋에는 평가에 쓰인
  **457개 발화의 전사 텍스트만** 들어 있으며 **오디오는 포함하지 않습니다.**
  KsponSpeech 원본을 쓰려면 AI Hub 이용약관에 따라 직접 내려받아야 합니다.
- 이 저장소의 색인·문서·스크립트는 CC BY 4.0 으로 제공합니다.
- `hyp` 열은 각 모델의 원본 출력이며, 일부 모델은 깨진 문자나 무관한 언어를 출력합니다
  (예: ARK-ASR 계열의 CER > 1.0). 이는 측정 오류가 아니라 실제 모델 동작입니다.

---

## 6. 고아 항목 (감사 결과)

### 산출물은 있는데 리더보드에 없는 모델 (고아 런)

n=457 정식 측정이 존재하지만 `data/results.json` 에 아예 없는 모델들입니다.

| 모델 | zeroth CER | kspon CER |
|---|---|---|
| `SeloWhisper-ko-disfluency` | 0.0661 | 0.0704 |
| `ARK-ASR-0.6B` | 1.0163 | 1.3804 |
| `ARK-ASR-3B` | 1.3776 | 1.8023 |

`SeloWhisper-ko-disfluency` 는 두 데이터셋 모두에서 현재 게시된 대부분의 모델보다
좋은 점수인데도 리더보드에 올라 있지 않습니다.
ARK 계열 두 모델은 CER이 1.0을 넘어 사실상 인식 실패 상태입니다.

### 결과가 하나도 없는 실패 런

`run_cat-zeroth-nemo_vertox-ai_…`, `run_cat-kspon-nemo_vertox-ai_…` 2개는
모델 로딩 실패(`config.json` 파싱 오류)로 결과를 내지 못했습니다.
비교용으로 로그와 함께 남겨 둡니다.

---

## 7. 인용

```bibtex
@misc{openkos2s_eval_artifacts,
  title  = {Open Ko-S2S Eval Artifacts},
  author = {Baryon Labs},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/datasets/baryonlabs/open-ko-s2s-eval-artifacts}}
}
```
