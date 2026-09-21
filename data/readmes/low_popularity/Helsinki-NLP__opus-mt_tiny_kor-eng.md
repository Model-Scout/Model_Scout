---
datasets:
- Helsinki-NLP/tatoeba
language:
- ko
- en
metrics:
- bleu
- chrf
pipeline_tag: translation
library_name: transformers

---
# Model info

Distilled model from a Tatoeba-MT Teacher: [Tatoeba-MT-models/kor-eng/opusTCv20210807-sepvoc_transformer-big_2022-07-28](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-eng/opusTCv20210807-sepvoc_transformer-big_2022-07-28.zip), which has been trained on the [Tatoeba](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/data) dataset.

We used the [OpusDistillery](https://github.com/Helsinki-NLP/OpusDistillery) to train new a new student with the tiny architecture, with a regular transformer decoder.
For training data, we used [Tatoeba](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/data).
The configuration file fed into OpusDistillery can be found [here](https://github.com/Helsinki-NLP/OpusDistillery/blob/main/configs/hplt/config.hplt.kor-eng.yml).

## How to run
```python
```python
from transformers import MarianMTModel, MarianTokenizer
model_name = "Helsinki-NLP/opus-mt_tiny_fra-eng"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
tok = tokenizer("2017년 말, 시미노프는 쇼핑 텔레비젼 채널인 QVC에 출연했다.", return_tensors="pt").input_ids
output = model.generate(tok)[0]
tokenizer.decode(output, skip_special_tokens=True)
```

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| flores200 	| 20.3 	| 50.3 |


## Marian models

We also provide Marian-compatible versions of this model. To use them, compile [Marian](https://marian-nmt.github.io/quickstart/) and run decoding with `marian-decoder`, for example:

```bash
marian-decoder \
  -i input.txt \
  -c final.model.npz.best-perplexity.npz.decoder.yml \
  -m final.model.npz.best-perplexity.npz \
  -v vocab.spm vocab.spm