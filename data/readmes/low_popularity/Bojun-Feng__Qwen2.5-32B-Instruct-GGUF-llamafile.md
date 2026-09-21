---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GGUF/blob/main/LICENSE
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
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-32B-Instruct
tags:
- chat
---
<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://cdn-uploads.huggingface.co/production/uploads/64a523ba1ed90082dafde3d3/kJrkxofwOp-89uYFe0EBb.png" alt="LlamaFile" style="width: 50%; min-width: 400px; display: block; margin: auto;">

<!-- markdownlint-disable MD041 -->

<!-- header start -->
<!-- 200823 -->

I am not the original creator of llamafile, all credit of llamafile goes to Jartine:
<!-- README_llamafile.md-about-llamafile end -->
<!-- repositories-available start -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/FwAVVu7eJ4">Chat & support: jartine's Discord server</a></p>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">jartine's LLM work is generously supported by a grant from <a href="https://mozilla.org">mozilla</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Qwen2.5 32B Instruct GGUF - llamafile

## Run LLMs locally with a single file - No installation required!

All you need is download a file and run it.

Our goal is to make open source large language models much more
accessible to both developers and end users. We're doing that by
combining [llama.cpp](https://github.com/ggerganov/llama.cpp) with [Cosmopolitan Libc](https://github.com/jart/cosmopolitan) into one
framework that collapses all the complexity of LLMs down to
a single-file executable (called a "llamafile") that runs
locally on most computers, with no installation.

## How to Use (Modified from [Git README](https://github.com/Mozilla-Ocho/llamafile/tree/8f73d39cf3a767897b8ade6dda45e5744c62356a?tab=readme-ov-file#quickstart))

The easiest way to try it for yourself is to download our example llamafile.
With llamafile, all inference happens locally; no data ever leaves your computer.

1. Download the llamafile.

2. Open your computer's terminal.

3. If you're using macOS, Linux, or BSD, you'll need to grant permission
for your computer to execute this new file. (You only need to do this
once.)

```sh
chmod +x qwen2.5-32b-instruct-q8_0.gguf
```

4. If you're on Windows, rename the file by adding ".exe" on the end.

5. Run the llamafile. e.g.:

```sh
./qwen2.5-32b-instruct-q8_0.gguf
```

6. Your browser should open automatically and display a chat interface.
(If it doesn't, just open your browser and point it at http://localhost:8080.)

7. When you're done chatting, return to your terminal and hit
`Control-C` to shut down llamafile.

Note: Hugging Face has a 50GB file upload Limit, so you may need to use the `cat` instruction to concatenate large llamafiles to run them.

Here is an example doing so to `Mozilla/Meta-Llama-3.1-405B-Instruct-llamafile`:
```
wget https://huggingface.co/Mozilla/Meta-Llama-3.1-405B-llamafile/resolve/main/Meta-Llama-3.1-405B.Q2_K.cat0.llamafile
wget https://huggingface.co/Mozilla/Meta-Llama-3.1-405B-llamafile/resolve/main/Meta-Llama-3.1-405B.Q2_K.cat1.llamafile
wget https://huggingface.co/Mozilla/Meta-Llama-3.1-405B-llamafile/resolve/main/Meta-Llama-3.1-405B.Q2_K.cat2.llamafile
wget https://huggingface.co/Mozilla/Meta-Llama-3.1-405B-llamafile/resolve/main/Meta-Llama-3.1-405B.Q2_K.cat3.llamafile
cat Meta-Llama-3.1-405B.Q2_K.cat{0,1,2,3}.llamafile >Meta-Llama-3.1-405B.Q2_K.llamafile
rm Meta-Llama-3.1-405B.Q2_K.cat*.llamafile
chmod +x Meta-Llama-3.1-405B.Q2_K.llamafile
./Meta-Llama-3.1-405B.Q2_K.llamafile
```


Please note that LlamaFile is still under active development. Some methods may be not be compatible with the most recent documents.

## Settings for Qwen2.5 32B Instruct GGUF Llamafiles

- Model creator: [Qwen](https://huggingface.co/Qwen)
- Quantized GGUF files used: [Qwen/Qwen2.5-32B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GGUF/tree/a15e3cc10f8bbb2c0af6f8f1f34a32e3b060c09d)
  - Commit message "upload fp16 weights"
  - Commit hash a15e3cc10f8bbb2c0af6f8f1f34a32e3b060c09d
- LlamaFile version used: [Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile/tree/29b5f27172306da39a9c70fe25173da1b1564f82)
  - Commit message "Merge pull request #687 from Xydane/main  Add Support for DeepSeek-R1 models"
  - Commit hash 29b5f27172306da39a9c70fe25173da1b1564f82
- `.args` content format (example):

```
-m
qwen2.5-32b-instruct-q8_0.gguf
...
```

## (Following is original model card for Qwen2.5 32B Instruct GGUF)
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">


# Qwen2.5-32B-Instruct-GGUF

## Introduction

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters. Qwen2.5 brings the following improvements upon Qwen2:

- Significantly **more knowledge** and has greatly improved capabilities in **coding** and **mathematics**, thanks to our specialized expert models in these domains.
- Significant improvements in **instruction following**, **generating long texts** (over 8K tokens), **understanding structured data** (e.g, tables), and **generating structured outputs** especially JSON. **More resilient to the diversity of system prompts**, enhancing role-play implementation and condition-setting for chatbots.
- **Long-context Support** up to 128K tokens and can generate up to 8K tokens.
- **Multilingual support** for over 29 languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, Arabic, and more. 

**This repo contains the instruction-tuned 32B Qwen2.5 model in the GGUF Format**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 32.5B
- Number of Paramaters (Non-Embedding): 31.0B
- Number of Layers: 64
- Number of Attention Heads (GQA): 40 for Q and 8 for KV
- Context Length: Full 32,768 tokens and generation 8192 tokens
  - Note: Currently, only vLLM supports YARN for length extrapolating. If you want to process sequences up to 131,072 tokens, please refer to non-GGUF models.
- Quantization: q2_K, q3_K_M, q4_0, q4_K_M, q5_0, q5_K_M, q6_K, q8_0

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2.5/), [GitHub](https://github.com/QwenLM/Qwen2.5), and [Documentation](https://qwen.readthedocs.io/en/latest/).

## Quickstart

Check out our [llama.cpp documentation](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html) for more usage guide.

We advise you to clone [`llama.cpp`](https://github.com/ggerganov/llama.cpp) and install it following the official guide. We follow the latest version of llama.cpp. 
In the following demonstration, we assume that you are running commands under the repository `llama.cpp`.

Since cloning the entire repo may be inefficient, you can manually download the GGUF file that you need or use `huggingface-cli`:
1. Install
   ```shell
   pip install -U huggingface_hub
   ```
2. Download:
   ```shell
   huggingface-cli download Qwen/Qwen2.5-32B-Instruct-GGUF --include "qwen2.5-32b-instruct-q5_k_m*.gguf" --local-dir . --local-dir-use-symlinks False
   ```
   For large files, we split them into multiple segments due to the limitation of file upload. They share a prefix, with a suffix indicating its index. For examples, `qwen2.5-32b-instruct-q5_k_m-00001-of-00006.gguf` to `qwen2.5-32b-instruct-q5_k_m-00006-of-00006.gguf`. The above command will download all of them.
3. (Optional) Merge:
   For split files, you need to merge them first with the command `llama-gguf-split` as shown below:
   ```bash
   # ./llama-gguf-split --merge <first-split-file-path> <merged-file-path>
   ./llama-gguf-split --merge qwen2.5-32b-instruct-q5_k_m-00001-of-00006.gguf qwen2.5-32b-instruct-q5_k_m.gguf
   ```

For users, to achieve chatbot-like experience, it is recommended to commence in the conversation mode:

```shell
./llama-cli -m <gguf-file-path> \
    -co -cnv -p "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." \
    -fa -ngl 80 -n 512
```


## Evaluation & Performance

Detailed evaluation results are reported in this [📑 blog](https://qwenlm.github.io/blog/qwen2.5/).

For quantized models, the benchmark results against the original bfloat16 models can be found [here](https://qwen.readthedocs.io/en/latest/benchmark/quantization_benchmark.html)

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