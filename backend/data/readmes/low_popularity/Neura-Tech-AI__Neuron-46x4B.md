---
license: apache-2.0
language:
  - en
  - zh
  - hi
  - ar
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - it
  - ru
  - tr
  - vi
  - th
  - id
  - ms
  - bn
  - ur
  - ta
  - te
  - mr
  - gu
  - pa
  - fa
base_model:
- Neura-Tech-AI/Neuron-4B-Instruct
- Qwen/Qwen3-4B-Instruct-2507
- Qwen/Qwen3-4B-Thinking-2507
new_version: Neura-Tech-AI/Neuron-46x4B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- Neuron-46x4B-Instruct
- Neura Tech AI
---

## Neuron-46x4B-Instruct

«A large-scale, sparse Mixture-of-Experts language model engineered by **Neura Tech AI**, combining 46 specialized experts with efficient sparse activation for high-capacity reasoning and instruction following.»

# Overview

**Neuron-46x4B-Instruct** is a high-capacity instruction-tuned **Mixture-of-Experts (MoE)** language model developed by **Neura Tech AI**.

The model combines **46 specialized experts**, each based on a 4B-scale expert design, resulting in approximately **125B total parameters** while activating only approximately **8B parameters per token** during inference.

This sparse architecture is designed to provide the representational capacity of a much larger model while keeping per-token computation substantially lower than a dense 125B-parameter model.

**Neuron-46x4B-Instruct** is designed for demanding AI workloads including reasoning, coding, multilingual conversations, mathematics, long-context understanding, and agentic applications.

# Model Architecture & Details

- **Model Name:** Neuron-46x4B-Instruct
- **Developer:** Neura Tech AI
- **Architecture:** Sparse Mixture of Experts (MoE)
- **Total Parameters:** ~125B
- **Active Parameters:** ~8B per token
- **Total Experts:** 46
- **Expert Scale:** ~4B parameters per expert
- **Base Model Family:** Qwen3
- **Model Type:** Instruction-Tuned Causal Language Model
- **License:** Apache-2.0
- **Primary Format:** Safetensors

# Why Neuron-46x4B-Instruct?

Neuron-46x4B-Instruct is built around the idea that **model capacity and inference efficiency do not necessarily have to scale together**.

Instead of activating the entire model for every token, the MoE routing mechanism dynamically selects a subset of specialized parameters. This allows Neuron to maintain a very large overall parameter capacity while keeping the number of active parameters significantly lower.

With approximately **125B total parameters and ~8B active parameters**, Neuron-46x4B-Instruct is designed to offer a strong balance between:

- Large model capacity
- Sparse computation
- Expert specialization
- Reasoning capability
- Instruction following
- Multilingual performance
- Efficient inference

# Key Features

# 🧠 Large-Scale Sparse MoE

Neuron-46x4B-Instruct contains **46 specialized experts** within a sparse MoE architecture. The router dynamically determines which experts should process each token.

# ⚡ Efficient Active Computation

Although the model contains approximately **125B total parameters**, only around **8B parameters are active per token**, significantly reducing the computational workload compared with activating the entire parameter set.

# 🔬 Expert Specialization

The large expert pool allows different experts to specialize in different patterns, domains, languages, reasoning behaviors, and instruction types.

# 💻 Coding & Software Engineering

Neuron is designed for programming-related workloads including:

- Code generation
- Debugging
- Code explanation
- Scripting
- Software architecture
- Technical reasoning

# 🧮 Reasoning & Mathematics

The model is intended to handle multi-step analytical tasks, mathematical reasoning, logical problems, and complex instructions.

# 🌍 Multilingual

**Neuron-46x4B-Instruct** supports a broad range of languages, including:

- English
- Chinese
- Hindi
- Arabic
- Japanese
- Korean
- French
- German
- Spanish
- Portuguese
- Italian
- Russian
- Turkish
- Vietnamese
- Thai
- Indonesian
- Malay
- Bengali
- Urdu
- Tamil
- Telugu
- Marathi
- Gujarati
- Punjabi
- Persian
- Etc

# 🤖 Agentic & Tool-Use Workloads

The model can be used as a foundation for AI agents, structured generation, automation systems, tool-calling workflows, and other intelligent applications.

# Model Configuration

| **Property** | **Value** |
| :--- | :--- |
| **Model** | Neuron-46x4B-Instruct |
| **Architecture** | Sparse Mixture of Experts (MoE) |
| **Total Parameters** | ~125B |
| **Active Parameters** | ~8B per token |
| **Total Experts** | 46 |
| **Expert Size** | ~4B |
| **Context Length** | 262,144 Tokens |
| **Model Family** | Qwen3 |
| **Model Type** | Instruction-Tuned Causal Language Model |
| **Task** | Text Generation |
| **Precision** | BF16 |
| **License** | Apache-2.0 |
| **Format** | Safetensors |

# Base Models

**Neuron-46x4B-Instruct** builds upon the Qwen3 model family and incorporates Neura Tech AI's Neuron model work.

# Base Model Acknowledgment

We sincerely thank the **Qwen Team** for developing and openly releasing the Qwen3 model family under the Apache-2.0 license.

We also acknowledge the upstream models and technologies that contributed to the development of the Neuron model family.

# Intended Use

**Neuron-46x4B-Instruct** can be used for:

- Conversational AI
- Coding assistants
- AI agents
- Research
- Education
- Mathematics
- Content generation
- Translation
- Document analysis
- Software engineering
- Multilingual applications
- Experimental MoE research

# Performance

**Neuron-46x4B-Instruct** is designed as a high-capacity sparse model with approximately **125B total parameters and ~8B active parameters per token**.

# Inference

**Neuron-46x4B-Instruct** is intended to be used with frameworks that support its model architecture and sparse Mixture-of-Experts implementation.

For deployment, users should ensure that their inference framework supports the specific architecture and routing configuration used by the model.

# Limitations

Despite its large parameter capacity, **Neuron-46x4B-Instruct** can still produce incorrect, incomplete, or hallucinated information.

Model outputs should be verified before being used in safety-critical, legal, financial, or medical applications.

Performance may also vary significantly depending on the inference framework, hardware, quantization method, prompt format, and deployment configuration.

# Developed by:

**Neura Tech AI**

Neuron is part of Neura Tech AI's ongoing research into efficient large-scale language models and sparse Mixture-of-Experts architectures.

# License

**Neuron-46x4B-Instruct** is released under the **Apache-2.0 License**.

Please review the license terms and the licenses of all upstream components before using the model in your application.

---
Neuron-46x4B-Instruct — Large capacity. Sparse activation. Specialized intelligence.

# © 2026 Neura Tech AI