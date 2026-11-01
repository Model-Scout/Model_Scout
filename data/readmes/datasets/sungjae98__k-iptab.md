---
license: other
license_name: aihub-redistribution-permitted
license_link: https://www.aihub.or.kr/
language:
- ko
task_categories:
- text-classification
- text-ranking
tags:
- legal
- patent
- korean
- invalidation
- inventive-step
pretty_name: K-IPTAB
size_categories:
- 1K<n<10K
configs:
- config_name: verdict
  data_files: kiptab_verdict.jsonl
- config_name: chart
  data_files: kiptab_chart.jsonl
- config_name: comb
  data_files: kiptab_comb.jsonl
---

# K-IPTAB: Korean Patent Invalidation Trial Benchmark

한국 특허 무효심판 심결문(KIPO/IPTAB)에서 구축한 3-태스크 벤치마크. PANORAMA(US 특허심사 벤치마크)의 한국·심판판.

| Task | Records | 설명 | answer |
|---|---|---|---|
| **verdict** | 3,664 | 사건단위 무효 vs 생존 예측 | `code` ∈ {INVALID, VALID} |
| **chart** | 1,537 | 구성요소×선행기술 개시행렬(4치) | `matrix` (DISCLOSE/DISCLOSE_SUBST/DIFFERENT/NOT_DISCLOSED) |
| **comb** | 2,236 | 선행기술 역할귀속(채택/배척)+조합 | `roles`, `adopted_combinations` |

3way split(`train`/`val`/`test`), 그룹분할(trial 누수 없음). 모두 **gold tier**(regex-clean 라벨 + 복원 선행기술).

## ⚠️ 사용법 — 입력/정답 분리 (벤치마크 무결성)

각 레코드는 **입력**과 **정답**이 분리돼 있습니다. 모델에는 **`context`만** 넣으세요.

```
{
  "id": "2010100003296",            # KIPRIS 심판번호
  "task": "comb", "split": "train",
  "context": {                      # ← 모델 입력 (leak-free)
     "claims": "...청구항 전문...",
     "prior_art_specifications": [{"country","ref","title","claims","abstract"}]
  },
  "answer": { ... 정답 라벨 ... },    # ← 예측 대상
  "rationale": {                    # ← 합의체 근거 (정답텍스트·당사자주장 포함)
     "party_arguments": "...", "reason": "...", (chart) matrix[].evidence{quote,cue}
  },
  "meta": { "verdict","grounds","decision_date","prior_art_status", ... }
}
```

**`rationale` 와 `answer.matrix[].evidence` 는 합의체의 판단 근거 원문**이라 정답("개시되어 있다", "무효")을 그대로 포함합니다. **절대 모델 입력에 넣지 마세요** — 넣으면 태스크가 무의미해집니다. 입력은 `context`(청구항+선행기술)뿐입니다.

빠른 입력 구성은 `load.py` 의 `build_input(rec)` 참조.

## 출처 · 라이선스

- **선행기술 명세서**: 공개 특허문헌(Google Patents/KIPRIS, 등록·공개번호로 복원).
- **PII 비식별**: 청구인/피청구인/대리인 성명·회사·주소·번호를 마스킹([성명]/[회사]/[주소]/[주민번호] 등). regex 기반 — 공개 전 spot-check 권장.

## 인용



## 무결성 검증 (실측)

- **입력 누설 0**: `context`(청구항+선행기술)에서 합의체 판단문(진보성 부정/무효/용이/개시 등)을 고정밀 마커로 제거 → verdict/chart/comb 모두 0건 잔존. (claim의 "결합하여"·"채택구성" 등 기술어는 보존.)
- **PII 9,782 → ~0**: 마스킹 후 잔여 매치 11건은 전부 기술용어 오탐("대구경파이프"=large-diameter pipe, "경기별"=per-game)이며 실제 PII 아님.
- verdict 입력은 설계된 `input_text`(평균 1,908자)를 스크럽해 사용.

## 한계

- **gold tier만** 포함(silver=별지미복원·NPL 제외). Chart/Comb 일부 선행기술은 set-level 정렬.
- **별지 의존 sparse claims**: chart 92·comb 141 레코드는 청구항이 별지에 있어 `context.claims`가 짧음(선행기술로 보완). 데이터 구조적 한계.
- 마스킹·누설스크럽은 regex best-effort. **공개 전 사람 spot-check 권장.**
