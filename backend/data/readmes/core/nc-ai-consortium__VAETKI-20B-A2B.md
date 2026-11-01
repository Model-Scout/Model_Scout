---
license: mit
pipeline_tag: text-generation
tags:
- VAETKI
- causal-lm
language:
- ko
- en
- zh
- ja
---


## 1. VAETKI-20B-A2B Highlights
VAETKI-20B-A2B is a (small) language model developed by the NC-AI, designed especially for inference efficienty.
VAETKI series adopt a Mixture-of-Experts (MoE) architecture to effectively balance performance and computational cost.

## 2. Model Overview
**VAETKI-20B-A2B** has the following features:

- **Type**: Causal (Auto-regressive) Language Models
- **Architecture**: Transformers, MoE (Mixture of Experts)
- **Developed by**: NC-AI
- **Training Stage**: Pretraining & Post-training 
- **Number of Parameters**: 19.64B in total and 2.2B activated
- **Number of Paramaters (Non-Embedding)**: 19.1B
- **Number of Layers**: 24
- **Number of Attention Heads**: 16
- **Number of Experts**: 128
- **Number of Activated Experts**: 8
- **Context Length**: 16k tokens
- **Vocabulary Size**: 126k
- **Languages**: Korean, English, Chinese, and Japanese
- **License**: MIT
- **Related URLs**: https://github.com/wbl-ncai/VAETKI/

For more details, please refer to our [Technical Report](https://github.com/wbl-ncai/VAETKI/blob/main/VAETKI_Technical_Report.pdf).

## 3. How to Use
See the [Quickstart](https://github.com/wbl-ncai/VAETKI/tree/main?tab=readme-ov-file#quickstart) for more details.

## 4. Training Details
### Training Data
Due to training time and resource constraints, only **3.62 trillion tokens** from [the available data sources](https://huggingface.co/nc-ai-consortium/VAETKI#training-data) were used for pre-training.

### Training Procedure
* Hardware
  * Platform: Naver Cloud MLX Platform
  * GPUs: NVIDIA H100 80GB HBM3 × 256
* Software: The model architecture configuration, training loop, checkpointing, and distributed optimization logic were implemented based on Megatron-Core v0.14, with selective modifications to accommodate experimental requirements.
* Hyperparameters
| Hyperparameters | Value |
|---------------|-------|
| Learning rate | 2e-4 → 1e-5 |
| Batch size | 8.1M → 32.4M Tokens |
| Context Length | 4096 → 16384 |

## 5. Evaluation Results
We evaluate VAETKI-20B-A2B on various benchmarks and compare it with a series of models, as shown in the following. All models were evaluated under the same experimental setup to ensure a fair and consistent comparison.

**to be updated**

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
