# 골든셋 v3

> **현재 상태: 골든셋 초안 + 전수 스캔 + 검수 준비 완료.**
> 아래의 2점·1점은 Claude 가 규칙으로 *제안*한 것이고, 사람이 확정하기 전에는 정답이 아니다.

최신 재적재(sync run `cb1b5e48-11dd-4018-bf6b-d48b8a76054b`)의 active 모델 4,017개를 기준으로,
실제 사용자가 물을 법한 질문 70개(7유형 × 10)의 **완전한** 정답 집합을 만들기 위한 도구와 초안이다.
기존 `../v2/`(3,872행 스냅샷)와 섞지 않는다. v2 의 숫자·후보·판정은 하나도 가져오지 않았고,
개념(전수 스캔, conditions_fidelity, 2·1점 등급)만 이어받아 최신 코퍼스에서 다시 계산했다.

## 용어

| 용어 | 뜻 |
|---|---|
| **Corpus** | 골든셋 판정 기준이 되는 최신 active 모델 전체(4,017개). `corpus_snapshot.meta.json` 에 고정했다 |
| **Hard filter** | 파라미터·컨텍스트·task·라이선스·commercial_status·gated·파일 형식처럼 기계가 판정할 수 있는 명시 조건 |
| **Eligible** | 질문의 모든 hard filter 를 통과한 모델 집합 |
| **Conditions fidelity** | 질문 conditions 의 각 조건이 질문 문장의 어느 표현에서 나왔는지 적은 표 |
| **Relevance rule** | eligible 모델을 2점·1점·정답 아님으로 나누는 사전 정의. 판정 *전에* 적는다 |

항상 **정답 ⊆ eligible ⊆ corpus** 가 성립한다. 조건 밖의 모델은 정의상 정답이 될 수 없기 때문이다.
단, 사용자가 말하지 않은 조건이 conditions 에 끼어들면 이 관계가 깨진다. 그래서 verifier 가 모든
조건에 대해 "질문 속 근거 표현이 실제로 질문에 있는가", "수치 조건이면 그 숫자가 질문에 있는가"를 검사한다.
"노트북에서 돌리고 싶다", "긴 문서" 같은 말은 숫자 조건으로 바꾸지 않았다.

### 점수

| 점수 | 뜻 | 저장 |
|---:|---|---|
| **2** | 모든 필수 조건이 확인됐고, 요구한 용도·능력이 명시적 근거로 정확히 일치 | `expected_any` |
| **1** | 필수 조건은 충족하지만 다국어·범용 모델이거나, 요구 능력이 부가 기능이거나, 원본의 변환·양자화·재업로드 | `acceptable` |
| 0 | 정답 아님 | **저장하지 않는다** |

0점 목록 대신 eligible 전체가 어떤 이유로 2점·1점·자동 제외됐는지 기록하고, verifier 가 다시 계산해서 증명한다.

### unknown 처리

숫자 제한·상업 이용·gated 처럼 필수 조건의 값이 unknown 이면 조건 충족을 증명할 수 없으므로 eligible 에서 뺀다.
unknown 을 false 나 permitted 로 취급하지 않는다. 운영 SQL(`match_model_scout_models`)의 WHERE 절과 같은 규칙이고,
`tools/corpus.py` 가 그 WHERE 절을 그대로 옮겼다. 05 의 `hard_filter` 와는 tasks 가 빈 경우와 최소 파라미터 처리가
달라 재사용하지 않았고, 겹치는 범위에서 결과가 같은지 테스트로 확인한다. `licenses` 조건만 운영 RPC 에 없는 판정용 조건이다.

### "근거 없음"의 의미

자동 제외 이유 "요구 능력을 뒷받침하는 저장된 근거 없음"은 그 모델이 실제로 그 능력이 없다는 뜻이 아니다.
**현재 Model Scout 데이터(모델명·메타데이터·의미 claim·벤치마크·README span)로 정답임을 증명할 수 없다**는 뜻이다.
골든셋의 범위는 이 원칙으로 고정한다.

## 왜 검색 Top-K 를 정답 후보에 쓰지 않나

검색기가 찾은 모델로 후보를 만들면, 그 검색기가 못 찾은 정답은 영원히 라벨이 없다. 그러면 그 검색기는 과대평가되고,
다른 방식(dense, RRF 등)이 찾은 진짜 정답은 오답으로 채점된다. 그래서 v3 는 BM25·dense·RRF·운영 검색 결과를 전혀 쓰지 않는다.
hard filter 로 eligible 을 만든 뒤 **eligible 전부**를 아래 순서로 스캔한다.

```
1 model_id → 2 canonical_model_id → 3 filter_metadata → 4 technical_metadata
→ 5 semantic_metadata → 6 benchmark_metadata → 7 source_provenance → 8 evidence(README span)
```

각 eligible 모델은 반드시 하나로 분류된다. `eligible_count = 2점 제안 + 1점 제안 + 자동 제외 + 사람 판단` 이 깨지면 실패한다.

