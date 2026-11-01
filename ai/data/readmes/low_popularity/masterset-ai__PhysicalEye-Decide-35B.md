---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- ko
- zh
tags:
- jev
- decision
- decision-engine
- calibrated
- calibration
- probability
- vision
- vision-language
- multimodal
- vlm
- image-classification
- zero-shot-image-classification
- zero-shot-classification
- visual-question-answering
- multiple-choice
- yes-no
- scoring
- visual-inspection
- quality-control
- defect-detection
- industrial-inspection
- food-inspection
- agriculture
- egg
- robotics
- physical-ai
- edge-ai
- document-understanding
- screen-understanding
- moe
- mixture-of-experts
- qwen3_5_moe
- qwen3.5
- multilingual
- korean
- chinese
---

<div align="center">

# 👁️ PhysicalEye-Decide-35B

### Show it an image. Ask a question. Get a calibrated decision in one forward pass.

[![Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Live%20Demo-PhysicalEye--Decide--35B-ffcc4d)](https://huggingface.co/spaces/masterset-ai/PhysicalEye-Decide-35B-demo)
[![Base model](https://img.shields.io/badge/Base-Darwin--35B--A3B-6f42c1)](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus)
[![Family](https://img.shields.io/badge/PhysicalEye-35B-ff7a59)](https://huggingface.co/masterset-ai/PhysicalEye-35B)
[![GitHub](https://img.shields.io/badge/GitHub-PhysicalEye--Decide-181717?logo=github)](https://github.com/masterset-ai/PhysicalEye-Decide)
[![License](https://img.shields.io/badge/License-Apache%202.0-2ea44f)](https://www.apache.org/licenses/LICENSE-2.0)

</div>

---

## What it is

PhysicalEye-Decide-35B is a **decision engine for images**. You give it an image, a question and the possible answers. It returns a probability for every answer.

It does not generate text. It reads the input once and scores every option directly. That makes it:

- **Fast**: about 0.05 seconds per decision on one GPU.
- **Predictable**: the answer is always one of your options. No parsing, no free text.
- **Calibrated**: the probability is meant to be used. Set a threshold, route low-confidence cases to a person, and log every score.

## Results

| Test | Setting | Result |
|---|---|---|
| **Egg inspection** | Held-out test, 100 candling photos, good vs bad | **98.0%** accuracy, mean confidence 0.964 |
| **AI2D** | 200 science diagram questions, 4 options | **87.0%** (chance 25%) |
| **Speed** | Median latency per decision, batched server, one B200 GPU | **0.051 s** (p80 0.068 s) |

## Where to use it

| Area | Example question | Type |
|---|---|---|
| Food and farm inspection | "Is this egg good or bad?" | `choice` |
| Factory quality control | "Is there a crack on this part?" | `noul` |
| Retail and logistics | "Which product is on the shelf?" | `choice` |
| Documents and screens | "Is the total on this receipt above 50?" | `noul` |
| Robots and edge devices | "Is the gripper holding the object?" | `noul` |
| Rating and triage | "How damaged is this package, from 0 to 10?" | `score` |

Try these in the **[live demo](https://huggingface.co/spaces/masterset-ai/PhysicalEye-Decide-35B-demo)**: a real-time inspection line, a sample gallery and a playground in English, Korean and Chinese.

## Quick start

```bash
pip install -U torch transformers accelerate safetensors pillow huggingface_hub
wget https://huggingface.co/masterset-ai/PhysicalEye-Decide-35B/resolve/main/decide.py
```

```python
from decide import Decider

d = Decider("masterset-ai/PhysicalEye-Decide-35B")   # downloads about 69 GB on first use

result = d.decide(
    images=["egg.jpg"],
    state="Candling photo: a light is shone through the egg in a dark room.",
    question={
        "type": "choice",
        "instructions": "Is this egg good or bad?",
        "criteria": {"good": "Normal, healthy egg", "bad": "Defective, spoiled or damaged egg"},
    },
)
print(result)
# {"type": "choice", "choice": "good", "confidence": ..., "probabilities": {"good": ..., "bad": ...}}
```

From the command line:

```bash
python decide.py --image egg.jpg --instructions "Is this egg good or bad?" --options good bad
python decide.py --image part.jpg --instructions "Is there a crack on this part?"   # yes/no
```

**Hardware**: the weights are about 69 GB in bfloat16. Use one GPU with 80 GB or more memory (for example H100 80GB, H200, B200), or spread the model over several GPUs.

## Question types

Every call takes up to **4 images**, a context string (`state`) and one question.

| Type | Fields | Returns |
|---|---|---|
| `choice` | `instructions`, `criteria`: a dict of option name to description (or `null`) | `choice`, `confidence`, `probabilities` |
| `noul` | `instructions`, optional `criteria`: `{"true": ..., "false": ...}` | `noul`: probability of yes |
| `score` | `instructions`, `criteria`: a list of level descriptions, lowest first | `score` (expected level), `confidence`, `probabilities` |

```python
# yes / no
d.decide(images=["part.jpg"], state="Steel bracket on a conveyor.",
         question={"type": "noul", "instructions": "Is there a visible crack?"})
# {"type": "noul", "noul": ...}

# score on a scale
d.decide(images=["box.jpg"], state="Parcel at the receiving dock.",
         question={"type": "score", "instructions": "How damaged is this package?",
                   "criteria": ["no damage", "minor dents", "torn or crushed", "destroyed"]})
# {"type": "score", "score": ..., "confidence": ..., "probabilities": {...}, "legend": {...}}
```

### Tips

- **Describe each option in plain words** in `criteria`. Short, concrete descriptions work best.
- **Put fixed context in `state`**, such as the camera setup or the product type. Keep `instructions` short.
- **Use the probability.** Accept high-confidence decisions automatically and send the rest to a person.
- Up to 255 options per question.

## How it works

1. A vision-language Mixture-of-Experts backbone reads the images, the context and the question together. It has 35B parameters in total and about 3B active per token, so it runs fast for its size.
2. A small decision readout on top of the backbone scores every option in the same forward pass.
3. A calibration temperature turns the scores into probabilities you can threshold.

## Files

| File | Content |
|---|---|
| `model-0000X-of-00015.safetensors` | Backbone weights |
| `readout.safetensors` | Decision readout |
| `decision_config.json` | Option codes, token ids and calibration temperature |
| `decide.py` | Self-contained inference code (Apache-2.0). Examples: [GitHub](https://github.com/masterset-ai/PhysicalEye-Decide) |
| `config.json`, `processor_config.json`, `tokenizer*`, `chat_template.jinja` | Model, image processor and tokenizer settings |

## Model family

| Model | Role |
|---|---|
| [PhysicalEye-35B](https://huggingface.co/masterset-ai/PhysicalEye-35B) | First-person video understanding |
| **PhysicalEye-Decide-35B** | Image and text decisions with calibrated probabilities |

## Base model and license

- Built on [FINAL-Bench/Darwin-35B-A3B-Opus](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus), a Qwen3.5 MoE based vision-language model.
- Released under the **Apache-2.0** license. The upstream Qwen license notice applies to the base weights.

## Training data credits

The decision readout was trained only on openly licensed data. We thank the authors of:

- **VQAv2** (CC BY 4.0, annotations) and **COCO** captions and instances 2017 (CC BY 4.0, annotations; images keep their Flickr licenses)
- **TextVQA 0.5.1** (CC BY 4.0), **ScreenQA**, **RICO-SCA** and **Screen2Words** on RICO (CC BY 4.0)
- **CLEVR v1.0** (CC BY 4.0), **A-OKVQA** (Apache-2.0), **VSR** (CC BY 4.0), **CORD v2** (CC BY 4.0)
- **Open-Jev** (CC0 1.0), **MMLU auxiliary train** (MIT), synthetic charts made in-house
- **Good and Bad Eggs Identification Image Dataset**, Md Mafiul Hasan Matin, Marium Jahan, Md. Saroar Jahan, Mendeley Data, doi:10.17632/mdty358x8m.1 (CC BY 4.0)

## Citation

```bibtex
@misc{physicaleye_decide_35b,
  title  = {PhysicalEye-Decide-35B: One-Pass Calibrated Image Decisions},
  author = {MASTERSET},
  year   = {2026},
  url    = {https://huggingface.co/masterset-ai/PhysicalEye-Decide-35B}
}
```
