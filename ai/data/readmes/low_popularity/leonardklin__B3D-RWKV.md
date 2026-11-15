---
base_model: BlinkDL/rwkv7-g1
datasets:
- allenai/tulu-3-sft-mixture
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
- angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k
language:
- en
- zh
- fr
- es
- de
- pt
- ru
- it
- ja
- ko
- vi
- ar
license: apache-2.0
pipeline_tag: text-generation
tags:
- dllm
- diffusion
- rwkv
- llm
---

# Triplet-Block Diffusion RWKV

This repository contains the checkpoint of **B3D-RWKV**, a 7.2B-parameter RWKV language model presented in the paper [Triplet-Block Diffusion RWKV](https://arxiv.org/abs/2605.25969).

B3D-RWKV is a diffusion RWKV variant that integrates the model's $O(L)$ inference efficiency with parallel, bidirectional discrete-diffusion through a *triplet-block layout* method. It reaches comparable accuracy on an 8-task suite versus existing models while significantly outperforming baselines in decoding throughput with an average of **1.6×** speedup.

- **Paper:** [Triplet-Block Diffusion RWKV](https://arxiv.org/abs/2605.25969)
- **Code:** [GitHub Repository](https://github.com/leonardodalinky/B3D-RWKV)

## Usage

For usage, please see the B3D-RWKV [infer](https://github.com/leonardodalinky/B3D-RWKV/tree/main/infer) and [serve](https://github.com/leonardodalinky/B3D-RWKV/tree/main/infer/serve) directories in the official repository for instructions on how to run inference and serve the model.

Note: This checkpoint is a supervised fine-tuned (SFT) version of `rwkv7-g1f-7.2B`.

## Citation

```bibtex
@misc{lin2026tripletblockdiffusionrwkv,
      title={Triplet-Block Diffusion RWKV}, 
      author={Ke Lin and Yiyang Luo and Zhaolong Su and Yunya Song and Anyi Rao},
      year={2026},
      eprint={2605.25969},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.25969}, 
}
```