| 분류 | 언제 |
|---|---|
| `proposed_grade_2` | 요구 능력이 모델명·원본명·의미 claim(1·2·5단계)에 명시돼 있고 2점 조건을 만족 |
| `proposed_grade_1` | 능력은 확인되지만 다국어·범용·부가 기능·변환본이거나, 근거가 메타데이터에만 있음 |
| `unresolved_for_human` | 근거가 README 원문(8단계)에만 있어 사람이 읽어야 함. **조용히 0점 처리하지 않는다** |
| `auto_rejected` | 기계가 확인할 수 있는 이유가 있음(근거 없음, 다른 계열, 다른 dataset·metric, 파인튜닝된 다른 모델 등) |

면책 문장("medical·legal 같은 중요한 용도에는 권장하지 않는다")은 능력 근거로 세지 않는다(매칭 직전 부정 표현 검사).

### Variant 처리

- 포맷을 요구한 질문(GGUF·ONNX 조건)이면 해당 변환본도 2점이 될 수 있다.
- 포맷을 요구하지 않았다면 원본은 2점, 같은 가중치의 변환·양자화·재업로드는 1점으로 제안한다.
- base_model 태그만 같은 **파인튜닝 모델은 변환본이 아니라 다른 모델**이다. 모델명 지목·비교 질문에서는 `variant_mismatch` 로 제외한다.
- 모든 후보에 `canonical_model_id`·`is_variant`·`variant_types`·관계 근거를 기록하고, 최종 라벨에 `family_labels`(family 기준 최고 점수)를 함께 저장해 model_id 기준과 family 기준 평가를 둘 다 할 수 있다.
- model_comparison 은 비교 대상 양쪽 계열에 후보가 각각 하나 이상 있어야 한다.

## 질문 70개

| 유형 | 내용 | 예 |
|---|---|---|
| structured_constraint | 수치·포맷·라이선스 조건이 정답을 정한다 | "Ollama 로 노트북에서 한국어 번역기를 돌려 보려는데, GGUF 파일 크기가 2GB 이하이고 상업적으로도 쓸 수 있는 라이선스 계열이면 좋겠어요." |
| semantic_capability | 용도·능력을 말한다 | "주민센터 민원 신청서처럼 손으로 쓴 한국어 서류를 사진으로 찍어 텍스트로 옮기고 싶어요." |
| semantic_constraint | 용도 + 조건 | "콜센터 통화를 실시간으로 받아 적는 서비스를 상업적으로 운영하려고 해요. … 파라미터 1B 이하 …" |
| lexical_exact | 모델 이름을 지목한다 | "KT 에서 나온 믿음 2.0 Mini 를 써 보라는 얘기를 들었어요." |
| model_comparison | 두 모델·계열 비교 | "NLLB-200 distilled 600M 이랑 M2M100 418M 을 비교하고 싶어요." |
| benchmark_lookup | 같은 dataset·metric 점수만 비교 | "KMMLU 점수가 공개된 한국어 모델들을 … 같은 기준으로 적힌 점수끼리만" |
| abstention | 현실적인 조건인데 교집합만 0개 | "MIT 라이선스이고 파라미터 1B 이하인 GGUF 번역 모델" |

표현 방식은 기술형 27·혼합형 27·목적형 16개다. structured_constraint 에는 목적형이 없다. 이 유형은 수치·포맷 조건을 사용자가
직접 말해야 성립해서, 목적만 말하게 쓰면 조건을 추론해 넣어야 하기 때문이다(`queries.py` 의 `STYLE_QUOTA_EXEMPTIONS`).
분포 전체는 `reports/quality_report.md` 에 있다.

### abstention 은 억지로 만들지 않았다

각 abstention 질문은 다음을 자동 검사한다.

- 조건 하나하나는 코퍼스에서 5개 이상이 만족한다(조건 자체가 비현실적이지 않다).
- 수치 조건이 코퍼스 하위 1%·상위 1% 밖이 아니다. 최소 > 최대 같은 직접 모순이 없다.
- 조건 하나만 빼면 후보가 생긴다(`relaxed_candidate_counts`).
- 조건 하나만 어긋난 near-miss 모델이 있다(`near_miss_models`). 검색기가 그 조건 하나를 무시하면 이 모델을 그럴듯한 오답으로 추천한다.

예: ab01 "MIT + 1B 이하 + GGUF 번역"은 라이선스만 빼면 6개(plamo-3-translate GGUF 등), 크기만 빼면 3개,
GGUF 만 빼면 3개(small100 등)가 생긴다.

## 기준 코퍼스 고정과 복구

`corpus_snapshot.jsonl`(약 143MB)은 커밋하지 않는다. 대신 `corpus_snapshot.meta.json` 에 sync_run_id·행 수·
model_id 집합 SHA256·파일 SHA256·Stage 버전·refreshed_at 범위를 커밋했다.

```bash
cd ai
python test/golden/v3/tools/dump_corpus.py --restore   # 같은 스냅샷 복구(읽기 전용 접속, SHA256 일치해야 성공)
python test/golden/v3/tools/dump_corpus.py --check     # 로컬 스냅샷 검사
```

