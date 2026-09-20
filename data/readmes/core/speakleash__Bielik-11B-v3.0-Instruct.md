---
license: apache-2.0
base_model:
- speakleash/Bielik-11B-v3-Base-20250730
language:
- multilingual
- pl
- en
- sq
- bel
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
library_name: transformers
inference:
  parameters:
    temperature: 0.2
widget:
- messages:
  - role: user
    content: Co przedstawia polskie godło?
extra_gated_fields:
  I agree to be contacted for feedback about Bielik models: checkbox
pipeline_tag: text-generation
---

<p align="center">
  <img src="https://huggingface.co/speakleash/Bielik-11B-v2/raw/main/speakleash_cyfronet.png">
</p>

# Bielik-11B-v3.0-Instruct

Bielik-11B-v3.0-Instruct is a generative text model featuring 11 billion parameters. 
It is an instruct fine-tuned version of the [Bielik-11B-v3-Base-20250730](https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730). 
Forementioned model stands as a testament to the unique collaboration between the open-science/open-source project SpeakLeash and the High Performance Computing (HPC) center: ACK Cyfronet AGH. 
Developed and trained on multilingual text corpora across 32 European languages, with emphasis on Polish, which has been cherry-picked and processed by the SpeakLeash team, this endeavor leverages Polish large-scale computing infrastructure, 
specifically within the PLGrid environment, and more precisely, the HPC centers: ACK Cyfronet AGH. 
The creation and training of the Bielik-11B-v3.0-Instruct was propelled by the support of computational grant number PLG/2024/016951, conducted on the Athena and Helios supercomputer, 
enabling the use of cutting-edge technology and computational resources essential for large-scale machine learning processes. 
As a result, the model exhibits an exceptional ability to understand and process the Polish language and other European languages, providing accurate responses and performing a variety of linguistic tasks with high precision.

