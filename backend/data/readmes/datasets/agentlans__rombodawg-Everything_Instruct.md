---
license: apache-2.0
task_categories:
- text-generation
language:
- en
- ur
- zh
- ko
- la
- ru
- fr
- es
- de
- it
- ja
- pt
- tr
- ro
- fi
- cs
- fa
- ar
- uk
- nl
- pl
- sh
- ca
tags:
- sft
- instruct
---
# Everything-Instruct: Supervised Finetuning Dataset

![Enhanced giant llama floating in space](BigLlama.jpg "Enhanced giant llama floating in space")

This dataset contains over 7&thinsp;000&thinsp;000 instruction-response pairs for supervised fine-tuning large language models.

It combines the following datasets:
- [rombodawg/Everything_Instruct](https://huggingface.co/datasets/rombodawg/Everything_Instruct)
- [rombodawg/Everything_Instruct_Multilingual](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual)

It can be used for:
- Improving code generation and debugging  
- Enhancing creative writing
- Improving general instruction following
- For English and many other languages

## Processing

- Removing duplicate rows. There was a lot of overlap between the two source datasets.
- Redacting sensitive data (URLs, emails, phone numbers) using [Trufflehog](https://github.com/trufflesecurity/trufflehog) and custom regex patterns
- Unicode normalization
- Language annotation using the Python `fasttext` package

| Language code | Number of rows |
|---------------|----------------:|
| en            | 5584156        |
| ur            | 1120182        |
| zh            | 679979         |
| ko            | 165658         |
| la            | 88678          |
| ru            | 47596          |
| fr            | 27888          |
| es            | 18532          |
| de            | 9005           |
| it            | 6635           |
| ja            | 5290           |
| pt            | 5225           |
| tr            | 4464           |
| ro            | 3892           |
| fi            | 3574           |
| cs            | 2522           |
| fa            | 2160           |
| ar            | 1692           |
| uk            | 1633           |
| nl            | 1358           |
| pl            | 1204           |
| sh            | 1190           |
| ca            | 1040           |

- Other languages have fewer than 1000 rows.
- It's an unusual distribution of languages with many detected Urdu and Latin rows which should be investigated.

## Limitations

- Occasional mangled code due to the preprocessing
- Irregular formatting and spacing from the original dataset 
- Does not include multi-turn conversations
- May not be as diverse as other instruction datasets due to its coding and translation focus
- Most instructions and input are given in English
- Sources for the prompts and answers not provided in the original datasets

## Licence

Apache 2.0 like the original datasets

The cover image is a modified version of [rombodawg/Everything_Instruct](https://huggingface.co/datasets/rombodawg/Everything_Instruct) using Google Gemini Nano-Banana Pro,
and manually edited in GIMP.