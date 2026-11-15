---
license: apache-2.0
language:
- ko
- en
library_name: transformers
base_model: Qwen/Qwen3.5-4B
tags:
- decision-model
- calibration
- classification
- system-one
- korean
datasets:
- AmazonScience/massive
- AmazonScience/massive-agents
- Davlan/sib200
- McGill-NLP/FaithDial
- UCLNLP/sharc
- allenai/qasc
- allenai/social_i_qa
- allenai/winogrande
- apple/mkqa
- clinc/clinc_oos
- deepmind/aqua_rat
- google-research-datasets/paws
- google-research-datasets/paws-x
- google-research-datasets/taskmaster3
- google/boolq
- google/civil_comments
- hotpotqa/hotpot_qa
- jeanlee/kmhas_korean_hate_speech
- kakaobrain/kor_nli
- klue/klue
- miracl/miracl
- miracl/nomiracl
- nayohan/korean-hate-speech
- nvidia/Aegis-AI-Content-Safety-Dataset-1.0
- nvidia/HelpSteer2
- nyu-mll/blimp
- openai/gsm8k
- rajpurkar/squad_v2
- skt/kobest_v1
- songys/kor_qpair
- tals/vitaminc
- tau/commonsense_qa
- wicho/kor_3i4k
---

# nari-decision-4b

A Korean + English **decision model**. Give it a *state* (text or JSON: a conversation, a document, a tool result…) and typed *questions* — yes/no (`noul`), pick-one (`choice`), or ordinal (`score`) — and it returns a calibrated probability for every option in **one forward pass**, without generating text. Use the confidence to route low-certainty cases to a person or a larger model (selective prediction). From the same pass it reads two answers per question — a trained decision head and the backbone's own answer letter — and averages them.

한국어·영어 결정 모델입니다. 상태(대화·문서·도구 결과 등)와 타입이 정해진 질문(예/아니오, 하나 고르기, 순서 척도)을 받아, 글을 생성하지 않고 한 번의 forward로 선택지마다 보정된 확률을 냅니다. 라우팅, 가드레일(그대로 보내도 되나), RAG 관련성 판단, 에이전트 분기, 데이터 라벨링에 씁니다. 같은 forward에서 질문마다 학습한 결정 헤드의 답과 백본이 직접 고른 글자 답을 함께 읽어 평균합니다.

## Highlights

