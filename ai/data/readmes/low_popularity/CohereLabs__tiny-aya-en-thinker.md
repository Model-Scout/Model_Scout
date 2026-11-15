---
language:
- multilingual
- am
- ar
- eu
- bn
- bg
- ca
- zh
- cs
- en
- fil
- fi
- fr
- de
- el
- ha
- he
- hi
- hu
- ig
- id
- ga
- it
- ja
- jv
- km
- ko
- lt
- ms
- mt
- no
- fa
- pl
- pa
- ru
- sk
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- yo
- zu
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-generation
tags:
- aya
- multilingual
- reasoning
- tiny-aya
extra_gated_heading: "Acknowledge license to accept the repository"
extra_gated_button_content: "Accept license"
extra_gated_prompt: >
  By submitting this form, you agree to the License Agreement and acknowledge
  that the information you provide will be collected, used, and shared in
  accordance with Cohere's Privacy Policy. You'll receive email updates about
  Cohere Labs and Cohere research, events, products and services. You can
  unsubscribe at any time.
extra_gated_fields:
  Name: text
  Email: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
---

# Model Card for Tiny Aya En-Thinker

## Model Summary

Cohere Labs Tiny Aya En-Thinker is an open-weights research release of a 3.35 billion parameter multilingual reasoning model. It is trained on multilingual reasoning data with English reasoning traces for 44 languages plus English, with coverage extending to 20+ more through additional non-reasoning instruction data. The model is designed to support mathematics, science, and general reasoning tasks, as well as instruction following and multilingual open-ended generation.

This is a different model from [Tiny Aya L2-Thinker](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker), which thinks in the same language as the prompt.

