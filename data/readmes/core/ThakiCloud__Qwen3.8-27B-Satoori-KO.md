---
license: other
license_name: aihub-terms
license_link: https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105
language:
- ko
base_model: Qwen/Qwen3.8-27B
base_model_relation: finetune
library_name: transformers
tags:
- korean
- dialect
- satoori
- gyeongsang
- jeolla
- jeju
- chungcheong
- gangwon
pipeline_tag: text-generation
---

# Qwen3.8-27B-Satoori-KO

A Korean **regional dialect transformation** model covering five regions: Gangwon,
Gyeongsang, Jeolla, Chungcheong, and Jeju. Trained directly on real dialect corpora, it
serves as the **real-data reference arm** against which our synthetic-data counterpart
is measured. It is a reference, not a ceiling: on a coupled marker metric the synthetic
arm scores above it, which we show is a measurement artifact rather than better dialect.

Read it together with the synthetic sibling,
[Qwen3.8-27B-Satoori-KO-Synth](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Satoori-KO-Synth),
which was trained without a single character of the source text.

⛔ **This is not a conversational model.** All training data is single-turn transformation
and classification, so the ability to hold a natural conversation in dialect was neither
trained nor measured.

## What it does

Three single-turn tasks, matching how it was trained.

| Task | Input | Output |
|---|---|---|
| Comprehension | a dialect sentence | the standard-Korean equivalent |
| Identification | a dialect sentence | which of the five regions it is |
| Generation | a standard sentence + a target region | the sentence in that dialect |

## Attribution (required notice)

This model was trained directly on the following corpora. Per the provider's terms, model
weights are a derivative work and may be released, but the source data may not be
redistributed with them.

- Korean dialect speech data (Gangwon 118, Gyeongsang 119, Jeolla 120, Jeju 121, Chungcheong 122)
- Korean dialect speech data, middle-aged and elderly speakers (71517, 71558)
- Source: AI Hub (https://aihub.or.kr)

⛔ This repository contains **no** source data and no derived data (including any
dialect-to-standard correspondence lexicon). Weights only.

## Performance

KoDialectBench v0, median of three repeats, identical serving configuration across arms.
`temperature=0` is not deterministic, which is why every figure is a median rather than a
single run.

| Task | Metric | base | **this model** | synthetic sibling |
|---|---|---|---|---|
| Comprehension | chrF | 50.7 | **80.1** | 69.4 |
| Comprehension | exact match % | 2.2 | **24.7** | 11.6 |
| Identification | accuracy % | 24.7 | **79.4** | 74.6 |
| Generation | dialectness | 0.034 | **0.141** | 0.133 |
| Generation | region match | 0.103 | 0.593 | 0.688 |
| Generation | ADI2 | 0.012 | 0.107 | 0.111 |
| Generation | meaning-preservation chrF | 68.7 | 75.8 | 79.5 |

Per region, identification accuracy: Gangwon 82.5%, and the remaining four regions are
reported in the benchmark repository.

## Limitations

**The dialectness metric is a lower bound.** It counts words matching a mined marker
lexicon, so dialect phenomena outside that lexicon (prosody, word order, discourse markers)
are invisible to it. A low score means "few markers", not "not dialect".

**Transcribed text only.** Training data is transcription, so the model has never seen
audio and carries none of the pronunciation-level information a speech model would.

**One training run per arm.** Each arm was trained with a single seed, so a small gap
between arms is not yet distinguishable from training noise. A seed repeat is in progress.

**One base model.** Measured only on Qwen3.8-27B; whether these results hold at other scales
is unverified.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

REPO = "ThakiCloud/Qwen3.8-27B-Satoori-KO"
tok = AutoTokenizer.from_pretrained(REPO)
m = AutoModelForCausalLM.from_pretrained(REPO, dtype=torch.bfloat16, device_map="cuda")

SYS = "너는 한국어 전문가다. 요청한 것만 정확히 답하고 설명·머리말·따옴표를 붙이지 않는다."

def ask(user, max_new=96):
    msgs = [{"role": "system", "content": SYS}, {"role": "user", "content": user}]
    enc = tok.apply_chat_template(msgs, add_generation_prompt=True,
                                  return_tensors="pt", enable_thinking=False)
    ids = (enc["input_ids"] if hasattr(enc, "keys") else enc)
    ids = (ids if ids.dim() > 1 else ids.unsqueeze(0)).to(m.device)
    out = m.generate(input_ids=ids, max_new_tokens=max_new, do_sample=False,
                     pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.shape[-1]:], skip_special_tokens=True).strip()

