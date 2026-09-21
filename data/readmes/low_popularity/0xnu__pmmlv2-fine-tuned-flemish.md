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
- vls
- zea
- lim
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

## 0xnu/pmmlv2-fine-tuned-flemish

Flemish fine-tuned LLM using [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2).

[Flemish](https://en.wikipedia.org/wiki/Flemish_dialects) words typically consist of various combinations of vowels and consonants. The Flemish language has a diverse phonetic structure, including twenty-two consonants, twelve vowels, and some diphthongs. The language also features many loanwords from French, Latin, and other languages, adopted and adapted over time to fit the language's phonetic and grammatical structure.

### Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

### Embeddings

```python
from sentence_transformers import SentenceTransformer
sentences = ["Met de deur in huis vallen", "Niet geschoten is altijd mis"]

model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-flemish')
embeddings = model.encode(sentences)
print(embeddings)
```

### Advanced Usage

```python
from sentence_transformers import SentenceTransformer, util
import torch

# Define sentences in Flemish
sentences = [
    "Wat is de hoofdstad van Engeland?",
    "Welk dier is het warmste ter wereld?",
    "Hoe kan ik Vlaams leren?",
    "Wat is het meest populaire gerecht in België?",
    "Welk soort kleding draagt men voor Vlaamse feesten?"
]

# Load the Flemish-trained model
model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-flemish')

# Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Function to find the closest sentence
def find_closest_sentence(query_embedding, sentence_embeddings, sentences):
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    # Find the position of the highest score
    best_match_index = torch.argmax(cosine_scores).item()
    return sentences[best_match_index], cosine_scores[best_match_index].item()

query = "Wat is de hoofdstad van Engeland?"
query_embedding = model.encode(query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(query_embedding, embeddings, sentences)

print(f"Vraag: {query}")
print(f"Meest gelijkende zin: {closest_sentence}")
print(f"Overeenkomstscore: {similarity_score:.4f}")

# You can also try with a new sentence not in the original list
new_query = "Wie is de huidige koning van België?"
new_query_embedding = model.encode(new_query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(new_query_embedding, embeddings, sentences)

print(f"\nNieuwe vraag: {new_query}")
print(f"Meest gelijkende zin: {closest_sentence}")
print(f"Overeenkomstscore: {similarity_score:.4f}")
```

### License

This project is licensed under the [MIT License](./LICENSE).

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).
