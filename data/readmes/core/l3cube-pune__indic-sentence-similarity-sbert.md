---
pipeline_tag: sentence-similarity
license: cc-by-4.0
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language:
- multilingual
- en
- hi
- mr
- kn
- ta
- te
- ml
- gu
- or
- pa
- bn
widget:
- source_sentence: "दिवाळी आपण मोठ्या उत्साहाने साजरी करतो"
  sentences:
    - "दिवाळी आपण आनंदाने साजरी करतो"
    - "दिवाळी हा दिव्यांचा सण आहे"
  example_title: "Monolingual- Marathi"

- source_sentence: "हम दीपावली उत्साह के साथ मनाते हैं"
  sentences:
    - "हम दीपावली खुशियों से मनाते हैं"
    - "दिवाली रोशनी का त्योहार है"
  example_title: "Monolingual- Hindi"

- source_sentence: "અમે ઉત્સાહથી દિવાળી ઉજવીએ છીએ"
  sentences:
    - "દિવાળી આપણે ખુશીઓથી ઉજવીએ છીએ"
    - "દિવાળી એ રોશનીનો તહેવાર છે"
  example_title: "Monolingual- Gujarati"
  
- source_sentence: "आम्हाला भारतीय असल्याचा अभिमान आहे"
  sentences:
    - "हमें भारतीय होने पर गर्व है"
    - "భారతీయులమైనందుకు గర్విస్తున్నాం"
    - "અમને ભારતીય હોવાનો ગર્વ છે"
  example_title: "Cross-lingual 1"

- source_sentence: "ਬਾਰਿਸ਼ ਤੋਂ ਬਾਅਦ ਬਗੀਚਾ ਸੁੰਦਰ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ"
  sentences:
    - "മഴയ്ക്ക് ശേഷം പൂന്തോട്ടം മനോഹരമായി കാണപ്പെടുന്നു"
    - "ବର୍ଷା ପରେ ବଗିଚା ସୁନ୍ଦର ଦେଖାଯାଏ |" 
    - "बारिश के बाद बगीचा सुंदर दिखता है"
  example_title: "Cross-lingual 2"
---

# IndicSBERT-STS

This is a IndicSBERT model (<a href='https://huggingface.co/l3cube-pune/indic-sentence-bert-nli'>l3cube-pune/indic-sentence-bert-nli</a>) trained on the STS dataset of ten major Indian Languages. <br>
The single model works for English, Hindi, Marathi, Kannada, Tamil, Telugu, Gujarati, Oriya, Punjabi, Malayalam, and Bengali.
The model also has cross-lingual capabilities. <br>
Released as a part of project MahaNLP: https://github.com/l3cube-pune/MarathiNLP <br>

Generic Indic Sentence BERT model is shared here : <a href='https://huggingface.co/l3cube-pune/indic-sentence-bert-nli'>l3cube-pune/indic-sentence-bert-nli</a> <br>
More details on the dataset, models, and baseline results can be found in our [paper] (https://arxiv.org/abs/2304.11434)

```
@article{deode2023l3cube,
  title={L3Cube-IndicSBERT: A simple approach for learning cross-lingual sentence representations using multilingual BERT},
  author={Deode, Samruddhi and Gadre, Janhavi and Kajale, Aditi and Joshi, Ananya and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2304.11434},
  year={2023}
}
```

<a href='https://arxiv.org/abs/2211.11187'> monolingual Indic SBERT paper </a> <br>
<a href='https://arxiv.org/abs/2304.11434'> multilingual Indic SBERT paper </a>

Other Monolingual similarity models are listed below: <br>
<a href='https://huggingface.co/l3cube-pune/marathi-sentence-similarity-sbert'> Marathi Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/hindi-sentence-similarity-sbert'> Hindi Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/kannada-sentence-similarity-sbert'> Kannada Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/telugu-sentence-similarity-sbert'> Telugu Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/malayalam-sentence-similarity-sbert'> Malayalam Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/tamil-sentence-similarity-sbert'> Tamil Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/gujarati-sentence-similarity-sbert'> Gujarati Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/odia-sentence-similarity-sbert'> Oriya Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/bengali-sentence-similarity-sbert'> Bengali Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/punjabi-sentence-similarity-sbert'> Punjabi Similarity </a> <br>
<a href='https://huggingface.co/l3cube-pune/indic-sentence-similarity-sbert'> Indic Similarity (multilingual)</a> <br>

Other Monolingual Indic sentence BERT models are listed below: <br>
<a href='https://huggingface.co/l3cube-pune/marathi-sentence-bert-nli'> Marathi SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/hindi-sentence-bert-nli'> Hindi SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/kannada-sentence-bert-nli'> Kannada SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/telugu-sentence-bert-nli'> Telugu SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/malayalam-sentence-bert-nli'> Malayalam SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/tamil-sentence-bert-nli'> Tamil SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/gujarati-sentence-bert-nli'> Gujarati SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/odia-sentence-bert-nli'> Oriya SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/bengali-sentence-bert-nli'> Bengali SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/punjabi-sentence-bert-nli'> Punjabi SBERT</a> <br>
<a href='https://huggingface.co/l3cube-pune/indic-sentence-bert-nli'> Indic SBERT (multilingual)</a> <br>


## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('{MODEL_NAME}')
embeddings = model.encode(sentences)
print(embeddings)
```



## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('{MODEL_NAME}')
model = AutoModel.from_pretrained('{MODEL_NAME}')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```
