---
language: [ko]
license: other
tags: [pii, prompt-injection, dlp, korean]
pretty_name: Garim (garim-guard) data and training records
---

# 가림(Garim) — 데이터 · 학습 기록

가림 L1 의 학습 · 평가 데이터와 RunPod 학습 기록이다. 저장소 루트가 프로젝트의 `data/` 디렉터리와 같은
구조라, 받아서 `data/` 에 두면 코드가 그대로 읽는다(`results/` 만 예외 — 아래). 모델은 model 저장소
[`cycloevan/garim-guard`](https://huggingface.co/cycloevan/garim-guard), 코드는 GitHub
[seok-hee97/garim-guard](https://github.com/seok-hee97/garim-guard).

> **빠진 것** — 체크섬을 통과하는 합성 주민등록번호가 든 파일(`corpus/pii-synthetic-*` · `corpus/kdpii-*` ·
> `merged/` · R1 병합 백업)과 원천 데이터 원본(`raw/`)은 이 저장소에 없다. 합성 PII 는 저장소의 생성기가 시드로
> 같은 바이트를 다시 만들고(`train/prepare_corpora.py --ack-sensitive-synthetic-identifiers`), 원천은 고정
> revision 으로 다시 받는다(`train/download_assets.py --execute`). 해시는 `*-manifest.json` 과 RUNPOD.md 에 있다.

## 구조

| 경로 | 무엇 | GPU 없이 다시 만들 수 있나 |
|---|---|---|
| `corpus/` | 공통 JSONL 코퍼스 — 공격 합성(R1 · R2) · T4 홀드아웃 · PII 음성 · KLUE · PolyGuard · deepset 번역 · 교사 입력 | ✅ 시드 결정적 |
| `local/` | deepset 한국어 번역 적용본 | ✅ |
| `runpod/2026-10-27/` | **R1** 교사 원출력 3종(kanana · Gemma 4 · Qwen3Guard) · 합의/폐기 감사 · 봉인 manifest · 6b 보고서 · Qwen 0.6B 대조본 · pod 로그 | ❌ |
| `runpod/2026-10-27-r2/` | **R2** 교사 원출력 · 합의 · 봉인 manifest · pod 로그 · `final/train/artifacts/r2/`(판정표 `verdict.json` · 지표 원본 · 결함 커널 대조값) | ❌ |
| `results/r1/` | R1 평가 결과 JSON(프로젝트의 `train/artifacts/*.json`) | — |
| `*-manifest.json` | 자산 · 학습 · 평가 봉인 | — |

교사 원출력에는 원문이 없다(id · 라벨 · 확률). 원문은 같은 id 의 `corpus/attack-teacher-input*.jsonl` 에 있다.

## 원천과 라이선스

이 저장소에 **들어 있는** 원천 파생분과 바꾼 것. 출처는 고정 revision 이다(`train/sources.yaml`).

| 원천 · 출처 | 들어 있는 파일 · 바꾼 것 | 라이선스 |
|---|---|---|
| KLUE-NER — [`klue/klue`](https://huggingface.co/datasets/klue/klue) `349481ec` | `corpus/klue_*` — NER 문장을 문자 단위 PERSON 스팬으로 바꾸고 분할 | [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| PolyGuardMix — [`ToxicityPrompts/PolyGuardMix`](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardMix) `5b7d93e9` | `corpus/polyguard_train-*` · `attack-teacher-*` · `runpod/*` 교사 출력 — 한국어 행을 고르고 교사 3종으로 공격 범주를 다시 붙임 | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |
| PolyGuardPrompts — [`ToxicityPrompts/PolyGuardPrompts`](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardPrompts) `c5b466a9` | `corpus/polyguard_eval-test` — 한국어 평가 행 선택 | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |
| deepset prompt-injections — [`deepset/prompt-injections`](https://huggingface.co/datasets/deepset/prompt-injections) `4f61ecb0` | `corpus/deepset*` · `local/deepset-*-ko` — 한국어로 번역(행별 `method`: Gemini · Claude)하고 교사로 다시 라벨링 | CC-BY-4.0 으로 다룸(원 카드는 Apache-2.0 — 더 엄격한 출처 표시 조건을 따른다) |
| bc-pii-ko — [`sehe1121/bc-pii-ko`](https://huggingface.co/datasets/sehe1121/bc-pii-ko) `327c775b` | `corpus/bc_pii_augmented_negative-test` — PII 아닌 숫자 문장 720행(학습 때 값 사전으로도 썼다) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

- PolyGuardMix 의 `source_id="itw"` 행은 공개 대화 로그에서 왔다. 원 로그에는 따로 이용 조건이 있을 수 있으니,
  그 행을 다시 배포하려면 PolyGuardMix 카드의 출처를 확인한다.
- 평가에만 쓰고 **이 저장소에 없는** 원천: KDPII([Zenodo 16759166](https://zenodo.org/records/16759166),
  CC-BY-4.0), KoreanGuardrail · korean_guardrail_test · XL-SafetyBench(CC-BY-4.0), TAB echr(MIT),
  CredData(Apache-2.0). 고정 revision 으로 다시 받는다(`train/download_assets.py --execute`).
- 프로젝트 합성 데이터(`attack-synthetic-*` · `t4-*` · `pii-negative-*` · 생성기 골드)와 학습 기록은
  Apache-2.0. 각 원천 파생분은 위 원천의 라이선스와 출처 표시 조건을 따른다.
