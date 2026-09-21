---
base_model: nayohan/llama3-instrucTrans-enko-8b
datasets:
- nayohan/aihub-en-ko-translation-1.2m
- nayohan/translate_corpus_313k
inference: true
language:
- en
- ko
library_name: transformers
license: llama3
metrics:
- sacrebleu
model_creator: nayohan
model_name: llama3-instrucTrans-enko-8b
pipeline_tag: text-generation
quantized_by: afrideva
tags:
- translation
- enko
- ko
- gguf
- ggml
- quantized
---

# llama3-instrucTrans-enko-8b-GGUF

Quantized GGUF model files for [llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b) from [nayohan](https://huggingface.co/nayohan)

## Original Model Card:

# **instructTrans**

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/oRlzxHQy3Qvqf4zfh5Wcj.png)
# **Introduction**

**llama3-8b-instructTrans-en-ko** model is trained on **translation datasets(english->korean)** based on Llama-3-8B-it. To translate the English instruction dataset.
- [nayohan/aihub-en-ko-translation-1.2m](https://huggingface.co/datasets/nayohan/aihub-en-ko-translation-1.2m)
- [nayohan/translate_corpus_313k](https://huggingface.co/datasets/nayohan/translate_corpus_313k)



### **Loading the Model**
Use the following Python code to load the model:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "nayohan/llama3-instrucTrans-enko-8b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
  model_name,
  device_map="auto",
  torch_dtype=torch.bfloat16
)
```

### **Generating Text**
This model supports translation from english to korean. To translate text, use the following Python code: 
```python
system_prompt="당신은 번역기 입니다. 영어를 한국어로 번역하세요."
sentence = "The aerospace industry is a flower in the field of technology and science."
conversation = [{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': sentence}]

inputs = tokenizer.apply_chat_template(
  conversation,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors='pt'
).to("cuda")

outputs = model.generate(inputs, max_new_tokens=4096) # Finetuned with length 4096
print(tokenizer.decode(outputs[0][len(inputs[0]):]))
```
```
# Result
INPUT: <|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n당신은 번역기 입니다. 영어를 한국어로 번역하세요.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nThe aerospace industry is a flower in the field of technology and science.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n
OUTPUT: 항공우주 산업은 기술과 과학 분야의 꽃입니다.<|eot_id|>

INPUT: <|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n당신은 번역기 입니다. 영어를 한국어로 번역하세요.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n
Technical and basic sciences are very important in terms of research. It has a significant impact on the industrial development of a country. Government policies control the research budget.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n
OUTPUT: 기술 및 기초 과학은 연구 측면에서 매우 중요합니다. 이는 한 국가의 산업 발전에 큰 영향을 미칩니다. 정부 정책은 연구 예산을 통제합니다.<|eot_id|>
```
```
# EVAL_RESULT (2405_KO_NEWS) (max_new_tokens=512)
"en_ref":"This controversy arose around a new advertisement for the latest iPad Pro that Apple released on YouTube on the 7th. The ad shows musical instruments, statues, cameras, and paints being crushed in a press, followed by the appearance of the iPad Pro in their place. It appears to emphasize the new iPad Pro's artificial intelligence features, advanced display, performance, and thickness. Apple mentioned that the newly unveiled iPad Pro is equipped with the latest 'M4' chip and is the thinnest device in Apple's history. The ad faced immediate backlash upon release, as it graphically depicts objects symbolizing creators being crushed. Critics argue that the imagery could be interpreted as technology trampling on human creators. Some have also voiced concerns that it evokes a situation where creators are losing ground due to AI."
"ko_ref":"이번 논란은 애플이 지난 7일 유튜브에 공개한 신형 아이패드 프로 광고를 둘러싸고 불거졌다. 해당 광고 영상은 악기와 조각상, 카메라, 물감 등을 압착기로 짓누른 뒤 그 자리에 아이패드 프로를 등장시키는 내용이었다. 신형 아이패드 프로의 인공지능 기능들과 진화된 디스플레이와 성능, 두께 등을 강조하기 위한 취지로 풀이된다. 애플은 이번에 공개한 아이패드 프로에 신형 ‘M4’ 칩이 탑재되며 두께는 애플의 역대 제품 중 가장 얇다는 설명도 덧붙였다. 광고는 공개 직후 거센 비판에 직면했다. 창작자를 상징하는 물건이 짓눌려지는 과정을 지나치게 적나라하게 묘사한 점이 문제가 됐다. 기술이 인간 창작자를 짓밟는 모습을 묘사한 것으로 해석될 여지가 있다는 문제의식이다. 인공지능(AI)으로 인해 창작자가 설 자리가 줄어드는 상황을 연상시킨다는 목소리도 나왔다."

"InstrucTrans":"이번 논란은 애플이 지난 7일 유튜브에 공개한 최신 아이패드 프로 광고를 중심으로 불거졌다. 이 광고는 악기, 조각상, 카메라, 물감 등을 누르기 시작하는 장면과 함께 그 자리에 아이패드 프로가 등장하는 장면을 보여준다. 이는 새로운 아이패드 프로의 인공지능 기능, 고급 디스플레이, 성능, 두께를 강조하는 것으로 보인다. 애플은 이번에 공개한 아이패드 프로에 최신 'M4' 칩이 탑재됐으며, 애플 역사상 가장 얇은 기기라고 언급했다. 이 광고는 출시하자마자 크리에이터를 상징하는 물건이 파쇄되는 장면이 그대로 그려져 논란이 되고 있다. 비평가들은 이 이미지가 기술이 인간 크리에이터를 짓밟는다는 의미로 해석될 수 있다고 주장한다. 또한 AI로 인해 크리에이터들이 밀리고 있다는 상황을 연상시킨다는 우려의 목소리도 나온다."

"KULLM3":"이 논란은 애플이 유튜브에 7일에 발표한 최신 iPad Pro 광고 주위에서 발생했습니다. 광고에서는 악기, 조각상, 카메라, 그리고 물감이 압축기에서 파괴되는 모습이 보여지고, 그 자리에 iPad Pro가 나타납니다. 이는 새로운 iPad Pro의 인공지능 기능, 고급 디스플레이, 성능, 그리고 얇은 디자인을 강조하는 것으로 보입니다. 애플은 최신 'M4' 칩을 탑재한 새로 공개된 iPad Pro가 자사 역사상 가장 얇은 기기라고 언급했습니다. 하지만 광고는 출시 직후 즉각적인 반발을 받았습니다. 광고에서는 창작자를 상징하는 물건들이 파괴되는 모습이 그래픽하게 보여지기 때문입니다. 비판자들은 이 이미지가 기술이 인간 창작자를 압도하는 것으로 해석될 수 있다고 주장하며, 일부는 이가 창작자들이 AI 때문에 지위를 잃는 상황을 연상시킨다고 우려하고 있습니다."
"EEVE-10.8b-it":해당 논란은 애플이 7일에 유튜브에 공개한 최신 아이패드 프로 광고와 관련하여 발생했습니다. 해당 광고에서는 악기, 조각상, 카메라, 그리고 붓이 눌러져 부서지는 모습과 함께 그 자리에 새로운 아이패드 프로가 등장하는 장면을 생생하게 보여주고 있습니다. 이는 새로운 아이패드 프로의 인공지능 기능, 진보된 디스플레이, 성능, 그리고 두께를 부각시키고자 하는 것으로 보입니다. 애플은 갓 발표된 아이패드 프로가 최신 'M4' 칩을 탑재하고 있으며, 애플 제품 중 가장 얇은 장치라고 언급했습니다. 광고가 출시되자마자 바로 뭇매를 맞았는데, 이는 창작자들을 상징하는 물건들이 눌려 부서지는 잔인한 장면을 담고 있기 때문입니다. 비판자들은 이러한 이미지가 기술이 인간 창작자들을 짓밟은 것으로 해석될 수 있다고 주장하고 있습니다. 일부 사람들은 또한 AI로 인해 창작자들이 도태되고 있는 상황을 암시하는 것 같아 우려를 표하고 있습니다."
"Seagull-13B":"이 논란이 발생한 것은 7일에 Apple이 YouTube에 공개한 최신 iPad Pro의 새로운 광고와 관련이 있습니다. 이 광고는 악기, 동상, 카메라, 물감을 프레스에 누르는 장면을 보여준 다음 그 자리에 iPad Pro가 나타납니다. 새로운 iPad Pro의 인공지능 기능, 고급 디스플레이, 성능 및 두께를 강조하는 것으로 보입니다. Apple은 새로 공개 된 iPad Pro에 최신 'M4' 칩이 장착되어 있으며 Apple 역사상 가장 얇은 장치라고 언급했습니다. 이 광고는 크리에이터를 상징하는 물체를 그래픽으로 표현하여 공개 직후 반발을 불러일으켰습니다. 비평가들은 이 이미지가 딥러닝이 인간 창작자를 짓밟는 기술로 해석될 수 있다고 지적합니다. 일부는 AI로 인해 크리에이터가 토대를 잃는 상황을 연상시킨다는 우려의 목소리도 제기했습니다.\n"
"Synatra-7B":"이 논란은 7일 Apple이 YouTube에 올린 최신 iPad Pro의 신규 광고를 중심으로 벌어졌습니다. 이 광고에는 목관악기, 조각상, 카메라, 물감이 압력을 가한 후 그 자리에 iPad Pro가 나타나는 장면이 표시되는 무단장식 광고입니다. 그 광고는 새 iPad Pro의 인공지능 기능, 고급 디스플레이, 성능 및 두께를 강조하는 것으로 보입니다. Apple은 새롭게 발표된 iPad Pro에는 최신 'M4' 칩이 탑재되어 있으며 역사상 가장 얇은 기기라고 언급했습니다. 이 광고는 크리에이터를 상징하는 물체가 짓기에 맞서 있다는 모습을 그래픽으로 표현한 후 즉시 반발을 불러 일으켰습니다. 비평가들은 이 이미지가 기술이 인간 크리에이터를 협박하는 것으로 해석될 수 있다고 주장합니다. 일부는 또한 AI로 인해 크리에이터가 지위를 잃는 상황을 불러일으킬 수 있다고 우려하는 목소리도 있습니다."
"nhndq-nllb":"이 논란은 애플이 7일 유튜브에 공개한 최신 아이패드 프로의 새 광고를 둘러싸고 불거졌다. 광고는 악기, 조각상, 카메라, 페인트 등이 프레스에서 으깨지고 그 자리에 아이패드 프로가 등장하는 모습을 보여준다. 이는 새로운 아이패드 프로의 인공지능 기능과 고급 디스플레이, 성능, 두께 등을 강조하는 것으로 보인다. 애플은 새로 공개된 아이패드 프로가 최신 'M4' 칩을 장착하고 있으며 애플 역사상 가장 얇은 장치라고 언급했다. AI로 인해 즉각"

"our-tech":"이번 논란은 애플이 지난 7일 유튜브에 공개한 최신 아이패드 프로 광고를 둘러싸고 불거졌다. 광고는 악기, 조각상, 카메라, 물감 등을 압착기에 넣어 부숴버리다가 그 자리에 아이패드 프로가 등장하는 것으로, 새로 공개된 아이패드 프로가 최신 'M4'칩을 탑재하고 애플 사상 가장 얇은 기기라는 점을 강조한 것으로 보인다. 광고는 출시 즉시 창작자를 상징하는 물건들이 압착기에 갈겨버리는 장면을 그래픽으로 보여줘, 기술이 인간 창작자를 짓밟는 것으로 해석될 수 있다는 지적과 함께, AI로 인해 창작자들이 지위를 잃어가는 상황을 연상시킨다는 비판이 제기됐다."
"our-general":이번 논란은 애플이 지난 7일 유튜브에 공개한 최신 아이패드 프로 광고를 중심으로 불거졌다. 광고는 악기, 조각상, 카메라, 물감 등을 누르기에 충분한 힘을 가진 프레스에 집어넣고 으깨는 모습을 보여준다. 이어 그 자리에 아이패드 프로가 등장하는 것으로, 새로 공개된 아이패드 프로가 최신 'M4' 칩을 탑재하고 애플 역사상 가장 얇은 기기라는 점을 강조한 것으로 보인다. 이 광고는 공개 직후부터 논란이 일었는데, 창작자를 상징하는 물건들이 으깨지는 장면이 그대로 담겨있어 기술이 창작자를 짓밟는다는 해석이 나올 수 있다는 지적이 나왔다. 또 AI에 밀려 창작자들이 힘을 잃는 상황을 연상시킨다는 우려도 제기됐다."
"our-sharegpt":"7일, Apple이 YouTube에 공개한 최신 iPad Pro의 새로운 광고와 관련하여 논란이 일어났습니다. 이 광고는 악기, 조각상, 카메라, 물감이 프레스에서 부서지는 장면을 보여준 후 그 자리에 iPad Pro가 등장합니다. 새로운 iPad Pro의 인공 지능 기능, 고급 디스플레이, 성능 및 두께를 강조하는 것으로 보입니다. Apple은 새로 공개된 iPad Pro가 최신 'M4' 칩이 탑재되어 있으며 Apple 역사상 가장 얇은 기기라고 언급했습니다. 이 광고는 크리에이터를 상징하는 물체가 부서지는 것을 그래픽으로 묘사하고 있어 출시와 동시에 반발을 불러일으켰습니다. 비평가들은 이 이미지가 기술이 인간 크리에이터를 짓밟는 것으로 해석될 수 있다고 주장합니다. 또한 일부에서는 크리에이터가 인공지능으로 인해 주눅 들고 있는 상황을 연상시킨다고 우려하는 목소리도 있습니다."
```

<br><br>

# **Evalution Result**
영어->한국어 번역 성능을 평가하기위한 데이터셋을 선정하여 평가를 진행하였습니다.

### **평가 데이터셋 출처**
- Aihub/FLoRes: [traintogpb/aihub-flores-koen-integrated-sparta-30k](https://huggingface.co/datasets/traintogpb/aihub-flores-koen-integrated-sparta-30k) | (test set 1k)
- iwslt-2023  : [shreevigneshs/iwslt-2023-en-ko-train-val-split-0.1](https://huggingface.co/datasets/shreevigneshs/iwslt-2023-en-ko-train-val-split-0.1) | (f_test 597, if_test 597)
- ko_news_2024: [nayohan/ko_news_eval40](https://huggingface.co/datasets/nayohan/ko_news_eval40) | (40)

### **모델 평가방법**
- 각 모델은 허깅페이스에 ReadMe에 적혀있는 추론코드를 기반으로 각각 추론하였습니다. (공통: max_new_tokens=512) 
- EEVE는 명령어("당신은 번역기 입니다. 영어를 한국어로 번역하세요.")를 시스템프롬프트에 추가하였고, KULLM3는 기존 시스템프롬프트를 유지하고, 유저의 입력 맨 앞에 추가하였습니다.

<br>

## **Aihub 영-한 번역데이터셋 평가**
* [Aihub 평가 데이터셋](https://huggingface.co/datasets/traintogpb/aihub-flores-koen-integrated-sparta-30k)은 모델들이 학습데이터셋에 포함되었을 수 있습니다. 카테고리별 성능을 확인하는 용도로만 참고해주세요. [[카테고리 설명 링크]](https://huggingface.co/datasets/traintogpb/aihub-koen-translation-integrated-tiny-100k)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/TMo05LOUhPGYNbT2ADOgi.png)
| model            |   aihub-111 |   aihub-124 |   aihub-125 |   aihub-126 |   aihub-563 |   aihub-71265 |   aihub-71266 |   aihub-71382 |   average |
|:-----------------|------------:|------------:|------------:|------------:|------------:|--------------:|--------------:|--------------:|----------:|
| [EEVE-10.8b-it](https://huggingface.co/yanolja/EEVE-Korean-10.8B-v1.0)    |        6.15 |       11.81 |        5.78 |        4.99 |        6.31 |         10.99 |          9.41 |          6.44 |    7.73   |
| [KULLM3](https://huggingface.co/nlpai-lab/KULLM3)           |        9.00 |       13.49 |       10.43 |        5.90 |        1.92 |         16.37 |         10.02 |          8.39 |    9.44   |
| [Seagull-13B](kuotient/Seagull-13b-translation)      |        9.8  |       18.38 |        8.51 |        5.53 |        8.74 |         17.44 |         10.11 |         11.21 |   11.21   |
| [Synatra-7B](maywell/Synatra-7B-v0.3-Translation)       |        6.99 |       25.14 |        7.79 |        5.31 |        9.95 |         19.27 |         13.20 |          8.93 |   12.07   |
| [nhndq-nllb](NHNDQ/nllb-finetuned-en2ko)       |       24.09 |       48.71 |       22.89 |       13.98 |       18.71 |         30.18 |         32.49 |         18.62 |   26.20   |
| [our-tech](nayohan/llama3-8b-it-translation-tech-en-ko-1sent)         |       20.19 |       37.48 |       18.50 |       12.45 |       16.96 |         13.92 |         43.54 |          9.62 |   21.58   |
| [our-general](https://huggingface.co/nayohan/llama3-8b-it-translation-general-en-ko-1sent)      |       24.72 |       45.22 |       21.61 |       18.97 |       17.23 |         30.00 |         32.08 |         13.55 |   25.42   |
| [our-sharegpt](https://huggingface.co/nayohan/llama3-8b-it-translation-sharegpt-en-ko)     |       12.42 |       19.23 |       10.91 |        9.18 |       14.30 |         26.43 |         12.62 |         15.57 |   15.08   |
| **our-instrucTrans** |       24.89 |       47.00 |       22.78 |       21.78 |       24.27 |         27.98 |         31.31 |         15.42 |**26.92**  |
## **FLoRes 영-한 번역데이터셋 평가**
[FloRes](https://huggingface.co/datasets/facebook/flores)는 페이스북에서 공개한 영어와 적은 리소스의 언어 200개에 대해서 병렬로 구성한 번역 벤치마크 데이터셋입니다. 
[traintogpb/aihub-flores-koen-integrated-sparta-30k](https://huggingface.co/datasets/traintogpb/aihub-flores-koen-integrated-sparta-30k)를 활용하여 평가를 진행하였습니다. (한문장 구성)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/ZDeA-7e-0xfXaGOmyS9zs.png)
| model            |   flores-dev |   flores-devtest |   average |
|:-----------------|-------------:|-----------------:|----------:|
| EEVE-10.8b-it    |        10.99 |            11.71 |    11.35  |
| KULLM3           |        12.83 |            13.23 |    13.03  |
| Seagull-13B      |        11.48 |            11.99 |    11.73  |
| Synatra-7B       |        10.98 |            10.81 |    10.89  |
| nhndq-nllb       |        12.79 |            15.15 |    13.97  |
| our-tech         |        12.14 |            12.04 |    12.09  |
| our-general      |        14.93 |            14.58 |    14.75  |
| our-sharegpt     |        14.71 |            16.69 |    15.70  |
| our-instrucTrans |        14.49 |            17.69 | **16.09** |
## **iwslt-2023**
[iwslt-2023 데이터셋](https://huggingface.co/datasets/shreevigneshs/iwslt-2023-en-ko-train-val-split-0.1)은 동일한 영어문장을 각각 반말, 존댓말의 한국어로 평가데이터셋이 구성되어 있습니다. 모델의 존대/반말 경향을 상대적으로 확인할 수 있습니다. (한문장 구성)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/UJvuCnbjWokBWQNhD4L63.png)
| model            |         iwslt_zondae |      iwslt_banmal |   average |
|:-----------------|---------------------:|------------------:|----------:|
| EEVE-10.8b-it    |                 4.62 |              3.79 |     4.20  |
| KULLM3           |                 5.94 |              5.24 |     5.59  |
| Seagull-13B      |                 6.14 |              4.54 |     5.34  |
| Synatra-7B       |                 5.43 |              4.73 |     5.08  |
| nhndq-nllb       |                 8.36 |              7.44 |  **7.90** |
| our-tech         |                 3.99 |              3.95 |     3.97  |
| our-general      |                 7.33 |              6.18 |     6.75  |
| our-sharegpt     |                 7.83 |              6.35 |     7.09  |
| our-instrucTrans |                 8.63 |              6.97 |     7.80  |
## **ko_news_eval40**
[ko_news_eval40 데이터셋](https://huggingface.co/datasets/nayohan/ko_news_eval40)은 학습되지 않았을 새로운 데이터셋에 평가하고자 24년5월 뉴스를 각 카테고리(4) 별 10개씩 기사 내 문단 일부를 수집하고, GPT4로 번역하여 구성하였습니다.
영어를 일상뉴스에 사용되는 한국어로 잘 번역하는지를 평가합니다. (문단 구성)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/OaE5z_yQT9sIIz0zsn644.png)
| model            |   IT/과학 |   경제 |   사회 |   오피니언  |   average |
|:-----------------|----------:|-------:|-------:|------------:|----------:|
| EEVE-10.8b-it    |      9.03 |   6.42 |   5.56 |        5.10 |    6.52   |
| KULLM3           |      9.82 |   5.26 |   3.48 |        7.48 |    6.51   |
| Seagull-13B      |      7.41 |   6.78 |   4.76 |        4.85 |    5.95   |
| Synatra-7B       |     11.44 |   5.59 |   4.57 |        6.31 |    6.97   |
| nhndq-nllb       |     11.97 |  11.12 |   6.14 |        5.28 |    8.62   |
| our-tech         |     10.45 |   9.98 |   5.13 |       10.15 |    8.92   |
| our-general      |     16.22 |  10.61 |   8.51 |        7.33 |   10.66   |
| our-sharegpt     |     12.71 |   8.06 |   7.70 |        6.43 |    8.72   |
| our-instrucTrans |     20.42 |  12.77 |  11.40 |       10.31 |**13.72**  |
## **Average**
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6152b4b9ecf3ca6ab820e325/bf2qjeg-03WRVTIbqvG7C.png)
| model            |   aihub |   flores |   iwslt |    news |   average |
|:-----------------|--------:|---------:|--------:|--------:|----------:|
| [EEVE-10.8b-it](https://huggingface.co/yanolja/EEVE-Korean-10.8B-v1.0)    |  7.73   |   11.35  |   4.20  |  6.52   |   7.45    |
| [KULLM3](https://huggingface.co/nlpai-lab/KULLM3)           |  9.44   |   13.03  |   5.59  |  6.51   |   8.64    |
| [Seagull-13B](kuotient/Seagull-13b-translation)      | 11.21   |   11.73  |   5.34  |  5.95   |   8.56    |
| [Synatra-7B](maywell/Synatra-7B-v0.3-Translation)       | 12.07   |   10.89  |   5.08  |  6.97   |   8.75    |
| [nhndq-nllb](NHNDQ/nllb-finetuned-en2ko)       | 26.20   |   13.97  |**7.90** |  8.62   |  14.17    |
| [our-tech](nayohan/llama3-8b-it-translation-tech-en-ko-1sent)         | 21.58   |   12.09  |   3.97  |  8.92   |  11.64    |
| [our-general](https://huggingface.co/nayohan/llama3-8b-it-translation-general-en-ko-1sent)      | 25.42   |   14.75  |   6.75  | 10.66   |  14.40    |
| [our-sharegpt](https://huggingface.co/nayohan/llama3-8b-it-translation-sharegpt-en-ko)     | 15.08   |   15.70  |   7.09  |  8.72   |  11.64    |
| **our-instrucTrans** |**26.92**| **16.09**|   7.80  |**13.72**| **16.13** |
### **Citation**
```bibtex
@article{InstrcTrans8b,
  title={llama3-instrucTrans-enko-8b},
  author={Na, Yohan},
  year={2024},
  url={https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b}
}
```
```bibtex
@article{llama3modelcard,
        title={Llama 3 Model Card},
        author={AI@Meta},
        year={2024},
        url={https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```