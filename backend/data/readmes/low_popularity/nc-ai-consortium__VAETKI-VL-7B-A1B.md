---
license: mit
pipeline_tag: image-text-to-text
tags:
- VAETKI
- causal-lm
- VAETKI-VL-7B-A1B
- multimodal
language:
- ko
- en
base_model:
- nc-ai-consortium/VAETKI-7B-A1B
- DeepGlint-AI/rice-vit-large-patch14-560
datasets:
- HuggingFaceM4/FineVision
- lmms-lab/LLaVA-OneVision-Data
- lmms-lab/M4-Instruct-Data
- lmms-lab/LLaVA-OneVision-Mid-Data
- liuhaotian/LLaVA-Pretrain
---


## 1. VAETKI-VL-7B-A1B Highlights
VAETKI-VL-7B-A1B is a vision-language model developed by the NC-AI, designed especially for inference efficienty.
VAETKI series adopt a Mixture-of-Experts (MoE) architecture to effectively balance performance and computational cost.

## 2. Model Overview
**VAETKI-VL-7B-A1B** has the following features:

- **Type**: Causal (Auto-regressive) Vision Language Models
- **Architecture**: LLM(VAETKI-VL-7B-A1B) + RICE-ViT + FFN
- **Developed by**: NC-AI consortium (with ETRI, Korea University)
- **Training Stage**: Stage 1(Projector alignment), Stage 2(Basic SFT), Stage 3(Advanced SFT)
- **Number of Parameters**: 7.58B (LLM: 7.25B in total and 1.2B activated, ViT: 0.33B)
- **Number of Paramaters (Non-Embedding)**: 6.8B
- **Number of Layers**: 24
- **Number of Attention Heads**: 12
- **Number of Experts**: 64
- **Number of Activated Experts**: 5
- **Context Length**: 16k tokens
- **Vocabulary Size**: 126k
- **Languages**: Korean, English
- **License**: MIT
- **Related URLs**: https://github.com/wbl-ncai/VAETKI/

## 3. How to Use
See the [Quickstart](https://github.com/wbl-ncai/VAETKI/blob/main/inference_vaetki_vl_7b_a1b.py) for more details.

## 4. Training Details
### Training Data
This model was trained on a curated collection of multimodal instruction-tuning datasets. We utilized subsets from the following open-source datasets, applying custom preprocessing and format conversion to align with our training objectives:

- **[HuggingFaceM4/FineVision](https://huggingface.co/datasets/HuggingFaceM4/FineVision)**
- **[lmms-lab/LLaVA-OneVision-Data](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data)**
- **[lmms-lab/M4-Instruct-Data](https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data)**
- **[lmms-lab/LLaVA-OneVision-Mid-Data](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Mid-Data)**
- **[liuhaotian/LLaVA-Pretrain](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain)**

The data was filtered and reformatted to ensure high-quality visual instruction alignment.

### Training Procedure
* Hardware
  * Platform: Naver Cloud MLX Platform
  * GPUs: NVIDIA H100 80GB HBM3 × 64
  * Interconnect: InfiniBand 400 Gb/s, 6 lanes (4 lanes were used for RDMA-based inter-node communication)
* Software: The model architecture configuration, training loop, checkpointing, and distributed optimization logic were implemented based on Megatron-Core v0.14, with selective modifications to accommodate experimental requirements. The implementation includes internal modifications to the original frameworks for research and optimization purposes, and this model does not claim full compatibility with original upstream implementations.
* Hyperparameters
| Hyperparameters | Value |
|-----------------|-------|
| Learning rate | 5e-5 → 5e-6 → 3e-6 |
| Learning rate for ViT | null →  1e-6 → 1e-6 |
| weight_decay | 0.01 |
| Context Length | 4096 → 16384 → 16384 |

## 5. Evaluation Results
**- to be updated**


## 6. Limitations
* **Limitations**:
This model may produce inaccurate or incomplete outputs, including hallucinated content, particularly for ambiguous prompts or tasks requiring high factual accuracy. It may have limitations in complex multi-step reasoning, precise mathematical computation, and strict correctness in code generation. The model does not have the ability to independently verify information.
* **(Potential) Biases**:
The training data may contain social or cultural biases, which can be reflected in the model’s outputs. Despite mitigation efforts, biases related to gender, ethnicity, nationality, or religion may still occur.
* **Out-of-Scope Use**:
This model is not designed for use in safety-critical or regulated domains, such as medical, legal, financial, or military applications. It should not be relied upon for decisions where errors could lead to harm.

## 7. License
This model repository is licensed under the MIT License. The use of VAETKI models is subject to the Model License.
For information on third-party open-source software and data licenses used in this model, please refer to the [NOTICE.md](https://github.com/wbl-ncai/VAETKI/blob/main/NOTICE.md) file.

## 8. Citation
```
@misc{ncai2025vaetkitechnicalreport,
      title={VAETKI Technical Report}, 
      author={NC-AI Consortium},
      year={2025},
      howpublished={\url{https://github.com/wbl-ncai/VAETKI/raw/releases/v1.0.0/VAETKI_Technical_Report.pdf}},
      note={Version 1.0.0}
}
```

## 9. Contact
If you are interested to leave a message or have any questions, please contact us at wbl.ncai.hf@gmail.com.