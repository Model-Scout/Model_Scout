---
license: apache-2.0
license_link: https://huggingface.co/quevirus/Xevn-4B/blob/main/LICENSE
base_model: quevirus/Xevn-4B
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-classification
language:
- ko
- en
tags:
- decision-model
- jev
- classification
- calibration
- korean
- gguf
- llama.cpp
---

# Xevn-4B-GGUF

[Transformers](https://huggingface.co/quevirus/Xevn-4B) | [MLX](https://huggingface.co/quevirus/Xevn-4B-MLX-5bit) | [GitHub](https://github.com/Nhahan/Xevn) | [Website](https://nhahan.github.io/Xevn/)

GGUF files of [Xevn-4B](https://huggingface.co/quevirus/Xevn-4B) for llama.cpp. Xevn is a 4B decision model built for Korean, trained for Korean understanding, knowledge, and judgment.

Xevn follows the [Jev](https://benchmarkheaven.com/jev-models) decision format. It reads a question and its options once and returns the answer together with a probability for every option. There is no text generation, so a request costs one forward pass.

## Model overview

- **Type:** Decision model with one forward pass per question and no text generation
- **Parameters:** 4B
- **Architecture:** Hybrid Gated DeltaNet and attention, 32 layers (24 Gated DeltaNet, 8 full attention)
- **Hidden size / vocabulary:** 2,560 / 248,320
- **Question types:** `choice`, `noul`, `score`
- **Languages:** Korean (primary), English
- **Format:** GGUF (llama.cpp)
- **Files:** BF16, Q8_0, Q6_K, Q5_K_M, Q4_K_M

## Files

| File | Quant | Size | Same answer as 16-bit |
|---|:-:|:-:|:-:|
| [Xevn-4B-BF16.gguf](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-BF16.gguf) | BF16 | 8.67 GB | 39/40 |
| [**Xevn-4B-Q8_0.gguf**](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q8_0.gguf) | Q8_0 | 4.61 GB | 38/40 |
| [Xevn-4B-Q6_K.gguf](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q6_K.gguf) | Q6_K | 3.56 GB | 37/40 |
| [Xevn-4B-Q5_K_M.gguf](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q5_K_M.gguf) | Q5_K_M | 3.16 GB | 36/40 |
| [Xevn-4B-Q4_K_M.gguf](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q4_K_M.gguf) | Q4_K_M | 2.78 GB | 38/40 |

`Xevn-4B-Q8_0.gguf` is the recommended default. "Same answer as 16-bit" counts held-out questions where the file picks the same top answer as the 16-bit Transformers model. With 40 questions, differences of one or two answers between files are within noise.

## Quickstart

```bash
pip install -U "llama-cpp-python>=0.3.36" huggingface_hub
# NVIDIA: CMAKE_ARGS="-DGGML_CUDA=on" pip install -U "llama-cpp-python>=0.3.36"
hf download quevirus/Xevn-4B-GGUF Xevn-4B-Q8_0.gguf xevn_gguf.py xevn_infer.py temps.json --local-dir Xevn-4B-GGUF
```

Older llama-cpp-python releases do not support this architecture. On macOS the default build uses Metal.

```python
import sys
sys.path.insert(0, "Xevn-4B-GGUF")  # the repository ships the xevn_gguf.py helper
from xevn_gguf import XevnGGUF

model = XevnGGUF("Xevn-4B-GGUF/Xevn-4B-Q8_0.gguf")  # n_ctx=8192, n_gpu_layers=-1 (all layers on the GPU)
```

```python
state = "고객: 어제 주문한 이어폰 값이 카드에서 두 번 결제됐어요. 오늘 안에 한 건 취소해 주세요."
# "Customer: the earphones I ordered yesterday were charged to my card twice. Please cancel one today."
questions = {
    "team": {"type": "choice", "instructions": "Which team should handle this ticket?",
             "criteria": {"billing": "Payments and refunds", "shipping": "Delivery", "account": "Login and account"}},
    "charged_twice": {"type": "noul", "instructions": "Was the customer charged more than once?"},
    "urgency": {"type": "score", "instructions": "How urgent is this ticket?",
                "criteria": ["Low", "Medium", "High"]},
}
result = {key: model.predict(state, q) for key, q in questions.items()}
```

Output (rounded):

```json
{
  "team": {"answer": "billing", "probs": {"billing": 0.998, "shipping": 0.001, "account": 0.001}},
  "charged_twice": {"answer": true, "probs": {"yes": 0.993, "no": 0.007}},
  "urgency": {"answer": 1.77, "probs": {"0": 0.041, "1": 0.150, "2": 0.809}}
}
```

Values differ slightly between quant types.

## Request format

A request is a `state` (text or any JSON value) and one or more named `questions`. Each question has a `type`, `instructions`, and `criteria`.

| Type | Use | `criteria` | `answer` in the result |
|---|---|---|---|
| `choice` | Pick one of up to 26 options | `{"key": "description", ...}`, 2 to 26 options | The key of the most probable option |
| `noul` | Yes or no | Optional `{"true": "...", "false": "..."}` | `true` or `false` |
| `score` | Rate on a graded scale | `["lowest level", ..., "highest level"]`, 2 to 10 levels | The expected level (0 is the first level) |

`probs` holds a probability for every option, `yes`/`no`, or level. For `noul`, a yes probability strictly between 0.2 and 0.8 is moved to 0.2 or 0.8 on the same side, so the model always commits to an answer. Readout temperatures per type are in `temps.json` (choice 1.1, noul 1.2, score 1.2).

Benchmark results are in the [Xevn-4B evaluation](https://huggingface.co/quevirus/Xevn-4B#evaluation); they were measured with the 16-bit weights.

## Model files

| Format | Precision | Size | Speed (p50) | Repository |
|---|:-:|:-:|:-:|---|
| Transformers | 16-bit | 9.3 GB |  | [Xevn-4B](https://huggingface.co/quevirus/Xevn-4B) |
| MLX | 16-bit | 8.4 GB | 88 ms | [Xevn-4B-MLX-bf16](https://huggingface.co/quevirus/Xevn-4B-MLX-bf16) |
| MLX | 8-bit | 4.5 GB | 83 ms | [Xevn-4B-MLX-8bit](https://huggingface.co/quevirus/Xevn-4B-MLX-8bit) |
| MLX | 6-bit | 3.4 GB | 82 ms | [Xevn-4B-MLX-6bit](https://huggingface.co/quevirus/Xevn-4B-MLX-6bit) |
| MLX | 5-bit | 2.9 GB | 80 ms | [Xevn-4B-MLX-5bit](https://huggingface.co/quevirus/Xevn-4B-MLX-5bit) |
| MLX | 4-bit | 2.4 GB | 78 ms | [Xevn-4B-MLX-4bit](https://huggingface.co/quevirus/Xevn-4B-MLX-4bit) |
| MLX | 3-bit | 1.8 GB | 77 ms | [Xevn-4B-MLX-3bit](https://huggingface.co/quevirus/Xevn-4B-MLX-3bit) |
| GGUF | BF16 | 8.67 GB |  | [Xevn-4B-GGUF](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-BF16.gguf) |
| GGUF | Q8_0 | 4.61 GB |  | [Xevn-4B-GGUF](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q8_0.gguf) |
| GGUF | Q6_K | 3.56 GB |  | [Xevn-4B-GGUF](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q6_K.gguf) |
| GGUF | Q5_K_M | 3.16 GB |  | [Xevn-4B-GGUF](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q5_K_M.gguf) |
| GGUF | Q4_K_M | 2.78 GB |  | [Xevn-4B-GGUF](https://huggingface.co/quevirus/Xevn-4B-GGUF/blob/main/Xevn-4B-Q4_K_M.gguf) |

Speed is the MLX p50 over an equal mix of the three input lengths in the Speed table, measured in one session on an Apple M4 Max. On every benchmark, MLX 8-bit to 5-bit stay within 2 points of 16-bit accuracy and 4-bit within 3 points. 3-bit loses 7 to 21 points and is provided for experimentation. The Transformers weights keep the original multimodal layout (9.3 GB); the helper uses the text model only.

## Intended use and limitations

Xevn is built for decisions: classification, multiple choice, yes/no judgments, and rating. It is not a chat or text-generation model. It is tuned for Korean; English input works but is not the focus.

- Xevn returns probabilities over the options you give it. It does not generate text and cannot answer open questions.
- The bundled helpers run one forward pass per question and accept 2 to 26 options and 2 to 10 score levels.
- Speed figures are for MLX on an Apple M4 Max with inputs up to 256 tokens.
- Ollama is not supported, because this readout needs the prompt logits.

## Citation

```bibtex
@misc{xevn2026,
  title  = {Xevn-4B: a Korean decision model},
  author = {Nhahan},
  year   = {2026},
  url    = {https://huggingface.co/quevirus/Xevn-4B}
}
```

## License

[Apache 2.0](https://huggingface.co/quevirus/Xevn-4B/blob/main/LICENSE). Built on [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B).