- **Most accurate in both languages.** Against every model below, on the same questions, it leads every column: held-out 85.9% Korean / 85.3% English, System One eval set 82.1% / 76.9% — 5.1–15.5 points above the best other model in each.
- **Reads the instruction, negation included.** Asked about the same text and options for the statement that matches and for the one that does not (1,000 held-out KLUE-NLI pairs, instruction wording not seen in training), it gets both right in 98.3% of pairs (v2: 98.9%).
- **Fast: all questions in one forward pass.** 32 ms per request on one NVIDIA A100 80GB PCIe at batch 1 with `enable_cuda_graphs()` (63 ms without; mean of 5 requests) — on par with laya (English) at 30 ms, 56% faster than clef-flash (9B) (73 ms), 72% faster than Prompted Qwen3.5-4B (115 ms) and 77% faster than JEV-9B (141 ms). Longer states and more questions add little (25 → 44 ms from simple to complex requests); models that send one request per question grow with each (Prompted Qwen3.5-4B 94 → 146 ms, JEV-9B 86 → 225 ms). Only laya-multilingual is faster (23 ms), at 30–36% accuracy on the eval set.
- **Calibrated confidence.** One temperature per question type, fitted on a separate calibration split: held-out ECE 0.012, eval set 0.041. Send low-confidence cases to a person or a larger model.
- **Hosted API.** This version is also served as [BlackOX](https://api.blackmallangcow.com). Send the same `state` and `questions` as `decide()` to `POST https://api.blackmallangcow.com/v1/decide` ([docs](https://api.blackmallangcow.com/docs/start)).

| Model | Size | Held-out ko | Held-out en | Eval set ko | Eval set en | ms / request |
|---|---|---:|---:|---:|---:|---:|
| **nari-decision-4b** (this model) | 4B | **85.9** | **85.3** | **82.1** | **76.9** | 32 |
| Prompted Qwen3.5-4B | 4B | 68.8 | 62.6 | 67.8 | 64.7 | 115 |
| clef-flash (9B) | 9B | 75.2 | 69.8 | 73.8 | 71.8 | 73 |
| JEV-9B | 9B | 67.3 | 53.2 | 76.0 | 67.3 | 141 |
| laya-multilingual | 322M | 51.0 | 49.9 | 36.4 | 30.1 | 23 |
| laya (English) | 395M | — | 52.1 | — | 36.5 | 30 |

Accuracy (%) after temperature calibration, same questions for every model (on held-out, Prompted Qwen3.5-4B and JEV-9B skip questions with more options than they can take). ms / request: mean of 5 requests at batch 1 on one NVIDIA A100 80GB PCIe (this model with `enable_cuda_graphs()`). Details under Evaluation.

**요약**

- **두 언어 모두 가장 정확합니다.** 같은 문항으로 비교한 아래 모델들보다 모든 칸에서 높습니다: held-out 한국어 85.9% / 영어 85.3%, System One 평가셋 82.1% / 76.9% (칸마다 그다음 모델보다 5.1–15.5%p 높음).
- **지시문을 읽습니다 (부정형 포함).** 같은 글·같은 보기에 맞는 것과 맞지 않는 것을 각각 물으면 (KLUE-NLI 검증 1,000쌍, 학습에 없던 지시문) 두 질문을 모두 맞히는 비율이 98.3%입니다 (v2: 98.9%).
- **빠릅니다.** 질문 여러 개를 한 번의 forward로 판단해 NVIDIA A100 80GB PCIe 한 장, 배치 1에서 요청당 32ms입니다 (`enable_cuda_graphs()`를 켠 값이고 끄면 63ms, 5건 평균). laya (English) 30ms와 비슷하고, clef-flash (9B) 73ms보다 56%, Prompted Qwen3.5-4B 115ms보다 72%, JEV-9B 141ms보다 77% 빠릅니다. 질문이 늘고 상태가 길어져도 25ms → 44ms로 조금만 늘어납니다. 이보다 빠른 건 23ms인 laya-multilingual뿐이고, 평가셋 정확도는 30–36%입니다.
- **확률이 보정되어 있습니다.** 질문 타입별 temperatures를 따로 떼어 둔 보정 분할로 맞춰 held-out ECE 0.012, 평가셋 0.041입니다. 확신이 낮은 건은 사람이나 더 큰 모델로 넘기면 됩니다.
- **호스팅 API.** 이 버전을 [블랙OX](https://api.blackmallangcow.com)로도 씁니다. `decide()`와 같은 상태와 질문을 `POST https://api.blackmallangcow.com/v1/decide`로 보내면 됩니다 ([문서](https://api.blackmallangcow.com/docs/start)).

## Usage

```python
from transformers import AutoModel, AutoTokenizer

tok = AutoTokenizer.from_pretrained("blackmallangcow/nari-decision-4b", trust_remote_code=True)
model = AutoModel.from_pretrained("blackmallangcow/nari-decision-4b", trust_remote_code=True).eval()
# On a GPU, for one request at a time: record the forward once per input-length bucket (about 5 s), then reuse it
# model.to("cuda").enable_cuda_graphs()
out = model.decide(
    tok,
    state="고객: 지난주 주문이 두 번 결제됐어요. 한 건은 취소해 주세요.",
    questions={
        "refund": {"type": "noul", "instructions": "환불·취소 요청인가요?"},
        "team": {"type": "choice", "instructions": "담당 팀을 고르세요.",
                 "options": ["billing", "shipping", "account", "none"]},
        "urgency": {"type": "score", "instructions": "긴급도", "options": ["1", "2", "3", "4", "5"]},
    },
)
# {"answers": {"refund": {"answer": True, "p_true": ..., "probs": {...}},
#              "team": {"answer": "billing", "confidence": ..., "probs": {...}},
#              "urgency": {"answer": "3", "confidence": ..., "expected": ..., "probs": {...}}},
#  "truncated": False}
```

- `instructions` is optional; the question name and options alone also work. Korean or English.
- If state + questions exceed 2,048 tokens the state is cut in the middle, keeping its first quarter and last three quarters of the room (`truncated` tells you). Questions and options are never cut.
- Several questions can be asked about the same state in one call.
- Each answer also has `paths`: the decision head's and the backbone letter's probabilities before averaging and calibration. Questions with more than 26 options use the head only.
- Needs a recent `transformers` with Qwen3.5 support. `flash-linear-attention` and `causal-conv1d` make it faster on GPU but are optional.

## Guidelines

### Writing questions

- Give each question a name that says what it asks. The name is written into the input, and without `instructions` it is the whole question:

  ```
  ### 질문 1: q1 [예/아니오 (true/false)]             <- the model cannot tell what is asked
  ### 질문 1: contains_pii [예/아니오 (true/false)]   <- the name alone asks the question
  ```

  - `q1` → `contains_pii` (does the text expose personal information?)
  - `flag` → `safe_to_send` (can this reply go to the user as is?)
  - `cat` → `support_team` (which team should handle it?)
  - `level` → `urgency` (how urgent, 1–5?)

- Add a `none` option when none of the options may apply.
- Keep options mutually exclusive.
- Put everything the decision depends on into the state, including settings and earlier turns. The model is more likely to call information missing when it appears only indirectly: in settings, in an earlier turn, or loosely ("any time this week").
- For an ordinal question (`"type": "score"`), list its options from lowest to highest, e.g. `["1", "2", "3", "4", "5"]` or `["low", "medium", "high"]`. The model reads this order as the scale, and the answer's `expected` is the probability-weighted position (1 = the first option).
- Phrase yes/no (`noul`) questions so that "yes" is the case you want to catch; `p_true` is its probability.
- With up to 26 options both readouts answer; with more, only the decision head does.

### Act on the confidence

Use the probability, not only the top answer: act automatically above a threshold and send the rest to a person or a larger model.

Example from the System One eval set: 50 guardrail responses (26 unsafe, 24 safe), sending a response only when `p_true` of `safe_to_send` is at least the threshold.

| Threshold | Unsafe responses sent | Safe responses held for a person |
|---:|---:|---:|
| 0.5 | 2 / 26 | 1 / 24 |
| 0.8 | 1 / 26 | 1 / 24 |
| 0.9 | 1 / 26 | 4 / 24 |

The sample is small. Start near these values and set the threshold on a few hundred labeled examples of your own.

For questions that decide whether to ask the user back (is information missing, does the request need clarification), ask back only above a higher threshold. Example from the System One eval set: 51 clarification questions, 21 where the information is given and 30 where it is missing, counting an answer as "missing" only when `p_true` is at least the threshold.

| Threshold | Information given but called missing | Missing information not caught |
|---:|---:|---:|
| 0.5 | 8 / 21 | 2 / 30 |
| 0.7 | 5 / 21 | 3 / 30 |
| 0.8 | 4 / 21 | 4 / 30 |

Again a small sample: tune the threshold on your own requests.

### Multi-step tool calls

Let the model choose the next tool, but enforce prerequisite steps such as authentication or looking up an ID in your agent code. The model tends to pick the tool for the user's goal rather than the step that has to come first: on the API-Bank tool-selection task of the Decision Index public suite, when the correct next call was the authentication step (`GetUserToken`), it chose it in 2 of 108 cases (256 of 508 correct overall).

For ordinal (`score`) questions, read `expected` or the whole distribution rather than only the top option: on held-out the top option is exactly right 57.7% of the time, but within one step 91.9%.

### Pin the version

Without `revision`, `from_pretrained` follows `main`, which moves with each release. In production, pin one: `revision="v3.2"`.

### Re-fit the temperatures

Probabilities are scaled by `temperatures` fitted on the calibration split, kept in `model.config.temperatures`. On data unlike the training mix, re-fit them: set `model.config.temperatures = {"*": 1.0}` to get unscaled probabilities, collect them for a few hundred labeled questions of your own, find for each key the value T that minimizes the log loss of softmax(log p / T), and write the values back.
Keys are `type:options` (`noul:2`, `choice:3-5`, `choice:6+`, `choice:2`, `score:3-5`, `choice:27+`, `score:6+`, where `choice:27+` is for head-only questions); `*` is used for any missing key.

### Intended use

- Decisions over text you already have: routing, guardrail checks, RAG relevance, agent branching, ticket triage, moderation queues and labeling, with low-confidence cases sent to a person or a larger model.

### Out of scope

- Decisions with legal, medical, hiring or credit consequences without human review.
- A general content-safety filter: the guardrail questions cover PII, secrets and prompt injection.
- Questions that need broad knowledge or long reasoning (see Limitations), and generating text.

### Bias

- Part of the training data is hate-speech and social-bias data (K-MHaS, Korean HateSpeech, KoSBi, DynaHate, Civil Comments). Judgments about groups of people can still be biased. On KoBBQ (Korean bias QA, never trained on) it answers 87.5% correctly.

### Hardware

- The weights are bf16: 4.2B parameters, 8.46 GB (text model only; the backbone's vision part is left out). Plan on GPU memory beyond that for the input; `enable_cuda_graphs()` keeps extra buffers for its recordings.
- `enable_cuda_graphs()` needs a CUDA GPU. CPU and Apple Silicon (MPS) are untested.
- There is no quantized version: quantizing would change the scores the `temperatures` were fitted on.
- `decide()` takes one state per call; for bulk labeling, loop over the records (about 31 requests per second on one NVIDIA A100 80GB PCIe with `enable_cuda_graphs()`).

**사용 가이드 요약**

- 질문 이름은 무엇을 묻는지 드러나게 짓습니다. 이름이 입력에 `### 질문 1: contains_pii [예/아니오 (true/false)]`처럼 그대로 들어가서, 지시문이 없으면 이름이 곧 질문입니다. 예: `q1` 대신 `contains_pii`(개인정보가 드러나 있나), `flag` 대신 `safe_to_send`(그대로 보내도 되나), `cat` 대신 `support_team`(어느 팀이 맡나), `level` 대신 `urgency`(얼마나 급한가, 1–5).
- 맞는 선택지가 없을 수 있으면 선택지에 `none`을 넣습니다.
- 선택지끼리 뜻이 겹치지 않게 씁니다.
- 판단에 필요한 설정·앞선 대화는 상태에 직접 넣습니다. 정보가 설정이나 앞선 대화에만 있거나 느슨하게 주어지면 ("이번 주 중 아무 때나") 빠졌다고 판정하기 쉽습니다.
- 순서 척도 질문(`"type": "score"`)은 선택지를 낮은 쪽에서 높은 쪽 순서로 적습니다. 예: `["1", "2", "3", "4", "5"]`, `["낮음", "보통", "높음"]`. 모델은 이 순서를 척도로 읽고, 답의 `expected`도 이 순서의 순번(첫 선택지 = 1)으로 계산합니다.
- 사용자에게 되물을지 정하는 질문(정보가 빠졌나, 확인이 필요한가)은 더 높은 확신에서만 되묻습니다. 평가셋 clarify 51문항에서 `p_true` 0.5 이상을 빠짐으로 보면 정보가 있는 21문항 중 8개를 빠졌다고 하고, 0.7 이상이면 5개로 줄어듭니다 (정말 빠진 30문항 중 놓치는 수는 2 → 3).
- 여러 단계 도구 호출에서 인증·ID 조회처럼 먼저 불러야 하는 단계는 에이전트 코드에서 순서를 지킵니다. 모델은 사용자 목적의 도구를 바로 고르는 경향이 있어, 공개 스위트 API-Bank에서 정답이 인증 단계인 108문항 중 2개만 골랐습니다.
- 순서 척도 질문은 1등 선택지만 보지 말고 `expected`나 확률 분포를 봅니다. held-out에서 1등 선택지가 정확히 맞는 건 57.7%지만, 한 칸 차이 안에는 91.9%가 들어옵니다.
- 운영에서는 `revision="v3.2"`로 버전을 고정합니다. 지정하지 않으면 새 버전이 나올 때 바뀝니다.
- 학습 분포와 다른 데이터에서는 `temperatures`를 자기 데이터 수백 건으로 다시 맞춥니다 (`model.config.temperatures`).
- 법률·의료·채용·대출처럼 결과가 큰 결정에는 사람 검토 없이 쓰지 않습니다. 일반 유해 콘텐츠 필터가 아니고, 넓은 지식이나 긴 추론이 필요한 질문과 글 생성에는 맞지 않습니다.
- 가중치는 bf16 8.46GB이고 그보다 많은 GPU 메모리가 필요합니다. CUDA 그래프는 CUDA GPU에서만 되고, 양자화본은 없습니다.

## Versions

- **v3.2** (2026-10-18, this version) — more decisions for agents and RAG: claim verification, checking a response against its sources, phishing and spam, choosing a tool or intent, commonsense and math. Each question family's answers are also balanced in the loss, so one task's yes/no habit does not leak into another. Continued from v2 (40,553 steps in total)
  - Hosted API (2026-10-31): this version is also served as [BlackOX](https://api.blackmallangcow.com), an HTTP API. Send the same `state` and `questions` as `decide()` to `POST https://api.blackmallangcow.com/v1/decide`. Docs: https://api.blackmallangcow.com/docs/start
  - 호스팅 API (2026-10-31): 이 버전을 HTTP API [블랙OX](https://api.blackmallangcow.com)로도 씁니다. `decide()`와 같은 상태와 질문을 `POST https://api.blackmallangcow.com/v1/decide`로 보내면 됩니다. 문서: https://api.blackmallangcow.com/docs/start
  - Decision Index 0.3, public suite (run locally, public part only): 38.49 → 44.80 (see the table under Evaluation)
  - New training data: HoVer, VitaminC, Fool Me Twice, FaithDial, MASSIVE-Agents, STAR, Taskmaster-3, BANKING77, Amazon ESCI, WinoGrande, CommonsenseQA, CSQA2, Social IQa, QASC, StrategyQA, AQuA-RAT, GSM8K, BLiMP, the Nazario and CLAIR phishing corpora, UCI SMS Spam, Korean public text messages, and new synthetic sets (response choice, RAG response checks, phishing). Training rows that overlap any Decision Index public benchmark were removed
  - System One eval set: 80.2% → 80.5% (Korean 82.6% → 82.1%, English 74.4% → 76.9%), ECE 0.034 → 0.041
  - Held-out, same 79,688 questions: 86.3% → 85.6%, ECE 0.012 → 0.012
  - MMMLU-ko, all 13,912 questions: 58.3% → 58.5%; 2026 bar and legal ethics exams (188 questions): 43.6% → 43.1%
  - Polarity pairs, both right: 98.9% → 98.3%
  - Batch-1 latency with `enable_cuda_graphs()` on one A100 80GB PCIe: 32 → 32 ms
  - Weaker than v2: Belebele-ko 87.1% → 84.6%. On the eval set's clarification items (80.4%, v2 86.3%) it more often judges information as missing when it is given only in settings, in earlier turns or loosely ("any time this week"); routing 72.1% (v2 73.8%)
  - 에이전트·RAG용 판단을 늘렸습니다: 주장 검증, 근거 대조, 피싱·스팸, 도구·의도 고르기, 상식·수학. 질문 묶음마다 정답 비율을 손실에서 맞춰, 한 과제의 예/아니오 습관이 다른 과제로 옮겨 가지 않게 했습니다. Decision Index 공개 지수 38.49 → 44.80
- **v2** (2026-10-15) — a second answer from the same forward pass: the backbone's own answer letter, averaged with the decision head. Trained from scratch for 1 epoch, then continued for 1 more at a lower learning rate (17,082 steps)
  - Input: each question is its own chat turn ending in "Answer with one letter."; the answer slot is the start of the assistant turn
  - The letter readout is trained with cross-entropy and kept close to the original backbone with a KL term, so the backbone's knowledge stays usable
  - New training data: Korean bar exam (1st–13th) and legal ethics exam (1st–15th) multiple-choice questions from the Ministry of Justice (KOGL Type 1)
  - MMMLU-ko, all 13,912 questions: 49.4% → 58.3% (the prompted backbone: 58.6%)
  - 2026 bar and legal ethics exams (188 questions, after every round used for training): 19.1% → 43.6% (the prompted backbone: 29.3%)
  - Belebele-ko: 79.6% → 87.1%
  - System One eval set: 79.8% → 80.2% (Korean 80.7% → 82.6%, English 77.6% → 74.4%), ECE 0.049 → 0.034
  - Held-out, same 79,688 questions: 85.4% → 86.3%, ECE 0.022 → 0.012
  - Ordinal (`score`) questions on held-out: 57.0% → 59.3% exactly right (90.9% → 91.4% within one step), ECE 0.040 → 0.020; unchanged on the eval set (50.5%, 99 questions)
  - Polarity pairs, both right: 97.9% → 98.9%
  - Batch-1 latency with `enable_cuda_graphs()` on one A100 80GB PCIe: 26 → 32 ms (the per-question chat turns add about 20 tokens per question)
  - 질문마다 채팅 차례를 나눠, 같은 forward에서 백본이 직접 고른 글자 답도 읽어 결정 헤드와 평균합니다. 학습에 쓰지 않은 지식(MMMLU 한국어)이 같은 백본 수준으로 돌아왔고, 법무부 국가시험 기출을 학습에 더했습니다
  - Still available with `revision="v2"`
- **v1.1** (2026-10-14) — continued from v1.0 with polarity pairs built from KLUE-NLI (both questions right: 1.6% → 97.9%); the 2026-10-15 code update added `enable_cuda_graphs()`
  - Still available with `revision="v1.1"`
- **v1.0** (2026-10-14) — first release
  - Still available with `revision="v1.0"`, e.g. `AutoModel.from_pretrained("blackmallangcow/nari-decision-4b", revision="v1.0", trust_remote_code=True)`

## Evaluation

### Held-out (79,688 questions)

Official validation/test splits of the training sources plus evaluation-only benchmarks (APEACH, Belebele 한국어, KoBBQ, MMMLU 한국어), at most 1,000 records per task. Never used for training or calibration.

| | Questions | Accuracy (%) | ECE (raw → calibrated) | NLL | Brier | Selective acc @80% (%) |
|---|---:|---:|---|---:|---:|---:|
| All | 79,688 | 85.6 | 0.009 → 0.012 | 0.412 | 0.199 | 92.7 |
| Korean | 43,730 | 85.9 | 0.022 → 0.025 | 0.407 | 0.209 | 92.3 |
| English | 35,958 | 85.3 | 0.012 → 0.009 | 0.418 | 0.187 | 93.3 |
| noul | 45,371 | 90.6 | 0.005 → 0.009 | 0.277 | 0.140 | 94.8 |
| choice | 27,907 | 83.9 | 0.028 → 0.020 | 0.490 | 0.226 | 91.5 |
| score | 6,410 | 57.7 | 0.028 → 0.026 | 1.025 | 0.502 | 62.7 |

The numbers above are from the evaluated model (LoRA kept separate). The released weights merge the LoRA into bf16; on a sample, accuracy of evaluated → released: eval set: 79.83 → 79.56 % (362 questions, answers agree 99.5%); held-out: 84.40 → 84.40 % (2,602 questions, answers agree 99.7%).

### System One eval set (519 questions, 200 items: Korean 140 / English 60)

Hand-checked scenarios close to real use: routing, guardrails, RAG relevance gates, agent branching, clarification. Written with an open-weights model and reviewed item by item; no overlap with the training data (MinHash, Jaccard 0.5).

| | Questions | Accuracy (%) | ECE (raw → calibrated) | NLL | Brier | Selective acc @80% (%) |
|---|---:|---:|---|---:|---:|---:|
| All | 519 | 80.5 | 0.045 → 0.041 | 0.521 | 0.278 | 88.2 |
| Korean | 363 | 82.1 | 0.044 → 0.048 | 0.490 | 0.262 | 89.3 |
| English | 156 | 76.9 | 0.095 → 0.075 | 0.593 | 0.315 | 86.4 |
| noul | 220 | 85.5 | 0.050 → 0.050 | 0.361 | 0.221 | 90.9 |
| choice | 200 | 86.5 | 0.061 → 0.049 | 0.415 | 0.195 | 94.4 |
| score | 99 | 57.6 | 0.153 → 0.118 | 1.090 | 0.572 | 60.0 |

| Category | Accuracy (%) | ECE |
|---|---:|---:|
| routing | 72.1 | 0.097 |
| guardrail | 83.0 | 0.057 |
| rag_gate | 83.5 | 0.066 |
| agent | 84.2 | 0.090 |
| clarify | 80.4 | 0.114 |

### Ordinal (`score`) questions

Exact accuracy is strict for ordinal labels, and most misses are one step off. `expected` is the probability-weighted position of the answer (1 = the first option); its error is counted in option steps.

| Set | Questions | Exact (%) | Within one step (%) | Mean error of `expected` (steps) | ECE |
|---|---:|---:|---:|---:|---:|
| Held-out | 6,410 | 57.7 | 91.9 | 0.62 | 0.026 |
| ↳ HelpSteer2 response ratings, 0–4 | 5,000 | 57.7 | 93.2 | 0.61 | 0.038 |
| ↳ KLUE-STS similarity, 0–5 | 519 | 56.6 | 97.1 | 0.53 | 0.075 |
| ↳ Korean HateSpeech level (none < offensive < hate) | 471 | 64.8 | 97.5 | 0.40 | 0.125 |
| ↳ HelpSteer2 preference strength, −3 to 3 | 420 | 51.4 | 64.3 | 1.14 | 0.062 |
| System One eval set | 99 | 57.6 | 87.9 | 0.62 | 0.118 |

### Two readouts from one pass

Each question is answered twice from the same forward pass: by the decision head and by the backbone's own answer letter. The released model averages the two (log-probabilities, 0.5 / 0.5) and then calibrates. Accuracy (%) / ECE, each readout calibrated on its own, on the questions that have an answer letter (at most 26 options): 75,688 held-out questions.

| Set | Decision head | Backbone letter | Averaged (this model) |
|---|---|---|---|
| Held-out | 85.6 / 0.016 | 83.8 / 0.030 | 85.7 / 0.011 |
| System One eval set | 80.9 / 0.059 | 77.8 / 0.041 | 80.5 / 0.041 |

### Knowledge, reading and exams (never trained on)

Accuracy (%). The prompted backbone is `Qwen/Qwen3.5-4B` without training, asked one question per request with the options as letters (first-token letter probabilities). MMMLU-ko is OpenAI's professional Korean translation of MMLU (MIT); Belebele-ko is Meta's reading benchmark (CC BY-SA 4.0); the exams are the Ministry of Justice's 2026 rounds, after every round used for training (KOGL Type 1, source: 법무부).

| Benchmark | Questions | This model | Prompted Qwen3.5-4B | v2 |
|---|---:|---:|---:|---:|
| MMMLU-ko, all questions (knowledge) | 13,912 | **58.5** | 58.6 | 58.3 |
| Belebele-ko (reading) | 898 | **84.6** | 82.5 | 87.1 |
| Korean bar exam (15th) + legal ethics exam (17th), 2026 | 188 | **43.1** | 29.3 | — |

### Decision Index 0.3, public suite

Chance-corrected skill (0 = random guessing, 100 = perfect) on the public benchmark panel of the [Decision Index](https://multimodalart-jev-decision-index.static.hf.space/index.html) leaderboard (edition 0.3, 140,178 scored requests), run locally with the leaderboard's own kit; unanswered requests count as wrong. The index is a fixed-weight mean of five areas. This is the public part only: the board's Full score adds private tests that its maintainers run. These are our own runs, not numbers taken from the leaderboard.

| | v2 | This model |
|---|---:|---:|
| Decision Index (public) | 38.49 | **44.80** |
| Knowledge & Reasoning | 24.6 | **28.8** |
| Language Understanding | 42.0 | **44.5** |
| Retrieval & Classification | 40.4 | **59.8** |
| Tools & Automation | 60.6 | **62.1** |
| Arts & Human Taste | 21.3 | **25.4** |

### Baselines (zero-shot, same questions)

- **Prompted Qwen3.5-4B**: the same backbone without training; options shown as letters, first-token letter probabilities (questions with more than 26 options skipped).
- **clef-flash (9B)**: Cloudflare's open decision model (Qwen3.5-9B based), released weights and code.
- **JEV-9B**: AutoTrust's open decision model (Qwen3.5-9B + decision LoRA/head), System 1 via vLLM as in its model card (choice ≤ 16 options, score ≤ 6 levels).
- **laya-multilingual**: Convai's open decision model (mmBERT-base, 322M), released weights via the laya package.
- **laya (English)**: Convai's English decision model (ModernBERT-large), English records only.
- All baselines are temperature-calibrated the same way on the calibration split. Cells are accuracy (%) / ECE.

| Set | This model | Prompted Qwen3.5-4B | clef-flash (9B) | JEV-9B | laya-multilingual | laya (English) |
|---|---|---|---|---|---|---|
| Held-out | 85.6 / 0.012 | 66.0 / 0.038 | 72.8 / 0.014 | 61.1 / 0.040 | 50.5 / 0.025 | — |
| Held-out, Korean | 85.9 / 0.025 | 68.8 / 0.040 | 75.2 / 0.021 | 67.3 / 0.028 | 51.0 / 0.029 | — |
| Held-out, English | 85.3 / 0.009 | 62.6 / 0.047 | 69.8 / 0.027 | 53.2 / 0.059 | 49.9 / 0.040 | 52.1 / 0.030 |
| System One eval set | 80.5 / 0.041 | 66.9 / 0.052 | 73.2 / 0.077 | 73.4 / 0.088 | 34.5 / 0.119 | — |
| Eval set, Korean | 82.1 / 0.048 | 67.8 / 0.061 | 73.8 / 0.077 | 76.0 / 0.115 | 36.4 / 0.110 | — |
| Eval set, English | 76.9 / 0.075 | 64.7 / 0.058 | 71.8 / 0.098 | 67.3 / 0.072 | 30.1 / 0.173 | 36.5 / 0.153 |

### Speed (batch 1, one NVIDIA A100 80GB PCIe)

5 requests from the System One eval set: 3 simple (2 questions, 43–97-character state; 2 Korean, 1 English) and 2 complex (3 questions, 552–900-character state; 1 Korean, 1 English). Each number is the mean over those requests of the median of 10 runs (after 3 warm-up runs). The other models were measured on one A100 80GB PCIe on 2026-10-15; this model (the released weights) was measured the same way on an A100 80GB PCIe on 2026-10-18. The computation is the same as v2's: 63.4 ms eager here, 64.3 ms for v2 on the first machine. Models run through transformers are eager (no compilation or CUDA graphs) unless the row says `enable_cuda_graphs()`; the vLLM servers use vLLM's default CUDA graphs.

| Model | Mean (ms) | Simple (ms) | Complex (ms) | How it runs |
|---|---:|---:|---:|---|
| laya-multilingual | 22.7 | 22.1 | 23.5 | laya package (encoder), all questions in one pass |
| laya (English) | 30.4 | 27.0 | 35.5 | laya package (encoder), all questions in one pass |
| **nari-decision-4b** (this model) | 32.2 | 24.7 | 43.5 | transformers + `enable_cuda_graphs()`, all questions in one forward pass |
| **nari-decision-4b** (this model) | 63.4 | 62.7 | 64.5 | transformers, all questions in one forward pass |
| clef-flash (9B) | 73.4 | 66.4 | 83.8 | transformers, all questions in one forward pass |
| Prompted Qwen3.5-4B | 115.1 | 94.4 | 146.1 | local vLLM server, one request per question |
| JEV-9B | 141.4 | 85.7 | 224.9 | local vLLM server, one request per question |

## Training

- Backbone: `Qwen/Qwen3.5-4B` (text model only), frozen, with LoRA on every linear layer (attention, Gated DeltaNet projections, MLP). The LoRA is merged into the released weights.
- Decision head: the hidden state at the end of each option line is the query; 2 layers of self-attention across options and cross-attention over the whole sequence, plus a linear prior; softmax per question.
- Input: the backbone's chat template with one user turn per question, ending in "Answer with one letter."; the answer slot is the start of the assistant turn (earlier questions get an empty one).
- Backbone letter: the hidden state at the answer slot times the backbone's own (tied) embedding rows for the option letters A, B, …. The answer averages the head's and the letters' log-probabilities (0.5 / 0.5), then applies the temperature.
- Loss: log loss + Brier score (+ ranked probability score for ordinal questions) on the head, all strictly proper scoring rules, plus cross-entropy on the answer letter and a KL term that keeps the letter distribution close to the original backbone (adapter off, on a quarter of each batch). Option order is shuffled every epoch (except ordinal).
- Calibration: one temperature per (question type, number of options), and one for head-only questions with more than 26 options, fitted on a separate calibration split: `{"*": 1.0, "noul:2": 0.9278, "choice:3-5": 1.1189, "choice:6+": 0.9632, "choice:2": 1.0, "score:3-5": 1.0382, "choice:27+": 1.1189, "score:6+": 0.8937}`
- Data: 427,158 labeled questions (Korean 52%, English 48%) from 54 sources. 40,553 steps on one A100 80GB.
- Answer balance: in 70 of 110 question families the loss weights each answer so the weighted answer mix is close to uniform (yes/no questions: 41.4% → 48.7% yes), so the model does not carry one task's answer prior into another. Families whose natural answer is "none" or "no" keep their mix, and 2 small families are up-weighted. Calibration and evaluation use the natural mix.
- No closed-model outputs anywhere in the training data. The synthetic part (D4) was generated by Qwen3.8-27B and kept only where Gemma-4-31B-it independently agreed, then spot-checked by a person.

### Training data

| Source | Questions | License | Attribution |
|---|---:|---|---|
| KLUE | 52,122 | CC BY-SA 4.0 | KLUE (Park et al., 2021), CC BY-SA 4.0 |
| KoSBi·SQuARe (NAVER) | 32,001 | MIT | KoSBi·SQuARe (Lee et al., 2023), NAVER, MIT |
| nari-decision synthetic decisions (D4) | 27,216 | Apache-2.0 (synthetic, generated and cross-checked by Apache-2.0 models) | Synthetic decisions generated with Qwen3.8-27B and cross-checked with Gemma-4-31B-it (Apache-2.0) |
| ABCD (Action-Based Conversations Dataset) | 16,000 | MIT | ABCD (Chen et al., 2021), ASAPP Research, MIT |
| MIRACL 한국어 | 15,110 | Apache-2.0 | MIRACL (Zhang et al., 2023), Apache-2.0 |
| Schema-Guided Dialogue (SGD) | 14,000 | CC BY-SA 4.0 | Schema-Guided Dialogue (Rastogi et al., 2020), Google, CC BY-SA 4.0 |
| KorNLI 학습 세트 (SNLI·MNLI 기계번역) | 14,000 | CC BY-SA 4.0 | KorNLI (Ham et al., 2020), Kakao Brain, CC BY-SA 4.0 |
| K-MHaS | 12,006 | CC BY-SA 4.0 | K-MHaS (Lee et al., 2022), CC BY-SA 4.0 |
| NoMIRACL 한국어 | 12,003 | Apache-2.0 | NoMIRACL (Thakur et al., 2024), Apache-2.0 |
| MASSIVE 1.1 한국어 (ko-KR) | 12,000 | CC BY 4.0 | MASSIVE (FitzGerald et al., 2022), Amazon, CC BY 4.0 |
| HelpSteer2 (NVIDIA) | 12,000 | CC BY 4.0 | HelpSteer2 (Wang et al., 2024), NVIDIA, CC BY 4.0 |
| KoBEST (SKT) | 11,485 | CC BY-SA 4.0 | KoBEST (Kim et al., 2022), SKT, CC BY-SA 4.0 |
| MKQA 한국어 | 10,000 | CC BY-SA 3.0 | MKQA (Longpre et al., 2021), Apple, CC BY-SA 3.0 |
| VitaminC | 10,000 | CC BY-SA 3.0 | VitaminC (Schuster et al., 2021), CC BY-SA 3.0 |
| CLINC150 (oos plus) | 10,000 | CC BY 3.0 | CLINC150 (Larson et al., 2019), CC BY 3.0 |
| HotpotQA (distractor) | 9,004 | CC BY-SA 4.0 | HotpotQA (Yang et al., 2018), CC BY-SA 4.0 |
| 3i4K | 8,000 | CC BY-SA 4.0 | 3i4K (Cho et al., 2018), CC BY-SA 4.0 |
| Civil Comments (TFDS/HF) | 7,000 | CC0 1.0 | Civil Comments (Borkan et al., 2019), Jigsaw, CC0 |
| 지자체 알림 문자와 부산 재난문자 | 6,161 | 공공데이터 이용허락범위 제한 없음 | 평택·안양·군포·용인·수원·남양주·동두천·과천·금천구 알림 문자, 부산광역시 재난문자, 공공데이터포털 |
| Aegis AI Content Safety 1.0 (NVIDIA) | 6,001 | CC BY 4.0 | Aegis 1.0 (Ghosh et al., 2024), NVIDIA, CC BY 4.0 |
| Amazon ESCI 학습 분할 | 6,000 | Apache-2.0 | Shopping Queries Dataset (Reddy et al., 2022), Amazon, Apache-2.0 |
| ShARC | 6,000 | CC BY-SA 3.0 | ShARC (Saeidi et al., 2018), CC BY-SA 3.0 |
| STAR | 6,000 | MIT | STAR (Mosig et al., 2020), Rasa, MIT |
| PAWS-X 한국어 | 6,000 | Free use, attribution requested (Google) | PAWS-X (Yang et al., 2019), Google |
| WinoGrande XL 학습 분할 | 6,000 | CC BY | WinoGrande (Sakaguchi et al., 2020), AI2, CC BY |
| Dynamically Generated Hate Speech (DynaHate) v0.2.3 | 6,000 | CC BY 4.0 | DynaHate (Vidgen et al., 2021), CC BY 4.0 |
| HoVer 학습 분할 | 6,000 | CC BY-SA 4.0, 코드 MIT | HoVer (Jiang et al., 2020), CC BY-SA 4.0 |
| Korean HateSpeech (kocohub / BEEP!) | 6,000 | CC BY-SA 4.0 | Korean HateSpeech Dataset (Moon et al., 2020), CC BY-SA 4.0 |
| GSM8K (OpenAI) | 5,877 | MIT | GSM8K (Cobbe et al., 2021), OpenAI, MIT |
| SQuAD 2.0 | 5,000 | CC BY-SA 4.0 | SQuAD 2.0 (Rajpurkar et al., 2018), CC BY-SA 4.0 |
| FaithDial | 5,000 | MIT | FaithDial (Dziri et al., 2022), MIT |
| MASSIVE 1.1 영어 (en-US, SLURP 원문) | 5,000 | CC BY 4.0 | MASSIVE (FitzGerald et al., 2022), Amazon, CC BY 4.0 |
| AQuA-RAT | 4,000 | Apache-2.0 | AQuA-RAT (Ling et al., 2017), Google DeepMind, Apache-2.0 |
| CommonsenseQA 2.0 | 4,000 | CC BY 4.0 | CommonsenseQA 2.0 (Talmor et al., 2021), AI2, CC BY 4.0 |
| CommonsenseQA 1.11 | 4,000 | MIT | CommonsenseQA (Talmor et al., 2019), MIT |
| Social IQa | 4,000 | CC BY 4.0 | Social IQa (Sap et al., 2019), AI2, CC BY 4.0 |
| Taskmaster-3 | 4,000 | CC BY 4.0 | Taskmaster-3 (Byrne et al., 2020), Google, CC BY 4.0 |
| MASSIVE-Agents 함수 정의 55개 | 4,000 | CC BY 4.0 | MASSIVE-Agents, Amazon, CC BY 4.0 |
| Fool Me Twice (FM2) | 4,000 | Apache-2.0 | Fool Me Twice (Eisenschlos et al., 2021), Google, Apache-2.0 |
| BLiMP | 4,000 | CC BY | BLiMP (Warstadt et al., 2020), CC BY |
| BANKING77 학습 분할 | 3,000 | CC BY 4.0 | BANKING77 (Casanueva et al., 2020), PolyAI, CC BY 4.0 |
| UCI SMS Spam Collection | 3,000 | CC BY 4.0 | SMS Spam Collection (Almeida & Gómez Hidalgo, 2011), UCI, CC BY 4.0 |
| PAWS (Wiki, labeled_final) | 3,000 | Free use, attribution requested (Google) | PAWS (Zhang et al., 2019), Google |
| QASC | 3,000 | CC BY 4.0 | QASC (Khot et al., 2020), AI2, CC BY 4.0 |
| 한국어 질문 쌍 (Question_pair) | 3,000 | MIT | Question_pair (songys), MIT |
| MKQA 영어 | 3,000 | CC BY-SA 3.0 | MKQA (Longpre et al., 2021), Apple, CC BY-SA 3.0 |
| Nazario 피싱 메일 모음 (2004~2025 메일함) | 3,000 | CC BY 4.0 | Phishing corpus by Jose Nazario, CC BY 4.0 |
| StrategyQA | 2,095 | MIT | StrategyQA (Geva et al., 2021), MIT |
| BoolQ | 2,000 | CC BY-SA 3.0 | BoolQ (Clark et al., 2019), Google, CC BY-SA 3.0 |
| CLAIR 사기 메일 모음 | 1,947 | CC BY-SA 3.0 US | CLAIR collection of fraud email (Radev, 2008), CC BY-SA 3.0 |
| 변호사시험 기출·선택형 최종정답 (법무부) | 1,824 | KOGL Type 1 (attribution) | 법무부, 변호사시험 기출문제 (공공누리 제1유형) |
| SIB-200 영어 (eng_Latn) | 648 | CC BY-SA 4.0 | SIB-200 (Adelani et al., 2024), CC BY-SA 4.0 |
| 법조윤리시험 기출·최종정답 (법무부) | 574 | KOGL Type 1 (attribution) | 법무부, 법조윤리시험 기출문제 (공공누리 제1유형) |
| SIB-200 한국어 | 84 | CC BY-SA 4.0 | SIB-200 (Adelani et al., 2024), CC BY-SA 4.0 |

## Limitations

- Calibration holds on data like the training mix. On a different distribution, re-fit the temperatures on a few hundred labeled examples of your own.
- Korean and English only. Other languages are untested.
- Ordinal (`score`) questions are the weakest type: 57.7% exactly right on held-out (91.9% within one step). Most of them are human ratings (HelpSteer2), where people also differ by a step. On the System One eval set they are poorly calibrated (ECE 0.118 on 99 questions).
- It judges what is in the state; it has no access to tools, the web or current facts.
- The guardrail questions cover PII, secrets and prompt injection; this is not a general content-safety classifier.
- Knowledge-heavy questions and long reading still favor larger models (same held-out questions): MMMLU-ko (1,000 questions) clef-flash (9B) 77.1%, JEV-9B 65.4% vs 55.7% here; Belebele-ko (898 questions) JEV-9B 90.0%, clef-flash (9B) 89.9% vs 84.6% here. Use the confidence to send such inputs to a larger model.
- On general-knowledge questions the confidence runs high: MMMLU-ko ECE 0.091 (mean confidence 67.6% at 58.5% accuracy). Re-fit the temperatures if that is your main use.
- The Ministry of Justice exams used for training (bar exam 1st–13th, legal ethics 1st–15th) are partly memorized (81.0% there vs 43.1% on the 2026 rounds); do not use them to evaluate this model.
- Weaker spots on held-out: Korean paraphrase detection (PAWS-X) 82.7% vs English (PAWS) 94.3%; knowledge (MMMLU-ko) 55.7%.

## License

Apache-2.0 for the weights and code. The training data includes CC BY and CC BY-SA sources; their attribution is listed in the table above.

The Korean national exam questions are public works of the Ministry of Justice released under KOGL Type 1 (공공누리 제1유형, attribution required); the attribution is in the table above.
