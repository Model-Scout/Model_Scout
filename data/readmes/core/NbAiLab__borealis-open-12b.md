---
license: gemma
datasets:
- NbAiLab/aurora-sft-open
language:
- 'no'
- nb
- nn
base_model:
- google/gemma-3-12b-it
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- conversational
- instruct
- borealis
- gemma3
- norwegian
- norwegian-bokmal
- norwegian-nynorsk
- open
---

![Borealis](./borealis.png)

# Borealis Open 12B

## Model Summary

**NbAiLab/borealis-open-12b** is a **12B-parameter** instruction-tuned **open release** model in the Borealis family from the National Library of Norway (Nasjonalbiblioteket, NB).

This is the first Borealis release to incorporate data made available under the agreement between rights-holder organizations in Norway and the Norwegian government. To date, only a limited subset of the material has been used, specifically to teach the model how to generate news article titles and ingress texts. Models with the suffix `-open`, do not include any material from the agreement.

All Borealis released models are based on the **Gemma 3** family. This model is based on [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it), and fine-tuned for Norwegian-centric instruction following.

### Sizes

| Size | Full release | Open release |
|---:|---|---|
| 27B | [NbAiLab/borealis-27b](https://huggingface.co/NbAiLab/borealis-27b) | [NbAiLab/borealis-open-27b](https://huggingface.co/NbAiLab/borealis-open-27b) |
| 12B | [NbAiLab/borealis-12b](https://huggingface.co/NbAiLab/borealis-12b) | [NbAiLab/borealis-open-12b](https://huggingface.co/NbAiLab/borealis-open-12b) |
| 4B | [NbAiLab/borealis-4b](https://huggingface.co/NbAiLab/borealis-4b) | [NbAiLab/borealis-open-4b](https://huggingface.co/NbAiLab/borealis-open-4b) |
| 1B | [NbAiLab/borealis-1b](https://huggingface.co/NbAiLab/borealis-1b) | [NbAiLab/borealis-open-1b](https://huggingface.co/NbAiLab/borealis-open-1b) |
| 270M | [NbAiLab/borealis-270m](https://huggingface.co/NbAiLab/borealis-270m) | [NbAiLab/borealis-open-270m](https://huggingface.co/NbAiLab/borealis-open-270m) |

## Training Data

Supervised fine-tuning (SFT) uses instruction data prepared by the National Library of Norway for Norwegian-centric assistant behavior, writing, summarization, question answering, and related tasks.

The SFT dataset for this model is [NbAiLab/aurora-sft-open](https://huggingface.co/datasets/NbAiLab/aurora-sft-open). [NbAiLab/aurora-sft-open](https://huggingface.co/datasets/NbAiLab/aurora-sft-open) is the open version of the SFT dataset. The only difference between [NbAiLab/aurora-sft-open](https://huggingface.co/datasets/NbAiLab/aurora-sft-open) and [NbAiLab/aurora-sft](https://huggingface.co/datasets/NbAiLab/aurora-sft) is the addition of 10k tasks derived from copyright-protected newspapers material.

## Evaluation

<figure>
  <img src="./borealis_evals_202605.png" alt="Borealis evaluation results">
  <figcaption>Borealis evaluation results on selected tasks (best score among {0-5}-shot).</figcaption>
</figure>

We evaluate Borealis with NorEval, MMLU-English, and nb-gpt-bench, our own evaluation suite, which will be published and described in an upcoming paper. The full Borealis models include around 10k newspaper-derived tasks from the abovementioned agreement and show a slight performance increase in some key metrics compared with the open variants. We hope to further increase the difference by incorporating proper pre-training on the newspaper material.

## Safety and Alignment

The Borealis family of models are aligned for safety using prompt baking and weighted merging of SFT and aligned models. The goal of this process is to balance model quality, usefulness, and safer behavior.

As with all generative models, outputs can still be incorrect, biased, harmful, or inappropriate. Do not use the model for safety-critical or high-stakes applications without additional evaluation and safeguards.

### Prompt Baking

To align the Borealis models, we employ *prompt baking*, a procedure that distills the behavior induced by a system prompt directly into the model weights using [`bakery`](https://github.com/marksverdhei/bakery). Specifically, we train a LoRA adapter to minimize the KL-divergence between two model distributions: Borealis conditioned on the system prompt, and the same base model augmented with the LoRA adapter but evaluated without the system prompt in context. This objective encourages the adapter to reproduce the behavioral effects of the prompt without requiring the prompt to be present at inference time.

To reduce degradation on downstream tasks and preserve general model utility, we merge the resulting prompt adapter into the base model using a scaling factor of `0.25`, which we found to provide the best empirical trade-off.

## Intended Use

- Norwegian-centric assistant-style tasks, including drafting, summarization, Q&A, and light reasoning (this is not a reasoning model).
- Assessment and improvement of Norwegian writing style and quality.
- Evaluation of behavior and language coverage for Norwegian, Bokmål, and Nynorsk.

## Usage

This repository contains the Transformers/safetensors version of the model. The
examples below use `NbAiLab/borealis-open-12b` as the model id; replace it with
another Borealis repo id if needed.

### Transformers

Use the Gemma 3 multimodal interface. For text-only prompts, omit image
content and keep only the text item in the message content list.

```python
import torch
from transformers import AutoProcessor, Gemma3ForConditionalGeneration

model_id = "NbAiLab/borealis-open-12b"

processor = AutoProcessor.from_pretrained(model_id)
model = Gemma3ForConditionalGeneration.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Forklar kort hva du ser på bildet."},
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png"},
        ],
    }
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256)
new_tokens = outputs[0, inputs["input_ids"].shape[-1]:]
print(processor.decode(new_tokens, skip_special_tokens=True))
```

### vLLM

Serve the model with vLLM's OpenAI-compatible server:

```bash
vllm serve NbAiLab/borealis-open-12b --served-model-name borealis-open-12b
```

Then call the local chat completions endpoint:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "borealis-open-12b",
    "messages": [
      {
        "role": "user",
        "content": "Skriv tre korte punkter om norsk språkteknologi."
      }
    ],
    "max_tokens": 256
  }'
```

Large models may require tensor parallelism or reduced memory settings depending
on the available GPU memory.

### llama.cpp

llama.cpp uses GGUF files, not the safetensors files in this repository. When
the planned GGUF companion repository is available, you can run it directly from
the Hub:

```bash
llama-server -hf NbAiLab/borealis-open-12b-gguf --port 8080
```

Or download a GGUF file and run it locally:

```bash
llama-cli -m borealis-open-12b.gguf \
  -p "Skriv et kort sammendrag av hva Nasjonalbiblioteket gjør." \
  -n 256
```

### Ollama

Ollama also requires a GGUF model. Once the GGUF companion repository is
available, you can run it from Hugging Face:

```bash
ollama run hf.co/NbAiLab/borealis-open-12b-gguf
```

For a local GGUF file, create a minimal `Modelfile`:

```text
FROM ./borealis-open-12b.gguf
```

Then create and run the local Ollama model:

```bash
ollama create borealis-open-12b -f Modelfile
ollama run borealis-open-12b "Skriv tre korte punkter om norsk språkteknologi."
```

## Limitations

- The model may hallucinate or produce incorrect information.
- Safety alignment reduces but does not eliminate harmful or inappropriate outputs.
- Performance outside Norwegian and English use cases has not been fully characterized.

## EU AI Act

The model is a fine-tune of Gemma 3. Using Gemma 3 27B as a conservative upper-bound reference, the original Gemma 3 27B training compute is estimated at approximately 2.1-2.3 x 10^24 FLOPs, based on the disclosed 14T training-token budget and the 27B parameter scale. The fine-tuning run used approximately 3.4 x 10^20 FLOPs, or about 0.015% of the estimated original training compute. This is substantially below the European Commission's indicative one-third threshold for treating a downstream modification as a significant modification that would make the modifier the provider of the modified General Purpose AI (GPAI) model.

On that basis, the fine-tuning activity is preliminarily assessed as not constituting a substantial modification for the purpose of becoming the provider of a new modified GPAI model under the compute-based criterion. However, the resulting model remains derived from a generative general-purpose AI model and may still be subject to downstream AI-system obligations under the EU AI Act.

For additional model-level documentation, see the [Model Documentation Form](./Model_Documentation_Form.pdf).

## License

The license of this model is an adaptation of the Apache 2.0 license with additional use-based restrictions. In particular, users of the model are required to refrain from intentionally using the model to recreate data the model has been trained on. The license also requires users not to use the model or its output to provide end-user services whose primary purpose is to give access to licensed press publications in the training data.

For more information, see the [LICENSE](./LICENSE) and the [License FAQ](./LICENSE_FAQ.pdf).

## Authenticity

This model release is signed by the National Library of Norway. The signed manifest in `signing/SHA256SUMS` covers the model-runtime artifacts, including model weights, configuration, tokenizer files, and chat template.

To verify model authenticity and file integrity after downloading the repository, run:

```bash
bash signing/verify.sh
```

For more verification instructions, see [ai.nb.no/verify](https://ai.nb.no/verify).

## Weights

This repository contains the Transformers (safetensors) release of **NbAiLab/borealis-open-12b**.

Companion formats:
- GGUF: [NbAiLab/borealis-open-12b-gguf](https://huggingface.co/NbAiLab/borealis-open-12b-gguf)
- MLX: [NbAiLab/borealis-open-12b-mlx](https://huggingface.co/NbAiLab/borealis-open-12b-mlx)
- MLX 8-bit: [NbAiLab/borealis-open-12b-mlx-8bits](https://huggingface.co/NbAiLab/borealis-open-12b-mlx-8bits)

## Citation and Contributors

The Borealis family of models is a joint effort of multiple teams at the National Library of Norway. Led by Javier de la Rosa ([@versae](https://huggingface.co/versae)), key contributors include (in alphabetical order) Rolv-Arild Braaten, Magnus Breder Birkenes, Lucas Charpentier, Pawel Cyrta, Tita Enstad, Markus Sverdvik Heiervang, Arne Martinus Lindstad, Marthe Løken Midtgaard, Marie Roald, Marie Røsok, Thea Tollersrud, and Angelina Zanardi. Olaus Ingskog Bergstrøm contributed with legal advice. And Yngvil Beyer, Svein Arne Brygfjeld, and Wilfred Østgulen helped with strategic oversight.

A tecnical report will be released soon.

## Acknowledgements

Thanks to the Gemma team at Google for releasing Gemma 3, and to everyone contributing to the Norwegian language technology ecosystem.

## Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions. When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence. In no event shall the owner of the models (The National Library of Norway) be liable for any results arising from the use made by third parties of these models.

## Contact

For feedback, technical concerns, or collaboration inquiries, please contact <a rel="noopener nofollow" href="mailto:ailab@nb.no">ailab@nb.no</a>.
