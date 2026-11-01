

---
language:
- en
- ko
license: llama3
tags:
- saltlux
- luxia
- meta
- llama-3
- pytorch
- GGUF
pipeline_tag: text-generation
quantized_by: andrijdavid
---
# Ko-Llama3-Luxia-8B-GGUF
- Original model: [Ko-Llama3-Luxia-8B](https://huggingface.co/saltlux/Ko-Llama3-Luxia-8B)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Ko-Llama3-Luxia-8B](https://huggingface.co/saltlux/Ko-Llama3-Luxia-8B).

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

Under Download Model, you can enter the model repo: LiteLLMs/Ko-Llama3-Luxia-8B-GGUF and below it, a specific filename to download, such as: Q4_0/Q4_0-00001-of-00009.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download LiteLLMs/Ko-Llama3-Luxia-8B-GGUF Q4_0/Q4_0-00001-of-00009.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download LiteLLMs/Ko-Llama3-Luxia-8B-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install huggingface_hub[hf_transfer]
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download LiteLLMs/Ko-Llama3-Luxia-8B-GGUF Q4_0/Q4_0-00001-of-00009.gguf --local-dir . --local-dir-use-symlinks False
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
# Original model card: Ko-Llama3-Luxia-8B


# Model Details
Saltlux, AI Labs 언어모델팀에서 학습 및 공개한 <b>Ko-Llama3-Luxia-8B</b> 모델은 Meta에서 출시한 Llama-3-8B 모델을 <b>한국어에 특화</b>한 모델입니다.<br><br>
자체 보유하고 있는 1TB 이상의 한국어 학습 데이터 중, 약 100GB 정도의 데이터를 선별하여 사전학습에 활용하였습니다.<br><br>
또한 공개된 Llama-3 Tokenizer를 한국어로 확장하고 사전학습에 활용했습니다.

- **Meta Llama-3:** Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8 and 70B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety.
- **License:** Llama3 License [https://llama.meta.com/llama3/license](https://llama.meta.com/llama3/license)

### Intended Use
Ko-Llama3-Luxia-8B는 연구용으로 제작되었으며, 다양한 자연어 생성 태스크를 위해 자유롭게 학습 및 활용할 수 있습니다.

### How to Use
해당 모델 카드에는 `Ko-Llama3-Luxia-8B` 모델과 transformers 라이브러리 기반의 예시 코드를 제공합니다.

```
import transformers
import torch

model_id = "saltlux/Ko-Llama3-Luxia-8B"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)
pipeline("<|begin_of_text|>안녕하세요. 솔트룩스 AI Labs 입니다.")

```
# Training Details
한국어 특화를 위한 사전학습 데이터는 Saltlux에서 보유한 뉴스, 법률, 특허, 의료, 역사, 사회, 문화, 대화(문어/구어) 등의 도메인으로 구성된 100GB 수준의 코퍼스(~2023년)를 활용하였습니다.<br>
- 현재 제공되는 모델은 1 Epoch 학습된 모델입니다.<br>
### Use Device
사전학습은 NVIDIA H100 80GB * 8EA 장비를 활용하여 진행하였습니다.

#### Training Hyperparameters
<table>
	<tr>
		<td><strong>Model</strong>
		</td>
		<td><strong>Params</strong>
		</td>
		<td><strong>Context length</strong>
		</td>
		<td><strong>GQA</strong>
		</td>
		<td><strong>Learning rate</strong>
		</td>
		<td><strong>Batch</strong>
		</td>
		<td><strong>Precision</strong>
		</td>
	</tr>
  <tr>
	  <td>Ko-Llama3-Luxia-8B
	  </td>
	  <td>8B
	  </td>
	  <td>8k
	  </td>
	  <td>yes
	  </td>
	  <td>1e-5
	  </td>
	  <td>128
	  </td>
	  <td>bf16
	  </td>
	</tr>
</table>

### Tokenizer
Llama-3-Tokenizer를 한국어 특화하기 위해 한국어 토큰 17,536개를 추가하고 활용하였습니다.
<table>
	<tr>
		<td><strong>Model</strong>
		</td>
		<td><strong>Vocab Size</strong>
		</td>
	</tr>
  <tr>
	  <td>Llama-3
	  </td>
	  <td>128,256
	  </td>
	</tr>
	  <tr>
	  <td>Ko-Llama3-Luxia-8B
	  </td>
	  <td>145,792
	  </td>
	</tr>
</table>

### Tokenizer Result
+ Ko
<table>
	<tr>
		<td><strong>입력</strong>
		</td>
		<td><strong>Llama-3</strong>
		</td>
		<td><strong>Ko-Llama3-Luxia-8B</strong>
		</td>
	</tr>
  <tr>
	  <td>요즘 날씨가 너무 오락가락해서 아직도 겨울옷을 못치웠어요..
	  </td>
	  <td>['요', '즘', ' 날', '씨', '가', ' 너무', ' 오', '락', '가', '락', '해서', ' 아직', '도', ' 겨', '울', '�', '�', '을', ' 못', '치', '웠', '어요', '..']
	  </td>
	  <td>['요즘', ' 날씨', '가', ' 너무', ' 오락', '가락', '해서', ' 아직', '도', ' 겨울', '옷', '을', ' 못', '치', '웠', '어요', '..']
	  </td>
	</tr>
	<tr>
		 <td>맛있는 밥을 드셨습니까? 맛이 궁금하네요.
		 </td>
		 <td>['맛', '있는', ' �', '�', '을', ' 드', '셨', '습', '니까', '?', ' 맛', '이', ' 궁금', '하', '네요', '.']
		 </td>
		 <td>['맛', '있는', ' 밥', '을', ' 드셨', '습', '니까', '?', ' 맛', '이', ' 궁금', '하', '네요', '.']
		 </td>
	</tr>
	<tr>
		 <td>대법원부터 하급심 판례까지 원하는 판례를 찾는 가장 빠른 방법 - 서면 검색, 요청 판례, 유사 판례, AI 추천, 판례 및 법령 검색.
		 </td>
		 <td>['대', '법', '원', '부터', ' 하', '급', '심', ' 판', '례', '까지', ' 원', '하는', ' 판', '례', '를', ' 찾', '는', ' 가장', ' 빠', '른', ' 방법', ' -', ' 서', '면', ' 검색', ',', ' 요청', ' 판', '례', ',', ' 유', '사', ' 판', '례', ',', ' AI', ' 추천', ',', ' 판', '례', ' 및', ' 법', '령', ' 검색', '.']
		 </td>
		 <td>['대', '법', '원', '부터', ' 하', '급', '심', ' 판례', '까지', ' 원', '하는', ' 판례', '를', ' 찾', '는', ' 가장', ' 빠른', ' 방법', ' -', ' 서면', ' 검색', ',', ' 요청', ' 판례', ',', ' 유사', ' 판례', ',', ' AI', ' 추천', ',', ' 판례', ' 및', ' 법령', ' 검색', '.']
		 </td>
	</tr>
	<tr>
		 <td>본 발명은 금속판의 다수 부분을 에칭시켜 특정 무늬모양을 형성하는 건축용 금속재 장식판으로 이루어진 것에 특징이 있다.
		 </td>
		 <td>['본', ' 발', '명', '은', ' 금', '속', '판', '의', ' 다', '수', ' 부분', '을', ' 에', '칭', '시', '켜', ' 특', '정', ' 무', '�', '�', '모', '양', '을', ' 형', '성', '하는', ' 건', '축', '용', ' 금', '속', '재', ' 장', '식', '판', '으로', ' 이루', '어진', ' 것', '에', ' 특', '징', '이', ' 있다', '.']
		 </td>
		 <td>['본', ' 발명', '은', ' 금속', '판', '의', ' 다수', ' 부분', '을', ' 에칭', '시', '켜', ' 특정', ' 무늬', '모', '양', '을', ' 형성', '하는', ' 건축', '용', ' 금속', '재', ' 장식', '판', '으로', ' 이루어진', ' 것', '에', ' 특징', '이', ' 있다', '.']
		 </td>
	</tr>
	<tr>
		 <td>골다공증은 왜 생기는거에요? 그리고 치료하려면 어떻게해야하죠?
		 </td>
		 <td>['골', '다', '공', '증', '은', ' 왜', ' 생', '기는', '거', '에', '요', '?', ' 그리고', ' 치', '료', '하려', '면', ' 어떻게', '해야', '하', '죠', '?']
		 </td>
		 <td>['골', '다', '공증', '은', ' 왜', ' 생', '기는', '거', '에', '요', '?', ' 그리고', ' 치료', '하려', '면', ' 어떻게', '해야', '하', '죠', '?']
		 </td>
	</tr>
</table>

+ En
<table>
	<tr>
		<td><strong>입력</strong>
		</td>
		<td><strong>Llama-3</strong>
		</td>
		<td><strong>Ko-Llama3-Luxia-8B</strong>
		</td>
	</tr>
	<tr>
		 <td>Korean cuisine, hanguk yori, or hansik, has evolved through centuries of social and political change.
		 </td>
		 <td>['K', 'orean', ' cuisine', ',', ' h', 'angu', 'k', ' y', 'ori', ',', ' or', ' hans', 'ik', ',', ' has', ' evolved', ' through', ' centuries', ' of', ' social', ' and', ' political', ' change', '.']
		 </td>
		 <td>['K', 'orean', ' cuisine', ',', ' h', 'angu', 'k', ' y', 'ori', ',', ' or', ' hans', 'ik', ',', ' has', ' evolved', ' through', ' centuries', ' of', ' social', ' and', ' political', ' change', '.']
		 </td>
	</tr>
		<tr>
		 <td>Son Heung-min is a South Korean professional footballer who plays as a forward for and captains both Premier League club Tottenham Hotspur and the South Korea national team.
		 </td>
		 <td>['Son', ' He', 'ung', '-min', ' is', ' a', ' South', ' Korean', ' professional', ' football', 'er', ' who', ' plays', ' as', ' a', ' forward', ' for', ' and', ' captains', ' both', ' Premier', ' League', ' club', ' Tottenham', ' Hot', 'sp', 'ur', ' and', ' the', ' South', ' Korea', ' national', ' team', '.']
		 </td>
		 <td>['Son', ' He', 'ung', '-min', ' is', ' a', ' South', ' Korean', ' professional', ' football', 'er', ' who', ' plays', ' as', ' a', ' forward', ' for', ' and', ' captains', ' both', ' Premier', ' League', ' club', ' Tottenham', ' Hot', 'sp', 'ur', ' and', ' the', ' South', ' Korea', ' national', ' team', '.']
		 </td>
	</tr>
</table>

### Inference Result
<table>
<tr>
<td><strong>Llama-3</strong>
</td>
<td><strong>Ko-Llama3-Luxia-8B</strong>
</td>
</tr>
<tr>
<td><b>캐리비안베이는 용인에</b> 위치한 캐리비안 베이의 공식 온라인 카지노입니다. 캐리비안 베이는 1994년부터 운영되어 왔으며, 2005년에 온라인으로 오픈했습니다. 이 사이트는 영국에서 운영되는 라이센스를 가지고 있으며, 영국 정부가 승인하고 있습니다.\n캐리비안 베이는 다양한 게임을 제공합니다. 슬롯 머신, 블랙잭, 룰렛, 포커, 바카라 등이 있습니다. 또한, 캐리비안 베이는 다양한 보너스와 프로모션을 제공합니다. 예를 들어, 신규 회원에게는 가입 시 100% 배팅 보너스가 주어집니다. 또한, 매주마다 다양한 이벤트와 프로모션이 진행됩니다.<이하 생략>
</td>
<td><b>캐리비안베이는 용인에</b> 있는 놀이공원인데요. 캐리비안베이의 경우에는 워터파크와 놀이공원이 같이 있습니다. 그래서 여름에는 물놀이를 즐기고 겨울에는 눈썰매를 탈 수 있어서 사계절 내내 즐길 수 있는 곳이죠.\n캐리비안베이를 이용하려면 우선 홈페이지에서 입장권을 구매해야 합니다. 그리고 캐리비안베이의 경우에는 1년 동안 자유롭게 이용할 수 있는 연간회원권도 판매하는데요. 연간회원권은 성인과 어린이 모두 구매가 가능합니다.<이하 생략>
</td>
</tr>
<tr>
<td><b>베트남 쌀국수는</b> 한국의 국밥과 비슷한 음식입니다. 베트남 쌀국수에는 쌀, 돼지고기, 계란, 양파, 마늘, 생강, 고추 등이 들어갑니다.\n1. 쌀을 씻어 물에 담가 둡니다.\n2. 돼지고기를 잘게 썰고, 양파와 마늘, 생강, 고추를 다져줍니다.\n3. 팬에 기름을 두르고 돼지고기를 볶다가 양파와 마늘, 생강, 고추를 넣습니다.\n4. 계란을 풀어서 넣고, 간장을 넣어 볶아줍니다.\n5. 쌀을 물에 불려서 넣고, 끓으면 소금과 후추를 넣어줍니다.\n6. 쌀국수를 먹기 좋은 상태가 되면 꺼내 줍니다.\n7. 쌀국수의 위에 돼지고기와 계란을 얹어 먹습니다.\nVietnamese rice noodles are similar to Korean rice porridge. Vietnamese rice noodles contain rice, pork, eggs, onions, garlic, ginger and chili peppers.<이하 생략>
</td>
<td><b>베트남 쌀국수는</b> 일반적으로 얇게 썬 쌀가루로 만든 면을 사용합니다. 면은 뜨거운 물에 삶아서 찬물에 헹구어냅니다. 면이 삶아지면 육수와 야채를 넣고 끓입니다. 육수를 만들 때는 닭고기, 소고기, 돼지고기 등 다양한 재료를 사용할 수 있습니다. 야채로는 당근, 양파, 파 등을 사용할 수 있습니다.<이하 생략>
</td>
</tr>
<tr>
<td><b>한국의 전통의상인</b> 한복과 일본의 전통의상인 요로카미는 모두 5대륙의 문화를 수용하고, 각기 다른 지역의 특징을 반영한 의상을 갖추고 있다. 이러한 의상의 특징은 각각의 국가에서 발전해 온 역사와 문화에 기초한다. 한편, 한국의 한복과 일본의 요로카미는 서로 비슷한 형태를 가지고 있지만, 그 의미는 다르다. 한복은 한국인의 정체성을 나타내며, 요로카미는 일본인의 정체성을 나타낸다. 따라서 이 두 가지 의상은 서로 다른 문화적 배경을 가진 사람들의 정체성 표현에 사용된다.\nThe traditional costumes of Korea and Japan are hanbok and yorokami respectively. Both have been influenced by the cultures of other countries and reflect the characteristics of their respective regions. The distinctive features of these costumes are based on the history and culture of each country. However, although hanbok and yorokami share similar forms, they have different meanings. Hanbok represents Korean identity while yorokami represents Japanese identity. <이하 생략>
</td>
<td><b>한국의 전통의상인</b> 한복은 한국의 문화를 대표하는 상징물이다. 하지만 최근에는 한복을 입는 사람들이 점점 줄어들고 있다. 이는 여러 가지 이유가 있겠지만, 그 중 하나는 한복이 불편하기 때문일 것이다. 한복은 일반적인 옷보다 더 많은 부분을 덮어야 하고, 움직이기 어렵다. 또한, 한복은 세탁하기가 어렵고, 관리하기도 쉽지 않다.\n하지만 한복은 단순히 불편하고 관리하기 어려운 옷이 아니다. 한복은 한국인의 역사와 문화를 담고 있는 소중한 문화유산이다. 한복은 한국의 전통과 미를 표현하는 중요한 수단이며, 한국의 정체성을 나타내는 상징물이다. 따라서 우리는 한복을 보존하고 계승해야 한다.<이하 생략>
</td>
</tr>
</table>


### Citation instructions
**Ko-Llama3-Luxia-8B**
```
@article{kollama3luxiamodelcard,
  title={Ko Llama 3 Luxia Model Card},
  author={AILabs@Saltux},
  year={2024},
  url={https://huggingface.co/saltlux/Ko-Llama3-Luxia-8B/blob/main/README.md}
}
```

**Original Llama-3**
```
@article{llama3modelcard,
title={Llama 3 Model Card},
author={AI@Meta},
year={2024},
url={https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```

<!-- original-model-card end -->
