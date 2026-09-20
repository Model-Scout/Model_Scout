---
language:
  - "no"  # Generic Norwegian
  - "nb"  # Norwegian Bokmål
  - "nn"  # Norwegian Nynorsk
  - "en"  # English
tags:
  - "llama"
  - "notram"
  - "norwegian"
  - "bokmål"
  - "nynorsk"
  - "multilingual"
  - "conversational"
  - "text-generation"
pipeline_tag: "text-generation"
license: "llama3.1"
base_model: "meta-llama/Llama-3.1-8B-Instruct"
library_name: "transformers"
---

## Model Card: "nb-notram-llama-3.1-8b-instruct"

### Model overview

"NbAiLab/nb-notram-llama-3.1-8b-instruct" is part of the "NB-Llama-3.x" series (covering "Llama 3.1", "Llama 3.2", and "Llama 3.3" based releases) and the "NoTraM" line of work, trained on top of Meta’s "Llama-3.1-8B-Instruct":
https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

The model is fine-tuned to improve instruction-following behavior in Norwegian Bokmål and Norwegian Nynorsk, while aiming to preserve strong English performance.

This release is an experiment in how far modern open-weight models can be adapted for Norwegian using **only publicly available data**. Although trained at the National Library of Norway, it does **not** include material that is only accessible through legal deposit. It may include public documents (for example governmental reports) that are publicly available and also part of legal deposit collections.

---

### Key features

- **Base model:** "Llama-3.1-8B-Instruct"
- **Languages:**
  - Strong: Norwegian Bokmål ("nb"), Norwegian Nynorsk ("nn"), English ("en")
- **Alignment recipe (high level):**
  - Primarily supervised fine-tuning ("SFT") for instruction-following and chat formatting.
  - A **very light** preference optimization step ("DPO") was applied mainly to stabilize instruction-following; note that the starting point ("Llama-3.1-8B-Instruct") is already preference-tuned by the base model provider.
- **Response style:** the model tends to produce **shorter, more concise answers** than many chatty assistants. This reflects the current instruction-tuning recipe and training mix. The behavior can be adjusted with an additional alignment round (for example "GRPO") to encourage more elaborate, conversational responses if desired.

---

### Motivation and research framing

Adapting instruction-tuned models to Norwegian can be approached in two broad ways:

1) **Adapt a base model first, then instruction-tune.**  
This tends to improve core Norwegian language modeling reliably, but producing a strong instruction-tuned assistant usually requires substantial alignment work and high-quality supervised data.

2) **Start from an instruction-tuned model, then adapt further.**  
This leverages general instruction-following behaviors already learned by large multilingual models. In practice, however, it can be difficult to add *generalizable* Norwegian cultural and historical knowledge at this late stage using only supervised instruction data. We have observed a failure mode where new knowledge becomes brittle and overly prompt-dependent—usable in narrow contexts, but not reliably accessible across phrasing and tasks. Internally we refer to this as "knowledge pocketing".

Within the "NoTraM" project, we explore techniques for adapting instruction-tuned models to Norwegian language, culture, and history while explicitly trying to reduce "knowledge pocketing" and improve generalization. This line of work is intentionally distinct from the "NB-GPT" approach, which primarily targets training from scratch or from base models using established pretraining-first recipes.

For smaller languages, fully closed post-training pipelines are rarely reproducible. Public-data approaches are therefore a pragmatic path to improving Norwegian-capable models—while being explicit about limitations and the remaining gap to highly resourced multilingual instruction-tuned systems.

---

### Model details

- **Developer:** "National Library of Norway (NB-AiLab)"
- **Parameters:** "8B"
- **Knowledge cutoff:** "May 2024" (practical guideline; the model may be incomplete or incorrect on specific facts)
- **License:** "Llama 3.1 Community License"
  - "https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE"

---

## Intended use

### Suitable for

