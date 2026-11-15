---
license: apache-2.0
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
base_model:
- CohereForAI/aya-expanse-8b
tags:
- gguf
- CohereForAI
- llama-cpp
- Aya-Expanse-8B-GGUF
pipeline_tag: text-generation
---
## AYA Expanse 8B Model Files

| File Name                    | Size    | Description           | Upload Status    |
|------------------------------|---------|-----------------------|------------------|
| `.gitattributes`             | 2.27 kB | Git attributes file   | Uploaded         |
| `README.md`                  | 4.53 kB | Documentation file    | Updated 5 days ago |
| `aya-expanse-8b-q2_k.gguf`   | 3.44 GB | Quantized Q2 model    | Uploaded (LFS)   |
| `aya-expanse-8b-q3_k_l.gguf` | 4.53 GB | Quantized Q3 (large)  | Uploaded (LFS)   |
| `aya-expanse-8b-q3_k_m.gguf` | 4.22 GB | Quantized Q3 (medium) | Uploaded (LFS)   |
| `aya-expanse-8b-q3_k_s.gguf` | 3.87 GB | Quantized Q3 (small)  | Uploaded (LFS)   |
| `aya-expanse-8b-q4_0.gguf`   | 4.8 GB  | Quantized Q4 model    | Uploaded (LFS)   |
| `aya-expanse-8b-q4_k_m.gguf` | 5.06 GB | Quantized Q4 (medium) | Uploaded (LFS)   |
| `aya-expanse-8b-q4_k_s.gguf` | 4.83 GB | Quantized Q4 (small)  | Uploaded (LFS)   |
| `aya-expanse-8b-q5_0.gguf`   | 5.67 GB | Quantized Q5 model    | Uploaded (LFS)   |
| `aya-expanse-8b-q5_k_m.gguf` | 5.8 GB  | Quantized Q5 (medium) | Uploaded (LFS)   |
| `aya-expanse-8b-q5_k_s.gguf` | 5.67 GB | Quantized Q5 (small)  | Uploaded (LFS)   |
| `aya-expanse-8b-q6_k.gguf`   | 6.6 GB  | Quantized Q6 model    | Uploaded (LFS)   |
| `aya-expanse-8b-q8_0.gguf`   | 8.54 GB | Quantized Q8 model    | Uploaded (LFS)   |

# Uploaded  model

- **Developed by:** prithivMLmods
- **License:** apache-2.0
- **Quants from model :** CohereForAI/aya-expanse-8b

Here's a well-structured README.md documentation for running models with Ollama:

# Run with Ollama 🦙

> [!WARNING]
> **Note:**  The model name mentioned in the README.md may or may not be same.

## Overview

Ollama is a powerful tool that allows you to run machine learning models effortlessly. This guide will help you download, install, and run your own GGUF models in just a few minutes.

## Table of Contents

| Section                      | Description                      |
|------------------------------|----------------------------------|
| [Download and Install Ollama](#download-and-install-ollama)       | Instructions for downloading and installing Ollama. |
| [Steps to Run GGUF Models](#steps-to-run-gguf-models)             | Guidelines for running GGUF models. |
| 1. [Create the Model File](#1-create-the-model-file)              | Steps to create the model file. |
| 2. [Add the Template Command](#2-add-the-template-command)        | Instructions for adding the template command. |
| 3. [Create and Patch the Model](#3-create-and-patch-the-model)    | Process for creating and patching the model. |
| [Running the Model](#running-the-model)                           | How to run the model. |
| [Sample Usage](#sample-usage)                                   | Examples of how to use the model. |

## Download and Install Ollama

To get started, download Ollama from [https://ollama.com/download](https://ollama.com/download) and install it on your Windows or Mac system.

## Steps to Run GGUF Models

### 1. Create the Model File
First, create a model file and name it appropriately. For example, you can name your model file `metallama`.

### 2. Add the Template Command
In your model file, include a `FROM` line that specifies the base model file you want to use. For instance:

```bash
FROM Llama-3.2-1B.F16.gguf
```

Ensure that the model file is in the same directory as your script.

### 3. Create and Patch the Model
Open your terminal and run the following command to create and patch your model:

```bash
ollama create metallama -f ./metallama
```

Once the process is successful, you will see a confirmation message.

To verify that the model was created successfully, you can list all models with:

```bash
ollama list
```

Make sure that `metallama` appears in the list of models.

---

## Running the Model

To run your newly created model, use the following command in your terminal:

```bash
ollama run metallama
```

### Sample Usage

In the command prompt, you can execute:

```bash
D:\>ollama run metallama
```

You can interact with the model like this:

```plaintext
>>> write a mini passage about space x
Space X, the private aerospace company founded by Elon Musk, is revolutionizing the field of space exploration.
With its ambitious goals to make humanity a multi-planetary species and establish a sustainable human presence in
the cosmos, Space X has become a leading player in the industry. The company's spacecraft, like the Falcon 9, have
demonstrated remarkable capabilities, allowing for the transport of crews and cargo into space with unprecedented
efficiency. As technology continues to advance, the possibility of establishing permanent colonies on Mars becomes
increasingly feasible, thanks in part to the success of reusable rockets that can launch multiple times without
sustaining significant damage. The journey towards becoming a multi-planetary species is underway, and Space X
plays a pivotal role in pushing the boundaries of human exploration and settlement.
```

---

## Conclusion

With these simple steps, you can easily download, install, and run your own models using Ollama. Whether you're exploring the capabilities of Llama or building your own custom models, Ollama makes it accessible and efficient.


- This README provides clear instructions and structured information to help users navigate the process of using Ollama effectively. Adjust any sections as needed based on your specific requirements or additional details you may want to include.



https://huggingface.co/prithivMLmods/Llama-3.2-1B-GGUF/resolve/main/Demo/gguf.gif