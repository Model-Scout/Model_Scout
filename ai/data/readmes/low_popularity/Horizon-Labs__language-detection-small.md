---
license: apache-2.0
language:
- ace
- afr
- aka
- als
- amh
- arb
- asm
- ast
- awa
- ayr
- azb
- azj
- bak
- bam
- ban
- bel
- bem
- ben
- bho
- bjn
- bod
- bos
- bul
- cat
- ceb
- ces
- ckb
- crh
- cym
- dan
- deu
- dik
- dzo
- ell
- eng
- epo
- est
- eus
- ewe
- fao
- fij
- fin
- fon
- fra
- fur
- fuv
- gaz
- gla
- gle
- glg
- grn
- guj
- hat
- hau
- heb
- hin
- hne
- hrv
- hun
- hye
- ibo
- ilo
- ind
- isl
- ita
- jav
- jpn
- kab
- kac
- kam
- kan
- kas
- kat
- kaz
- kbp
- kea
- khk
- khm
- kik
- kin
- kir
- kmb
- kmr
- knc
- kon
- kor
- lao
- lij
- lim
- lin
- lit
- lmo
- ltg
- ltz
- lua
- lug
- luo
- lus
- lvs
- mag
- mai
- mal
- mar
- min
- mkd
- mlt
- mni
- mos
- mri
- mya
- nld
- nno
- nob
- npi
- nso
- nya
- oci
- ory
- pag
- pan
- pap
- pbt
- pes
- plt
- pol
- por
- quy
- ron
- run
- rus
- sag
- san
- sat
- scn
- shn
- sin
- slk
- slv
- smo
- sna
- snd
- som
- sot
- spa
- srd
- srp
- ssw
- sun
- swe
- swh
- szl
- tam
- taq
- tat
- tel
- tgk
- tgl
- tha
- tir
- tpi
- tsn
- tso
- tuk
- tum
- tur
- tzm
- uig
- ukr
- umb
- urd
- uzn
- vec
- vie
- war
- wol
- xho
- ydd
- yor
- zho
- zsm
- zul
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-small
datasets:
- HuggingFaceFW/fineweb-2
- HuggingFaceFW/fineweb
tags:
- language-identification
- language-detection
- lid
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "Wie spät ist es eigentlich?"
  example_title: "German"
- text: "Habari za asubuhi, rafiki yangu"
  example_title: "Swahili"
- text: "أين محطة القطار؟"
  example_title: "Arabic"
- text: "Tôi muốn đặt một bàn cho hai người"
  example_title: "Vietnamese"
- text: "Kiitos paljon avustasi!"
  example_title: "Finnish"
---

# Language Detection (small, 141M): 183 languages

A fast language identifier for **183 languages** (the FLORES-200 set), built on the multilingual
[mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) encoder. It works on sentences and on short strings (titles,
chat messages, search queries), runs with the standard transformers `text-classification` pipeline, and ships ONNX files
for CPU and the browser (transformers.js). Apache-2.0; trained only on openly licensed web text.

- Labels are FLORES-200 codes: ISO 639-3 language + ISO 15924 script, e.g. `eng_Latn`, `hin_Deva`, `srp_Cyrl`; the full
  list is in `labels.json`. Chinese is one label, `zho_Hani` (Simplified and Traditional together), and **Arabic is one
  label, `arb_Arab`**: the dialect labels (`acm_Arab`, `aeb_Arab`, `apc_Arab`, `ars_Arab`, `ary_Arab`, `arz_Arab`) were too unreliable (they pulled Modern
  Standard Arabic away from the right answer) and are merged; Dyula (`dyu_Latn`) is merged into Bambara (`bam_Latn`).
- You can restrict the prediction to the languages you expect (see Usage), which makes it more accurate on short text.
- `onnx/model_quantized.onnx` (int8 embeddings, 269 MB) picks the same language as fp32 on 100.0% of 400 FLORES sentences and prefixes.

## Usage

```python
from transformers import pipeline

lid = pipeline("text-classification", model="Horizon-Labs/language-detection-small", top_k=3)
lid("Je voudrais réserver une table pour deux personnes.")
# [[{'label': 'fra_Latn', 'score': 0.99...}, ...]]
```

Restrict to candidate languages (recommended when you know the possible set):

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tok = AutoTokenizer.from_pretrained("Horizon-Labs/language-detection-small")
model = AutoModelForSequenceClassification.from_pretrained("Horizon-Labs/language-detection-small").eval()
allowed = ["eng_Latn", "spa_Latn", "por_Latn", "fra_Latn"]
mask = torch.full((model.config.num_labels,), float("-inf"))
mask[[model.config.label2id[l] for l in allowed]] = 0
with torch.no_grad():
    logits = model(**tok(["obrigado pela ajuda"], return_tensors="pt")).logits + mask
