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

<p align="center">
  [<a href="https://huggingface.co/nc-ai-consortium/VAETKI">🤗 Models</a>] |
  [<a href="https://github.com/wbl-ncai/VAETKI/tree/releases/v1.0.0">💻 Github</a>] |
  [<a href="https://github.com/wbl-ncai/VAETKI/blob/releases/v1.0.0/VAETKI_Technical_Report.pdf">📝 Technical Report</a>]
</p>


## VAETKI 모델 소개

VAETKI는 NC-AI를 중심으로 총 13개 기관이 참여하는 NC-AI 컨소시엄에서 공동 개발한 대규모 언어 모델입니다.
대규모 협력 체계를 기반으로 구축된 VAETKI는 효율성과 확장성을 핵심 목표로 설계되었으며, 이를 위해 Mixture-of-Experts (MoE) 아키텍처를 채택하였습니다.

VAETKI는 연구 및 실서비스 환경 모두를 고려해 설계된 모델로서, 향후 고난도 추론 중심 태스크, 전문 지식 기반 응용, 에이전트형 활용 시나리오 등 다양한 분야에서 활용 가능성을 확장해 나갈 수 있도록 개발되고 있으며, 아래와 같은 주요 특징을 가지고 있습니다:

- **Tool agent**의 경우 **non-thinking mode**로 작동하며, 그 외의 모든 작업은 **thinking mode**로 작동합니다.
- 지시 사항을 정확히 따르도록 설계된 **인간 선호 정렬**을 통해 보다 자연스럽고 일관된 대화를 제공합니다.
- **영어, 한국어, 중국어 및 일본어**로 구성된 지시 이행과 번역을 지원합니다.

## 1. VAETKI Highlights
VAETKI is a large language model developed by the NC-AI consortium, a collaborative initiative led by NC-AI with participation from a total of 13 organizations.
Designed with scalability and efficiency as primary goals, VAETKI adopts a Mixture-of-Experts (MoE) architecture to effectively balance performance and computational cost.

VAETKI is developed with both research and real-world applications in mind.
It is intended to serve as a flexible foundation for a wide range of use cases, including advanced reasoning tasks, domain-specific knowledge applications, and agent-oriented systems, with the following key features:

- **Tool agent** tasks operate in **non-thinking mode**, while all other tasks run in **thinking mode**.
- **Human preference alignment** is designed to ensure accurate instruction following and more natural, consistent conversations.
- **Support of English, Korean, Chinese, and Japanese** for instruction following and translation.

## 2. Model Overview
**VAETKI-100B-A10B** has the following features:

- **Type**: Causal (Auto-regressive) Language Models
- **Architecture**: Transformers, MoE
- **Developed by**: NC-AI consortium
- **Training Stage**: Pre-training & Post-training 
- **Number of Parameters**: 112.2B in total and 10.1B activated
- **Number of Paramaters (Non-Embedding)**: 111.3B
- **Number of Layers**: 48
- **Number of Attention Heads**: 24
- **Number of Experts**: 128
- **Number of Activated Experts**: 8
- **Context Length**: 32k tokens
- **Vocabulary Size**: 126k
- **Languages**: Korean, English, Chinese, and Japanese
- **License**: MIT
- **Related URLs**: https://github.com/wbl-ncai/VAETKI/tree/releases/v1.0.0

