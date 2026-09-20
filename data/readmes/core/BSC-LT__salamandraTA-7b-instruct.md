---
license: gpl-3.0
library_name: transformers
pipeline_tag: translation
language:
- bg
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fi
- fr
- ga
- gl
- hr
- hu
- it
- lt
- lv
- mt
- nl
- nb
- 'no'
- oc
- pl
- pt
- ro
- ru
- sl
- sk
- sr
- sv
- uk
- ast
- an
- ar
- ja
- hi
- ko
- zh
- is
base_model:
- BSC-LT/salamandra-7b
---


![](./images/salamandra_header.png)


## Releases

| Version | Ref | Description |
|---------|-----|-------------|
| [v3.0](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct) | `main` | Current release |
| [v2.0](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/tree/v2.0) | `v2.0` | Second release |
| [v1.0](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/tree/v1.0) | `v1.0` | Initial release |

> To load a specific version use the `revision` parameter:
> ```python
> model = AutoModelForCausalLM.from_pretrained(
>     "BSC-LT/salamandraTA-7b-instruct",
>     revision="v1.0"  # omit revision for current release
> )
> ```

# SalamandraTA Model Card

SalamandraTA-7b-instruct is a translation LLM that has been instruction-tuned from SalamandraTA-7b-base. 
The base model results from continually pre-training [Salamandra-7b](https://huggingface.co/BSC-LT/salamandra-7b) on monolingual and parallel data and has not been published, but is reserved for internal use. 
SalamandraTA-7b-instruct (v3) is proficient in **40 languages (+ 3 varieties)**, including both European and non-European languages such as Arabic, Japanese, Hindi, Korean, and Simplified Chinese, and is mainly trained to perform general translation tasks at the sentence, paragraph, and document levels.
Building on [our previous model's version](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/tree/v2.0), this version adds translation-related tasks such as terminology-aware machine translation, structured text (e.g., HTML, XML) translation, translation post-editing, and named entity recognition, while maintaining the strong translation performance of the previous version (see [Evaluation](#evaluation-on-general-machine-translation)).
For this release data under terms requiring GPL-3 distribution was used.

### License Notice
This release includes data licensed under GPL-3, and is therefore distributed under the terms of the GPL-3 license.

> [!WARNING]
> **DISCLAIMER:** This version of Salamandra is tailored exclusively for translation and the mentioned translation-related tasks. It lacks chat capabilities and has not been trained with any chat instructions.


---

## Model Details

### Description

SalamandraTA-7b-base is a continual pre-training of [Salamandra-7b](https://huggingface.co/BSC-LT/salamandra-7b). 

The continual pretraining phase is the same as in [our previous model's version](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/tree/v2.0).



### Architecture

|                         |               |
|-------------------------|:--------------|
| Total Parameters        | 7,768,117,248 |
| Embedding Parameters    | 1,048,576,000 |
| Layers                  | 32            |
| Hidden size             | 4,096         |
| Attention heads         | 32            |
| Context length          | 8,192         |
| Vocabulary size         | 256,000       |
| Precision               | bfloat16      |
| Embedding type          | RoPE          |
| Activation Function     | SwiGLU        |
| Layer normalization     | RMS Norm      |
| Flash attention         | ✅            |
| Grouped Query Attention | ✅            |
| Num. query groups       | 8             |


---

## Intended Use

### Direct Use

The model is intended for both research and commercial use in any of the languages included in the training data for general machine translation tasks and multiple translation-related tasks such as terminology-aware machine translation, structured text (e.g., HTML, XML) translation, and translation post-editing.

### Out-of-scope Use

The model is not intended for malicious activities, such as harming others or violating human rights. 
Any downstream application must comply with current laws and regulations. 
Irresponsible usage in production environments without proper risk assessment and mitigation is also discouraged. 

---


## Hardware and Software

### Training Framework

SalamandraTA-7b-base was continually pre-trained using NVIDIA's [NeMo Framework](https://github.com/NVIDIA-NeMo/NeMo), 
which leverages PyTorch Lightning for efficient model training in highly distributed settings.

SalamandraTA-7b-instruct was produced with [FastChat](https://github.com/lm-sys/FastChat).

### Compute Infrastructure

All models were trained on [MareNostrum 5](https://www.bsc.es/ca/marenostrum/marenostrum-5), a pre-exascale EuroHPC supercomputer hosted and
operated by Barcelona Supercomputing Center.

The accelerated partition is composed of 1,120 nodes with the following specifications:
- 4x Nvidia Hopper GPUs with 64GB HBM2 memory
- 2x Intel Sapphire Rapids 8460Y+ at 2.3Ghz and 32c each (64 cores)
- 4x NDR200 (BW per node 800Gb/s)
- 512 GB of Main memory (DDR5)
- 460GB on NVMe storage

---


## How to use

> [!NOTE]
> You can view and download the full user guide for the model here [How to use SalamandraTA models](./usage_guide.md).

The model can be used either directly in Python using the `transformers` library or deployed as a service and used through standard API calls.

While the former gives the most control over the inference process it requires the code to be executed on a machine with a sufficiently powerful GPU to run the model locally, and is more error prone than the alternative.
We therefore strongly recommend the latter, as deploying the model as a service can be done either locally or on a remote server and makes the model available to multiple clients in parallel among other advantages.

Unless you have very specific needs (e.g. for research) that require adapting the inference process it is preferable to follow the "deployment as a service" guidelines below.

### Local inference with Python / transformers

You can translate between the following **40 languages** (and 3 varieties):

Arabic, Aragonese, Asturian, Basque, Bulgarian, Catalan (and Catalan-Valencian variety), Chinese (simplified), Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hindi, Hungarian, Irish, Italian, Japanese, Korean, Latvian, Lithuanian, Maltese, Norwegian (Bokmål and Nynorsk varieties), Occitan (and Aranese variety), Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swedish, Ukrainian, Welsh.

The instruction-following model uses the commonly adopted ChatML template:

```
<|im_start|>system
{SYSTEM PROMPT}<|im_end|>
<|im_start|>user
{USER PROMPT}<|im_end|>
<|im_start|>assistant
{MODEL RESPONSE}<|im_end|>
<|im_start|>user
[...]
```

The easiest way to apply it is by using the tokenizer's built-in functions, as shown in the following snippet.

```python
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model_id = "BSC-LT/salamandraTA-7b-instruct"

source = 'Spanish'
target = 'Catalan'
sentence = "Ayer se fue, tomó sus cosas y se puso a navegar. Una camisa, un pantalón vaquero y una canción, dónde irá, dónde irá. Se despidió, y decidió batirse en duelo con el mar. Y recorrer el mundo en su velero. Y navegar, nai-na-na, navegar"
 
text = f"Translate the following text from {source} into {target}.\n{source}: {sentence} \n{target}:"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16
  )

message = [ { "role": "user", "content": text } ]
date_string = datetime.today().strftime('%Y-%m-%d')

prompt = tokenizer.apply_chat_template(
    message,
    tokenize=False,
    add_generation_prompt=True,
    date_string=date_string
)

inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
input_length = inputs.shape[1]
outputs = model.generate(input_ids=inputs.to(model.device), 
                         max_new_tokens=400,
                         early_stopping=True,
                         num_beams=5)

print(tokenizer.decode(outputs[0, input_length:], skip_special_tokens=True))
# Ahir se'n va anar, va recollir les seves coses i es va fer a la mar. Una camisa, uns texans i una cançó, on anirà, on anirà. Es va acomiadar i va decidir batre's en duel amb el mar. I fer la volta al món en el seu veler. I navegar, nai-na-na, navegar
```

Using this template, each turn is preceded by a `<|im_start|>` delimiter and the role of the entity 
(either `user`, for content supplied by the user, or `assistant` for LLM responses), and finished with the `<|im_end|>` token.

#### General translation

For machine translation tasks, you can use the following prompt template:

```
Translate the following text from {source} into {target}.
{source}: {source sentence}
{target}:
```
<details>
<summary>Show an example</summary>

```python
source = 'Catalan'
target = 'Galician'
source_sentence = "Als antics egipcis del període de l'Imperi Nou els fascinaven els monuments dels seus predecessors, que llavors tenien més de mil anys."

text = f"Translate the following text from {source} into {target}.\n{source}: {source_sentence} \n{target}:"
# Os antigos exipcios do período do Imperio Novo estaban fascinados polos monumentos dos seus predecesores, que entón tiñan máis de mil anos de antigüidade.
```

</details>


#### Terminology-aware translation

For terminology-aware translation tasks, you can use the following prompt template:

```
Please translate the following {source} text to {target} while respecting the glossary entries.

Required Terminology:

- {source_term_1} -> {target_term_1}
- {source_term_2} -> {target_term_2}

Source Text:

{source_sentence}
```
<details>
<summary>Show an example</summary>

```python
source = 'English'
target = 'Spanish'
source_term_1 = 'partner'
target_term_1 = 'socio'
source_term_2 = 'rule'
target_term_2 = 'regla'
source_sentence = "You create an installment plan, if there are one or more open items in the contract account of a business partner and the business partner cannot fulfill the payment obligation within the scope of the usual payment rules."

text = f"Please translate the following {source} text to {target} while respecting the glossary entries.\n\n\nRequired Terminology:\n\n- {source_term_1} -> {target_term_1}\n- {source_term_2} -> {target_term_2}\n\nSource Text: {source_sentence}"
# Usted crea un plan de cuotas, si hay uno o más artículos abiertos en la cuenta del contrato de un socio comercial y el socio comercial no puede cumplir con la obligación de pago dentro del alcance de las reglas de pago habituales.
```

</details>


#### Register-specific translation

To translate text using a formal or informal register, you can use the following prompt template:

```
Translate the text below from {source} to {target}. Use {register} language throughout.
{source_sentence}
```
<details>
<summary>Show an example</summary>

```python
source = 'English'
target = 'Spanish'
register = 'formal'
source_sentence = "When you finish the report, contact me."

text = f"Translate the text below from {source} to {target}. Use {register} language throughout.\n\n{source_sentence}"
# Cuando termine el informe, pongase en contacto conmigo.
```

</details>


#### Translating structured text (XML/HTML)

To translate text while keeping XML/HTML tags in place, use the following prompt template:

```
Translate this {source} text into {target}. Preserve any formatting, tags, delimiters, or structural elements exactly, and translate only the human-readable parts: {source_sentence}
```
<details>
<summary>Show an example</summary>

```python
source = 'English'
target = 'Spanish'
source_sentence = "In <ph>Lightning Experience</ph>: Compose a post. Mention people and groups, use rich text formating, and scroll down to see past posts to the dashboard feed. In <ph>Lightning Experience</ph>, you always post to the dashboard feed."

text = f"Translate this {source} text into {target}. Preserve any formatting, tags, delimiters, or structural elements exactly, and translate only the human-readable parts: {source_sentence}"
# En <ph>Lightning Experience</ph>: Cree una publicación. Mencione personas y grupos, use el formato de texto enriquecido y desplácese hacia abajo para ver publicaciones anteriores en el feed del panel. En <ph>Lightning Experience</ph>, siempre publica en el feed del panel.
```

</details>

#### Machine translation post-editing

To post-edit a machine-translated sentence, use the following prompt template:

```
"I need a polished, human-level translation. Edit the 'Machine Translation' "
"using the 'Source Text' as the definitive guide.\n"
"Source Text: {source_sentence}\n"
"Machine Translation (to be edited): {mt}"
```
<details>
<summary>Show an example</summary>

```python
source_sentence = 'But the daemon hordes came again, in far greater numbers and with much more ferocity.'
mt = "但是雏菊又来了, 数量大得多, 凶猛得多."

text = f"I need a polished, human-level translation. Edit the 'Machine Translation' using the 'Source Text' as the definitive guide.\nSource Text: {source_sentence}\nMachine Translation (to be edited): {mt}"
# 但是恶魔大军又来了，数量大得多，而且更加凶残。
```

</details>


#### Named Entity Recognition

The model is trained to recognize the following four entity types:

- PER — individual people or named groups of people
- ORG — named groups or organizations
- LOC — physical places or natural landmarks
- MISC — entities that don't fit the standard categories

To perform named entity recognition (NER) on a tokenized sentence, use the following prompt template:

```
"Study this taxonomy for classifying named entities:\n"
"PER (Refers to individual people or named groups of people), "
"ORG (Refers to named groups or organizations), "
"LOC (Refers to physical places or natural landmarks), "
"MISC (Refers to entities that don't fit into standard categories). "
"Identify all named entities in the following tokens:\n{tokens}\n"
"Additionally, you should add B- to the first token of a given entity "
"and I- to subsequent ones if they exist. "
"For tokens that are not named entities, mark them as O."
```

<details>
<summary>Show an example</summary>

```python
tokens = "["Aquesta", "xifra", "indica", "una", "tendència", "a", "la", "baixa", "en", "el", "pes", "de", "les", "ETT", "iniciat", "l'", "any", "1998", "."]"
text = (
    "Study this taxonomy for classifying named entities:\n"
    "PER (Refers to individual people or named groups of people), "
    "ORG (Refers to named groups or organizations), "
    "LOC (Refers to physical places or natural landmarks), "
    "MISC (Refers to entities that don't fit into standard categories). "
    "Identify all named entities in the following tokens:\n{tokens}\n"
    "Additionally, you should add B- to the first token of a given entity "
    "and I- to subsequent ones if they exist. "
    "For tokens that are not named entities, mark them as O."
)
# [('Aquesta', 'O'), ('xifra', 'O'), ('indica', 'O'), ('una', 'O'), ('tendència', 'O'), ('a', 'O'), ('la', 'O'), ('baixa', 'O'), ('en', 'O'), ('el', 'O'), ('pes', 'O'), ('de', 'O'), ('les', 'O'), ('ETT', 'B-ORG'), ('iniciat', 'O'), ('l', 'O'), ('any', 'O'), ('1998', 'O'), ('.', 'O')]
```

</details>


### Deployment as service and remote use (Messages API)

In our experience, `vllm` works well for deploying the full unquantized version of the model, whereas `llama.cpp` is appropriate for the quantized (GGUF) version.
**We strongly discourage using ollama as we have encountered compatibility issues that may seriously degrade the model's performance.**

The easiest and most reliable way to have a working deployment of ALIA-40b-instruct is through the "Deploy / HF Inference Endpoints" option directly on the Hugging Face model page.
This automatically creates a functioning endpoint, using vllm or llama.cpp according to the model variant, with an appropriately dimensioned GPU.
While there are additional settings available for the endpoint we found the standard configuration proposed by Hugging Face to be a reasonable starting point.

Once the endpoint is running, the model can be easily called using OpenAI's "Messages API" (the de facto standard API for LLM use). By using this API the chat template is applied automatically by the service, requiring no explicit configuration on the client side. The endpoint's configuration page on Hugging Face also provides a "Playground" for testing and API examples, as well as a simple chat interface.

Note that when using the model through the API you need to provide the prompt in the same format as described in the previous section.

Example usage:
```python
# pip install openai 

from openai import OpenAI 

client = OpenAI(
	base_url = YOUR_ENDPOINT_URL,
	api_key = YOUR_HF_TOKEN
)

model_id = "BSC-LT/salamandraTA-7b-instruct"

source = 'Spanish'
target = 'Catalan'
sentence = "Ayer se fue, tomó sus cosas y se puso a navegar. Una camisa, un pantalón vaquero y una canción, dónde irá, dónde irá. Se despidió, y decidió batirse en duelo con el mar. Y recorrer el mundo en su velero. Y navegar, nai-na-na, navegar"
 
text = f"Translate the following text from {source} into {target}.\n{source}: {sentence} \n{target}:"

chat_completion = client.chat.completions.create(
	model = model_id,
	messages = [
		{
			"role": "user",
			"content": text
		}
	],
  max_tokens = 1000,
  temperature = 0.0
)

print(chat_completion.choices[0].message.content)
```

The model can also be deployed locally or on any server infrastructure with sufficient GPUs, using vllm or llama.cpp.
We recommend an initial deployment on Hugging Face as a point of reference and comparison to make sure the model is behaving as expected in the desired deployment setup.

#### Compatibility wrapper

In order to integrate SalamandraTA as a drop-in replacement for translation services such as Google Translate or DeepL you can use the wrapper provided at https://github.com/langtech-bsc/mt-wrapper .
This service accepts incoming requests in Google Translate or DeepL format and translates them to appropriately formatted requests to a SalamandraTA endpoint.

The wrapper service can be deployed locally or on any hosting platform with minimal resource requirements.

---

## Data

For information on the pretraining data, please refer to the [README](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/blob/v2.0/README.md) of our previous version, since it remains the same. The difference lies in the supervised fine-tuning phase, where we included translation-related tasks in addition to the general machine translation task.



### Instruction Tuning Data

This model has been fine-tuned on ~930k instructions, targeting general machine translation tasks and translation-related tasks. It's important to note that no chat data was used in the fine-tuning process.

The table below lists every task, the datasets used, the language directions covered, and the number of instructions. 

The synthetic datasets *Catalan hours* and *Formality_synth* were generated from scratch using [Gemma 4](https://deepmind.google/models/gemma/gemma-4/).
The synthetic datasets *MeSpEn synthetic*, *EMEA synthetic*, *Synthetic Noisy Translation*, *escagleu-pe* were generated using [Gemma 4](https://deepmind.google/models/gemma/gemma-4/) starting from the original datasets linked for each of them in the following table.
EUpress is an internally created, unpublished dataset.

**Notation:** `→` = one direction, `↔` = both directions, `{...}` = a set of target languages, "N pairs" = number of language directions when the full list is too long to display.

| Task | Dataset | Language directions | # Instructions |
|---|---|---|---|
| General MT | [ALT](https://huggingface.co/datasets/mutiyama/alt) | en↔{hi, ja, zh}, ja↔zh | 4,000 |
| General MT | [SMOL (SmolSent)](https://huggingface.co/datasets/google/smol) | en→{ar, es, hi, is, ja, ko} | 4,957 |
| General MT | Eupress *(Internally created dataset)* | ca/en/es → 24 EU languages (72 pairs) | 36,000 |
| General MT | [NTEU](https://huggingface.co/datasets/BSC-LT/NTEU_Multilingual_Evaluation_Dataset) | ca/en/es → 24 EU languages (72 pairs) | 36,000 |
| General MT | [Tatoeba](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt) | 500+ pairs across 40+ languages | 121,361 |
| General MT | [WMT++](https://huggingface.co/datasets/google/wmt24pp) | en→32 languages | 16,000 |
| General MT | [FLEURS](https://huggingface.co/datasets/google/fleurs) | en/ca/es → XX | 12,900 |
| Terminology-aware MT | [MeSpEn synthetic](https://github.com/PlanTL-GOB-ES/MeSpEn_Glossaries/tree/master) *(Internally created synthetic dataset)* | 79 pairs (medical) | 12,479 |
| Terminology-aware MT | [EMEA synthetic](https://opus.nlpl.eu/datasets/EMEA) *(Internally created synthetic dataset)* | es/cs/de/en → EU languages (19 pairs, medical) | 21,136 |
| Paragraph-level | [ACAData (bench)](https://huggingface.co/datasets/BSC-LT/ACAData) | 12 pairs (ca/es/en/fr/pt) | 5,944 |
| Paragraph-level | [ACAData (train)](https://huggingface.co/datasets/BSC-LT/ACAData) | 96 pairs (Iberian + EU) | 27,852 |
| Paragraph-level | [News-Commentary](https://huggingface.co/datasets/Helsinki-NLP/news_commentary) | 70+ pairs | 56,000 |
| Paragraph-level | [NewsPalm](https://github.com/google-research/google-research/tree/master/newspalm) | en↔de | 10,000 |
| Paragraph-level | [npk_ndla](https://huggingface.co/datasets/NbAiLab/merged_npk_ndla_parallel_paragraphs)  | nb↔nn | 2,000 |
| Document-level | [SMOL (SmolDoc)](https://huggingface.co/datasets/google/smol) | en→{ar, hi, ja, ko, ru} | 1,177 |
| Document-level | [Europarl](https://huggingface.co/datasets/Helsinki-NLP/europarl) | 200+ EU pairs | 105,000 |
| Document-level | [Project Gutenberg](https://www.gutenberg.org/) | 30+ EU pairs | 8,959 |
| Post-editing | [QE4PE](https://huggingface.co/datasets/gsarti/qe4pe) | en→{it, nl} | 113 |
| Post-editing | [escagleu-pe](https://huggingface.co/datasets/projecte-aina/escagleu-64k) *(Internally created synthetic dataset)* | es/ca→{eu, gl} | 20,000 |
| Post-editing | [LangMark](https://zenodo.org/records/15553365) | en→{de, es, fr, it, ja, pt, ru} | 35,000 |
| Post-editing | [QT21](https://lindat.mff.cuni.cz/repository/items/f22bfcdc-413d-459a-a550-cf8851245cac) | en→{cs, de, lv}, de→en | 30,000 |
| Post-editing | [ApeQuest](https://apequest.wordpress.com/downloads/) | en→{fr, nl, pt} | 15,000 |
| Structured text (HTML) | [ACAData (bench)](https://huggingface.co/datasets/BSC-LT/ACAData) | 12 pairs (ca/es/en/fr/pt) | 5,381 |
| Structured text (HTML) | [ACAData (train)](https://huggingface.co/datasets/BSC-LT/ACAData) | 96 pairs (Iberian + EU) | 22,591 |
| Structured text (HTML) | Catalan hours *(Internally created dataset)* | ca↔es | 389 |
| Structured text (HTML) | [Europarl](https://huggingface.co/datasets/Helsinki-NLP/europarl) | 200+ EU pairs | 36,437 |
| Structured text (HTML) | [FLEURS](https://huggingface.co/datasets/google/fleurs) | 129 pairs | 12,900 |
| Structured text (HTML) | [News-Commentary](https://huggingface.co/datasets/Helsinki-NLP/news_commentary) | 60+ pairs | 15,040 |
| Structured text (HTML) | [Project Gutenberg](https://www.gutenberg.org/) | multiple | 2,497 |
| Grammar checking | [CoEdIT](https://huggingface.co/datasets/grammarly/coedit) | en | 20,308 |
| Grammar checking | Synthetic Noisy Translation (NTEU, EUpress) *(Internally created dataset)* | 25 languages | 12,500 |
| Paraphrase | [CoEdIT](https://huggingface.co/datasets/grammarly/coedit) | en | 15,897 |
| Register (formality) | formality_synth *(Internally created synthetic dataset)* | 17 pairs | 24,003 |
| Gender | [MT-GenEval](https://huggingface.co/datasets/gsarti/mt_geneval) | en→{ar, ca, de, es, fr, hi, it, nl, pt, ru} | 26,809 |
| Gender | [GLITTER](https://huggingface.co/datasets/mbvslowride/glitter) | en→de | 1,202 |
| Gender | [GeNTE](https://huggingface.co/datasets/FBK-MT/GeNTE) | en→it | 3,000 |
| Gender | [EuroGEST](https://huggingface.co/datasets/utter-project/EuroGEST) | en→21 languages | 29,076 |
| Named Entity Recognition | [AnCora-Ca-NER](https://huggingface.co/datasets/projecte-aina/ancora-ca-ner) | ca | 10,629 |
| Named Entity Recognition | [EIEC](https://www.ixa.eus/node/4486?language=en) | eu | 2,552 |
| Named Entity Recognition | [SLI NERC Galician](https://github.com/xavier-gz/SLI_Galician_Corpora) | gl | 6,483 |
| Multi-reference translation | [Tatoeba](https://huggingface.co/datasets/Helsinki-NLP/tatoeba_mt) | 500+ pairs across 40+ languages | 100,973 |
| **Total** | | | **930,545** |


<details id="instr-references">
<summary>References</summary>

### References

- Agerri, R., Gómez Guinovart, X., Rigau, G., & Solla Portela, M. A. (2018). Developing new linguistic resources and tools for the Galician language. In *Proceedings of the Eleventh Language Resources and Evaluation Conference (LREC 2018)* (pp. 2322–2325). European Language Resources Association. https://aclanthology.org/L18-1369/
- Agrawal, P., Hackenbuchner, J., Attanasio, G., Lardelli, M., & Lauscher, A. (2025). Glitter: A multi-sentence, multi-reference benchmark for gender-fair German machine translation. In *Findings of the Association for Computational Linguistics: EMNLP 2025* (pp. 18450–18477). Association for Computational Linguistics. https://aclanthology.org/2025.findings-emnlp.1002/
- Armengol-Estapé, J., Carrino, C. P., Rodriguez-Penagos, C., de Gibert Bonet, O., Armentano-Oller, C., Gonzalez-Agirre, A., Melero, M., & Villegas, M. (2021). Are multilingual models the best choice for moderately under-resourced languages? A comprehensive assessment for Catalan. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021* (pp. 4933–4946). Association for Computational Linguistics. https://aclanthology.org/2021.findings-acl.437
- Bié, L., Cerdà-i-Cucó, A., Degroote, H., Estela, A., García-Martínez, M., Herranz, M., Kohan, A., Melero, M., O'Dowd, T., O'Gorman, S., Pinnis, M., Rozis, R., Superbo, R., & Vasiļevskis, A. (2020). Neural Translation for the European Union (NTEU) Project. In *Proceedings of the 22nd Annual Conference of the European Association for Machine Translation* (pp. 477–478). European Association for Machine Translation. https://aclanthology.org/2020.eamt-1.60/
- Caswell, I., Nielsen, E., Luo, J., Cherry, C., Kovacs, G., Shemtov, H., Talukdar, P., Tewari, D., Diane, B. M., Doumbouya, K. M., Diane, D., & Cissé, S. F. (2025). *SMOL: Professionally translated parallel data for 115 under-represented languages* (No. arXiv:2502.12301). arXiv. https://arxiv.org/abs/2502.12301
- Conneau, A., Ma, M., Khanuja, S., Zhang, Y., Axelrod, V., Dalmia, S., Riesa, J., Rivera, C., & Bapna, A. (2022). FLEURS: Few-shot learning evaluation of universal representations of speech. *2022 IEEE Spoken Language Technology Workshop (SLT)*, 798–805. https://arxiv.org/abs/2205.12446
- Currey, A., Nadejde, M., Pappagari, R., Mayer, M., Lauly, S., Niu, X., Hsu, B., & Dinu, G. (2022). MT-GenEval: A counterfactual and contextual dataset for evaluating gender accuracy in machine translation. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (pp. 4287–4299). Association for Computational Linguistics. https://aclanthology.org/2022.emnlp-main.288/
- Deutsch, D., Briakou, E., Caswell, I., Finkelstein, M., Galor, R., Juraska, J., Kovacs, G., Lui, A., Rei, R., Riesa, J., Rijhwani, S., Riley, P., Salesky, E., Trabelsi, F., Winkler, S., Zhang, B., & Freitag, M. (2025). WMT24++: Expanding the language coverage of WMT24 to 55 languages & dialects (No. arXiv:2502.12404). arXiv. https://arxiv.org/abs/2502.12404
- Finkelstein, M., Juraska, J., & Freitag, M. (2024). Introducing the NewsPaLM MBR and QE dataset: LLM-generated high-quality parallel data outperforms traditional web-crawled data (No. arXiv:2408.06537). arXiv. https://arxiv.org/abs/2408.06537
- Ive, J., Specia, L., Szoc, S., Vanallemeersch, T., Van den Bogaert, J., Farah, E., Maroti, C., Ventura, A., & Khalilov, M. (2020). A post-editing dataset in the legal domain: Do we underestimate neural machine translation quality? In N. Calzolari et al. (Eds.), *Proceedings of the Twelfth Language Resources and Evaluation Conference* (pp. 3692–3697). European Language Resources Association. https://aclanthology.org/2020.lrec-1.455/
- Koehn, P. (2005). Europarl: A parallel corpus for statistical machine translation. In *Proceedings of Machine Translation Summit X* (pp. 79–86). https://aclanthology.org/2005.mtsummit-papers.11/
- Kummervold, P. E., Tollersrud, T., & Zanardi, A. (2026). Building a One-Million-Pair Bokmål–Nynorsk translation corpus: A quality-first harvesting and cleaning pipeline. In *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)* (pp. 8551–8555). European Language Resources Association (ELRA). https://doi.org/10.63317/4jidtc8558q6
- Lacunza, I., Garcia Gilabert, J., De Luca Fornaciari, F., Aula-Blasco, J., Gonzalez-Agirre, A., Melero, M., & Villegas, M. (2025). ACAData: Parallel dataset of academic data for machine translation (No. arXiv:2510.12621). arXiv. https://arxiv.org/abs/2510.12621
- Masciolini, A., Caines, A., De Clercq, O., Kruijsbergen, J., Kurfalı, M., Muñoz Sánchez, R., Volodina, E., Östling, R., Allkivi, K., Arhar Holdt, Š., Auzina, I., Darģis, R., Drakonaki, E., Frey, J.-C., Glišić, I., Kikilintza, P., Nicolas, L., Romanyshyn, M., Rosen, A., Rozovskaya, A., Suluste, K., Syvokon, O., Tantos, A., Touriki, D.-O., Tsiotskas, K., Tsourilla, E., Varsamopoulos, V., Wisniewski, K., Žagar, A., & Zesch, T. (2025). Towards better language representation in natural language processing: A multilingual dataset for text-level grammatical error correction. *International Journal of Learner Corpus Research, 11*(2). https://doi.org/10.1075/ijlcr.24033.mas
- Piergentili, A., Savoldi, B., Fucci, D., Negri, M., & Bentivogli, L. (2023). Hi guys or hi folks? Benchmarking gender-neutral machine translation with the GeNTE corpus. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 7892–7907). Association for Computational Linguistics. https://arxiv.org/abs/2310.05294
- Pranav, A., Hackenbuchner, J., Attanasio, G., Lardelli, M., & Lauscher, A. (2025). Glitter: A multi-sentence, multi-reference benchmark for gender-fair German machine translation. In Findings of the Association for Computational Linguistics: EMNLP 2025 (pp. 18450–18477). Association for Computational Linguistics. https://aclanthology.org/2025.findings-emnlp.1002/
- Project Gutenberg. (n.d.). Project Gutenberg. https://www.gutenberg.org/
- Raheja, V., Kumar, D., Koo, R., & Kang, D. (2023). CoEdIT: Text editing by task-specific instruction tuning (No. arXiv:2305.09857). arXiv. https://arxiv.org/abs/2305.09857
- Riza, H., Purwoadi, M., Gunarso, Uliniansyah, T., Ti, A. A., Aljunied, S. M., Mai, L. C., Thang, V. T., Thai, N. P., Chea, V., Sun, R., Sam, S., Seng, S., Soe, K. M., Nwet, K. T., Utiyama, M., & Ding, C. (2016). *Introduction of the Asian Language Treebank*. Proceedings of the 2016 Conference of the Oriental Chapter of the International Committee for Coordination and Standardization of Speech Databases and Assessment Techniques (O-COCOSDA), 1–6. IEEE. https://ieeexplore.ieee.org/document/7918974
- Rowe, J., Klimaszewski, M., Guillou, L., Vallor, S., & Birch, A. (2025). EuroGEST: Investigating gender stereotypes in multilingual language models. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*. https://arxiv.org/abs/2506.03867
- Sarti, G., Zouhar, V., Chrupała, G., Guerberof Arenas, A., Nissim, M., & Bisazza, A. (2025). QE4PE: Word-level quality estimation for human post-editing (No. arXiv:2503.03044). arXiv. https://arxiv.org/abs/2503.03044
- Specia, L., Harris, K., Blain, F., Burchardt, A., Macketanz, V., Skadiņa, I., Negri, M., & Turchi, M. (2017). Translation quality and productivity: A study on rich morphology languages. *Proceedings of Machine Translation Summit XVI*, 55–71.
- Taulé, M., Martí, M. A., & Recasens, M. (2008). AnCora: Multilevel annotated corpora for Catalan and Spanish. In Proceedings of the Sixth International Conference on Language Resources and Evaluation (LREC 2008). European Language Resources Association. https://aclanthology.org/L08-1222/
- Tiedemann, J. (2020). The Tatoeba translation challenge – Realistic data sets for low-resource and multilingual MT. *Proceedings of the Fifth Conference on Machine Translation*, 1174–1182. Association for Computational Linguistics. https://aclanthology.org/2020.wmt-1.139
- Urbizu, G., San Vicente, I., Saralegi, X., Agerri, R., & Soroa, A. (2022). BasqueGLUE: A natural language understanding benchmark for Basque. *Proceedings of the Language Resources and Evaluation Conference*, 1603–1612. European Language Resources Association. https://aclanthology.org/2022.lrec-1.172
- Velazquez, D., Grace, M., Karageorgos, K., Carin, L., Schliem, A., Zaikis, D., & Wechsler, R. (2025). LangMark: A multilingual dataset for automatic post-editing. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics* (Vol. 1, pp. 32653–32667). Association for Computational Linguistics. https://aclanthology.org/2025.acl-long.1569/
- Villegas, M., Intxaurrondo, A., Gonzalez-Agirre, A., Marimon, M., & Krallinger, M. (2018). The MeSpEN resource for English-Spanish medical machine translation and terminologies: Census of parallel corpora, glossaries and term translations. In Proceedings of the LREC 2018 Workshop "MultilingualBIO: Multilingual Biomedical Text Processing" (pp. 32–39). European Language Resources Association.

</details>


## Evaluation on General Machine Translation

Below are the evaluation results on the [FLORES+200 devtest set](https://huggingface.co/datasets/openlanguagedata/flores_plus) and [BOUQuET test subset (sentence-level)](https://huggingface.co/datasets/facebook/bouquet), compared against the widely-used [MADLAD400-7B-mt model](https://huggingface.co/google/madlad400-7b-mt) ([Kudugunta, S., et al.](https://arxiv.org/abs/2309.04662)), and [our previously released translation LLM](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/tree/v2.0). 
These results cover the translation directions CA-XX, ES-XX, EN-XX, as well as XX-CA, XX-ES, and XX-EN, including both European and Asian languages.
The metrics have been computed excluding Asturian, Aranese, and Aragonese, as we report them separately.
The evaluation was conducted using [MT-Lens](https://github.com/langtech-bsc/mt-evaluation), following the standard setting (beam search with beam size 5, limiting the translation length to 800 tokens). We report the following metrics:

<details>
<summary>Click to show metrics details</summary>

- `BLEU`: Sacrebleu implementation. Signature: nrefs:1— case:mixed— eff:no— tok:13a— smooth:exp—version:2.3.1
- `TER`: Sacrebleu implementation.
- `ChrF`: Sacrebleu implementation.
- `Comet`: Model checkpoint: "Unbabel/wmt22-comet-da".
- `Comet-kiwi`: Model checkpoint: "Unbabel/wmt22-cometkiwi-da".
- `Bleurt`: Model checkpoint: "lucadiliello/BLEURT-20".
- `MetricX`: Model checkpoint: "google/metricx-23-xl-v2p0".
- `MetricX-QE`: Model checkpoint: "google/metricx-23-qe-xl-v2p0".

</details>


<details>
<summary>English evaluation</summary>
  
### English

This section presents the evaluation metrics for English translation tasks.

#### Flores+200 devtest set

|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **EN-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 37.64 | 54.42 | 62.10 | 0.89 | 0.85 | 0.78 | 1.24 | 1.31 |
| SalamandraTA-7b-instruct v3 | **37.95** | **54.32** | **62.31** | **0.89** | **0.85** | **0.78** | **1.17** | **1.21** |
| MADLAD400-7B | 33.95 | 61.26 | 59.55 | 0.87 | 0.83 | 0.76 | 1.67 | 1.60 |
| **XX-EN** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 44.65 | 42.50 | 68.20 | 0.89 | 0.85 | 0.79 | 1.21 | 1.38 |
| SalamandraTA-7b-instruct v3 | **44.83** | **42.23** | **68.36** | **0.89** | 0.85 | 0.79 | 1.18 | 1.31 |
| MADLAD400-7B | 42.71 | 43.96 | 67.60 | 0.89 | **0.85** | **0.79** | **1.15** | **1.17** |


<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_en_flores+_devtest.png" alt="English FLORES" width="100%"/>

#### BOUQuET test subset (sentence-level)

|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **EN-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 43.06 | 49.37 | 63.41 | 0.90 | 0.85 | 0.81 | 0.76 | 0.89 |
| SalamandraTA-7b-instruct v3 | **43.61** | **49.05** | **63.60** | **0.90** | **0.85** | **0.81** | **0.73** | **0.82** |
| MADLAD400-7B | 41.45 | 53.17 | 62.91 | 0.89 | 0.85 | 0.79 | 0.93 | 0.94 |
| **XX-EN** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 47.78 | **40.84** | 66.85 | 0.90 | 0.85 | 0.80 | 0.85 | 0.86 |
| SalamandraTA-7b-instruct v3 | **47.92** | 40.94 | 66.79 | 0.90 | 0.85 | 0.80 | 0.84 | 0.84 |
| MADLAD400-7B | 47.68 | 41.14 | **66.92** | **0.90** | **0.85** | **0.81** | **0.80** | **0.71** |



<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_en_bouquet.png" alt="English BOUQuET" width="100%"/>

</details>

<details>
<summary>Spanish evaluation</summary>
  
### Spanish

This section presents the evaluation metrics for Spanish translation tasks.

#### Flores+200 devtest set


|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **ES-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 24.93 | 68.08 | 52.71 | 0.86 | 0.82 | 0.75 | 1.17 | 1.27 |
| SalamandraTA-7b-instruct v3 | **25.05** | **67.77** | **52.85** | **0.87** | 0.82 | **0.75** | **1.12** | **1.15** |
| MADLAD400-7B | 21.60 | 76.69 | 50.45 | 0.85 | **0.82** | 0.73 | 1.50 | 1.58 |
| **XX-ES** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | **25.39** | **61.34** | **52.94** | 0.85 | 0.83 | 0.73 | 1.11 | 1.59 |
| SalamandraTA-7b-instruct v3 | 25.03 | 61.54 | 52.85 | 0.85 | 0.83 | 0.73 | 1.11 | **1.53** |
| MADLAD400-7B | 24.45 | 62.40 | 52.61 | **0.85** | **0.84** | **0.74** | **1.07** | 1.54 |


<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_es_flores+_devtest.png" alt="Spanish FLORES" width="100%"/>


#### BOUQuET test subset (sentence-level)

|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **ES-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 33.47 | **59.89** | 55.73 | 0.88 | 0.82 | 0.78 | 0.78 | 0.84 |
| SalamandraTA-7b-instruct v3 | **33.84** | 60.11 | 55.71 | **0.89** | **0.82** | **0.78** | **0.76** | **0.78** |
| MADLAD400-7B | 32.98 | 61.71 | **55.82** | 0.88 | 0.81 | 0.77 | 0.91 | 0.95 |
| **XX-ES** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 36.58 | 53.91 | 59.54 | 0.88 | 0.82 | 0.78 | 0.73 | 0.95 |
| SalamandraTA-7b-instruct v3 | 37.05 | **53.56** | 59.69 | **0.88** | 0.83 | 0.79 | 0.72 | 0.91 |
| MADLAD400-7B | **37.30** | 53.61 | **60.19** | 0.88 | **0.83** | **0.79** | **0.67** | **0.80** |


<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_es_bouquet.png" alt="Spanish BOUQuET" width="100%"/>


</details>

<details>
<summary>Catalan evaluation</summary>
  
### Catalan

This section presents the evaluation metrics for Catalan translation tasks.

#### Flores+200 devtest set


|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **CA-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 30.34 | 61.72 | 56.67 | 0.87 | 0.80 | 0.76 | 1.24 | 1.50 |
| SalamandraTA-7b-instruct v3 | **30.42** | **61.13** | **56.78** | **0.87** | 0.81 | **0.76** | **1.17** | **1.36** |
| MADLAD400-7B | 27.92 | 73.50 | 54.55 | 0.86 | **0.81** | 0.75 | 1.54 | 1.83 |
| **XX-CA** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 34.50 | 53.66 | 60.04 | 0.86 | 0.80 | 0.75 | 1.20 | 1.81 |
| SalamandraTA-7b-instruct v3 | **34.69** | **53.53** | **60.28** | **0.86** | 0.81 | **0.75** | **1.09** | **1.61** |
| MADLAD400-7B | 32.50 | 55.67 | 58.94 | 0.86 | **0.81** | 0.75 | 1.23 | 1.79 |

<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_ca_flores+_devtest.png" alt="Catalan FLORES" width="100%"/>


#### BOUQuET test subset (sentence-levl, updated)

|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **CA-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 30.20 | 68.20 | 53.90 | 0.88 | 0.79 | 0.77 | 0.83 | 1.06 |
| SalamandraTA-7b-instruct v3 | **32.35** | **64.38** | **54.56** | **0.88** | **0.79** | **0.77** | **0.77** | **0.93** |
| MADLAD400-7B | 30.79 | 67.54 | 53.86 | 0.87 | 0.79 | 0.76 | 0.97 | 1.27 |
| **XX-CA** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v2 | 33.22 | 56.51 | 56.58 | 0.86 | 0.78 | 0.75 | 0.93 | 1.42 |
| SalamandraTA-7b-instruct v3 | **34.22** | **56.08** | **56.87** | **0.86** | **0.78** | **0.76** | **0.86** | **1.29** |
| MADLAD400-7B | 30.91 | 59.25 | 54.72 | 0.84 | 0.78 | 0.74 | 1.04 | 1.55 |



<img src="https://huggingface.co/BSC-LT/salamandraTA-7b-instruct/resolve/v3.0-dev/images/bleu_ca_bouquet.png" alt="Catalan BOUQuET" width="100%"/>

</details>


### Low-Resource Languages of Spain

The tables below report performance metrics on the FLORES-200 devtest set for translation from English, Spanish, and Catalan into Asturian, Aranese, and Aragonese. Results are compared 
to [Transducens/IbRo-nllb](https://huggingface.co/Transducens/IbRo-nllb) [(Galiano Jimenez, et al.)](https://aclanthology.org/2024.wmt-1.85/).


<details>
<summary>English evaluation</summary>

#### English-XX

| Model                     | source | target | Bleu ↑ | Ter ↓ | ChrF ↑ |
|:--------------------------|:-------|:-------|:-----------|:-----------|:-----------|
| SalamandraTA-7b-instruct v2 | en     | ast    | 35.08 | 50.94 | 62.32 |
| SalamandraTA-7b-instruct v3 |        |        | **35.46** | **50.28** | **62.64** |
| Transducens/IbRo-nllb     |        |        | 20.56 | 63.92 | 53.32 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | en     | arn    | 26.82 | 59.78 | 55.76 |
| SalamandraTA-7b-instruct v3 |        |        | **27.02** | **59.66** | **56.20** |
| Transducens/IbRo-nllb     |        |        | 12.81 | 73.21 | 45.76 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | en     | arg    | 25.82 | 59.73 | 55.02 |
| SalamandraTA-7b-instruct v3 |        |        | **26.60** | **59.44** | **55.50** |
| Transducens/IbRo-nllb     |        |        | 14.07 | 70.37 | 46.89 |
| | | | | | |





</details>



<details>
<summary>Spanish evaluation</summary>

#### Spanish-XX

| Model                     | source | target | Bleu ↑ | Ter ↓ | ChrF ↑ |
|:--------------------------|:-------|:-------|:-----------|:-----------|:-----------|
| SalamandraTA-7b-instruct v2 | es     | ast    | 23.95 | 65.13 | **54.59** |
| SalamandraTA-7b-instruct v3 |        |        | **24.38** | **64.41** | 54.15 |
| Transducens/IbRo-nllb     |        |        | 16.79 | 76.36 | 50.89 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | es     | arn    | **54.73** | **34.09** | **74.64** |
| SalamandraTA-7b-instruct v3 |        |        | 54.26 | 34.47 | 74.48 |
| Transducens/IbRo-nllb     |        |        | 50.20 | 36.60 | 73.16 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | es     | arg    | 58.31 | 29.31 | 77.53 |
| SalamandraTA-7b-instruct v3 |        |        | 59.00 | 29.06 | 77.64 |
| Transducens/IbRo-nllb     |        |        | **59.75** | **28.01** | **78.73** |
| | | | | | |


  
</details>


<details>
<summary>Catalan evaluation</summary>

  
#### Catalan-XX


| Model                     | source | target | Bleu ↑ | Ter ↓ | ChrF ↑ |
|:--------------------------|:-------|:-------|:-----------|:-----------|:-----------|
| SalamandraTA-7b-instruct v2 | ca     | ast    | 30.86 | 55.50 | **59.76** |
| SalamandraTA-7b-instruct v3 |        |        | **30.92** | **54.96** | 59.51 |
| Transducens/IbRo-nllb     |        |        | 24.77 | 61.60 | 57.49 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | ca     | arn    | 32.83 | 53.17 | 60.76 |
| SalamandraTA-7b-instruct v3 |        |        | **32.93** | **53.04** | **61.06** |
| Transducens/IbRo-nllb     |        |        | 31.22 | 54.30 | 60.30 |
| | | | | | |
| SalamandraTA-7b-instruct v2 | ca     | arg    | 26.02 | **59.24** | 55.80 |
| SalamandraTA-7b-instruct v3 |        |        | **27.11** | 59.41 | **56.33** |
| Transducens/IbRo-nllb     |        |        | 24.44 | 60.79 | 55.51 |
| | | | | | |


</details>



## Gender bias evaluation (GenEval)

Comparing **SalamandraTA-7b-instruct (v3)** against **v2** and four public baselines, translating from English to the target language.

<details>
<summary>Contextual — gender_from_context</summary>

The source sentence pair only reveals the referent's gender through surrounding discourse context (e.g. a preceding sentence using "he"/"she"); accuracy at recovering the correct grammatical gender in translation without an explicit local cue.

| Language | SalamandraTA-7b-instruct (v3) | SalamandraTA-7b-instruct (v2) | NLLB-200-3.3B | MADLAD-400-7B | Qwen2.5-7B-Instruct | EuroLLM-9B-Instruct |
|---|---|---|---|---|---|---|
| ar | **93.3** | 87.1 | 79.2 | 83.1 | 92.0 | 86.5 |
| ca | **95.0** | 91.0 | 77.1 | 86.9 | 86.5 | 91.2 |
| de | **91.9** | 87.9 | 76.1 | 88.0 | 79.3 | 88.8 |
| es | **91.7** | 83.8 | 81.8 | 81.7 | 78.7 | 86.0 |
| fr | **92.9** | 84.7 | 68.5 | 77.1 | 78.5 | 82.8 |
| it | **90.6** | 83.8 | 71.1 | 78.1 | 79.5 | 84.2 |
| nl | **89.4** | 77.6 | 72.8 | 71.2 | 84.9 | 79.6 |
| pt | **90.2** | 86.3 | 71.4 | 79.2 | 77.9 | 85.7 |
| ru | **92.4** | 87.5 | 81.6 | 85.8 | 90.5 | 89.3 |
|---|---|---|---|---|---|---|
| **Avg** (n=9) | **91.9** | **85.5** | **75.5** | **81.2** | **83.1** | **86.0** |

</details>

<details>
<summary>Single — PAIR (both genders correct)</summary>

No context is provided; source sentences come as masculine/feminine minimal-pair contrasts, and PAIR accuracy requires both the masculine-referent and feminine-referent versions of a pair to be translated with correct gender. nl has no single/no-context split in this eval set, hence its absence from this table.

| Language | SalamandraTA-7b-instruct (v3) | SalamandraTA-7b-instruct (v2) | NLLB-200-3.3B | MADLAD-400-7B | Qwen2.5-7B-Instruct | EuroLLM-9B-Instruct |
|---|---|---|---|---|---|---|
| ar | 80.0 | 80.0 | 76.0 | 76.7 | **83.0** | 73.0 |
| ca | **71.7** | 69.3 | 62.0 | 61.3 | 66.3 | 68.0 |
| de | **76.3** | 75.7 | 67.7 | 71.3 | 71.3 | 71.3 |
| es | 70.7 | 69.0 | 66.3 | 68.7 | 65.7 | **71.7** |
| fr | **72.3** | 65.7 | 64.3 | 66.3 | 69.7 | 69.0 |
| it | **68.3** | 63.3 | 59.7 | 59.7 | 61.7 | 63.7 |
| pt | **72.3** | 71.3 | 65.0 | 62.7 | 65.0 | 66.7 |
| ru | 78.0 | 72.7 | 72.3 | 74.0 | **80.3** | 75.3 |
|---|---|---|---|---|---|---|
| **Avg** (n=8) | **73.7** | **70.9** | **66.7** | **67.6** | **70.4** | **69.8** |

</details>


## Evaluation on Translation-related Tasks

### Terminology-aware translation

Below are the evaluation results on the [WMT25 Terminology Shared Task (Track 1) test set](https://www2.statmt.org/wmt25/terminology.html#data), covering sentence- and paragraph-level translation on 3 language pairs: en-de (English → German), en-ru (English → Russian), en-es (English → Spanish). 
We compare against the top-ranked systems in the shared task and report chrF and term accuracy from the official [WMT2025 Findings](https://aclanthology.org/2025.wmt-1.30.pdf) rankings.

<details>
<summary>WMT2025 Terminology Translation Shared Task Track 1 Ranking</summary>

| System | ChrF Avg | Es | De | Ru | Acc Avg | Es | De | Ru |
|---|---|---|---|---|---|---|---|---|
| o3-term-guide | 71.0 | 75.9 | 71.6 | 65.6 | 99.1 | 99.1 | 99.1 | 99.0 |
| duterm | 70.1 | 76.1 | 70.7 | 63.6 | 98.2 | 98.7 | 98.2 | 97.6 |
| **SalamandraTA-7b-instruct (v3)** | **69.4** | **75.6** | **70.4** | **62.2** | **94.0** | **95.2** | **95.4** | **91.6** |
| Erlendur | 69.3 | 74.8 | 69.9 | 63.3 | 92.9 | 94.4 | 93.2 | 91.2 |
| TiUTermV1 | 68.9 | 77.1 | 65.7 | 63.8 | 87.6 | 89.4 | 87.3 | 86.1 |
| GPT-4.1-nano | 67.4 | 72.4 | 67.4 | 62.3 | 90.7 | 95.2 | 89.0 | 88.0 |
| salamandrata (WMT25 submission) | 67.3 | 72.0 | 69.6 | 60.4 | 91.3 | 92.7 | 91.7 | 89.4 |
| MeGuMa | 67.2 | 72.0 | 67.7 | 61.9 | 97.4 | 97.0 | 96.3 | 98.8 |
| tower | 66.0 | 74.0 | 65.9 | 58.1 | 93.7 | 95.0 | 94.8 | 91.2 |
| CommandA (WMT) | 65.9 | 70.7 | 67.6 | 59.3 | 79.9 | 81.9 | 86.9 | 70.7 |
| BIT | 63.7 | 69.8 | 62.4 | 58.9 | 97.0 | 96.3 | 98.0 | 96.7 |
| TiUTermV0 | 62.7 | 69.0 | 61.0 | 58.3 | 74.4 | 75.2 | 71.1 | 76.8 |
| laniqo | 61.7 | 68.5 | 59.8 | 56.9 | 99.3 | 98.7 | 99.4 | 99.6 |
| LC-primary | 61.4 | 68.9 | 61.2 | 54.2 | 70.2 | 74.1 | 70.7 | 65.8 |
| LC-2 | 60.8 | 67.7 | 61.0 | 53.7 | 70.0 | 73.6 | 70.7 | 65.6 |
| LC-3 | 60.8 | 67.7 | 61.0 | 53.7 | 70.0 | 73.6 | 70.7 | 65.6 |
| CurTermNLLB | 60.1 | 69.1 | 60.3 | 51.0 | 63.4 | 76.5 | 79.0 | 34.6 |
| ContexTerm | 48.5 | 53.7 | 40.2 | 51.5 | 72.0 | 68.5 | 79.9 | 67.6 |

</details>

### Structured documentation translation

Below are the evaluation results on the [Salesforce Localization XML MT dataset](https://github.com/salesforce/localization-xml-mt), a collection of parallel sentences with naturally occurring XML tags, covering translation between English and German, Finnish, French, Japanese, Dutch, Russian, and Chinese. We compare against [Tower-Plus-9B](https://huggingface.co/Unbabel/Tower-Plus-9B) using greedy decoding, and report both machine translation quality metrics and XML tag preservation.

<details>
<summary>Machine translation quality metrics result</summary>

|  | Bleu↑ | Ter↓ | ChrF↑ | Comet↑ | Comet-kiwi↑ | Bleurt↑ | MetricX↓ | MetricX-QE↓ |
|:---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| **EN-XX** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v3 | 45.39 | 64.07 | 63.76 | 0.88 | 0.82 | 0.74 | 1.18 | 1.24 |
| Tower-Plus-9B | **47.39** | **61.45** | **65.09** | **0.88** | **0.82** | **0.75** | **1.06** | **1.17** |
| **XX-EN** |  |  |  |  |  |  |  |  |
| SalamandraTA-7b-instruct v3 | **52.02** | **41.97** | **71.33** | **0.89** | 0.82 | **0.78** | 1.10 | 1.40 |
| Tower-Plus-9B | 49.33 | 43.94 | 71.00 | 0.88 | **0.82** | 0.77 | **1.07** | **1.34** |

</details>


We report XML tag preservation quality using a position-aware F1 score, evaluating how faithfully each model keeps XML tags intact when translating. Precision (P) measures how many of the tags the model produced were correct—valid and in the right position. It penalizes spurious or misplaced tags. Recall (R) measures how many of the tags that should have been preserved were actually kept, so it penalizes dropped or missing tags. F1 is the harmonic mean of the two, giving a single balanced score that is high only when the model both places tags correctly and retains them. A high precision with a much lower recall indicates a model that is accurate when it does emit a tag but drops many it should have kept, whereas closely matched, uniformly high P and R indicate consistent, reliable tag preservation.

<details>
<summary>XML tag preservation - F1 score (Position-aware)</summary>

| Language | Tower-Plus-9B P | Tower-Plus-9B R | Tower-Plus-9B F1 | SalamandraTA-7b-instruct (v3) P | SalamandraTA-7b-instruct (v3) R | SalamandraTA-7b-instruct (v3) F1 |
|---|---|---|---|---|---|---|
| de→en | 98.6 | 90.4 | 94.3 | 98.6 | 97.9 | 98.2 |
| en→de | 99.2 | 94.0 | 96.5 | 98.8 | 98.3 | 98.6 |
| en→fi | 97.9 | 92.0 | 94.9 | 98.0 | 97.1 | 97.5 |
| en→fr | 99.9 | 92.9 | 96.3 | 99.9 | 99.8 | 99.8 |
| en→ja | 99.4 | 92.0 | 95.6 | 98.9 | 98.3 | 98.6 |
| en→nl | 99.7 | 96.1 | 97.9 | 99.0 | 98.8 | 98.9 |
| en→ru | 99.4 | 92.7 | 95.9 | 97.5 | 97.8 | 97.7 |
| en→zh | 98.9 | 93.1 | 95.9 | 99.1 | 98.7 | 98.9 |
| fi→en | 97.9 | 84.7 | 90.9 | 98.2 | 97.1 | 97.7 |
| fr→en | 99.8 | 90.5 | 94.9 | 100.0 | 99.1 | 99.5 |
| ja→en | 98.7 | 73.6 | 84.3 | 89.0 | 98.0 | 93.3 |
| nl→en | 99.3 | 89.8 | 94.3 | 99.5 | 98.6 | 99.0 |
| ru→en | 99.1 | 84.9 | 91.4 | 99.0 | 98.8 | 98.9 |
| zh→en | 99.2 | 87.3 | 92.8 | 98.6 | 98.8 | 98.7 |
| **Average** | **99.1** | **89.6** | **94.0** | **98.2** | **98.4** | **98.2** |


</details>


### Named Entity Recognition (NER)

NER datasets for the languages of Spain were included during instruction tuning, but the model is not specifically optimized for this task. Despite this, it has learned to annotate entity tags. We evaluate it on the datasets below and compare against published baselines. Note that these baselines are encoder models, some of them fine-tuned specifically for this task, so they are expected to score higher; the comparison is intended as a reference point rather than a like-for-like benchmark. We plan to improve NER performance in future versions by including more training data for this task and covering more languages.


<details>
<summary>NER evaluation results</summary>
  
| Test set | Lang | Precision | Recall | micro-F1 | Published baseline | Baseline F1 |
|---|---|---|---|---|---|---|
| Catalan AnCora | ca | 84.6 | 84.9 | 84.8 | [RoBERTa-large-ca-v2](https://huggingface.co/projecte-aina/roberta-large-ca-v2) | 89.8 |
| Spanish CoNLL 2002 | es | 82.5 | 82.6 | 82.5 | [SpanMarker XLM-R-large](https://huggingface.co/alvarobartt/span-marker-xlm-roberta-large-conll-2002-es) | 89.1 |
| Basque BasqueGLUE | eu | 76.4 | 74.1 | 75.2 | [XLM-RoBERTa-large](https://huggingface.co/FacebookAI/xlm-roberta-large) | 82.1 |
| Galician SLI NERC Gold | gl | 73.7 | 73.9 | 73.8 | [XLM-RoBERTa-large](https://huggingface.co/FacebookAI/xlm-roberta-large) | 88.1 |

</details>


## Ethical Considerations and Limitations

Detailed information on the work done to examine the presence of unwanted social and cognitive biases in the base model can be found 
at [Salamandra-7B model card](https://huggingface.co/BSC-LT/salamandra-7b).
With regard to MT models, no specific analysis has yet been carried out in order to evaluate potential biases or limitations in translation accuracy across different languages, dialects, or domains. However, we recognize the importance of identifying and addressing any harmful stereotypes, cultural inaccuracies, or systematic performance discrepancies that may arise in Machine Translation. As such, we plan to continue performing more analyses as we implement the necessary metrics and methods within our evaluation framework [MT-Lens](https://github.com/langtech-bsc/mt-evaluation).
Note that the model has only undergone preliminary instruction tuning. 
We urge developers to consider potential limitations and conduct safety testing and tuning tailored to their specific applications.

## Additional information

### Author
Machine Translation Group, AI Institute, the Barcelona Supercomputing Center (ai_institute_mt@bsc.es).

### Contact
For further information, please send an email to <ai_institute_mt@bsc.es>.

### Copyright
Copyright(c) 2026 by AI Institute, Barcelona Supercomputing Center.

### Funding

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project Desarrollo Modelos ALIA.

This work has been promoted and financed by the Government of Catalonia through the [Aina Project](https://projecteaina.cat/).

### Acknowledgements



### Disclaimer
Be aware that the model may contain biases or other unintended distortions. 
When third parties deploy systems or provide services based on this model, or use the model themselves, 
they bear the responsibility for mitigating any associated risks and ensuring compliance with applicable regulations, including those governing the use of Artificial Intelligence.

The Barcelona Supercomputing Center, as the owner and creator of the model, shall not be held liable for any outcomes resulting from third-party use.

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)


### Citation