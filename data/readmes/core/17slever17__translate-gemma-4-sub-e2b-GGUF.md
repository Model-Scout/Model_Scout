---
license: apache-2.0
language:
  - en
  - ru
  - de
  - es
  - ja
  - fr
  - pt
  - zh
  - nl
  - it
  - ko
library_name: llama.cpp
pipeline_tag: image-text-to-text
base_model:
  - 17slever17/translate-gemma-4-sub-e2b
base_model_relation: quantized
tags:
  - gemma4
  - translation
  - subtitle-translation
  - multilingual
  - context-aware-translation
  - conversational-translation
  - unsloth
  - gguf
---

<p align="center">
  <img src="https://huggingface.co/17slever17/translate-gemma-4-sub-e2b-GGUF/resolve/main/assets/translate-gemma-sub-banner.png"
       alt="Translate Gemma 4 Sub"
       width="100%">
</p>

# Translate Gemma 4 Sub

**Translate Gemma 4 Sub** is a multilingual Gemma 4 fine-tune specialized for both general translation and context-aware subtitle translation.

👉🏻 The models are used by [**SubWave**](https://github.com/17slever17/SubWave), an open-source realtime subtitle translator. 👈🏻

The model supports ordinary source-to-target translation as well as subtitle translation with previous source and translated segments provided as context. It is optimized to preserve meaning, tone, slang, uncertainty, repetitions, incomplete speech, and natural/official conversational style.

### Why not use [google/translategemma-4b-it](https://huggingface.co/google/translategemma-4b-it)?

Subtitle translation often requires previous context because phrases may be split across segments or lose their meaning when translated in isolation. Translate Gemma 4 Sub can use previous source and translated subtitles as context, while also supporting custom style instructions, speaker information, terminology rules, glossaries, and other translation constraints.

Other instruction-following translation models, such as [tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B), performed even worse than the base Gemma 4 model in our evaluation.

## Available formats

### E4B:

- **Transformers:** [**Translate Gemma 4 Sub E4B**](https://huggingface.co/17slever17/translate-gemma-4-sub-e4b)
- **GGUF:** [**Translate Gemma 4 Sub E4B GGUF**](https://huggingface.co/17slever17/translate-gemma-4-sub-e4b-GGUF)

### E2B:

- **Transformers:** [**Translate Gemma 4 Sub E2B**](https://huggingface.co/17slever17/translate-gemma-4-sub-e2b)
- **GGUF:** [**Translate Gemma 4 Sub E2B GGUF**](https://huggingface.co/17slever17/translate-gemma-4-sub-e2b-GGUF)

## Intended use

The model is especially optimized for live and conversational speech, including streaming content, where meaning often depends on previous lines, speaker intent, tone, and incomplete context. It performs particularly well when previous source and translated segments are supplied and can follow additional user instructions that define the desired style, tone, or level of formality.

Translate Gemma 4 Sub retains the language coverage of the underlying Gemma 4 model. The most extensively trained languages are:

- **Tier 1:** English, Russian, Spanish, German and Japanese;
- **Tier 2:** French, Portuguese, Chinese, Dutch, Italian, and Korean.

Other languages supported by Gemma 4 may also work, but they have not undergone specific translation fine-tuning and have not been evaluated as extensively.

## Benchmark results

All models in the following table were evaluated in GGUF Q4 format under the same generation and evaluation pipeline.

Higher is better for **chrF++**, **BERTScore**, **COMET-DA**, and **COMETKiwi**. Lower is better for **MetricX Ref** and **MetricX QE**.

| Model                                 |    chrF++ ↑ |  BERTScore ↑ |   COMET-DA ↑ |  COMETKiwi ↑ | MetricX-24 Ref ↓ | MetricX-24 QE ↓ |
| ------------------------------------- | ----------: | -----------: | -----------: | -----------: | ---------------: | --------------: |
| **Translate Gemma 4 Sub E4B Q4_K_XL** | **51.8218** | **0.867594** | **0.835393** |     0.745391 |       **2.7074** |          2.8150 |
| Translate Gemma 4 Sub E2B Q4_K_XL     |     49.1003 |     0.857130 |     0.822867 |     0.741567 |           3.1002 |          3.0091 |
| Gemma 4 12B QAT Q4_K_XL               |     51.5596 |     0.855906 |     0.828904 | **0.758124** |           2.8813 |      **2.7447** |
| Gemma 4 E4B Q4_K_XL                   |     48.4846 |     0.848822 |     0.811101 |     0.752102 |           3.2390 |          3.0889 |
| Gemma 4 E2B Q4_K_XL                   |     45.0172 |     0.836204 |     0.782135 |     0.732084 |           3.8652 |          3.3755 |

The evaluation set was independent from the training data. Its reference translations were prepared from randomly selected stream segments that were not used during training.

### MetricX-24 Ref by target language

Scores are grouped by target language. Lower is better.

| Model                                 | Russian ↓ | English ↓ | Japanese ↓ | Spanish ↓ |  German ↓ |
| ------------------------------------- | --------: | --------: | ---------: | --------: | --------: |
| **Translate Gemma 4 Sub E4B Q4_K_XL** | **2.997** | **2.512** |      2.809 | **2.805** |     2.217 |
| Translate Gemma 4 Sub E2B Q4_K_XL     |     3.100 |     2.573 |      3.138 |     2.901 |     2.370 |
| Gemma 4 12B QAT Q4_K_XL               |     3.252 |     2.619 |  **2.737** |     2.921 | **2.165** |
| Gemma 4 E4B Q4_K_XL                   |     3.477 |     2.687 |      3.172 |     3.310 |     2.694 |
| Gemma 4 E2B Q4_K_XL                   |     4.108 |     3.270 |      3.522 |     3.646 |     2.948 |

## Prompt format

The model was trained with a system message that specifies the source language, target language, subtitle task, and style.

### System message

```text
TASK: Translate {source_language} subtitles into {target_language}.
RULES: Speakers name: ...; speaker gender: ...; other rules.
STYLE: friendly/official/neutral.
Translate only CURRENT_SOURCE. PREVIOUS_SOURCE and PREVIOUS_TRANSLATION are context only. Preserve meaning, tone, slang, profanity, uncertainty, repetitions and incomplete speech. Return only the final translation without labels or commentary.
```

### User message

```text
[PREVIOUS_SOURCE]
Previous source-language subtitles context.

[PREVIOUS_TRANSLATION]
Previous translated subtitles context.

[CURRENT_SOURCE]
The subtitle segment to translate.
```

Only `CURRENT_SOURCE` should be translated. `PREVIOUS_SOURCE` and `PREVIOUS_TRANSLATION` are context only.

The previous-context blocks may be omitted when no context is available:

```text
[CURRENT_SOURCE]
The subtitle segment to translate.
```

### Example

System message:

```text
TASK: Translate English subtitles into Russian.
RULES: speaker gender: female.
STYLE: friendly.
Translate only CURRENT_SOURCE. PREVIOUS_SOURCE and PREVIOUS_TRANSLATION are context only. Preserve meaning, tone, slang, profanity, uncertainty, repetitions and incomplete speech. Return only the final translation without labels or commentary.
```

User message:

```text
[PREVIOUS_SOURCE]
I thought you said you weren't coming.

[PREVIOUS_TRANSLATION]
Я думала, ты сказала, что не придёшь.

[CURRENT_SOURCE]
Yeah, well... I changed my mind.
```

Expected response:

```text
Ну да... Я передумала.
```

### FLORES-200 general translation benchmark

Evaluation was performed on FLORES-200 using MetricX-24 QE. Lower is better.

| Model                     | Mean error ↓ |   Median ↓ |      P90 ↓ |
| ------------------------- | -----------: | ---------: | ---------: |
| Gemma 4 12B QAT           |   **1.8811** | **1.5391** | **3.5938** |
| Translate Gemma 4 Sub E4B |       2.0658 |     1.6523 |     4.0312 |
| Gemma 4 E4B               |       2.0769 |     1.6875 |     4.1562 |
| Translate Gemma 4 Sub E2B |       2.2247 |     1.7930 |     4.4062 |
| Gemma 4 E2B               |       2.2774 |     1.8359 |     4.4062 |

Despite being primarily optimized for contextual and conversational translation, Translate Gemma 4 Sub also slightly improved general translation quality over the corresponding base Gemma 4 models.

The following prompt was used for general translation:

```text
TASK: Translate {source_language} into {target_language}.
Follow all demonstrations, glossary mappings, partial-translation constraints and formatting instructions in the user prompt.
Preserve meaning, names, numbers, terminology, register and document structure. Return only the requested final translation without commentary.
```

## Usage with llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="translate_gemma4_sub-E2B-Q4_K_XL.gguf",
    n_ctx=1344,
    n_gpu_layers=-1,
)

messages = [
    {
        "role": "system",
        "content": """TASK: Translate English subtitles into Russian.
STYLE: friendly.
Translate only CURRENT_SOURCE. PREVIOUS_SOURCE and PREVIOUS_TRANSLATION are context only. Preserve meaning, tone, slang, profanity, uncertainty, repetitions and incomplete speech. Return only the final translation without labels or commentary.""",
    },
    {
        "role": "user",
        "content": """[PREVIOUS_SOURCE]
I thought you said you weren't coming.

[PREVIOUS_TRANSLATION]
Я думала, ты сказала, что не придёшь.

[CURRENT_SOURCE]
Yeah, well... I changed my mind.""",
    },
]

response = llm.create_chat_completion(
    messages=messages,
    temperature=0,
    max_tokens=256,
)
print(response["choices"][0]["message"]["content"])
```

## Training overview

Translate Gemma 4 Sub E2B is based on `google/gemma-4-E2B-it`.

Training was performed with Unsloth using an optimized training run derived from the official Gemma 4 model.

## Citation

```bibtex
@misc{17slever17_translate_gemma_4_sub_2026,
  author       = {17slever17},
  title        = {Translate Gemma 4 Sub E2B GGUF},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/17slever17/translate-gemma-4-sub-e2b-GGUF}}
}
```
