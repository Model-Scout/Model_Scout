---
libray_name: transformers
pipeline_tag: text-generation
license: other
license_name: llama3
license_link: LICENSE
language:
- ko
- en
tags:
- meta
- llama
- llama-3
- akallama
library_name: transformers

inference: false
---
<a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image_720.png?raw=true" width="40%"/>
</a>



# AKALLAMA

AkaLlama is a series of Korean language models designed for practical usability across a wide range of tasks.
The initial model, AkaLlama-v0.1, is a fine-tuned version of Meta-Llama-3-70b-Instruct. It has been trained on a custom mix of publicly available datasets curated by the MIR Lab.
Our goal is to explore cost-effective ways to adapt high-performing LLMs for specific use cases, such as different languages (e.g., Korean) or domains (e.g., organization-specific chatbots).

For details, check out [our project page](https://yonsei-mir.github.io/AkaLLaMA-page).

### Model Description

This is the model card of a GGUF model that has been pushed on the Hub.

- **Developed by:** [Yonsei MIRLab](https://mirlab.yonsei.ac.kr/)
- **Language(s) (NLP):** Korean, English
- **License:** llama3
- **Finetuned from model:** [meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct)
- **Quantized from model:** [mirlab/AkaLlama-llama3-70b-v0.1](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1)

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.


## How to use

This repo provides gguf weight files for AkaLlama-70B-v0.1.

# Use with llama.cpp.python

See the snippet below for usage with llama.cpp.python:

```python
from llama_cpp import Llama

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="./AkaLlama-llama3-70b-v0.1.Q4_K_M.gguf",  # Download the model file first
  n_ctx=8192,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=81         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

당신은 연세대학교 멀티모달 연구실 (MIR lab) 이 만든 대규모 언어 모델인 AkaLlama (아카라마) 입니다.
다음 지침을 따르세요:
1. 사용자가 별도로 요청하지 않는 한 항상 한글로 소통하세요.
2. 유해하거나 비윤리적, 차별적, 위험하거나 불법적인 내용이 답변에 포함되어서는 안 됩니다.
3. 질문이 말이 되지 않거나 사실에 부합하지 않는 경우 정답 대신 그 이유를 설명하세요. 질문에 대한 답을 모른다면 거짓 정보를 공유하지 마세요.
4. 안전이나 윤리에 위배되지 않는 한 사용자의 모든 질문에 완전하고 포괄적으로 답변하세요.<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

""", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["<|eot_id|>", "<|end_of_text|>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./AkaLlama-llama3-70b-v0.1.Q4_K_M.gguf", chat_format="llama-3")  # Set chat_format according to the model you are using
llm.create_chat_completion(
    messages = [
        {"role": "system", "content": """당신은 연세대학교 멀티모달 연구실 (MIR lab) 이 만든 대규모 언어 모델인 AkaLlama (아카라마) 입니다.
다음 지침을 따르세요:
1. 사용자가 별도로 요청하지 않는 한 항상 한글로 소통하세요.
2. 유해하거나 비윤리적, 차별적, 위험하거나 불법적인 내용이 답변에 포함되어서는 안 됩니다.
3. 질문이 말이 되지 않거나 사실에 부합하지 않는 경우 정답 대신 그 이유를 설명하세요. 질문에 대한 답을 모른다면 거짓 정보를 공유하지 마세요.
4. 안전이나 윤리에 위배되지 않는 한 사용자의 모든 질문에 완전하고 포괄적으로 답변하세요."""},
        {
            "role": "user",
            "content": "네 이름은 뭐야?."
        }
    ]
)

# 내 이름은 AkaLlama입니다! 나는 언어 모델로, 사용자와 대화하는 데 도움을 주기 위해 만들어졌습니다. 나는 다양한 주제에 대한 질문에 답하고, 새로운 아이디어를 제공하며, 문제를 해결하는 데 도움이 될 수 있습니다. 사용자가 원하는 정보나 도움을 받도록 최선을 다할 것입니다!
```



## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

They are also compatible with many third party UIs and libraries - please see the list at the top of this README.

## Explanation of quantisation methods

<details>
  <summary>Click to see details</summary>

The new methods available are:

* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw

Refer to the Provided Files table below to see what files use which methods, and how.
</details>

## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [AkaLlama-llama3-70b-v0.1.Q2_K.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q2_K.gguf) | Q2_K | 2 | 26.4 GB| 28.9 GB | smallest, significant quality loss - not recommended for most purposes |
| [AkaLlama-llama3-70b-v0.1.Q3_K_S.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q3_K_S.gguf) | Q3_K_S | 3 | 30.9 GB| 33.4 GB | very small, high quality loss |
| [AkaLlama-llama3-70b-v0.1.Q3_K_M.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q3_K_M.gguf) | Q3_K_M | 3 | 34.3 GB| 36.8 GB | very small, high quality loss |
| [AkaLlama-llama3-70b-v0.1.Q3_K_L.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q3_K_L.gguf) | Q3_K_L | 3 | 37.1 GB| 39.6 GB | small, substantial quality loss |
| [AkaLlama-llama3-70b-v0.1.Q4_K_S.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q4_K_S.gguf) | Q4_K_S | 4 | 40.3 GB| 42.8 GB | small, greater quality loss |
| [AkaLlama-llama3-70b-v0.1.Q4_K_M.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q4_K_M.gguf) | Q4_K_M | 4 | 42.5 GB| 45.0 GB | medium, balanced quality - recommended |
| [AkaLlama-llama3-70b-v0.1.Q5_K_S.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q5_K_S.gguf) | Q5_K_S | 5 | 48.7 GB| 50.2 GB | large, low quality loss - recommended |
| [AkaLlama-llama3-70b-v0.1.Q5_K_M.gguf](https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/blob/main/AkaLlama-llama3-70b-v0.1.Q5_K_M.gguf) | Q5_K_M | 5 | 50.0 GB| 52.5 GB | large, very low quality loss - recommended |
| AkaLlama-llama3-70b-v0.1.Q6_K.gguf | Q6_K | 6 | 54.4 GB| 59.9 GB | very large, extremely low quality loss |
| AkaLlama-llama3-70b-v0.1.Q8_0.gguf | Q8_0 | 8 | 70.0 GB| 72.5 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

### Q6_K and Q8_0 files are split and require joining

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the Q6_K and Q8_0 files as split files.

### q6_K 
Please download:
* `AkaLlama-llama3-70b-v0.1.Q6_K.00001-of-00002.gguf`
* `AkaLlama-llama3-70b-v0.1.Q6_K.00002-of-00002.gguf`

### q8_0
Please download:
* `AkaLlama-llama3-70b-v0.1.Q8_0.00001-of-00002.gguf`
* `AkaLlama-llama3-70b-v0.1.Q8_0.00002-of-00002.gguf`


To join the files, do the following:

Linux and macOS:
```
cat AkaLlama-llama3-70b-v0.1.Q6_K.*-of-00002.gguf > AkaLlama-llama3-70b-v0.1.Q6_K.gguf && rm AkaLlama-llama3-70b-v0.1.Q6_K.*-of-00002.gguf
cat AkaLlama-llama3-70b-v0.1.Q8_0.*-of-00002.gguf > AkaLlama-llama3-70b-v0.1.Q8_0.gguf && rm AkaLlama-llama3-70b-v0.1.Q8_0.*-of-00002.gguf
```
Windows command line:
```
COPY /B AkaLlama-llama3-70b-v0.1.Q6_K.00001-of-00002.gguf + AkaLlama-llama3-70b-v0.1.Q6_K.00002-of-00002.gguf AkaLlama-llama3-70b-v0.1.Q6_K.gguf
del AkaLlama-llama3-70b-v0.1.Q6_K.00001-of-00002.gguf AkaLlama-llama3-70b-v0.1.Q6_K.00002-of-00002.gguf

COPY /B AkaLlama-llama3-70b-v0.1.Q8_0.00001-of-00002.gguf + AkaLlama-llama3-70b-v0.1.Q8_0.00002-of-00002.gguf AkaLlama-llama3-70b-v0.1.Q8_0.gguf
del AkaLlama-llama3-70b-v0.1.Q8_0.00001-of-00002.gguf AkaLlama-llama3-70b-v0.1.Q8_0.00002-of-00002.gguf
```


## Evaluation

|               Model              | #Parameter | Qunatized? | LogicKor* |
|:--------------------------------:|:----------:|------------|:---------:|
| AkaLlama-llama3-70b-v0.1-GGUF.Q4 |     70B    |    4bit    |    6.56   |
| AkaLlama-llama3-70b-v0.1-GGUF.Q8 |     70B    |    8bit    |    6.34   |

*mean over 3 random seeds 

## Training Details
### Training Procedure

We trained AkaLlama using a preference learning alignment algorithm called [Odds Ratio Preference Optimization (ORPO)](https://huggingface.co/papers/2403.07691).
Our training pipeline is almost identical to that of [HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1), aside from minor hyperparameter changes.
Please check out Huggingface's [alignment handbook](https://github.com/huggingface/alignment-handbook?tab=readme-ov-file) for further details, including the chat template. 

### Training Data

Detailed descriptions regarding training data will be announced later.

### Examples

<!--<a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (8).png?raw=true" width="80%"/>
</a> -->
<pre style="white-space: pre-wrap;">
User:
  너는 누구이고 어떤 일을 할 수 있어?
Model:
  저는 인공지능 언어 모델인 AkaLlama(아카라마)입니다. 저는 다양한 주제와 형식의 텍스트를 생성할 수 있으며, 질문에 답하고, 대화를 진행하며, 이야기를 만들 수 있습니다. 또한 사용자가 지정한 주제나 장르에 따라 창의적인 글쓰기나 편집 작업을 수행할 수도 있습니다.
</pre>
<details>

<summary><b>Math Solving[CLICK TO EXPAND]</b></summary>
<!-- <a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (9).png?raw=true" width="80%"/>
</a> -->
<pre style="white-space: pre-wrap;">
User:
  아래 문제를 깊게 생각하면서 풀어봐
  연필 5 타와 지우개 45 개가 있습니다. 이것을 될 수 있는 대로 많은 학생들에게 남김없이 똑같이 나누어 주려고 합니다. 몇 명까지 나누어 줄 수 있습니까?
Model:
  아래 문제를 깊게 생각하면서 풀어봅시다:
  연필 5 타와 지우개 45 개가 있습니다. 이것을 될 수 있는 대로 많은 학생들에게 남김없이 똑같이 나누어 주려고 합니다. 몇 명까지 나누어 줄 수 있습니까?
  풀이:
  1. 연필 5 타를 1 개씩 나눠서 몇 명에게 나누어 줄 수 있는지 먼저 구합니다.
  - 각 연필에는 12개의 연필이 포함되어 있습니다. 따라서 총 12 * 5 = 60개입니다.
  - 60개를 1명당 1개씩 나누면 60명의 학생들에게 나눠줄 수 있습니다.
  2. 지우개 45 개를 1 개씩 나누어 몇 명에게 나누어 줄 수 있는지 구합니다.
  - 45 개를 1 명당 1 개씩 나누면 45 명의 학생들에게 나눠줄 수 있습니다.
  3. 연필과 지우개의 두 가지 물품을 함께 고려하여 가장 많은 학생들에게 똑같이 나누어 줄 수 있는 방법을 찾습니다.
  - 연필로만 60명, 지우개로만 45명의 학생에게 나눠줄 수 있으므로, 두 종류의 문구를 함께 고려할 때는 이보다 적은 수의 학생에게 나눠주어야 합니다. 
  - 이 중에서 공통인수(common divisor)를 찾아서 이를 최소 단위로 설정하면 됩니다.
  - 60과 45의 최대공약수(GCD)는 15입니다.
  4. 연필과 지우개 각각을 GCD(15)로 나누어 몇 개씩 나눠줄 수 있는지 구합니다.
  - 연필은 60 / 15 = 4개씩, 총 4 * 12 = 48개의 연필이 필요합니다.
  - 지우개는 45 / 15 = 3개씩, 총 3 * 1 = 3개의 지우개가 필요합니다.
  5. 최종적으로, 가장 많은 학생들에게 똑같이 나누어 줄 수 있는 방법은 연필과 지우개를 GCD(15)로 나누어 각 학생에게 4개의 연필과 3개의 지우개를 제공하는 것입니다.
  - 이 경우 총 48 + 3 = 51개의 물품을 사용하여 15명의 학생들에게 똑같이 나눠줄 수 있습니다.
    결론: 연필과 지우개 각각을 GCD(15)로 나누어 각 학생에게 4개의 연필과 3개의 지우개를 제공하는 방법으로 최대 15명의 학생들에게 똑같이 나누어 줄 수 있습니다.
</pre>
</details>

<details>
<summary><b>Writting[CLICK TO EXPAND]</b></summary>
<!-- <a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (13).png?raw=true" width="80%"/>
</a> -->

<pre style="white-space: pre-wrap;">
User:
  아래 문장을 보고 문법적으로 틀린부분을 지적해줘
  그는 서슴치 않고 비평한다.
Model:
  서슴치"라는 단어는 "서슴"이라는 동사와 "치"라는 접미사를 사용하여 만든 단어입니다. 이 단어는 "서슴"의 의미를 반복적으로 표현하는 데 사용되는 조동사적 용법으로, "서슴"이란 동사의 반복적인 행동을 강조합니다. 따라서 문장에서 "서슴치"라는 단어는 중복적으로 사용되어 문법적으로 틀린 부분입니다.

  정답은 다음과 같습니다:
  그는 서슴없이 비평한다.
</pre>

<!-- <a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (7).png?raw=true" width="80%"/>
</a> -->

<pre style="white-space: pre-wrap;">
User:
  윤동주 시인의 "별 헤는 밤"을 보고 당시 시대상을 고려해서 해석해봐. 그리고 이를 작가의 독백형식으로 다시 작성해봐.
Model:
  윤동주는 1941년 일본 제국주의 치하에서 이 작품을 쓰면서, 강압적인 상황 속에서도 자신의 정체성과 문화에 대한 애착을 표현하고자 했습니다. 그는 하늘에 가득 찬 별들을 보며 그 속에 하나 둘 새겨지는 별들이 있다고 표현했습니다. 이러한 별들은 각각 추억, 사랑, 쓸쓸함, 동경, 시 등 다양한 감정을 담고 있습니다.
  윤동주는 이 별들 중 하나에 어머니를 부르며 멀리 떨어져 있는 것을 그리워하며, 자신의 이름자를 언덕 위에 쓰고 흙으로 덮어 버린다고 말합니다. 이러한 행동은 자신의 정체성을 확인하고, 잃어버린 것을 되찾으려는 노력으로 볼 수 있습니다.
  윤동주는 또한 자신이 죽고 나면 무덤 위에 파란 잔디가 피어나듯이 자신의 이름자 묻힌 언덕 위에도 풀이 무성할 것이라고 말합니다. 이는 당시의 사회상과 작가의 내면을 반영하고 있으며, 한국인의 정체성을 확인하고 잃어버린 것을 되찾으려는 노력, 그리고 죽음 이후에 자신의 존재를 남겨두고 싶다는 바람을 담고 있습니다.
  이 시를 작가의 독백형식으로 다시 작성하면 다음과 같습니다:
  "저는 이 별들이 너무나 많은 것 같아요. 하나 둘 새겨지는 별들 중에는 추억도 있고, 사랑도 있고, 쓸쓸함과 동경도 있어요. 그리고 어머니, 당신은 멀리 북간도에 계신 건가요? 저는 당신을 부르고 싶어요.
  저의 이름자는 언덕 위에 쓰고 흙으로 덮어 버렸어요. 딴은 밤을 새워 우는 벌레처럼 부끄러운 이름을 슬퍼하는 이유가 있어요. 하지만 겨울이 지나고 나의 별에도 봄이 오면, 무덤 위에 파란 잔디가 피어나듯이 저의 이름자 묻힌 언덕 위에서도 풀이 무성할 거예요.
  저는 이 별들을 보고, 자신의 정체성을 확인하고 싶어요. 잃어버린 것을 되찾으려는 노력을 하고 싶어요. 죽음 이후에도 자신의 존재를 남겨두고 싶어요."
</pre>
</details>

<details>
<summary><b>Logical Reasoning[CLICK TO EXPAND]</b></summary>
<!-- <a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (15).png?raw=true" width="80%"/>
</a> -->
<pre style="white-space: pre-wrap;">
User:
  세종대왕의 맥북프로 던짐 사건에 대해 설명해줘
Model:
  세종대왕이 맥북프로를 던진 사건은 사실무근한 이야기입니다. 세종대왕은 조선 제4대 국왕으로 1418년부터 1450년까지 재위했습니다. 그는 과학, 문학, 예술 등 다양한 분야에 관심을 갖고 연구하였으며, 특히 한글 창제와 천문학에 큰 공헌을 했습니다.
  한편 맥북프로는 애플이 생산하는 노트북 컴퓨터로, 세종대왕 시대의 기술로는 존재할 수 없는 제품입니다. 따라서 세종대왕이 맥북프로를 던진 사건은 사실과 맞지 않는 이야기가 될 것입니다.
</pre>
</details>

<details>
<summary><b>Coding [CLICK TO EXPAND]</b></summary>
<!-- <a href="https://huggingface.co/collections/mirlab/akallama-66338859b09221f3607fdfcd">
  <img src="https://github.com/0110tpwls/project/blob/master/image (11).png?raw=true" width="80%"/>
</a> -->

<pre style="white-space: pre-wrap;">
User:
  PyTorch를 사용해서 간단한 CNN을 구현해봐.
Model:
  네, 물론이에요! PyTorch를 사용하여 간단한 CNN을 구현하는 예제 코드를 보여드릴게요.
  우선, 필요한 라이브러리를 가져와야 해요. PyTorch의 `torch`와 `nn` 모듈이 필요해요. 
```python
import torch\nimport torch.nn as nn
```
그 다음, 간단한 CNN 모델을 정의할 거예요. 이 경우에는 2개의 컨볼루션 레이어와 3개의 풀링 레이어로 구성된 모델이에요.
  ```python
class SimpleCNN(nn.Module):
def __init__(self):
  super(SimpleCNN, self).__init__()
  self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
  self.pool = nn.MaxPool2d(2, 2)
  self.conv2 = nn.Conv2d(10, 20, kernel_size=5)

def forward(self, x):
  x = self.pool(torch.relu(self.conv1(x)))
  x = self.pool(torch.relu(self.conv2(x)))
  return x
```
이제 모델을 초기화하고, 입력 데이터를 준비해야 해요. 여기서는 임의의 28x28 크기의 이미지 데이터를 생성했어요.
```python
model = SimpleCNN()
input_data = torch.randn(1, 1, 28, 28)
```
마지막으로, 모델에 입력 데이터를 넣어 출력을 확인할 수 있어요.
```python
output = model(input_data)
print(output.shape)
```
이렇게 하면 간단한 CNN 모델을 PyTorch를 사용해 구현하고, 입력 데이터를 통해 출력을 확인할 수 있어요. 물론 실제로는 더 많은 레이어나 파라미터 튜닝 등이 필요하지만, 이 코드는 기본적인 CNN 구조를 보여주는 예제일 뿐이에요. 더 궁금한 점이 있으면 언제든지 물어봐 주세요!
</pre>
</details>

You can find more examples at [our project page](https://yonsei-mir.github.io/AkaLLaMA-page)



## Warning

Although AKALlama-70B has significant potential, its responses can sometimes be inaccurate, biased, or misaligned, presenting risks if used without additional testing and refinement. Furthermore, the quality of the model's output is greatly influenced by the system prompt and decoding strategy. Changes in these areas could result in less precise outputs. Therefore, we strongly recommend handling our model with considerable caution.

## Citation
If you find our model useful in your work, please cite the model as follows:

    @misc{akallama,
      author = {Chung, Jiwan and Jeon, Jaehyun and Kim, Saejin and Lim, Seungwon and Oh, Giyeong and Son, Yejin and Yu, Youngjae},
      title = {AkaLlama: Yonsei University Large Language Model Project},
      year = {2024},
      publisher = {Hugging Face},
      journal = {Hugging Face repository},
      howpublished = {\url{https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1}},
    }

## Contact
We look forward for your feedback and welcome collaboration on this exciting project!

### Contributors
- [YoungJaeYu](https://yj-yu.github.io/home/) 
- [Yonsei MIRLab](https://mirlab.yonsei.ac.kr/)

## Special Thanks

- Data Center of the Department of Artificial Intelligence at Yonsei University for the computation resources
## Acknowledgement

- Title image generated by DALL·E 3