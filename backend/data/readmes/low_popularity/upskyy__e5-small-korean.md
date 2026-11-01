---
language: 
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
license: mit
library_name: sentence-transformers
tags:
  - korean
  - sentence-transformers
  - transformers
  - multilingual
  - sentence-transformers
  - sentence-similarity
  - feature-extraction
base_model: intfloat/multilingual-e5-small
datasets: []
metrics:
- pearson_cosine
- spearman_cosine
- pearson_manhattan
- spearman_manhattan
- pearson_euclidean
- spearman_euclidean
- pearson_dot
- spearman_dot
- pearson_max
- spearman_max
widget:
- source_sentence: 이집트 군대가 형제애를 단속하다
  sentences:
  - 이집트의 군대가 무슬림 형제애를 단속하다
  - 아르헨티나의 기예르모 코리아와 네덜란드의 마틴 버커크의 또 다른 준결승전도 매력적이다.
  - 그것이 사실일 수도 있다고 생각하는 것은 재미있다.
- source_sentence: 오, 그리고 다시 결혼은 근본적인 인권이라고 주장한다.
  sentences:
  - 특히 결혼은 근본적인 인권이라고 말한 후에.
  - 해변에 있는 흑인과 그의 개...
  - 이란은 핵 프로그램이 평화적인 목적을 위한 것이라고 주장한다
- source_sentence: 한 소년이 파란 플라스틱 슬라이드 위에서 뛰어내린다.
  sentences:
  - 아이들이 놀고 있다
  - 한 소년이 빨간 플라스틱 사다리 꼭대기에서 뛰어내린다.
  - 슬라이드가 있다.
- source_sentence: 감각주의자들은 일부러 오르가즘 없이 섹스를 한다. 그녀는 촛불을 좋아하고, 몸에 기름을 바른 히보스에 대해 쓰고
    있다.
  sentences:
  - 감각주의자들은 섹스하는 동안 오르가즘을 느끼고 싶어한다.
  - 하지만 밤마다 드로잉을 하는 것보다 전국적으로 방송되는 대질심문을 하는 것이 훨씬 더 힘든 일이다, 그래서 미스.
  - 감각주의자들은 일부러 오르가즘 없이 섹스를 한다.
- source_sentence: 조지 샤힌은 안데르센 컨설팅 사업부에서 일했다.
  sentences:
  - 심장 박동이 빨라졌다.
  - 안데르센 컨설팅은 여전히 번창하는 사업이다.
  - 이것은 내가 영국의 아서 안데르센 사업부의 파트너인 짐 와디아를 아서 안데르센 경영진이 선택한 것보다 래리 웨인바흐를 안데르센 월드와이드의
    경영 파트너로 승계하기 위해 안데르센 컨설팅 사업부(현재의 엑센츄어라고 알려져 있음)의 전 관리 파트너인 조지 샤힌에 대한 지지를 표명했을
    때 가장 명백했다.
pipeline_tag: sentence-similarity
model-index:
- name: upskyy/e5-small-korean
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts dev
      type: sts-dev
    metrics:
    - type: pearson_cosine
      value: 0.8479945412588525
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8466656037931976
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.8309207821128262
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.8372540023545114
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.8328087877425099
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.8395342346643203
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.8212157223150336
      name: Pearson Dot
    - type: spearman_dot
      value: 0.8225569441483638
      name: Spearman Dot
    - type: pearson_max
      value: 0.8479945412588525
      name: Pearson Max
    - type: spearman_max
      value: 0.8466656037931976
      name: Spearman Max
---

# upskyy/e5-small-korean

This model is korsts and kornli finetuning model from [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) <!-- at revision fd1525a9fd15316a2d503bf26ab031a61d056e98 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```


## Usage

### Usage (Sentence-Transformers)


First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("upskyy/e5-small-korean")

# Run inference
sentences = [
    '아이를 가진 엄마가 해변을 걷는다.',
    '두 사람이 해변을 걷는다.',
    '한 남자가 해변에서 개를 산책시킨다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

### Usage (HuggingFace Transformers)

Without sentence-transformers, you can use the model like this: 
First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("upskyy/e5-small-korean")
model = AutoModel.from_pretrained("upskyy/e5-small-korean")

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input["attention_mask"])

print("Sentence embeddings:")
print(sentence_embeddings)
```


## Evaluation

### Metrics

#### Semantic Similarity
* Dataset: `sts-dev`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
| :----------------- | :--------- |
| pearson_cosine     | 0.848      |
| spearman_cosine    | 0.8467     |
| pearson_manhattan  | 0.8309     |
| spearman_manhattan | 0.8373     |
| pearson_euclidean  | 0.8328     |
| spearman_euclidean | 0.8395     |
| pearson_dot        | 0.8212     |
| spearman_dot       | 0.8226     |
| **pearson_max**    | **0.848**  |
| **spearman_max**   | **0.8467** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->



### Framework Versions
- Python: 3.10.13
- Sentence Transformers: 3.0.1
- Transformers: 4.42.4
- PyTorch: 2.3.0+cu121
- Accelerate: 0.30.1
- Datasets: 2.16.1
- Tokenizers: 0.19.1

## Citation

### BibTeX

```bibtex
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```

```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```
