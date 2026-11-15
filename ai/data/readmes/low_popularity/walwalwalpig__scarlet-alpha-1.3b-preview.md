---
license: cc-by-nc-sa-4.0
language:
- ko
- en
pipeline_tag: text-generation
tags:
- pytorch
- causal-lm
- korean
- from-scratch
- nanochat
- preview
---

<p align="center">
  <img src="scarlet-alpha-1.3B.svg" alt="Scarlet alpha 1.3B" width="720">
</p>

# Scarlet alpha 1.3B preview

## 모델 설명 Model Description

Scarlet alpha 1.3B는 한국어 중심으로 처음부터 사전학습한 1.35B 파라미터 자기회귀 언어 모델입니다.

유해 요청 거절 학습을 하지 않은 연구용 미리보기라 유해하거나 사실과 다른 내용을 만들 수 있습니다.

*English summary: a 1.35B-parameter Korean-centric language model pretrained from scratch on about 22B tokens and chat
fine-tuned on about 60M tokens. Research preview, CC BY-NC-SA 4.0.*

| 하이퍼파라미터 | 값 |
|---|---|
| n_parameters | 1,354,760,266 (입력 임베딩과 출력 행렬 공유) |
| n_layers | 24 |
| d_model | 2,048 |
| d_ff | 5,888 (SwiGLU) |
| n_heads | 쿼리 16 / KV 4 (GQA) |
| d_head | 128 |
| n_ctx | 8,192 |
| n_vocab | 65,536 (바이트 수준 BPE 65,472 + 특수 토큰 64) |
| 위치 인코딩 | [RoPE](https://arxiv.org/abs/2104.09864), θ = 100,000, 헤드 차원 전체에 적용 |
| 어텐션 창 | 층마다 S·S·S·L 반복 (S = 2,048, L = 8,192), 마지막 층은 L |

## 학습 데이터 Training data

토큰 수는 Scarlet 토크나이저 기준입니다.

**사전학습 본 구간** (18.59B 토큰)

| 원천 | 토큰 | 링크 |
|---|---|---|
| FineWeb2 한국어 (교육성 점수 컷, 스팸·기계번역·미러 거르기) | 9.72B | [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) |
| FineMath 4+ | 2.30B | [HuggingFaceTB/finemath](https://huggingface.co/datasets/HuggingFaceTB/finemath) |
| StarCoderData Python (교육성 분류기 3점 이상) | 2.10B | [bigcode/starcoderdata](https://huggingface.co/datasets/bigcode/starcoderdata) |
| FineWeb-Edu (int_score ≥ 4) | 2.02B | [HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) |
| 나무위키 (2021-03 덤프) | 1.22B | [heegyu/namuwiki](https://huggingface.co/datasets/heegyu/namuwiki) |
| StarCoderData Jupyter | 0.77B | [bigcode/starcoderdata](https://huggingface.co/datasets/bigcode/starcoderdata) |
| 한국어 위키백과 | 0.44B | [HuggingFaceFW/finewiki](https://huggingface.co/datasets/HuggingFaceFW/finewiki) |

**annealing** (3.41B 토큰)

| 원천 | 토큰 |
|---|---|
| FineWeb2 한국어 (점수 상위 + 추가 문서) | 1.43B |
| StarCoderData Python·Jupyter (점수 상위) | 0.48B |
| FineMath 4+ (점수 상위) | 0.44B |
| 나무위키 (품질 선별) | 0.34B |
| 한국어·영어 지시·질문답·수학 공개 데이터, 규칙으로 만든 산수 글 | 0.32B |
| FineWeb-Edu (본 구간에 없던 문서) | 0.24B |
| 한국어 위키백과 (다시 보기) | 0.10B |
| 공개 대화 데이터를 Scarlet 대화 형식으로 렌더한 것 | 0.05B |

annealing의 지시·대화 데이터: PoSTMEDIA rosetta, KLUE MRC, kakaobrain/kor_nli, KETI-NLP/kor_qasc, solonsophy/winogrande-ko,
nlpai-lab/databricks-dolly-15k-ko, allenai tulu-3-sft-personas-instruction-following·dolmino-mix-1124(FLAN)·dolma3_dolmino_pool(RC QA),
NotoriousH2/gsm8k-ko, keunhyeung/dmath-ko-reasoning-dpo, philschmid/DMath, kikikara/ko-math, huggingface-KREW
KoCulture-Dialogues·korean-role-playing, smilegate-ai/korean_smile_style_dataset, maywell/koVast, mkd-chanwoo/keural-conversation-chatml-ko.

**대화 SFT** (약 60M 토큰): PoSTMEDIA rosetta(chat·지시 따르기·수학), maywell/koVast, coastral/korean-writing-style-instruct,
schneiderkamplab/dfm14-ko-synthetic-summary-rewrite-r1(원천: 한국어 위키백과·위키문헌), izlley2/llm0to1-sft-synth-ko,
Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2, angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k, KLUE MRC,
NotoriousH2/gsm8k-ko(train), keunhyeung/dmath-ko-reasoning-dpo, philschmid/DMath, kikikara/ko-math, KOREAson/YiSang-HighQuality,
werty1248/SFT-Reasoning-Ko-Translated, cshs-14-rne/OpenThoughts-Korean, OLAIR/Open-R1-Ko-SFT-v2.0, 직접 만든 틀 대화,
DeepSeek-V4.1-Flash로 생성하거나 다듬은 대화.

- **AI Hub**: 토크나이저 학습 표본에 AI Hub 데이터셋 9종(543, 591, 625, 653, 71343, 71627, 71631, 71632, 71694)이 일부 들어 있습니다.
  한국지능정보사회진흥원의 사업결과임. 가중치 학습(사전학습·annealing·SFT)에는 AI Hub 데이터를 쓰지 않았습니다.

## 학습 절차 Training procedure

- **사전학습**: 20,973 step × 2^20 토큰, 약 22.0B 토큰. 본 구간 데이터는 한 번만 봤고, annealing에서 그중 점수 상위 일부를 다시 봤습니다.
  - 본 구간(step 0–17,724): 문맥 512 → 1,024 → 2,048, RTX 5090 4장(step 11,100부터 8장).
  - annealing(step 17,724–20,973): 문맥 4,096(마지막 400 step은 8,192), RTX 5090 4장.
  - 학습률은 warmup 40 step 뒤 전체의 65% 구간에서 최댓값의 5%까지 줄였습니다. 옵티마이저는 Muon(행렬)·AdamW(임베딩·스칼라), Linear는 FP8입니다.
- **대화 SFT**: 457 step, 약 60M 토큰, RTX PRO 6000 2장. 생각(think) 켬·끔, 계산기 도구 호출, 시스템 프롬프트, 최대 8K 토큰의 다중 턴 대화를 포함합니다.

## 사용법 How to use

```bash
pip install -r requirements.txt
python scarlet.py --model-dir .               # 터미널 대화 (생각 끔)
python scarlet.py --model-dir . --think on    # 생각 켬
```

```python
import scarlet
model, tok = scarlet.load(".")                 # CUDA면 bf16, 그 밖에는 fp32
reply = scarlet.chat(model, tok, [{"role": "user", "content": "광합성을 세 문장으로 설명해 줘."}], think="off")
print(reply["content"])
```

Transformers 구조가 아니라서 `AutoModelForCausalLM`으로는 불러올 수 없고, `scarlet.py`(PyTorch 한 파일)로 불러옵니다.
대화 형식은 [chat_format.md](chat_format.md)에 있습니다.
권장 생성 설정: temperature 0.7, top-k 50, 반복 벌점 1.1(최근 64토큰). `<|assistant_end|>`·`<|bos|>`·`<|user_start|>`에서 멈춥니다.

## 평가 결과 Evaluation results

평가 코드와 문구는 공개하지 않아서 외부에서 그대로 재현할 수는 없습니다. 조건을 아래에 적습니다.

### 사전학습 체크포인트: 0-shot 객관식

공개한 모델의 SFT 직전 체크포인트(base, step 20,973)로 잰 값입니다. 이 base 가중치는 공개하지 않습니다. annealing에 지시·QA·수학·대화
공개 데이터(약 0.37B 토큰)가 들어 있어서, 순수 사전학습 모델끼리의 비교는 아닙니다.

![사전학습 체크포인트의 0-shot 객관식 acc. Scarlet base는 COPA·HAE-RAE·CLIcK에서 gemma-3-1b-pt보다 높고, HellaSwag는 비슷하며, SentiNeg는 polyglot-ko-1.3b가 앞서고, WiC·KMMLU는 모든 모델이 찬스 근처입니다. BoolQ는 학습 데이터와 겹쳐 뺐습니다.](base_0shot.png)

- **방법**: 0-shot으로 선택지마다 로그 우도를 구해 고릅니다. 같은 러너, 같은 문구, fp32로 전체 문항을 쟀습니다.
  polyglot-ko-1.3b만 KoBEST를 Mac MPS(fp32, 문맥 상한 2,048)에서 따로 쟀습니다.
- **문구**: HAE-RAE·CLIcK·KMMLU는 보기 글자 대신 보기 내용을 직접 채점하는 자체 cloze 문구입니다. 공식 하네스의 보기 글자 형식과 달라서
  공개된 다른 점수와 직접 비교할 수 없습니다. HAE-RAE의 형식은 Scarlet 학습 초기 체크포인트가 보기 글자 형식에서 찬스였기 때문에
  정했습니다. HAE-RAE는 생성형(denoising)을 뺀 객관식 11개 하위 과제입니다.
- **지표**:
  - **macro-F1**: KoBEST 공식 지표입니다.
  - **acc**: 선택지 로그 우도 합이 가장 큰 것을 고릅니다. 길이 정규화를 하지 않습니다.
  - **acc_norm**: 로그 우도를 선택지 글자 수(앞 공백 포함)로 나눠 고릅니다. 토크나이저가 달라도 비교할 수 있습니다.
- **러너 확인**: 같은 러너로 잰 polyglot-ko-1.3b의 0-shot F1은 그 모델 카드 값과 COPA·BoolQ·SentiNeg에서 같고(0.7196·0.3552·0.6790),
  WiC는 0.3276 대 0.3297입니다. HellaSwag만 카드 값(0.5247)과 달라서 acc·acc_norm도 함께 적습니다.

**[KoBEST](https://huggingface.co/datasets/skt/kobest_v1) (macro-F1, 0-shot)**

| 모델 | 파라미터 (비임베딩) | 학습 토큰 | COPA | HellaSwag | BoolQ† | SentiNeg | WiC |
|---|---|---|---|---|---|---|---|
| **Scarlet base (step 20,973, 미공개)** | **1.35B (1.22B)** | **22B** | **0.7414** | **0.3996** | **0.5502** | **0.3478** | **0.3280** |
| [EleutherAI/polyglot-ko-1.3b](https://huggingface.co/EleutherAI/polyglot-ko-1.3b) | 1.3B (1.21B) | 213B | 0.7196 | 0.4013 | 0.3552 | 0.6790 | 0.3276 |
| [google/gemma-3-270m](https://huggingface.co/google/gemma-3-270m) | 0.27B (0.10B) | 6T | 0.5499 | 0.3646 | 0.3421 | 0.3395 | 0.3280 |
| [google/gemma-3-1b-pt](https://huggingface.co/google/gemma-3-1b-pt) | 1B (0.70B) | 2T | 0.6651 | 0.4073 | 0.3662 | 0.3457 | 0.4206 |

† BoolQ는 지문 대부분이 학습 데이터와 겹쳐 비교에 쓰지 않습니다(아래 "오염"). 학습 토큰은 토크나이저마다 단위가 다르고,
Gemma 3는 큰 모델의 지식 증류로 사전학습했습니다.

**KoBEST (acc / acc_norm, 0-shot)**

| 모델 | COPA (1,000) | HellaSwag (500) | BoolQ† (1,404) | SentiNeg (397) | WiC (1,260) |
|---|---|---|---|---|---|
| 찬스 | 0.50 | 0.25 | 0.50 | 0.50 | 0.50 |
| **Scarlet base (미공개)** | **0.742 / 0.783** | **0.402 / 0.536** | **0.577 / 0.498** | **0.466 / 0.466** | **0.488 / 0.529** |
| polyglot-ko-1.3b | 0.720 / 0.754 | 0.406 / 0.520 | 0.499 / 0.500 | 0.690 / 0.690 | 0.487 / 0.517 |
| gemma-3-270m | 0.551 / 0.565 | 0.366 / 0.452 | 0.503 / 0.496 | 0.464 / 0.464 | 0.488 / 0.511 |
| gemma-3-1b-pt | 0.666 / 0.707 | 0.410 / 0.546 | 0.505 / 0.498 | 0.499 / 0.499 | 0.490 / 0.511 |

**한국어 지식 (acc / acc_norm, 0-shot, 자체 cloze 문구)**

| 모델 | [HAE-RAE 1.1](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.1) (3,606) | [CLIcK](https://huggingface.co/datasets/EunsuKim/CLIcK) (1,995) | [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) (35,030) |
|---|---|---|---|
| 찬스 | 0.200 | 0.244 | 0.250 |
| **Scarlet base (미공개)** | **0.338 / 0.318** | **0.353 / 0.412** | **0.223 / 0.241** |
| gemma-3-270m | 0.257 / 0.231 | 0.225 / 0.261 | 0.209 / 0.227 |
| gemma-3-1b-pt | 0.287 / 0.270 | 0.294 / 0.348 | 0.217 / 0.237 |

- **Gemma 3 1B보다 높은 과제**: COPA·HAE-RAE·CLIcK. acc와 acc_norm 모두 95% 신뢰구간(Wilson)이 겹치지 않습니다.
  polyglot-ko-1.3b는 HAE-RAE·CLIcK를 재지 않았습니다.
- **같은 수준인 과제**: HellaSwag는 Gemma 3 1B·polyglot-ko-1.3b와 같은 수준입니다.
- **약한 과제**: SentiNeg는 찬스 수준이고(397문항 중 366문항을 같은 답으로 고름), polyglot-ko-1.3b(0.690)가 크게 앞섭니다.
- **가르지 못하는 과제**: WiC는 잰 모델 모두 찬스 근처이고, Scarlet은 모든 문항에 같은 답을 골랐습니다. KMMLU는 세 모델 모두
  찬스(0.25)보다 낮아서 이 문구로는 재지 못합니다.
- **오염**: Scarlet 학습 데이터(본 구간·annealing)와 문항의 13-gram 겹침을 대조했습니다.
  - BoolQ는 지문이 위키백과 글이라 1,404문항 중 1,025문항이 많이 겹칩니다(13-gram 절반 이상). 겹친 문항을 빼면(379문항)
    acc 0.583 대 gemma-3-1b-pt 0.533으로 신뢰구간이 겹치고, acc_norm은 0.470 대 0.472입니다. 그래서 BoolQ는 비교에 쓰지 않습니다.
  - HAE-RAE·CLIcK는 13-gram이 하나도 겹치지 않는 문항(2,013·1,382문항)만 봐도 acc 0.407·0.389 대 gemma-3-1b-pt 0.325·0.315로
    결론이 같습니다.

### 공개 모델 SFT: 생성

greedy 디코딩, system 프롬프트 없음, 같은 생성 상한(각 모델의 토큰 기준)입니다. Gemma는 자기 대화 틀과 fp32로, Scarlet은 bf16·생각 끔·
내장 계산기 켬으로 돌렸습니다(Gemma에는 도구가 없습니다). IFEval-Ko 전체와 GSM8K-ko 중 200문항은 SFT를 만들 때 탐침으로도 썼습니다.

![공개 모델과 Gemma 3 instruct의 IFEval-Ko 문항 엄격과 GSM8K-ko 정확도. GSM8K-ko는 gemma-3-1b-it와 차이가 유의하지 않고, IFEval-Ko는 0.06 낮으며, 두 벤치 모두 gemma-3-270m-it보다 높습니다.](sft_generation.png)

| 모델 | 사후학습 | IFEval-Ko 문항 엄격 | IFEval-Ko 지시 단위 | GSM8K-ko (384) |
|---|---|---|---|---|
| **Scarlet alpha 1.3B preview (this)** | **SFT 한 번, 약 60M 토큰** | **0.284** | **0.387** | **0.198** |
| [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it) | 증류 + RL | 0.193 | 0.291 | 0.018 |
| [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 증류 + RL | 0.342 | 0.426 | 0.214 |
| *반복 벌점 1.1(최근 64토큰)을 건 경우* | | | | |
| Scarlet alpha 1.3B preview | | 0.272 | 0.368 | 0.185 |
| gemma-3-270m-it | | 0.211 | 0.302 | 0.031 |
| gemma-3-1b-it | | 0.360 | 0.441 | 0.188 |

- **IFEval-Ko**:
  - 데이터: [allganize/IFEval-Ko](https://huggingface.co/datasets/allganize/IFEval-Ko) 342문항, 생성 상한 1,024토큰입니다.
  - 채점: 자체 채점기입니다(allganize가 제공하는 하네스 과제가 아님). Google IFEval의 엄격 판정을 옮기되, 응답 언어는 문자 체계로,
    단어·문장 수와 금지어는 한국어에 맞게 바꿔 판정합니다.
  - 문항 엄격은 모든 지시를 통과한 문항의 비율이고, 지시 단위는 지시 하나하나의 통과율입니다.
- **GSM8K-ko**:
  - 데이터: [NotoriousH2/gsm8k-ko](https://huggingface.co/datasets/NotoriousH2/gsm8k-ko) test입니다. annealing에 test의 70%가 들어갔으므로 나머지 384문항만 씁니다. SFT는 train만 썼습니다.
  - 채점: 답의 마지막 숫자가 정답과 같은지 봅니다. 생성 상한은 512토큰입니다.
  - 계산기를 끄고 도구 금지 system 프롬프트를 넣으면 Scarlet은 0.190입니다.
- **해석**:
  - GSM8K-ko: gemma-3-1b-it와의 차이(−0.016)가 통계적으로 유의하지 않습니다(같은 문항 짝 비교 95% 신뢰구간 −0.07에서 +0.03).
    SFT 탐침으로 쓰지 않은 184문항만 봐도 0.245 대 0.250입니다.
  - IFEval-Ko: 이 채점기 기준 문항 엄격이 0.06–0.09 낮습니다. 특히 "…로 끝내라" 지시가 약합니다(15개 중 1개 대 7개).
- **반복**: 반복 벌점 없이 생성하면 IFEval-Ko 답의 43%가 1,024토큰 상한에 닿고, 그중 73%(147개 중 107개)는 같은 문장을 세 번 이상
  되풀이합니다. 벌점 1.1이면 상한 도달이 9%로 줄지만 점수는 오르지 않습니다.

## 한계와 편향 Limitations and Biases

이 모델은 다음 토큰 예측으로 학습했습니다. 가장 사실에 맞는 답이 아니라 통계적으로 그럴듯한 답을 냅니다. 사회적으로 받아들이기 어렵거나
불쾌한 내용을 만들 수 있으니, 사람이 검토하거나 별도 필터를 두기를 권합니다.

## 인용 Citation

```bibtex
@misc{scarlet2026alpha,
  title  = {Scarlet alpha 1.3B (preview)},
  author = {Walwalwalpig},
  year   = {2026},
  note   = {Research preview},
  url    = {https://huggingface.co/walwalwalpig/scarlet-alpha-1.3b-preview}
}
```

## 라이선스 Licensing

- 가중치·토크나이저: **CC BY-NC-SA 4.0** ([LICENSE](LICENSE))
- 코드(`scarlet.py`): **MIT** ([LICENSE-CODE](LICENSE-CODE)), nanochat(MIT, Andrej Karpathy)에서 나왔습니다.
- 로고(`scarlet-alpha-1.3B.svg`): 위 라이선스에 포함되지 않습니다. 모든 권리 보유.

## 감사의 말 Acknowledgement

- 학습 코드는 Andrej Karpathy의 [nanochat](https://github.com/karpathy/nanochat)에서 출발했습니다.
- 데이터를 공개해 준 분들께 감사드립니다:
  - Hugging Face(FineWeb2·FineWeb-Edu·FineMath·FineWiki)
  - BigCode(StarCoderData)
  - 나무위키와 위키백과·위키문헌 기여자
  - 위에 적은 공개 데이터셋 제작자들
