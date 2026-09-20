---
language: 
  - af
  - ar
  - az
  - be
  - bg
  - bn
  - ca
  - ceb
  - cs
  - cy
  - da
  - de
  - el
  - en
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - gl
  - gu
  - he
  - hi
  - hr
  - ht
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
  - ky
  - lo
  - lt
  - lv
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - pa
  - pl
  - pt
  - qu
  - ro
  - ru
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - vi
  - yo
  - zh
library_name: sentence-transformers
tags:
  - korean
  - sentence-transformers
  - transformers
  - multilingual
  - sentence-transformers
  - sentence-similarity
  - feature-extraction
base_model: BAAI/bge-m3
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
- source_sentence: 두 사람이 계단을 올라가 건물 안으로 들어간다
  sentences:
  - 글쎄, 나는 우리가 꽤 나빠진 사이트 목록을 만들었고 일부를 정리해야한다는 일부 사이트에서 알았고 지금 법은 슈퍼 펀드이며 당신이 아무리간에
    독성 폐기물을 일으킨 사람이라면 누구나 알고 있습니다. 결국 당신이 아는 사람은 누구나 땅에 손상을 입혔거나 모두가 기여해야한다는 것을 알고
    있습니다. 그리고 우리가이 돈을 정리하기 위해 수퍼 펀드 거래를 가져 왔을 때 많은 돈을 벌었습니다. 모든 것을 꺼내서 다시 실행하면 다른
    지역을 채울 수 있습니다. 음. 확실히 셔먼 시설과 같은 더 나은 솔루션을 가지고있는 것 같습니다. 기름 통에 넣은 다음 시멘트가 깔려있는
    곳에서 밀봉하십시오.
  - 한 사람이 계단을 올라간다.
  - 두 사람이 함께 계단을 올라간다.
- source_sentence: 그래, 내가 알아차린 적이 있어
  sentences:
  - 나는 알아차리지 못했다.
  - 이것은 내가 영국의 아서 안데르센 사업부의 파트너인 짐 와디아를 아서 안데르센 경영진이 선택한 것보다 래리 웨인바흐를 안데르센 월드와이드의
    경영 파트너로 승계하기 위해 안데르센 컨설팅 사업부(현재의 엑센츄어라고 알려져 있음)의 전 관리 파트너인 조지 샤힌에 대한 지지를 표명했을
    때 가장 명백했다.
  - 나는 메모했다.
- source_sentence: 여자가 전화를 하는 동안 두 남자가 돈을 위해 악기를 연주한다.
  sentences:
  - 마이크에 대고 노래를 부르고 베이스를 연주하는 남자.
  - 빨대를 사용하는 아이
  - 돈을 위해 악기를 연주하는 사람들
pipeline_tag: sentence-similarity
model-index:
- name: upskyy/bge-m3-korean
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts dev
      type: sts-dev
    metrics:
    - type: pearson_cosine
      value: 0.8740181295716805
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8723737976913686
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.8593266961329962
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.8687629058449345
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.8597907936339472
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.8693987158996017
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.8683777071455441
      name: Pearson Dot
    - type: spearman_dot
      value: 0.8665500024614361
      name: Spearman Dot
    - type: pearson_max
      value: 0.8740181295716805
      name: Pearson Max
    - type: spearman_max
      value: 0.8723737976913686
      name: Spearman Max
---

# upskyy/bge-m3-korean

This model is korsts and kornli finetuning model from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) <!-- at revision 5617a9f61b028005a4858fdac845db406aefb181 -->
- **Maximum Sequence Length:** **8192 tokens**
- **Output Dimensionality:** 1024 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("upskyy/bge-m3-korean")

# Run inference
sentences = [
    '아이를 가진 엄마가 해변을 걷는다.',
    '두 사람이 해변을 걷는다.',
    '한 남자가 해변에서 개를 산책시킨다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
print(similarities)
# tensor([[1.0000, 0.6173, 0.3672],
#         [0.6173, 1.0000, 0.4775],
#         [0.3672, 0.4775, 1.0000]])
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
tokenizer = AutoTokenizer.from_pretrained("upskyy/bge-m3-korean")
model = AutoModel.from_pretrained("upskyy/bge-m3-korean")

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
| pearson_cosine     | 0.874      |
| spearman_cosine    | 0.8724     |
| pearson_manhattan  | 0.8593     |
| spearman_manhattan | 0.8688     |
| pearson_euclidean  | 0.8598     |
| spearman_euclidean | 0.8694     |
| pearson_dot        | 0.8684     |
| spearman_dot       | 0.8666     |
| **pearson_max**    | **0.874**  |
| **spearman_max**   | **0.8724** |

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
@misc{bge-m3,
      title={BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation}, 
      author={Jianlv Chen and Shitao Xiao and Peitian Zhang and Kun Luo and Defu Lian and Zheng Liu},
      year={2024},
      eprint={2402.03216},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
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
