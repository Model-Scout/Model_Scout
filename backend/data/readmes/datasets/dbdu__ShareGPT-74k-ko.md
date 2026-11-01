---
language:
- ko
pretty_name: ShareGPT-74k-ko
tags:
- conversation
- chatgpt
- gpt-3.5
license: cc-by-2.0
task_categories:
- text-generation
size_categories:
- 10K<n<100K
---
# ShareGPT-ko-74k
ShareGPT 90k의 cleaned 버전을 구글 번역기를 이용하여 번역하였습니다.\
원본 데이터셋은 [여기](https://github.com/lm-sys/FastChat/issues/90)에서 확인하실 수 있습니다.

Korean-translated version of ShareGPT-90k, translated by Google Translaton.\
You can check the original dataset [here](https://github.com/lm-sys/FastChat/issues/90).


## Dataset Description

json 파일의 구조는 원본 데이터셋과 동일합니다.\
`*_unclneaed.json`은 원본 데이터셋을 번역하고 따로 후처리하지 않은 데이터셋입니다. (총 74k)\
`*_cleaned.json`은 위의 데이터에서 코드가 포함된 데이터를 러프하게 제거한 데이터셋입니다. (총 55k)\
**주의**: 코드는 번역되었을 수 있으므로 cleaned를 쓰시는 걸 추천합니다.

The structure of the dataset is the same with the original dataset.\
`*_unclneaed.json` are Korean-translated data, without any post-processing. (total 74k dialogues)\
`*_clneaed.json` are post-processed version which dialogues containing code snippets are eliminated from. (total 55k dialogues)\
**WARNING**: Code snippets might have been translated into Korean. I recommend you use cleaned files.



## Licensing Information
GPT를 이용한 데이터셋이므로 OPENAI의 [약관](https://openai.com/policies/terms-of-use)을 따릅니다.\
그 외의 경우 [CC BY 2.0 KR](https://creativecommons.org/licenses/by/2.0/kr/)을 따릅니다.

The licensing status of the datasets follows [OPENAI Licence](https://openai.com/policies/terms-of-use) as it contains GPT-generated sentences.\
For all the other cases, the licensing status follows [CC BY 2.0 KR](https://creativecommons.org/licenses/by/2.0/kr/).

## Code
번역에 사용한 코드는 아래 리포지토리에서 확인 가능합니다. Check out the following repository to see the translation code used.\
https://github.com/dubuduru/ShareGPT-translation

You can use the repository to translate ShareGPT-like dataset into your preferred language.