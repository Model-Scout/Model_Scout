---
language:
- en
- de
- es
- ko
- tr
- it
datasets:
- uonlp/CulturaX
- togethercomputer/RedPajama-Data-V2
---

<div align="center" style="border-radius: 8px; overflow: hidden;">
  <img src="DynamoGuard_Banner.png" alt="DynamoFL | Secure & Compliant AI for the Enterprise" style="border-radius: 8px;">
</div>

# Dynamo 8B Model Card

Dynamo 8B is an improvement of the Mistral 7B architecture for the purpose of multilingual language modeling. Dynamo 8B outperforms Mistral 7B, Llama2 13B, Bloom 7B, and PolyLM 13B on most multilingual benchmarks we tested (i.e. PAWS and XCOPA). For additional details, please refer to our [blog post](https://www.dynamofl.com/blogs/introducing-dynamo-8b-a-multilingual-foundation-model-for-global-enterprises).

It includes an extended tokenizer that was pretrained to better leverage tokens in different languages. The tokenizer was extended by training a sentence BPE tokenizer on selected languages (200M tokens were used per language) and then combined the merges/vocab that were not already present in the Mistral tokenizer. After the tokenizers were merged, the model was pretrained with an additional 210B tokens from multilingual data like German, Spanish, Korean, Italian, and Turkish texts. The pretraining dataset also incorporated English tokens to mitigate catastrophic forgetting.  

Dynamo 8B has not been instruction fine-tuned and has not undergone alignment using techniques like reinforcement learning from human feedback. The intention behind crafting this model is to provide the research community with a model to explore vital multilingual capabilities that enable widespread use of LLMs globally. 


# Model Specifications: 

- Supported Languages: English, German, Spanish, Korean, Italian, Turkish. 

- Context Window: 128K tokens* 

- License: At the moment, Dynamo 8B is released under a [DynamoFL research-only license](https://huggingface.co/dynamofl/dynamoLLM-8.27B/blob/main/custom-license 'DynamoFL Research License'). 

*Pretraining on the multilingual dataset was done with a sequence length of 4096 tokens 

# Evaluation Results:

In our recent evaluation, we used several multilingual benchmarks to assess our model's capabilities. These benchmarks included PAWS, XCOPA, and xstorycloze, all part of EleutherAI's evaluation harness. All runs were done in 32bit precision. Here is an in-depth description of each benchmark we used:

| Multilingual Benchmark | Language | Dynamo 8B | Mistral 7B | Llama2 13B | Bloom 7B | PolyLM 13B |
|------------------------|----------|-----------|------------|------------|----------|------------|
| PAWS                   | German   | **0.516**     | 0.363      | 0.377      | 0.502    | 0.390      |
| PAWS                   | English  | **0.497**     | 0.311      | 0.336      | 0.422    | 0.413      |
| PAWS                   | Spanish  | **0.515**     | 0.339      | 0.422      | 0.424    | 0.452      |
| PAWS                   | Korean   | **0.552**     | 0.422      | 0.534      | **0.551**    | 0.544      |
| XCOPA                  | Italian  | **0.710**     | 0.63       | 0.692      | 0.516    | 0.644      |
| XCOPA                  | Turkish  | **0.672**     | 0.562      | 0.550      | 0.520    | 0.574      |
| xstorycloze            | Spanish  | **0.645**     | 0.632      | 0.622      | 0.639    | **0.642**      |

# Training Data:

This model was trained on a variety of datasets including information from an mC4 database which is made available under the ODC Attribution License. This includes the CulturaX dataset and RedPajama. 

# Notice
Dynamo 8B is a pre-trained model that can be adapted and fine-tuned for a variety of tasks. However, it is new technology that carries risk. In some scenarios, it may generate inaccurate, unverified, or biased output despite efforts we have made to maximize model safety. As with all LLMs, we recommend users exercise critical thinking, validate outputs, and perform the requisite safety evaluations for specific downstream applications of the Dynamo model. We also require any use or deployment of the model to be in adherence with our Acceptable Use Policy.(https://www.dynamofl.com/legal/acceptable-use-policy)