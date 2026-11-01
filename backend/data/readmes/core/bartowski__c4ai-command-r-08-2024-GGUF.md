---
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
license: cc-by-nc-4.0
library_name: transformers
extra_gated_prompt: "By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and acknowledge that the information you provide will be collected, used, and shared in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy)." 
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
 Receive email updates on C4AI and Cohere research, events, products and services?:
   type: select
   options: 
     - Yes
     - No
 I agree to use this model for non-commercial use ONLY: checkbox
quantized_by: bartowski
pipeline_tag: text-generation
base_model: CohereForAI/c4ai-command-r-08-2024
---

## Llamacpp imatrix Quantizations of c4ai-command-r-08-2024

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3634">b3634</a> for quantization.

Original model: https://huggingface.co/CohereForAI/c4ai-command-r-08-2024

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>{system_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [c4ai-command-r-08-2024-f16.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/tree/main/c4ai-command-r-08-2024-f16) | f16 | 64.60GB | true | Full F16 weights. |
| [c4ai-command-r-08-2024-Q8_0.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q8_0.gguf) | Q8_0 | 34.33GB | false | Extremely high quality, generally unneeded but max available quant. |
| [c4ai-command-r-08-2024-Q6_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q6_K_L.gguf) | Q6_K_L | 27.01GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [c4ai-command-r-08-2024-Q6_K.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q6_K.gguf) | Q6_K | 26.51GB | false | Very high quality, near perfect, *recommended*. |
| [c4ai-command-r-08-2024-Q5_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_K_L.gguf) | Q5_K_L | 23.56GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [c4ai-command-r-08-2024-Q5_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_K_M.gguf) | Q5_K_M | 23.05GB | false | High quality, *recommended*. |
| [c4ai-command-r-08-2024-Q5_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_K_S.gguf) | Q5_K_S | 22.49GB | false | High quality, *recommended*. |
| [c4ai-command-r-08-2024-Q4_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_K_L.gguf) | Q4_K_L | 20.31GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [c4ai-command-r-08-2024-Q4_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_K_M.gguf) | Q4_K_M | 19.80GB | false | Good quality, default size for must use cases, *recommended*. |
| [c4ai-command-r-08-2024-Q4_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_K_S.gguf) | Q4_K_S | 18.85GB | false | Slightly lower quality with more space savings, *recommended*. |
| [c4ai-command-r-08-2024-Q4_0.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_0.gguf) | Q4_0 | 18.78GB | false | Legacy format, generally not worth using over similarly sized formats |
| [c4ai-command-r-08-2024-Q4_0_8_8.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_0_8_8.gguf) | Q4_0_8_8 | 18.72GB | false | Optimized for ARM and CPU inference, much faster than Q4_0 at similar quality. |
| [c4ai-command-r-08-2024-Q4_0_4_8.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_0_4_8.gguf) | Q4_0_4_8 | 18.72GB | false | Optimized for ARM and CPU inference, much faster than Q4_0 at similar quality. |
| [c4ai-command-r-08-2024-Q4_0_4_4.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_0_4_4.gguf) | Q4_0_4_4 | 18.72GB | false | Optimized for ARM and CPU inference, much faster than Q4_0 at similar quality. |
| [c4ai-command-r-08-2024-Q3_K_XL.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_XL.gguf) | Q3_K_XL | 18.07GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [c4ai-command-r-08-2024-IQ4_XS.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ4_XS.gguf) | IQ4_XS | 17.83GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [c4ai-command-r-08-2024-Q3_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_L.gguf) | Q3_K_L | 17.56GB | false | Lower quality but usable, good for low RAM availability. |
| [c4ai-command-r-08-2024-Q3_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_M.gguf) | Q3_K_M | 16.23GB | false | Low quality. |
| [c4ai-command-r-08-2024-IQ3_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ3_M.gguf) | IQ3_M | 15.24GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [c4ai-command-r-08-2024-Q3_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_S.gguf) | Q3_K_S | 14.71GB | false | Low quality, not recommended. |
| [c4ai-command-r-08-2024-IQ3_XS.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ3_XS.gguf) | IQ3_XS | 14.05GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [c4ai-command-r-08-2024-Q2_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q2_K_L.gguf) | Q2_K_L | 13.32GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [c4ai-command-r-08-2024-Q2_K.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q2_K.gguf) | Q2_K | 12.81GB | false | Very low quality but surprisingly usable. |
| [c4ai-command-r-08-2024-IQ2_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ2_M.gguf) | IQ2_M | 11.61GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [c4ai-command-r-08-2024-IQ2_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ2_S.gguf) | IQ2_S | 10.79GB | false | Low quality, uses SOTA techniques to be usable. |
| [c4ai-command-r-08-2024-IQ2_XS.gguf](https://huggingface.co/bartowski/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-IQ2_XS.gguf) | IQ2_XS | 10.31GB | false | Low quality, uses SOTA techniques to be usable. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/c4ai-command-r-08-2024-GGUF --include "c4ai-command-r-08-2024-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/c4ai-command-r-08-2024-GGUF --include "c4ai-command-r-08-2024-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (c4ai-command-r-08-2024-Q8_0) or download them all in place (./)

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski

