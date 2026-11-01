

---
language:
- en
- ko
license: other
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-3-ko
- GGUF
pipeline_tag: text-generation
license_name: llama3
license_link: LICENSE
quantized_by: andrijdavid
---
# Llama-3-Open-Ko-8B-Instruct-preview-GGUF
- Original model: [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF
GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.
Here is an incomplete list of clients and libraries that are known to support GGUF:
* [llama.cpp](https://github.com/ggerganov/llama.cpp). This is the source project for GGUF, providing both a Command Line Interface (CLI) and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), Known as the most widely used web UI, this project boasts numerous features and powerful extensions, and supports GPU acceleration.
* [Ollama](https://github.com/jmorganca/ollama) Ollama is a lightweight and extensible framework designed for building and running language models locally. It features a simple API for creating, managing, and executing models, along with a library of pre-built models for use in various applications​
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), A comprehensive web UI offering GPU acceleration across all platforms and architectures, particularly renowned for storytelling.
* [GPT4All](https://gpt4all.io), This is a free and open source GUI that runs locally, supporting Windows, Linux, and macOS with full GPU acceleration.
* [LM Studio](https://lmstudio.ai/) An intuitive and powerful local GUI for Windows and macOS (Silicon), featuring GPU acceleration.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui). A notable web UI with a variety of unique features, including a comprehensive model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), An attractive, user-friendly character-based chat GUI for Windows and macOS (both Silicon and Intel), also offering GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python),  A Python library equipped with GPU acceleration, LangChain support, and an OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), A Rust-based ML framework focusing on performance, including GPU support, and designed for ease of use.
* [ctransformers](https://github.com/marella/ctransformers), A Python library featuring GPU acceleration, LangChain support, and an OpenAI-compatible AI server.
* [localGPT](https://github.com/PromtEngineer/localGPT) An open-source initiative enabling private conversations with documents. 
<!-- README_GGUF.md-about-gguf end -->

<!-- compatibility_gguf start -->
## Explanation of quantisation methods
<details>
  <summary>Click to see details</summary>
The new methods available are:

* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw.
</details>
<!-- compatibility_gguf end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single folder.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: LiteLLMs/Llama-3-Open-Ko-8B-Instruct-preview-GGUF and below it, a specific filename to download, such as: Q4_0/Q4_0-00001-of-00009.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download LiteLLMs/Llama-3-Open-Ko-8B-Instruct-preview-GGUF Q4_0/Q4_0-00001-of-00009.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download LiteLLMs/Llama-3-Open-Ko-8B-Instruct-preview-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install huggingface_hub[hf_transfer]
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download LiteLLMs/Llama-3-Open-Ko-8B-Instruct-preview-GGUF Q4_0/Q4_0-00001-of-00009.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->
<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m Q4_0/Q4_0-00001-of-00009.gguf --color -c 8192 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<PROMPT>"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 8192` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries. Note that at the time of writing (Nov 27th 2023), ctransformers has not been updated for some time and is not compatible with some recent models. Therefore I recommend you use llama-cpp-python.

### How to load this model in Python code, using llama-cpp-python

For full documentation, please see: [llama-cpp-python docs](https://abetlen.github.io/llama-cpp-python/).

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install llama-cpp-python
# With NVidia CUDA acceleration
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Or with OpenBLAS acceleration
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
# Or with CLBLast acceleration
CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
# Or with AMD ROCm GPU acceleration (Linux only)
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
# Or with Metal GPU acceleration for macOS systems only
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
# In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format; eg for NVidia CUDA:
$env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
pip install llama-cpp-python
```

#### Simple llama-cpp-python example code

```python
from llama_cpp import Llama
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="./Q4_0/Q4_0-00001-of-00009.gguf",  # Download the model file first
  n_ctx=32768,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)
# Simple inference example
output = llm(
  "<PROMPT>", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)
# Chat Completion API
llm = Llama(model_path="./Q4_0/Q4_0-00001-of-00009.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }
    ]
)
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_GGUF.md-how-to-run end -->

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Llama-3-Open-Ko-8B-Instruct-preview


## Llama-3-Open-Ko-8B-Instruct-preview

> Update @ 2024.05.01: Pre-Release [Llama-3-KoEn-8B](https://huggingface.co/beomi/Llama-3-KoEn-8B-preview) model & [Llama-3-KoEn-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-KoEn-8B-Instruct-preview)

> Update @ 2024.04.24: Release [Llama-3-Open-Ko-8B model](https://huggingface.co/beomi/Llama-3-Open-Ko-8B) & [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview)

## Model Details

**Llama-3-Open-Ko-8B-Instruct-preview**

Llama-3-Open-Ko-8B model is continued pretrained language model based on Llama-3-8B.

This model is trained fully with publicily available resource, with 60GB+ of deduplicated texts.

With the new Llama-3 tokenizer, the pretraining conducted with 17.7B+ tokens, which slightly more than Korean tokenizer(Llama-2-Ko tokenizer).

The train was done on TPUv5e-256, with the warm support from TRC program by Google.

With applying the idea from [Chat Vector paper](https://arxiv.org/abs/2310.04799), I released Instruction model named [Llama-3-Open-Ko-8B-Instruct-preview](https://huggingface.co/beomi/Llama-3-Open-Ko-8B-Instruct-preview).

Since it is NOT finetuned with any Korean instruction set(indeed `preview`), but it would be great starting point for creating new Chat/Instruct models.

**Sample usage**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "beomi/Llama-3-Open-Ko-8B-Instruct-preview"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘."},
    {"role": "user", "content": "피보나치 수열이 뭐야? 그리고 피보나치 수열에 대해 파이썬 코드를 짜줘볼래?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    eos_token_id=terminators,
    do_sample=True,
    temperature=1,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```

**Sample Output**

    여러분께서는 물론 아시는지라도 설명을 드리겠습니다!  피보나치(Piconacci) 수열은 다음과 같은 수열을 말합니다: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,....  이렇게 계속되고 있습니다. 이 수열은 일반적으로는 수학에서 무한히 지속됩니다. 각 수는 이전 수의 두 배가 되는 수열입니다.

    이 수열을 파이썬(Python)으로 구현하고자 하신다면 다음과 같은 코드를 작성할 수 있습니다.
    ```python
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    ```
    이 코드에서는 `n`이 입력받은 수를 나타내는 변수로, 피보나치 수열을 구현합니다. 이 코드를 실행시키면 입력받은 수에 따라 피보나치 수열의 해당 항을 반환합니다. 예를 들어, `fibonacci(10)` 하면 55를 반환합니다.

    이 코드는 재귀적 함수이기 때문에 메모리 사용이 줄어들 수 있습니다. 그러나 재귀적 함수는 메모리 사용량이 많아질 수 있습니다. 이를 줄이기 위해 이터레이티브 함수로 구현할 수도 있습니다.
    ```python
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    ```
    이 코드에서는 이터레이티브 함수로 피보나치 수열을 구현합니다. 이 코드를 실행시키면 입력받은 수에 따라 피보나치 수열의 해당 항을 반환합니다. 이 코드는 메모리 사용량을 줄입니다. 다만, 이 코드는 더 복잡합니다. 이 코드를 더 간단하게 하려면 이터레이티브 함수를 더 잘 구현할 수 있습니다.
    ```python
    a, b = 0, 1
    while True:
        if n == 1:
            return a
        a, b = b, a + b
        n -= 1
    ```
    이 코드에서는 입력받은 수에 따라 피보나치 수열의...

### More samples

> I used same system prompt, but you could change on your own.

```python
messages = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘."},
    {"role": "user", "content": "한국의 제헌 헌법에 대해서 자세히 설명해주세요."},
]

이순신 장군은 조선시대의 무인으로, 대한민국의 국가유공자인 우의정공 이순신 장군은 1545년 9월 28일 경상남도 의령에서 태어났습니다. 이순신 장군은 통제사 시절의 왜란 때 조선과 명나라 연합군의 대규모 군대를 일으켜 대첩을 성공적으로 이끌어 정유재란과 임진왜란을 승리로 이끈 인물입니다. 그는 1592년 전라좌수영관찰사가 되어 전라좌수영에서 왜적을 물리쳤으며, 1597년에는 수원과 한양 방어을 성공적으로 치료했습니다. 또한 명량대첩에서 왜적과 격전하여 이순신 이순신 장군은 명량대첩에서 조선 관군의 승리를 이끌었습니다. 이순신 장군은 의리를 지키기 위해 전리품을 고수하는 결단을 내렸습니다. 이순신 장군은 1598년 사천성 전투에서 패전한 후 전세가 역전돼 전세가 불리해지자, 남하하여 이순신 장군은 결국 충무공 이순신의 칭호를 받았습니다. 그의 공적은 대한민국 이순신 장군 기념관으로 명예를 높이고 있습니다. 이순신 장군님은 선현의 칭호로 1963년 건국훈장 최고 훈장을 수여받았으며, 대한민국의 국보 제13호로 지정됐습니다. 이순신 장군은 전설적인 인물로 한국의 역사에서 큰 족적을 남겼습니다. 이순신 장군이 왜란 당시의 전투장소는 충무공이 신라 천자에게 나라를 위해 싸운 곳을 이순신 장군의 묘가 있습니다. 나라의 고난에 지성 이순신 장군님의 위업과 의리를 기념하는 곳입니다. 이순신 장군의 행적은 이순신 장군 기념관, 이순신 공원 등이 있습니다. 이순신 장군의 공적을 기념하기 위해 다양한 문화유산과 기념물이 조성됐습니다. 이순신 장군의 정신은 나라를 위해 싸운 위대한 우리의 영웅입니다. 1552년 12월에는 이순신 장군의 전설을 옛날 동네에 배향, 현재는 충무공 이순신 장군께서는 우리나라의 상징적 인물이 됐습니다. 이순신 장군은 조선왕조의 중시를 받고 있습니다. 이순신 장군은 선조에게 많은 대의를 이루었습니다. 이순신 장군의 공적을 오늘날에 이끌어 주는 인물입니다. 그를 모신 것은 전국의 사람들입니다. 이순신 장군님의 고결한 정신은 우리나라가 이룩한 성과입니다. 이순신 장군은 나라를 위해 싸운 위대한 인물입니다. 이순신 장군은 대한민국에서 가장 위대한 인물입니다. 이순신 장군의 행적은 영원히 기억 되겠지요.
```

```python
messages = [
    {"role": "system", "content": "친절한 챗봇으로서 상대방의 요청에 최대한 자세하고 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘."},
    {"role": "user", "content": "세종대왕의 집현전 맥북 던짐 사건에 대해서 알고 있어?"},
]

사과의 수량을 확인하겠습니다. 저는 5개의 사과가 있으신데, 그 중 2개를 이미 먹었으니 3개의 사과가 남아있습니다! ㅎㅎ. 계속해서 먹을 계획 없잖아요? 😉
```



<!-- original-model-card end -->
