---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
library_name: transformers
---

# Model Card for EuroLLM-9B


This is the model card for EuroLLM-9B. You can also check the instruction tuned version: [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct).

- **Developed by:** Unbabel, Instituto Superior Técnico, Instituto de Telecomunicações, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 9B parameter multilingual transfomer LLM.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

## Model Details

The EuroLLM project has the goal of creating a suite of LLMs capable of understanding and generating text in all European Union languages as well as some additional relevant languages.
EuroLLM-9B is a 9B parameter model trained on 4 trillion tokens divided across the considered languages and several data sources: Web data, parallel data (en-xx and xx-en), and high-quality datasets.
EuroLLM-9B-Instruct was further instruction tuned on EuroBlocks, an instruction tuning dataset with focus on general instruction-following and machine translation.


### Model Description

EuroLLM uses a standard, dense Transformer architecture:
- We use grouped query attention (GQA) with 8 key-value heads, since it has been shown to increase speed at inference time while maintaining downstream performance.
- We perform pre-layer normalization, since it improves the training stability, and use the RMSNorm, which is faster.
- We use the SwiGLU activation function, since it has been shown to lead to good results on downstream tasks.
- We use rotary positional embeddings (RoPE) in every layer, since these have been shown to lead to good performances while allowing the extension of the context length.

For pre-training, we use 400 Nvidia H100 GPUs of the Marenostrum 5 supercomputer, training the model with a constant batch size of 2,800 sequences, which corresponds to approximately 12 million tokens, using the Adam optimizer, and BF16 precision.
Here is a summary of the model hyper-parameters:
|                                      |                      |
|--------------------------------------|----------------------|
| Sequence Length                      |      4,096           |
| Number of Layers                     |         42           |
| Embedding Size                       |           4,096      |
| FFN Hidden Size                      |            12,288    |
| Number of Heads                      |        32            |
| Number of KV Heads (GQA)             |         8            |
| Activation Function                  | SwiGLU               |
| Position Encodings                   | RoPE (\Theta=10,000) |
| Layer Norm                           | RMSNorm              |
| Tied Embeddings                      | No                   |
| Embedding Parameters                 | 0.524B               |
| LM Head Parameters                   | 0.524B               |
| Non-embedding Parameters             | 8.105B               |
| Total Parameters                     | 9.154B               |

## Run the model
    
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    model_id = "utter-project/EuroLLM-9B"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    
    text = "English: My name is EuroLLM. Portuguese:"
    
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=20)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))


## Results

### EU Languages


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f33ecc0be81bdc5d903466/ob_1sLM8c7dxuwpv6AAHA.png)
**Table 1:** Comparison of open-weight LLMs on multilingual benchmarks. The borda count corresponds to the average ranking of the models (see  ([Colombo et al., 2022](https://arxiv.org/abs/2202.03799))). For Arc-challenge, Hellaswag, and MMLU we are using Okapi datasets ([Lai et al., 2023](https://aclanthology.org/2023.emnlp-demo.28/)) which include 11 languages. For MMLU-Pro and MUSR we translate the English version with Tower ([Alves et al., 2024](https://arxiv.org/abs/2402.17733)) to 6 EU languages.  
\* As there are no public versions of the pre-trained models, we evaluated them using the post-trained versions.

The results in Table 1 highlight EuroLLM-9B's superior performance on multilingual tasks compared to other European-developed models (as shown by the Borda count of 1.0), as well as its strong competitiveness with non-European models, achieving results comparable to Gemma-2-9B and outperforming the rest on most benchmarks.

### English


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f33ecc0be81bdc5d903466/EfilsW_p-JA13mV2ilPkm.png)

**Table 2:** Comparison of open-weight LLMs on English general benchmarks.    
\*  As there are no public versions of the pre-trained models, we evaluated them using the post-trained versions.

The results in Table 2 demonstrate EuroLLM's strong performance on English tasks, surpassing most European-developed models and matching the performance of Mistral-7B (obtaining the same Borda count).


## Bias, Risks, and Limitations

EuroLLM-9B has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).
