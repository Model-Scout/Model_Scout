---
base_model: Qwen/Qwen2.5-1.5B-Instruct
datasets: lemon-mint/korean-reasoning-v02
library_name: transformers
model_name: Qwen2.5-1.5B-Open-R1-Distill-ko
tags:
- generated_from_trainer
- open-r1
- trl
- sft
licence: license
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---

# Model Card for Qwen2.5-1.5B-Open-R1-Distill-ko

This model is a fine-tuned version of [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) on the [lemon-mint/korean-reasoning-v02](https://huggingface.co/datasets/lemon-mint/korean-reasoning-v02) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "프랑스의 수도는?"
generator = pipeline("text-generation", model="whooray/Qwen2.5-1.5B-Open-R1-Distill-ko", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
<think>\n먼저 프랑스 수도를 알아봐야겠어요. 프랑스는 잘 알려진 유럽 국가 중 하나인데 수도를 알려주면 더 편하겠죠. 주요 귀족과 수도는 오스만 식민지와 무역의 중심지였던 아름디라는 지역에 있었다는 말이 있던데, 최근에는 오타냐 근처에 있는 파리가 수도로 통일되었을 거예요. 이렇게 논란이 있었던 걸로 기억하는데, 독일이나 이집트, 이스라엘 같은 국가들도 수도로 다른 지역을 사용했던 경우가 있었음을 알고 있어요. 프랑스는 CIA 월스트리트 journal에서 프랑스 수도는 파리가 아닐 거라고 말한 적 있을까요? 최근 대부분의 관측나라들이 파리로 인정하고 있으므로 정확한지 확인이 필요할 것 같아요. 하지만 프랑스에서 수도가 변했는지, 아니면 옛 수도가 현재 정부 인근에 있는지 궁금하네요. 아마도 1962년 제5공화국에서령으로 습격된 곳을 포함한 모든 정부 기관이 파리를 중심으로 하는 교두보 역할을 하게 된 걸로 알고 있어요. 특별히 역사적으로 정당한 주장을 사용해 개통 가능한 답변을 완성해야겠는데요. \n</think>\n\n프랑스의 수도는 **파리(Paris)**예요. 역사적으로 수도 역할을 하지 못했던 지점에 위치한 프랑스 비국민대책 정부를 중심으로 한 정권이 1944년에 백제온을 탈환하여 새로운 수도로 지정하며 최종적으로 확립되었어요.\n\n### 프랑스 수도 교체의 주요 이유  \n당시 연합군의 인도주의 의지를 반영한 조치였어요. 1932년 17개 연합군 단체가 파리 기지를 공유하면서 공식적인 수도 기능을 잃었다는 점에서 '특허 수도'로 검열되며 미국, 일본 등 유럽 국가들 중 파리를 중심으로 한 정부 주도의 통치가 유려되어 표준화되었죠.  \n> **비유**: 프랑스 수도는
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/llm-est/huggingface/runs/mrisof65) 


This model was trained with SFT.

### Framework versions

- TRL: 0.15.0.dev0
- Transformers: 4.49.0.dev0
- Pytorch: 2.5.1
- Datasets: 3.2.0
- Tokenizers: 0.21.0

## Citations



Cite TRL as:
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallouédec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```