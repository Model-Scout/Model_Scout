---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: seed
    dtype: int64
  - name: temperature
    dtype: float64
  - name: top_p
    dtype: float64
  - name: answer
    dtype: string
  - name: min_neighbor_distance
    dtype: float64
  splits:
  - name: train
    num_bytes: 230989443.96223754
    num_examples: 113742
  download_size: 92161623
  dataset_size: 230989443.96223754
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---

### Data Generation

#### System Message

- Korean Reasoning Template
```
"pre_query_template": "<|im_start|>system\n당신은 알리바바 클라우드에서 만든 Qwen입니다. 당신은 유용한 어시스턴트입니다.\nuser가 논리적인 다단계의 추론 과정이 필요한 복잡한 문제를 내면, assistant는 한국어로 단계적으로 풀이를 제시합니다.<|im_end|>\n<|im_start|>user\n"
```

- (Original)
```
"pre_query_template": "<|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>\n<|im_start|>user\n"
```

#### Model

- Question: [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)
  - With vLLM
- Answer: [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
  - With [openrouter.ai](https://openrouter.ai/), Provider: [Together.ai](https://www.together.ai/)

※ Together AI's Qwen2.5-72b-instruct answer is not guaranteed to be reproducible, even with temperature=0.0.
 
#### Options

- temperature: {1.0, 0.9, 0.8}
- Amount: {40k, 40k, 40k}
- top_p: 0.99
- max_length: 1024(question), 4096(answer)

### Filtering

#### Non-Korean Result

- Removed question/answer contains Chinese character
- Removed question/answer contains full English sentence

#### Question Similarity

- Embedding model: [jinaai/jina-embeddings-v3](https://huggingface.co/jinaai/jina-embeddings-v3)
  - Based on [Korean Embedding Model Benchmark](https://github.com/su-park/mteb_ko_leaderboard) from su-park

- Similarity Distribution

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/qMR6K00UsJFSUSf5S-ggH.png)

- Removed min_neighbor_distance < 0.1 (about 1%)

#### Repitition(Max Token)

- Removed answer length == 4096

#### Question Distribution

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/25RqhB1PJCK7uv5fH1F4D.png)

---

### Question Quality(Completeness) based filtering (Not Applied Yet)

- Some questions are not solvable without additional conditions. The answers are confusing. I didn't remove it yet.

### Difficulty based filtering (Not Applied Yet)

- Some questions are too easy to solve.