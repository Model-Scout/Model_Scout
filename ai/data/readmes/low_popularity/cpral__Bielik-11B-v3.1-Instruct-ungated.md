---
license: apache-2.0
base_model:
- speakleash/Bielik-11B-v3.1-Instruct
language:
- multilingual
- pl
- en
- sq
- bs
- bg
- hr
- cs
- da
- et
- fi
- fr
- el
- es
- is
- lt
- nl
- de
- 'no'
- pt
- ru
- ro
- sr
- hbs
- sv
- sk
- sl
- tr
- uk
- hu
- it
- lv
- ar
- hy
- az
- be
- ca
- cnr
- zh
- cy
- eu
- fo
- gd
- gl
- he
- hi
- id
- ga
- ja
- ka
- ko
- kk
- la
- lb
- mk
- mt
- fa
- vi
library_name: transformers
inference:
  parameters:
    temperature: 0.3
widget:
- messages:
  - role: user
    content: Co przedstawia polskie godło?
pipeline_tag: text-generation
---

SAME AS ORIGINAL, WITH DISABLED DATA COLLECTION AND A REQUIREMENT TO AUTHENTHICATE TO HF TO DOWNLOAD WEIGHTS

the rest of the model card follows.. 
# Bielik-11B-v3.1-Instruct

