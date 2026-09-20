---
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
- no
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
license: apache-2.0
library_name: transformers
tags:
- finetuned
- gguf
- 8bit
inference: false
pipeline_tag: text-generation
base_model: speakleash/Bielik-11B-v3.0-Instruct
---
<p align="center">
  <img src="https://huggingface.co/speakleash/Bielik-11B-v2/raw/main/speakleash_cyfronet.png">
</p>

# Bielik-11B-v3.0-Instruct-FP8-Dynamic

This model was obtained by quantizing the weights and activations of [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct) to FP8 data type, ready for inference with vLLM >= 0.5.0 or SGLang. 
AutoFP8 is used for quantization. This optimization reduces the number of bits per parameter from 16 to 8, reducing the disk size and GPU memory requirements by approximately 50%.
Only the weights and activations of the linear operators within transformers blocks are quantized. Symmetric per-tensor quantization is applied, in which a single linear scaling maps the FP8 representations of the quantized weights and activations. 

FP8 compuation is supported on Nvidia GPUs with compute capability > 8.9 (Ada Lovelace, Hopper).

**DISCLAIMER: Be aware that quantised models show reduced response quality and possible hallucinations!**

## Use with vLLM

This model can be deployed efficiently using the [vLLM](https://docs.vllm.ai/en/latest/) backend, as shown in the example below.

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_id = "speakleash/Bielik-11B-v3.0-Instruct-FP8-Dynamic"

sampling_params = SamplingParams(temperature=0.2, top_p=0.95, max_tokens=4096)

tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    {"role": "system", "content": "Jesteś pomocnym asystentem Bielik."},
    {"role": "user", "content": "Kim był Mikołaj Kopernik i z czego zasłynął?"},
]

prompts = tokenizer.apply_chat_template(messages, tokenize=False)

llm = LLM(model=model_id, max_model_len=4096)

outputs = llm.generate(prompts, sampling_params)

generated_text = outputs[0].outputs[0].text
print(generated_text)
```

vLLM aslo supports OpenAI-compatible serving. See the [documentation](https://docs.vllm.ai/en/latest/) for more details.


## Use with SGLang Runtime
Launch a server of SGLang Runtime:

```
python -m sglang.launch_server --model-path speakleash/Bielik-11B-v3.0-Instruct-FP8-Dynamic --port 30000
```

Then you can send http request or use OpenAI Compatible API. 

```python
import openai
client = openai.Client(
    base_url="http://127.0.0.1:30000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="default",
    messages=[
        {"role": "system", "content": "Jesteś pomocnym asystentem Bielik."},
        {"role": "user", "content": "Kim był Mikołaj Kopernik i z czego zasłynął?"},
    ],
    temperature=0,
    max_tokens=4096,
)
print(response)

```

### Model description:

* **Developed by:** [SpeakLeash](https://speakleash.org/) & [ACK Cyfronet AGH](https://www.cyfronet.pl/)
* **Language:** Multilingual (32 European languages, optimized for Polish)
* **Model type:** causal decoder-only
* **Quant from:** [Bielik-11B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct)
* **Finetuned from:** [speakleash/Bielik-11B-v3-Base-20250730](https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730)
* **License:** Apache 2.0

### Responsible for model quantization  
* [Remigiusz Kinas](https://www.linkedin.com/in/remigiusz-kinas/)<sup>SpeakLeash</sup> - team leadership, conceptualizing, calibration data preparation, process creation and quantized model delivery.

## Contact Us

If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our [Discord SpeakLeash](https://discord.gg/CPBxPce4).