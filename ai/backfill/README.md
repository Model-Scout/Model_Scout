# Stage 2 메타데이터 백필

파라미터 수를 모르는 모델이 1,527개(39.4%)였다. 원인을 찾고, 기존 데이터를
건드리지 않는 병행 데이터셋을 만들어 두었다. 확인하고 문제가 없으면 교체한다.

**기존 `ai/data/`는 읽기만 했다. Supabase는 건드리지 않았다.**

---

## 1. 무엇이 문제인가

```
코퍼스 3,872개
  파라미터 수 있음   2,345
  파라미터 수 없음   1,527  (39.4%)
```

연쇄로 VRAM 추정도 그 1,527개가 전부 `null`이었다.

```json
"42ailab/TranslateGemma-27B-GGUF": {
  "weights_only": {"fp16_gib": null, "int8_gib": null, "int4_gib": null}
}
```

사용자가 "8GB VRAM에서 돌아가는 모델"이나 "3B 이하 모델"을 물으면 이 모델들은
하드 필터에서 통째로 탈락한다. 찾을 방법이 없다.

### 어떻게 발견했나

골든셋 v2의 `abstention` 질의(조건에 맞는 모델이 없어야 하는 질의)를 만들다가
"후보 0개"를 만들 수 없었다. `numeric_ok`가 값이 없으면 조건을 통과시키기
때문이다. 왜 값이 없는지 조사하다 나왔다.

---

## 2. 원인

`02_enrich_metadata.extract_parameter_count()`가 한 곳만 본다.

```python
safetensors = safe_get(info, "safetensors", None)
if safetensors is None:
    return None          # 여기서 끝난다
```

`architecture`·`model_type`·`context_length`는 `config.json`에서 뽑는다.

**GGUF 전용 레포에는 두 파일이 다 없다.** 그래서 네 필드가 함께 비었다.
파라미터와 컨텍스트가 둘 다 없는 모델이 1,359개로, 같은 레포들이다.

### 의도적 배제는 아니다

- `git log -L`로 보면 초기 코드가 `getattr(info, "safetensors", None)` 형태였다.
  객체에 무엇이 들어 있는지 파악하지 않고 필요한 것만 꺼내 쓴 구조다.
- `ModelInfo`에 `gguf` 속성이 버젓이 있다. 라이브러리가 막은 것도, 나중에 생긴
  것도 아니다.
- GGUF를 제외하려 한 흔적이 없다. 오히려 `01`/`02`는 파일명 패턴으로
  `artifacts.gguf`를 판정하고 `runtime_compatibility.llama_cpp`의 근거로 쓴다.

**원칙 위반이 아니라 수집 범위의 공백이다.**

---

## 3. 문제의 크기 — 1,527개를 셋으로 나눴다

`canonical_model_id`로 "이 모델의 원본은 무엇인가"를 추적했다.

| | 수 | 뜻 |
|---|---:|---|
원본이 코퍼스에 **있음** | 605 | 중복. 그중 567은 원본에 파라미터가 있다 |
원본이 코퍼스에 **없음** | 701 | 이 레포가 유일한 접근 경로 |
변종이 아님 | 221 | GGUF는 81개뿐. `mGPT`처럼 safetensors가 없는 옛 레포 |

**605개는 고칠 필요가 없다.** `05_validate_retrieval.dedupe_canonical`이 같은
원본의 변종을 하나만 남기므로, 원본이 대신 답한다. 설계대로 동작하는 중이다.

**실제로 고쳐야 할 것은 960개(701 + 221 + 원본도 비어 있는 38)다.**
처음에 1,527개 전부를 손실로 본 것은 과장이었다.

---

## 4. 어떻게 고쳤나 — 추측하지 않는다

Hugging Face API가 GGUF 레포에 `gguf` 키를 돌려준다.

```json
"gguf": {"total": 27009346304, "architecture": "gemma3", "context_length": 131072}
```

HF가 GGUF 파일 헤더를 파싱한 값이다. 지금 쓰고 있는 `safetensors.parameters`와
같은 등급의 1차 출처다.

### 쓰지 않은 것

**모델명에서 숫자를 긁는 방법은 쓰지 않았다.** 72%가 이름에 크기를 적어두지만
틀린다.

```
AaryanK/Mistral-Small-4-119B-2603-GGUF   정규식은 4B를 잡는다. 실제는 119B
LFM2.5-24B-A2B-Abliterated-GGUF          24B? A2B? MoE라 둘 다 의미가 있다
```

`delta.jsonl`의 `confidence`에 `low`는 0건이다.

---

## 5. 검증 — "1차 출처다"로 끝내지 않았다

변환본의 `gguf.total`을 코퍼스에 있는 원본의 파라미터 수와 대조했다. 양자화해도
파라미터 수는 변하지 않으므로 같아야 한다.

```
비교 가능한 쌍      510
일치 (5% 이내)     427  (83.7%)
불일치              83  (16.3%)
```

불일치는 무작위가 아니라 패턴이 있었다.

