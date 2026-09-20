---
library_name: transformers
license: cc-by-4.0
language:
- en
- fr
- de
- it
- pt
- es
pipeline_tag: text-generation
---

# helium-1-preview-2b

<!-- Provide a quick summary of what the model is/does. -->

<img src="https://huggingface.co/kyutai/moshi-1-2b/resolve/main/helium_sticker.png" width="400">

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

Helium-1 preview is a lightweight language model with 2B parameters, targeting edge and mobile devices.
It supports the following languages: English, French, German, Italian, Portuguese, Spanish.

⚠️ Helium-1 Preview is a base model, which was not fine-tuned to follow instructions or human preferences.
For most downstream use cases, the model should be aligned with supervised fine-tuning, RLHF or related methods.

- **Developed by:** Kyutai
- **Model type:** Large Language Model
- **Language(s) (NLP):** English, French, German, Italian, Portuguese, Spanish
- **License:** CC-BY 4.0

<!-- ### Model Sources [optional]

 Provide the basic links for the model.

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]  -->

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The intended use of the Helium model is research and development of natural language processing systems, including but not limited to language generation and understanding.
The model can be used in English, French, German, Italian, Portuguese and Spanish.
For most downstream use cases, the model should be aligned with supervised fine-tuning, RLHF or related methods.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model should not be used in other languages than the ones on which it was trained.
The model is not intended to be used for any malicious or illegal activities of any kind.
The model was not fine-tuned to follow instructions, and thus should not be used as such.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Helium-1 preview is a base language model, which was not aligned to human preferences.
As such, the model can generate incorrect, biased, harmful or generally unhelpful content.
Thus, the model should not be used for downstream applications without further alignment, evaluations and mitigations of risks.
<!-- Thus, it should not be used without further evaluations of risks and mitigations. -->

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import torch
from transformers import pipeline

model_id = "kyutai/helium-1-preview-2b"

pipe = pipeline(
    "text-generation", 
    model=model_id, 
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

text = pipe("Hello, today is a great day to")
```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

Helium-1 preview was trained on a mix of data including: Wikipedia, Stack Exchange, open-access scientific articles (from peS2o) and Common Crawl.

<!--#### Training Hyperparameters

- **Training regime:** [More Information Needed] -->

<!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

The model was evaluated on MMLU, TriviaQA, NaturalQuestions, ARC Easy & Challenge, Open Book QA, Common Sense QA, 
Physical Interaction QA, Social Interaction QA, HellaSwag, WinoGrande, Multilingual Knowledge QA, FLORES 200.

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

We report accuracy on MMLU, ARC, OBQA, CSQA, PIQA, SIQA, HellaSwag, WinoGrande.
We report exact match on TriviaQA, NQ and MKQA.
We report BLEU on FLORES.

#### English Results

| Benchmark | Helium-1 Preview | HF SmolLM2 (1.7B) | Gemma-2 (2.6B) | Llama-3.2 (3B) | Qwen2.5 (1.5B) |
|--------------|:------:|:------:|:------:|:------:|:------:|
| | | | | | |
| MMLU | 51.2 | 50.4 | 53.1 | 56.6 | 61.0 |
| NQ   | 17.3 | 15.1 | 17.7 | 22.0 | 13.1 |
| TQA  | 47.9 | 45.4 | 49.9 | 53.6 | 35.9 |
| ARC E | 80.9 | 81.8 | 81.1 | 84.6 | 89.7 |
| ARC C | 62.7 | 64.7 | 66.0 | 69.0 | 77.2 |
| OBQA | 63.8 | 61.4 | 64.6 | 68.4 | 73.8 |
| CSQA | 65.6 | 59.0 | 64.4 | 65.4 | 72.4 |
| PIQA | 77.4 | 77.7 | 79.8 | 78.9 | 76.0 |
| SIQA | 64.4 | 57.5 | 61.9 | 63.8 | 68.7 |
| HS | 69.7 | 73.2 | 74.7 | 76.9 | 67.5 |
| WG | 66.5 | 65.6 | 71.2 | 72.0 | 64.8 |
| | | | | | |
| Average | 60.7 | 59.3 | 62.2 | 64.7 | 63.6 |

#### Multilingual Results

| Language | Benchmark | Helium-1 Preview | HF SmolLM2 (1.7B) | Gemma-2 (2.6B) | Llama-3.2 (3B) | Qwen2.5 (1.5B) |
|-----|--------------|:------:|:------:|:------:|:------:|:------:|
| | | | | | | |
| German | MMLU | 45.6 | 35.3 | 45.0 | 47.5 | 49.5 |
| | ARC C | 56.7 | 38.4 | 54.7 | 58.3 | 60.2 |
| | HS | 53.5 | 33.9 | 53.4 | 53.7 | 42.8 |
| | MKQA | 16.1 | 7.1 | 18.9 | 20.2 | 10.4 |
| | FLORES | 33.9 | 12.2 | 30.7 | 28.2 | 20.8 |
| Spanish | MMLU | 46.5 | 38.9 | 46.2 | 49.6 | 52.8 |
| | ARC C | 58.3 | 43.2 | 58.8 | 60.0 | 68.1 |
| | HS | 58.6 | 40.8 | 60.5 | 61.1 | 51.4 |
| | MKQA | 16.0 | 7.9 | 18.5 | 20.6 | 10.6 |
| | FLORES | 25.7 | 15.0 | 25.7 | 23.7 | 20.4 |
| French | MMLU | 46.0 | 37.7 | 45.7 | 48.8 | 51.9 |
| | ARC C | 57.9 | 40.6 | 57.5 | 60.1 | 67.4 |
| | HS | 59.0 | 41.1 | 60.4 | 59.6 | 51.2 |
| | MKQA | 16.8 | 8.4 | 18.4 | 19.6 | 9.7 |
| | FLORES | 44.3 | 20.0 | 43.3 | 39.3 | 31.2 |
| Italian | MMLU | 46.1 | 36.3 | 45.6 | 48.8 | 50.5 |
| | ARC C | 57.4 | 39.1 | 53.9 | 60.1 | 64.6 |
| | HS | 55.2 | 37.7 | 56.2 | 56.8 | 46.8 |
| | MKQA | 15.3 | 6.3 | 18.0 | 19.0 | 9.9 |
| | FLORES | 25.8 | 10.4 | 25.2 | 23.8 | 16.4 |
| Portuguese | MMLU | 46.2 | 37.7 | 45.6 | 49.2 | 53.0 |
| | ARC C | 56.8 | 40.6 | 57.0 | 62.1 | 66.6 |
| | HS | 57.3 | 41.0 | 58.7 | 59.1 | 50.9 |
| | MKQA | 14.7 | 6.6 | 16.9 | 19.1 | 9.2 |
| | FLORES | 43.0 | 20.0 | 43.6 | 40.5 | 33.0 |
| | | | | | | |
| | Average | 42.1 | 27.8 | 42.3 | 43.6 | 40.0

## Technical Specifications

### Model Architecture and Objective

| Hyperparameter | Value |
|--------------|:------:|
| Layers | 24 |
| Heads  | 20 |
| Model dimension | 2560 |
| MLP dimension | 7040 |
| Context size | 4096 |
| Theta RoPE | 100,000 |

#### Hardware

The model was trained on 128 NVIDIA H100 Tensor Core GPUs.

#### Software

The model was trained using Jax.

## Citation

Blog post: https://kyutai.org/2025/01/13/helium.html
