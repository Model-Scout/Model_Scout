---
license: mit
task_categories:
  - text-generation
language:
  - ko
size_categories:
  - 10K<n<100K
tags:
  - fish
  - character
  - korean
  - tiny-llm
  - synthetic
pretty_name: GuppyLM Korean Chat
---

<p align="center">
  <img src="assets/guppy.png" alt="GuppyLM" width="300"/>
</p>

<p align="center">
  <a href="https://github.com/arman-bd/guppylm"><img src="https://img.shields.io/badge/GitHub-guppylm-181717?logo=github" alt="GitHub"/></a>&nbsp;
  <a href="https://huggingface.co/arman-bd/guppylm-9M"><img src="https://img.shields.io/badge/🤗_Model-guppylm--9M-orange" alt="Model"/></a>&nbsp;
  <a href="https://colab.research.google.com/github/arman-bd/guppylm/blob/main/train_guppylm.ipynb"><img src="https://img.shields.io/badge/Open_in-Colab-F9AB00?logo=googlecolab" alt="Colab"/></a>
  <br/>
  <a href="https://www.linkedin.com/pulse/build-your-own-language-model-5-minutes-i-made-mine-hossain--supif/"><img src="https://img.shields.io/badge/Article-LinkedIn-0A66C2?logo=linkedin" alt="LinkedIn Article"/></a>&nbsp;
  <a href="https://arman-bd.medium.com/build-your-own-llm-in-5-minutes-i-made-mine-talk-like-a-fish-e20c338a3d14"><img src="https://img.shields.io/badge/Article-Medium-000000?logo=medium" alt="Medium Article"/></a>
</p>

# GuppyLM Korean Chat Dataset

Training data for a Korean-localized GuppyLM — a ~9M parameter LLM that talks like a small fish.

## Dataset Description

60K single-turn conversations between a human and Guppy, a small fish character.
This version is localized for Korean and keeps the same fish-like personality.
Guppy speaks in short, casual sentences about water, food, light, and tank life.
It doesn't understand human abstractions.

### Example

```
Input:  배고파?
Output: 응. 항상 배고파. 지금 바로 위로 올라갈게.

Input:  정치에 대해 어떻게 생각해?
Output: 정치가 뭔지 모르겠어. 물에 젖어 있어?

Input:  잘 자, 구피
Output: 잘 자. 바닥 근처에서 쉴게. 내일은 펠릿이 있으면 좋겠다.
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `input` | string | 사용자 메시지 |
| `output` | string | 구피의 응답 |
| `category` | string | 주제 카테고리 (60개 범주) |

## Categories

Greetings, feelings, temperature (hot/cold), food, light, water, about, confused (human things),
tank, noise, night, lonely, misc, goodbye, bubbles, glass, reflection, breathing, swimming,
colors, taste, plants, filter, algae, snail, glass tapping, scared, excited, bored, curious,
happy, tired, outside, cat, rain, seasons, music, visitors, children, meaning of life, time,
memory, dreams, size, future, past, name, weather, sleep, friends, jokes, fear, love, age,
intelligence, bathroom, health, singing, TV.

## Usage

```python
from datasets import load_dataset
ds = load_dataset("arman-bd/guppylm-60k-generic")
print(ds["train"][0])
# {'input': '배고파?', 'output': '응. 항상 배고파. 지금 바로 위로 올라갈게.', 'category': 'food'}
```

## Generation

Data is synthetically generated using template composition with randomized components
(tank objects, food types, activities, body parts, etc.) for high output diversity.
For a Korean fork, the same generation logic can be translated and regenerated in Korean.

## Links

- **Original Repo:** [github.com/arman-bd/guppylm](https://github.com/arman-bd/guppylm)
- **Original Model:** [huggingface.co/arman-bd/guppylm-9M](https://huggingface.co/arman-bd/guppylm-9M)

## License

MIT
