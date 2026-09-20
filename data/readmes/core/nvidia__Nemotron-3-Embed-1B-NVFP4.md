---
license: other
license_name: openmdw-1.1
license_link: >-
  https://openmdw.ai/license/1-1/
base_model:
  - nvidia/Nemotron-3-Embed-1B-BF16
tags:
  - text
  - text-embeddings
  - retrieval
  - semantic-search
  - vllm
  - nvfp4
  - rag
language:
  - multilingual
  - en
  - ar
  - as
  - bn
  - bg
  - zh
  - da
  - nl
  - fi
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - ms
  - mr
  - ne
  - "no"
  - fa
  - pt
  - ro
  - ru
  - es
  - sw
  - sv
  - ta
  - te
  - th
  - uk
  - ur
  - vi
library_name: vllm
pipeline_tag: sentence-similarity
---

<div align="center">

**NVIDIA Nemotron 3 Embed**

<a href="https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16">
  <img alt="Nemotron 3 Embed 1B BF16" src="https://img.shields.io/badge/1B-BF16-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
</a>
&nbsp;
<a href="https://huggingface.co/nvidia/Nemotron-3-Embed-1B-NVFP4">
  <img alt="Nemotron 3 Embed 1B NVFP4" src="https://img.shields.io/badge/1B-NVFP4-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
</a>
&nbsp;
<a href="https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16">
  <img alt="Nemotron 3 Embed 8B BF16" src="https://img.shields.io/badge/8B-BF16-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
</a>

</div>

# Model Overview

### Description
**Nemotron-3-Embed-1B-NVFP4** is the quantized version of the [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) model, which is developed for text question-answering retrieval. For more information, please check [here](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16). The **Nemotron-3-Embed-1B-NVFP4** model is quantized with [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer), using nvidia-modelopt v0.45.0.
This model was evaluated on 34 languages: English, Arabic, Assamese, Bengali, Bulgarian, Chinese, Danish, Dutch, Finnish, French, German, Hindi, Hinglish, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Nepali, Norwegian, Persian, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Ukrainian, Urdu, Vietnamese. Read more details in our [Blog Post](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb).

This model is ready for commercial use.

### License/Terms of Use

