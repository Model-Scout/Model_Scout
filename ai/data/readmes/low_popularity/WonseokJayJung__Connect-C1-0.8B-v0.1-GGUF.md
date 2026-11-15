---
license: apache-2.0
language:
- ko
- en
base_model:
- WonseokJayJung/Connect-C1-0.8B-v0.1
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
tags:
- gguf
- ollama
- lm-studio
- decision-making
- connect-ai
- research
---

# Connect AI · C1

**Independent brains. Connected intelligence.**

An experimental decision model for AI-native companies. Built by **Jay · Connect AI LAB**. Now packaged as a single **812 MB Q8_0 GGUF** for Ollama and LM Studio.

[Watch Connect AI LAB](https://www.youtube.com/channel/UCdLZ0MsYS4hmqFgOYCB6C9w) · [Explore our research](https://www.ezerai.xyz/models) · [Inside the Lab](https://www.aicitybuilders.com/lab) · [Learn with Jay](https://www.aicitybuilders.com)

**C1 takes a question, its context, and a list of actions. Decision Studio returns a relative probability for every action and selects the highest-scoring one.** It computes these numbers from actual first-token log probabilities; it never asks the model to write percentage strings.

한국어 상황·질문·행동을 넣고 **행동별 확률 + 추천 행동**을 받으세요. **일반 채팅창에 “안녕”이나 질문만 입력하는 것은 C1의 판단 입력 형식이 아닙니다.** 아래 전용 화면을 사용하세요.

## Open Decision Studio

**[Open the web Decision Studio →](https://www.ezerai.xyz/studio)**

누구나 웹페이지를 열고 **자신의 LM Studio·Ollama API**에 연결할 수 있습니다. 별도 Python 설치 없이 상황·질문·행동을 입력하고 실제 행동별 확률을 확인하세요.

The webpage is public; C1 inference runs on **your own computer**. Install C1 in LM Studio or Ollama, start its API server, and click **Connect**. The browser sends your input directly to that local API, not through an EZERAI inference server. No cloud model or hosted GPU is included. The model remains **C1 v0.1**; this interface does not change its weights.

- **LM Studio:** load C1, open **Developer → Server Settings**, enable **CORS**, and start the server. Use `http://127.0.0.1:1234` in Studio. If API authentication is enabled, enter the token in Studio's optional field; the page keeps it only in memory for the current tab.
- **Ollama:** download C1 with `ollama pull hf.co/WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF:Q8_0`. Quit the existing Ollama app, then start the API with the website explicitly allowed (macOS/Linux shell):

```bash
OLLAMA_HOST=127.0.0.1:11434 OLLAMA_ORIGINS="https://www.ezerai.xyz" ollama serve
```

Leave that terminal running. Use `http://127.0.0.1:11434` in Studio. Its setup guide also includes Windows PowerShell syntax. Keep the API bound to loopback; no LAN exposure is needed. When your browser requests local-device access for this connection, allow it. Browser support varies; if it blocks the connection, use a current desktop browser or the local Python interface below.

### Optional local Python interface

[Download c1_local.py](c1_local.py) — one self-contained file, Python 3.10+, no extra Python packages. It hosts the interface on your own computer and calls the same model APIs. This alternative remains useful for CLI/JSON integrations and browsers that cannot connect directly. Client version **0.2.0**; model **C1 v0.1**.

#### LM Studio

1. Search for `WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF` and download **Q8_0**. Or download the [GGUF file](Connect-C1-0.8B-v0.1-Q8_0.gguf) and import it with `lms import` below.
2. **Load C1**, then open **Developer → Start Server** (default port 1234).
3. Download the client into a folder, open a terminal there, and run:

```bash
python3 c1_local.py --runtime lmstudio --serve
```

The browser opens **http://127.0.0.1:8765**. Enter the context, question, and actions, then click **행동별 확률 계산**. The client detects the C1 model identifier and sets the required inference parameters automatically. Do not replace the GGUF's embedded chat template. If multiple C1 models are available or you renamed it, specify its API identifier with `--model`.

Optional CLI model import from the GGUF download folder:

```bash
lms import Connect-C1-0.8B-v0.1-Q8_0.gguf --user-repo WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF --copy
lms load connect-c1-0.8b-v0.1 --context-length 4096 --identifier connect-c1 --yes
lms server start
```

#### Ollama

Install/open Ollama, then:

```bash
ollama pull hf.co/WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF:Q8_0
python3 c1_local.py --runtime ollama --serve
```

For an already downloaded GGUF, place [Modelfile](https://huggingface.co/WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF/blob/main/Modelfile) beside it, run `ollama create connect-c1:0.1 -f Modelfile`, and add `--model connect-c1:0.1` to the client command.

**The ordinary Ollama / LM Studio chat window does not calculate or display this probability distribution.** Raw generation is trained toward a single action letter when given the structured decision prompt. Free chat can produce unrelated or multilingual text. The probability client is the intended decision interface.

### JSON / integration

Run the built-in public example, or supply [example.json](example.json):

```bash
python3 c1_local.py --runtime lmstudio --input example.json
python3 c1_local.py --runtime ollama --input example.json
```

Actual Q8_0 output for the refund request with no matching payment record (rounded here):

| Action | Relative confidence |
| --- | ---: |
| `ask_customer` — request missing information | **69.98%** |
| `auto_reply` — reply automatically | 11.09% |
| `draft_for_review` — draft for review | 8.78% |
| `jay_direct` — handle personally | 5.12% |
| `ignore` — do not reply | 3.22% |
| `ask_jay` — escalate to the owner | 1.80% |

The JSON contains `action`, `confidence`, every action in `options` (including its confidence and actual logprob), `calibrated: false`, and `executed: false`. See the complete real output in [probability-validation.json](probability-validation.json).

### What confidence means

For each supplied action letter `i`, the client computes `exp(logprob_i) / sum(exp(logprob_j))` over **all supplied actions**, using a numerically stable softmax. This is a distribution **conditional on the listed actions**, not a calibrated probability that the action is correct. Missing options, changed wording/order, or unsuitable questions can change the scores. A high score can still be wrong.

- Input: `state`, `question`, and **2–20** actions with unique `key` and non-empty `description`. Labels are assigned A, B, C… Optional labels must match this order. The original MLX client separately supports up to 24.
- The client requests one token, temperature 0, repeat penalty 1, thinking off, `logprobs: true`, and `top_logprobs: 20`. The runtimes expose only the top 20 token scores. **If any supplied label is absent, it returns an error, never a made-up zero or a partial distribution.** Reduce the number of actions or use the original MLX client for direct access to all logits.
- Input is capped at 3,000 UTF-8 bytes including action descriptions to stay inside the tested 4,096-token context. Every decision is a fresh single-turn request.
- The client binds only to `127.0.0.1`, sends input only to the chosen local runtime, and does not persist inputs or execute actions. Runtime logging/storage is controlled by the runtime itself. Stop the local screen with Ctrl+C. Use `--port` if 8765 is busy and `--url` for a different loopback API port (without `/v1`).
- Tested: **Ollama 0.35.0**, **LM Studio 0.4.24+1 / Metal 2.50.0**, Apple M5 Max. Older builds without logprobs fail with an error. Windows/Linux have not been verified; on Windows, use the installed Python launcher (for example `py`).

**Probability validation:** all action scores were available for all **360/360** internal synthetic cases in both apps. Maximum cross-runtime probability difference was **2.23 × 10⁻¹⁶** (rounded up). Choices and accuracy stayed unchanged. This tests runtime consistency, not real-world reliability or confidence calibration. [10 integrity tests](test_c1_local.py) cover missing scores, invalid inputs, unsupported runtimes, numerical stability, and local-only requests.

## Verified compatibility, separate from the MLX results

Evaluated on 2026-10-02, using the same internal synthetic 360-case set as the original adapter. Temperature 0, repeat penalty 1.0, one output token, context 4096, thinking off.

| Runtime / format | Valid option outputs | Company subset | All decisions | Same prediction as original MLX |
| --- | ---: | ---: | ---: | ---: |
| Original MLX LoRA reference | 360/360 | 159/240 · 66.25% | 224/360 · 62.22% | 360/360 |
| Ollama 0.35.0 · Q8_0 | 360/360 | 157/240 · 65.42% | 225/360 · 62.50% | 353/360 |
| LM Studio 0.4.24+1 · Q8_0 | 360/360 | 157/240 · 65.42% | 225/360 · 62.50% | 353/360 |

**Ollama and LM Studio matched each other on all 360 cases.** Seven predictions differ from the original MLX adapter; conversion and runtime precision can change borderline selections. The small aggregate change is not evidence of an improvement.

[compatibility.json](compatibility.json) contains settings, runtime versions, per-case predictions, and file provenance. Full internal evaluation inputs are not released, so this evaluation cannot be fully reproduced from this repository alone. Training/evaluation overlap has not been independently audited. These results do not establish production reliability. Windows/Linux hardware has not been tested. Website public-benchmark and simulator results were recorded with MLX and are **not GGUF measurements**.

## What was trained and converted

- **Base:** [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B), revision `2fc06364715b967f1860aea9cf38778875588b17`.
- **Fine-tune:** [original Connect AI C1 v0.1 MLX LoRA](https://huggingface.co/WonseokJayJung/Connect-C1-0.8B-v0.1), rank 8, scale 2; 5,084 labelled training examples. Supervised fine-tuning / imitation learning, **not a completed reward-based reinforcement-learning run**.
- **Export:** merge the released adapter into text-only HF weights in float32, preserving the effective BF16 Qwen RMSNorm weights used by MLX. Convert to F16, then Q8_0 with llama.cpp commit `159c651f5798e7b98e7afc29c485b96137aa9ada`. No vision or MTP tensors are exported.
- **Artifact:** `Connect-C1-0.8B-v0.1-Q8_0.gguf`, 811,843,584 bytes; includes base and adapter weights. No separate Qwen download is needed for this GGUF.
- **SHA-256:** `ea65c274a44cc8e879320a8339e209ae29d9da47bde478b89214bf5ddc32911e`.

Conversion source: [export_hf.py](export_hf.py). With the pinned base, original adapter, and the pinned llama.cpp checkout downloaded:

```bash
python export_hf.py --base /path/to/Qwen3.5-0.8B --adapter /path/to/C1-adapter --output ./c1-hf
python /path/to/llama.cpp/convert_hf_to_gguf.py ./c1-hf --outtype f16 --no-nextn --model-name 'Connect AI C1 0.8B v0.1' --outfile ./Connect-C1-0.8B-v0.1-F16.gguf
/path/to/llama-quantize ./Connect-C1-0.8B-v0.1-F16.gguf ./Connect-C1-0.8B-v0.1-Q8_0.gguf Q8_0 8
```

The conversion script requires PyTorch and safetensors; use the pinned llama.cpp conversion dependencies. Only Q8_0 is distributed here. The original MLX adapter remains available separately for Apple silicon users and original-result reproduction.

## Build AI with Jay

We build in public and turn the work into practical education—from running local AI to creating decision models for AI-native businesses.

- **Watch:** [CONNECT AI LAB on YouTube](https://www.youtube.com/channel/UCdLZ0MsYS4hmqFgOYCB6C9w). Start with the local AI / second-brain series: [EP.1](https://youtu.be/eyFk27mwFJo), [EP.2](https://youtu.be/ZtVTeLQDyHQ), [EP.3](https://youtu.be/TNEwF_WmgO4), [Connect AI v1 release](https://youtu.be/TAkD3UL0_kE). These videos document the earlier application, not a C1 training tutorial.
- **Explore:** [Connect AI research](https://www.ezerai.xyz/models) and [Connect AI LAB](https://www.aicitybuilders.com/lab), a member research space.
- **Learn:** [AI City Builders](https://www.aicitybuilders.com), Jay's education and community for AI-native solo businesses.

## Limits and attribution

C1 is an early experimental option selector. It depends on the supplied options and can confidently make mistakes. It is an independent Qwen fine-tune by Connect AI; the decision format is inspired by public Together AI / Typesafe tev1 work. C1 is not Typesafe's jev and is not affiliated with or endorsed by Qwen, Typesafe, Together AI, Ollama, or LM Studio. Reward-based RL and connecting specialist models remain research directions.

Apache-2.0. See [LICENSE](https://huggingface.co/WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF/blob/main/LICENSE), [NOTICE](https://huggingface.co/WonseokJayJung/Connect-C1-0.8B-v0.1-GGUF/blob/main/NOTICE), and [manifest.json](manifest.json).