print(model.config.id2label[int(logits.argmax(-1))])   # por_Latn
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const lid = await pipeline("text-classification", "Horizon-Labs/language-detection-small", { dtype: "q8" });
console.log(await lid("Dziękuję bardzo!", { top_k: 3 }));
```

## Evaluation

FLORES-200 devtest (1,012 professionally translated sentences per language; evaluation only, never trained on - any
training text containing a FLORES sentence was removed), on the 183 languages this model supports. "First 20-40
characters" cuts every sentence to a short prefix, to measure short-text behaviour. Every model is scored on the same
sentences with the same script; GlotLID and fastText can predict more languages than these, which can only cost them.
The same label merges (Arabic dialects, Dyula, Akan/Twi, Chinese scripts) are applied to every model's predictions.

| | **this model** (141M) | GlotLID (fastText, 1.7 GB) | fastText LID-218 (NLLB, CC-BY-NC) |
|---|---|---|---|
| FLORES-200 devtest, full sentences: accuracy | **0.984** | 0.958 | 0.970 |
| FLORES-200 devtest, full sentences: macro-F1 | **0.983** | 0.958 | 0.970 |
| First 20-40 characters: accuracy | **0.874** | 0.845 | 0.837 |
| First 20-40 characters: macro-F1 | **0.866** | 0.852 | 0.831 |

Against the most-downloaded transformers language detector, on its 20 languages (it can only predict those 20, so the
fair comparison is with our model restricted to the same 20):

| papluca's 20 languages | **this model**, all 183 labels | **this model**, restricted to the 20 | papluca/xlm-roberta-base-language-detection (278M) |
|---|---|---|---|
| full sentences (accuracy) | 0.995 | **1.000** | 0.994 |
| first 20-40 characters (accuracy) | 0.953 | **0.991** | 0.973 |

### Where it is weak

Languages below 0.90 accuracy on full sentences (mostly close varieties such as Bosnian/Croatian and Hindi-belt languages,
or languages with little training text):

| language code | this model | GlotLID |
|---|---|---|
| `bos_Latn` | 0.46 | 0.46 |
| `taq_Latn` | 0.51 | 0.97 |
| `hrv_Latn` | 0.76 | 0.95 |
| `kin_Latn` | 0.81 | 0.95 |
| `mag_Deva` | 0.85 | 0.98 |
| `mos_Latn` | 0.90 | 0.98 |
| `zsm_Latn` | 0.90 | 0.88 |

Not supported: `ace_Arab`, `acq_Arab`, `ajp_Arab`, `bug_Latn`, `cjk_Latn`, `kas_Deva`, `knc_Arab`, `min_Arab`, `nus_Latn`, `prs_Arab`, `taq_Tfng`, `yue_Hant` (no or too little FineWeb-2 text; Cantonese `yue_Hant` because it
could not be told apart from Mandarin and took Mandarin predictions).

## Training

- **Data**: [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) and, for English,
  [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) (both ODC-BY): up to 6,000 samples per language from the
  first files of each language subset, as 1-3 sentence snippets and 10-60 character spans (about 1.6M samples).
- **Cleaning**: FineWeb-2's language labels come from an automatic identifier (GlotLID), and its subsets contain off-language
  pages. We dropped samples whose script does not match the label's script, and non-English Latin-script samples that are
  mostly English function words (about 30k samples, 2%); Akan and Twi share one subset and are one label (`aka_Latn`).
  The model still inherits some label noise from FineWeb-2.
- **Model**: mmBERT-small with a 183-way classification head, 2 epochs, max length 128 tokens.
- Code: `code/` in this repository.

## Limitations

- Close varieties are often confused (see the table above), e.g. Bosnian vs Croatian; Arabic dialects and Cantonese are
  not distinguished (Arabic dialects are reported as `arb_Arab`; Cantonese is not supported).
- Accuracy drops on very short inputs (a few words); restrict the candidates when you can. On 64 everyday phrases we
  wrote ourselves (4 per language in 16 major languages, e.g. "Thank you very much for your help", "Bom dia"), it gets
  56 right; the misses are two-word greetings that go to a close relative ("Goedemorgen" -> Limburgish, "Bom dia" ->
  Kabuverdianu), and confidence on short English phrases is often low even when the label is right.
- Mixed-language text gets one label; romanized text (Hindi, Arabic, Russian written in Latin letters) is not a trained case.
- Chinese Simplified vs Traditional is not distinguished.
