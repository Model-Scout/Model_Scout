---
license: gemma
language:
- ko
base_model:
- google/gemma-4-e4b-it
pipeline_tag: text-generation
tags:
- roleplay
- korean
- character
- gemma4
- qlora
- unsloth
- rlaif
- constitutional-ai
- gguf
---

# Gemma4 E4B RP RLAIF (Aetheria) — r5_v2

Gemma 4 E4B(it)를 한국어 캐릭터 롤플레이(RP)용으로 QLoRA 파인튜닝한 모델입니다.
캐릭터 챗 앱의 실서비스 프롬프트 포맷 그대로, 10조 헌법 기반 RLAIF-lite 파이프라인(합성 → 판정 → 비평-수정 → 필터)으로 만든 데이터로 학습했습니다.

*Korean character-RP QLoRA fine-tune of Gemma 4 E4B. Built by a solo middle-school founder; total cash cost ≈ $15 of GPU credit. This card documents the full arc honestly — including a retracted claim and a measured regression.*

## 버전 이력 (전부 측정 기반, 실패 포함)

| 라운드 | 데이터 | 쌍대 선호 승률(vs 베이스, LLM 판정·순서 교차 2표) | 결론 |
|---|---|---|---|
| r2 | 저가 teacher 합성 240편 | **22.8%** (CI 17.1~29.7) | 스타일 회귀 — 하향 증류로 판명, 미채택 |
| r3 | teacher를 GPT-5.6으로 교체, 157편 | **37.5%** (2회 평균) | 원인 진단 입증, 미채택 |
| **r5_v2 (현재)** | 데이터 2.15배(338편·407창), lr 4e-5·2ep | **46.3%** (82결정쌍, CI 35.6~57.3 — 동급) | **채택** |

r2 시점에는 절대 점수 루브릭이 천장에 포화해 "베이스 동급"으로 보였으나, 쌍대 선호 평가를 도입하자 열세가 드러났습니다(1회차의 "베이스보다 우세" 주장은 재측정으로 철회). 이후 학습 전 데이터를 베이스 출력과 쌍대 비교하는 게이트를 도입해, teacher 교체와 데이터 스케일로 위 궤적을 만들었습니다.

## 채택 근거 (r5_v2 vs 베이스 E4B)

| 지표 | r5_v2 | 베이스 |
|---|---|---|
| 헌법 hard_fail (1차 / 확인런 2표) | **6% / 18%** | 18% / 30% |
| 헌법 루브릭 total(20) | **19.20 / 18.96** | 19.02 / 18.42 |
| LLM 쌍대 선호 | 46.3% — 동급 | — |
| 인간 블라인드 20쌍(좌우 무작위) | **13승 (65%)** | 7승 |
| 독립 LLM 블라인드 20쌍(Claude Opus 4.6, 판정 후 언블라인드) | **15승 (75%)** | 5승 |

요약: **산문 선호는 베이스와 동급, 헌법(캐릭터 일관성·유저 대필 금지·비밀 유지 등) 위반은 절반 수준, 인간·독립 LLM 블라인드 평가는 우세.** 남은 약점은 맥락 밖 hallucination(시대착오 소품 등)으로, 인간 블라인드 평가에서 발견되어 차기 헌법 개정 항목으로 등록했습니다.

## 사용법 (Ollama)

```bash
ollama run hf.co/linda1476/Gemma4-E4B-RP-RLAIF_Pubilc
```

또는 GGUF + 동봉 `Modelfile`:

```bash
ollama create aetheria-rp-e4b -f Modelfile
```

권장: `temperature 0.9, top_k 64, top_p 0.95, num_ctx 8192`

주의:
- Gemma 4 템플릿은 user/assistant 교대 강제 — 캐릭터 오프닝(assistant 먼저)으로 시작할 땐 빈 user 턴을 앞에 넣으세요.
- Ollama `/v1` 엔드포인트에서는 요청에 `reasoning_effort: "none"` 필요(기본 thinking ON이라 content가 빔).

## 파일

| 파일 | 설명 |
|---|---|
| `gemma4-e4b-rp-rlaif.Q4_K_M.gguf` | r5_v2, 5,335,275,744 bytes, sha256 `64d51b005e297c830982ba5ac36738e1a0e874f7fb6334d55a98ede98acbd367` |
| `adapter/` | r5_v2 LoRA 어댑터(r16/α32) — 베이스 `unsloth/gemma-4-E4B-it` |
| `Modelfile` | Ollama 생성용(gemma4 renderer/parser) |

## 라이선스

[Gemma Terms of Use](https://ai.google.dev/gemma/terms) · [Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)