# Generation: standard -> dialect
ask("다음 표준어 문장을 경상도 방언으로 바꿔라. 뜻은 그대로 두고 말투만 바꾼다. "
    "바뀐 문장만 출력한다.\n\n어제 비가 많이 와서 길이 다 젖었더라")

# Comprehension: dialect -> standard
ask("다음 방언 문장을 표준어로 바꿔라. 바뀐 문장만 출력한다.\n\n어제 비가 마이 와가꼬 길이 다 젖었더라")

# Identification
ask("다음 문장이 어느 지역 방언인지 하나만 고른다. 지역 이름만 출력한다.\n"
    "보기: 강원도 / 경상도 / 전라도 / 제주도 / 충청도\n\n어제 비가 하영 와가주 길이 다 젖었더라", 16)
```

Prompt wording matters: these are the exact instruction templates the model was trained on.
Rephrasing them degrades output.

## Measured on out-of-domain register

The benchmark draws from the same conversational corpora the real-data arm trained on. To see
what happens outside that, we wrote six sentences ourselves (customer service, public notice,
tourism, drama dialogue, game NPC, everyday speech) and ran both models over all five regions.

| | real-data model | synthetic model |
|---|---|---|
| Region differentiation (5 regions give 5 distinct outputs) | 77% | **97%** |
| Round-trip exact recovery | **93%** | 83% |
| Correctly identifies its own generated dialect | 40% | 63% |

⛔ **The real-data model collapsed on formal customer-service register**: for
"주문하신 상품은 내일 오후에 도착할 예정입니다" it returned the identical sentence for all five
regions, ignoring the requested region entirely. The synthetic model, whose source sentences
were model-generated across a wider register range, kept the regions apart.

⛔ Differentiating is not the same as differentiating *correctly*: the synthetic model
produced a Jeju ending for a Jeolla request. And both models identify their own output poorly.

⛔ Six scenes, one greedy run. This is a demonstration, not a benchmark — do not rank the two
models on these numbers.

## Benchmark

https://huggingface.co/datasets/ThakiCloud/kodialectbench

---

<details>
<summary>한국어</summary>

한국어 **사투리 변환** 모델입니다. 강원·경상·전라·충청·제주 5개 권역을 다루며, 실제
방언 말뭉치로 직접 학습해 **성능 상한선** 역할을 합니다. 원문을 한 글자도 쓰지 않은
합성 학습 모델
([Synth](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Satoori-KO-Synth))과 짝으로
읽으십시오.

⛔ **대화 모델이 아닙니다.** 학습 데이터가 전부 단일턴 변환·분류라, 사투리로 자연스럽게
대화하는 능력은 학습된 적도 측정된 적도 없습니다.

**출처(필수 고지)**: 한국어 방언 발화 데이터(강원 118 · 경상 119 · 전라 120 · 제주 121 ·
충청 122), 중·노년층 한국어 방언 발화 데이터(71517 · 71558). 출처: AI 허브
(https://aihub.or.kr). ⛔ 이 저장소에는 원본 데이터도, 재가공 데이터(방언형·표준어형
대응 사전 포함)도 들어 있지 않습니다. 가중치만 배포합니다.

**성능**(KoDialectBench v0, 3회 중앙값): 이해 chrF 80.1 · 완전일치 24.7% · 권역식별
79.4% · 방언성 0.141 · 권역일치 0.593 · ADI2 0.107.

**한계**: 방언성 지표는 마커 어휘 기반이라 하한값입니다. 전사 텍스트만 학습해 발음
정보가 없습니다. 팔당 학습 1회라 작은 차이는 아직 학습 잡음과 구분되지 않습니다.

</details>

## Paper

Metric-Construction Coupling Inflates Measured Synthetic Dialect Recovery — [arXiv:2610.00164](https://arxiv.org/abs/2610.00164)

This checkpoint is the real-data arm that every recovery ratio in the paper is measured against — the synthetic arm's gain is reported as a fraction of this arm's gain over the base model. The paper also introduces the benchmark these cards score on, [KoDialectBench](https://huggingface.co/datasets/ThakiCloud/kodialectbench) (1,000 items · 5 regions · 3 axes). Read the numbers here as one arm of a two-arm comparison rather than as a standalone result. Synthetic arm: [Qwen3.8-27B-Satoori-KO-Synth](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Satoori-KO-Synth).
