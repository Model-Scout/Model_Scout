---
license: mit
language:
- ko
library_name: transformers
---

# Update 2025-05-31

[Full dataset](https://huggingface.co/datasets/north-wind/ko-TinyStories) released.

# Experimental-Neo-TinyStories-Korean-800K-20240819

A new model trained with new datasets while retaining the almost identical architecture to the [previous version](https://huggingface.co/north-wind/TinyStories-Korean-800K).
The only difference in the architecture is that the context length has been increased to 1024.

- Architecture: Llama
- Vocab size: 4096
- Hidden size: 64
- Layers: 5
- Heads: 8 (MHA)
- Context length: up to 1024 tokens

## Improvements
Even though this model is exceptionally small for a language model, it has achieved significant improvements in generating accurate and
logical sentences compared to its predecessor. These improvements were made possible by learning from super simple stories generated
by more powerful language models, inspired by the [TinyStories paper](https://arxiv.org/abs/2305.07759). Instead of using a dataset translated
from English data, a much higher quality dataset was obtained by generating new synthetic data in line with the methodology outlined in the paper.

This model was intentionally kept the same size as its [predecessor](https://huggingface.co/north-wind/TinyStories-Korean-800K) to
demonstrate the impact of dataset quality on model performance. In fact, despite being trained on only about 10% of the tokens used
by the previous model, it exhibits significantly better performance. The dataset will be released along with a larger version of the
Neo-TinyStories-Korean model once its creation and validation are complete.

## Generation Examples
Result of **this model** with only single `<s>` token was given:
> 푸르른 하늘 아래 눈부신 햇살이 가득한 날이었어요. 아기 곰은 엄마 곰과 함께 숲으로 놀러 갔어요. 숲 속에는 예쁜 꽃들이 피어 있었고, 아기 곰은 신이 나서 꽃을 구경했어요. 아기 곰은 꽃을 보며 신이 났어요. 갑자기 아기 곰은 엄마 곰에게 달려가 "엄마, 저 꽃 예뻐요!"라고 말했어요. 엄마 곰은 아기 곰에게 "그래, 예쁜 꽃이야!"라고 말하며 아기 곰을 꼭 안아 올렸어요. 아기 곰은 엄마 곰의 말을 듣고 꽃을 꺾지 않고 예쁘게 바라보는 것을 배웠어요. 아기 곰은 엄마 곰의 말을 잘 듣는 것이 중요하다는 것을 알았어요.

Result of **previous model** with only single `<s>` token was given:
> 옛날 옛날, 큰 숲속에 큰 나무들이 작은 숲에 살고 있었습니다. 그 나무들은 매우 행복했습니다. 어느 날, 작은 새들이 그 나무에 왔어요. 그 나무는 작은 새를 보고 매우 기뻐했습니다. "안녕, 작은 새야! 어떻게 해야?"라고 새가 말했습니다. "나는 잎이 없어서 그래요." 작은 새는 "저는 크고 강해지는데, 저는 정말 강해요."라고 말했습니다. 작은 새는 날아올라 잎을 먹고 싶어 했습니다. 새는 잎을 잡고 싶어 했습니다. 작은 새는 잎을 찾아서 잎을 찾아 나섰습니다. 마침내, 작은 새는 잎을 찾아 큰 잎을 찾았습니다. 작은 새는 잎사귀들을 찾아서 잎을 찾아내어 잎을 뽑아냈습니다. 새는 잎을 따서 잎을 다시 뽑아냈습니다. 작은 새는 매우 행복했습니다. 그들은 종일 잎으로 놀았고, 그 날 이후로 그들은 항상 함께 놀았습니다.

Result of **this model** with start sequence `먼 옛날, 고양이` was given:
> 먼 옛날, 고양이 한 마리가 살았습니다. 고양이는 밥을 먹고 싶었습니다. 고양이는 밥을 찾아 숲 속으로 들어갔습니다. 고양이는 맛있는 과일을 찾았습니다. 고양이는 과일을 먹고 싶었습니다. 고양이는 과일을 먹으려고 했지만, 고양이는 배에 올라갈 수 없었습니다. 고양이는 슬펐습니다. 고양이는 밥을 못 먹었습니다. 고양이는 슬펐습니다. 고양이는 엄마에게 말했습니다. "엄마, 밥이 없어요!" 고양이는 슬펐습니다. 고양이는 엄마에게 밥을 주었습니다. 엄마는 고양이에게 밥을 주었습니다. 고양이는 밥을 맛있게 먹었습니다. 고양이는 엄마에게 고맙다고 말했습니다. 고양이는 엄마 말을 잘 들었습니다.

Result of **previous model** with start sequence `먼 옛날, 고양이` was given:
> 먼 옛날, 고양이, 보라색인 새, 톰은 공원에서 놀고 있었습니다. 그는 큰 나무를 보고 올라가고 싶어 했습니다. 그는 올라가고 올라가기 시작했습니다. 그는 올라가서 나무를 오르기 시작했습니다. 톰이 올라 가면서 그는 큰 나무를 보았습니다. 그는 나무를 오르기 시작했습니다. 톰은 나무를 오르기 시작했습니다. 그는 손을 잡았습니다. 그는 나무 꼭대기까지 올라갔습니다. 그 나무 꼭대기에 도달했습니다. 톰은 매우 행복했습니다. 그는 나무 아래 큰 나무를 보았습니다. 그는 나무에서 내려오며 나무를 오를 수 있었습니다. 그는 나무를 오르고 싶었습니다. 하지만 톰은 나무를 오르기 시작했습니다. 그는 큰 나무를 오르기 위해 올라가 올라갔습니다. 톰은 나무 꼭대기에 도달했습니다. 그는 나무를 오르는 것이 너무 기뻤습니다. 그는 나무 꼭대기까지 도달했습니다. 나무 꼭대기에는 큰 나무가 있는 것을 보았습니다. 그는 나무 위로 올라갔고 나무를 오르기 시작했습니다. 나무는 나무 꼭대기에 올라갔습니다. 톰은 매우 기뻤습니다. 그는 나무의 모든 친구들을 방문해 오랫동안 내려왔습니다. 그들은 함께 많은 재미를 느꼈습니다.


## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained('north-wind/Experimental-Neo-TinyStories-Korean-800K-20240819')
tokenizer = AutoTokenizer.from_pretrained('north-wind/Experimental-Neo-TinyStories-Korean-800K-20240819')

input_text = ''
input_ids = tokenizer(input_text, return_tensors='pt').input_ids

output = model.generate(input_ids, max_length=1024, do_sample=True, temperature=0.5)
print(tokenizer.decode(output[0]))
```

## Further plans
- Generate more data to match the quantity to the original English version of TinyStories dataset
- Apply quality filter to generated dataset
- Train a larger model on the final dataset
- Release the model and dataset