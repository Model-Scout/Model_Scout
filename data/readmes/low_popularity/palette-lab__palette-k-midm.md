---
license: apache-2.0
base_model: K-intelligence/Midm-2.0-Base-Instruct
language:
  - ko
  - en
tags:
  - korean
  - enterprise
  - document-drafting
  - meeting-minutes
  - qlora
  - minimal-perturbation
pipeline_tag: text-generation
---

# Palette-K-Midm

**한국 기업 문서 벤치마크 1위 모델** · Minimal-perturbation adaptation of KT Mi:dm-2.0
for Korean enterprise document work · Apache-2.0 (베이스 MIT 고지 유지)

## 요약

`K-intelligence/Midm-2.0-Base-Instruct`(11.5B, MIT)를 **최소 교란(minimal-perturbation)**
방식으로 적응시킨 모델. 회의록→결정 추출 패밀리 **한 가지에만**, 교사 모델이 생성한
397건으로, LoRA r=8 · lr 4×10⁻⁵ · **1 epoch**만 학습했다.

**PALETTE-BENCH-KO v0.2 (32문항) 기준 7개 모델 중 1위 — 0.866.**

| № | 모델 | 전체 |
|---|---|---|
| 01 | **Palette-K-Midm (이 모델)** | **0.866** |
| 02 | Mi:dm-2.0 (KT, 베이스) | 0.856 |
| 03 | Palette-K-14B (자매 모델) | 0.839 |
| 04 | Qwen2.5-32B | 0.770 |
| 05 | Qwen2.5-14B | 0.765 |
| 06 | Kanana-1.5-8B (Kakao) | 0.713 |
| 07 | HyperCLOVAX-SEED-14B (Naver) | 0.705 |

## 정직한 해석 (읽고 사용할 것)

1. **격차는 0.010이다.** 32문항 시드 규모에서 통계적으로 강한 차이가 아니다.
   "이 벤치마크에서 근소하게 앞선다"가 정확한 표현이며, "한국 최고 LLM"이 아니다.
   일반 한국어 능력은 측정 대상이 아니다.
2. **회의록→결정은 개선하지 못했다** (0.582, 베이스와 동일). 매크로 이득은 학습하지 않은
   패밀리들의 능력을 보존한 데서 나온다(이메일 +0.062, 품의서 +0.062, 정책 −0.063).
3. **공격적으로 학습하면 오히려 나빠진다.** 같은 베이스를 r=32 · lr 2×10⁻⁴ · 697건 ·
   6패밀리 · 3 epoch로 학습한 버전은 **0.769로 베이스보다 낮았다**(파국적 망각, 작성
   계열 −0.06~−0.13). 이 카드의 모델이 이긴 이유는 **적게 학습했기 때문**이다.
4. 루브릭 4개 패밀리는 gpt-4o 심사 — 심사자가 바뀌면 절대값이 움직인다. 결정적 2개
   패밀리(공시·회의록)가 교차 모델 비교의 기준이다.

## 학습 방법

- **베이스:** Midm-2.0-Base-Instruct (11.5B, MIT) — NF4 4-bit double-quant, **동결**
- **어댑터:** LoRA r=8, α=16, dropout 0.05 — q,k,v,o,gate,up,down 전 projection
- **데이터:** 회의록→결정 397건 (교사 모델 생성: 상대 날짜·보류 항목·진행중 방해
  항목·기한 없는 결정 명시 포함). 벤치마크 32문항 전체와 **SHA-256 해시 검증 disjoint**
- **학습:** 1 epoch, lr 4×10⁻⁵ cosine (warmup 3%), 유효 배치 16, paged-AdamW-8bit,
  max_seq 2048, H100 1장 · CPU에서 bf16 병합
- **데이터 출처:** 합성 데이터만 사용. 고객 데이터·크롤링 자료 미사용

## 사용

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
m = "imcapsule/palette-k-midm"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype="bfloat16", device_map="auto")
msgs = [{"role":"user","content":"다음 회의록에서 결정 사항을 JSON으로 추출하라. ..."}]
ids = tok.apply_chat_template(msgs, return_tensors="pt", add_generation_prompt=True).to(model.device)
print(tok.decode(model.generate(ids, max_new_tokens=800, do_sample=False)[0][ids.shape[-1]:]))
```

## 인용

```bibtex
@misc{palettekmidm2026,
  title  = {Palette-K-Midm: Minimal-Perturbation Korean Enterprise Adaptation of Mi:dm-2.0},
  author = {Palette}, year = {2026},
  note   = {Apache-2.0; ranks 1st on PALETTE-BENCH-KO v0.2 (margin 0.010, n=32)}
}
```

## English summary

A minimal-perturbation QLoRA adaptation of KT's Mi:dm-2.0 (11.5B, MIT): LoRA rank 8,
lr 4×10⁻⁵, **one epoch**, on 397 teacher-generated meeting-minutes examples only —
hash-verified disjoint from the benchmark. **Ranks 1st of 7 (0.866)** on PALETTE-BENCH-KO
v0.2, ahead of its own base (0.856). The margin is 0.010 at n=32 — *narrowly ahead on this
benchmark*, not "Korea's best LLM". The interesting result is the ablation: an aggressive
configuration of the same base (rank 32, lr 2×10⁻⁴, 3 epochs, six families, ~100× the
cumulative update budget) scored **0.769 — below the untuned base** — through catastrophic
forgetting. Less training won. Minutes→decision extraction remains unimproved at 0.582,
the open hard family for every model tested. Full methodology, equations and failed rounds:
see the PALETTE-BENCH-KO technical report.
