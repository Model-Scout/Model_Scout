---
license:
- apache-2.0
- mit
- cc-by-nc-4.0
language:
- ko
- en
task_categories:
- text-generation
size_categories:
- 100K<n<1M
pretty_name: Perdix SFT Data
tags:
- sft
- instruction-tuning
- chatml
- conversational
- korean
configs:
- config_name: kullm-v2
  data_files: raw/kullm-v2/kullm-v2.jsonl
- config_name: koalpaca
  data_files: raw/oki/koalpaca.json
- config_name: OIG-smallchip2-ko
  data_files: raw/oki/OIG-smallchip2-ko.json
- config_name: korquad-chat
  data_files: raw/oki/korquad-chat.json
- config_name: everyday-conversations
  data_files: raw/smoltalk/data/everyday-conversations/train-*.parquet
- config_name: smol-magpie-ultra
  data_files: raw/smoltalk/data/smol-magpie-ultra/train-*.parquet
- config_name: smol-constraints
  data_files: raw/smoltalk/data/smol-constraints/train-*.parquet
- config_name: smol-rewrite
  data_files: raw/smoltalk/data/smol-rewrite/train-*.parquet
- config_name: smol-summarize
  data_files: raw/smoltalk/data/smol-summarize/train-*.parquet
- config_name: metamathqa-50k
  data_files: raw/smoltalk/data/metamathqa-50k/train-*.parquet
- config_name: numina-cot-100k
  data_files: raw/smoltalk/data/numina-cot-100k/train-*.parquet
---

# Perdix-SFT-Data

