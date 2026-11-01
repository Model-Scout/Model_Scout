---
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
extra_gated_prompt: "By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll receive email updates about Cohere Labs and Cohere research, events, products and services. You can unsubscribe at any time." 
extra_gated_fields:
 Name: text
 Affiliation: text
 Country:
    type: select
    options: 
      - Aruba
      - Afghanistan
      - Angola
      - Anguilla
      - Åland Islands
      - Albania
      - Andorra
      - United Arab Emirates
      - Argentina
      - Armenia
      - American Samoa
      - Antarctica
      - French Southern Territories
      - Antigua and Barbuda
      - Australia
      - Austria
      - Azerbaijan
      - Burundi
      - Belgium
      - Benin
      - Bonaire Sint Eustatius and Saba
      - Burkina Faso
      - Bangladesh
      - Bulgaria
      - Bahrain
      - Bahamas
      - Bosnia and Herzegovina
      - Saint Barthélemy
      - Belarus
      - Belize
      - Bermuda
      - Plurinational State of Bolivia
      - Brazil
      - Barbados
      - Brunei-Darussalam
      - Bhutan
      - Bouvet-Island
      - Botswana
      - Central African Republic
      - Canada
      - Cocos (Keeling) Islands
      - Switzerland
      - Chile
      - China
      - Côte-dIvoire
      - Cameroon
      - Democratic Republic of the Congo
      - Cook Islands
      - Colombia
      - Comoros
      - Cabo Verde
      - Costa Rica
      - Cuba
      - Curaçao
      - Christmas Island
      - Cayman Islands
      - Cyprus
      - Czechia
      - Germany
      - Djibouti
      - Dominica
      - Denmark
      - Dominican Republic
      - Algeria
      - Ecuador
      - Egypt
      - Eritrea
      - Western Sahara
      - Spain
      - Estonia
      - Ethiopia
      - Finland
      - Fiji
      - Falkland Islands (Malvinas)
      - France
      - Faroe Islands
      - Federated States of Micronesia
      - Gabon
      - United Kingdom
      - Georgia
      - Guernsey
      - Ghana
      - Gibraltar
      - Guinea
      - Guadeloupe
      - Gambia
      - Guinea Bissau
      - Equatorial Guinea
      - Greece
      - Grenada
      - Greenland
      - Guatemala
      - French Guiana
      - Guam
      - Guyana
      - Hong Kong
      - Heard Island and McDonald Islands
      - Honduras
      - Croatia
      - Haiti
      - Hungary
      - Indonesia
      - Isle of Man
      - India
      - British Indian Ocean Territory
      - Ireland
      - Islamic Republic of Iran
      - Iraq
      - Iceland
      - Israel
      - Italy
      - Jamaica
      - Jersey
      - Jordan
      - Japan
      - Kazakhstan
      - Kenya
      - Kyrgyzstan
      - Cambodia
      - Kiribati
      - Saint-Kitts-and-Nevis
      - South Korea
      - Kuwait
      - Lao-Peoples-Democratic-Republic
      - Lebanon
      - Liberia
      - Libya
      - Saint-Lucia
      - Liechtenstein
      - Sri Lanka
      - Lesotho
      - Lithuania
      - Luxembourg
      - Latvia
      - Macao
      - Saint Martin (French-part)
      - Morocco
      - Monaco
      - Republic of Moldova
      - Madagascar
      - Maldives
      - Mexico
      - Marshall Islands
      - North Macedonia
      - Mali
      - Malta
      - Myanmar
      - Montenegro
      - Mongolia
      - Northern Mariana Islands
      - Mozambique
      - Mauritania
      - Montserrat
      - Martinique
      - Mauritius
      - Malawi
      - Malaysia
      - Mayotte
      - Namibia
      - New Caledonia
      - Niger
      - Norfolk Island
      - Nigeria
      - Nicaragua
      - Niue
      - Netherlands
      - Norway
      - Nepal
      - Nauru
      - New Zealand
      - Oman
      - Pakistan
      - Panama
      - Pitcairn
      - Peru
      - Philippines
      - Palau
      - Papua New Guinea
      - Poland
      - Puerto Rico
      - North Korea
      - Portugal
      - Paraguay
      - State of Palestine
      - French Polynesia
      - Qatar
      - Réunion
      - Romania
      - Russia
      - Rwanda
      - Saudi Arabia
      - Sudan
      - Senegal
      - Singapore
      - South Georgia and the South Sandwich Islands
      - Saint Helena Ascension and Tristan da Cunha
      - Svalbard and Jan Mayen
      - Solomon Islands
      - Sierra Leone
      - El Salvador
      - San Marino
      - Somalia
      - Saint Pierre and Miquelon
      - Serbia
      - South Sudan
      - Sao Tome and Principe
      - Suriname
      - Slovakia
      - Slovenia
      - Sweden
      - Eswatini
      - Sint Maarten (Dutch-part)
      - Seychelles
      - Syrian Arab Republic
      - Turks and Caicos Islands
      - Chad
      - Togo
      - Thailand
      - Tajikistan
      - Tokelau
      - Turkmenistan
      - Timor Leste
      - Tonga
      - Trinidad and Tobago
      - Tunisia
      - Turkey
      - Tuvalu
      - Taiwan 
      - United Republic of Tanzania
      - Uganda
      - Ukraine
      - United States Minor Outlying Islands
      - Uruguay
      - United-States
      - Uzbekistan
      - Holy See (Vatican City State)
      - Saint Vincent and the Grenadines
      - Bolivarian Republic of Venezuela
      - Virgin Islands British
      - Virgin Islands U.S.
      - VietNam
      - Vanuatu
      - Wallis and Futuna
      - Samoa
      - Yemen
      - South Africa
      - Zambia
      - Zimbabwe
 
 I agree to use this model for non-commercial use ONLY: checkbox
