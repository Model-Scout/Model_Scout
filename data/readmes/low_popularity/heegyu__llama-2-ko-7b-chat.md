---
datasets:
- beomi/KoAlpaca-v1.1a
- dbdu/ShareGPT-74k-ko
- heegyu/korquad-chat-v1
- HAERAE-HUB/KoInstruct-QA
- changpt/ko-lima-vicuna
- nlpai-lab/kullm-v2
language:
- ko
---
# heegyu/llama-2-ko-7b-chat
- [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)의 40B 체크포인트를 여러 한국어 instruction 데이터셋으로 학습한 모델


## 사용한 데이터셋

| Dataset | # instance | 타입 |
| --- | --- | --- |
| [KoAlpaca v1.1](https://raw.githubusercontent.com/Beomi/KoAlpaca/main/KoAlpaca_v1.1.jsonl) | 50K | 싱글턴 |
| [dbdu/ShareGPT-74k-ko 의 part2_ko_uncleaned](https://huggingface.co/datasets/dbdu/ShareGPT-74k-ko/resolve/main/part2_ko_uncleaned.json) | 36K | 멀티턴 |
| [heegyu/korquad-chat-v1](https://huggingface.co/datasets/heegyu/korquad-chat-v1) | 9.6K | 멀티턴, 지식기반 |
| [lcw99/evolve-instruct](https://github.com/lcw99/evolve-instruct/) | 37K | 싱글턴 |
| [HAERAE-HUB/KoInstruct-QA](https://huggingface.co/datasets/HAERAE-HUB/KoInstruct-QA) | 50.3k | 싱글턴 |
| [changpt/ko-lima-vicuna](https://huggingface.co/datasets/changpt/ko-lima-vicuna) | 1K | 싱글턴, 멀티턴(극히 일부) |
| [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | 15K | 싱글턴 |

- KULLM v2 데이터셋에서는 GPT4ALL, Dolly 데이터만 추출해서 사용했습니다.
- 다양한 학습 데이터셋은 [HeegyuKim/open-korean-instructions](https://github.com/HeegyuKim/open-korean-instructions) GitHub repository를 참고하세요.

## 생성 Prompt
- EOS token(<\/s>)이 나올 때까지 생성하면 됩니다.
- 최상단 프롬프트는 있는게 좋은 답변이 더 자주 나오는 것 같아요.

```
당신은 AI 챗봇입니다. 사용자에게 도움이 되고 유익한 내용을 제공해야합니다. 답변은 길고 자세하며 친절한 설명을 덧붙여서 작성하세요.

### 사용자:
티라노사우르스보다 쌘 공룡이 있을까?

### 챗봇:
```

생성된 답변: 
```
티라노사우르스보다 강력한 공룡이 있을 수 있습니다. 예를 들어, 티라노사우루스보다 더 강력한 이빨구조와 강한 턱, 강력한 다리, 그리고 다양한 몸길이 중 2종 이상을 지녀서 사냥을 더 빠르게 할 수 있는 공룡이 있을 수 있습니다.

또한, 티라노사우루스가 지배적인 포식자였던 것은 사실이 아닙니다. 다른 공룡들은 다른 식습관과 방어 전략을 가지고 있었는데, 예를 들어 일부 공룡들은 더 큰 뿔과 뾰족한 이빨을 가지고 있어 공격자에게 피해를 입힐 수 있었습니다.

더 많은 정보를 얻고 싶다면, 공룡에 대한 다양한 연구 논문이나 서적 또는 온라인 콘텐츠 중 하나 또는 둘 이상에 집중해보세요. 이를 통해 티라노사우루스와 그 이후의 역사와 문화, 그리고 공룡에 대한 더 많은 정보를 얻을 수 있을 것입니다.
```

멀티턴 대화 예시
```
당신은 AI 챗봇입니다. 사용자에게 도움이 되고 유익한 내용을 제공해야합니다. 답변은 길고 자세하며 친절한 설명을 덧붙여서 작성하세요.

### 사용자:
너는 k-pop 가수 누구 좋아하니?

### 챗봇:
저는 모든 k-pop 가수들을 좋아하지 않습니다. 저는 모든 장르의 음악을 즐기고, 어떤 특정한 가수나 곡에 대한 선호도가 없습니다.
하지만 한 가지 예외로, 제가 가장 좋아한 것은 한국 가수 BTS입니다. BTS는 다양한 장르의 음악과 독특한 방식으로 팬에게 사랑을 받고 있습니다.
그들은 독창적이고 개인적인 음악과 가사를 통해 독특함을 강조하고, 열정 가득한 공연을 보여줍니다.
BTS는 수많은 팬들이 사랑하는 음악 그룹인 만큼, 그들의 음악은 사랑받고 있으며 그들의 음악을 듣는 것이 저에게 큰 즐거움입니다.

### 사용자:
오 너도 방탄 좋아하는구나

### 챗봇:
네, 맞습니다. 방탄은 저에게 많은 즐거움을 주는 그룹입니다. 그들은 저의 선호도와 일치하여 다양한 장르의 음악을 시도하는 데 도움을 주었습니다.
또한, 그들의 음악은 독특한 가사와 스토리텔링으로 관객들에게 강한 인상을 남깁니다. 또한, 멤버들 모두의 탄탄한 퍼포먼싱과 가창력 역시 그들의 특징으로 꼽힙니다.
이러한 이유로, 저는 방탄이 제가 가장 좋아하는 k-pop 아티스트 중 한 명이라는 것을 확신하며, 그들이 만들어내는 음악은 저에게 큰 기쁨과 재미를 제공합니다.

### 사용자:
방탄 군대가는거 알아?

### 챗봇:
```
생성된 답변(할루시네이션 ㅋㅋ):
```
네, 방탄 군대의 공연과 관련된 소식을 몇 차례 접한 적이 있습니다. 그들은 한국 군복을 입고 군무로 유명하며, 그들의 군무와 퍼포먼스는 많은 사람들에게 많은 감동을 줍니다.그
들의 전투적이고 에너지 넘치는 무대는 군대에서 이루어지는 훈련과 훈련을 통해 만들어지는 것이라고 합니다. 이 공연은 그들의 음악과 함께 군인들이 자신의 능력을 발휘할 수 있게 해주는 기회를 제공하기도 합니다.
방탄 군대는 한국 국방의 핵심적인 역할을 담당하고 있으며, 그들의 음악도 군인들의 사명을 위해 함께 달려가고 있습니다.
```