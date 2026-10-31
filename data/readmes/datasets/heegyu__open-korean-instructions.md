---
license: mit
---

4가지 한국어 챗봇 학습용 데이터셋을 합쳐놓았습니다. 이중 ShareGPT 데이터는 멀티턴으로 되어있습니다. 
데이터 생성 및 합치는 코드는 https://github.com/HeegyuKim/open-korean-instructions 여기를 참고하세요

| 이름 | # | 타입 |
|---|---|---|
| [KoAlpaca v1.0](https://huggingface.co/datasets/Bingsu/ko_alpaca_data) | 52K | 싱글턴 |
| [KoAlpaca v1.1](https://raw.githubusercontent.com/Beomi/KoAlpaca/main/KoAlpaca_v1.1.jsonl) | 21K | 싱글턴 |
| [ShareGPT DeepL 번역](https://huggingface.co/datasets/junelee/sharegpt_deepl_ko) | 620K(싱글턴), 84K(멀티턴) | 멀티턴, 싱글턴 |
| [OIG-small-chip2-ko](https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko) | 210K | 싱글턴 |
| [Korquad-Chat](https://huggingface.co/datasets/heegyu/korquad-chat-v1) | 9.6K | 멀티턴, 지식기반 |

모든 데이터는 포멧이 통일되어 있습니다. `<sys>`, `<usr>`, `<bot>` 세가지 토큰과 줄넘김으로 화자를 구분합니다.
korquad-chat 데이터의 경우, 유저와 봇이 서로를 호칭할 때는 `<|bot|>`, `<|user|>`로 되어있습니다.

```
{"source": "koalpaca-v1.0", "text": "<usr> 홀수 중 하나를 밝히세요.\n<sys> 트위터, 인스타그램, 텔레그램\n<bot> 텔레그램입니다."}
{"source": "korquad-chat", "text": "
       <sys>1984년 9월부터 덴노지 역 ~ 히네노 역간에 운전을 개시한 '홈 라이너 이즈미'가 전신이다. 특급 구로시오의 381계 전동차의 히네노 전차구 입선 회송 열차를 좌석 정리권을 필요로 하는 정원제 열차로서 운행해온 것으로 간사이 지방 최초의 홈 라이너였다. 1986년 11월 개정에 따라 운전 구간이 와카야마 역까지 연장되어 한와 라이너로 개칭되어 현재에 이르게 되었다. 이전에는 평일에 상행 3편, 하행 6편이 운전되었지만 일부가 신오사카 역이나 교토 역 방면 발착 특급 구로시오로 변경되어 2002년 3월 이후에는 상행 2편, 하행 4편으로 축소되었다. 2009년 3월의 시간표 개정부터는 휴일 시간대의 운전이 중단되었으며 같은 해 6월 1일부터는 전면 금연화되었다.\n
       <usr> 안녕하세요, <|bot|>. \"한와_선\"에 대해 알고 계시나요?\n
       <bot> 네, 전체적으로 알고 있습니다. 1984년에 운전을 개시한 \"홈 라이너 이즈미\"가 전신이며, 간사이 지방 최초의 홈 라이너였습니다. 1986년에는 와카야마 역까지 연장된 후 \"한와 라이너\"로 개칭되었습니다.\n
       <usr> 그렇군요. 이전에는 평일에 몇 편이 운행되었나요?\n
       <bot> 평일에 상행 3편, 하행 6편이 운전되었습니다. 하지만 2002년 이후로는 상행 2편, 하행 4편으로 축소되었습니다.\n
       <usr> 그렇군요. 혹시 특급 구로시오와 연관이 있을까요?\n
       <bot> 네, \"한와 라이너\"는 특급 구로시오의 381계 전동차의 히네노 전차구 입선 회송 열차를 좌석 정리권을 필요로 하는 정원제 열차로서 운행되었습니다."
}
```
