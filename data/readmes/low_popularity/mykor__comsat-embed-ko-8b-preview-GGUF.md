---
language:
    - en
    - ko
library_name: GGUF
license: cc-by-nc-4.0
pipeline_tag: sentence-similarity
tags:
    - sentence-transformers
    - feature-extraction
    - sentence-similarity
    - mteb
    - korean
    - retrieval
base_model: sionic-ai/comsat-embed-ko-8b-preview
---

# comsat-embed-ko-8b-preview-GGUF

```py
import numpy as np
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "sionic-ai/comsat-embed-ko-8b-preview",
)
llama = Llama.from_pretrained(
    repo_id="mykor/comsat-embed-ko-8b-preview-GGUF",
    filename="comsat-embed-ko-8B-preview-BF16.gguf",
    verbose=False,
    embedding=True,
    n_ctx=0,
)

text = """남아있던 나를 떠나 더 희미해지고
어떤 외로움을 품고 살아가더라도
내게 닿았던 기억은 늘 찬란하게 번져
아직도 난 왜 잊지도 못하고 또
왜 난 더, 더 왜 갇힌 것 같은데
겁에 질린 채로

처음이라서 그래
가본 적 없는 길에
날 잠시 잊은 채
가시를 세운 채
상처 난 꽃잎처럼
떨어질 때 내 손을 잡아줄래?
끝의 밤을 지울게
빛으로 늘

내 맘에 핀 그림자는 날 삼키는 듯하고
기다리던 햇살은 날 스쳐 가듯 떠나고
겨우 매달린 희미한 달빛은 미끄러져
아직도 난 벗어나질 못하고 또
왜 난 더, 더 왜 무너져가는데
어쩔 줄 모르고

처음이라서 그래
가본 적 없는 길에
날 잠시 잊은 채
가시를 세운 채
상처 난 꽃잎처럼
떨어질때 내 손을 잡아줄래?
끝의 밤을 지울게
빛으로

그냥 달아나자 저 너머에
어두워지는 하늘이
우릴 다신 찾을 수 없게
검은 밤이 무섭지 않다기보단
포기할 수 있는 게 아냐 oh

이제서야 보이네
이미 따뜻했는데
고개를 떨구고
두 귀를 막고
내 곁을 지켜주던
널 놓칠 때 또 한 번 잡아줄래
약속할게 찬란한 미소를 oh, oh (오늘 밤이) oh
아침일 거야 우린 늘"""

embed1 = model.encode(text)
embed2 = np.array(llama.embed(text), dtype=np.float32)
print(cos_sim(embed1, embed2).item())
```

```
0.9998719096183777
```
