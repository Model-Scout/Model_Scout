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

# Model Card for EuroLLM-22B

This is the model card for EuroLLM-22B. You can also check the post-trained version: [EuroLLM-22B-Instruct-2515](https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512).

- **Developed by:** Instituto Superior Técnico - University of Lisbon, Instituto de Telecomunicações, University of Edinburgh, Aveni, Unbabel, University of Paris-Saclay, Artefact Research Center, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 22B parameter multilingual transfomer LLM.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

## Model Details

The EuroLLM project has the goal of creating a suite of LLMs capable of understanding and generating text in all European Union languages as well as some additional relevant languages.
EuroLLM-22B is a 22B parameter model trained on 4 trillion tokens divided across the considered languages and several data sources: Web data, parallel data (en-xx and xx-en), and high-quality datasets.
EuroLLM-22B-Instruct was further instruction tuned on EuroBlocks, an instruction tuning dataset with focus on general instruction-following and machine translation.

### Architecture

EuroLLM uses a standard, dense Transformer architecture withgrouped query attention (GQA), pre-layer normalization with RMSNorm, SwiGLU activations and rotary positional embeddings (RoPE) in every layer. Here is a summary of the model hyper-parameters:
|                                      |                      |
|--------------------------------------|----------------------|
| Sequence Length                      |      32,768          |
| Number of Layers                     |         56           |
| Embedding Size                       |           6,144      |
| FFN Hidden Size                      |            16,384    |
| Number of Heads                      |        48            |
| Number of KV Heads (GQA)             |         8            |
| Activation Function                  | SwiGLU               |
| Position Encodings                   | RoPE (\Theta=1,000,000) |
| Layer Norm                           | RMSNorm              |
| Tied Embeddings                      | No                   |
| Embedding Parameters                 | 0.786B               |
| LM Head Parameters                   | 0.786B               |
| Non-embedding Parameters             | 21.067B               |
| Total Parameters                     | 22.639B               |

### Pre-training

EuroLLM-22B was trained on approximately 4 trillion tokens, using 400 Nvidia H100 GPUs on the MareNostrum5 supercomputer, thanks to an EuroHPC extreme-scale access grant. The training process was carefully structured into three key phases:

<ol>
<li>Initial Pre-training (3.6 trillion tokens) 
This phase includes the warm-up and constant learning rate stages, during which the model is trained on a mixture of web data alongside higher quality sources such as parallel data, Wikipedia, Arxiv, books, math, code and Apollo datasets. This balanced mix helps the model build a strong multilingual foundation.</li>

<li>Annealing (400 billion tokens) During this phase, there is a linear decay of the learning rate and we adjust the data mix to reduce the proportion of web data while increasing the multilingual content and select the highest quality data—by making use of quality filters such as [CometKiwi-22](https://huggingface.co/Unbabel/wmt22-cometkiwi-da) and [EuroFilter](https://huggingface.co/utter-project/EuroFilter-v1). This shift helps the model refine its understanding across diverse languages and domains.</li>

<li>Annealing to Zero (100 billion tokens) In this final stage, the learning rate decays linearly to zero. In this phase, the data mix was optimized to be of even higher quality, in order to polish the model's performance, and long context data sources were upsampled to increase the model context window to 32k tokens.</li>
</ol>

### Post-training

This model was not post-trained. For an instruction-following version of this model see [EuroLLM-22B-Instruct-2515](https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512).

## Run the model
    
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_id = "utter-project/EuroLLM-22B-2512"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    text = "English: My name is EuroLLM. Portuguese:"

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=20)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

## Bias, Risks, and Limitations

EuroLLM-22B has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).

## Citation
If you use our work, please cite:
```
@misc{ramos2026eurollm22btechnicalreport,
      title={EuroLLM-22B: Technical Report}, 
      author={Miguel Moura Ramos and Duarte M. Alves and Hippolyte Gisserot-Boukhlef and João Alves and Pedro Henrique Martins and Patrick Fernandes and José Pombal and Nuno M. Guerreiro and Ricardo Rei and Nicolas Boizard and Amin Farajian and Mateusz Klimaszewski and José G. C. de Souza and Barry Haddow and François Yvon and Pierre Colombo and Alexandra Birch and André F. T. Martins},
      year={2026},
      eprint={2602.05879},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.05879}, 
}
```