- Dialogue systems and assistant-style applications in Norwegian ("nb"/"nn") and English ("en")
- Summarization and Q&A in Bokmål or Nynorsk

### Out of scope

- Use in violation of applicable laws or regulations
- High-stakes domains (medical/legal/financial) without additional controls, evaluation, and human oversight
- Reliance on the model as a sole source of truth (it can hallucinate)

---

## How to use

This is a research release. For end-user deployments, we recommend careful evaluation in your target setting. Quantized variants (when provided) typically run faster with minimal loss in quality on many platforms. When fine-tuning instruction-tuned Llama models, best results usually require using the correct "Llama 3.1" chat templates.

### Using "transformers" (pipeline)

```python
import torch
from transformers import pipeline

model_id = "NbAiLab/nb-notram-llama-3.1-8b-instruct"

pipe = pipeline(
    task="text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Hvem døde på Stiklestad?"},
]

outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1])
```

---

## Training data

### Overview

Training is based entirely on publicly available datasets and synthetically generated data.

For more details on the base model’s pretraining data and data selection, see:
https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

### Public datasets (partial use)

- "CulturaX"  
  https://huggingface.co/datasets/uonlp/CulturaX
- "HPLT monolingual v1.2"  
  https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2
- "Norwegian Colossal Corpus (NCC)"  
  https://huggingface.co/datasets/NCC/Norwegian-Colossal-Corpus
- "Wikipedia"  
  https://huggingface.co/datasets/wikimedia/wikipedia

### Alignment data sources ("SFT" + light preference optimization)

- "Magpie" (English)  
  https://huggingface.co/Magpie-Align
- "Anthropic Helpful and Harmless" (used lightly)  
  https://huggingface.co/datasets/Anthropic/hh-rlhf
- Various synthetic and translated datasets derived from the above

---

## Data selection and quality filtering

Only a small subset of raw web-scale data was used. We used the "FineWeb" approach as inspiration for large-scale web data curation and filtering, and applied similar principles when selecting and filtering public data:
https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1

In addition, we trained "Corpus Quality Classifiers" (educational value + linguistic quality) based on "NbAiLab/nb-bert-base" and release them as part of the broader "NB-Llama" effort:

- **Classifier collection:**  
  https://huggingface.co/collections/NbAiLab/corpus-quality-classifier-673f15926c2774fcc88f23aa

- **What we optimize for:**
  - **Educational value:** prioritize content likely to improve reasoning and usefulness.
  - **Linguistic quality:** prioritize well-formed, clear language (important for Norwegian norms and orthography).

---

## EU AI Act transparency note

To support transparency obligations under the EU AI Act, this model card documents:

- **Model lineage:** the "base_model" is listed in the metadata and linked above.
- **Primary training data sources:** the main public datasets used (see "Training data" and links).
- **Curation methodology:** we explicitly state that our data selection and filtering is guided by the "FineWeb" approach and we provide a public reference.
- **Filtering tools:** we link to the released "Corpus Quality Classifiers" used to score educational value and linguistic quality.

The training data used for this release is restricted to **publicly available sources** as described above (no legal-deposit-only material).

---

## Limitations and known issues

- The model can produce incorrect statements, fabricated details, or plausible-sounding but wrong explanations.
- Norwegian cultural/historical knowledge may be uneven; some knowledge can appear "pocketed" (prompt-sensitive) depending on topic and phrasing.
- Safety alignment is limited by the scope of the released recipe and data; evaluate carefully for your use case.

---

## Licensing

The model is released under the "Llama 3.1 Community License":
https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE

Refer to the "Acceptable Use Policy" for restrictions:
https://llama.meta.com/llama3.1/use-policy

---

## Citing & authors

Model training and documentation: **Per Egil Kummervold**.

---

## Funding and acknowledgement

Training was supported by Google’s TPU Research Cloud ("TRC"), which provided Cloud TPUs essential for the computational work.