필요한 환경변수: `SUPABASE_DB_HOST`, `SUPABASE_DB_PORT`, `SUPABASE_DB_NAME`, `SUPABASE_DB_USER`, `SUPABASE_PASSWORD`
(`ai/.env` 또는 저장소 루트 `.env`). DB 의 최신 reingest run 이 메타와 다르면 복구가 실패한다. 그때는 기준 코퍼스가
바뀐 것이므로 골든셋을 다시 만들어야 한다. 스냅샷이 없거나 SHA256 이 다르면 draft·final 검증은 실패한다.

## 실행 순서

```bash
cd ai
python test/golden/v3/tools/build_drafts.py        # 70개 전수 스캔 → drafts/, review/judgments/ (판정은 보존)
python test/golden/v3/tools/verify.py --mode draft # 재계산 대조 + 워크시트 생성
python test/golden/v3/tools/quality_report.py      # 품질 보고서, 질문 검수표
# --- 사람 검수 ---
python test/golden/v3/tools/judge.py --status
python test/golden/v3/tools/judge.py st01 <model_id> --decision approve --reason "…" --by <이름>
python test/golden/v3/tools/finalize.py            # 판정이 다 끝나야 final/ 생성
python test/golden/v3/tools/verify.py --mode final # 미판정·보류·unresolved 가 하나라도 있으면 실패
python test/test_golden_v3.py                      # 도구 단위 테스트(코퍼스 불필요)
```

`verify.py --mode structure-only` 는 스냅샷 없이 질문 구조(70개, 유형별 10개, 중복 ID, persona, 숨은 조건)만 검사한다.

## 사람 검수 순서

1. `review/QUESTION_REVIEW.md` — 질문 70개가 실제 사용자 질문다운지 먼저 본다. 고칠 질문은 `queries.py` 를 고치고 `build_drafts.py` 를 다시 돌린다.
2. `review/SUMMARY.md` — 질의별 eligible·제안·검수 대상 수.
3. `review/worksheets/<유형>.md` — 후보마다 근거와 함께 Claude 제안 점수를 본다. 판정은 `tools/judge.py` 로 기록한다
   (`approve` = 제안 점수 확정, `2`·`1` = 점수 직접 지정, `exclude`, `hold`). README 원문에만 근거가 있는 `unresolved` 후보는 `approve` 할 수 없다.
4. 각 워크시트의 "자동 제외 이유별 수와 감사 표본"으로 제외 규칙이 정답을 잘못 버리지 않았는지 확인한다.
5. abstention 은 질문마다 `judge.py <id> "(abstain)" --decision approve` 로 '정답 없음'을 확인한다.

## 파일

```
v3/
├── README.md                     이 문서
├── queries.py                    질문 70개와 relevance rule (사람이 쓰는 유일한 원본)
├── corpus_snapshot.meta.json     기준 코퍼스 메타 (커밋)
├── corpus_snapshot.jsonl         기준 코퍼스 원문 (gitignore, --restore 로 복구)
├── drafts/<유형>.jsonl           전수 스캔 결과와 제안 (생성물)
├── review/
│   ├── SUMMARY.md                질의별 요약 (생성물)
│   ├── QUESTION_REVIEW.md        질문 검수표 (생성물)
│   ├── worksheets/<유형>.md      후보 검수 워크시트 (생성물)
│   └── judgments/<유형>.jsonl    사람 판정 입력 (judge.py 로 기록, 재생성해도 보존)
├── reports/quality_report.*      질문 품질 보고서 (생성물)
├── final/<유형>.jsonl            최종 골든셋 (사람 판정 후 finalize.py 가 생성)
└── tools/
    ├── corpus.py                 스냅샷 로더·무결성 검사·SQL 과 같은 hard filter
    ├── dump_corpus.py            읽기 전용 덤프·복구
    ├── scan.py                   전수 스캔·분류·near-miss·극단성 검사
    ├── build_drafts.py           초안 생성
    ├── make_worksheet.py         워크시트
    ├── quality_report.py         품질 보고서
    ├── judge.py                  판정 입력
    ├── finalize.py               최종 골든셋 생성
    └── verify.py                 structure-only / draft / final 검증
```

## 한계

- 규칙 스캔은 정규식이다. 근거를 놓칠 수 있으므로 자동 제외 감사 표본과 README-only(`unresolved`) 후보를 사람이 본다.
- `korean_required` 는 현재 코퍼스 전체가 korean_verified=true 라서 걸러내는 효과가 없다. 한국어 전용 여부는 2점·1점 구분에서만 쓴다.
- 벤치마크 dataset 이름은 README 표기를 그대로 저장한 것이라 표기가 다르면 다른 dataset 으로 본다(예: `KMMLU` 와 `kmmlu (chat CoT)`).
- 막연한 질문("한국어 모델 추천해줘")은 정답이 수백 개라 완전성을 보장할 수 없어 넣지 않았다.
