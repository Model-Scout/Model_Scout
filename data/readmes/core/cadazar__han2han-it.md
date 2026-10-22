---
license: apache-2.0
language:
- ko
library_name: transformers
pipeline_tag: feature-extraction
base_model: cadazar/han2han-pt
datasets:
- seyoungsong/Open-Korean-Historical-Corpus
tags:
- han2han
- hanja
- hangul
- historical-korean
- encoder-decoder
- custom_code
---

# Han2Han IT

Instruction-tuned checkpoint of [Han2Han](https://github.com/cadazar/han2han),
a 169M-parameter encoder-decoder model that learns script-invariant
representations of Korean text. A document written in Hanja and its Hangul
transcription land at the same point in embedding space. The recipe (jamo and
character-level embedding fusion, morpheme-aware denoising, bidirectional
Hanja-Hangul transcription) is described in the paper, accepted to Findings of
EMNLP 2026.

**Two versions live in this repo.**

| Revision | Weights | Use it for |
| --- | --- | --- |
| `main` | the instruction tuning continued for 30M tokens in fp32 (step 762 of the continuation) | generation and chat: it ends its turns |
| `emnlp2026` | `han2han-ul2-base-1-it`, step 43153, the checkpoint behind the paper | reproducing the paper |

The orbax (Flax) checkpoint behind `main` is
[`cadazar/han2han-it-flax`](https://huggingface.co/cadazar/han2han-it-flax), the starting point of
[`cadazar/han2han-rl`](https://huggingface.co/cadazar/han2han-rl).

The first checkpoint was trained with its weights in bf16. The updates to the
embedding rows of the chat tokens were too small to survive bf16 rounding, so
those rows barely moved from where pre-training left them, `<|end_of_turn|>`
among them, and the model did not learn to end a turn. Sampled at temperature 0.7, none of
its outputs stopped. `main` continues the same instruction tuning (the same
four task families, learning rate 3e-5) in fp32 until those rows are trained.
Nothing else about the recipe changed. To load the paper's weights, pass
`revision="emnlp2026"` to `from_pretrained`.

On 256 newspaper sentences from the 1920s, greedy decoding with the task prompt
in the system message:

| | `emnlp2026` | `main` |
| --- | --- | --- |
| Hangul to Hanja: share of the original Hanja restored | 0.19 | 0.31 |
| Hanja to Hangul: share of the Hanja read correctly | 0.65 | 0.89 |
| outputs that end on their own (to Hanja / to Hangul) | 76% / 91% | 99% / 100% |
| the same, sampled at temperature 0.7 | 0% / 0% | 100% / 100% |
| three articles in slices of 250 to 500 characters: Hanja restored | 0.66 | 0.81 |

The sentences are from the validation and test splits of the sentence-level
transcription set. The instruction tuning used the article-level set and the
same newspapers were part of pre-training, so read the table as a comparison
of the two checkpoints, not as performance on unseen text.

The sentence embeddings of `main` have not been run through the paper's
evaluations, so for those results use `emnlp2026`.
[`cadazar/han2han-pt`](https://huggingface.co/cadazar/han2han-pt) is the
pre-trained checkpoint both started from, and
[`cadazar/han2han-rl`](https://huggingface.co/cadazar/han2han-rl) is `main`
trained further on transcription with reinforcement learning, which is the one
to use for converting between the scripts.

This repo holds the PyTorch weights, the tokenizer with its chat template, and
the modeling code needed to load them through the `transformers` Auto classes
with `trust_remote_code=True`. Training code, the Flax model, the Flax-to-PyTorch
converter, and the evaluation pipeline live in the GitHub repo.

## Intended use

Han2Han is meant for representations. That means classification and fine-tuning on
downstream tasks, and sentence embeddings that treat Hanja and Hangul spellings
of the same text alike. The model generates text, but generation is not what it
was built or evaluated for, and improving it is follow-up work:

- **Prompt layout.** The task prompt goes in the system message and the text
  alone in the user message, which is how the instruction tuning presented
  every task. With the instruction written into the user message instead,
  Hangul to Hanja restoration returns the Hangul input unchanged.
- **Hangul to Hanja** restoration (`한글을 한자로 전사하시오:`) works on
  article-length input. Given the first 478 characters of a 1922 newspaper
  article in Hangul, greedy decoding restores 84% of its 251 Hanja. The
  article comes from a corpus used in pre-training, so this is an illustration
  and not a held-out measurement. On single sentences it restores much less
  (0.31 above), and a third of the outputs come back with no Hanja at all. The
  instruction tuning had articles for this task and no single sentences.
- **Hanja to Hangul** transcription (`한자를 한글로 전사하시오:`) works on
  sentences and articles, but can leave some Hanja untranscribed or change a
  word.
- **Layout matters in both directions.** With the instruction in the user
  message, Hangul to Hanja restores under 1% of the Hanja and Hanja to Hangul
  reads 45% of them.
- **Stopping.** The outputs measured here end on their own, in fp32. Give
  `generate()` a token limit anyway. Twice the input's tokens plus 8 leaves
  room for a correct answer and cuts off the occasional output that repeats
  itself (about 4% of the sentences).

`hanja_transcription_demo.ipynb` in the GitHub repo was written with the other
layout (the instruction in the user message), so the Hangul to Hanja outputs in
its sections 4 to 9 understate what this checkpoint does. Its section 10 runs
the layout described here.

## Usage

Running the model needs `torch` and `transformers` (tested with torch 2.14.1 and
transformers 5.18.0 on CPU). The model class ships in this repo, so loading needs
`trust_remote_code=True`. The tokenizer itself runs no custom code, but without
the flag `AutoTokenizer` stops to ask.

### Sentence embeddings

`output_sentence_embeddings=True` returns the mean-pooled encoder states, one
640-dimensional vector per input.

```python
import torch
import torch.nn.functional as F
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

repo = "cadazar/han2han-it"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained(repo, trust_remote_code=True).eval()

texts = [
    "會場을 一巡하고 돌아올 때까지도 日本人側 畵家까지도 一人도 發見할 수가 없었다.",
    "회장을 일순하고 돌아올 때까지도 일본인측 화가까지도 일인도 발견할 수가 없었다.",
    "南畵나 四君子에서는 破墨의 妙法으로 白雪을 象徵할 수 있다.",
]
inputs = tokenizer(texts, return_tensors="pt", padding=True)
with torch.no_grad():
    embeddings = model(**inputs, output_sentence_embeddings=True)[0]
embeddings = F.normalize(embeddings, dim=-1)
print(embeddings @ embeddings.T)
# tensor([[1.0000, 0.9020, 0.8546],
#         [0.9020, 1.0000, 0.8100],
#         [0.8546, 0.8100, 1.0000]])
```

The first two rows are the same 1920s newspaper sentence in mixed script and in
Hangul, and the third is a different sentence.

### Chat

`AutoModelForCausalLM` loads `Han2HanForCausalLM`, a wrapper that gives the
encoder-decoder the interface chat tooling expects. Its `generate()` takes the
rendered chat prompt as one sequence and returns the prompt followed by the
reply. `pipeline("text-generation")` works with it, and so does the
`transformers` server:

```bash
transformers serve --trust-remote-code
transformers chat cadazar/han2han-it --system-prompt "한자를 한글로 전사하시오:"
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "cadazar/han2han-it"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(repo, trust_remote_code=True).eval()


def run(task_prompt, text):
    messages = [
        {"role": "system", "content": task_prompt},
        {"role": "user", "content": text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
    )
    budget = 2 * len(tokenizer(text).input_ids) + 8
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=budget, do_sample=False)
    return tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)


print(run(
    "한자를 한글로 전사하시오:",
    "會場을 一巡하고 돌아올 때까지도 日本人側 畵家까지도 一人도 發見할 수가 없었다.",
))
# 회의장을 일순하고 돌아올 때까지도 일본인측 화가까지도 일인도 발견할 수가 없었다.

hangul = (
    "미술전람 계획 총독부 사안으로 명년 초차 개설총독부에서는 조선에 재 한 미술의 발달을 비보할 "
    "목적으로 동경의 제국미술원전람회를 방하 여 매년 일차 미술전람회를 개할 방침을 내정하고 시 "
    "이십육일 오전 십시 총독부 제이회의실에 박영효 후, 민병석 자, 서화협회의 정대유, 김돈희, 이도영 "
    "외 제씨, 서화연구회의 김규진 씨, 일본인측 서화가로  고목배수 외 수씨 기타 서화가에 관계있는 "
    "인사를 초청하고 수야 정무총감 이하 학무당국자가 회합하여 차에 관한 상의회를 개한바"
)
print(run("한글을 한자로 전사하시오:", hangul))
# 美術美術舘 計劃 總督府 事案으로 明年 初次 開設總督府에서는 朝鮮에 在 한 美術의 發達을 備報할
# 目的으로 東京의 帝國美術院展覽會를 訪하 여 每年 日次 美術展覽會를 開할 方針을 內定하고 時
# 二十六日 午前 十時 總督府 第二回의室에 朴永孝 後, 閔丙錫 子, 書畵協會의 精大類, 金敦熙,
# 伊道榮 外 諸氏, 書畵硏究會의 金奎鎭 氏, 日本人側 書畵家로 高木培水外 氏等 其他 書畵家에
# 關係있는 人事를 招請하고 受也 政務總監 以下 學務當局者가 會合하여 此에 關한 商議會를 開한바
```

The outputs are shown as generated (each is one line). In the first, `會場`
came out as `회의장` where `회장` was meant. The second is the opening of the
1922 article. The original reads `美術展覽 計劃 總督府 事案으로 明年 初次
開設總督府에서는 朝鮮에 在 한 美術의 發達을 裨補할 목적으로 東京의
帝國美術院展覽會를 倣하 여 每年 一次 ...`, so the output doubles a word at the
start (`美術美術舘`) and writes same-sounding characters for several words and
names (`備報`, `訪`, `日次`, `精大類`).

Prompt format, as used by the SFT collator in the GitHub repo and by the chat
template:

- `<|system|>{system}<|user|>{user}<|end_of_turn|>`, with
  `<|assistant|>{reply}<|end_of_turn|><|user|>{user}<|end_of_turn|>` for each
  further turn. The system part is optional in the format, but it is where
  this checkpoint expects the task prompt. Each direction was trained with
  three wordings. They were `한자를 한글로 전사하시오:`, `다음 한문을 한글로 옮기시오:`,
  `한자 표기를 한글 독음으로 변환하시오:` for Hanja to Hangul, and
  `한글을 한자로 전사하시오:`, `다음 한글 텍스트에 적절한 한자를 추가하시오:`,
  `한자 표기가 필요한 부분에 한자를 병기하시오:` for Hangul to Hanja.
- The generation prompt is `<|assistant|>`. A turn ends with `<|end_of_turn|>`
  (`eos_token_id` 10).
- **Thinking.** The chat template accepts `enable_thinking=True`, which starts
  the reply at `<|think|>`, and the training data had reasoning examples. The
  model did not learn a separate reasoning step from them. Started at
  `<|think|>`, it answers as it does from `<|assistant|>`, or writes one
  sentence of rationale and ends the turn, and it never moves on to an
  `<|assistant|>` answer. Leave thinking off.

The wrapper splits the prompt at its last `<|end_of_turn|>`. Everything up to
and including it is the encoder input, and the generation prompt after it starts
the decoder. A prompt without a generation prompt raises. `forward()` is not
wrapped and stays encoder-decoder.

### Encoder-decoder generation

`AutoModelForSeq2SeqLM` loads the model itself. `generate()` is the standard
`transformers` one, with a KV cache. Greedy decoding, beam search, and sampling
all work. The encoder takes the prompt up to `<|end_of_turn|>`, and the decoder
starts from `<|assistant|>` (`decoder_start_token_id` 9).

```python
from transformers import AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained(repo, trust_remote_code=True).eval()
prompt = (
    "<|system|>한자를 한글로 전사하시오:"
    "<|user|>會場을 一巡하고 돌아올 때까지도 日本人側 畵家까지도 一人도 發見할 수가 없었다.<|end_of_turn|>"
)
inputs = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### Tokenizer

`tokenizer.json` is a `tokenizers`-library build of the SentencePiece model
(`spiece.model`, kept here as the source), made by
`scripts/build_hf_tokenizer.py` in the GitHub repo. Calling the tokenizer does
not add BOS or EOS tokens, and special tokens written into the text are mapped
to their ids. It encodes like the SentencePiece wrapper the training code uses,
with one known difference. Where two segmentations of a span have exactly the
same score (runs of digits, mostly), the same pieces can come out in a different
order.

## Files

| File | Contents |
| --- | --- |
| `model.safetensors` | fp32 weights, 169.2M parameters, plus the `jbu` / `cbu` subword bucket tables |
| `config.json`, `generation_config.json` | model and generation config, with `auto_map` entries for the Auto classes |
| `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja` | fast tokenizer (38400 pieces) and chat template |
| `spiece.model` | the SentencePiece model `tokenizer.json` was built from |
| `modeling_han2han.py`, `han2han_config.py` | modeling code from the GitHub repo at commit [`af1330e`](https://github.com/cadazar/han2han/commit/af1330e49f1edf46e26b63937724ddbaeffc3bee) |

`modeling_han2han.py` (`modeling_han2han_pytorch.py` there) differs in two
places. The config import is relative, and the module-level `register_han2han`
import is replaced by the `auto_map` entries. `han2han_config.py` is the GitHub
copy at commit `7304c38`, and it has not changed since. `config.json` names
`AutoModelForCausalLM` under `architectures` so that `transformers serve`, which
looks that name up in the `transformers` namespace, can load the model.

## Instruction tuning

1. **Pre-training**: 35B tokens. The uniform average of its last five
   checkpoints is [`cadazar/han2han-pt`](https://huggingface.co/cadazar/han2han-pt).
2. **Instruction tuning** (`emnlp2026`): 1.5B tokens from that average on
   instruction following, chain-of-thought reasoning, Hanja-Hangul article
   transcription, and summarization data, weights in bf16
   (`configs/it-muon-stage_1.yaml` in the GitHub repo).
3. **Continuation** (`main`): 30M more tokens on the same four task families
   in fp32, learning rate 3e-5, about 40k tokens per update, 762 updates
   (the orbax checkpoint is [`cadazar/han2han-it-flax`](https://huggingface.co/cadazar/han2han-it-flax)).

The embedding row of `<|end_of_turn|>` sits at an L2 distance of 0.014 from its
pre-trained value after step 2 and 0.30 after step 3. Ordinary token rows moved
0.01 to 0.04 in step 3.

## Acknowledgements

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The instruction tuning ran on a TPU v6e-8 host from TRC.

## Citation

```bibtex
@inproceedings{han2han2026,
  title     = {Han2Han: Efficient Language-Specific Character Representation
               through Script-Aware Pre-Training for Historical Text Analysis},
  author    = {Adams, Cellik and Jo, EunKyoung and Kim, Juae},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2026},
  year      = {2026}
}
```

## License

Apache License 2.0, the same as the [GitHub repo](https://github.com/cadazar/han2han).
