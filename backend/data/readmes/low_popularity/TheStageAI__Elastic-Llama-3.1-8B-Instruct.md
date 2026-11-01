---
license: other
license_name: thestageai-elastic
base_model:
- meta-llama/Llama-3.1-8B-Instruct
base_model_relation: quantized
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
---

# Elastic model: Llama-3.1-8B-Instruct


## Overview

---

ElasticModels are the models produced by TheStage AI ANNA: Automated Neural Networks Accelerator. ANNA allows you to control model size, latency and quality with a simple slider movement, routing different compression algorithms to different layers. For each model, we have produced a series of optimized models:

- **XL**: Mathematically equivalent neural network, optimized with our DNN compiler.
- **L**: Near lossless model, with less than 1% degradation obtained on corresponding benchmarks.
- **M**: Faster model, with accuracy degradation less than 1.5%.
- **S**: The fastest model, with accuracy degradation less than 2%.

Models can be accessed via TheStage AI Python SDK: ElasticModels, or deployed as Docker containers with REST API endpoints (see Deploy section).

## Installation

---

### System Requirements

| **Property**| **Value** |
 | ---  | ---  |
| **GPU** | L40s, RTX 5090, H100, B200 |
| **Python Version** | 3.10-3.12 |
| **CPU** | Intel/AMD x86_64 |
| **CUDA Version** | 12.9+ |


### TheStage AI Access token setup

Install TheStage AI CLI and setup API token:

```bash
pip install thestage
thestage config set --access-token <YOUR_ACCESS_TOKEN>
```

### ElasticModels installation

Install TheStage Elastic Models package:

```bash
pip install 'thestage-elastic-models[nvidia,cudnn]' \
    --extra-index-url https://thestage.jfrog.io/artifactory/api/pypi/pypi-thestage-ai-production/simple
pip install --force-reinstall --no-deps nvidia-cudnn-frontend==1.18.0
```

## Usage example

---

Elastic Models provides the same interface as HuggingFace Transformers. Here is an example of how to use the Llama-3.1-8B-Instruct model:

```python
import torch
from transformers import AutoTokenizer
from elastic_models.transformers import AutoModelForCausalLM

# Currently we require to have your HF token
# as we use original weights for part of layers and
# model configuration as well
model_name = "meta-llama/Llama-3.1-8B-Instruct"
hf_token = ''
device = torch.device("cuda")

# Create mode
tokenizer = AutoTokenizer.from_pretrained(
    model_name, token=hf_token
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token=hf_token,
    torch_dtype=torch.bfloat16,
    attn_implementation="sdpa",
    mode='S'
).to(device)
model.generation_config.pad_token_id = tokenizer.eos_token_id

# Inference simple as transformers library
prompt = "Describe basics of DNNs quantization."
messages = [
  {
    "role": "system",
    "content": "You are a search bot, answer on user text queries."
  },
  {
    "role": "user",
    "content": prompt
  }
]

chat_prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False
)

inputs = tokenizer(chat_prompt, return_tensors="pt")
inputs.to(device)

with torch.inference_mode():
    generate_ids = model.generate(**inputs, max_length=500)

input_len = inputs['input_ids'].shape[1]
generate_ids = generate_ids[:, input_len:]
output = tokenizer.batch_decode(
    generate_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)[0]

# Validate answer
print(f"# Q:\n{prompt}\n")
print(f"# A:\n{output}\n")
```


## Quality Benchmarks

---

We have used the `lm_eval` library to validate the models. For each model size (S, M, L, XL), we have run the following tasks: MMLU, PIQA, Arc Challenge, Winogrande.

