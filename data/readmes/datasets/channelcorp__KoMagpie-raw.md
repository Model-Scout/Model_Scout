---
language:
- ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: model
    dtype: string
  splits:
  - name: train
    num_bytes: 3720289639
    num_examples: 2569865
  download_size: 2087068614
  dataset_size: 3720289639
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

<div style="max-width: 350px; margin: 0 auto;">
<img src='https://huggingface.co/datasets/channelcorp/KoMagpie-raw-preview/resolve/main/komagpie_logo.png' />
</div>

# KoMagpie-raw-preview 🐦

This is the first, preview version of 🐦 KoMagpie dataset.

## How to use

```python
>>> from datasets import load_dataset

>>> ds = load_dataset("channelcorp/komagpie-raw-preview", split="train")
>>> ds
Dataset({
    features: ['instruction', 'output', 'model'],
    num_rows: 487171
})
```


```python
>>> ds[0]
{'instruction': '안녕하세요? 저는 마케팅 매니저로 일하면서 새로운 소비자 트렌드를 파악하기 위해 노력하고 있습니다. 이와 관련해 도움이 될 만한 영어 자료를 찾아주실 수 있나요?',
 'output': '안녕하세요! 물론이죠, 적절한 리소스를 찾는 것은 중요합니다. 이 밑에 있는 사이트들은 마케팅 및 소비자 트렌드에 관한 최신 정보를 제공하는 곳들입니다:\n\n1. **eMarketer:** 이 사이트는 디지털 마케팅, 미디어, 그리고 전자상거래의 세계적인 트렌드를 분석합니다. (www.emarketer.com)\n\n2. **Marketing Dive:** 이 웹사이트는 일상적인 비즈니스 뉴스와 마케팅 업계의 트렌드를 포함합니다. (www.marketingdive.com)\n\n3. **HubSpot:** 이 조직은 새로운 디지털 마케팅 트렌드와 그들의 인플루언스에 대한 광범위한 정보를 제공합니다. 또한 리소스, 툴 및 트레이닝을 제공합니다. (www.hubspot.com)\n\n4. **Adweek:** 광고, 디지털 마케팅, 미디어 트렌드를 설명하는 자료를 제공합니다. (www.adweek.com)\n\n5. **Nielsen:** 이 사이트는 전세계의 소비자 행동에 대한 통찰을 제공합니다. ((www.nielsen.com)\n\n6. **Trend Hunter:** 아이디어, 트렌드, 그리고 방대한 혁신에 관한 세계 최대의 웹사이트입니다. (www.trendhunter.com)\n\n Parses는 더 많은 정보가 필요하시다면 무언가를 명확히 말씀해주시면 감사하겠습니다.',
 'model': 'Qwen/Qwen2-72B-Instruct'}
```

### Development Process
We followed [Magpie's process](https://github.com/magpie-align/magpie) to create a Korean version.

1. Generate instruction data using BOS token

```python
payload = {
    "model": "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct",
    "prompt": "[|system|]You are a helpful assistant.[|endofturn|]\n[|Korean user|]", # we used [|Korean user|] instead of [|user|] to gather Korean Instructions
    "stream": False,
    "n": 128,
    "max_tokens": 128,
    "stop": ["\n", "**", "|"]
}
```

We used [LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct) model to generate instruction part of the dataset,
following Magpie's method.

2. Deduplicate using Exact Match
3. Generate output part using open LLMs

We used [Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct) model to generate output part of the dataset, while limiting within single turn.


## License
- Qwen/Qwen2-72B-Instruct : https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/LICENSE
- LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct : https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct/blob/main/LICENSE


## Disclaimer
This is not an officially supported Channel Corp product.


## Acknowledgement
This research is supported by **TPU Research Cloud program**.