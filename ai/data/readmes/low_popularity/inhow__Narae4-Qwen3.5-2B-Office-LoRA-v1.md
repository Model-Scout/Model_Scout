---
language: [ko, en]
license: other
license_name: apache-2.0-and-lfm1.0-components
license_link: https://huggingface.co/inhow/Narae4-Qwen3.5-2B-Office-LoRA-v1/blob/main/COMPONENT_LICENSES.md
library_name: peft
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3.5-2B
base_model_relation: adapter
tags: [gguf, lora, narae4, qwen3_5, tool-calling, experimental]
---
# 나래4 / Narae4-Qwen3.5-2B-Office-LoRA-v1

Korean office agent model for **Narae Hangul Office**. This is the adopted,
actually weight-trained **v1 LoRA**, with GGUF inference files and the original
PEFT adapter. Recent school-accounting automation is an application/runtime
improvement; it is not a new weight-trained v2 model.

## 구성 / Components

- Main model: [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B).
- Quantized base and F16 visual projector: unmodified files from
  [unsloth/Qwen3.5-2B-GGUF](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF/tree/f6d5376be1edb4d416d56da11e5397a961aca8ae).
- Trained component: Office LoRA v1, strength **1.0**, last full-attention block 23.
- Included decision companion: `d1-2B-Q4_K_M.gguf`, an unchanged copy from
  [LiquidAI/d1-2B-GGUF](https://huggingface.co/LiquidAI/d1-2B-GGUF/tree/e968f6575f0d4fad928312d7af15cad90fd365c0).
  The pretrained companion has its own [LFM Open License v1.0](D1-LICENSE).
  All four runtime files are included so a download contains the tested setup.
- Visual encoder/projector and decision companion weights were **not trained by Narae**.
- The application routes components when needed. This is **not a jointly trained sparse MoE**.

## 실제 학습 / Actual training

| Item | Recorded result |
|---|---|
| Synthetic training / validation dialogues | 32 / 3 |
| Epochs / optimizer updates | 2 / 16 |
| Trainable parameters / changed tensors | 638,976 / 14 |
| LoRA rank / alpha | 16 / 32 |
| Validation loss before / after | 1.570969 / 1.550289 |
| Fixed held-out next-action score before / after | 7/8 / 7/8 |

The held-out accuracy did not improve. Later v2 candidates were not adopted.
The GGUF adapter's 14 tensors were checked bit-for-bit against the saved trained
adapter. Frozen BF16 training versus Q4_K_M inference is a quantization difference.
Training scripts and synthetic dataset hashes are in the
[reproduction folder](https://github.com/y5496694/Narae_hangul_office/tree/6d732d5e3b69e8598014cf2904fb27ff112050d4/experiments/narae4-office-20261031).

## 사용 / Use

For one-click installation of all four files, use Narae Hangul Office
**preview.25 or later**. The [preview.25 application source](https://github.com/y5496694/Narae_hangul_office/tree/b9d03f5671c4821a24fd50b31d6452aec03f97ae)
includes the pinned download catalog. Select **나래4** in the local AI settings
and install its verified files. New installations select Narae4 by default;
existing explicit AI choices are preserved.
The application verifies SHA256, the loaded model alias and the actual LoRA.
Tool execution, Hangul/Windows integration and authenticated school UI access
require the application and the user's own local setup; weights alone do not
provide those tools or authorization.

For llama.cpp, download the GGUF base and adapter and always load both:

```sh
llama-server --model Qwen3.5-2B-Q4_K_M.gguf --lora Narae4-Qwen3.5-2B-Office-LoRA-v1-f32.gguf --alias Narae4-Qwen3.5-2B-Office-LoRA-v1 --host 127.0.0.1 --ctx-size 8192 --gpu-layers 0 --jinja
```

Add `--mmproj mmproj-F16.gguf --no-mmproj-offload` for image input.
Use a llama.cpp build supporting Qwen3.5 and its visual projector. The PEFT
adapter pins the original Qwen base revision in `adapter_config.json`; the full
Transformers base is not included. See the
[runtime and workflow guide](https://github.com/y5496694/Narae_hangul_office/blob/6d732d5e3b69e8598014cf2904fb27ff112050d4/docs/school-accounting.md).

## 실행 검증과 한계 / Evaluation and limitations

On 2026-11-01 the v1 model with the preview.24 runtime completed one explicitly
authorized synthetic 1-won requisition cycle: enter, choose an observed budget,
enter an item, attach original bytes, save, reopen from a server query, verify
attachment bytes/SHA256, delete, and verify absence in a fresh query. It took
20 tool stages and 131.296 seconds; the test record was deleted. Approval
submission and actual purchasing/payment were not performed. This measures
the **model plus bounded runtime/controller**, not free-form model-only autonomy.

Earlier synthetic document/vision smoke tests and the above single integration
run do not establish general school-work accuracy. Missing budget choices,
ambiguous document identities and uncertain writes stop the workflow. Current
financial approval submission, arbitrary existing-record deletion, multiple
budgets and complete virtualized-grid traversal are not validated capabilities.
See `evaluation-summary.json` for the distinct training and runtime evidence.

No real school documents, student/staff identities, portal screenshots, sessions,
credentials, private conversations or live execution logs are included.

## 파일 / Files

| File | Bytes | SHA256 |
|---|---:|---|
| Qwen3.5-2B-Q4_K_M.gguf | 1280835840 | `aaf42c8b7c3cab2bf3d69c355048d4a0ee9973d48f16c731c0520ee914699223` |
| Narae4-Qwen3.5-2B-Office-LoRA-v1-f32.gguf | 2557408 | `19f20486e744bcb9636efcdaf6583c1b9bef545733987a8837e63afdfeecf105` |
| mmproj-F16.gguf | 668227264 | `7035e9cb8d7c6a9681d07eef9a364783e86ea4cd73faab2eabb4f43a101830c7` |
| d1-2B-Q4_K_M.gguf | 1099629888 | `adca5789ad30ae6027e8e936749bb9f19673097492ab26fa1c5b69643ca50b4b` |
| adapter_model.safetensors | 2557984 | `3380c0dfbee1737fa7f741d5ec475efdbfbba15206e78373a93592f4c745fc4d` |
| adapter_config.json | 1253 | `70151bec3a55e5b846976b58a3f778427716947fe3e2001deec569a5a762c4c7` |

## 라이선스 / License

The Qwen-derived files and Narae LoRA use **Apache-2.0**;
retain [LICENSE](LICENSE) and [NOTICE](NOTICE). The included LiquidAI companion
uses **LFM Open License v1.0** in [D1-LICENSE](D1-LICENSE).
See [COMPONENT_LICENSES.md](COMPONENT_LICENSES.md) for the file-specific terms.
The application's MIT license does not replace the model licenses.