![Quality Benchmarking](https://cdn.thestage.ai/production/cms_file_upload/1773422713-7d51617f-e70a-41db-95f9-abd0d9ff338f/Elastic_Llama_3.1_8B_Instruct_MMLU.png)

### Quality Benchmark Results

| **Metric/Model Size**| **S**| **M**| **L**| **XL**| **Original**| **W8A8, int8** |
 | ---  | ---  | ---  | ---  | ---  | ---  | ---  |
| **MMLU** | 67.4 | 68.1 | 68.3 | 68.5 | 68.4 | 24.3 |
| **PIQA** | 79.8 | 80.2 | 80.1 | 79.9 | 80.0 | 64.6 |
| **Arc Challenge** | 55.1 | 54.6 | 54.7 | 55.6 | 55.5 | 29.6 |
| **Winogrande** | 73.7 | 73.6 | 73.7 | 74.0 | 74.0 | 62.8 |


## Datasets

---

- **MMLU**: Measures model performance on a diverse set of multiple-choice questions covering various academic subjects, testing general knowledge and reasoning.
- **PIQA**: Evaluates physical commonsense reasoning by asking the model to choose the most plausible solution to everyday physical problems.
- **Arc Challenge**: Assesses scientific and factual reasoning using challenging multiple-choice questions from the AI2 Reasoning Challenge dataset.
- **Winogrande**: Tests commonsense understanding and pronoun resolution through sentences requiring the model to identify the correct referent.

## Metrics

---

- **Accuracy**: Accuracy measures the proportion of model predictions that exactly match the correct answers across evaluation tasks.


## Latency Benchmarks

---

We measured TPS (tokens per second) for each model size using 100 input tokens and 300 output tokens.

![Latency Benchmarking](https://cdn.thestage.ai/production/cms_file_upload/1779128494-03458602-0144-446d-bebd-6d3ebc8b9907/Elastic_Llama_3.1_8B_Instruct_latency.png)

### Latency Benchmark Results

Tokens per second for different model sizes on various GPUs.

| **GPU/Model Size**| **S**| **M**| **L**| **XL**| **Original**| **W8A8_int8** |
 | ---  | ---  | ---  | ---  | ---  | ---  | ---  |
| **H100** | 204 | 182 | 168 | 143 | 60 | 191 |
| **L40s** | 73 | 64 | 57 | 46 | 37 | 77 |
| **B200** | 276 | 270 | 264 | 249 | 100 | N/A |
| **GeForce RTX 5090** | 153 | N/A | N/A | N/A | 60 | N/A |
| **GeForce RTX 4090** | 95 | N/A | N/A | N/A | 41 | N/A |


## Benchmarking Methodology

---

The benchmarking was performed on a single GPU with a batch size of 1. Each model was run for 10 iterations, and the average latency was calculated.

> **Algorithm summary:**
> 1. Load the Llama-3.1-8B-Instruct model with the specified size (S, M, L, XL, original).
> 2. Move the model to the GPU.
> 3. Prepare a sample prompt for text generation.
> 4. Run the model for a number of iterations (e.g., 10) and measure the time taken for each iteration. On each iteration:
>    - Synchronize the GPU to flush any previous operations.
>    - Record the start time.
>    - Generate the text using the model.
>    - Synchronize the GPU again.
>    - Record the end time and calculate the TTFT and TPS for that iteration.
> 5. Calculate the average TTFT and TPS over all iterations.


## Serving with Docker Image

---

For serving with Nvidia GPUs, we provide ready-to-go Docker containers with OpenAI-compatible API endpoints.
Using our containers you can set up an inference endpoint on any desired cloud/serverless providers as well as on-premise servers.
You can also use this container to run inference through TheStage AI platform.

### Prebuilt image from ECR

Pull docker image and start inference container:

```bash
docker pull public.ecr.aws/i3f7g5s7/thestage/elastic-models:0.2.1.post0-llm-24.09a
```
```bash
docker run --rm -ti \
  --name serving_thestage_model \
  -p 8000:80 \
  -e AUTH_TOKEN=<AUTH_TOKEN> \
  -e MODEL_REPO=meta-llama/Llama-3.1-8B-Instruct \
  -e MODEL_SIZE=<MODEL_SIZE> \
  -e MODEL_BATCH=<MAX_BATCH_SIZE> \
  -e HUGGINGFACE_ACCESS_TOKEN=<HUGGINGFACE_ACCESS_TOKEN> \
  -e THESTAGE_AUTH_TOKEN=<THESTAGE_ACCESS_TOKEN> \
  -v /mnt/hf_cache:/root/.cache/huggingface \
  public.ecr.aws/i3f7g5s7/thestage/elastic-models:0.2.1.post0-llm-24.09a
```

| **Parameter**              | **Description**                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------|
| `<MODEL_SIZE>`             | Available: S, M, L, XL.                                                                              |
| `<MAX_BATCH_SIZE>`         | Maximum batch size to process in parallel.                                                           |
| `<HUGGINGFACE_ACCESS_TOKEN>` | Hugging Face access token.                                                                         |
| `<THESTAGE_ACCESS_TOKEN>`  | TheStage token generated on the platform (Profile -> Access tokens).                                 |
| `<AUTH_TOKEN>`             | Token for endpoint authentication. You can set it to any random string; it must match the value used by the client. |

## Invocation

---

You can invoke the endpoint using CURL as follows:

```bash
curl -X POST 'http://127.0.0.1:8000/v1/chat/completions' \
    -H 'Authorization: Bearer 123' \
    -H 'Content-Type: application/json' \
    -H "X-Model-Name: llama-3-1-8b-instruct-<MODEL_SIZE>-bs<MAX_BATCH_SIZE>-paged" \
    -d '{
        "messages":[{"role":"user","content":"Define AI"}]
    }'
```

Or using OpenAI python client:

```python
import os, base64, pathlib, json
from openai import OpenAI

BASE_URL = "http://<your_ip>/v1"
API_KEY  = "123"
MODEL    = "llama-3-1-8b-instruct-<MODEL_SIZE>-bs<MAX_BATCH_SIZE>-paged"

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    default_headers={"X-Model-Name": MODEL}
)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Define AI"}
    ]
)

print(response.choices[0].message.content)
```

## Endpoint Parameters

---

### Method

> **POST** `/v1/chat/completions`

### Header Parameters

> `Authorization`: `string`
>
> Bearer token for authentication. Should match the `AUTH_TOKEN` set during container startup.

> `Content-Type`: `string`
>
> Must be set to `application/json`.

> `X-Model-Name`: `string`
>
> Specifies the model to use for generation. Format: `llama-3-1-8b-instruct-<size>-bs<batch_size>`, where `<size>` is one of `S`, `M`, `L`, `XL`, `original` and `<batch_size>` is the maximum batch size configured during container startup.

### Input Body

> `messages` : `string`
>
> The input text prompt.


## Deploy on Modal

---

For more details please use the tutorial [Modal deployment](https://docs.thestage.ai/tutorials/source/modal_thestage.html)

### Clone modal serving code

```shell
git clone https://github.com/TheStageAI/ElasticModels.git
cd ElasticModels/examples/modal
```

### Configuration of environment variables

Set your environment variables in `modal_serving.py`:

```python
# modal_serving.py

ENVS = {
    "MODEL_REPO": "meta-llama/Llama-3.1-8B-Instruct",
    "MODEL_BATCH": "4",
    "THESTAGE_AUTH_TOKEN": "",
    "HUGGINGFACE_ACCESS_TOKEN": "",
    "PORT": "80",
    "PORT_HEALTH": "80",
    "HF_HOME": "/cache/huggingface",
}
```

### Configuration of GPUs

Set your desired GPU type and autoscaling variables in `modal_serving.py`:

```python
# modal_serving.py

@app.function(
    image=image,
    gpu="B200",
    min_containers=8,
    max_containers=8,
    timeout=10000,
    ephemeral_disk=600 * 1024,
    volumes={"/opt/project/.cache": HF_CACHE},
    startup_timeout=60*20
)
@modal.web_server(
    80,
    label="meta-llama/Llama-3.1-8B-Instruct-test",
    startup_timeout=60*20
)
def serve():
    pass
```

### Run serving

```shell
modal serve modal_serving.py
```


## Links

---

* __Platform__: [app.thestage.ai](https://app.thestage.ai)
* __Subscribe for updates__: [TheStageAI X](https://x.com/TheStageAI)
* __Contact email__: contact@thestage.ai
