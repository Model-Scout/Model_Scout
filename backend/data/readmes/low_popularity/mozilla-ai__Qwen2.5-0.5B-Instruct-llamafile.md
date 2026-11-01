---
license: apache-2.0
pipeline_tag: text-generation
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
license_link: LICENSE
base_model: Qwen/Qwen2.5-0.5B
quantized_by: bartowski
tags:
- llamafile
- chat
---

# Qwen 2.5 Instruct 0.5B - llamafile

- Model creator: [Qwen](https://huggingface.co/Qwen/)
- Original model: [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/)

Mozilla packaged the Qwen 2.5 models into executable weights that we
call [llamafiles](https://github.com/Mozilla-Ocho/llamafile). This gives
you the easiest fastest way to use the model on Linux, MacOS, Windows,
FreeBSD, OpenBSD and NetBSD systems you control on both AMD64 and ARM64.

*Software Last Updated: 2025-03-31*

*Llamafile Version: 0.9.2*

## Quickstart

To get started, you need both the Qwen 2.5 weights, and the llamafile
software. Both of them are included in a single file, which can be
downloaded and run as follows:

```
wget https://huggingface.co/Mozilla/Qwen2.5-0.5B-Instruct-llamafile/resolve/main/Qwen2.5-0.5B-Instruct-Q6_K.llamafile
chmod +x Qwen2.5-0.5B-Instruct-Q6_K.llamafile
./Qwen2.5-0.5B-Instruct-Q6_K.llamafile
```

The default mode of operation for these llamafiles is our new command
line chatbot interface.

## Usage

You can use triple quotes to ask questions on multiple lines. You can
pass commands like `/stats` and `/context` to see runtime status
information. You can change the system prompt by passing the `-p "new
system prompt"` flag. You can press CTRL-C to interrupt the model.
Finally CTRL-D may be used to exit.

If you prefer to use a web GUI, then a `--server` mode is provided, that
will open a tab with a chatbot and completion interface in your browser.
For additional help on how it may be used, pass the `--help` flag. The
server also has an OpenAI API compatible completions endpoint that can
be accessed via Python using the `openai` pip package.

```
./Qwen2.5-0.5B-Instruct-Q6_K.llamafile --server
```

An advanced CLI mode is provided that's useful for shell scripting. You
can use it by passing the `--cli` flag. For additional help on how it
may be used, pass the `--help` flag.

```
./Qwen2.5-0.5B-Instruct-Q6_K.llamafile --cli -p 'four score and seven' --log-disable
```

## Troubleshooting

Having **trouble?** See the ["Gotchas"
section](https://github.com/mozilla-ocho/llamafile/?tab=readme-ov-file#gotchas-and-troubleshooting)
of the README.

On Linux, the way to avoid run-detector errors is to install the APE
interpreter.

```sh
sudo wget -O /usr/bin/ape https://cosmo.zip/pub/cosmos/bin/ape-$(uname -m).elf
sudo chmod +x /usr/bin/ape
sudo sh -c "echo ':APE:M::MZqFpD::/usr/bin/ape:' >/proc/sys/fs/binfmt_misc/register"
sudo sh -c "echo ':APE-jart:M::jartsr::/usr/bin/ape:' >/proc/sys/fs/binfmt_misc/register"
```

On Windows there's a 4GB limit on executable sizes.

## Context Window

This model has a max context window size of 128k tokens. By default, a
context window size of 8192 tokens is used. You can ask llamafile 
to use the maximum context size by passing the `-c 0` flag. That's big 
enough for a small book. If you want to be able to have a conversation
with your book, you can use the `-f book.txt` flag.

## GPU Acceleration

On GPUs with sufficient RAM, the `-ngl 999` flag may be passed to use
the system's NVIDIA or AMD GPU(s). On Windows, only the graphics card
driver needs to be installed if you own an NVIDIA GPU. On Windows, if
you have an AMD GPU, you should install the ROCm SDK v6.1 and then pass
the flags `--recompile --gpu amd` the first time you run your llamafile.

On NVIDIA GPUs, by default, the prebuilt tinyBLAS library is used to
perform matrix multiplications. This is open source software, but it
doesn't go as fast as closed source cuBLAS. If you have the CUDA SDK
installed on your system, then you can pass the `--recompile` flag to
build a GGML CUDA library just for your system that uses cuBLAS. This
ensures you get maximum performance.

For further information, please see the [llamafile
README](https://github.com/mozilla-ocho/llamafile/).

## About llamafile

llamafile is a new format introduced by Mozilla on Nov 20th 2023. It
uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp
binaries that run on the stock installs of six OSes for both ARM64 and
AMD64.

---

# Qwen2.5-0.5B-Instruct

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 0.5B Qwen2.5 model**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias and tied word embeddings
- Number of Parameters: 0.49B
- Number of Paramaters (Non-Embedding): 0.36B
- Number of Layers: 24
- Number of Attention Heads (GQA): 14 for Q and 2 for KV
- Context Length: Full 32,768 tokens and generation 8192 tokens

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2.5/), [GitHub](https://github.com/QwenLM/Qwen2.5), and [Documentation](https://qwen.readthedocs.io/en/latest/).

## Requirements

The code of Qwen2.5 has been in the latest Hugging face `transformers` and we advise you to use the latest version of `transformers`.

With `transformers<4.37.0`, you will encounter the following error:
```
KeyError: 'qwen2'
```

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```


## Evaluation & Performance

Detailed evaluation results are reported in this [📑 blog](https://qwenlm.github.io/blog/qwen2.5/).

For requirements on GPU memory and the respective throughput, see results [here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html).

## Citation

If you find our work helpful, feel free to give us a cite.

```
@misc{qwen2.5,
    title = {Qwen2.5: A Party of Foundation Models},
    url = {https://qwenlm.github.io/blog/qwen2.5/},
    author = {Qwen Team},
    month = {September},
    year = {2024}
}

@article{qwen2,
      title={Qwen2 Technical Report}, 
      author={An Yang and Baosong Yang and Binyuan Hui and Bo Zheng and Bowen Yu and Chang Zhou and Chengpeng Li and Chengyuan Li and Dayiheng Liu and Fei Huang and Guanting Dong and Haoran Wei and Huan Lin and Jialong Tang and Jialin Wang and Jian Yang and Jianhong Tu and Jianwei Zhang and Jianxin Ma and Jin Xu and Jingren Zhou and Jinze Bai and Jinzheng He and Junyang Lin and Kai Dang and Keming Lu and Keqin Chen and Kexin Yang and Mei Li and Mingfeng Xue and Na Ni and Pei Zhang and Peng Wang and Ru Peng and Rui Men and Ruize Gao and Runji Lin and Shijie Wang and Shuai Bai and Sinan Tan and Tianhang Zhu and Tianhao Li and Tianyu Liu and Wenbin Ge and Xiaodong Deng and Xiaohuan Zhou and Xingzhang Ren and Xinyu Zhang and Xipin Wei and Xuancheng Ren and Yang Fan and Yang Yao and Yichang Zhang and Yu Wan and Yunfei Chu and Yuqiong Liu and Zeyu Cui and Zhenru Zhang and Zhihao Fan},
      journal={arXiv preprint arXiv:2407.10671},
      year={2024}
}
```
