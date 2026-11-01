---
language:
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - bo
  - bs
  - ca
  - ceb
  - co
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
  - haw
  - he
  - hi
  - hmn
  - hr
  - ht
  - hu
  - hy
  - id
  - ig
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
  - lb
  - lo
  - lt
  - lv
  - mg
  - mi
  - mk
  - ml
  - mn
  - mr
  - ms
  - mt
  - my
  - ne
  - nl
  - no
  - ny
  - or
  - pa
  - pl
  - pt
  - ro
  - ru
  - rw
  - si
  - sk
  - sl
  - sm
  - sn
  - so
  - sq
  - sr
  - st
  - su
  - sv
  - sw
  - ta
  - te
  - tg
  - th
  - tk
  - tl
  - tr
  - tt
  - ug
  - uk
  - ur
  - uz
  - vi
  - wo
  - xh
  - yi
  - yo
  - zh
  - zu
tags:
- ctranslate2
- int8
- float16
  - bert
  - sentence_embedding
  - multilingual
  - google
  - sentence-similarity
license: apache-2.0
datasets:
  - CommonCrawl
  - Wikipedia
---
# # Fast-Inference with Ctranslate2
Speedup inference while reducing memory by 2x-4x using int8 inference in C++ on CPU or GPU.

quantized version of [setu4993/LaBSE](https://huggingface.co/setu4993/LaBSE)
```bash
pip install hf-hub-ctranslate2>=2.12.0 ctranslate2>=3.17.1
```

```python
# from transformers import AutoTokenizer
model_name = "michaelfeil/ct2fast-LaBSE"
model_name_orig="setu4993/LaBSE"

from hf_hub_ctranslate2 import EncoderCT2fromHfHub
model = EncoderCT2fromHfHub(
        # load in int8 on CUDA
        model_name_or_path=model_name,
        device="cuda",
        compute_type="int8_float16"
)
outputs = model.generate(
    text=["I like soccer", "I like tennis", "The eiffel tower is in Paris"],
    max_length=64,
) # perform downstream tasks on outputs
outputs["pooler_output"]
outputs["last_hidden_state"]
outputs["attention_mask"]

# alternative, use SentenceTransformer Mix-In
# for end-to-end Sentence embeddings generation
# (not pulling from this CT2fast-HF repo)

from hf_hub_ctranslate2 import CT2SentenceTransformer
model = CT2SentenceTransformer(
    model_name_orig, compute_type="int8_float16", device="cuda"
)
embeddings = model.encode(
    ["I like soccer", "I like tennis", "The eiffel tower is in Paris"],
    batch_size=32,
    convert_to_numpy=True,
    normalize_embeddings=True,
)
print(embeddings.shape, embeddings)
scores = (embeddings @ embeddings.T) * 100

# Hint: you can also host this code via REST API and
# via github.com/michaelfeil/infinity  


```

Checkpoint compatible to [ctranslate2>=3.17.1](https://github.com/OpenNMT/CTranslate2)
and [hf-hub-ctranslate2>=2.12.0](https://github.com/michaelfeil/hf-hub-ctranslate2)
- `compute_type=int8_float16` for `device="cuda"`
- `compute_type=int8`  for `device="cpu"`

Converted on 2023-10-13 using
```
LLama-2 -> removed <pad> token.
```

# Licence and other remarks:
This is just a quantized version. Licence conditions are intended to be idential to original huggingface repo.

# Original description
    

# LaBSE

## Model description

Language-agnostic BERT Sentence Encoder (LaBSE) is a BERT-based model trained for sentence embedding for 109 languages. The pre-training process combines masked language modeling with translation language modeling. The model is useful for getting multilingual sentence embeddings and for bi-text retrieval.

- Model: [HuggingFace's model hub](https://huggingface.co/setu4993/LaBSE).
- Paper: [arXiv](https://arxiv.org/abs/2007.01852).
- Original model: [TensorFlow Hub](https://tfhub.dev/google/LaBSE/2).
- Blog post: [Google AI Blog](https://ai.googleblog.com/2020/08/language-agnostic-bert-sentence.html).
- Conversion from TensorFlow to PyTorch: [GitHub](https://github.com/setu4993/convert-labse-tf-pt).

This is migrated from the v2 model on the TF Hub, which uses dict-based input. The embeddings produced by both the versions of the model are [equivalent](https://github.com/setu4993/convert-labse-tf-pt/blob/ec3a019159a54ed6493181a64486c2808c01f216/tests/test_conversion.py#L31).

## Usage

Using the model:

```python
import torch
from transformers import BertModel, BertTokenizerFast


tokenizer = BertTokenizerFast.from_pretrained("setu4993/LaBSE")
model = BertModel.from_pretrained("setu4993/LaBSE")
model = model.eval()

english_sentences = [
    "dog",
    "Puppies are nice.",
    "I enjoy taking long walks along the beach with my dog.",
]
english_inputs = tokenizer(english_sentences, return_tensors="pt", padding=True)

with torch.no_grad():
    english_outputs = model(**english_inputs)
```

To get the sentence embeddings, use the pooler output:

```python
english_embeddings = english_outputs.pooler_output
```

Output for other languages:

```python
italian_sentences = [
    "cane",
    "I cuccioli sono carini.",
    "Mi piace fare lunghe passeggiate lungo la spiaggia con il mio cane.",
]
japanese_sentences = ["犬", "子犬はいいです", "私は犬と一緒にビーチを散歩するのが好きです"]
italian_inputs = tokenizer(italian_sentences, return_tensors="pt", padding=True)
japanese_inputs = tokenizer(japanese_sentences, return_tensors="pt", padding=True)

with torch.no_grad():
    italian_outputs = model(**italian_inputs)
    japanese_outputs = model(**japanese_inputs)

italian_embeddings = italian_outputs.pooler_output
japanese_embeddings = japanese_outputs.pooler_output
```

For similarity between sentences, an L2-norm is recommended before calculating the similarity:

```python
import torch.nn.functional as F


def similarity(embeddings_1, embeddings_2):
    normalized_embeddings_1 = F.normalize(embeddings_1, p=2)
    normalized_embeddings_2 = F.normalize(embeddings_2, p=2)
    return torch.matmul(
        normalized_embeddings_1, normalized_embeddings_2.transpose(0, 1)
    )


print(similarity(english_embeddings, italian_embeddings))
print(similarity(english_embeddings, japanese_embeddings))
print(similarity(italian_embeddings, japanese_embeddings))
```

## Details

Details about data, training, evaluation and performance metrics are available in the [original paper](https://arxiv.org/abs/2007.01852).

### BibTeX entry and citation info

```bibtex
@misc{feng2020languageagnostic,
      title={Language-agnostic BERT Sentence Embedding},
      author={Fangxiaoyu Feng and Yinfei Yang and Daniel Cer and Naveen Arivazhagan and Wei Wang},
      year={2020},
      eprint={2007.01852},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