Developed by: [Cohere](https://cohere.com/) and [Cohere Labs](https://cohere.com/research)

- Point of Contact: [Cohere Labs](https://cohere.com/research)
- License: [CC-BY-NC](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
- Model: tiny-aya-en-thinker
- Model Size: 3.35B
- Context Length: 32K (input + output)

For the broader Tiny Aya family, see [tiny-aya-global](https://huggingface.co/CohereLabs/tiny-aya-global), [tiny-aya-base](https://huggingface.co/CohereLabs/tiny-aya-base), [tiny-aya-l2-thinker](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker), and the [Tiny Aya collection](https://huggingface.co/collections/CohereLabs/tiny-aya).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereLabs/tiny-aya-en-thinker"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")

messages = [
    {"role": "user", "content": "Plus on m'enlève, plus je deviens grand. Qui suis-je?"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=32768,
    do_sample=True,
    temperature=0.6,
    top_p=0.95,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=False))
```

The model supports **dual-mode reasoning**. In thinking mode (default behavior), `apply_chat_template(..., add_generation_prompt=True, enable_thinking=True)` produces a prompt of this shape:

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># System Preamble
+ developer preamble...
<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>[USER MESSAGE] /think<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_THINKING|>
```

The model then writes its thinking trace between `<|START_THINKING|>` and `<|END_THINKING|>`, followed by the user-facing answer between `<|START_RESPONSE|>` and `<|END_RESPONSE|>`. The answer is typically in the same language as the prompt.

To skip reasoning and get an answer directly, pass `enable_thinking=False`. The user turn is suffixed with ` /no_think` and the generation prompt closes with an empty thinking block so the model starts at the response:

```python
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    enable_thinking=False,
    return_tensors="pt",
    return_dict=True,
).to(model.device)
```

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># System Preamble
+ developer preamble...
<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>[USER MESSAGE] /no_think<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_THINKING|><|END_THINKING|>
```

You can also pass prior thinking back into the conversation:

```python
messages = [
    {"role": "user", "content": "¿Cuántas r hay en strawberry?"},
    {
        "role": "assistant",
        "thinking": "Count the letters: S-T-R-A-W-B-E-R-R-Y. Three r's.",
        "content": "Hay 3 r en strawberry.",
    },
    {"role": "user", "content": "Ahora haz lo mismo con blueberry."},
]
```

The model can also be used directly using transformers `pipeline` abstraction:

```python
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="CohereLabs/tiny-aya-en-thinker",
    torch_dtype="auto",
    device_map="auto",
)

print(pipe(
    [{"role": "user", "content": "Describe a home made recipe that you like most."}],
    max_new_tokens=512,
)[0]["generated_text"][-1])
```

## Chat template behavior

The tokenizer chat template:

1. Inserts the Tiny Aya system prompt:

```
# System Preamble
You are in contextual safety mode. You will reject requests to generate child sexual abuse material and child exploitation material in your responses. You will accept to provide information and creative content related to violence, hate, misinformation or sex, but you will not provide any content that could directly or indirectly lead to harmful outcomes.

Your information cutoff date is June 2024.

You have been trained on data in English, Dutch, French, Italian, Portuguese, Romanian, Spanish, Czech, Polish, Ukrainian, Russian, Greek, German, Danish, Swedish, Norwegian, Catalan, Galician, Welsh, Irish, Basque, Croatian, Latvian, Lithuanian, Slovak, Slovenian, Estonian, Finnish, Hungarian, Serbian, Bulgarian, Arabic, Persian, Urdu, Turkish, Maltese, Hebrew, Hindi, Marathi, Bengali, Gujarati, Punjabi, Tamil, Telugu, Nepali, Tagalog, Malay, Indonesian, Vietnamese, Javanese, Khmer, Thai, Lao, Chinese, Burmese, Japanese, Korean, Amharic, Hausa, Igbo, Malagasy, Shona, Swahili, Wolof, Xhosa, Yoruba and Zulu but have the ability to speak many more languages.

# Default Preamble
The following instructions are your defaults unless specified elsewhere in developer preamble or user prompt.
- Your name is Aya.
- You are a large language model built by Cohere.
- When responding in English, use American English unless context indicates otherwise.
- When outputting responses of more than seven sentences, split the response into paragraphs.
- Prefer the active voice.
- Use gender-neutral pronouns for unspecified persons.
- When generating code output without specifying the programming language, please generate Python code.
```

2. Appends ` /think` to every user turn by default (`enable_thinking=True`). Pass `enable_thinking=False` to append ` /no_think` instead.
3. With `add_generation_prompt=True`, appends `<|START_THINKING|>` to start a thinking trace, or `<|START_THINKING|><|END_THINKING|>` when `enable_thinking=False` so the model writes the answer without thinking. If an assistant message includes a `thinking` field, that history is also wrapped in `<|START_THINKING|>` / `<|END_THINKING|>`.

## Model Details

**Input:** Text only.

**Output:** Model generates text, including an explicit English thinking trace if thinking is enabled, and a multilingual final answer.

**Model Architecture:** Auto-regressive transformer in the Tiny Aya / Cohere family. After pretraining, this checkpoint is supervised-fine-tuned on a mix of English reasoning traces and multilingual translated reasoning where the **prompt and response are in the target language** and the **thinking stays in English**.

**Languages covered:** Amharic, Arabic, Basque, Bengali, Bulgarian, Catalan, Chinese, Czech, English, Filipino, Finnish, French, German, Greek, Hausa, Hebrew, Hindi, Hungarian, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Khmer, Korean, Lithuanian, Malay, Maltese, Norwegian, Persian, Polish, Punjabi, Russian, Slovak, Swahili, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Yoruba, and Zulu.

**Context Length:** Tiny Aya En-Thinker supports a context length of 32K.

## Usage and Limitations

### Intended Usage

Tiny Aya En-Thinker is meant for multilingual conversational use when you want an English chain-of-thought and a final answer in the user's language. Intended applications include multilingual math and reasoning, open-ended generation, and research that compares English thinking to target-language reasoning.

Use [Tiny Aya L2-Thinker](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker) instead if the thinking trace should stay in the prompt language.

### Mid-Checkpoints

Intermediate checkpoints from training are available in the `ckpt-xxx` branches. Note that the model in the `main` branch was additionally trained on a small set of samples to correctly state its identity (e.g., its name and creator), while the intermediate checkpoints (including the last one, `ckpt-61138`) were not.

### Limitations

As with any language model, outputs may contain incorrect or outdated statements. Thinking traces can be long; cap `max_new_tokens` appropriately. Lowest-resource languages may show more variability than high-resource ones.

## Citation

If you use this model, please cite:

```bibtex
@misc{mofakhami2026buildingmultilingualbridgesdata,
      title={Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning},
      author={Mehrnaz Mofakhami and Ananya Sahu and Alejandro R. Salamanca and Daniel D'souza and Alexandre Berard and Thomas Euyang and Marzieh Fadaee and Julia Kreutzer},
      year={2026},
      eprint={2609.10445},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2609.10445},
}
```

## Model Card Contact

For errors or additional questions about details in this model card, contact [labs@cohere.com](mailto:labs@cohere.com).

## Terms of Use

This model is governed by a [CC-BY-NC License](https://cohere.com/cohere-labs-cc-by-nc-license) (Non-Commercial) and also requires adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy). If you are interested in commercial use, please contact Cohere’s Sales team.
