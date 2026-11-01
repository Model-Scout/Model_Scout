---
task_categories:
- text-generation
language:
- en 
- zh 
- ko 
- es 
- fr 
- ja 
- de 
- pt 
- ru 
- it 
- id 
- vi 
- nl 
- pl 
- tr 
- cs 
- he 
- uk 
---
# openchat/openchat_sharegpt4_dataset

- This is a processed version of `sharegpt_clean.json` from [openchat/openchat_sharegpt4_dataset](https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset).
- Unfortunately, there's not much information about that dataset on Huggingface and GitHub.

Changes:
- Corrected turn order
- Added `language` field for detected language
- Removed duplicates
- Redacted URLs, e-mails, phone numbers
- Shuffled

| Language code | Number of rows |
|---------------|----------------:|
| en            | 54288          |
| zh            | 8966           |
| ko            | 2928           |
| es            | 2193           |
| fr            | 1885           |
| ja            | 1402           |
| de            | 823            |
| pt            | 755            |
| ru            | 507            |
| it            | 483            |
| id            | 383            |
| vi            | 240            |
| nl            | 196            |
| pl            | 192            |
| tr            | 141            |
| cs            | 132            |
| he            | 120            |
| uk            | 107            |

Other languages have fewer than 100 rows each.