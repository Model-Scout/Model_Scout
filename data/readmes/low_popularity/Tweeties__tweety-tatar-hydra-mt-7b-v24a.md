---
base_model: Unbabel/TowerInstruct-7B-v0.1
license: cc-by-nc-4.0
language:
- tt
- en
- de
- fr
- zh
- pt
- nl
- ru
- ko
- it
- es
tags:
- tweety
datasets:
- oscar-corpus/OSCAR-2301
---

<img align="right" src="https://huggingface.co/Tweeties/tweety-tatar-base-7b-2024-v1/resolve/main/TweetyTatar.png?download=true" alt="Tweety-Tatar-7B: A Tatar Large Language Model" width="20%">

# Tweety Tatar / Hydra-MT 7b / 2024-v1

## Model description
This model is our Hydra LLM for the [Tatar language](https://en.wikipedia.org/wiki/Tatar_language), converted from the [TowerInstruct-7b-v0.1](https://huggingface.co/Unbabel/TowerInstruct-7B-v0.1) model trained by Unbabel, via [our Hydra-Base model](https://huggingface.co/Tweeties/tweety-tatar-hydra-base-7b-2024-v1). 
Hydra LLMs are trans-tokenized language models finetuned to produce output in a particular language, while accepting input encoded using either their own tokenizer, the one of their base model, or a mix of both. 
This enables them to receive code-switched input in both their native language and other languages, which is an ideal setup for translation tasks, or retrieval-augmented generation (RAG) in cross-lingual scenarios (see [our Hydra-Base model](https://huggingface.co/Tweeties/tweety-tatar-hydra-base-7b-2024-v1)).

- **Developed by:** [François Remy](https://huggingface.co/FremyCompany) (UGent), [Alfiya Khabibullina](https://huggingface.co/justalphie) (BeCode), [et al.](#citation)
- **Funded by:** IDLab / GPULab
- **Model type:** Foundation model using the mistral architecture
- **Language(s) (NLP):** Tatar
- **License:** Creative Commons Attribution Non Commercial 4.0

## In-scope usage
This model can be used as-is or finetuned into a machine translation system from one of the 10 languages supported by TowerInstruct into the Tatar language. 
This list of languages nobably includes English and Russian. 
The model performs best when translating sentences or small paragraphs, and is not suited for document translation tasks. 
This model should not be used in the reverse direction, to translate Tatar into English. 
While the system is finetuned for translation, enabling beam search provides better results. 
Take note of the non-commercial license imposed by Unbabel on the base model, which also applies to this model.

## Usage instructions
Using this model usually requires building the prompts by mixing tokens from two tokenizers, the original TowerInstruct tokenizer for input in the source language, and the new Tatar tokenizer for the prompt and output, as described in the examples below:

```py
import re
import torch
import torch.nn as nn
import transformers

MODEL_NAME = "Tweeties/tweety-tatar-hydra-mt-7b-2024-v1"
MAIN_TOKENIZER_NAME = "Tweeties/tweety-tatar-hydra-mt-7b-2024-v1"
UTIL_TOKENIZER_NAME = "Unbabel/TowerInstruct-7B-v0.1"

model = transformers.AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
main_tokenizer = transformers.LlamaTokenizerFast.from_pretrained(MAIN_TOKENIZER_NAME)
util_tokenizer = transformers.LlamaTokenizerFast.from_pretrained(UTIL_TOKENIZER_NAME)

main_tokenizer_len = len(main_tokenizer)
```

### Machine Translation

```py
def translate_english_text(english_text: str) -> str:
    
    # craft the input
    input_ids = torch.concat([
        main_tokenizer.encode(f"Түбәндәге текстны инглиз теленнән татар теленә тәрҗемә итегез:\n", return_tensors='pt'),
        util_tokenizer.encode(f"{english_text}", add_special_tokens=False, return_tensors='pt') + torch.tensor([main_tokenizer_len]),
        main_tokenizer.encode(f"\nТекстны татар теленә тәрҗемә итү:\n", add_special_tokens=False, return_tensors='pt')
    ], axis=1)

    # prevent the model from repeating the prompt
    prompt_starts = [
        main_tokenizer.encode("Түбәндәге"), 
        main_tokenizer.encode("\nТүбәндәге")[2:], 
        main_tokenizer.encode("Текстны"), 
        main_tokenizer.encode("\nТекстны")[2:]
    ]
   
    # genereate the output
    model_inputs = {'input_ids':input_ids.to(model.device)}
    model_outputs = model.generate(
        **model_inputs,
        max_new_tokens=128,
        num_beams=8,
        no_repeat_ngram_size=6,
        early_stopping=False,
        pad_token_id=main_tokenizer.eos_token_id,
        eos_token_id=main_tokenizer.convert_tokens_to_ids(['<0x0A>','</s>']),
        bad_words_ids=prompt_starts
    )

    # decode the output
    return (main_tokenizer.decode(model_outputs[0][input_ids.shape[1]:]))

translate_english_text("The city of Paris is very pretty.") # Париж шәһәре бик матур.
```


## Citation

If you use this model, please cite our work as:

```
@article{tweeties2024,
    title = {Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP},
    author = {François Remy and Pieter Delobelle and Hayastan Avetisyan and Alfiya Khabibullina and Miryam de Lhoneux and Thomas Demeester},
    url = {https://arxiv.org/abs/2408.04303},
    year = {2024},
    note = {Accepted at COLM 2024}
}
```