---
language:
- 'no'
- nb
- nn
inference: true
tags:
- mistral
- gpt
- generative
license: apache-2.0
pipeline_tag: text-generation
datasets:
- uonlp/CulturaX
- NbAiLab/NCC
- vikp/starcoder_filtered
---

# **NorMistral-7b-warm**

<img align="center" src="https://huggingface.co/ltg/norbert3-base/resolve/main/norbert.png" width=12.5%>

NorMistral-7b-warm is a large Norwegian language model initialized from [Mistral-7b-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) and 
continuously pretrained on a total of 260 billion subword tokens (using six repetitions of open Norwegian texts).

This model is a part of the NORA.LLM family developed in collaboration between [the Language Technology Group at the University of Oslo](https://huggingface.co/ltg), [the High Performance Language Technologies (HPLT) project](https://hplt-project.org/), [the National Library of Norway](https://huggingface.co/NbAiLab), and [the University of Turku](https://huggingface.co/TurkuNLP).
All the models are pre-trained on the same dataset and with the same tokenizer.
NorMistral-7b-warm has over 7 billion parameters and is based on [the Mistral architecture](https://huggingface.co/mistralai/Mistral-7B-v0.1).

The NORA.LLM language model family includes (as of now):
- [**NorMistral-7b-warm**](https://huggingface.co/norallm/normistral-7b-warm) -- an LLM initialized from [Mistral-7b-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) and continuously pretrained on Norwegian data;
- [**NorMistral-7b-scratch**](https://huggingface.co/norallm/normistral-7b-scratch) -- a Mistral-based LLM pretrained from scratch on Norwegian data;
- [**NorBLOOM-7b-scratch**](https://huggingface.co/norallm/NorBLOOM-7b-scratch) -- a BLOOM-based LLM pretrained from scratch on Norwegian data.


*Disclaimer: This model is pretrained on raw (mostly web-based) textual data.
It is not finetuned to follow instructions, and it can generate harmful completions after inappropriate user prompts.
It is primarily intended for research purposes.*

_____
## Pretraining corpus

The model is continually pretrained exclusively on publicly available data. We combine the resources from [the public part of the NCC corpus](https://huggingface.co/datasets/NbAiLab/NCC), from [the cleaned HPLT corpus](https://hplt-project.org/datasets/v1.2), and from [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX).
This resulted in over 34B subword tokens of Norwegian (Bokmål or Nynorsk) in total, which amounts to about 26.7B whitespace-separated tokens.
We also augment the corpus with [Starcoder](https://huggingface.co/datasets/vikp/starcoder_filtered); 20% of the 260B tokens are sampled from this code corpus.
The natural language data is repeated six times to get the pretraining budget of 260B tokens, in accordance with findings from [Muennighoff et al. (2023)](https://neurips.cc/virtual/2023/poster/70706).

_____
## Model details

**Model Developers:** Language Technology Group at the University of Oslo.

**Variations:** NorMistral is currently published as two 7B variants: one trained entirely from *scratch* and one *warm*-started from the Mistral model.

**Input:** Textual input.

**Output:** Generated text.

**Model Architecture:** NorMistral is an auto-regressive language model that uses an optimized transformer architecture based on the Mistral/Llama language models.

||Training Data|Params|Context Length|Tokens|LR|
|---|---|---|---|---|---|
|NorMistral-7b-warm|NCC+HPLT+CulturaX+Starcoder|7B|2k|260B|1.0 x 10<sup>-4</sup>|
|NorMistral-7b-scratch|NCC+HPLT+CulturaX+Starcoder|7B|2k|260B|3.0 x 10<sup>-4</sup>|
|NorBLOOM-7b-scratch|NCC+HPLT+CulturaX+Starcoder|7B|2k|260B|1.2 x 10<sup>-4</sup>|

**Tokenizer:** Byte-based BPE tokenizer trained on the same Norwegian corpus as this model. The vocabulary size is 32,768 tokens.

**Training FLOPs** The approximate amount is 1.22e+22 FLOPs; calculated as in [Chowdhery et al. (2022)](https://arxiv.org/abs/2204.02311).

**Model Dates:** The models were pretrained between December 2023 and January 2024.

**Status:** These are only pretrained language models; instruction-finetuned models will follow soon.

**License:** [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

**Research Paper:** Forthcoming

_____
## Initial evaluation

*Disclaimer: our model evaluation is an ongoing phase and is not claimed to be exhaustive. We provide our initial evaluation results on standard natural language understanding and generation tasks, and our evaluation design will be extended. 
The user should perform evaluation for their particular model application scenario, including safety and bias evaluations.*

The perplexity on the heldout [validation set from the Norwegian Colossal Corpus (NCC)](https://huggingface.co/datasets/NbAiLab/NCC) is 7.43 and the final training perplexity is 4.76.

Our initial downstream evaluation is conducted on reading comprehension, sentiment analysis and machine translation tasks using open-source peer-reviewed datasets and benchmarks in native Norwegian.
We release [our codebase here](https://github.com/ltgoslo/norallm). We compare against other pretrained generative language models that officially support Norwegian: [NB-GPT-J](https://huggingface.co/NbAiLab/nb-gpt-j-6B), [GPT-Sw3 6.7B](https://huggingface.co/AI-Sweden-Models/gpt-sw3-6.7b), [GPT-Sw3 6.7B v2](https://huggingface.co/AI-Sweden-Models/gpt-sw3-6.7b-v2), and [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b); we also include evaluation of [Mistral-7b-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1).


### Sentiment analysis

[NoReC](https://huggingface.co/datasets/ltg/norec_sentence) ([Øvrelid et al., 2020](https://aclanthology.org/2020.lrec-1.618/)) is a dataset for sentence-level sentiment analysis derived from the Norwegian Review Corpus [(Velldal et al., 2018)](https://aclanthology.org/L18-1661/).
We use the binary formulation of this task (positive vs. negative).

<details>
<summary>Method (click to expand)</summary>
  
* Evaluation setting: zero-shot and few-shot perplexity-based evaluation.
* Prompt: ```"Tekst: {text}\nSentiment:{label}"```, where the ```label``` is either "positiv" or "negativ".
* Few-shot results show the average scores across 5 repetitions
* Evaluation script: https://github.com/ltgoslo/norallm/blob/main/initial_evaluation/sentiment_analysis.py
* Performance metric: macro-averaged F1-score.

</details>

<details open>
<summary>Macro-averaged F1-scores on the sentence-level sentiment analysis task (NoReC)</summary>

|Model|0-shot (macro F1)|1-shot (macro F1)|16-shot (macro F1)|
|---|---|---|---|
|NorMistral-7b-warm|60.6|**77.8**|**87.3**|
|NorMistral-7b-scratch|47.3|62.2|80.1|
|NorBLOOM-7b|**75.7**|73.8|65.5|
|NB-GPT-J|48.4|56.5|65.2|
|GPT-Sw3-6.7B|61.5|72.2|76.5|
|GPT-Sw3-6.7B-v2|42.4|69.1|83.4|
|Falcon-7B|53.3|61.6|74.9|
|Mistral-7B-v0.1|70.2|72.9|84.8|

</details>



### Reading comprehension

[NorQuAD](https://huggingface.co/datasets/ltg/norquad) ([Ivanova et al., 2023](https://aclanthology.org/2023.nodalida-1.17/)) is a dataset for extractive question answering in Norwegian designed similarly to [SQuAD (Rajpurkar et al., 2016)](https://aclanthology.org/D16-1264/).

<details>
<summary>Method (click to expand)</summary>
  
* Evaluation setting: zero-shot and few-shot settings via natural language generation using the greedy decoding strategy.
* Prompt: ```"Tittel: {title}\n\nTekst: {text}\n\nSpørsmål: {question}\n\nSvar:{answer}"``` Based on [Brown et al. (2020)](https://arxiv.org/abs/2005.14165).
* Few-shot results show the average scores across 5 repetitions
* Evaluation script: https://github.com/ltgoslo/norallm/blob/main/initial_evaluation/norquad.py
* Performance metrics: macro-averaged F1-score and exact match (EM).
  
</details>

<details open>
<summary>Performance results on the extractive question answering task (NorQuAD)</summary>

|Model|0-shot (F1/EM)|1-shot (F1/EM)|2-shot (F1/EM)|
|---|---|---|---|
|NorMistral-7b-warm|**48.6**/**24.8**|63.6/40.0|66.5/43.8|
|NorMistral-7b-scratch|34.0/15.7|46.5/25.8|48.5/27.8|
|NorBLOOM-7b|35.0/13.3|47.7/28.0|49.3/30.1|
|NB-GPT-J|24.4/6.8|32.8/11.6|35.0/12.3|
|GPT-Sw3-6.7B|46.5/22.0|55.9/32.0|58.1/34.3|
|GPT-Sw3-6.7B-v2|46.9/22.5|61.1/38.9|66.0/44.5|
|Falcon-7B|15.8/7.0|27.3/13.9|27.4/13.1|
|Mistral-7B-v0.1|46.4/22.4|**64.9**/**41.1**|**71.7**/**49.4**|

</details>


### Grammatical error correction

[ASK-RAW](https://huggingface.co/datasets/ltg/ask-gec) is dataset for Norwegian grammatical error correction (GEC) created by [Matias Jentoft (2023)](https://www.duo.uio.no/handle/10852/103885).

<details>
<summary>Method (click to expand)</summary>
  
* Evaluation setting: zero-shot and few-shot settings via natural language generation using the greedy decoding strategy.
* Prompt: ```"Her er eksempler på perfekt korrigering av grammatiske feil:\n\nTekst: {source_text}\nKorreksjon:{target_text}"```
* Few-shot results show the average scores across 5 repetitions
* Evaluation script: https://github.com/ltgoslo/norallm/blob/main/initial_evaluation/gec.py
* Performance metrics: the evaluation metric uses [ERRANT](https://github.com/chrisjbryant/errant/tree/main), which identifies edit-spans and then calculates the F_{0.5} scores between the gold edits and predicted edits. 
  
</details>

<details open>
<summary>Results on [the ASK corpus](https://huggingface.co/datasets/ltg/ask-gec) (ERRANT F_{0.5})</summary>

|Model|0-shot (F0.5)|1-shot (F0.5)|32-shot (F0.5)|
|---|---|---|---|
|NorMistral-7b-warm|**40.8**|41.8|48.5|
|NorMistral-7b-scratch|22.1|28.8|42.1|
|NorBLOOM-7b|8.7|24.5|32.0|
|NB-GPT-J|9.1|28.2|30.6|
|GPT-Sw3-6.7B|30.5|42.9|**50.6**|
|GPT-Sw3-6.7B-v2|40.6|**43.4**|49.8|
|Falcon-7B|10.8|12.4|15.5|
|Mistral-7B-v0.1|26.0|27.4|30.6|

</details>


### Machine translation

[Tatoeba](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt) [(Tiedemann, 2020)](https://aclanthology.org/2020.wmt-1.139/) is a benchmark for machine translation, which includes hundreds of language pairs. We consider six language pairs (English <-> Bokmål, English <-> Nynorsk, and Bokmål <-> Nynorsk).

<details>
<summary>Method (click to expand)</summary>
  
* Evaluation setting: zero-shot and few-shot settings via natural language generation using the greedy decoding strategy.
* Prompt: ```"{source_language}: {source_text}\n{target_language}:{target_text}"```, where the ```source_language``` and ```target_language``` are ```Engelsk```, ```Bokmål```, or ```Nynorsk```. Based on [Garcia et al. (2023)](https://arxiv.org/abs/2302.01398).
* Few-shot results show the average scores across 5 repetitions
* Evaluation script: https://github.com/ltgoslo/norallm/blob/main/initial_evaluation/machine_translation.py
* Performance metrics: BLEU ([Papineni et al., 2002](https://aclanthology.org/P02-1040/)) and chrF++ ([Popović, 2015](https://aclanthology.org/W15-3049/)).

</details>

<details open>
<summary>English → Norwegian Bokmål</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**55.8**/**70.7**|**56.7**/**71.5**|57.7/72.4|
|NorMistral-7b-scratch|46.4/62.9|50.4/66.3|52.1/67.6|
|NorBLOOM-7b|37.1/53.6|50.1/65.8|52.0/67.6|
|NB-GPT-J|8.6/39.1|35.9/64.5|47.2/68.7|
|GPT-Sw3-6.7B|21.8/55.2|54.5/69.6|**58.6**/**73.2**|
|GPT-Sw3-6.7B-v2|20.6/53.2|51.2/66.6|58.4/73.0|
|Falcon-7B|19.1/40.1|20.6/41.8|22.1/43.6|
|Mistral-7B-v0.1|32.5/51.9|35.4/55.1|36.3/56.0|


</details>

<details open>
<summary>English → Norwegian Nynorsk</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**43.6**/**62.0**|**44.2**/**63.2**|44.3/**63.7**|
|NorMistral-7b-scratch|38.0/56.9|39.2/57.9|40.7/59.3|
|NorBLOOM-7b|35.6/54.7|36.6/56.3|38.1/57.4|
|NB-GPT-J|1.7/14.7|6.3/34.1|35.2/60.4|
|GPT-Sw3-6.7B|13.4/44.3|43.6/62.5|**44.5**/63.5|
|GPT-Sw3-6.7B-v2|14.8/45.5|43.7/62.3|44.0/63.6|
|Falcon-7B|6.4/28.6|8.3/30.5|9.3/32.1|
|Mistral-7B-v0.1|11.6/35.7|13.5/38.7|15.0/40.0|


</details>


<details open>
<summary>Norwegian Bokmål → English</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**56.7**/**70.6**|**57.7**/**71.7**|**58.5**/**72.2**|
|NorMistral-7b-scratch|48.1/62.9|51.5/66.6|52.6/67.6|
|NorBLOOM-7b|46.0/61.5|51.3/66.7|51.7/66.9|
|NB-GPT-J|23.9/55.3|32.3/63.1|48.5/68.7|
|GPT-Sw3-6.7B|47.9/67.8|52.4/70.6|50.0/70.7|
|GPT-Sw3-6.7B-v2|38.8/59.6|49.0/68.6|50.7/70.6|
|Falcon-7B|42.4/58.5|47.3/62.3|48.6/63.3|
|Mistral-7B-v0.1|53.8/68.2|54.6/69.0|56.9/70.7|

</details>

<details open>
<summary>Norwegian Nynorsk → English</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**55.1**/**68.4**|**55.5**/**69.5**|56.0/69.8|
|NorMistral-7b-scratch|47.1/61.9|49.4/64.2|52.3/66.2|
|NorBLOOM-7b|45.0/59.3|48.3/64.0|49.0/64.7|
|NB-GPT-J|2.9/19.5|10.1/41.0|44.4/66.9|
|GPT-Sw3-6.7B|47.8/66.2|49.1/68.1|49.6/69.4|
|GPT-Sw3-6.7B-v2|46.3/67.5|48.9/69.3|**58.2**/**72.8**|
|Falcon-7B|21.6/40.6|31.7/47.4|36.6/57.1|
|Mistral-7B-v0.1|40.7/57.1|46.2/60.7|49.9/63.8|

</details>


<details open>
<summary>Norwegian Bokmål → Norwegian Nynorsk</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**75.8**/**87.5**|74.0/**86.9**|75.3/87.5|
|NorMistral-7b-scratch|38.0/56.9|39.2/57.9|40.7/59.3|
|NorBLOOM-7b|71.5/84.4|70.1/84.1|71.9/85.1|
|NB-GPT-J|6.6/35.5|9.6/41.0|26.0/64.7|
|GPT-Sw3-6.7B|63.6/82.8|74.7/86.0|75.8/86.9|
|GPT-Sw3-6.7B-v2|57.5/81.1|**75.3**/86.7|**76.7**/**87.6**|
|Falcon-7B|28.7/59.2|29.8/60.8|32.1/62.3|
|Mistral-7B-v0.1|32.0/62.2|32.9/62.6|35.2/63.9|


</details>

<details open>
<summary>Norwegian Nynorsk → Norwegian Bokmål</summary>

|Model|0-shot (BLEU/chrF++)|1-shot (BLEU/chrF++)|5-shot (BLEU/chrF++)|
|---|---|---|---|
|NorMistral-7b-warm|**88.1**/**93.6**|**89.2**/**94.3**|**89.3**/**94.6**|
|NorMistral-7b-scratch|85.1/91.4|86.6/92.4|87.4/93.0|
|NorBLOOM-7b|78.7/88.5|84.2/90.7|87.4/93.0|
|NB-GPT-J|2.7/18.5|6.9/35.6|52.9/84.3|
|GPT-Sw3-6.7B|652.3/82.4|86.1/92.5|87.8/93.6|
|GPT-Sw3-6.7B-v2|72.0/88.6|86.1/92.5|88.2/93.9|
|Falcon-7B|36.7/61.6|38.3/63.5|45.8/68.1|
|Mistral-7B-v0.1|57.0/74.8|59.9/77.5|62.6/79.1|

</details>



_____
## Hardware and Software

**Training Factors:** The models were pretrained using the Megatron-DeepSpeed library on [the LUMI cluster in Finland](https://lumi-supercomputer.eu/).

**Carbon Footprint:** Pretraining one model took approximately 70k GPU hours of computation on AMD MI250X GPUs (assuming 2 GPUs per one AMD MI250X device), each of which draws 500W.
LUMI is [one of the most eco-efficient data centers in the world](https://www.lumi-supercomputer.eu/sustainable-future/), and its energy consumption is covered 100% with renewable electricity.



_____
## Example usage

Let's try to use this model for English-to-Norwegian machine translation using simple zero-shot prompting:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# First, we will have to import the tokenizer and the language model
tokenizer = AutoTokenizer.from_pretrained("norallm/normistral-7b-warm")
model = AutoModelForCausalLM.from_pretrained("norallm/normistral-7b-warm").cuda().eval()

# Now we will define the zero-shot prompt template
prompt = """Engelsk: {0}
Bokmål:"""

# A function that will take care of generating the output
@torch.no_grad()
def generate(text):
    text = prompt.format(text)
    input_ids = tokenizer(text, return_tensors='pt').input_ids.cuda()
    prediction = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=False,
        eos_token_id=tokenizer('\n').input_ids
    )
    return tokenizer.decode(prediction[0, input_ids.size(1):]).strip()

# Now you can simply call the generate function with an English text you want to translate:
generate("I'm super excited about this Norwegian NORA model! Can it translate these sentences?")
# > this should output: 'Jeg er super spent på denne norske NORA modellen! Kan den oversette disse setningene?'
```

## Example usage on a GPU with ~16GB VRAM (try for yourself [in Google Colab](https://colab.research.google.com/drive/1AQgJ8lN-SNOqkUKj4xpQI5rr0R7V2Xzy?usp=sharing))
Install bitsandbytes if you want to load in 8bit

```bash
pip install bitsandbytes
pip install accelerate
```


```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
    "norallm/normistral-7b-warm"
)

# This setup needs about 8gb VRAM
# Setting `load_in_8bit=False` -> 15gb VRAM
# Using `torch.float32` and `load_in_8bit=False` -> 21gb VRAM
model = AutoModelForCausalLM.from_pretrained(
    "norallm/normistral-7b-warm",
    device_map='auto',
    load_in_8bit=True,
    torch_dtype=torch.bfloat16
)
```

_____
## Quantization

### Provided files

| Name | Quant method | Bits Per Weight | Size | Max RAM/VRAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [normistral-7b-warm-Q3_K_M.gguf](https://huggingface.co/norallm/normistral-7b-warm/blob/main/normistral-7b-warm-Q3_K_M.gguf) | Q3_K_M | 3.89 | 3.28 GB| 5.37 GB | very small, high loss of quality |
| [normistral-7b-warm-Q4_K_M.gguf](https://huggingface.co/norallm/normistral-7b-warm/blob/main/normistral-7b-warm-Q4_K_M.gguf) | Q4_K_M | 4.83 | 4.07 GB| 6.16 GB | medium, balanced quality |
| [normistral-7b-warm-Q5_K_M.gguf](https://huggingface.co/norallm/normistral-7b-warm/blob/main/normistral-7b-warm-Q5_K_M.gguf) | Q5_K_M | 5.67 | 4.78 GB| 6.87 GB | large, very low quality loss |
| [normistral-7b-warm-Q6_K.gguf](https://huggingface.co/norallm/normistral-7b-warm/blob/main/normistral-7b-warm-Q6_K.gguf) | Q6_K | 6.56 | 5.54 GB| 7.63 GB | very large, extremely low quality loss |
| [normistral-7b-warm-Q8_0.gguf](https://huggingface.co/norallm/normistral-7b-warm/blob/main/normistral-7b-warm-Q8_0.gguf) | Q8_0 | 8.50 | 7.17 GB| 9.26 GB | very large, extremely low quality loss |

### How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for example.

#### How to load this model in Python code, using llama-cpp-python

For full documentation, please see: [llama-cpp-python docs](https://llama-cpp-python.readthedocs.io/en/latest/).

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base llama-ccp-python with no GPU acceleration
pip install llama-cpp-python
# With NVidia CUDA acceleration
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Or with OpenBLAS acceleration
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
# Or with CLBLast acceleration
CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
# Or with AMD ROCm GPU acceleration (Linux only)
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
# Or with Metal GPU acceleration for macOS systems only
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format; eg for NVidia CUDA:
$env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
pip install llama-cpp-python
```

#### Simple llama-cpp-python example code

```python
from llama_cpp import Llama

# Directly from huggingface-hub (requires huggingface-hub to be installed)
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama.from_pretrained(
  repo_id="norallm/normistral-7b-warm",  # HuggingFace repository containing the GGUF files.
  filename="*Q4_K_M.gguf", # suffix of the filename containing the level of quantization. 
  n_ctx=32768,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "Engelsk: Hello everyone! I'm a language model, how are you doing today?\nBokmål:", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token
  echo=True,       # Whether to echo the prompt
  temperature=0.3  # Temperature to set, for Q3_K_M, Q4_K_M, Q5_K_M, and Q6_0 it is recommended to set it relatively low.
)
```

### Citation

```bibtex
@inproceedings{samuel-etal-2025-small,
    title = "Small Languages, Big Models: {A} Study of Continual Training on Languages of {Norway}",
    author = "Samuel, David  and
      Mikhailov, Vladislav  and
      Velldal, Erik  and
      {\O}vrelid, Lilja  and
      Charpentier, Lucas Georges Gabriel  and
      Kutuzov, Andrey  and
      Oepen, Stephan",
    editor = "Johansson, Richard  and
      Stymne, Sara",
    booktitle = "Proceedings of the Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025)",
    month = mar,
    year = "2025",
    address = "Tallinn, Estonia",
    publisher = "University of Tartu Library",
    url = "https://aclanthology.org/2025.nodalida-1.61/",
    pages = "573--608",
    ISBN = "978-9908-53-109-0"
}
```