📚 Technical report: [Bielik_11B_v3.pdf](https://github.com/speakleash/bielik-papers/blob/main/v3/Bielik_11B_v3.pdf)

🗣️ Chat: https://chat.bielik.ai/

## Model

The model is a successor to the [Bielik v2](https://arxiv.org/abs/2505.02410) series, and its development also leveraged the knowledge and experience gained while working on the [Bielik v3 Small](https://arxiv.org/abs/2505.02550) models.

The [SpeakLeash](https://speakleash.org/) team is working on their own set of instructions in Polish, which is continuously being expanded and refined by annotators. A portion of these instructions, which had been manually verified and corrected, has been utilized for training purposes. Moreover, due to the limited availability of high-quality instructions in Polish, synthetic instructions were generated and used in training. The dataset used for training comprised over 20 million instructions, consisting of more than 17 billion tokens.

To align the model with user preferences we employed the [DPO-Positive](https://arxiv.org/abs/2402.13228) method, utilizing both generated and manually corrected examples, which were scored by a metamodel. A dataset comprising over 114,000 examples of varying lengths to address different aspects of response style. It was filtered and evaluated by the reward model to select instructions with the right level of difference between chosen and rejected. The novelty introduced in DPO-P was multi-turn conversations introduction.

In the final stage of the alignment pipeline, Reinforcement Learning (RL) was used to further enhance the model's analytical capabilities. Training employed [Group Relative Policy Optimization (GRPO)](https://arxiv.org/abs/2402.03300) and its variant, [Dr. GRPO](https://arxiv.org/abs/2503.20783), which was chosen to improve token efficiency by reducing the tendency of models to artificially increase response length to maximize rewards. The RL training was conducted using the [Volcano Engine Reinforcement Learning (VERL)](https://arxiv.org/abs/2409.19256) framework, providing a scalable and modular training environment. The training corpus comprised 143k curated problems spanning logic, STEM, mathematics, and tool-use domains, with all samples selected based on the availability of Reinforcement Learning from Verifiable Rewards (RLVR), ensuring that each problem had a definitive, verifiable solution.

Bielik instruct models have been trained with the use of an original open source framework called [ALLaMo](https://github.com/chrisociepa/allamo) implemented by [Krzysztof Ociepa](https://www.linkedin.com/in/krzysztof-ociepa-44886550/). This framework allows users to train language models with architecture similar to LLaMA and Mistral in fast and efficient way.

### Model description:

* **Developed by:** [SpeakLeash](https://speakleash.org/) & [ACK Cyfronet AGH](https://www.cyfronet.pl/)
* **Language:** Multilingual (32 European languages, optimized for Polish)
* **Model type:** causal decoder-only
* **Finetuned from:** [Bielik-11B-v3-Base-20250730](https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730)
* **License:** Apache 2.0


### Chat template

Bielik-11B-v3.0-Instruct uses [ChatML](https://github.com/cognitivecomputations/OpenChatML) as the prompt format.

E.g.
```
prompt = "<s><|im_start|> user\nJakie mamy pory roku?<|im_end|> \n<|im_start|> assistant\n"
completion = "W Polsce mamy 4 pory roku: wiosna, lato, jesień i zima.<|im_end|> \n"
```

This format is available as a [chat template](https://huggingface.co/docs/transformers/main/chat_templating) via the `apply_chat_template()` method:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model_name = "speakleash/Bielik-11B-v3.0-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)

messages = [
    {"role": "system", "content": "Odpowiadaj krótko, precyzyjnie i wyłącznie w języku polskim."},
    {"role": "user", "content": "Jakie mamy pory roku w Polsce?"},
    {"role": "assistant", "content": "W Polsce mamy 4 pory roku: wiosna, lato, jesień i zima."},
    {"role": "user", "content": "Która jest najcieplejsza?"}
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = input_ids.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

Fully formated input conversation by apply_chat_template from previous example:

```
<s><|im_start|> system
Odpowiadaj krótko, precyzyjnie i wyłącznie w języku polskim.<|im_end|> 
<|im_start|> user
Jakie mamy pory roku w Polsce?<|im_end|> 
<|im_start|> assistant
W Polsce mamy 4 pory roku: wiosna, lato, jesień i zima.<|im_end|> 
<|im_start|> user
Która jest najcieplejsza?<|im_end|>
```

## Limitations and Biases

Bielik-11B-v3.0-Instruct is a quick demonstration that the base model can be easily fine-tuned to achieve compelling and promising performance. It does not have any moderation mechanisms. We're looking forward to engaging with the community in ways to make the model respect guardrails, allowing for deployment in environments requiring moderated outputs.

Bielik-11B-v3.0-Instruct can produce factually incorrect output, and should not be relied on to produce factually accurate data. Bielik-11B-v3.0-Instruct was trained on various public datasets. While great efforts have been taken to clear the training data, it is possible that this model can generate lewd, false, biased or otherwise offensive outputs.

## Responsible for training the model

* [Krzysztof Ociepa](https://www.linkedin.com/in/krzysztof-ociepa-44886550/)<sup>SpeakLeash</sup> - team leadership, conceptualizing, data preparation, process optimization and oversight of training
* [Łukasz Flis](https://www.linkedin.com/in/lukasz-flis-0a39631/)<sup>Cyfronet AGH</sup> - coordinating and supervising the training
* [Remigiusz Kinas](https://www.linkedin.com/in/remigiusz-kinas/)<sup>SpeakLeash</sup> - conceptualizing, coordinating RL trainings, data preparation, benchmarking and quantizations
* [Adrian Gwoździej](https://www.linkedin.com/in/adrgwo/)<sup>SpeakLeash</sup> - data preparation and ensuring data quality
* [Krzysztof Wróbel](https://www.linkedin.com/in/wrobelkrzysztof/)<sup>SpeakLeash</sup> - benchmarks


The model could not have been created without the commitment and work of the entire SpeakLeash team, whose contribution is invaluable. Thanks to the hard work of many individuals, it was possible to gather a large amount of content in Polish and establish collaboration between the open-science SpeakLeash project and the HPC center: ACK Cyfronet AGH. Individuals who contributed to the creation of the model:
[Sebastian Kondracki](https://www.linkedin.com/in/sebastian-kondracki/),
[Marek Magryś](https://www.linkedin.com/in/magrys/),
[Igor Ciuciura](https://www.linkedin.com/in/igor-ciuciura-1763b52a6/),
[Szymon Baczyński](https://www.linkedin.com/in/szymon-baczynski/),
[Dominika Basaj](https://www.linkedin.com/in/dominika-basaj/),
[Kuba Sołtys](https://www.linkedin.com/in/qooba/),
[Karol Jezierski](https://www.linkedin.com/in/karol-jezierski/),
[Jan Sowa](https://www.linkedin.com/in/janpiotrsowa/),
[Anna Przybył](https://www.linkedin.com/in/annaprzybyl/),
[Agnieszka Ratajska](https://www.linkedin.com/in/agnieszka-ratajska/),
[Witold Wydmański](https://www.linkedin.com/in/witold-wydmanski/),
[Katarzyna Starosławska](https://www.linkedin.com/in/kstaroslawska/),
[Izabela Babis](https://www.linkedin.com/in/izabela-babis-2274b8105/),
[Nina Babis](https://www.linkedin.com/in/nina-babis-00055a140/).

We gratefully acknowledge Polish high-performance computing infrastructure PLGrid (HPC Center: ACK Cyfronet AGH) for providing computer facilities and support within computational grant no. PLG/2024/016951.

## Legal Aspects

EU AI Act Transparency Documentation: [Bielik 11B v3 EU Public Summary.pdf](https://bit.ly/4qDcE81)

## Data Protection and Copyright Requests

For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly: [biuro@speakleash.org.pl](mailto:biuro@speakleash.org.pl).

## Citation
Please cite this model using the following format:

```
@misc{ociepa2025bielik11bv3multilingual,
      title={Bielik 11B v3: Multilingual Large Language Model for European Languages}, 
      author={Krzysztof Ociepa and Łukasz Flis and Remigiusz Kinas and Krzysztof Wróbel and Adrian Gwoździej},
      year={2025},
      eprint={2601.11579},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.11579}, 
}
@misc{Bielik11Bv3i,
    title     = {Bielik-11B-v3.0-Instruct model card},
    author    = {Ociepa, Krzysztof and Flis, Łukasz and Kinas, Remigiusz and Gwoździej, Adrian and Wróbel, Krzysztof and {SpeakLeash Team} and {Cyfronet Team}},
    year      = {2025},
    url       = {https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct},
    note      = {Accessed: 2025-12-31}, % change this date
    urldate   = {2025-12-31} % change this date
}
```

## Contact Us

If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our [Discord SpeakLeash](https://discord.gg/pv4brQMDTy).