---
language: 
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - pt
  - ru
  - th
  - zh

    
multilinguality:
- multilingual    

task_categories:
- text-retrieval

license: mit
---

# Dataset Summary
MLDR is a Multilingual Long-Document Retrieval dataset built on Wikipeida, Wudao and mC4, covering 13 typologically diverse languages. Specifically, we sample lengthy articles from Wikipedia, Wudao and mC4 datasets and randomly choose paragraphs from them. Then we use GPT-3.5 to generate questions based on these paragraphs. The generated question and the sampled article constitute a new text pair to the dataset. The prompt for GPT3.5 is “You are a curious AI assistant, please generate one specific and valuable question based on the following text. The generated question should revolve around the core content of this text, and avoid using pronouns (e.g., ”this”). Note that you should generate only one question, without including additional content:”. 

The details of MLDR are shown in the following table.

| Language Code |  Language  |      Source      | #train  | #dev  | #test | #corpus | Avg. Length of Docs |
| :-----------: | :--------: | :--------------: | :-----: | :---: | :---: | :-----: | :-----------------: |
|      ar       |   Arabic   |    Wikipedia     |  1,817  |  200  |  200  |  7,607  |        9,428        |
|      de       |   German   |  Wikipedia, mC4  |  1,847  |  200  |  200  | 10,000  |        9,039        |
|      en       |  English   |    Wikipedia     | 10,000 |  200  |  800  | 200,000 |        3,308        |
|      es       |  Spanish   |  Wikipedia, mc4  |  2,254  |  200  |  200  |  9,551  |        8,771        |
|      fr       |   French   |    Wikipedia     |  1,608  |  200  |  200  | 10,000  |        9,659        |
|      hi       |   Hindi    |    Wikipedia     |  1,618  |  200  |  200  |  3,806  |        5,555        |
|      it       |  Italian   |    Wikipedia     |  2,151  |  200  |  200  | 10,000  |        9,195        |
|      ja       |  Japanese  |    Wikipedia     |  2,262  |  200  |  200  | 10,000  |        9,297        |
|      ko       |   Korean   |    Wikipedia     |  2,198  |  200  |  200  |  6,176  |        7,832        |
|      pt       | Portuguese |    Wikipedia     |  1,845  |  200  |  200  |  6,569  |        7,922        |
|      ru       |  Russian   |    Wikipedia     |  1,864  |  200  |  200  | 10,000  |        9,723        |
|      th       |    Thai    |       mC4        |  1,970  |  200  |  200  | 10,000  |        8,089        |
|      zh       |  Chinese   | Wikipedia, Wudao | 10,000  |  200  |  800  | 200,000 |        4,249        |
|     Total     |     -      |        -         | 41,434  | 2,600 | 3,800 | 493,709 |        4,737        |


# Evaluation Pipeline

This task has been merged into [MTEB](https://github.com/embeddings-benchmark/mteb), you can easily use mteb tool to do the evaluation.   
We also provide some [scripts](https://github.com/FlagOpen/FlagEmbedding/tree/master/C_MTEB/MLDR) to test dense retrieval, sparse retrieval and colbert retrieval.


# Dataset Structure
The only configuration here is the `language`. For each language, there are three splits: `train`, `dev`, and `test`. The `corpus` is also avaliable here.

An example of `train` set looks as follows:
```python
{
  'query_id': 'q-zh-<...>', 
  'query': '...', 
  'positive_passages': [
    {
      'docid': 'doc-zh-<...>',
      'text': '...'
    }],
   'negative_passages': [
    {
      'docid': 'doc-zh-<...>',
      'text': '...'
    },
    ...
   ]
}
```

An example of `dev` and `test` set looks as follows.
```python
{
  'query_id': 'q-zh-<...>', 
  'query': '...', 
  'positive_passages': [
    {
      'docid': 'doc-zh-<...>',
      'text': '...'
    }],
   'negative_passages': []
}
```

An example of `corpus` looks as follows.
```python
{
  'docid': 'doc-zh-<...>', 
  'text': '...'
}
```


# Load Dataset

An example to load the dataset:
```python
# Avaliable languages: ['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'zh']
language = 'zh'

# to load all train, dev and test sets
dataset = load_dataset('Shitao/MLDR', language)

# or to load a specific split:
split = 'train'
dataset = load_dataset('Shitao/MLDR', language, split=split)

# load corpus
corpus = load_dataset('Shitao/MLDR', f'corpus-{language}', split='corpus')
```


# Citation Information
```
@misc{bge-m3,
      title={BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation}, 
      author={Jianlv Chen and Shitao Xiao and Peitian Zhang and Kun Luo and Defu Lian and Zheng Liu},
      year={2024},
      eprint={2402.03216},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

