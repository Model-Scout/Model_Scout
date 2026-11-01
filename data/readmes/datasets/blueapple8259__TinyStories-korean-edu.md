---
license: cdla-sharing-1.0
task_categories:
- text-generation
language:
- ko
---

[TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)와 [TinyStories-Korean](https://huggingface.co/datasets/g0ster/TinyStories-Korean), [fineweb-edu-classifier](https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier)를 이용하여 만든 데이터입니다.

TinyStories를 fineweb-edu-classifier로 평가를 한 뒤 int_score가 3 이상이면 이에 해당되는 TinyStories-Korean을 데이터에 추가하는 방식으로 제작하였습니다.

TinyStories-Korean에서 데이터 300개가 누락되어 있어서 데이터 누락이 되지 않음을 확인한 1832000번째 데이터까지만 평가하였습니다.

## score 비율

- 3: 99.4%(501,651개)

- 4: 0.6%(2,931개)
