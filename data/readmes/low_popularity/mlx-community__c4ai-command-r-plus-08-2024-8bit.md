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
library_name: transformers
license: cc-by-nc-4.0
tags:
- mlx
inference: false
extra_gated_prompt: By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and
  acknowledge that the information you provide will be collected, used, and shared
  in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy).
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
---

# mlx-community/c4ai-command-r-plus-08-2024-8bit

The Model [mlx-community/c4ai-command-r-plus-08-2024-8bit](https://huggingface.co/mlx-community/c4ai-command-r-plus-08-2024-8bit) was converted to MLX format from [CohereForAI/c4ai-command-r-plus-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024) using mlx-lm version **0.18.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/c4ai-command-r-plus-08-2024-8bit")
response = generate(model, tokenizer, prompt="hello", verbose=True)
```
