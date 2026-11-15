---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
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
pipeline_tag: image-text-to-text
base_model: LiquidAI/d1-3B
base_model_relation: quantized
tags:
- liquid
- lfm2.5
- edge
- decision
- classification
- calibration
- system-one
- multimodal
- quantized
- int8
- w8a8
- torchao
- jetson
- orin
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# d1-3B-w8a8

d1-3B-w8a8 is the **INT8 quantized** version of [d1-3B](https://huggingface.co/LiquidAI/d1-3B), a 3B parameter
**decision model**, intended for **devices with INT8 matrix multiplication (`torch._int_mm`) on INT8 tensor
cores** (e.g. NVIDIA Jetson devices, and NVIDIA GPUs from Ampere on). You give it a state (text, JSON, images, or
a mix) and a set of questions. It returns calibrated, typed answers in **one forward pass with
zero output tokens**.

> [!NOTE]
> 📖 For the model's description and benchmark results, see the base model card:
> [**LiquidAI/d1-3B**](https://huggingface.co/LiquidAI/d1-3B).

- **W8A8**: INT8 weights and INT8 activations on the language model, so its matrix products run as INT8
  matrix multiplications (`torch._int_mm`) on the GPU's INT8 tensor cores.
- **Quantized ahead of time** with [torchao](https://github.com/pytorch/ao): the checkpoint stores the INT8
  weights, and loads as INT8 with no calibration or conversion at load time.
- **Smaller**: 3.8 GB instead of 6.2 GB for the bf16 checkpoint, which leaves more memory to the rest of the
  application (on a Jetson, the GPU shares it with the CPU).

Find more information about open d1 in our [blog post](https://www.liquid.ai/blog/open-d1).

> [!NOTE]
> On other devices (CPUs, Apple silicon, AMD GPUs, NVIDIA GPUs before Ampere), use [d1-3B](https://huggingface.co/LiquidAI/d1-3B).

## 🗒️ Model Details

| Model | Parameters | Description |
|---|---|---|
| [LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) | 3.1B | General-purpose vision-language model (base) |
| [d1-3B](https://huggingface.co/LiquidAI/d1-3B) | 3.1B | Post-trained for single-pass, calibrated decisions |
| **[d1-3B-w8a8](https://huggingface.co/LiquidAI/d1-3B-w8a8)** | 3.1B | d1-3B in INT8 (W8A8), for devices with INT8 tensor cores (e.g. Jetson) |

### Quantization

| | |
|---|---|
| Method | torchao `Int8DynamicActivationInt8WeightConfig` |
| Weights | INT8, symmetric, one scale per output channel, round to nearest |
| Activations | INT8, symmetric, one scale per token, computed at run time |
| Quantized layers | the 166 linear layers of the language model (attention, short convolution and MLP projections) |
| Kept in bf16 | the vision encoder, the multimodal projector, the embeddings and the output head |

We recommend d1-3B-w8a8 wherever a pipeline on such a device needs a yes/no, a pick from named options, or a
rating: routing and triage, moderation, intent and topic classification, extraction checks, reranking,
agent guardrails, and visual inspection. It is not a chat model and does not write text.

## 🏃 How to use

The model needs a GPU where `torch._int_mm` runs on INT8 tensor cores (NVIDIA, from Ampere on, e.g. Jetson
Orin), PyTorch, and torchao. On a Jetson with JetPack 6, install PyTorch from the Jetson AI Lab index, then the
rest:

```bash
pip install --index-url https://pypi.jetson-ai-lab.io/jp6/cu126 torch torchvision triton
pip install "transformers>=5.19" "torchao>=0.18" pillow
```

On another NVIDIA GPU, `pip install torch torchvision "transformers>=5.19" "torchao>=0.18" pillow`.

The model ships its own code, so load it with `trust_remote_code=True`. Call `model.compile()`: torchao's INT8
kernels are only fast compiled.

```python
from transformers import AutoModel
from transformers.image_utils import load_image

model = AutoModel.from_pretrained("LiquidAI/d1-3B-w8a8", trust_remote_code=True).to("cuda")
model.compile(mode="reduce-overhead")

# Text: several named questions over one state, answered in one pass
questions = {
    "refund": {
        "type": "noul",
        "instructions": "Is the customer asking for a refund?",
    },
    "team": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": {
            "billing": "Charges, refunds, invoices",
            "technical": "App or site faults",
            "fraud": "Suspected unauthorised use",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this?",
        "criteria": ["Can wait", "Today", "Blocking the customer now"],
    },
}
print(model.system_one("I was charged twice this month, please refund one of them.", questions))

# Image: the photo is the whole state
image = load_image("http://images.cocodataset.org/val2017/000000039769.jpg")  # two cats on a sofa
cats = {
    "type": "choice",
    "instructions": "How many cats are there?",
    "criteria": {"one": "One", "two": "Two", "more": "Three or more"},
}
print(model.system_one(None, {"cats": cats}, images=[image]))

# Batch: many requests, packed together with no padding
tickets = ["Where is my parcel? It was due Monday.", "The app crashes when I open settings."]
print(model.system_one_batch([(t, {"team": questions["team"]}) for t in tickets]))
```

The first call with a new shape compiles it, which takes a while on a Jetson, so warm up the shapes you serve
before timing or serving.

| call | |
|---|---|
| `system_one(state, questions, images=None)` | Named questions over one state, in one pass. The state and its images are read once for all questions. |
| `system_one_batch([(state, questions[, images]), ...])` | Many requests, packed with no padding. |

A state is a string, any JSON value, or `None` when the images are the whole state.

### Questions and answers

Questions follow the Decision Index schema: `type`, `instructions`, and `criteria`.

| `type` | `criteria` | answer fields |
|---|---|---|
| `noul`: yes or no | optional: `{"true": "...", "false": "..."}` to define each side | `noul`: P(yes) |
| `choice`: one of named options | `{name: description}` | `choice`, `confidence`, `probabilities` |
| `score`: 2 to 10 ordered levels | a list of level descriptions, lowest first | `score` (the expected level), `confidence`, `probabilities`, `legend` |

Each call returns `{"answers": {name: answer}, "usage": {"input_tokens": n, "output_tokens": 0}}`.

## ⚡ Speed

Warm calls, one request at a time: a single question, three questions over one state, a 3.4k-token state and a
384 px image. The last column is throughput with 64 states packed into one pass. We measure on an NVIDIA Jetson
AGX Orin 64 GB (MAXN, JetPack 6.2, PyTorch 2.11, torchao 0.18), fastest of 5 runs. Both checkpoints run the same
code, compiled with `model.compile(mode="reduce-overhead")`:

| | one question | 3 questions, one pass | 3.4k-token state | 384 px image | 64 states, packed |
|---|---:|---:|---:|---:|---:|
| d1-3B (bf16) | 37 ms | 65 ms | 831 ms | 137 ms | 68 / s |
| **d1-3B-w8a8** | **31 ms** | **45 ms** | **562 ms** | **99 ms** | **107 / s** |

Peak memory of the process (on a Jetson, it includes the GPU's) drops from 12.4 GB to 7.9 GB.

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```bibtex
@article{liquidAI2026opend1,
  author  = {Liquid AI},
  title   = {Open d1: Edge decision models for text, vision, and audio},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {https://www.liquid.ai/blog/open-d1},
}
```

```bibtex
@article{liquidai2025lfm2,
  title   = {LFM2 Technical Report},
  author  = {Liquid AI},
  journal = {arXiv preprint arXiv:2511.23404},
  year    = {2025}
}
```
