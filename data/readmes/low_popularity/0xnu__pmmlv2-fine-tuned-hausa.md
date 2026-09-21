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
- ha
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

## 0xnu/pmmlv2-fine-tuned-hausa

Hausa fine-tuned LLM using [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2).

[Hausa](https://en.wikipedia.org/wiki/Hausa_language) words typically comprise diverse blends of vowels and consonants. The Hausa language boasts a vibrant phonetic framework featuring twenty-three consonants, five vowels, and two diphthongs. Words in Hausa can fluctuate in length and intricacy, but they usually adhere to uniform configurations of syllable arrangement and articulation. Additionally, Hausa words often incorporate diacritical marks like the apostrophe and macron to signify glottal stops and long vowels.

### Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

### Embeddings

```python
from sentence_transformers import SentenceTransformer
sentences = ["Tambarin talaka cikinsa", "Gwanin dokin wanda yake kansa"]

model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-hausa')
embeddings = model.encode(sentences)
print(embeddings)
```

### Advanced Usage

```sh
from sentence_transformers import SentenceTransformer, util
import torch

# Define sentences in Hausa
sentences = [
    "Menene sunan babban birnin Ingila?",
    "Wanne dabba ne mafi zafi a duniya?",
    "Ta yaya zan iya koyon harshen Hausa?",
    "Wanne abinci ne mafi shahara a Najeriya?",
    "Wane irin kaya ake sawa don bikin Hausa?"
]

# Load the Hausa-trained model
model = SentenceTransformer('path/to/pmmlv2-fine-tuned-hausa')

# Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Function to find the closest sentence
def find_closest_sentence(query_embedding, sentence_embeddings, sentences):
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    # Find the position of the highest score
    best_match_index = torch.argmax(cosine_scores).item()
    return sentences[best_match_index], cosine_scores[best_match_index].item()

query = "Menene sunan babban birnin Ingila?"
query_embedding = model.encode(query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(query_embedding, embeddings, sentences)

print(f"Tambaya: {query}")
print(f"Jimla mafi kusa: {closest_sentence}")
print(f"Alamar kama: {similarity_score:.4f}")

# You can also try with a new sentence not in the original list
new_query = "Wanne sarki ne yake mulkin Kano a yanzu?"
new_query_embedding = model.encode(new_query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(new_query_embedding, embeddings, sentences)

print(f"\nSabuwar Tambaya: {new_query}")
print(f"Jimla mafi kusa: {closest_sentence}")
print(f"Alamar kama: {similarity_score:.4f}")
```

### License

This project is licensed under the [MIT License](./LICENSE).

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).
