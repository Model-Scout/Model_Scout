---
language:
- multilingual
- ar
- bg
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- ka
- ko
- ku
- lt
- lv
- mk
- mn
- mr
- ms
- my
- nb
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- th
- tr
- uk
- ur
- vi
- yo
license: mit
library_name: sentence-transformers
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language_bcp47:
- fr-ca
- pt-br
- zh-cn
- zh-tw
pipeline_tag: sentence-similarity
inference: false
---

## 0xnu/pmmlv2-fine-tuned-yoruba

Yoruba fine-tuned LLM using [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2).

> Yoruba words typically consist of various combinations of vowels and consonants. The Yoruba language has a rich phonetic structure, including eighteen consonants and seven vowels. Words in Yoruba can vary in length and complexity, but they generally follow consistent patterns of syllable structure and pronunciation. Additionally, Yoruba words may include diacritical marks such as accents and underdots to indicate tone and vowel length; they are essential to the language's phonology and meaning.

### Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

### Embeddings

```python
from sentence_transformers import SentenceTransformer
sentences = ["Kini olu ilu England", "Kini eranko ti o gbona julọ ni agbaye?"]

model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-yoruba')
embeddings = model.encode(sentences)
print(embeddings)
```

### Advanced Usage

```python
from sentence_transformers import SentenceTransformer, util
import torch

# Define sentences
sentences = [
    "Kini olu ilu England",
    "Kini eranko ti o gbona julọ ni agbaye?",
    "Bawo ni o se le kọ ede Yoruba?",
    "Kini ounje to gbajumo julọ ni Naijiria?",
    "Iru aso wo ni a maa n wọ fun ijo Yoruba?"
]

# Load the model
model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-yoruba')

# Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Function to find the closest sentence
def find_closest_sentence(query_embedding, sentence_embeddings, sentences):
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    # Find the position of the highest score
    best_match_index = torch.argmax(cosine_scores).item()
    return sentences[best_match_index], cosine_scores[best_match_index].item()

query = "Kini olu ilu England"
query_embedding = model.encode(query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(query_embedding, embeddings, sentences)

print(f"Ibeere: {query}")
print(f"Gbolohun ti o jọ mọ julọ: {closest_sentence}")
print(f"Iwọn ijọra: {similarity_score:.4f}")

# You can also try with a new sentence not in the original list
new_query = "Kini oruko oba to wa ni ilu Oyo?"
new_query_embedding = model.encode(new_query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(new_query_embedding, embeddings, sentences)

print(f"\nIbeere Tuntun: {new_query}")
print(f"Gbolohun ti o jọ mọ julọ: {closest_sentence}")
print(f"Iwọn ijọra: {similarity_score:.4f}")
```

### License

This project is licensed under the [MIT License](./LICENSE).

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).