This model and its associated configuration files are licensed under the [OpenMDW License Agreement, version 1.1 (OpenMDW-1.1)](https://openmdw.ai/license/1-1/). 

ADDITIONAL INFORMATION: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.

### Deployment Geography
Global

### Use Case

The **Nemotron-3-Embed-1B-NVFP4** is most suitable for users who want to build a multilingual question-and-answer application over a large text corpus, leveraging the latest dense retrieval technologies.

Generally [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) and **Nemotron-3-Embed-1B-NVFP4** models share the embedding space and can be used interchangeably, but we recommend validating retrieval quality on a representative sample before switching the models.

### Release Date

07/16/2026 via https://huggingface.co/nvidia/Nemotron-3-Embed-1B-NVFP4

## Model Architecture

- **Architecture Type:** Transformer
- **Network Architecture:** [Ministral-3-3B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512)-based pruned encoder
- **Number of model parameters:** The model has 1.14B parameters
- **Hidden Size:** 2048

The **Nemotron-3-Embed-1B-NVFP4** is the quantized version of the [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), which is a transformer-based text embedding model trained with bidirectional attention masking, where the final embedding vector is obtained by applying average pooling to the transformer’s token-level representations. It encodes each input text into a dense embedding vector of dimension 2048.

## Input(s)

- **Input Type(s):** Text
- **Input Format(s):**
  - Text: List of strings
- **Input Parameters:**
  - Text: One-Dimensional (1D)
- **Other Properties Related to Input:** Text inputs should be tokenized by the model tokenizer. The model’s max sequence length is 32768. Longer inputs should be chunked or truncated.

## Output(s)

- **Output Type(s):** Floats
- **Output Format(s):**
  - List of float arrays
- **Output Parameters:** One-Dimensional (1D) embedding vector per input text string
- **Other Properties Related to Output:** The model outputs a 2048-dimensional embedding vector for each input text string. It also supports dynamic embedding sizes by slicing the vector from the start (for example, keeping the first 1024 or 512 dimensions). These sliced embeddings remain highly functional, provided the resulting sub-vector is re-normalized (L2 normalization) after slicing.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.


## Post-Training Quantization and Quantization-Aware Distillation

This model is a post-training quantized variant of [nvidia/Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16). Quantization was applied to the weights and activations of linear layers only, targeting the **NVFP4** data type for efficient inference. Quantization-Aware Distillation (QAD) was applied primarily to recover accuracy for long input sequences.

## vLLM Usage

This NVFP4 checkpoint is intended for vLLM. The examples below show offline Python use and online serving. Use [nvidia/Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) if you need Transformers or Sentence Transformers.

Use the Hugging Face model ID by default. If you are working from a local checkpoint, replace `MODEL_ID` with that path:

```bash
MODEL_ID=nvidia/Nemotron-3-Embed-1B-NVFP4
```

The output tables use `q[i]` for queries and `d[i]` for documents. Scores are rounded to four decimal places, and runtime differences might affect the final decimal places.

### Tested vLLM Versions

This checkpoint has been explicitly tested with the following vLLM distributions:

| Distribution | Tested version |
| --- | --- |
| Python package | `vllm==0.25.0` |
| Upstream container | `vllm/vllm-openai:v0.22.1`, `vllm/vllm-openai:v0.25.0` |
| NVIDIA container | `nvcr.io/nvidia/vllm:26.06-py3` |

Use vLLM `0.25.0` for the examples below. vLLM `0.23.x` and `0.24.x` have known issues with this NVFP4 checkpoint family. Other versions have not been explicitly validated.

To install vLLM without a container image, run the following command:

```bash
pip install --upgrade "vllm==0.25.0" openai requests numpy
```


### vLLM Offline Python

Use the offline Python API for local vLLM inference without an HTTP server.
`LLM.embed` accepts formatted strings.
Add the `query: ` and `passage: ` prefixes manually.
The example limits input sequences to 4,096 tokens and leaves batch and CUDA graph sizing at the vLLM defaults.

<details>
<summary>vLLM Offline Python Example</summary>

```python
import numpy as np
from vllm import LLM

MODEL_ID = "nvidia/Nemotron-3-Embed-1B-NVFP4"
MAX_MODEL_LEN = 4096

QUERIES = [
    "Write a Python function that counts the frequency of each element in a list of lists.",
    "Write a function that orders a dictionary with tuple keys by the product of each key's tuple values.",
    "What symptoms and common triggers help distinguish eczema from other inflammatory skin conditions?",
    "How can someone reduce exposure to pollen during allergy season?",
]

DOCUMENTS = [
    "def frequency_lists(list1):\n    flattened = [item for sublist in list1 for item in sublist]\n    counts = {}\n    for item in flattened:\n        if item in counts:\n            counts[item] += 1\n        else:\n            counts[item] = 1\n    return counts",
    "def sort_dict_item(test_dict):\n    return {key: test_dict[key] for key in sorted(test_dict.keys(), key=lambda ele: ele[0] * ele[1])}",
    "Eczema commonly causes itchy, dry, inflamed patches of skin. The affected areas may look red, scaly, cracked, or darker than the surrounding skin depending on skin tone. Symptoms can flare after exposure to irritants, allergens, stress, or changes in weather.",
    "People with pollen allergy can reduce exposure by staying indoors on dry, windy days, avoiding early-morning outdoor activity, and going outside after rain when pollen levels are lower. They should check pollen forecasts, close windows and doors when counts are high, and consider starting allergy medication before symptoms begin if high pollen is expected. After being outside, showering, changing clothes, avoiding outdoor laundry drying, and wearing a face mask for yard work can help limit pollen contact.",
]

def main():
    llm = LLM(
        model=MODEL_ID,
        max_model_len=MAX_MODEL_LEN,
    )
    texts = ["query: " + query for query in QUERIES] + [
        "passage: " + doc for doc in DOCUMENTS
    ]
    outputs = llm.embed(texts, use_tqdm=False)
    embeddings = np.array(
        [output.outputs.embedding for output in outputs],
        dtype=np.float32,
    )

    query_embeddings = embeddings[: len(QUERIES)]
    document_embeddings = embeddings[len(QUERIES) :]

    scores = query_embeddings @ document_embeddings.T
    print("Similarity scores:")
    print(f"{'':>8}" + "".join(f"d[{i}]   " for i in range(scores.shape[1])))
    for query_index, row in enumerate(scores):
        print(f"q[{query_index}]   " + "  ".join(f"{score:>7.4f}" for score in row))


if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>vLLM Offline Python Expected Output</summary>

The following output is expected:

```text
Similarity scores:
          d[0]      d[1]      d[2]      d[3]
q[0]    0.8064   0.0201   0.0003  -0.0320
q[1]    0.0445   0.6469  -0.0516   0.0388
q[2]   -0.0083  -0.0402   0.6558   0.1071
q[3]   -0.0222   0.0265   0.1261   0.7677
```

</details>

### vLLM Online Serving

vLLM reads the checkpoint's NVFP4 and pooling metadata, so you do not need to set quantization or runner flags.

Use the following Bash or Zsh command as a starting point on NVIDIA Blackwell GPUs.
Set `VLLM_CACHE_ROOT` to a writable directory that persists across restarts so vLLM can reuse compatible compilation and FP4 GEMM autotuning artifacts:

```bash
export VLLM_CACHE_ROOT=/mnt/vllm-cache
mkdir -p "$VLLM_CACHE_ROOT"

vllm serve nvidia/Nemotron-3-Embed-1B-NVFP4 \
  --cudagraph-capture-sizes \
    1 2 4 {8..248..8} {256..4096..16} \
    {4224..8192..128} {8448..16384..256} \
    {16896..32768..512}
```

The example uses `/mnt/vllm-cache`, but you can use any writable directory that persists across restarts.
For container deployments, mount persistent storage at the directory you choose.
Bash and Zsh expand the capture-size ranges before vLLM starts.
For other launchers, pass the expanded integer list to `--cudagraph-capture-sizes`.

The sparse CUDA graph profile is a practical starting point. Benchmark representative traffic before changing it or increasing `--api-server-count`.
For other cache or tuning configurations, refer to the vLLM [`VLLM_CACHE_ROOT` reference](https://docs.vllm.ai/en/v0.25.0/usage/security/?h=vllm_cache_root#cache-directory-configuration), [`--cudagraph-capture-sizes` reference](https://docs.vllm.ai/en/v0.25.0/configuration/engine_args/#-cudagraph-capture-sizes), and [Parallel Processing guide](https://docs.vllm.ai/en/v0.25.0/configuration/optimization/#parallel-processing).

Expect the first startup to take several minutes while vLLM tunes FP4 GEMMs and captures CUDA graphs.
vLLM recaptures CUDA graphs on every launch.
Startup time varies by hardware and deployment configuration.

Add `--host` or `--port` to the serving command if you need non-default network settings.

To serve a local checkpoint, replace the model ID with its path. Add `--served-model-name nvidia/Nemotron-3-Embed-1B-NVFP4` if clients should continue using the Hugging Face model ID.

#### Recommended Retrieval Endpoint

After the server is running, use `/v2/embed` for retrieval. Send raw query and document strings. `input_type` applies the saved query and document prompt metadata.

The following example uses the recommended endpoint:

```python
import numpy as np
import requests

MODEL = "nvidia/Nemotron-3-Embed-1B-NVFP4"
URL = "http://localhost:8000/v2/embed"

QUERIES = [
    "Write a Python function that counts the frequency of each element in a list of lists.",
    "Write a function that orders a dictionary with tuple keys by the product of each key's tuple values.",
    "What symptoms and common triggers help distinguish eczema from other inflammatory skin conditions?",
    "How can someone reduce exposure to pollen during allergy season?",
]

DOCUMENTS = [
    "def frequency_lists(list1):\n    flattened = [item for sublist in list1 for item in sublist]\n    counts = {}\n    for item in flattened:\n        if item in counts:\n            counts[item] += 1\n        else:\n            counts[item] = 1\n    return counts",
    "def sort_dict_item(test_dict):\n    return {key: test_dict[key] for key in sorted(test_dict.keys(), key=lambda ele: ele[0] * ele[1])}",
    "Eczema commonly causes itchy, dry, inflamed patches of skin. The affected areas may look red, scaly, cracked, or darker than the surrounding skin depending on skin tone. Symptoms can flare after exposure to irritants, allergens, stress, or changes in weather.",
    "People with pollen allergy can reduce exposure by staying indoors on dry, windy days, avoiding early-morning outdoor activity, and going outside after rain when pollen levels are lower. They should check pollen forecasts, close windows and doors when counts are high, and consider starting allergy medication before symptoms begin if high pollen is expected. After being outside, showering, changing clothes, avoiding outdoor laundry drying, and wearing a face mask for yard work can help limit pollen contact.",
]

def embed(input_type: str, texts: list[str]) -> np.ndarray:
    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "input_type": input_type,
            "texts": texts,
            "embedding_types": ["float"],
            "truncate": "END",
        },
        timeout=120,
    )
    response.raise_for_status()
    return np.array(response.json()["embeddings"]["float"], dtype=np.float32)

