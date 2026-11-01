---
license: apache-2.0
language:
- ko
- en
library_name: gguf
pipeline_tag: text-generation
base_model: LLM-OS-Models/KoHRM-Text-1.4B
base_model_relation: quantized
tags:
- gguf
- llama.cpp
- hrm-text
- kohrm
- korean
- text-generation
---

# KoHRM-Text-1.4B-GGUF

GGUF exports for [LLM-OS-Models/KoHRM-Text-1.4B](https://huggingface.co/LLM-OS-Models/KoHRM-Text-1.4B).

This is a custom `hrm_text` architecture. Standard upstream `llama.cpp`, Ollama, LM Studio, and other GGUF frontends will not load these files until `hrm_text` support lands upstream. Use the included runtime patch:

```text
runtime/llama.cpp-hrm_text.patch
```

The patch is based on the HRM-Text GGUF work from [sinimiini/HRM-Text-1B-GGUF](https://huggingface.co/sinimiini/HRM-Text-1B-GGUF), adapted for KoHRM-Text-1.4B. The KoHRM conversion infers the physical H/L stack depth from safetensors, because the public config reports `num_hidden_layers=32` while the exported tensors are arranged as `H: 16` and `L: 16`.

## Files

| file | type | size | sha256 |
|---|---:|---:|---|
| `KoHRM-Text-1.4B-BF16.gguf` | BF16 | 2.6G | `d5c66f994327c1e2f05b33b0a2ff798a1d05f8b905b7f93943e101bca06c8b0a` |
| `KoHRM-Text-1.4B-Q8_0.gguf` | Q8_0 | 1.4G | `8dae86207987804c7e8fc34fcba0d78ae2e54cd8563e907e9e5aea8442f7300c` |
| `KoHRM-Text-1.4B-Q6_K.gguf` | Q6_K | 1.1G | `dd54d24344e842c3cd0f261e4b740c42c0ec78ed0b3414cdb8b2ac5022b7fb8a` |
| `KoHRM-Text-1.4B-Q5_K_M.gguf` | Q5_K_M | 961M | `90f47f54bd7cf545583a2be43a9d0c971cf6112ff16261e2e926cfabe2e9e35a` |
| `KoHRM-Text-1.4B-Q4_K_M.gguf` | Q4_K_M | 841M | `e521243be6733796f221ec7de3ca3d1ff9014301f812138a173072d6def2f090` |
| `KoHRM-Text-1.4B-Q3_K_M.gguf` | Q3_K_M | 700M | `29fe588fdc434980cdc484c6324af8ca0c92122b995b26a09b8fed5baceae4be` |
| `KoHRM-Text-1.4B-Q2_K.gguf` | Q2_K | 569M | `6010878b117e639f9a1fb5332aa6c5a76bdf50ee08e6af4d7661a12d77cf7157` |

## Build Patched llama.cpp

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
git checkout 6a257d44633d4a752183ed778b88d2924d0a6b9d
git apply /path/to/runtime/llama.cpp-hrm_text.patch

cmake -S . -B build-hrm \
  -DCMAKE_BUILD_TYPE=Release \
  -DLLAMA_CURL=OFF \
  -DGGML_NATIVE=OFF

cmake --build build-hrm --target llama-cli llama-quantize llama-completion llama-results -j 8
```

## CPU Run

Download a quantized GGUF file:

```bash
huggingface-cli download LLM-OS-Models/KoHRM-Text-1.4B-GGUF \
  KoHRM-Text-1.4B-Q8_0.gguf \
  --local-dir .
```

Run on CPU:

```bash
./build-hrm/bin/llama-cli \
  -m ./KoHRM-Text-1.4B-Q8_0.gguf \
  -ngl 0 \
  -t 4 \
  -c 1024 \
  -n 260 \
  --seed 41 \
  --temp 0.45 \
  --top-p 0.9 \
  --repeat-penalty 1.08 \
  --single-turn \
  --simple-io \
  --no-warmup \
  --display-prompt \
  -p $'해외주식 투자에서 원/달러 환율 변동이 원화 수익률에 미치는 영향과 대응 방안을 간단히 설명해 주세요.'
```

## H/L Cycle Override (수정 실행: H/L 사이클 직접 지정)

KoHRM-Text-GGUF stores recurrence settings as GGUF metadata:

```text
hrm_text.h_cycles = 2
hrm_text.l_cycles = 3
```

현재 패치된 llama.cpp에서는 실행 시 모델 로딩 단계에서 아래 키를 메타데이터 오버라이드할 수 있습니다.

```bash
./build-hrm/bin/llama-cli \
  -m ./KoHRM-Text-1.4B-Q8_0.gguf \
  -ngl 0 \
  -t 4 \
  -c 1024 \
  -n 260 \
  --seed 41 \
  --temp 0.45 \
  --top-p 0.9 \
  --repeat-penalty 1.08 \
  --single-turn \
  --simple-io \
  --no-warmup \
  --display-prompt \
  --override-kv hrm_text.h_cycles=int:1 \
  --override-kv hrm_text.l_cycles=int:2 \
  -p $'해외주식 투자에서 원/달러 환율 변동이 원화 수익률에 미치는 영향과 대응 방안을 간단히 설명해 주세요.'
```

Use case:

- `h_cycles/l_cycles`를 낮추면 동일 조건에서 응답속도는 빨라지는 경향이 있지만 품질 저하가 자주 증가합니다.
- `2/3`은 현재 기본값(문서 상 안정 동작)입니다.
- `1/2`는 속도 우선 테스트로 추천하며, 실제 정밀 추론에서는 `2/3`이 더 안정적입니다.

`--override-kv` uses key format `KEY=TYPE:VALUE`, same as upstream llama.cpp:

- `hrm_text.h_cycles=int:1`
- `hrm_text.l_cycles=int:2`

If you need a persistent configuration (e.g., fixed 1/1 for a workload), export a new GGUF after changing `H_cycles` / `L_cycles` in the source config before `convert_hf_to_gguf.py` conversion. That preserves one set of cycles inside the artifact and avoids runtime override overhead.

## CPU Generation Tests

Tested locally on CPU with the patched `llama.cpp` build and the prompt shown above.

This prompt was chosen after checking the KoHRM training-data path. KoHRM uses
the HRM `V1Dataset` instruction-response layout:

```text
<|im_start|><condition_token>instruction<|im_end|>response<|box_end|>
```

The instruction/prefix span is not trained with loss; the response span is
trained with response-only loss. Local decoded samples include short Korean
finance QA rows, so the representative GGUF smoke prompt below uses the same
plain instruction style instead of a legal reasoning prompt.

| file | prompt speed | generation speed | value check |
|---|---:|---:|---|
| `KoHRM-Text-1.4B-Q8_0.gguf` | 25.3 t/s | 5.0 t/s | Runtime OK; useful qualitative finance QA sample |

Q8_0 output excerpt:

```text
1. **환율 변동의 영향:** 해외 주식 투자의 수익률은 주가 상승에 따른 수익뿐만 아니라 환율 변동에 따른 수익 또는 손실을 포함합니다.
...
2. **대응 방안:**
   - **환율 변동 위험 관리:** 환율 변동 위험을 줄이기 위해 환헤지 상품을 활용하거나, 분할 매수/매도 전략을 통해 환율 변동에 따른 영향을 완화할 수 있습니다.
   - **장기 투자:** 장기 투자를 통해 환율 변동의 단기적인 영향을 완화하고, 장기적인 주가 상승에 집중할 수 있습니다.
   - **분산 투자:** 다양한 국가의 주식에 분산 투자하여 특정 국가의 환율 변동 위험을 줄일 수 있습니다.
```

The full smoke-test log is in `reports/generation_tests/finance_short_q8_0.txt`.
This is a qualitative CPU runtime sample, not a benchmark or financial advice.

## Prompt Format

The source training/inference wrapper is:

```text
<|im_start|><|object_ref_start|>PROMPT<|im_end|>
```

`prepare_sft_data.py` writes the generic HRM V1Dataset layout with
`direct=<|object_ref_start|>` by default. In this patched GGUF runtime,
`llama-completion` could load the model but returned an immediate end token for
the tested prompts, while `llama-cli --single-turn` produced visible CPU token
generation. The public checkpoint is a rolling pretraining-stage model, not a
final chat/SFT model, so instruction following can still be unstable.

## GGUF Metadata

Key converted metadata:

```text
general.architecture = hrm_text
hrm_text.context_length = 4096
hrm_text.embedding_length = 1536
hrm_text.block_count = 128
hrm_text.layers_per_stack = 16
hrm_text.h_cycles = 2
hrm_text.l_cycles = 3
tokenizer.ggml.model = gpt2
tokenizer.ggml.pre = qwen2
tokenizer.ggml.bos_token_id = 2
tokenizer.ggml.eos_token_id = 35
tokenizer.ggml.padding_token_id = 0
```

## Notes

- Source model: `LLM-OS-Models/KoHRM-Text-1.4B`
- Source revision converted: `c413eee318b28e4f970f1be83698b161e60b3adb`
- `llama.cpp` base commit used for the patch: `6a257d44633d4a752183ed778b88d2924d0a6b9d`
- BF16 conversion wrote 259 tensors.
- `llama-completion` can load the model non-interactively, but in local probes it immediately returned an end token for the tested prompts. `llama-cli --single-turn` produced visible CPU token generation and is the command shown above.