Bielik-11B-v3.1-Instruct is a generative text model featuring 11 billion parameters.
It is an update to the Bielik 11B v3 line that expands multilingual continual pre-training and strengthens post-training for instruction following, tool use, and reasoning.
Forementioned model stands as a testament to the unique collaboration between the open-science/open-source project SpeakLeash and the High Performance Computing (HPC) center: ACC Cyfronet AGH.
Developed and trained on multilingual text corpora covering 56 languages, with an emphasis on European languages and Polish, which have been cherry-picked and processed by the SpeakLeash team, this endeavor leverages Polish large-scale computing infrastructure of the [ACC Cyfronet AGH HPC center](https://www.cyfronet.pl/en). The creation and training of Bielik-11B-v3.1-Instruct was propelled by resources provided within the [PLGrid](https://plgrid.pl/) environment under computational grant number [PLG/2026/019559], conducted on the [Athena](https://www.cyfronet.pl/en/supercomputers/our-supercomputers#athena) and [Helios](https://www.cyfronet.pl/en/supercomputers/our-supercomputers#helios) supercomputers, and within the [Gaia AI Factory](https://gaia.plgrid.pl/), funded by the European Union through the [EuroHPC Joint Undertaking](https://www.eurohpc-ju.europa.eu/index_en).
As a result, the model exhibits an exceptional ability to understand and process the Polish language and other European languages, providing accurate responses and performing a variety of linguistic tasks with high precision.

🗣️ Chat: https://chat.bielik.ai/

## Model

The model was trained on carefully curated, high-quality datasets that underwent extensive cleaning and rigorous quality assessment to ensure data consistency, reliability, and relevance. The training pipeline consisted of three stages: pretraining on 500B tokens, SFT on 26M samples, and RL (modified GRPO) across 14 diverse environments. This multi-stage training approach was designed to enhance the model's language understanding, instruction-following capabilities, and ability to perform effectively across a broad range of tasks.

Bielik instruct models have been trained with the use of an original open source framework called [ALLaMo](https://github.com/chrisociepa/allamo) implemented by [Krzysztof Ociepa](https://www.linkedin.com/in/krzysztof-ociepa-44886550/).

### Model description:

* **Developed by:** [SpeakLeash](https://speakleash.org/) & [ACC Cyfronet AGH](https://www.cyfronet.pl/)
* **Language:** Multilingual (56 unique languages, optimized for European languages, with a particular focus on Polish)
* **Model type:** causal decoder-only
* **License:** Apache 2.0

## Serving with vLLM (tool calling and reasoning)

Bielik-11B-v3.1-Instruct uses its own tool-call and reasoning format
(`<tool_call>{"name": …, "arguments": …}</tool_call>` and `<think>…</think>`).
To get structured `tool_calls` and a separate `reasoning` field in the
OpenAI-compatible API, start vLLM with the Bielik parsers from
[speakleash/bielik-tools](https://github.com/speakleash/bielik-tools).

Requirements: vLLM **0.24 or newer** (tested on 0.32). The chat template ships
with the model (`chat_template.jinja`), so `--chat-template` is not needed.

```bash
git clone https://github.com/speakleash/bielik-tools.git

vllm serve speakleash/Bielik-11B-v3.1-Instruct \
    --enable-auto-tool-choice \
    --tool-parser-plugin ./bielik-tools/tools/bielik_vllm_tool_parser.py \
    --tool-call-parser bielik \
    --reasoning-parser-plugin ./bielik-tools/tools/bielik_vllm_reasoning_parser.py \
    --reasoning-parser bielik \
    --exclude-tools-when-tool-choice-none \
    --max-model-len 32768
```

- Load exactly one tool parser and one reasoning parser (both register the name `bielik`).
- `--exclude-tools-when-tool-choice-none` removes tool definitions from the prompt
  when a request sets `tool_choice="none"`; otherwise the model may still write a
  tool call as plain text.
- Older per-version parsers (`*_v0.12.0.py`, `*_v0.13.0.py`, `*_v0.15.0.py`, the 0.20 plugin)
  are frozen and meant for older vLLM releases; see the bielik-tools README.

### Reasoning

Thinking is controlled with `reasoning_effort`: `none` (default), `low`, `medium`,
`high`, `max`. With `none` the model answers directly. The `enable_thinking`
flag used by Bielik v3.0 is ignored by this template.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

resp = client.chat.completions.create(
    model="speakleash/Bielik-11B-v3.1-Instruct",
    messages=[{"role": "user", "content": "Ile jest liczb pierwszych mniejszych od 50?"}],
    reasoning_effort="high",          # or extra_body={"chat_template_kwargs": {"reasoning_effort": "high"}}
    max_tokens=4096,
)
msg = resp.choices[0].message
print("reasoning:", getattr(msg, "reasoning", None) or getattr(msg, "reasoning_content", None))
print("answer:", msg.content)
```

Leave enough `max_tokens` for reasoning plus the answer: if generation stops while
still thinking, `content` is empty.

### Tool calling

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Returns the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

resp = client.chat.completions.create(
    model="speakleash/Bielik-11B-v3.1-Instruct",
    messages=[{"role": "user", "content": "Jaka jest pogoda w Krakowie?"}],
    tools=tools,
    tool_choice="auto",               # "required", "none" or a named function also work
)
print(resp.choices[0].message.tool_calls)
```

- `tool_choice="required"` and a named function are enforced by the parser
  (constrained decoding of the call; the argument schema itself is not enforced).
- The request-level `tool_choice` and `response_format` do not reach the chat
  template. To also add the template's instructions, repeat them in
  `extra_body={"chat_template_kwargs": {"tool_choice": "required"}}`.
- Treat tool arguments as untrusted input.

### Default system prompt

The template prepends a built-in system prompt ("Model Guidelines": identity,
knowledge cutoff, current date, safety rules; about 1,000 tokens). Your own system
message is appended under "Additional Instructions". The current date comes from the
server clock; for reproducible runs pass `current_date` and `current_day_of_week`
in `chat_template_kwargs`. To disable the built-in prompt for all requests:

```bash
vllm serve … --default-chat-template-kwargs '{"provider_system_prompt": false}'
```

or per request: `extra_body={"chat_template_kwargs": {"provider_system_prompt": False}}`.


## Limitations and Biases

Bielik-11B-v3.1-Instruct is a quick demonstration that the base model can be easily fine-tuned to achieve compelling and promising performance. It does not have any moderation mechanisms. We're looking forward to engaging with the community in ways to make the model respect guardrails, allowing for deployment in environments requiring moderated outputs.

Bielik-11B-v3.1-Instruct can produce factually incorrect output, and should not be relied on to produce factually accurate data. Bielik-11B-v3.1-Instruct was trained on various public datasets. While great efforts have been taken to clear the training data, it is possible that this model can generate lewd, false, biased or otherwise offensive outputs.

## Responsible for training the model

* [Krzysztof Ociepa](https://www.linkedin.com/in/krzysztof-ociepa-44886550/)<sup>SpeakLeash</sup> - team leadership, conceptualizing, data preparation, process optimization and oversight of training
* [Łukasz Flis](https://www.linkedin.com/in/lukasz-flis-0a39631/)<sup>Cyfronet AGH</sup> - coordinating and supervising the training
* [Adrian Gwoździej](https://www.linkedin.com/in/adrgwo/)<sup>SpeakLeash</sup> - data preparation and quality assurance
* [Krzysztof Wróbel](https://www.linkedin.com/in/wrobelkrzysztof/)<sup>SpeakLeash</sup> - benchmarks
* [Karol Jezierski](https://www.linkedin.com/in/karol-jezierski/)<sup>SpeakLeash</sup> - data deduplication and RL environment setup
* [Igor Ciuciura](https://www.linkedin.com/in/igor-ciuciura-1763b52a6/)<sup>SpeakLeash</sup> - data preparation


The model could not have been created without the commitment and work of the entire SpeakLeash team, whose contribution is invaluable. Thanks to the hard work of many individuals, it was possible to gather a large amount of content in Polish and establish collaboration between the open-science SpeakLeash project and the HPC center: ACC Cyfronet AGH. Individuals who contributed to the creation of the model:
[Sebastian Kondracki](https://www.linkedin.com/in/sebastian-kondracki/),
[Marek Magryś](https://www.linkedin.com/in/magrys/),
[Sonia Staniek](https://www.linkedin.com/in/sonia-staniek/),
[Waldemar Boszko](https://www.linkedin.com/in/waldemarboszko),
[Maria Czarkowska](https://www.linkedin.com/in/mariaczarkowska/),
[Jacek Chwiła](https://www.linkedin.com/in/jacek-chwila/),
[Kuba Sołtys](https://www.linkedin.com/in/qooba/),
[Dominika Basaj](https://www.linkedin.com/in/dominika-basaj/),
[Remigiusz Kinas](https://www.linkedin.com/in/remigiusz-kinas/),
[Marcin Dąbrowski](https://www.linkedin.com/in/mdabrowski-ai/),
[Anna Przybył](https://www.linkedin.com/in/annaprzybyl/),
[Agnieszka Ratajska](https://www.linkedin.com/in/agnieszka-ratajska/),
[Daria Bartkowiak](https://www.linkedin.com/in/daria-bartkowiak-16742b391/),
[Witold Wydmański](https://www.linkedin.com/in/witold-wydmanski/),
[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/),
[Grzegorz Anioł](https://www.linkedin.com/in/grzegorz-aniol/),
[Bartosz Bartnicki](https://www.linkedin.com/in/bartosz-bartnicki-2480151a5/), and many other wonderful researchers and enthusiasts of the AI world.

## Legal Aspects

EU AI Act Transparency Documentation: [Bielik 11B v3 EU Public Summary.pdf](https://bit.ly/4qDcE81)

## Data Protection and Copyright Requests

For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly: [biuro@speakleash.org.pl](mailto:biuro@speakleash.org.pl).

## Citation
Please cite this model using the following format:

```
@misc{Bielik11Bv31i,
    title     = {Bielik-11B-v3.1-Instruct model card},
    author    = {Ociepa, Krzysztof and Flis, Łukasz and Gwoździej, Adrian and Wróbel, Krzysztof and Jezierski, Karol and Ciuciura, Igor and {SpeakLeash Team} and {Cyfronet Team}},
    year      = {2026},
    url       = {https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct},
    note      = {Accessed: 2026-10-31}, % change this date
    urldate   = {2026-10-31} % change this date
}
```

## Contact Us

If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our [Discord SpeakLeash](https://discord.gg/pv4brQMDTy).

## Acknowledgements

We gratefully acknowledge Polish high-performance computing infrastructure PLGrid (HPC Center: ACC Cyfronet AGH) for providing computer facilities and support within computational grant no. [PLG/2026/019559].

This work was supported by the Gaia AI Factory project, funded by the European Union under Grant Agreement No. 101314359 through the EuroHPC Joint Undertaking (EuroHPC JU).