```
LFM3-VL-2B-GGUF      gguf 1.73B  원본 1.92B   ← VL. 비전 인코더가 빠짐
LFM2.5-VL-3B-GGUF    gguf 2.70B  원본 3.12B   ← 같은 이유
A.X-K2-VQ-GGUF       gguf 14.1B  원본 691.7B  ← MoE 또는 부분 양자화
```

GGUF는 비전 인코더를 `mmproj` 파일로 분리한다. 그래서 VL 모델의 `gguf.total`은
언어 모델 부분만 센다.

### 네 가지로 검증하고 신뢰도를 조정했다

| 검사 | 수 |
|---|---:|
검증 대상 | 1,278 |
✅ 원본 파라미터와 5% 이내 일치 | 427 |
⚠️ 원본과 불일치 | 83 |
⚠️ `mmproj` 있음 (VL) | 238 |
⚠️ MoE 신호 | 120 |
└ 파일 크기로 전체 파라미터 확인됨 | 88 |
⚠️ 파일 크기 불일치 | 27 |

| 최종 신뢰도 | 수 | 비율 |
|---|---:|---:|
**high** — 검증 통과 | 966 | 75.6% |
**medium** — 사람 확인 필요 | 312 | 24.4% |

**값을 지어내지 않고 등급만 내렸다.** medium은 `delta.jsonl`에
`validation_notes`로 이유가 적혀 있다.

### 센티넬 값 걸러내기

`QuantFactory/aya-23-8B-GGUF`의 `gguf.context_length`가 `4294967295`
(= 2³²−1)로 왔다. 실제 Aya-23-8B는 8K다. GGUF 헤더의 센티넬이 그대로 넘어온
것이다. 범위를 벗어난 값은 "모름"으로 두는 편이 틀린 값을 넣는 것보다 낫다.

```python
SENTINELS = {0, -1, 2**16-1, 2**31-1, 2**32-1, 2**63-1}
CONTEXT_RANGE = (128, 16_777_216)
PARAM_RANGE = (1_000_000, 2_000_000_000_000)
```

지금은 1건뿐이지만 재발을 막기 위해 코드에 넣었다.

MoE는 파일 크기로 풀었다. 24B-A2B 모델의 IQ4 파일이 12.9 GiB였고, 24B 기준과
맞았다. `gguf.total`이 전체 파라미터를 센다는 뜻이다(VRAM 판단에 맞는 값).

---

## 6. 결과

### 커버리지

| 필드 | 전 | 후 | 증가 |
|---|---:|---:|---:|
`parameter_count` | 60.6% | **93.6%** | +1,278 |
`context_length` | 62.3% | **92.1%** | +1,153 |
`architectures` | 63.2% | **95.7%** | +1,259 |
`model.type` | 64.7% | **96.1%** | +1,217 |
**VRAM 추정** | 55.3% | **88.3%** | +1,278 |
`disk_size_gib` (신규) | 0% | 40.8% | +1,579 |

### 안전성

**기존 값 덮어쓰기 0건.** 빈칸만 채웠다. `compare.py`가 자동 검사한다.

### 실제 검색 결과 변화

골든셋 v2 질의 70개를 양쪽 코퍼스에 돌렸다. 하드 필터와 어휘 점수는
`05_validate_retrieval`의 함수를 그대로 썼다.

| | |
|---|---|
eligible 합계 | **3,973 → 4,762** (+789) |
바뀐 질의 | **33개** / 60 |
상위 10위 신규 진입 | **69건**, 서로 다른 모델 **25개** |

```
cstr/internvl2-1b-crispembed-GGUF              5개 질의에서 새로 상위권
FadedRedStar/LFM2.5-VL-450M-heretic-GGUF       5
Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF           5
neureps/warmly-qwen35-08b-enko-gguf            5
localdeel/ko-hand-ocr-vl-GGUF                  4
```

백필 전에는 파라미터·컨텍스트가 `null`이라 하드 필터에서 탈락했던 모델들이다.

### 골든셋 영향

**abstention 10개 전부 후보 0개를 유지한다.** 재작성이 필요 없다.

---

## 7. ⚠️ 해결하지 못한 것

### 라이선스는 전혀 나아지지 않았다

```
license 없는 모델 277개
  HF cardData에도 license 있음   0개   ← 복구 가능한 것이 하나도 없다
```

그리고 더 큰 문제가 따로 있다.

| "상업 이용 가능한가" 판정 | 수 | 비율 |
|---|---:|---:|
`commercial` | 2,231 | 57.6% |
`conditional` | 1,104 | 28.5% |
`unknown` | 277 | 7.2% |
`non_commercial` | 260 | 6.7% |

**1,381개(35.7%)는 여전히 알 수 없다.** `conditional`의 대부분은 라이선스
이름이 `"other"`라 아무 정보가 없다.

API로는 안 된다. 레포마다 LICENSE 파일을 받아 읽어야 한다. **별건으로 분리한다.**

### medium 312건

사람이 확인해야 한다. VL 모델의 `gguf.total`은 언어부만 세므로 전체보다 작다.

---

## 8. 별건 — 중복 변종의 처리 비용

