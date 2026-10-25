---
language:
- ko
- en
license: apache-2.0
library_name: pytorch
pipeline_tag: text-generation
base_model: shopkeeper/kor-finewiki-1b-base
tags:
- korean
- chat
- gated-deltanet
- hybrid
- from-scratch
datasets:
- lemon-mint/smol-koreantalk
- maywell/koVast
- nayohan/Magpie-Pro-MT-300K-v0.1-ko
- nlpai-lab/kullm-v2
- beomi/KoAlpaca-v1.1a
- jojo0217/korean_safe_conversation
- FreedomIntelligence/sharegpt-korean
---

# Korean 1B hybrid chat model (Gated DeltaNet + GQA), trained from scratch

The chat version of [shopkeeper/kor-finewiki-1b-base](https://huggingface.co/shopkeeper/kor-finewiki-1b-base): a 1.0B-parameter Korean language model
pretrained from random initialisation on 25.2B tokens, then supervised fine-tuned on 392,615 public
Korean conversations. Architecture, tokenizer, kernels, optimizer, pretraining and fine-tuning loops are our own code
(PyTorch + Triton). See the base model card for the architecture, pretraining corpus and pretraining method.

## Chat template

Single-token role markers; no whitespace between segments:

```
<|endoftext|>[<|system|>{system}<|end|>]<|user|>{user 1}<|end|><|assistant|>{reply 1}<|end|><|user|>{user 2}<|end|><|assistant|>
```

Generation starts after `<|assistant|>` and stops at `<|end|>`. The system turn is optional (the fine-tuning data
mostly has none). Details in `CHAT_TEMPLATE.md`; `kollm.generate.build_prompt` implements it.

## Fine-tuning data

| source | Hugging Face dataset | conversations used | license |
|---|---|---|---|
| smol-koreantalk (Korean translation of SmolTalk) | [lemon-mint/smol-koreantalk](https://huggingface.co/datasets/lemon-mint/smol-koreantalk) | 150,000 | Apache-2.0 |
| koVast | [maywell/koVast](https://huggingface.co/datasets/maywell/koVast) | 100,000 | MIT |
| Magpie-Pro-MT-ko (Korean translation of Magpie-Pro-MT) | [nayohan/Magpie-Pro-MT-300K-v0.1-ko](https://huggingface.co/datasets/nayohan/Magpie-Pro-MT-300K-v0.1-ko) | 60,000 | not stated |
| KULLM-v2 | [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | 50,000 | Apache-2.0 |
| KoAlpaca v1.1a | [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) | 21,136 | not stated |
| korean_safe_conversation | [jojo0217/korean_safe_conversation](https://huggingface.co/datasets/jojo0217/korean_safe_conversation) | 6,914 | Apache-2.0 |
| ShareGPT-ko | [FreedomIntelligence/sharegpt-korean](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-korean) | 5,565 | Apache-2.0 |

392,615 training conversations (231M tokens, of which
196M are assistant tokens that carry the loss) and 1,000
held out for validation. Rows with malformed turns were dropped, duplicates were removed by first user turn, the larger
sets were subsampled to the counts above, and conversations longer than 2,048 tokens were cut back to whole turns.
Conversations overlapping our evaluation sets (held-out text, KoBEST, KMMLU test, chat eval prompts) were removed with
the same n-gram filter used for pretraining.

## Fine-tuning method

- Loss on assistant tokens (and their closing `<|end|>`) only.
- 1 epoch = 984 optimizer steps; AdamW (β = 0.9/0.95, no weight decay), gradient clipping 1.0.
- Learning rate 5e-05: 100 warmup steps, then cosine decay to 10%.
- Length-bucketed micro-batches of ≤ 8,192 padded tokens, 16 accumulation steps × 2 GPUs
  per optimizer step (up to 262k tokens); bf16 autocast, per-block activation checkpointing.
- 2× RTX A6000, 6.6 h. Validation loss 1.811 (step 200) → 1.692 (final).

## Evaluation

Same harness for every model: held-out bits per byte (lower is better), KoBEST 0-shot accuracy and KMMLU 0-shot.

| model | BPB ↓ | COPA | HellaSwag acc / norm | SentiNeg | BoolQ | KMMLU |
|---|---|---|---|---|---|---|
| **this model (1.0B, chat)** | 0.749 | 0.703 | 0.416 / 0.518 | 0.587 | 0.517 | 0.298 |
| [kor-finewiki-1b-base](https://huggingface.co/shopkeeper/kor-finewiki-1b-base) (its base model) | 0.729 | 0.690 | 0.418 / 0.546 | 0.599 | 0.496 | 0.255 |
| EleutherAI/polyglot-ko-1.3b (base) | 1.052 | 0.711 | 0.408 / 0.534 | 0.703 | 0.499 | 0.153 |
| skt/kogpt2-base-v2 (125M, base) | 1.092 | 0.584 | 0.318 / 0.422 | 0.615 | 0.502 | 0.177 |

KMMLU chance is 0.25. Fine-tuning costs a little held-out BPB (expected: the model moves toward the chat format)
and lifts KMMLU above chance; WiC (not shown) is at chance for every model.

## Sample conversations

The first 2 prompts of each category in our fixed 30-prompt Korean chat evaluation, one sample each
(temperature 0.7, top-p 0.9, repetition penalty 1.1, up to
384 new tokens), unedited and not cherry-picked. They include the model's mistakes.

**mt01 (multi-turn)**

> **User:** 안녕하세요! 저는 이번 주말에 부산에 여행을 가려고 해요.  
>
> **Assistant:** 주말 여행 계획에 대해 기꺼이 도와드리겠습니다. 어디로 가고 싶으세요? 해변에서 휴식을 원하시나요, 아니면 문화 체험을 찾으시나요? 선호도를 알려주시면 더 맞춤화된 추천을 해드릴 수 있습니다.  

> **User:** 가 볼 만한 곳 세 군데만 추천해 주세요.  
>
> **Assistant:** 다음은 가볼만한 세 가지 장소입니다:  
>
> 1. 해운대 해수욕장 (부산광역시 해운대구) - 겨울의 따뜻함과 여름의 햇살을 모두 즐길 수 있는 완벽한 여행지입니다.  
> 2. 광안리 해수욕장 (부산광역시 수영구) - 광안대교를 감상하며 바다 풍경을 즐기는 것도 좋습니다.  
> 3. 감천문화마을 (부산시 사하구) - 한국의 가장 대표적인 벽화 마을 중 하나입니다. 독특한 벽화와 아기자기한 상점들이 있어 많은 여행객들에게 인기가 많습니다.  
> 4. 부산 박물관 (부산 중구) - 60년 이상의 역사를 가진 박물관으로 다양한 전시물을 제공합니다. 특히 부산 박물관은 부산의 역사와 문화를 잘 보여주는 곳으로 유명합니다.  
> 5. 이기대와 송정해수욕장 (울산광역시 북구) - 두 곳은 모두 아름다운 해안 경치를 가지고 있으며, 둘 다 독특한 해변 경험을 선사합니다. 송정은 한적한 분위기 때문에 여유롭고 여유로운 시간을 보내기에 좋은 곳입니다. 반면 기대는 해변과 해양 스포츠를 즐기기에 적합한 곳입니다.  
> 6. 광안대교와 마린시티 아파트 단지 (부산 남구) - 이 두 곳은 도시의 멋진 전망을 제공하며, 특히 마린시티 아파트는 고층 빌딩이 많아 도시적인 분위기를 느낄 수 있습니다.  
> 7. 태종대 (부산 영도구) - 부산 최대의 관광지로, 해녀와 해풍 등의 자연 환경을 감상할 수 있는 곳입니다. 또한, 유람선을 타거나 바닷길을 따라 걷는 등 다양한 액티비티를 즐길 수도 있습니다.  
> 8. 용두산공원 및 주변 관광지 (부산 중구) - 이 공원에는 부산의 역사와 문화를 소개하는 다양한 유적지와 명소가 있습니다. 공원을 산책하면서 부산의 다양한 면모를 경험할 수 있습니다.  
> 9. 국제시장 및 자갈치 시장 (부산 중구) - 두 곳 모두 오래된 시장으로, 부산의 대표적인 음식들을 맛볼 수 있습니다. 또한, 시장이 활기를 띠는 저녁 시간에는 관광객들의 발길이 끊이지 않습니다.  
> 10. 용호동 횟집 거리 (부산 동구) - 맛있는 해산물 요리와 함께 맛있는 회를 즐길 수 있는  

> **User:** 그중에서 바다가 보이는 곳은 어디예요?  
>
> **Assistant:** 바다가 보이는 세 곳을 추천드리면 다음과 같습니다:  
>
> 1. 해운대 해수욕장(Busan beach): 이곳은 해운대 해수욕장에서 가장 아름다운 전망 중 하나입니다. 푸른 바다와 하얀 모래사장이 펼쳐져 있어 바다 풍경을 즐기기 좋습니다.  
> 2. 광안리 해수욕장(Busan beach): 이곳은 해운대 해수욕장과 마찬가지로 바다와 함께 아름다운 전망을 제공합니다. 하지만 수영을 하기보다는 물놀이나 바다를 감상하는 데 초점을 맞추는 것이 좋습니다.  
> 3. 감천문화마을: 감천문화마을은 부산의 유명한 벽화 마을입니다. 이곳에서도 바다가 보이며, 부산 4대문 안에 속해있어 문화체험을 할 수 있는 기회가 많습니다.  
> 4. 부산 박물관: 이곳은 부산의 역사 유적을 모아 놓은 박물관으로, 바다와 함께 역사적인 역사를 배울 수 있는 장소입니다.  
> 5. 이기대와 송정해수욕장: 이곳에서 바다 전망이 매우 아름답습니다. 이곳에서는 해수욕뿐만 아니라 해변에서 즐기는 활동도 즐길 수 있습니다.  
> 6. 광안리 해수욕장: 이곳은 해운대의 해변과는 달리 비교적 조용한 분위기로, 바다와 함께 휴식을 취하기 좋은 장소이기도 합니다.  
> 7. 태종대: 태종대는 부산의 대표적인 관광지로, 시원한 산들과 바다의 조화가 아름다운 곳입니다. 등산이나 산책을 하면서 부산의 자연을 만끽할 수 있습니다.  
> 8. 용두산공원 및 주변 관광지: 이곳에서는 부산의 랜드마크인 용두산공원이 위치해있습니다. 용두산공원을 산책하며 부산의 다양한 문화와 역사를 배울 수 있고, 관광지를 방문하면서 부산의 매력을 느낄 수 있습니다.  

**mt02 (multi-turn)**

> **User:** 제 이름은 민수예요. 저는 고양이 두 마리를 키워요.  
>
> **Assistant:** 안녕, 내 이름은 민수이고, 고양이 두 마리에게 둘러싸여 있어요!  
>
> 저는 고양이들과 함께 사는 것을 좋아해요 - 정말 특별한 조합이에요 – 하지만, 항상 즐거운 시간을 보내는 것은 아니에요. 제 삶은 바쁘게 돌아가지만, 저는 항상 제 고양이들을 위해 시간을 내고 싶어요. 그래서 제가 좋아하는 몇 가지 것들을 소개해 드릴게요:  
>
> 1.  **산책**: 저는 항상 고양이를 데리고 동네를 산책하는 데 많은 시간을 할애하고 싶어요. 그리고 저는 그들이 지루하지 않도록 새로운 곳으로 데려갈 수 있도록 가끔 새로운 장소를 탐험해야 해요.  
>
> 2.  **고양이 놀이 시간**: 고양이와 놀면 제 삶이 훨씬 더 즐거워져요. 그들은 그들의 독립적인 성격을 가지고 있고, 때로는 제가 그들만의 시간을 갖는 것이 필요해요. 저는 그들에게 간식이나 장난감을 주면서 그들을 즐겁게 할 수 있지만, 그들이 스스로 놀도록 내버려 둬도 괜찮아요.  
>
> 3.  **요리하기**: 저는 고양이들이 제대로 식사를 하는지 확인하는 데 많은 시간을 보내는데, 특히 바쁜 아침에는 쉽지 않아요. 그래도 가끔 맛있는 간식을 만들려고 노력하지만, 고양이들이 직접 먹는 것을 보는 것도 재미있어요.  
>
> 4.  **장난감 정리하기**: 저는 그들이 가장 좋아하는 장난감과 간식을 다락방에 보관하는 경우가 많아요. 시간이 좀 걸릴 수 있지만, 정리하는 것도 재미있고, 고양이들은 제가 그들을 위해 해내는 일을 보면 행복해할 거예요.  
>
> 5.  **재미있는 대화 나누기**: 고양이는 항상 저에게 재미있는 이야기를 들려줘요. 그들은 저를 웃게 만들고, 저는 그들에 대해 더 많이 배우면서 그들을 관찰하게 돼요. 그리고 물론, 저는 그들을 위해 간식을 먹거나 그들의 코를 핥는 등 그들과 놀아주는 것만큼 재미있는 일도 많이 하고 있어요.  
>
> 모든 사람이 다르고 모든 것이 서로 다르다는 것을 기억하세요 – 그것이 바로 우리가 함께 있는 이유에요! 당신은 어떠세요?  

> **User:** 고양이 사료는 하루에 몇 번 주는 게 좋을까요?  
>
> **Assistant:** 고양이의 영양 요구량은 다양하며, 고양이의 나이, 품종 및 크기에 따라 달라질 수 있다는 점을 명심해주세요. 다음은 일반적인 지침이에요:  
>
> - 어린 새끼 고양이 (1~2개월): 하루 60g에서 80g 사이  
> - 성묘(7~12주): 하루 90g에서 100g 사이  
> - 노령 고양이 또는 비만성 고양이 (12주 이상): 하루 100g에서 120g 사이  
>
> 더 정확한 지침은 다음과 같아요:  
>
> * 2개월 미만의 아기 고양이를 위해 특별히 고안된 고양이 사료의 경우, 1일 최대 급여량인 약 60g을 목표로 하세요.  
> * 2개월 이상의 성묘를 위한 사료는 일일 총 칼로리의 약 20%에 해당하는 150~200g의 체중 당 사료여야 해요.  
> * 성체 고양이는 보통 하루에 약 150~200g의 먹이를 필요로 하며, 이는 일일 총 칼로리의 25%가 될 거에요.  
>
> 그러나 항상 수의사나 반려동물 전문가와 상담하여 개별적인 필요에 맞는 적절한 양의 음식과 사료를 제공하는 것이 좋아요.  

> **User:** 제 이름이 뭐라고 했죠? 그리고 제가 키우는 동물은 몇 마리예요?  
>
> **Assistant:** 저는 민수라고 해요 – 제 이름은 민수이고, 네 마리의 고양이와 함께 살고 있어요!  
>
> 저는 4마리의 고양이와 함께 살고 있는데, 그 중 두 마리는 믹스이며, 한 마리는 스탠다드 랙입니다. 제 고양이들은 모두 다정한 아이들이며, 서로 잘 지내고 있어요.  
>
> 3살 된 코숏인 제 큰 형제 중 하나는 "코비"라는 이름의 똑똑하고 호기심 많은 고양이에요. 그는 항상 새로운 장난감을 가지고 놀고 싶어 하는데, 제 주방 구석에 있는 스크래칭 포스트와 같은 것이죠. 하지만 그는 또한 훌륭한 리더이기도 하고, 다른 사람들을 잘 따르기도 해요.  
>
> 그리고 작은 친구인 멋진 샴고양이인 "레이첼"이라는 고양이가 있어요. 그녀는 항상 주변을 돌아다니고, 심지어 집안을 돌아다닐 수도 있어요. 그녀의 털과 성격 때문에 그녀는 저를 정말 행복하게 해줘요.  
>
> 3살 된 골든 리트리버인 제 둘째는 "루비"인데, 그는 온순하지만 애정이 많고 똑똑해요. 그는 저를 끊임없이 쫓아다니는데, 마치 제가 그를 위해 자신의 공간을 만들고 싶어하는 것 같죠.  
>
> 마지막으로, 사랑스러운 퍼그인 저만의 강아지인 "루시"도 있습니다. 루시는 항상 제 침대 옆에서 자고, 놀아주길 원해요. 아직 어리고, 매우 충성스럽지만요...  
>
> 제가 돌보는 고양이들의 수를 세어보지는 못했지만, 4마리 모두 건강하고 행복하다고 확신할 수 있어요! 저는 그들을 사랑하지 않는 것은 상상할 수가 없어요.  

**fa01 (factual)**

> **User:** 대한민국의 수도는 어디인가요?  
>
> **Assistant:** 대한민국의 수도는 서울특별시입니다.  

**fa02 (factual)**

> **User:** 훈민정음은 누가, 언제 만들었나요?  
>
> **Assistant:** 훈민정음(訓民正音)은 1446년 세종대왕이 직접 만든 한글입니다. 훈민정음의 창제 목적은 중국어를 한글로 표기하여 백성들이 쉽게 읽고 쓸 수 있도록 하는 것이었습니다. 따라서 이 훈민정음이 언제 만들어졌는지는 정확히 알 수는 없습니다. 하지만 조선 시대에 만들어진 것으로 추정됩니다.  
>
> 훈민정음을 만든 것은 세종대왕 혼자 한 것이 아니라 신하들과 학자들이 함께 만들었습니다. 또한 훈민정음에 대한 자세한 내용은 기록되어 있지 않지만, 세종대왕 스스로가 만들었다는 것을 알 수 있습니다.  
>
> 따라서 훈민정음은 세종의 명으로 만들어진 글자인데, 이는 세종이 직접 만들어 사용했기 때문입니다.  

**ca01 (casual)**

> **User:** 오늘 너무 피곤하다... 퇴근하고 뭐 하면 좋을까?  
>
> **Assistant:** 오늘 너무 피곤하다면, 출근 전에 가벼운 스트레칭이나 스트레칭을 하여 근육을 풀어주는 것이 좋습니다. 또한, 점심시간에 따뜻한 물을 마시고 산책을 하거나 낮잠을 자는 것도 좋은 방법입니다. 업무 시간 중에는 집중력을 높이기 위해 독서를 하거나 공부를 하는 것을 추천합니다. 이러한 방법들을 통해 피로를 극복하고 업무를 효율적으로 처리할 수 있습니다.  

**ca02 (casual)**

> **User:** 너는 어떤 음식을 좋아해?  
>
> **Assistant:** 저는 다양한 음식을 좋아합니다. 특히, 한국 음식 중에서도 김치찌개, 된장찌개와 같은 한국의 전통음식을 즐겨 먹습니다. 또한, 매운 음식을 좋아하며, 마라탕이나 닭발과 같이 한국 요리에도 자주 들어갑니다.  

**in01 (instruction)**

> **User:** 다음 문장을 존댓말로 바꿔 주세요: "내일 몇 시에 올 거야?"  
>
> **Assistant:** 내일 아침 8시에 올게요.  

**in02 (instruction)**

> **User:** '봄'을 주제로 짧은 시를 4줄로 써 주세요.  
>
> **Assistant:** 봄은 달콤한 시간, 신선한 공기, 그리고 끝없는 즐거움으로 가득해요  
> 꽃들은 만개하고, 나무들은 싹 트고 있어요  
> 모든 것이 새롭게 시작되고, 모든 것이 새롭게 시작돼요  
> 사방은 밝은 빛에 휩싸여 있고, 모든 것을 밝혀줘요  
> 계절의 순환이 이어지고, 봄의 시작을 알립니다  
> 겨울과 여름 사이의, 새로운 계절이에요  
> 그리고 모든 생명체는 봄이 올 때 그것을 기념합니다.  

## Limitations

- Small model: frequent factual errors stated confidently (e.g. it names the wrong highest mountain and wrong
  distances), unreliable arithmetic, and weak tracking of facts across turns.
- Often ignores explicit constraints such as the number of items or lines requested.
- Speaks as a human at times (claims to eat food); no preference tuning or dedicated safety training beyond a small
  safe-conversation set in the fine-tuning data.
- 2,048-token context; Korean-focused, limited English.

## Usage

Requires a CUDA GPU, PyTorch, Triton, `tokenizers` and `safetensors` (tested with PyTorch 2.8 + Triton 3.4). Not a
`transformers` architecture; load it with the included code:

```python
import sys
from huggingface_hub import snapshot_download
path = snapshot_download("shopkeeper/kor-finewiki-1b-chat")
sys.path.insert(0, path)
from kollm.load import load_model
from kollm.generate import build_prompt, generate, special_ids

model, tok, _ = load_model(path)                       # bf16 on cuda
sp = special_ids(tok)
messages = [{"role": "user", "content": "훈민정음은 누가 만들었나요?"}]
out = generate(model, build_prompt(tok, messages), max_new_tokens=256, temperature=0.7, top_p=0.9,
               repetition_penalty=1.1, stop_ids={sp["end"], sp["endoftext"], sp["user"]})
print(tok.decode(out))
```

Or interactively: `python chat.py` inside the downloaded folder (`/reset` clears the history, `/exit` quits).

## License and data attribution

Model weights and code: apache-2.0. Pretraining data: FineWeb-2 and FineWeb-Edu (ODC-By 1.0) and Wikipedia
(CC BY-SA 4.0). Fine-tuning data: see the table above; check those terms before using this model.
