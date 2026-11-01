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
base_model:
- utter-project/EuroMoE-2.6B-A0.6B-2512
---

# Model Card for EuroMoE-2.6B-A0.6B-Instruct-2512

This is the model card for EuroMoE-2.6B-A0.6B-Instruct-2512. You can also check the pre-trained version: [EuroMoE-2.6B-A0.6B-2512](https://huggingface.co/utter-project/EuroMoE-2.6B-A0.6B-2512).

- **Developed by:** Instituto Superior Técnico - University of Lisbon, Instituto de Telecomunicações, University of Edinburgh, Aveni, Unbabel, University of Paris-Saclay, Artefact Research Center, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 2.6B parameter multilingual transformer MoE with 0.6B active parameters.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

## Model Details

The EuroLLM project has the goal of creating a suite of LLMs capable of understanding and generating text in all European Union languages as well as some additional relevant languages.
EuroMoE-2.6B-A0.6B is a 2.6B parameter model trained on 8 trillion tokens divided across the considered languages and several data sources: Web data, parallel data (en-xx and xx-en), and high-quality datasets.
EuroMoE-2.6B-A0.6B-Instruct was further instruction tuned on EuroBlocks, an instruction tuning dataset with focus on general instruction-following and machine translation.


### Model Description

EuroMoE uses a standard MoE Transformer architecture:
- We use grouped query attention (GQA) with 2 key-value heads, since it has been shown to increase speed at inference time while maintaining downstream performance.
- We perform pre-layer normalization, since it improves the training stability, and use the RMSNorm, which is faster.
- We use the SwiGLU activation function, since it has been shown to lead to good results on downstream tasks.
- We use rotary positional embeddings (RoPE) in every layer, since these have been shown to lead to good performances while allowing the extension of the context length.

For pre-training, we use 512 Nvidia A100 GPUs of the Leonardo supercomputer, training the model with a constant batch size of 4096 sequences, which corresponds to approximately 17 million tokens, using the Adam optimizer, and BF16 precision.
Here is a summary of the model hyper-parameters:
|                                      |                      |
|--------------------------------------|----------------------|
| Sequence Length                      |      4,096           |
| Number of Layers                     |         24           |
| Embedding Size                       |           1,024      |
| Total/Active experts                  |      64/8      |
| Expert Hidden Size                   |            512      |
| Number of Heads                      |        8            |
| Number of KV Heads (GQA)             |         2            |
| Activation Function                  | SwiGLU               |
| Position Encodings                   | RoPE (\Theta=500,000) |
| Layer Norm                           | RMSNorm              |
| Tied Embeddings                      | Yes                  |
| Embedding Parameters                 | 0.13B               |
| LM Head Parameters                   | 0.13B               |
| Active Non-embedding Parameters             | 0.34B               |
| Total Non-embedding Parameters             | 2.35B               |
| Active Parameters                   | 0.6B               |
| Total Parameters                     | 2.61B               |

## Run the model
    
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    model_id = "utter-project/EuroMoE-2.6B-A0.6B-Instruct-2512"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    messages = [
        {
            "role": "system",
            "content": "You are EuroLLM --- an AI assistant specialized in European languages that provides safe, educational and helpful answers.",
        },
        {
            "role": "user", "content": "What is the capital of Portugal? How would you describe it?"
        },
        ]

    inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    outputs = model.generate(inputs, max_new_tokens=1024)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))


## Bias, Risks, and Limitations

EuroMoE-2.6B-A0.6B-Instruct-2512 has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).