605개는 검색에서 `dedupe_canonical`로 버려지는데, 수집 단계에서는 풀코스를
거친다. Stage 3 LLM 추출과 Stage 4 임베딩 비용이 결과적으로 버려진다.

**수집 정책 변경이라 이번 범위 밖이다. 보고만 한다.** 섣불리 지우면 안 되는
이유도 있다. `dedupe_canonical`은 먼저 나온 것을 남기므로, 점수가 높은 쪽이
변종이면 변종이 답이 된다. 양자화 버전이 필요한 사용자에겐 변종이 정답이다.

---

## 9. 무엇을 바꿨고 무엇을 안 바꿨나

### 바꾼 것 — `ai/backfill/out/` 안에서만

```
model.parameter_count / parameter_count_billion
model.context_length (+ context_evidence 에 출처 추가)
model.architectures / model.type
model.metadata_status.{parameter_count,context_length}
hardware.weights_only.*
model.disk_size_gib          ★ 새 필드 (별도 제안)
```

### 안 바꾼 것

- **`ai/data/`** — 읽기만 했다
- **Supabase** — 건드리지 않았다. 검증에 쓰는 도구가 전부 로컬 파일을 읽는다
- **`stage2_version`** — 올리지 않았다. 올리면 `08_sync_supabase`의 정합성
  검증과 Stage 3 재실행 판정에 걸린다. 교체 시점에 팀이 결정할 일이다
- **Stage 3** — 기존 출력을 승계했다. 입력인 README가 바뀌지 않아 claim도 같다.
  LLM 호출이 없었으므로 비용도 없다
- **공유 BGE 인덱스** — `ai/backfill/index/`에 따로 만들었다

### 비용

```
HF API 조회 1,817개          무료 (16분)
Stage 3                      재실행 안 함
Stage 4 재임베딩 1,321개      $0.018  (text-embedding-3-small)
BGE 인덱스 1,309개            로컬 CPU 35분
```

---

## 10. 재현 방법

```bash
cd ai
../.venv/bin/python backfill/fetch_hf.py                 # HF API 조회 (16분)
../.venv/bin/python backfill/build_delta.py              # 델타 생성
../.venv/bin/python backfill/validate_delta.py           # 검증 + 신뢰도 조정
../.venv/bin/python backfill/apply_stage2.py             # Stage 2 패치
../.venv/bin/python backfill/compare.py                  # 커버리지·안전성
../.venv/bin/python backfill/rebuild_stage4.py --estimate # 비용 확인
../.venv/bin/python backfill/rebuild_stage4.py --apply    # Stage 4 재임베딩
../.venv/bin/python backfill/compare_search.py           # 검색 결과 비교
```

## 11. 파일

```
ai/backfill/
├── README.md                  이 문서
├── delta.jsonl                ★ 1,724건. 모델별 before/after/source/confidence
├── fetch_hf.py                HF API 조회
├── build_delta.py             무엇을 어떤 근거로 채울지 결정
├── validate_delta.py          원본 대조·mmproj·MoE·파일 크기로 검증
├── apply_stage2.py            Stage 2 패치
├── rebuild_stage4.py          Stage 4 재임베딩
├── build_index.py             백필용 BGE 인덱스
├── compare.py                 커버리지·안전성 비교
├── compare_search.py          검색 결과 비교
├── raw/                       HF 원본 응답 (gitignore, 재생성 가능)
├── out/                       백필 Stage 2/4 (gitignore, 재생성 가능)
├── index/                     백필 BGE 인덱스 (gitignore)
└── reports/
    ├── validation.md          ★ 신뢰도 조정 근거
    ├── comparison.md          ★ 커버리지·안전성
    ├── search_comparison.md   ★ 검색 결과 변화
    ├── delta_summary.md
    └── apply_summary.json
```

---

## 12. 확인이 필요한 것

1. **`gguf.total`을 1차 출처로 인정할 것인가.** `safetensors.parameters`와 같은
   등급으로 본 판단이 맞는지. 검증 결과 83.7%가 원본과 일치했고, 불일치는
   VL·MoE로 설명된다.
2. **medium 312건을 어떻게 할 것인가.** 제외하고 high 966건만 적용할 수도 있다.
3. **`disk_size_gib` 새 필드를 받을 것인가.** "내 GPU에 들어가나"는 파라미터
   추정보다 실제 파일 크기가 정확하다. 기존 필드 채우기와 분리해 심사할 수 있게
   따로 기록해 두었다.
4. **교체 방식.** `02_enrich_metadata.py`를 고쳐 정식 재실행할 것인지, 이
   백필 결과를 그대로 반영할 것인지. 전자가 깔끔하지만 Stage 2 버전이 올라가
   Stage 3 재실행(LLM 비용)을 유발한다.
5. **`huggingface_hub` 버전.** `requirements.txt`는 `0.36.2`로 고정인데 실제
   설치본은 `1.33.0`이었다. 이 백필은 REST API를 직접 호출해 라이브러리 버전에
   의존하지 않지만, 파이프라인을 고칠 때는 확인이 필요하다.
