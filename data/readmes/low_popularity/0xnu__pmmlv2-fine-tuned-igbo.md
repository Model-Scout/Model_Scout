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
- ig
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

## 0xnu/pmmlv2-fine-tuned-igbo

Igbo fine-tuned LLM using [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2).

[Igbo](https://en.wikipedia.org/wiki/Igbo_language) words, like those in [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language), are composed of different combinations of vowels and consonants. The Igbo language has a complex phonetic system featuring twenty-eight consonant sounds and eight vowels. Igbo words can range from simple to intricate in their structure, but they adhere to specific patterns of syllable formation and pronunciation. Igbo employs three distinct tones to distinguish meaning: high, low, and downstep. These tones are indicated by diacritical marks, such as acute accents (´), grave accents (`), and macrons (¯), required for accurate pronunciation and comprehension. Furthermore, Igbo words may include digraphs (two-letter combinations representing a single sound) and diphthongs (gliding vowel sounds), adding to the language's phonological richness.

### Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

### Embeddings

```python
from sentence_transformers import SentenceTransformer
sentences = ["Unu bụcha ezigbo mmadụ", "Anyị bụcha ezigbo mmadụ"]

model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-igbo')
embeddings = model.encode(sentences)
print(embeddings)
```

### Advanced Usage

```python
from sentence_transformers import SentenceTransformer, util
import torch

# Define sentences in Igbo
sentences = [
    "Gịnị bụ olu obodo England?",
    "Kedu anụmanụ kachasị ọkụ n'ụwa?",
    "Olee otú e si amụta asụsụ Igbo?",
    "Gịnị bụ nri kachasị ewu ewu na Naịjirịa?",
    "Kedu ụdị uwe a na-eyi maka emume Igbo?"
]

# Load the Igbo-trained model
model = SentenceTransformer('0xnu/pmmlv2-fine-tuned-igbo')

# Compute embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Function to find the closest sentence
def find_closest_sentence(query_embedding, sentence_embeddings, sentences):
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    # Find the position of the highest score
    best_match_index = torch.argmax(cosine_scores).item()
    return sentences[best_match_index], cosine_scores[best_match_index].item()

query = "Gịnị bụ olu obodo England?"
query_embedding = model.encode(query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(query_embedding, embeddings, sentences)

print(f"Ajụjụ: {query}")
print(f"Ahịrịokwu yiri ya kachasị: {closest_sentence}")
print(f"Skọọ nyiri: {similarity_score:.4f}")

# You can also try with a new sentence not in the original list
new_query = "Kedu aha eze nọ n'obodo Enugwu?"
new_query_embedding = model.encode(new_query, convert_to_tensor=True)
closest_sentence, similarity_score = find_closest_sentence(new_query_embedding, embeddings, sentences)

print(f"\nAjụjụ ọhụrụ: {new_query}")
print(f"Ahịrịokwu yiri ya kachasị: {closest_sentence}")
print(f"Skọọ nyiri: {similarity_score:.4f}")
```

### License

This project is licensed under the [MIT License](./LICENSE).

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).
