---
base_model: maywell/Synatra-V0.1-7B-Instruct
inference: false
language:
- ko
library_name: transformers
license: cc-by-nc-4.0
model_creator: Jeonghwan Park
model_name: Synatra V0.1 7B Instruct
model_type: mistral
pipeline_tag: text-generation
prompt_template: '<s>[INST] {prompt} [/INST]

  '
quantized_by: TheBloke
---
<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/theblokeai">Chat & support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Synatra V0.1 7B Instruct - GGUF
- Model creator: [Jeonghwan Park](https://huggingface.co/maywell)
- Original model: [Synatra V0.1 7B Instruct](https://huggingface.co/maywell/Synatra-V0.1-7B-Instruct)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Jeonghwan Park's Synatra V0.1 7B Instruct](https://huggingface.co/maywell/Synatra-V0.1-7B-Instruct).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.

<!-- README_GGUF.md-about-gguf end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF)
* [Jeonghwan Park's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/maywell/Synatra-V0.1-7B-Instruct)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Mistral

```
<s>[INST] {prompt} [/INST]

```

<!-- prompt-template end -->


<!-- compatibility_gguf start -->
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
<!-- compatibility_gguf end -->

<!-- README_GGUF.md-provided-files start -->
## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [synatra-v0.1-7b-instruct.Q2_K.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q2_K.gguf) | Q2_K | 2 | 3.08 GB| 5.58 GB | smallest, significant quality loss - not recommended for most purposes |
| [synatra-v0.1-7b-instruct.Q3_K_S.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q3_K_S.gguf) | Q3_K_S | 3 | 3.16 GB| 5.66 GB | very small, high quality loss |
| [synatra-v0.1-7b-instruct.Q3_K_M.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q3_K_M.gguf) | Q3_K_M | 3 | 3.52 GB| 6.02 GB | very small, high quality loss |
| [synatra-v0.1-7b-instruct.Q3_K_L.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q3_K_L.gguf) | Q3_K_L | 3 | 3.82 GB| 6.32 GB | small, substantial quality loss |
| [synatra-v0.1-7b-instruct.Q4_0.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q4_0.gguf) | Q4_0 | 4 | 4.11 GB| 6.61 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [synatra-v0.1-7b-instruct.Q4_K_S.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q4_K_S.gguf) | Q4_K_S | 4 | 4.14 GB| 6.64 GB | small, greater quality loss |
| [synatra-v0.1-7b-instruct.Q4_K_M.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q4_K_M.gguf) | Q4_K_M | 4 | 4.37 GB| 6.87 GB | medium, balanced quality - recommended |
| [synatra-v0.1-7b-instruct.Q5_0.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q5_0.gguf) | Q5_0 | 5 | 5.00 GB| 7.50 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [synatra-v0.1-7b-instruct.Q5_K_S.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q5_K_S.gguf) | Q5_K_S | 5 | 5.00 GB| 7.50 GB | large, low quality loss - recommended |
| [synatra-v0.1-7b-instruct.Q5_K_M.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q5_K_M.gguf) | Q5_K_M | 5 | 5.13 GB| 7.63 GB | large, very low quality loss - recommended |
| [synatra-v0.1-7b-instruct.Q6_K.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q6_K.gguf) | Q6_K | 6 | 5.94 GB| 8.44 GB | very large, extremely low quality loss |
| [synatra-v0.1-7b-instruct.Q8_0.gguf](https://huggingface.co/TheBloke/Synatra-V0.1-7B-Instruct-GGUF/blob/main/synatra-v0.1-7b-instruct.Q8_0.gguf) | Q8_0 | 8 | 7.70 GB| 10.20 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.



<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/Synatra-V0.1-7B-Instruct-GGUF and below it, a specific filename to download, such as: synatra-v0.1-7b-instruct.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Synatra-V0.1-7B-Instruct-GGUF synatra-v0.1-7b-instruct.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Synatra-V0.1-7B-Instruct-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Synatra-V0.1-7B-Instruct-GGUF synatra-v0.1-7b-instruct.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m synatra-v0.1-7b-instruct.Q4_K_M.gguf --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<s>[INST] {prompt} [/INST]"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model in Python code, using ctransformers

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install ctransformers
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]
# Or with AMD ROCm GPU acceleration (Linux only)
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems only
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

#### Simple ctransformers example code

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Synatra-V0.1-7B-Instruct-GGUF", model_file="synatra-v0.1-7b-instruct.Q4_K_M.gguf", model_type="mistral", gpu_layers=50)

print(llm("AI is going to"))
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_GGUF.md-how-to-run end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute

Thanks to the [chirper.ai](https://chirper.ai) team!

Thanks to Clay from [gpus.llm-utils.org](llm-utils)!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Aemon Algiz.

**Patreon special mentions**: Brandon Frisco, LangChain4j, Spiking Neurons AB, transmissions 11, Joseph William Delisle, Nitin Borwankar, Willem Michiel, Michael Dempsey, vamX, Jeffrey Morgan, zynix, jjj, Omer Bin Jawed, Sean Connelly, jinyuan sun, Jeromy Smith, Shadi, Pawan Osman, Chadd, Elijah Stavena, Illia Dulskyi, Sebastain Graf, Stephen Murray, terasurfer, Edmond Seymore, Celu Ramasamy, Mandus, Alex, biorpg, Ajan Kanaga, Clay Pascal, Raven Klaugh, 阿明, K, ya boyyy, usrbinkat, Alicia Loh, John Villwock, ReadyPlayerEmma, Chris Smitley, Cap'n Zoog, fincy, GodLy, S_X, sidney chen, Cory Kujawski, OG, Mano Prime, AzureBlack, Pieter, Kalila, Spencer Kim, Tom X Nguyen, Stanislav Ovsiannikov, Michael Levine, Andrey, Trailburnt, Vadim, Enrico Ros, Talal Aujan, Brandon Phillips, Jack West, Eugene Pentland, Michael Davis, Will Dee, webtim, Jonathan Leane, Alps Aficionado, Rooh Singh, Tiffany J. Kim, theTransient, Luke @flexchar, Elle, Caitlyn Gatomon, Ari Malik, subjectnull, Johann-Peter Hartmann, Trenton Dambrowitz, Imad Khwaja, Asp the Wyvern, Emad Mostaque, Rainer Wilmers, Alexandros Triantafyllidis, Nicholas, Pedro Madruga, SuperWojo, Harry Royden McLaughlin, James Bentley, Olakabola, David Ziegler, Ai Maven, Jeff Scroggin, Nikolai Manek, Deo Leter, Matthew Berman, Fen Risland, Ken Nordquist, Manuel Alberto Morcote, Luke Pendergrass, TL, Fred von Graf, Randy H, Dan Guido, NimbleBox.ai, Vitor Caleffi, Gabriel Tamborski, knownsqashed, Lone Striker, Erik Bjäreholt, John Detwiler, Leonard Tan, Iucharbius


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Jeonghwan Park's Synatra V0.1 7B Instruct



# **V0.3 IS UP**

[Link to V0.3](https://huggingface.co/maywell/Synatra-7B-v0.3-base)

# **Synatra-V0.1-7B**

Made by StableFluffy

[Visit my website! - Currently on consturction..](https://www.stablefluffy.kr/)

## License

This model is strictly [*non-commercial*](https://creativecommons.org/licenses/by-nc/4.0/) (**cc-by-nc-4.0**) use only which takes priority over the **LLAMA 2 COMMUNITY LICENSE AGREEMENT**.
The "Model" is completely free (ie. base model, derivates, merges/mixes) to use for non-commercial purposes as long as the the included **cc-by-nc-4.0** license in any parent repository, and the non-commercial use statute remains, regardless of other models' licences.
The licence can be changed after new model released.

## Model Details
**Base Model**
[mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)

**Trained On**
A6000 48GB * 8

## Instruction format

**학습 과정의 실수로 [/INST]가 아닌 [\INST]가 적용되었습니다. v0.2 에서 수정 될 예정입니다.**

In order to leverage instruction fine-tuning, your prompt should be surrounded by `[INST]` and `[\INST]` tokens. The very first instruction should begin with a begin of sentence id. The next instructions should not. The assistant generation will be ended by the end-of-sentence token id.
Plus, It is strongly recommended to add a space at the end of the prompt.

E.g.
```
text = "<s>[INST] 아이작 뉴턴의 업적을 알려줘. [\INST] "
```

# **Model Benchmark**

## KULLM Evaluation
구름v2 repo 에서 제공되는 데이터셋과 프롬프트를 사용하여 평가했습니다.
당시 GPT4와 현재 GPT4가 완전히 동일하지는 않기에 실제 결과와 약간의 차이가 존재 할 수 있습니다.

![img](./kullm_eval.png)
| Model | 이해가능성 | 자연스러움 | 맥락유지 | 흥미로움 | 지시어사용 | 전반적퀄리티
| --- | --- | --- | --- | --- | --- | ---
| GPT-3.5 | 0.980 | 2.806 | 2.849 | 2.056 | 0.917 | 3.905
| GPT-4 | 0.984 | 2.897 | 2.944 | 2.143 | 0.968 | 4.083
| KoAlpaca v1.1 | 0.651 | 1.909 | 1.901 | 1.583 | 0.385 | 2.575
| koVicuna | 0.460 | 1.583 | 1.726 | 1.528 | 0.409 | 2.440
| KULLM v2 | 0.742 | 2.083 | 2.107 | 1.794 | 0.548 | 3.036
| **Synatra-V0.1-7B** | **0.960** | **2.821** | **2.755** | **2.356** | **0.934** | **4.065**

## KOBEST_BOOLQ, SENTINEG, WIC - ZERO_SHOT
[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot)를 사용하여 BoolQ, SentiNeg, Wic을 측정했습니다.

HellaSwag와 COPA는 원본코드를 수정하는 과정에서 어려움을 겪어 아직 진행하지 않았습니다.

### NOTE
BoolQ에는 Instruction 모델의 이해를 돕기위해 "위 글에 대한 질문에 사실을 확인하는 작업입니다.", "예, 아니오로 대답해주세요."의 프롬프트를 추가했습니다.
SentiNeg에는 Instruction 모델의 이해를 돕기위해 "위 문장의 긍정, 부정 여부를 판단하세요."의 프롬프트를 추가했습니다.
Wic의 경우는 [INST], [\INST]만 추가하였습니다.


| Model | COPA | HellaSwag | BoolQ | SentiNeg | Wic
| --- | --- | --- | --- | --- | ---
| EleutherAI/polyglot-ko-12.8b | 0.7937 | 0.5954 | 0.4818 | 0.9117 | 0.3985
| **Synatra-V0.1-7B** | **NaN** | **NaN** | **0.849** | **0.8690** | **0.4881**

# **Implementation Code**

Since, chat_template already contains insturction format above.
You can use the code below.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("maywell/Synatra-V0.1-7B")
tokenizer = AutoTokenizer.from_pretrained("maywell/Synatra-V0.1-7B")

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

If you run it on oobabooga your prompt would look like this. - ** Need to add Space at the end! **
```
[INST] 링컨에 대해서 알려줘. [\INST]
```

> Readme format: [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)

---
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_maywell__Synatra-V0.1-7B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 53.54   |
| ARC (25-shot)         | 55.29          |
| HellaSwag (10-shot)   | 76.63    |
| MMLU (5-shot)         | 55.29         |
| TruthfulQA (0-shot)   | 55.76   |
| Winogrande (5-shot)   | 72.77   |
| GSM8K (5-shot)        | 19.41        |
| DROP (3-shot)         | 39.63         |

<!-- original-model-card end -->
