---
license: cc-by-sa-4.0
language:
- ko
- en
---

# **kiqu-70b** [(Arena Leaderboard)](https://huggingface.co/spaces/instructkr/ko-chatbot-arena-leaderboard)
<img src="./kiqu.webp" alt="kiqu-70B" width="390"/>

**kiqu-70b** is a SFT+DPO trained model based on Miqu-70B-Alpaca-DPO using **Korean** datasets.

Since this model is finetune of miqu-1-70b using it on commercial purposes is at your own risk. — leaked early version Mistral-Medium

본 모델 **kiqu-70b**는 Miqu-70B-Alpaca-DPO 모델을 기반으로 **한국어** 데이터셋을 사용하여 SFT+DPO 훈련을 진행하여 제작되었습니다.

베이스 모델인 miqu-1-70b 모델이 미스트랄-미디움의 초기 유출 버전이기에 상업적 사용에 대한 risk는 본인에게 있습니다.

Beside that this model follows **cc-by-sa-4.0**

본 모델 자체로서는 **cc-by-sa-4.0**을 따릅니다.

# **Model Details**

**Base Model**  
miqu-1-70b (Early Mistral-Medium)

**Instruction format**

It follows **Mistral** format.
Giving few-shots to model is highly recommended

본 모델은 미스트랄 포맷을 따릅니다.
few-shot 사용을 적극 권장합니다.
```
[INST] {instruction}
[/INST] {output}
```

Multi-shot
```
[INST] {instruction}
[/INST] {output}

[INST] {instruction}
[/INST] {output}

[INST] {instruction}
[/INST] {output}
.
.
.
```

**Recommended Template** - 1-shot with system prompt
```
너는 kiqu-70B라는 한국어에 특화된 언어모델이야. 깔끔하고 자연스럽게 대답해줘!
[INST] 안녕?
[/INST] 안녕하세요! 무엇을 도와드릴까요? 질문이나 궁금한 점이 있다면 언제든지 말씀해주세요.

[INST] {instruction}
[/INST]
```

Trailing space after [/INST] can affect models performance in significant margin. So, when doing inference it is recommended to not include trailing space in chat template.

[/INST] 뒤에 띄어쓰기는 모델 성능에 유의미한 영향을 미칩니다. 따라서, 인퍼런스(추론)과정에서는 챗 템플릿에 띄어쓰기를 제외하는 것을 적극 권장합니다.

# **Model Benchmark**
TBD


# **Author's Message**

This model's training got sponsered by no one but support from people around Earth.

[Support Me](https://www.buymeacoffee.com/mwell)

[Discord Server](https://discord.gg/MrBt3PXdXc)

Contact Me on Discord - is.maywell

Follow me on twitter - https://twitter.com/stablefluffy