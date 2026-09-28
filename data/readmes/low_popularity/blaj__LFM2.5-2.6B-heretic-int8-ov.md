---
library_name: openvino
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - heretic-org/LFM-2.5-2.6B-heretic
  - LiquidAI/LFM2.5-2.6B
pipeline_tag: text-generation
language:
  - en
  - ar
  - zh
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - pl
  - pt
  - ru
  - es
  - th
  - vi
tags:
  - openvino
  - int8
  - intel
  - arc
  - lfm2.5
  - heretic
  - uncensored
  - abliterated
---

# LFM2.5-2.6B-heretic int8 OpenVINO IR

An int8 OpenVINO IR conversion of
[heretic-org/LFM-2.5-2.6B-heretic](https://huggingface.co/heretic-org/LFM-2.5-2.6B-heretic),
which is itself a decensored (abliterated) build of
[LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) produced with
[Heretic](https://heretic-project.org) v1.4.0.

This repository contains the converted OpenVINO IR only. No weight values were
modified beyond int8 weight compression — the abliteration is inherited from the
source model.

## Conversion details

| Property | Value |
| --- | --- |
| Source | `heretic-org/LFM-2.5-2.6B-heretic` (BF16 safetensors) |
| Tool | `optimum-cli export openvino` (optimum-intel 2.2.0) |
| Task | `text-generation-with-past` |
| Weight format | `int8` (asymmetric, per-channel) |
| Compression | NNCF — 189/189 weight layers int8_asym |
| Transformers | 5.4.0 (required pin; optimum-intel rejects newer at export) |
| Repository size | 2.7 GB |

## Files

```text
openvino_model.xml / .bin          # main graph + int8 weights
openvino_tokenizer.xml / .bin      # tokenizer
openvino_detokenizer.xml / .bin    # detokenizer
config.json                        # model architecture config
generation_config.json
chat_template.jinja
tokenizer.json
openvino_config.json               # records export + quantization settings
LICENSE                            # LFM Open License v1.0
```

## Usage

### OpenVINO GenAI

```python
import openvino_genai as og

pipe = og.LLMPipeline("lfm2.5-2.6b-heretic-int8-ov", "GPU")
config = og.GenerationConfig(max_new_tokens=256, temperature=0.7)

print(pipe.generate("User: Hello\nAssistant:", config))
```

### OpenAI-compatible serving (OVMS)

```bash
ovms --configure --model_path ./lfm2.5-2.6b-heretic-int8-ov --task text_generation
ovms --model_path ./lfm2.5-2.6b-heretic-int8-ov --task text_generation --rest_port 11436
```

The model is then available at `http://127.0.0.1:11436/v1/chat/completions`.

## Chosen format: int8, not int4

Abliteration removes the refusal direction from the model's weights. Aggressive
quantization can erode other capabilities along with it, so int8 is used here to
preserve more of the source model's behavior. int4 would roughly halve the size
again at a larger quality cost — see the [int4 sibling](https://huggingface.co/blaj/LFM2.5-2.6B-heretic-int4-ov).

## Verifying the conversion

The IR was tested by loading it through `openvino_genai.LLMPipeline` on an Intel
Arc iGPU and running generation before publication. If you re-convert, do the
same — a successful export does not guarantee a model that produces coherent
output.

## Reproducing

```bash
pip install optimum[openvino] nncf
pip install "transformers==5.4.0"   # hard requirement of the export gate

optimum-cli export openvino \
  --model heretic-org/LFM-2.5-2.6B-heretic \
  --task text-generation-with-past \
  --weight-format int8 \
  ./lfm2.5-2.6b-heretic-int8-ov
```

## Benchmark

Single-stream, Intel Core Ultra 7 258V (Arc 130V/140V iGPU), 30 GB RAM,
OpenVINO Model Server 2026.4.0 on GPU:

| Metric | This build (int8) | Sibling build |
| --- | --- | --- |
| Throughput | **26.3 tok/s** | 42.5 tok/s |
| Model size | 2.7 GB | 1.6 GB |

Full configuration, hardware detail and methodology: [BENCHMARK.md](./BENCHMARK.md).

### Cross-model reference

Same harness, same hardware:

| Model | Precision | tok/s |
| --- | --- | --- |
| lfm2.5-8b-a1b (non-abliterated) | int4 | 68.7 |
| lfm2.5-8b-a1b-heretic | int4 | 67.3 |
| lfm2.5-2.6b-heretic | int4 | 42.5 |
| lfm2.5-8b-a1b-heretic | int8 | 34.8 |
| lfm2.5-2.6b-heretic | int8 | 26.3 |
| gemma4-e4b | int4 | 24.0 |
| qwen3.5-9b (+ DFlash draft) | int4 | 23.6 |

The 8B A1B is a mixture-of-experts model and decodes faster than the 2.6B dense
model despite the larger checkpoint, because fewer parameters are active per
token. Figures in this table are from one canonical run of
`benchmark_ov_models.py`; expect a few percent variance between runs.

## Attribution

- Base model: [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) (LFM Open License v1.0)
- Abliteration: [heretic-org/LFM-2.5-2.6B-heretic](https://huggingface.co/heretic-org/LFM-2.5-2.6B-heretic)
- Conversion: OpenVINO IR via `optimum-intel`

Redistribution is permitted under the LFM Open License v1.0, which is included
verbatim in this repository. The license's commercial-use threshold applies to
this Derivative Work as it does to the source.

## Intended use

Research and local inference. Abliterated models have reduced refusal behavior;
outputs should be evaluated accordingly and not deployed without appropriate
consideration.