query_embeddings = embed("query", QUERIES)
document_embeddings = embed("document", DOCUMENTS)

scores = query_embeddings @ document_embeddings.T
print("Similarity scores:")
print(f"{'':>8}" + "".join(f"d[{i}]   " for i in range(scores.shape[1])))
for query_index, row in enumerate(scores):
    print(f"q[{query_index}]   " + "  ".join(f"{score:>7.4f}" for score in row))
```

<details>
<summary>Recommended Retrieval Endpoint Expected Output</summary>

The following output is expected:

```text
Similarity scores:
          d[0]      d[1]      d[2]      d[3]
q[0]    0.8063   0.0201   0.0003  -0.0320
q[1]    0.0445   0.6469  -0.0516   0.0388
q[2]   -0.0082  -0.0402   0.6558   0.1072
q[3]   -0.0222   0.0265   0.1261   0.7677
```

</details>

You can also use the OpenAI-compatible `/v1/embeddings` endpoint. For those requests, pass strings in `input` and manually prefix them with `query: ` or `passage: `.

### Expected Configuration Warning

When vLLM loads this checkpoint, its Transformers configuration parser can emit the following warning.

```text
[transformers] Unrecognized keys in `rope_parameters` for 'rope_type'='yarn': {'apply_yarn_scaling'}
```

This warning is expected and does not prevent vLLM from loading the model or running inference. `apply_yarn_scaling` is a temporary vLLM compatibility field that preserves the checkpoint's intended long-context rotary position embedding (RoPE) behavior. Do not remove it from `config.json`. Refer to [vLLM issue #48621](https://github.com/vllm-project/vllm/issues/48621) for upstream compatibility work.


## Software Integration

- **Runtime Engine(s):** vLLM
- **Supported Hardware Microarchitecture Compatibility:**
  - NVIDIA Ampere
  - NVIDIA Blackwell
  - NVIDIA Hopper
  - NVIDIA Lovelace
- **Supported Operating System(s):**
  - Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s)

**Nemotron-3-Embed-1B-NVFP4**

## Training, Testing, and Evaluation Datasets

### Dataset Overview

This checkpoint is an NVFP4 post-training-quantized derivative of [nvidia/Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16). Quantization-Aware Distillation (QAD) was applied on a small sample of the original BF16 data mix for further accuracy recovery.

### Calibration Dataset

**Data Collection Method by dataset:** Automated

**Labeling Method by dataset:** Automated

**Properties:** A calibration dataset of 512 total samples was used for NVFP4 post-training quantization, consisting of 256 queries and 256 passages from the [abisee/cnn_dailymail](https://huggingface.co/datasets/abisee/cnn_dailymail) dataset, formatted with query and passage prefixes.

### Training Dataset

QAD training was performed as part of the NVFP4 model development. The information below describes the QAD training datasets used for this model. For details about the training datasets used to build the underlying base model, [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), please refer to its model card.

**Total Size:** 20k data samples

**Total Number of Datasets:** 5 dataset files

**Dataset Partition:** Training [100%], Testing [N/A — evaluation benchmarks used separately], Validation [N/A — evaluation benchmarks used separately].

#### Public Datasets:

| Dataset name | Reference |
| --- | --- |
| MLDR | [https://huggingface.co/datasets/Shitao/MLDR](https://huggingface.co/datasets/Shitao/MLDR) |

#### Synthetic Datasets:

Synthetic query-document pairs were generated either from scratch or by using seed datasets to generate queries with the models listed below.

<table>
  <tr>
    <th>LLMs used to generate synthetic datasets</th>
  </tr>
  <tr>
    <td>nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16<br>nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4</td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="2">Seed Datasets</th>
  </tr>
  <tr>
    <th>Dataset</th>
    <th>Reference</th>
  </tr>
  <tr>
    <td>FinePdfs</td>
    <td><a href="https://huggingface.co/datasets/HuggingFaceFW/finepdfs">https://huggingface.co/datasets/HuggingFaceFW/finepdfs</a></td>
  </tr>
</table>



#### Data Modality

- Text

#### Training Data Size

**Text Training Data Size:** 20k

**Data Collection Method by dataset:** Hybrid: Human, Automated, Synthetic

**Labeling Method by dataset:** Hybrid: Human, Automated, Synthetic

**Properties:** Model distillation training of the underlying model was conducted on text datasets using question–passage pairs from publicly available, commercially permissible datasets and synthetically generated datasets. For more information, please visit [this link](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16).

### Testing Dataset

**Data Collection Method by dataset:** Not Applicable

**Labeling Method by dataset:** Not Applicable

**Properties:** Not Applicable. Model quality was assessed using the evaluation benchmark datasets described in the Evaluation Dataset subsection.

### Evaluation Dataset

**Data Collection Method by dataset:** Hybrid: Human, Automated, Synthetic

**Labeling Method by dataset:** Hybrid: Human, Automated, Synthetic

**Properties:** In this section, we compare the performance of quantized model **Nemotron-3-Embed-1B-NVFP4** with baseline implementation **Nemotron-3-Embed-1B-BF16**.

This model is evaluated on 16 public tasks on [Retrieval Embedding Benchmark (RTEB)](https://huggingface.co/blog/rteb), a new benchmark designed to reliably evaluate the retrieval accuracy of embedding models for real-world applications. More details on RTEB can be found on their [leaderboard](https://huggingface.co/spaces/mteb/leaderboard?benchmark_name=RTEB%28beta%29).

We set the model sequence length to 4096 for the evaluation results below. The `NVFP4` model was evaluated on an NVIDIA GB200 GPU.

**Text Retrieval Benchmarks (chunk retrieval) – Avg. NDCG@10**
| Model Name | Precision | RTEB |
| --- | --- | --- |
| Nemotron-3-Embed-1B-BF16 | BF16 | 72.38 |
| Nemotron-3-Embed-1B-NVFP4 | NVFP4 | 72.00 |


## Inference

- **Acceleration Engine:** vLLM
- **Test Hardware:**
  - NVIDIA Ampere - A100 PCIe/SXM
  - NVIDIA Blackwell - GB200 and RTX 6000 PRO
  - NVIDIA Hopper - H100 PCIe/SXM
  - NVIDIA Lovelace - L40 and L4

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing | None |
| Measures taken to mitigate against unwanted bias | None |
| Bias Metric (If Measured): | None |

## Explainability

| Field | Response |
| ----- | ----- |
| Intended Task/Domain: | Passage and query embedding for question and answer retrieval |
| Model Type: | Transformer encoder |
| Intended Users: | Generative AI creators working with conversational AI models - users who want to build a multilingual question and answer application over a large text corpus, leveraging the latest dense retrieval technologies. |
| Output: | Array of float numbers (Dense Vector Representation for the input text) |
| Describe how the model works: | Model transforms the tokenized input text into a dense vector representation. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Technical Limitations & Mitigation: | The model’s max sequence length is 32768. Therefore, the longer text inputs should be truncated. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Throughput, and Latency |
| Potential Known Risks: | This model does not always guarantee to retrieve the correct passage(s) for a given query. |
| Licensing: | This model and its associated configuration files are licensed under the [OpenMDW License Agreement, version 1.1 (OpenMDW-1.1)](https://openmdw.ai/license/1-1/). Additional Information: Built with [Ministral-3-3B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512), which is released under Apache 2.0. |

## Privacy

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | None |
| Was consent obtained for any personal data used? | Not Applicable |
| Personal data used to create this model? | None Known |
| How often is the dataset reviewed? | Before Every Release |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | Not Applicable |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety

| Field | Response |
| ----- | ----- |
| Model Application(s): | Text Embedding for Retrieval |
| Describe the physical safety impact (if present). | Not Applicable |
| Use Case Restrictions: | This model and its associated configuration files are licensed under the [OpenMDW License Agreement, version 1.1 (OpenMDW-1.1)](https://openmdw.ai/license/1-1/). Additional Information: Built with [Ministral-3-3B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512), which is released under Apache 2.0. |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |
