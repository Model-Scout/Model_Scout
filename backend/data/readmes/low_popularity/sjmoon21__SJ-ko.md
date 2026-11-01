---
language:
  - ko
  - en
license: cc-by-nc-sa-4.0
library_name: gguf
tags:
  - korean
  - gpt
  - from-scratch
  - educational
  - gguf
  - tool-use
pipeline_tag: text-generation
---

# SJ-ko

A 75M parameter Korean GPT built and trained from scratch.
Current release: `SJ-0.7.1simft` (`sj-0.7.1simft.gguf`).
The earlier 11M releases `sj-0.5.6simf.gguf` and `sj-0.5.1si.gguf` are kept in `legacy/`.

In training: a ~400M-parameter successor (run28 — 26 layers · 1024 dim, 32k byte-fallback BPE, 7.6B-token Korean/English/code corpus)
on Kaggle T4×2. It is not published yet; the training history below is updated as runs finish.

No Hugging Face Transformers, no existing training framework. The BPE tokenizer,
attention, training loop, and GGUF converter were all written by hand. This is an
educational project, not a production model. It invents facts and can fall into
repetition loops.

- Author: Sungjin Moon, Seoul National University, Department of Physics & Astronomy, Physics
- Contact: mongsil88@snu.ac.kr

## Specification

| | |
|---|---|
| Parameters | 75.32M (14.7% embeddings). The GGUF counts 75.61M: llama.cpp needs 565 extra byte-sequence tokens, whose embedding rows copy `<unk>` |
| Architecture | 20 layers · 512 dim · 8 heads · RMSNorm · RoPE · SwiGLU · QK-Norm · tied embeddings |
| GGUF layout | `qwen3` (the model's layout matches Qwen3's; the converter only reorders RoPE pairs, so no weights change) |
| Context | 1024 tokens (≈2,450 characters) |
| Vocabulary | 21,626 (byte-fallback BPE trained from scratch, 2.40 characters per token, digits kept as single tokens) |
| Hardware | Colab T4 → Kaggle T4×2 (pre-training), T4 (SFT) |
| Pre-training | 1.65B tokens × 1.03 epochs · 26.3억 (2.63B) characters of unique text |
| SFT | 55,016 training pairs × 2.87 epochs · 71 minutes |

The GGUF was checked against the PyTorch model: greedy generation matches token
for token on 9 of 9 test prompts (Ollama 0.33.3).

## Usage (Ollama)

```bash
ollama create sj-0.7.1simft -f Modelfile
ollama run sj-0.7.1simft
```

For the previous 11M release, download `legacy/sj-0.5.6simf.gguf` and `legacy/Modelfile-0.5.6simf` into one folder and run
`ollama create sj-0.5.6simf -f Modelfile-0.5.6simf`.

The bundled `Modelfile` carries settings that are required. Without them the
model echoes the question back or never stops generating.

```
TEMPLATE """{{- range .Messages }}{{- if eq .Role "user" }}<|user|>{{ .Content }}<|assistant|>{{- else }}{{ .Content }}<|endoftext|>{{- end }}{{- end }}"""
PARAMETER stop "<|endoftext|>"
PARAMETER stop "<|user|>"
```

The template walks `.Messages`, so multi-turn conversations work through
`/api/chat`. Building the prompt yourself with `raw: true` does not work — the
special tokens are then treated as plain text rather than control tokens.

### Tools

This release was fine-tuned to call three tools — `calc`, `clock`, and `search`
(BM25 over a local document index) — through the special tokens `<|tool|>`,
`<|end|>`, and `<|result|>`. In this "forced" variant the calling program, not
the model, decides when a tool is needed and writes the tool token; the model then
fills in the arguments (for `calc`) and answers from the tool's result.

```
<|user|> question <|assistant|> <|tool|> name args <|end|> <|result|> result <|end|> answer <|endoftext|>
```

Plain `ollama run` never inserts a tool token, so there the model answers from
its own weights only. Tool calls need a harness that runs this loop; the harness
is not part of this repository.

