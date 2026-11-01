---
library_name: transformers
license: gpl-3.0
pipeline_tag: translation
language:
- bg
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fi
- fr
- ga
- gl
- hr
- hu
- it
- lt
- lv
- mt
- nl
- nb
- 'no'
- oc
- pl
- pt
- ro
- ru
- sl
- sk
- sr
- sv
- uk
- ast
- an
- ar
- ja
- hi
- ko
- zh
- is
base_model:
- BSC-LT/salamandraTA-7b-instruct
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/633b489acbdbadd99c0b75ef/MhsW4ODhK6ofYq8DnpyKc.png)

# SalamandraTA-7B-instruct-GGUF Model Card

This model is the GGUF-quantized version of [SalamandraTA-7b-instruct (v3)](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct).

> [!NOTE]
> The `main` branch of this repository contains the GGUF quantization of the **latest** SalamandraTA-7b-instruct release (v3).
> The previous quantized version is preserved on the [`v1` branch](https://huggingface.co/BSC-LT/salamandraTA-7B-instruct-GGUF/tree/v1).

The model weights are quantized from FP16 to **Q4_K_M** (4-bit weights with K-quant, medium)
using the [Llama.cpp](https://github.com/ggml-org/llama.cpp) framework.
Inferencing with this model can be done using [VLLM](https://docs.vllm.ai/en/stable/models/engine_args.html).

SalamandraTA-7b-instruct is a translation LLM that has been instruction-tuned from SalamandraTA-7b-base.
The base model results from continually pre-training [Salamandra-7b](https://huggingface.co/BSC-LT/salamandra-7b) on monolingual and parallel data and has not been published,
but is reserved for internal use.
SalamandraTA-7b-instruct (v3) is proficient in **40 languages (+ 3 varieties)**, including both European and non-European languages such as Arabic, Japanese, Hindi, Korean, and Simplified Chinese,
and is mainly trained to perform general translation tasks at the sentence, paragraph, and document levels.
This version adds translation-related tasks such as terminology-aware machine translation, structured text (e.g., HTML, XML) translation, translation post-editing,
and named entity recognition, while maintaining the strong translation performance of the previous version.

### License Notice
This release includes data licensed under GPL-3, and is therefore distributed under the terms of the GPL-3 license.

> [!WARNING]
> **DISCLAIMER:** This version of Salamandra is tailored exclusively for translation and the mentioned translation-related tasks. It lacks chat capabilities and has not been trained with any chat instructions.

---

## Available files

| File | Quantization | Size (approx.) |
|---|---|---|
| `salamandraTA_7B_v3_q4_k_m.gguf` | Q4_K_M — 4-bit, best size/quality balance | ~4.1 GB |

### Quantization impact
The Q4_K_M quantization shows a 1–2 BLEU difference compared to the full-precision (unquantized) model.

## How to Use

The following example code works under ``Python 3.10.4``, ``vllm==0.7.3``, ``torch==2.5.1`` and ``torchvision==0.20.1``, though it should run on
any current version of the libraries. This is an example of translation using the model:

```
from huggingface_hub import snapshot_download
from vllm import LLM, SamplingParams

model_dir = snapshot_download(repo_id="BSC-LT/salamandraTA-7B-instruct-GGUF", revision="main")
model_name = "salamandraTA_7B_v3_q4_k_m.gguf"

llm = LLM(model=model_dir + '/' + model_name, tokenizer=model_dir)

source = "Spanish"
target = "English"
sentence = "Ayer se fue, tomó sus cosas y se puso a navegar. Una camisa, un pantalón vaquero y una canción, dónde irá, dónde irá. Se despidió, y decidió batirse en duelo con el mar. Y recorrer el mundo en su velero. Y navegar, nai-na-na, navegar."

prompt = f"Translate the following text from {source} into {target}.\\n{source}: {sentence} \\n{target}:"
messages = [{'role': 'user', 'content': prompt}]

outputs = llm.chat(messages,
                   sampling_params=SamplingParams(
                       temperature=0.1,
                       stop_token_ids=[5],
                       max_tokens=200)
                   )[0].outputs

print(outputs[0].text)
    

```

## Additional information

### Author
Machine Translation Group, AI Institute, the Barcelona Supercomputing Center (ai_institute_mt@bsc.es).

### Contact
For further information, please send an email to <ai_institute_mt@bsc.es>.

### Copyright
Copyright(c) 2026 by AI Institute, Barcelona Supercomputing Center.

### Funding

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project Desarrollo Modelos ALIA.

This work has been promoted and financed by the Government of Catalonia through the [Aina Project](https://projecteaina.cat/).


### Acknowledgements

The success of this project has been made possible thanks to the invaluable contributions of our partners in the [ILENIA Project](https://proyectoilenia.es/):
[HiTZ](http://hitz.ehu.eus/es), and [CiTIUS](https://citius.gal/es/).
Their efforts have been instrumental in advancing our work, and we sincerely appreciate their help and support.

### Disclaimer
Be aware that the model may contain biases or other unintended distortions.
When third parties deploy systems or provide services based on this model, or use the model themselves,
they bear the responsibility for mitigating any associated risks and ensuring compliance with applicable regulations,
including those governing the use of Artificial Intelligence.

The Barcelona Supercomputing Center, as the owner and creator of the model, shall not be held liable for any outcomes resulting from third-party use.

### License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)