[Perdix-1.1B-Instruct](https://huggingface.co/prismdata/Perdix-1.1B-Instruct)를 만들 때 쓴 지시 미세조정(SFT) 데이터입니다. 두 부분으로 되어 있습니다.

- `raw/` — 공개 대화 데이터셋 세 곳에서 받은 원본 파일. 내용은 손대지 않았습니다.
- `packed/` — 원본을 골라 ChatML로 토큰화하고 loss 마스크를 붙인 결과. 실제 학습 입력입니다.

The conversation data used to supervised-finetune Perdix-1.1B-Instruct: unmodified source files from smoltalk, kullm-v2 and open-korean-instructions under `raw/`, and the tokenized ChatML training set (391,887 conversations, 194M tokens, with assistant-only loss masks) under `packed/`.

## 원본 (`raw/`)

| 폴더 | 원 데이터셋 | 파일 | 원본 건수 | 라이선스 |
|---|---|---|---|---|
| `raw/smoltalk/data/everyday-conversations/` | [HuggingFaceTB/smoltalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) | parquet 1 | 2,260 | Apache-2.0 |
| `raw/smoltalk/data/smol-magpie-ultra/` | smoltalk (6개 샤드 중 첫 번째만) | parquet 1 | 68,257 | Apache-2.0 |
| `raw/smoltalk/data/smol-constraints/` | smoltalk | parquet 1 | 34,424 | Apache-2.0 |
| `raw/smoltalk/data/smol-rewrite/` | smoltalk | parquet 1 | 53,342 | Apache-2.0 |
| `raw/smoltalk/data/smol-summarize/` | smoltalk | parquet 1 | 96,356 | Apache-2.0 |
| `raw/smoltalk/data/metamathqa-50k/` | smoltalk ← [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA) | parquet 1 | 47,500 | MIT |
| `raw/smoltalk/data/numina-cot-100k/` | smoltalk ← [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | parquet 1 | 106,147 | Apache-2.0 |
| `raw/kullm-v2/` | [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | jsonl 1 | 152,630 | Apache-2.0 (GPT4ALL·Dolly·Vicuna 번역) |
| `raw/oki/koalpaca.json` | [heegyu/open-korean-instructions](https://huggingface.co/datasets/heegyu/open-korean-instructions) ← [KoAlpaca](https://github.com/Beomi/KoAlpaca) | jsonl 1 | 70,775 | **CC-BY-NC-4.0** |
| `raw/oki/OIG-smallchip2-ko.json` | open-korean-instructions ← OIG | jsonl 1 | 210,282 | Apache-2.0 |
| `raw/oki/korquad-chat.json` | open-korean-instructions ← [KorQuAD 1.0](https://korquad.github.io/KorQuad%201.0/) | jsonl 1 | 9,619 | KorQuAD 1.0: CC BY-ND 2.0 KR |

smoltalk은 `messages` 컬럼(role/content 목록), kullm-v2는 `instruction`/`input`/`output`, open-korean-instructions는 `<usr>`, `<bot>`, `<sys>` 태그가 든 `text` 한 컬럼입니다. open-korean-instructions의 `.json` 파일은 이름과 달리 한 줄에 한 건인 JSON Lines입니다.

## 학습 입력 (`packed/`)

`sft_data.py`가 만든 파일입니다.

| 파일 | 내용 |
|---|---|
| `packed/train.npz` | 390,887건, 193.4M 토큰 (loss 대상 146.1M) |
| `packed/val.npz` | 1,000건, 0.5M 토큰 (loss 대상 0.4M) |
| `packed/stats.json` | 소스별 사용 건수 |

npz 안에는 세 배열이 있습니다. `ids`(uint16, 모든 대화를 이어 붙인 토큰), `mask`(uint8, assistant 답변 구간만 1), `offsets`(int64, i번째 대화는 `ids[offsets[i]:offsets[i+1]]`). 토크나이저는 Perdix 기본 토크나이저에 `<|im_start|>`, `<|im_end|>`를 추가한 것으로, [Perdix-1.1B-Instruct](https://huggingface.co/prismdata/Perdix-1.1B-Instruct)의 `tokenizer.json`과 같습니다.

원본에서 고른 규칙은 이렇습니다. 소스별 건수와 반복 횟수는 `sft_data.py` 위쪽 `SMOLTALK`, `KOREAN` 표에 있습니다.

| 소스 | 사용 건수 | 비고 |
|---|---|---|
| everyday-conversations | 6,780 | 2,260건 × 3회 반복 |
| smol-magpie-ultra | 68,257 | 첫 샤드(`train-00000-of-00006`) 전부 |
| smol-constraints | 34,424 | 전부 |
| smol-rewrite | 20,000 | 무작위 2만 건 |
| smol-summarize | 20,000 | 무작위 2만 건 |
| metamathqa-50k | 25,000 | 무작위 2.5만 건 |
| numina-cot-100k | 15,000 | 무작위 1.5만 건 |
| kullm-v2 | 151,345 | 전부 (빈 답변 제외) |
| koalpaca | 14,529 | 무작위 2만 건 중 user/assistant 교대가 맞는 것 |
| OIG-smallchip2-ko | 30,000 | 무작위 3만 건 |
| korquad-chat | 7,980 | 무작위 8천 건 중 형식이 맞는 것 |

- 형식은 ChatML: `<|im_start|>role\n내용<|im_end|>\n`. system → user → assistant 순서가 맞지 않는 대화는 버렸습니다.
- 2,048토큰을 넘는 대화는 들어가는 턴까지만 썼습니다.
- 섞은 뒤 앞 1,000건을 검증용으로 뗐습니다. 시드 1234.

## 받기와 재현

```bash
hf download prismdata/Perdix-SFT-Data --repo-type dataset --local-dir .
```

`raw/`만 받아서 `packed/`를 다시 만들려면, [Perdix 저장소](https://github.com/theprismdata/Perdix) 루트에 `raw/`를 `sft_data/`로 두고 `python3 sft_data.py`를 실행하면 됩니다. 원 저장소에서 직접 받으려면 `download_sft_data.sh`를 쓰면 같은 폴더 구조로 받아집니다.

## 라이선스

이 저장소에 새로 만든 저작물은 없습니다. 각 파일은 원 데이터셋의 라이선스를 따르며, 위 표에 적어 두었습니다. 특히 두 가지를 알아 두세요.

- **`raw/oki/koalpaca.json`은 CC-BY-NC-4.0**이라 상업적 이용이 안 됩니다. `packed/`에는 이 데이터가 14,529건 섞여 있으므로, 상업 용도라면 `sft_data.py`의 `KOREAN` 표에서 `koalpaca`를 빼고 다시 만드세요.
- **`raw/oki/korquad-chat.json`**은 KorQuAD 1.0(CC BY-ND 2.0 KR) 지문을 바탕으로 생성된 대화입니다. 원 라이선스에 2차 저작물 제한이 있으니, 재배포하거나 상업적으로 쓸 때는 직접 판단해 주세요.

나머지(smoltalk, MetaMathQA, NuminaMath-CoT, kullm-v2, OIG)는 Apache-2.0 또는 MIT입니다. 출처를 밝힐 때는 원 데이터셋을 인용해 주세요.