## Self-hosting the chat UI

`serve_ollama.py` is a dependency-free chat server (Python standard library only,
no PyTorch). It talks to a local Ollama instance and streams responses.

```bash
OLLAMA_HOST=127.0.0.1:11434 ollama serve &
ollama create sj-0.7.1simft -f Modelfile
python3 serve_ollama.py --model sj-0.7.1simft --host 0.0.0.0 --port 3000
```

Keep Ollama bound to localhost. Its API has no authentication and allows model
deletion, so it must never be exposed to the internet.

## Training data

Pre-training (corpus v5, 2.63B unique characters; share of the training stream, with repeats)

| Source | Repeats | Share |
|---|---|---|
| AI Hub, 029.대규모 구매도서 기반 한국어 말뭉치 데이터 | 2 | 42.3% |
| [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) 20231101 en (CC BY-SA) | 1 | 21.0% |
| [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) 20231101 ko (CC BY-SA) | 2 | 18.0% |
| 나무위키 via [heegyu/namuwiki-extracted](https://huggingface.co/datasets/heegyu/namuwiki-extracted) (2021-03-01 dump, CC BY-NC-SA 2.0 KR) | 1 | 10.3% |
| Synthetic arithmetic, generated in Python with guaranteed-correct answers | 2 | 3.7% |
| AI Hub, 121.한국어 성능이 개선된 초거대AI 언어모델 개발 및 데이터 — YouTube subtitle subset | 3 | 2.5% |
| AI Hub, 018.논문자료 요약 데이터 — abstracts | 1 | 2.0% |
| AI Hub, 121 — 국립국어원 grammar Q&A subset | 1 | 0.2% |

Supervised fine-tuning (55,588 pairs loaded; 72 longer than 1,024 tokens dropped, 499 held out for validation)

| Source | Count |
|---|---|
| AI Hub, 121.한국어 성능이 개선된 초거대AI 언어모델 개발 및 데이터 (RLHF) | 32,275 |
| Tool-use pairs: `search` 5,006 (question-answer pairs over Korean Wikipedia passages, generated by DeepSeek) · `calc` 4,588 · `clock` 500 · no-tool contrast 175 | 10,269 |
| Synthetic atomic-fact question-answer pairs (900 facts × 8 phrasings, generated by DeepSeek) | 7,200 |
| Synthetic multi-turn (4,000 concatenated pairs + 908 follow-up turns generated by DeepSeek) | 4,908 |
| Synthetic identity pairs | 936 |

### Attribution

This model was developed using the following datasets provided by AI Hub
(https://aihub.or.kr):

- 018.논문자료 요약 데이터
- 029.대규모 구매도서 기반 한국어 말뭉치 데이터
- 121.한국어 성능이 개선된 초거대AI 언어모델 개발 및 데이터

It was also trained on 나무위키 (namu.wiki) text, licensed CC BY-NC-SA 2.0 KR,
and on Wikipedia text, licensed CC BY-SA.

No original data is included in this repository, and none is redistributed.

## License

CC BY-NC-SA 4.0 for `sj-0.7.1simft.gguf`, because its training data includes
나무위키 text under a NonCommercial-ShareAlike license. Non-commercial use only;
derivatives must carry the same license.

The earlier 11M releases (`legacy/sj-0.5.6simf.gguf`, `legacy/sj-0.5.1si.gguf`) did not use
나무위키 and were published under MIT; they remain available under MIT.

The terms of the original training data remain with their respective providers.

## Training history

Every run from the first character-level bigram to the current release. Loss per
char (nats per character) is the only column comparable across runs — token loss
depends on the tokenizer, which changed several times. Notes are the author's own
working notes, in Korean.

| Run | Version | Method | Data | Train tokens | Epochs | Wall clock | Params | Tokens/param | Loss per char | Notes (Korean) |
|---|---|---|---|---|---|---|---|---|---|---|
| run01 | 0.1.0p | pre-training | 커뮤니티 크롤링 298만자 | 2.84M | 6.5 | 54분 | 5.45M | 3.39 | - | 크롤링 데이터 기반 pre-training. char-level tokenize. clien 데이터가 대부분이라, 커뮤니티 말투이긴 한데 아저씨 말투여서 실패. 추가로, char-level이어서 인지 한자가 너무 많이 등장하는 문제도 존재. step 3000/6000에서 수동 중단 |
| run02 | 0.2.0p | pre-training | 웹소설 716만자 | 6.80M | 4.2 | 94.8분 | 5.22M | 5.47 | 2.1032 | 웹소설 3권 데이터 활용. char-level tokenized. val split이 격차가 −0.15로 편향된 결함 발견 |
| run03 | 0.2.1p | pre-training | 웹소설 714만자 | 3.75M | 4.10 | 51.6분 | 5.82M | 2.64 | 2.3095 | BPE tokenizer로 변경(vocab 4096). 웹 소설 문체여서 대괄호나 너무 고유명사들이 많이 나오는 문제가 있었음. 데이터 교체필요. 회차 단위 분할 + &lt;&#124;endoftext&#124;&gt; 도입 |
| run04 | 0.3.0p | pre-training | AI hub 도서 1.79억자 | 91.4M | 1.01 | 312.7분 | 6.15M | 15.01 | 2.2369 | AI hub 도서 데이터 도입(vocab 5366). 영어, 기호 아예 존재하지 않는 문제 있음. 문단이 저작권 보호로 무작위 섞여 있어 논리 전개 학습 불가. 참고문헌 음차 오염 1.7%. 영문/한글 위키 도입 예정 |
| run05 | 0.3.1s | sft | AI hub RLHF 21,650쌍 | 6.30M | 1.04 | 58.7분 | 6.25M | 1.05 | 1.5161 (sft) | 첫 sft 진행. 나름 성공적 — EOT 학습 성공(질문 유형별 길이 조절까지). 첫 gguf 파일 생성, `ollama run` 확인. bias 이슈로 인한 변환 과정 약 3% 손실 |
| run06 | 0.3.2si | sft-identity | SFT + 정체성 350쌍 | 6.31M | 1.04 | 66.5분 | 6.25M | 1.05 | 1.4776 (sft) | 모델 정체성 주입 시도했지만 실패. 고유 쌍당 노출이 적어 실패한 것으로 확인 |
| run07 | 0.3.3si | sft-identity | SFT + 정체성 1,170쌍 | 6.33M | 1.00 | 59.8분 | 6.25M | 1.01 | 1.4762 (sft) | 모델 정체성 주입 2트. 사본을 늘려 노출 횟수 증가. 과잉발화 문제가 있기는 함 |
| run08 | 0.4.0p | pre-training | AI hub 도서 + 한/영 위키 2.96억자 | 146.9M | 1.00 | 319.2분 | 6.10M | 24.08 | 2.0069 | 6층 구조. 음차 제거, 위키로 영어와 기호 확보, vocab은 오히려 감소(압축률 증가), bias false로 변경해서 gguf에서 손실 나지 않도록 조치. |
| run09 | 0.4.1si | sft-identity | SFT 33,741쌍 + 정체성 936쌍 | 10.49M | 3.05 | 87.4분 | 6.20M | 5.16 | 1.2665 (sft) | 6층 구조 identity 포함 sft. 영문, 기호가 포함되었기 때문에 활용 가능한 SFT 쌍이 증가. 정체성은 사본 6개 x 3 epoch로 노출 18회. |
| run10 | 0.4.2p | pre-training | AI hub 도서 + 한/영 위키 2.96억자 | 146.9M | 1.00 | 318.8분 | 6.16M | 23.85 | 1.9529 | 6층 구조. minimind 참고하여 RoPE 적용한 v2 아키텍쳐 도입. run08과 데이터는 동일 |
| run11 | 0.4.3si | sft-identity | SFT 33,741쌍 + 정체성 936쌍 | 10.49M | 1.99 | 43.0분 | 6.16M | 3.39 | 1.2602 (sft) | v2 아키텍쳐 적용 identity 포함 sft. gguf 생성 엔진 수정 |
| run12 | 0.4.4p | pre-training | AI hub 도서 + 한/영 위키 2.96억자 | 146.9M | 1.00 | 400.2분 | 10.97M | 13.39 | 1.8823 | 12층 v2 아키텍쳐 모델. 층수 증가로 인한 파라미터 증가. 파라미터 +78%인데 시간은 +26% |
| run13 | 0.4.5si | sft-identity | SFT 33,741쌍 + 정체성 936썽 | 10.49M | 2.70 | 161.2분 | 10.98M | 2.58 | 1.1243 (sft) | v2 아키텍쳐 적용 12층 sft. 과잉발화 문제 완화. 조기종료 |
| run14 | 0.5.0p | pre-training | AI hub 도서 + 한/영 위키 + 합성 산술 3.10억자 | 160.6M | 2.03 | 1,133.8분 | 10.97M | 29.72 | 1.7796 | 숫자 한 자리씩 토크나이징 + 합성 산술 5% 도입. block 128→256. 프롬프트가 \n으로 시작할 때만이기는 하지만 4자리 덧셈 받아올림 완주 100% |
| run15 | 0.5.1sim | sft-identity | SFT 32,275 + 정체성 936 + 다중턴 4,908 + 산술 2,000 | 13.1M | 3.01 | 645.2분 | 10.97M | 3.59 | 1.0948 (sft) | 다중 턴 도입 성공. 기존에는 처음 물은 질문에 관한 답변만 제공하던 문제 해결. 기존 SFT 데이터셋에서 답변=질문인 데이터셋 발견 후 수정. 산술 문답 데이터 적용. RoPE 도입 후 부작용 없는 block 증가 |
| run16 | 0.5.2d | dpo | on-policy DPO 2,435쌍 (rep<=1) | 1.76M | 1.00 | 31.7분 | 10.97M | 0.16 | - | DPO 첫 시도. 반복 감소를 목표. 하지만 모든 지표 악화(반복률 10.6→20.0%, 길이 374→572자, EOT 97→87.6%, unk 25.6→39.4%. 정체성 완전 소실, 토큰 파괴) |
| run17 | 0.5.3d | dpo | on-policy DPO 2,435쌍 (rep<=1) | 1.76M | 1.00 | 31.5분 | 10.97M | 0.16 | - | β를 5배로. 마진 억제, 정체성 보존. 그러나 반복률 22.4%로 최악. 토큰 파괴는 잔존 |
| run18 | 0.5.4d | dpo | on-policy DPO 2,435쌍 (rep<=1) | 1.76M | 1.00 | 32.4분 | 10.97M | 0.16 | - | 마진 36으로 가장 잘 묶임. 셋 중 제일 낫지만 원본보다는 나쁨. DPO 결론: β 문제가 아니라 데이터 구조 문제. 긴 내용 선호로 바뀌면서 채울 내용이 없어 반복으로 떼운 듯 |
| run19 | 0.5.5sf | sft-facts | 사실 QnA 7,200 + 정체성 936 | 0.14M | 2.95 | 44.0분 | 10.97M | 0.04 | 0.1276 (sft) | run15 위에 추가로 sft 얹은 방식. deepseek 생성 사실 900개를 질문 8가지씩 SFT. 훈련에 안 쓴 표현으로 물어도 핵심어 44.3% / 완전 일치 29.0% (이전 8.0% / 0.0%). 하지만, 산술 10/20 → 0/20, 일반 서술 답변이 한 문장으로 붕괴. 전체 sft 재실행 예정 |
| run20 | 0.5.6simf | sft-full | SFT 32,275 + 정체성 936 + 다중턴 4,908 + 산술 2,000 + 사실 7,200 | 13.1M | 2.99 | 349.1분 | 10.97M | 3.56 | 1.0549 (sft) | run19의 대량 망각을 사실 비중 88%→15.2%로 낮춰 해결. 길이 버킷팅(풀 단위 정렬) 도입으로 12.7시간→5.8시간. 남은 결함은 사실 간 혼선(한라산 답에 독도 설명이 붙음)과 다중 턴 내용 붕괴. |
| run21 | 0.5.7p | pre-training(이어서) | AI hub 도서 + 한/영 위키 + 합성 산술 3.10억자 | 160.6M | 0.19 | 151.6분 | 10.97M | 2.80 | 1.7375 | run14에서 이어서 문맥 256→512. 복사 능력 전 구간 개선되었지만 RAG 사용 가능 수준에는 미달 → 문맥 1024로 다시 pre-training 예정 |
| run22 | 0.6.0p | pre-training | 나무위키 + AI hub 도서 + 한/영 위키 + 합성 산술 7.64억자 | 353.6M | 1.22 | 4,279.1분 | 22.34M | 19.0 | 1.6328 | 나무위키 도입 + 토크나이저 v4 + 22M 확장. 코퍼스 3.10→7.64억자(나무위키 33.6% / 도서 24.1% / 영문위키 22.1% / 한국어위키 17.5% / 산술 2.7%, 한국어 75.2%). vocab 5,206→14,241로 자/토큰 1.881→2.107, unk 0.320→0.054%. 문맥 256→1024, 12층 d256→14층 d320 |
| run23 | 0.6.1simf | sft-full | SFT 32,275 + 정체성 936 + 다중턴 4,908 + 산술 2,000 + 사실 7,200 | 11.8M | 3.00 | 475.8분 | 22.34M | 1.58 | 1.0253 (sft) | run22 기반 전체 SFT. 같은 데이터·시드로 run20 대비 사실 29→39.5%로 개선, unk 20.5→0.5%. run20의 사실 간 혼선 현상 감소. parameter count 올린 효과 확인. 아직 RAG은 거의 불가능. 이는 "찾는" 방법에 대한 학습이 없기 때문으로 판단, sft 재실시 예정 |
| run24 | 0.6.2simfr | sft-rag | SFT 32,275 + 정체성 936 + 다중턴 4,908 + 산술 2,000 + 사실 7,200 + RAG 5,006 | 11.9M | 3.00 | 885.6분 | 22.34M | 1.60 | 1.0301 (sft) | Deepseek 생성 RAG-SFT 5,006쌍(9.6%) 추가. 700자 문단에서 맞는 문장을 찾아 발췌하기 시작함. 하지만복합 답 부분 발췌와 정답 찾은 뒤 반복 루프 문제 있음 |
| run25 | 0.7.0p | pre-training | 코퍼스 v5 — 도서·나무위키·한/영 위키·유튜브 자막·산술·논문·국어원 8종 26.3억자 (출처별 반복 포함 39.6억자) | 1,704M | 1.03 | ~921분 | 75.32M | 22.62 | 1.2883 | notes/22 B안. 토크나이저 v5(바이트 폴백, vocab 21,621)로 unk 0. 20층 d512, QK-Norm·z-loss·WSD·fp16 AMP·torch.compile 도입. Colab T4 2,137스텝(13.4 s/step) → Kaggle T4×2 DDP 4,363스텝(6.2 s/step). 글자당 loss 1.633→1.288(−21%). 문장·문단 구조와 인용부호는 잡혔으나 사실은 지어내고 base 특유의 반복 루프 있음 — SFT·RAG 몫 |
| run26 | 0.7.1simft (forced) | sft-tool-forced | SFT 32,275 + 정체성 792 + 다중턴 4,908 + 사실 7,200 + 도구 10,269 (search 5,006 · calc 4,588 · clock 500 · 대조 175) | 11.2M | 2.87 | 71.1분 | 75.32M | 0.43 | 0.7281 (sft) |  |
| run27 | 0.7.1simft (auto) | sft-tool-auto | SFT 32,275 + 정체성 792 + 다중턴 4,908 + 사실 7,200 + 도구 10,269 (search 5,006 · calc 4,588 · clock 500 · 대조 175) | 11.4M | 2.87 | 73.7분 | 75.32M | 0.43 | 0.7120 (sft) |  |
