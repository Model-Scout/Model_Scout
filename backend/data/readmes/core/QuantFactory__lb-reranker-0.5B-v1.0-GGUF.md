
---

library_name: transformers
license: apache-2.0
language:
- en
- zh
- es
- de
- ar
- ru
- ja
- ko
- hi
- sk
- vi
- tr
- fi
- id
- fa
- 'no'
- th
- sv
- pt
- da
- bn
- te
- ro
- it
- fr
- nl
- sw
- pl
- hu
- cs
- el
- uk
- mr
- ta
- tl
- bg
- lt
- ur
- he
- gu
- kn
- am
- kk
- hr
- uz
- jv
- ca
- az
- ms
- sr
- sl
- yo
- lv
- is
- ha
- ka
- et
- bs
- hy
- ml
- pa
- mt
- km
- sq
- or
- as
- my
- mn
- af
- be
- ga
- mk
- cy
- gl
- ceb
- la
- yi
- lb
- tg
- gd
- ne
- ps
- eu
- ky
- ku
- si
- ht
- eo
- lo
- fy
- sd
- mg
- so
- ckb
- su
- nn
datasets:
- lightblue/reranker_continuous_filt_max7_train
base_model:
- Qwen/Qwen2.5-0.5B-Instruct
pipeline_tag: text-generation
tags:
- reranker

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/lb-reranker-0.5B-v1.0-GGUF
This is quantized version of [lightblue/lb-reranker-0.5B-v1.0](https://huggingface.co/lightblue/lb-reranker-0.5B-v1.0) created using llama.cpp

# Original Model Card


# LB Reranker v1.0

<div style="width: 100%; height: 160px; 
            display: flex; align-items: center; 
            justify-content: center; 
            border: 8px solid black; 
            font-size: 120px; font-weight: bold; 
            text-align: center;
            color: #438db8; 
            font-family: 'Helvetica Neue', sans-serif;">
  LBR
</div>

The LB Reranker has been trained to determine the relatedness of a given query to a piece of text, therefore allowing it to be used as a ranker or reranker in various retrieval-based tasks.

This model is fine-tuned from a [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) model checkpoint and was trained for roughly 5.5 hours using the 8 x L20 instance ([ecs.gn8is-8x.32xlarge](https://www.alibabacloud.com/help/en/ecs/user-guide/gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1)) on [Alibaba Cloud](https://www.alibabacloud.com/).

The training data for this model can be found at [lightblue/reranker_continuous_filt_max7_train](https://huggingface.co/datasets/lightblue/reranker_continuous_filt_max7_train) and the code for generating this data as well as running the training of the model can be found on [our Github repo](https://github.com/lightblue-tech/lb-reranker).

Trained on data in over 95 languages, this model is applicable to a broad range of use cases.

This model has three main benefits over comparable rerankers.
1. It has shown slightly higher performance on evaluation benchmarks.
2. It has been trained on more languages than any previous model.
3. It is a simple Causal LM model trained to output a string between "1" and "7".

This last point means that this model can be used natively with many widely available inference packages, including vLLM and LMDeploy.
This in turns allows our reranker to benefit from improvements to inference as and when these packages release them.

Update: We have also found that this model works pretty well as a code snippet reranker too (P@1 of 96%)! See our [Colab](https://colab.research.google.com/drive/1ABL1xaarekLIlVJKbniYhXgYu6ZNwfBm?usp=sharing) for more details.

# How to use

The model was trained to expect an input such as:

```
<<<Query>>>
{your_query_here}

<<<Context>>>
{your_context_here}
```

And to output a string of a number between 1-7.

In order to make a continuous score that can be used for reranking query-context pairs (i.e. a method with few ties), we calculate the expectation value of the scores.

We include scripts to do this in both vLLM and LMDeploy:

#### vLLM

Install [vLLM](https://github.com/vllm-project/vllm/) using `pip install vllm`.

```python
from vllm import LLM, SamplingParams
import numpy as np

def make_reranker_input(t, q):
    return f"<<<Query>>>\n{q}\n\n<<<Context>>>\n{t}"

def make_reranker_training_datum(context, question):
    system_message = "Given a query and a piece of text, output a score of 1-7 based on how related the query is to the text. 1 means least related and 7 is most related."

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": make_reranker_input(context, question)},
    ]

def get_prob(logprob_dict, tok_id):
    return np.exp(logprob_dict[tok_id].logprob) if tok_id in logprob_dict.keys() else 0

llm = LLM("lightblue/lb-reranker-v1.0")
sampling_params = SamplingParams(temperature=0.0, logprobs=14, max_tokens=1)
tok = llm.llm_engine.tokenizer.tokenizer
idx_tokens = [tok.encode(str(i))[0] for i in range(1, 8)]

query_texts = [
    ("What is the scientific name of apples?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
    ("What is the Chinese word for 'apple'?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
    ("What is the square root of 999?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
]

chats = [make_reranker_training_datum(c, q) for q, c in query_texts]
responses = llm.chat(chats, sampling_params)
probs = np.array([[get_prob(r.outputs[0].logprobs[0], y) for y in idx_tokens] for r in responses])

N = probs.shape[1]
M = probs.shape[0]
idxs = np.tile(np.arange(1, N + 1), M).reshape(M, N)

expected_vals = (probs * idxs).sum(axis=1)
print(expected_vals)
# [6.66570732 1.86686378 1.01102923]
```

#### LMDeploy

Install [LMDeploy](https://github.com/InternLM/lmdeploy) using `pip install lmdeploy`.

```python
# Un-comment this if running in a Jupyter notebook, Colab etc.
# import nest_asyncio
# nest_asyncio.apply()

from lmdeploy import GenerationConfig, ChatTemplateConfig, pipeline
import numpy as np

def make_reranker_input(t, q):
    return f"<<<Query>>>\n{q}\n\n<<<Context>>>\n{t}"

def make_reranker_training_datum(context, question):
    system_message = "Given a query and a piece of text, output a score of 1-7 based on how related the query is to the text. 1 means least related and 7 is most related."

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": make_reranker_input(context, question)},
    ]

def get_prob(logprob_dict, tok_id):
    return np.exp(logprob_dict[tok_id]) if tok_id in logprob_dict.keys() else 0

pipe = pipeline(
    "lightblue/lb-reranker-v1.0",
    chat_template_config=ChatTemplateConfig(
                    model_name='qwen2d5',
                    capability='chat'
    )
)
tok = pipe.tokenizer.model
idx_tokens = [tok.encode(str(i))[0] for i in range(1, 8)]

query_texts = [
    ("What is the scientific name of apples?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
    ("What is the Chinese word for 'apple'?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
    ("What is the square root of 999?", "An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica)."),
]

chats = [make_reranker_training_datum(c, q) for q, c in query_texts]
responses = pipe(
    chats, 
    gen_config=GenerationConfig(temperature=1.0, logprobs=14, max_new_tokens=1, do_sample=True)
)
probs = np.array([[get_prob(r.logprobs[0], y) for y in idx_tokens] for r in responses])

N = probs.shape[1]
M = probs.shape[0]
idxs = np.tile(np.arange(1, N + 1), M).reshape(M, N)

expected_vals = (probs * idxs).sum(axis=1)
print(expected_vals)
# [6.66415229 1.84342025 1.01133205]
```

# Evaluation

We perform an evaluation on 9 datasets from the [BEIR benchmark](https://github.com/beir-cellar/beir) that none of the evaluated models have been trained upon (to our knowledge).

* Arguana
* Dbpedia-entity
* Fiqa
* NFcorpus
* Scidocs
* Scifact
* Trec-covid-v2
* Vihealthqa
* Webis-touche2020

We evaluate on a subset of all queries (the first 250) to save evaluation time.

We find that our model performs similarly or better than many of the state-of-the-art reranker models in our evaluation, without compromising on inference speed.

We make our evaluation code and results available [on our Github](https://github.com/lightblue-tech/lb-reranker/blob/main/run_bier.ipynb).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/xkNzCABFUmU7UmDXUduiz.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/P-XCA3TGHqDSX8k6c4hCE.png)

As we can see, this reranker attains greater IR evaluation metrics compared to the two benchmarks we include for all positions apart from @1.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/puhhWseBOcIyOEdW4L-B0.png)

We also show that our model is, on average, faster than the BGE reranker v2.

# License

We share this model under an Apache 2.0 license.

# Developed by

<a href="https://www.lightblue-tech.com">
<img src="https://www.lightblue-tech.com/wp-content/uploads/2023/08/color_%E6%A8%AA%E5%9E%8B-1536x469.png" alt="Lightblue technology logo" width="400"/>
</a>

This model was trained by Peter Devine ([ptrdvn](https://huggingface.co/ptrdvn)) for Lightblue
