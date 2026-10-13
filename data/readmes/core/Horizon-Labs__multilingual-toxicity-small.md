---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- cs
- ro
- sv
- da
- fi
- hu
- el
- tr
- ar
- he
- fa
- hi
- bn
- ur
- zh
- ja
- ko
- vi
- th
- id
- sw
- am
- tt
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-small
datasets:
- google/civil_comments
- Horizon-Labs/civil-comments-multilingual
tags:
- toxicity
- toxic-comment-classification
- content-moderation
- detoxify
- multi-label-classification
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "Thanks for sharing, this was really helpful!"
  example_title: "Harmless"
- text: "You are a complete idiot and nobody wants you here."
  example_title: "Insult"
- text: "Halt die Klappe, du Vollidiot."
  example_title: "German"
- text: "Eres un inútil, lárgate de aquí."
  example_title: "Spanish"
---

# Multilingual Toxicity (small, 141M): Detoxify labels in many languages

A multi-label toxic-comment classifier with the labels of [Detoxify](https://github.com/unitaryai/detoxify) /
[unitary/unbiased-toxic-roberta](https://huggingface.co/unitary/unbiased-toxic-roberta): **toxicity, severe_toxicity,
obscene, threat, insult, identity_attack, sexual_explicit**. It works on comments in English and 33 other languages.
Built on [mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) and trained on Civil Comments (CC0) plus translations,
so it is a multilingual drop-in for Detoxify-style moderation. Apache-2.0. ONNX files for CPU and the browser
(transformers.js) are included.
A larger, more accurate version is available as [Horizon-Labs/multilingual-toxicity-base](https://huggingface.co/Horizon-Labs/multilingual-toxicity-base).

- Each label gets an independent probability (sigmoid), as in Detoxify. A common choice is to flag a comment when
  `toxicity >= 0.5`, but tune the threshold for your platform. Scores for non-English text tend to be lower than for
  English (see F1 @ 0.5 below), so a lower threshold may suit multilingual content. Check it on your own data.
- For harmful requests to an LLM (weapons, self-harm, etc.) rather than rude comments, see our
  [content-safety-guard](https://huggingface.co/Horizon-Labs/content-safety-guard-small).
- For hate speech specifically (attacks on people because of race, religion, origin, gender, sexuality, age or disability,
  with the targeted group), see [multilingual-hate-speech-base](https://huggingface.co/Horizon-Labs/multilingual-hate-speech-base).
- `onnx/model_quantized.onnx` (int8 embeddings, 268 MB): probabilities differ from fp32 by 0.0009 on average over 448 test texts.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/multilingual-toxicity-small", top_k=None)
print(clf("Halt die Klappe, du Vollidiot."))
# [[{'label': 'toxicity', 'score': ...}, {'label': 'insult', 'score': ...}, ...]]
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/multilingual-toxicity-small", { dtype: "q8" });
console.log(await clf("Eres un inútil, lárgate de aquí.", { top_k: null }));
```

## Evaluation

The benchmarks were used only for evaluation, and training texts that also occur in them were removed.

- **Civil Comments test** (English, 20,000 random comments): ROC AUC per label, with labels binarised at >= 0.5 as in the
  Jigsaw competitions. The table gives the mean over the 6 labels that have at least 20 positives (severe_toxicity
  has none at that threshold), and the toxicity AUC. Models without a label are scored on the labels they have.
- **TextDetox** ([textdetox/multilingual_toxicity_dataset](https://huggingface.co/datasets/textdetox/multilingual_toxicity_dataset)):
  binary toxic/non-toxic in 15 languages, 1,000 balanced texts each. The score is ROC AUC of each model's toxicity
  probability, plus F1 at 0.5.

| model | licence | Civil Comments, mean AUC (6 labels) | Civil Comments, toxicity AUC | TextDetox (15 languages), AUC | TextDetox, F1 @ 0.5 | labels |
|---|---|---|---|---|---|---|
| **this model** (141M) | Apache-2.0 | 0.988 | 0.972 | 0.835 | 0.547 | 7 Detoxify labels, multilingual |
| [Horizon-Labs/multilingual-toxicity-base](https://huggingface.co/Horizon-Labs/multilingual-toxicity-base) (308M) | Apache-2.0 | 0.988 | 0.971 | 0.854 | 0.433 |  |
| [unitary/unbiased-toxic-roberta](https://huggingface.co/unitary/unbiased-toxic-roberta) (125M) | Apache-2.0 | 0.985 | 0.969 | 0.588 | 0.086 | 7 Detoxify labels (+ identity labels), English |
| [unitary/toxic-bert](https://huggingface.co/unitary/toxic-bert) (110M) | Apache-2.0 | 0.946 | 0.926 | 0.623 | 0.142 | 6 labels, English |
| [s-nlp/roberta_toxicity_classifier](https://huggingface.co/s-nlp/roberta_toxicity_classifier) (125M) | OpenRAIL++ | 0.975 | 0.975 | 0.642 | 0.092 | binary, English |
| [martin-ha/toxic-comment-model](https://huggingface.co/martin-ha/toxic-comment-model) (67M) | none given | 0.943 | 0.943 | 0.572 | 0.160 | binary, English |
| [unitary/multilingual-toxic-xlm-roberta](https://huggingface.co/unitary/multilingual-toxic-xlm-roberta) (278M) | Apache-2.0 | 0.961 | 0.961 | 0.678 | 0.352 | 1 label, multilingual |
| [citizenlab/distilbert-base-multilingual-cased-toxicity](https://huggingface.co/citizenlab/distilbert-base-multilingual-cased-toxicity) (135M) | none given | 0.843 | 0.843 | 0.698 | 0.277 | binary, multilingual |
| [textdetox/xlmr-large-toxicity-classifier](https://huggingface.co/textdetox/xlmr-large-toxicity-classifier) (560M) | OpenRAIL++ | 0.869 | 0.869 | 0.922 | 0.878 | binary, multilingual; trained on TextDetox data |
| [textdetox/xlmr-large-toxicity-classifier-v2](https://huggingface.co/textdetox/xlmr-large-toxicity-classifier-v2) (560M) | OpenRAIL++ | 0.895 | 0.895 | 0.987 | 0.961 | binary, multilingual; trained on TextDetox data |
| [gravitee-io/distilbert-multilingual-toxicity-classifier](https://huggingface.co/gravitee-io/distilbert-multilingual-toxicity-classifier) (135M) | OpenRAIL++ | 0.809 | 0.809 | 0.941 | 0.896 | binary, multilingual; trained on TextDetox data (ONNX copy: onnx-community/distilbert-multilingual-toxicity-classifier) |

- The table shows the released checkpoint. Means over two training seeds: small Civil Comments mean AUC .988 / toxicity .972 / TextDetox .838; base .988 / .972 / .855.
- Models ahead of this one: Civil Comments mean AUC: none (single-label models are
  scored on their one label, so compare the toxicity column too); Civil Comments toxicity AUC: roberta_toxicity_classifier; TextDetox AUC:
  xlmr-large-toxicity-classifier, xlmr-large-toxicity-classifier-v2, distilbert-multilingual-toxicity-classifier. The English models
  were trained on Jigsaw/Civil Comments data, the same source as this test set. The three TextDetox-trained models were trained on
  TextDetox data (so that column is in-domain for them); on Civil Comments they score 0.81-0.90 versus 0.97-0.99 here.

Per label (Civil Comments, AUC):

| label | this model | unbiased-toxic-roberta |
|---|---|---|
| toxicity | 0.972 | 0.969 |
| obscene | 0.995 | 0.991 |
| threat | 0.994 | 0.985 |
| insult | 0.980 | 0.980 |
| identity_attack | 0.988 | 0.987 |
| sexual_explicit | 0.997 | 0.996 |

Per TextDetox language (AUC):

| language | this model (AUC) | multilingual-toxic-xlm-roberta | xlmr-large-toxicity (in-domain) |
|---|---|---|---|
| Amharic | 0.636 | 0.548 | 0.982 |
| Arabic | 0.721 | 0.413 | 0.989 |
| German | 0.859 | 0.662 | 0.997 |
| English | 0.990 | 0.992 | 1.000 |
| Spanish | 0.899 | 0.819 | 0.998 |
| French | 0.984 | 0.981 | 0.971 |
| Hebrew | 0.778 | 0.501 | 0.701 |
| Hindi | 0.897 | 0.644 | 0.995 |
| Hinglish (romanised Hindi) | 0.749 | 0.631 | 0.756 |
| Italian | 0.840 | 0.818 | 0.805 |
| Japanese | 0.831 | 0.506 | 0.852 |
| Russian | 0.956 | 0.807 | 1.000 |
| Tatar | 0.808 | 0.626 | 0.806 |
| Ukrainian | 0.808 | 0.680 | 0.996 |
| Chinese | 0.771 | 0.547 | 0.979 |

## Training

- **Data**: 518,854 English comments from [Civil Comments](https://huggingface.co/datasets/google/civil_comments)
  (CC0; enriched for toxic ones), with their fractional annotator labels. Qwen3.8-27B (Apache-2.0) translated
  390,862 of them into 33 languages, about 12,000 per language and half of them toxic. It was told to
  keep insults, profanity and threats intact, and the labels are copied to each translation (published as
  [Horizon-Labs/civil-comments-multilingual](https://huggingface.co/datasets/Horizon-Labs/civil-comments-multilingual)).
- **Model**: mmBERT-small with 7 sigmoid outputs, binary cross-entropy on the fractional labels (as in Detoxify), max
  length 256 tokens. The checkpoint was chosen by mean AUC on held-out comments and their translations.
- Code: `code/` in this repository.

## Limitations

- Toxicity labels are subjective and culture-dependent. Translated comments keep English annotators' judgements, and
  slurs or insults that exist only in other languages are under-represented.
- Like other toxicity models, it can over-flag mentions of identity groups and reclaimed or quoted language, and miss
  implicit or sarcastic abuse. Do not use it as the only basis for decisions about people.
- Accuracy is lower for low-resource languages, where both translation and the base model are weaker (see the per-language table).
