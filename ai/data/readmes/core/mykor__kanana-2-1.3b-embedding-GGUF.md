---
library_name: gguf
pipeline_tag: sentence-similarity
license: other
license_name: kanana-open-license
license_link: https://huggingface.co/kakaocorp/kanana-2-1.3b-embedding/blob/main/LICENSE
tags:
    - feature-extraction
    - mteb
    - matryoshka
    - custom_code
language:
    - ko
    - en
base_model: kakaocorp/kanana-2-1.3b-embedding
---

# kanana-2-1.3b-embedding-GGUF

```py
import numpy as np
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "kakaocorp/kanana-2-1.3b-embedding",
)
llama = Llama.from_pretrained(
    repo_id="mykor/kanana-2-1.3b-embedding-GGUF",
    filename="kanana-2-1.3B-embedding-BF16.gguf",
    verbose=False,
    embedding=True,
    n_ctx=0,
)

text = """끝도 없이 흩어지는 심연 속에 떠오르는 빛
하염없이 쫓아가도 가까워지지 않아
숨이 차올라 주저앉던 그 순간 깨달았어
저 별들이 빛나는 이유 어둠이 있어서란 걸

오랜 외로움 속에 지새우던 이 별로 이 맘을 채우고 싶던
나와 이별하고서 다시 일어설게

달려 나가, 세상 모든 반짝임이 숨죽이고 있는 우리만의 무대로
괜찮아, 이 밤을 물들여 가는 건 이제 우리의 어둠이 될 테니까
그래, 우린 저 반짝이는 별빛들을
끌어안을 가장 따스한 어둠일 거야

수없이 많은 시선 우리 위로 쏟아져도
흔들리지 않을 이유를 이젠 알아
오랜 시간 헤매왔던 발자국이 오늘의 나를 만든 이유니까
영원히 간직할 거야 내 맘에 깊숙이 담아

조금 더 멀리 가보고 싶어 아무도 닿지 못한 저곳까지
눈부신 별들을 더 빛나게 할 거야

처음부터, 아무것도 없었던 그곳에서 어둠으로 태어났으니까
알잖아, 정해진 길 하나 없어도 우린 서로를 잃지 않을 거란 걸
깊은 밤의 그 한가운데 나 피어나
알 수 없는 내일은 우릴 더 빛나게 해

모든 빛이 잠들어 버린다 해도
그 곁에 우린 남아 있어
저 먼 곳에서부터 흘러온 빛이 너의 마음속에 닿는다면
그 속엔 우리가 있을 테니까

달려 나가, 세상 모든 반짝임이 기다리고 있는 우리만의 무대로 (Ah)
괜찮아, 이 밤을 물들여 가는 건 이제 우리만의 색이 될 테니까
그래, 우린 (그래, 우린) 저 반짝이는 (저 반짝이는) 별빛들을 (별빛들을)
끌어안을 가장 따스한 어둠일 거야"""

embed1 = model.encode(text)
embed2 = np.array(llama.embed(text), dtype=np.float32)
print(cos_sim(embed1, embed2).item())
```

```
0.9745417833328247
```
