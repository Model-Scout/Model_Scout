---
language:
- en
- ko
tags:
- translation
license: cc-by-4.0
datasets:
- quickmt/quickmt-train.ko-en
model-index:
- name: quickmt-en-ko
  results:
  - task:
      name: Translation eng-kor
      type: translation
      args: eng-kor
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng_Latn kor_Hang devtest
    metrics:
    - name: CHRF
      type: chrf
      value: 56.25
    - name: BLEU
      type: bleu
      value: 27.03
    - name: COMET
      type: comet
      value: 86.11 
---


<a href="https://huggingface.co/spaces/quickmt/quickmt-gui"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-lg-dark.svg" alt="Open in Spaces"></a>

# `quickmt-en-ko` Neural Machine Translation Model 

`quickmt-en-ko` is a reasonably fast and reasonably accurate neural machine translation model for translation from `en` into `ko`.



## Model Information

* Trained using [`eole`](https://github.com/eole-nlp/eole)
* 185M parameter transformer 'big' with 8 encoder layers and 2 decoder layers
* 20k sentencepiece vocabularies
* Exported for fast inference to [CTranslate2](https://github.com/OpenNMT/CTranslate2) format
* Training data: https://huggingface.co/datasets/quickmt/quickmt-train.ko-en/tree/main

See the `eole` model configuration in this repository for further details and the `eole-model` for the raw `eole` (pytorch) model.


## Usage with `quickmt`

You must install the Nvidia cuda toolkit first, if you want to do GPU inference.

Next, install the `quickmt` [python library](github.com/quickmt/quickmt). 

```bash
git clone https://github.com/quickmt/quickmt.git
pip install ./quickmt/
```

Finally, use the model in python:

```python
from quickmt import Translator
from huggingface_hub import snapshot_download

# Download Model (if not downloaded already) and return path to local model
# Device is either 'auto', 'cpu' or 'cuda'
t = Translator(
    snapshot_download("quickmt/quickmt-en-ko", ignore_patterns="eole-model/*"),
    device="cpu"
)

# Translate - set beam size to 5 for higher quality (but slower speed)
sample_text = 'Dr. Ehud Ur, professor of medicine at Dalhousie University in Halifax, Nova Scotia and chair of the clinical and scientific division of the Canadian Diabetes Association cautioned that the research is still in its early days.'
t(sample_text, beam_size=5)

# Get alternative translations by sampling
# You can pass any cTranslate2 `translate_batch` arguments
t([sample_text], sampling_temperature=1.2, beam_size=1, sampling_topk=50, sampling_topp=0.9)

> '노바 스코샤 주 핼리팩스에 있는 댈하우지 대학교 의과 교수인 에후드 우르 박사와 캐나다 당뇨병 협회의 임상 및 과학 부문 의장은 이 연구가 아직 초기 단계에 있다고 경고했다.'

```

The model is in `ctranslate2` format, and the tokenizers are `sentencepiece`, so you can use `ctranslate2` directly instead of through `quickmt`. It is also possible  to get this model to work with e.g. [LibreTranslate](https://libretranslate.com/) which also uses `ctranslate2` and `sentencepiece`.


## Metrics

`bleu` and `chrf2` are calculated with [sacrebleu](https://github.com/mjpost/sacrebleu) on the [Flores200 `devtest` test set](https://huggingface.co/datasets/facebook/flores) ("kor_Hang"->"eng_Latn"). `comet22` with the [`comet`](https://github.com/Unbabel/COMET) library and the [default model](https://huggingface.co/Unbabel/wmt22-comet-da). "Time (s)" is the time in seconds to translate (using `ctranslate2`) the flores-devtest dataset (1012 sentences) on an RTX 4070s GPU with batch size 32 (faster speed is possible using a large batch size).


|                                  |   bleu |   chrf2 |   comet22 |   Time (s) |
|:---------------------------------|-------:|--------:|----------:|-----------:|
| quickmt/quickmt-en-ko            |  14.97 |   36.96 |     87.10 |       1.36 |
| facebook/nllb-200-distilled-600M |  12.15 |   33.66 |     87.39 |      24.75 |
| facebook/nllb-200-distilled-1.3B |  13.23 |   35.62 |     88.39 |      40.29 |
| facebook/m2m100_418M             |   9.91 |   30.69 |     83.20 |      22.23 |
| facebook/m2m100_1.2B             |  11.35 |   33.26 |     85.65 |      41.15 |


`quickmt-en-ko` is the fastest and is higher quality than `m2m100_418m`, `m2m100_1.2B` and `nllb-200-distilled-600M`.
