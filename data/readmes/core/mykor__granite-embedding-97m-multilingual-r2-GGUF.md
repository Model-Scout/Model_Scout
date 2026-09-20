---
language:
  - ar
  - az
  - bg
  - bn
  - ca
  - cs
  - da
  - de
  - el
  - en
  - es
  - et
  - fa
  - fi
  - fr
  - he
  - hi
  - hr
  - hu
  - id
  - is
  - it
  - ja
  - ka
  - kk
  - km
  - ko
  - lt
  - lv
  - mr
  - ms
  - nl
  - "no"
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - sq
  - sr
  - sv
  - sw
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - uz
  - vi
  - zh
library_name: GGUF
license: apache-2.0
pipeline_tag: feature-extraction
tags:
  - granite
  - embeddings
  - multilingual
  - mteb
  - feature-extraction
  - sentence-similarity
base_model: ibm-granite/granite-embedding-97m-multilingual-r2
---

# Granite-Embedding-97M-Multilingual-R2-GGUF

```py
import numpy as np
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "ibm-granite/granite-embedding-97m-multilingual-r2",
)
llama = Llama.from_pretrained(
    repo_id="mykor/granite-embedding-97m-multilingual-r2-GGUF",
    filename="granite-embedding-97M-multilingual-r2-BF16.gguf",
    verbose=False,
    embedding=True,
    n_ctx=0,
)

text = """이젠 깨어나 설레는 이 마음 따라
기다리던 오늘을 만들 거야

이 많은 시간을 난
흘리고 싶지는 않아

이제 나는 분명히
준비가 돼 있는데

어떤 무기력함이 와도
나에겐 의미가 없을 만큼

또다시 wake up 더 wake up
달궈져 더 뜨겁게

굳이 봐줄 필요 없어 어차피 never give up
뭐가 덤벼오든 나는 어쩌라 하듯이
뭐든 할 수 있을 거 같아

이젠 깨어나 설레는 이 마음 따라
기다리던 오늘을 만들 거야

도시 사이에 피어나 이겨내온 꽃처럼
분명 피워낼 거야 나를

나에게 남아 있는 게 얼마 되지 않는 것 같아도
두 번 다신 내게 부끄럽지 않게
똑바로 봐

굳이 봐줄 필요 없어 어차피 never give up
뭐가 덤벼오든 나는 어쩌라 하듯이
뭐든 이길 수 있을거야

이젠 깨어나 설레는 이 마음 따라
기다리던 오늘을 만들 거야

도시 사이에 피어나 이겨내온 꽃처럼
분명 피워낼 거야 나를

time’s up 몇 번을 해도 Overcharge
그만해도 된다 해도 (그만해도 된다 해도)
no matter no matter 숨이 차올라도
이 길을 바란다면

하늘 저 너머 뻗어가는 빛 따라
이 마음도 날려 곧 닿을 것만 같아

도시 사이에 피어나 이겨내온 꽃처럼
분명 피워낼 거야 나를"""

embed1 = model.encode(text)
embed2 = np.array(llama.embed(text), dtype=np.float32)
print(cos_sim(embed1, embed2).item())
```

```
0.9999578595161438
```