---

# Model Card for Aya-23-8B

**Note:** This is an older version of Aya. The latest version is Aya Expanse 8B which is available [here](https://huggingface.co/CohereLabs/aya-expanse-8b). We also have multimodal variant, Aya Vision 8B which is available [here](https://huggingface.co/CohereLabs/aya-vision-8b).

**Try Aya Expanse and Aya Vision:**

You can try out latest Aya models before downloading the weights in our hosted Hugging Face Space [here](https://huggingface.co/spaces/CohereLabs/aya_expanse).

## Model Summary

Aya 23 is an open weights research release of an instruction fine-tuned model with highly advanced multilingual capabilities. Aya 23 focuses on pairing a highly performant pre-trained [Command family](https://huggingface.co/CohereLabs/c4ai-command-r-plus) of models with the recently released [Aya Collection](https://huggingface.co/datasets/CohereLabs/aya_collection). The result is a powerful multilingual large language model serving 23 languages.

This model card corresponds to the 8-billion version of the Aya 23 model. We also released a 35-billion version which you can find [here](https://huggingface.co/CohereLabs/aya-23-35B).

We cover 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

Developed by: [Cohere Labs](https://cohere.for.ai) and [Cohere](https://cohere.com/) 

- Point of Contact: Cohere Labs: [cohere.for.ai](https://cohere.for.ai/)
- License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
- Model: aya-23-8B
- Model Size: 8 billion parameters

### Usage

Please install transformers from the source repository that includes the necessary changes for this model

```python
# pip install transformers==4.41.1
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereLabs/aya-23-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the command-r-plus chat template
messages = [{"role": "user", "content": "Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
## <BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>

gen_tokens = model.generate(
    input_ids, 
    max_new_tokens=100, 
    do_sample=True, 
    temperature=0.3,
    )

gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

### Example Notebook

[This notebook](https://huggingface.co/CohereLabs/aya-23-8B/blob/main/Aya_23_notebook.ipynb) showcases a detailed use of Aya 23 (8B) including inference and fine-tuning with [QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes). 

## Model Details

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: Aya-23-8B is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model is fine-tuned (IFT) to follow human instructions.

**Languages covered**: The model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

**Context length**: 8192

### Evaluation

<img src="./assets/benchmarks.png" alt="multilingual benchmarks" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="./assets/winrates.png" alt="average win rates" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

Please refer to the [Aya 23 technical report](https://cohere.com/research/papers/aya-command-23-8b-and-35b-technical-report-2024-05-23) for further details about the base model, data, instruction tuning, and evaluation.

### Model Card Contact

For errors or additional questions about details in this model card, contact labs@cohere.com

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant multilingual model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).

### Try the model today

You can try Aya 23 in the Cohere [playground](https://dashboard.cohere.com/playground/chat) here. You can also use it in our dedicated Hugging Face Space [here](https://huggingface.co/spaces/CohereLabs/aya-23).

### Citation info
```bibtex
@misc{aryabumi2024aya,
      title={Aya 23: Open Weight Releases to Further Multilingual Progress}, 
      author={Viraat Aryabumi and John Dang and Dwarak Talupuru and Saurabh Dash and David Cairuz and Hangyu Lin and Bharat Venkitesh and Madeline Smith and Kelly Marchisio and Sebastian Ruder and Acyr Locatelli and Julia Kreutzer and Nick Frosst and Phil Blunsom and Marzieh Fadaee and Ahmet Üstün and Sara Hooker},
      year={2024},
      eprint={2405.15032},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```