For more details, please refer to our [Technical Report](https://github.com/wbl-ncai/VAETKI/blob/releases/v1.0.0/VAETKI_Technical_Report.pdf).

## 3. How to Use
See the [Quickstart](https://github.com/wbl-ncai/VAETKI/tree/releases/v1.0.0?tab=readme-ov-file#quickstart) for more details.

## 4. Training Details
### Training Data
| Dataset | # Tokens |
|---------|---------:|
| [FineWeb-2(kor_Hang)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/viewer/kor_Hang) | 54.5B |
| [FineWeb2-HQ](https://huggingface.co/datasets/epfml/FineWeb2-HQ) | 338.9B |
| [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2-train-smol-ids) | 1.571T |
| [StackExchange_Mar2023](https://huggingface.co/datasets/HuggingFaceGECLM/StackExchange_Mar2023) | 2.6B |
| [finemath(finemath-3plus)](https://huggingface.co/datasets/HuggingFaceTB/finemath/viewer/finemath-3plus) | 37.4B |
| [finemath(infiwebmath-3plus)](https://huggingface.co/datasets/HuggingFaceTB/finemath/viewer/infiwebmath-3plus) | 23.7B |
| [proof-pile-2](https://huggingface.co/datasets/EleutherAI/proof-pile-2) | 28.2B |
| [Nemotron-CC-v2](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2) | 3.360T |
| [Nemotron-CC-Math-v1](https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1) | 214.3B |
| [Nemotron-Pretraining-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1) | 191.4B |
| [Nemotron-Pretraining-SFT-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-SFT-v1) | 367.2B |
| [DCLM-baseline-1.0](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0) | 3.190T |
| [WanJuan-Korean](https://huggingface.co/datasets/opendatalab/WanJuan-Korean) | 68.9B |
| [finemath(finemath-4plus)](https://huggingface.co/datasets/HuggingFaceTB/finemath/viewer/finemath-4plus) | 10.4B |
| [MegaMath](https://huggingface.co/datasets/LLM360/MegaMath) | 208.0B |
| [Stack-Edu](https://huggingface.co/datasets/HuggingFaceTB/stack-edu) | 86.7B |
| [AceReason-1.1-SFT](https://huggingface.co/datasets/nvidia/AceReason-1.1-SFT) | 31.4B |
| [OpenScience-OS-Q2](https://huggingface.co/datasets/nvidia/OpenScience/) | 18.1B |
| [OpenScience-OS-Q3](https://huggingface.co/datasets/nvidia/OpenScience/) | 0.7B |
| [Nemotron-PrisMath](https://huggingface.co/datasets/nvidia/Nemotron-PrismMath) | 6.2B |
| [OpenCodeGeneticInstruct-Qwen2.5-32b-instruct](https://huggingface.co/datasets/nvidia/OpenCodeGeneticInstruct/viewer/qwen2.5-32b-instruct) | 6.8B |
| [OpenCodeGeneticInstruct-mixtral-8x22b-instruct](https://huggingface.co/datasets/nvidia/OpenCodeGeneticInstruct/viewer/mixtral-8x22b-instruct) | 9.0B |
| Total | 9.8T |
* **NIA-Supported Multilingual & Reasoning Datasets**: To enhance multilingual processing and complex reasoning capabilities,
we constructed a large-scale dataset with the support of the **National Information Society Agency (NIA)**.
During the **pre-training phase**, we secured **7.6 billion tokens** by integrating Chinese and Japanese corpora with data specifically tailored for **long-context comprehension**
and **Chain-of-Thought (CoT)** reasoning. In the subsequent **post-training stage**,
we developed an additional 10-billion-token dataset—focusing on specialized **Korean studies** and **mathematical reasoning**—to maximize the model's linguistic nuance
and logical performance, ultimately refining the overall maturity of the foundation model.

### Training Procedure
* Hardware
  * Platform: Naver Cloud MLX Platform
  * GPUs: NVIDIA H100 80GB HBM3 × 1,016
  * Interconnect: InfiniBand 400 Gb/s, 6 lanes (4 lanes were used for RDMA-based inter-node communication)
* Software: The model architecture configuration, training loop, checkpointing, and distributed optimization logic were implemented based on Megatron-Core v0.14, with selective modifications to accommodate experimental requirements. The implementation includes internal modifications to the original frameworks for research and optimization purposes, and this model does not claim full compatibility with original upstream implementations.
* Hyperparameters
| Hyperparameters | Value |
|-----------------|-------|
| Learning rate | 2e-4 → 1e-4 → 8e-5 |
| Batch size | 8M Tokens → 32M Tokens → 46M Tokens |
| Context Length | 4096 → 4096 → 32768 |

## 5. Evaluation Results
We evaluate VAETKI-100B-A10B on various benchmarks and compare it with other models, as shown below.

| Language | Tasks | Benchmark (Metric) | gpt-oss-120b (medium) | VAETKI-100B-A10B |
|----------|-------|--------------------|-----------------------|------------------|
||| Architecture | MoE | MoE |
||| # Total Params | 117B | 112B |
||| # Activated Params | 5.1B | 10B |
| Korean | General | KMMLU-Pro | 61.9 | 58.4 |
|| General | CLIcK | 73.0 | 75.5 |
|| General | KoBALT | 46.0 | 47.5 |
|| Reasoning | HRM8K | 83.3 | 70.6 |
| English | General | MMLU-Pro | 79.1 | 71.0 |
|| Reasoning | GPQA-Diamond | 73.1 | 53.2 |
|| Reasoning | HLE (text only) | 8.6 | 5.9 |
|| Reasoning | IFBench | 63.1 | 52.3 |
|| Reasoning | IFEval | 83.6 | 86.0 |

## 6. Limitations
* **Limitations**:
This model may produce inaccurate or incomplete outputs, including hallucinated content, particularly for ambiguous prompts or tasks requiring high factual accuracy. It may have limitations in complex multi-step reasoning, precise mathematical computation, and strict correctness in code generation. The model does not have the ability to independently verify information.
* **(Potential) Biases**:
The training data may contain social or cultural biases, which can be reflected in the model’s outputs. Despite mitigation efforts, biases related to gender, ethnicity, nationality, or religion may still occur.
* **Out-of-Scope Use**:
This model is not designed for use in safety-critical or regulated domains, such as medical, legal, financial, or military applications. It should not be relied upon for decisions where errors could lead to harm.

## 7. License
This model repository is licensed under the MIT License. The use of VAETKI models is subject to the Model License.
For information on third-party open-source software and data licenses used in this model, please refer to the [NOTICE.md](https://github.com/wbl-ncai/VAETKI/blob/releases/v1.0.0/NOTICE.md) file.

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