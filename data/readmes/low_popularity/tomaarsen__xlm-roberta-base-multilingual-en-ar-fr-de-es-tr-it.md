---
language:
- en
- multilingual
- ar
- bg
- ca
- cs
- da
- de
- el
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
- zh
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- loss:MSELoss
base_model: FacebookAI/xlm-roberta-base
metrics:
- negative_mse
- src2trg_accuracy
- trg2src_accuracy
- mean_accuracy
- pearson_cosine
- spearman_cosine
- pearson_manhattan
- spearman_manhattan
- pearson_euclidean
- spearman_euclidean
- pearson_dot
- spearman_dot
- pearson_max
- spearman_max
widget:
- source_sentence: Grazie tante.
  sentences:
  - Grazie infinite.
  - Non c'è un solo architetto diplomato in tutta la Contea.
  - Le aziende non credevano che fosse loro responsabilità.
- source_sentence: Avance rapide.
  sentences:
  - Très bien.
  - Donc, je voulais faire quelque chose de spécial aujourd'hui.
  - Et ils ne tiennent pas non plus compte des civils qui souffrent de façon plus
    générale.
- source_sentence: E' importante.
  sentences:
  - E' una materia fondamentale.
  - Sono qui oggi per mostrare le mie fotografie dei Lakota.
  - Non ero seguito da un corteo di macchine.
- source_sentence: Müfettişler…
  sentences:
  - İşçi sınıfına dair birşey.
  - Antlaşmaya göre, o topraklar bağımsız bir ulustur.
  - Son derece düz ve bataklık bir coğrafya.
- source_sentence: Wir sind eins.
  sentences:
  - Das versuchen wir zu bieten.
  - Ihre Gehirne sind ungefähr 100 Millionen Mal komplizierter.
  - Hinter mir war gar keine Autokolonne.
pipeline_tag: sentence-similarity
co2_eq_emissions:
  emissions: 23.27766676567869
  energy_consumed: 0.05988563672345058
  source: codecarbon
  training_type: fine-tuning
  on_cloud: false
  cpu_model: 13th Gen Intel(R) Core(TM) i7-13700K
  ram_total_size: 31.777088165283203
  hours_used: 0.179
  hardware_used: 1 x NVIDIA GeForce RTX 3090
model-index:
- name: SentenceTransformer based on FacebookAI/xlm-roberta-base
  results:
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en ar
      type: en-ar
    metrics:
    - type: negative_mse
      value: -20.395545661449432
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en ar
      type: en-ar
    metrics:
    - type: src2trg_accuracy
      value: 0.7603222557905337
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.7824773413897281
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.7713997985901309
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 en ar test
      type: sts17-en-ar-test
    metrics:
    - type: pearson_cosine
      value: 0.40984231242712876
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.4425400227662121
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.4068582195810505
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.4194184278683204
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.38014538983821944
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.38651157412220366
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.4077636003696869
      name: Pearson Dot
    - type: spearman_dot
      value: 0.37682818098716137
      name: Spearman Dot
    - type: pearson_max
      value: 0.40984231242712876
      name: Pearson Max
    - type: spearman_max
      value: 0.4425400227662121
      name: Spearman Max
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en fr
      type: en-fr
    metrics:
    - type: negative_mse
      value: -19.62321847677231
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en fr
      type: en-fr
    metrics:
    - type: src2trg_accuracy
      value: 0.8981854838709677
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.8901209677419355
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.8941532258064516
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 fr en test
      type: sts17-fr-en-test
    metrics:
    - type: pearson_cosine
      value: 0.5017606394120642
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.5333594401322842
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.4461108010622129
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.45470883061015244
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.44313058261278737
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.44806261424208443
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.40165874540768454
      name: Pearson Dot
    - type: spearman_dot
      value: 0.41339619568003433
      name: Spearman Dot
    - type: pearson_max
      value: 0.5017606394120642
      name: Pearson Max
    - type: spearman_max
      value: 0.5333594401322842
      name: Spearman Max
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en de
      type: en-de
    metrics:
    - type: negative_mse
      value: -19.727922976017
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en de
      type: en-de
    metrics:
    - type: src2trg_accuracy
      value: 0.8920282542885973
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.8910191725529768
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.8915237134207871
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 en de test
      type: sts17-en-de-test
    metrics:
    - type: pearson_cosine
      value: 0.5262798164154752
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.5618005565496922
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.5084907192868734
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.5218456102379673
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.5055278909013912
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.5206420646365548
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.3742195121194434
      name: Pearson Dot
    - type: spearman_dot
      value: 0.3691237073066472
      name: Spearman Dot
    - type: pearson_max
      value: 0.5262798164154752
      name: Pearson Max
    - type: spearman_max
      value: 0.5618005565496922
      name: Spearman Max
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en es
      type: en-es
    metrics:
    - type: negative_mse
      value: -19.472387433052063
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en es
      type: en-es
    metrics:
    - type: src2trg_accuracy
      value: 0.9434343434343434
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.9464646464646465
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.944949494949495
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 es en test
      type: sts17-es-en-test
    metrics:
    - type: pearson_cosine
      value: 0.4944989376773328
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.502096516024397
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.44447965250345656
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.428444032581959
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.43569887867301704
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.4169602915053127
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.3751122541083453
      name: Pearson Dot
    - type: spearman_dot
      value: 0.37961391381473436
      name: Spearman Dot
    - type: pearson_max
      value: 0.4944989376773328
      name: Pearson Max
    - type: spearman_max
      value: 0.502096516024397
      name: Spearman Max
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en tr
      type: en-tr
    metrics:
    - type: negative_mse
      value: -20.754697918891907
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en tr
      type: en-tr
    metrics:
    - type: src2trg_accuracy
      value: 0.743202416918429
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.743202416918429
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.743202416918429
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 en tr test
      type: sts17-en-tr-test
    metrics:
    - type: pearson_cosine
      value: 0.5544917743538167
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.581923120433332
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.5103770986779784
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.5087986920849596
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.5045523005860614
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.5053157708914061
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.47262046401401747
      name: Pearson Dot
    - type: spearman_dot
      value: 0.4297595645819756
      name: Spearman Dot
    - type: pearson_max
      value: 0.5544917743538167
      name: Pearson Max
    - type: spearman_max
      value: 0.581923120433332
      name: Spearman Max
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: en it
      type: en-it
    metrics:
    - type: negative_mse
      value: -19.76993829011917
      name: Negative Mse
  - task:
      type: translation
      name: Translation
    dataset:
      name: en it
      type: en-it
    metrics:
    - type: src2trg_accuracy
      value: 0.878147029204431
      name: Src2Trg Accuracy
    - type: trg2src_accuracy
      value: 0.8831822759315207
      name: Trg2Src Accuracy
    - type: mean_accuracy
      value: 0.8806646525679758
      name: Mean Accuracy
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts17 it en test
      type: sts17-it-en-test
    metrics:
    - type: pearson_cosine
      value: 0.506365733914274
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.5250284136808592
      name: Spearman Cosine
    - type: pearson_manhattan
      value: 0.45167598168533407
      name: Pearson Manhattan
    - type: spearman_manhattan
      value: 0.46227952068355316
      name: Spearman Manhattan
    - type: pearson_euclidean
      value: 0.4423426674780287
      name: Pearson Euclidean
    - type: spearman_euclidean
      value: 0.45072801992723094
      name: Spearman Euclidean
    - type: pearson_dot
      value: 0.4201989776020174
      name: Pearson Dot
    - type: spearman_dot
      value: 0.42253906764732746
      name: Spearman Dot
    - type: pearson_max
      value: 0.506365733914274
      name: Pearson Max
    - type: spearman_max
      value: 0.5250284136808592
      name: Spearman Max
---

# SentenceTransformer based on FacebookAI/xlm-roberta-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) on the [en-ar](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks), [en-fr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks), [en-de](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks), [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks), [en-tr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) and [en-it](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) datasets. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) <!-- at revision e73636d4f797dec63c3081bb6ed5c7b0bb3f2089 -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
- **Training Datasets:**
    - [en-ar](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
    - [en-fr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
    - [en-de](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
    - [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
    - [en-tr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
    - [en-it](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
- **Languages:** en, multilingual, ar, bg, ca, cs, da, de, el, es, et, fa, fi, fr, gl, gu, he, hi, hr, hu, hy, id, it, ja, ka, ko, ku, lt, lv, mk, mn, mr, ms, my, nb, nl, pl, pt, ro, ru, sk, sl, sq, sr, sv, th, tr, uk, ur, vi, zh
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("tomaarsen/xlm-roberta-base-multilingual-en-ar-fr-de-es-tr-it")
# Run inference
sentences = [
    'Wir sind eins.',
    'Das versuchen wir zu bieten.',
    'Ihre Gehirne sind ungefähr 100 Millionen Mal komplizierter.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Knowledge Distillation
* Dataset: `en-ar`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-20.3955** |

#### Translation
* Dataset: `en-ar`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.7603     |
| trg2src_accuracy  | 0.7825     |
| **mean_accuracy** | **0.7714** |

#### Semantic Similarity
* Dataset: `sts17-en-ar-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.4098     |
| spearman_cosine    | 0.4425     |
| pearson_manhattan  | 0.4069     |
| spearman_manhattan | 0.4194     |
| pearson_euclidean  | 0.3801     |
| spearman_euclidean | 0.3865     |
| pearson_dot        | 0.4078     |
| spearman_dot       | 0.3768     |
| pearson_max        | 0.4098     |
| **spearman_max**   | **0.4425** |

#### Knowledge Distillation
* Dataset: `en-fr`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-19.6232** |

#### Translation
* Dataset: `en-fr`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.8982     |
| trg2src_accuracy  | 0.8901     |
| **mean_accuracy** | **0.8942** |

#### Semantic Similarity
* Dataset: `sts17-fr-en-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.5018     |
| spearman_cosine    | 0.5334     |
| pearson_manhattan  | 0.4461     |
| spearman_manhattan | 0.4547     |
| pearson_euclidean  | 0.4431     |
| spearman_euclidean | 0.4481     |
| pearson_dot        | 0.4017     |
| spearman_dot       | 0.4134     |
| pearson_max        | 0.5018     |
| **spearman_max**   | **0.5334** |

#### Knowledge Distillation
* Dataset: `en-de`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-19.7279** |

#### Translation
* Dataset: `en-de`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.892      |
| trg2src_accuracy  | 0.891      |
| **mean_accuracy** | **0.8915** |

#### Semantic Similarity
* Dataset: `sts17-en-de-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.5263     |
| spearman_cosine    | 0.5618     |
| pearson_manhattan  | 0.5085     |
| spearman_manhattan | 0.5218     |
| pearson_euclidean  | 0.5055     |
| spearman_euclidean | 0.5206     |
| pearson_dot        | 0.3742     |
| spearman_dot       | 0.3691     |
| pearson_max        | 0.5263     |
| **spearman_max**   | **0.5618** |

#### Knowledge Distillation
* Dataset: `en-es`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-19.4724** |

#### Translation
* Dataset: `en-es`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.9434     |
| trg2src_accuracy  | 0.9465     |
| **mean_accuracy** | **0.9449** |

#### Semantic Similarity
* Dataset: `sts17-es-en-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.4945     |
| spearman_cosine    | 0.5021     |
| pearson_manhattan  | 0.4445     |
| spearman_manhattan | 0.4284     |
| pearson_euclidean  | 0.4357     |
| spearman_euclidean | 0.417      |
| pearson_dot        | 0.3751     |
| spearman_dot       | 0.3796     |
| pearson_max        | 0.4945     |
| **spearman_max**   | **0.5021** |

#### Knowledge Distillation
* Dataset: `en-tr`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-20.7547** |

#### Translation
* Dataset: `en-tr`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.7432     |
| trg2src_accuracy  | 0.7432     |
| **mean_accuracy** | **0.7432** |

#### Semantic Similarity
* Dataset: `sts17-en-tr-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value      |
|:-------------------|:-----------|
| pearson_cosine     | 0.5545     |
| spearman_cosine    | 0.5819     |
| pearson_manhattan  | 0.5104     |
| spearman_manhattan | 0.5088     |
| pearson_euclidean  | 0.5046     |
| spearman_euclidean | 0.5053     |
| pearson_dot        | 0.4726     |
| spearman_dot       | 0.4298     |
| pearson_max        | 0.5545     |
| **spearman_max**   | **0.5819** |

#### Knowledge Distillation
* Dataset: `en-it`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | Value        |
|:-----------------|:-------------|
| **negative_mse** | **-19.7699** |

#### Translation
* Dataset: `en-it`
* Evaluated with [<code>TranslationEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator)

| Metric            | Value      |
|:------------------|:-----------|
| src2trg_accuracy  | 0.8781     |
| trg2src_accuracy  | 0.8832     |
| **mean_accuracy** | **0.8807** |

#### Semantic Similarity
* Dataset: `sts17-it-en-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric             | Value     |
|:-------------------|:----------|
| pearson_cosine     | 0.5064    |
| spearman_cosine    | 0.525     |
| pearson_manhattan  | 0.4517    |
| spearman_manhattan | 0.4623    |
| pearson_euclidean  | 0.4423    |
| spearman_euclidean | 0.4507    |
| pearson_dot        | 0.4202    |
| spearman_dot       | 0.4225    |
| pearson_max        | 0.5064    |
| **spearman_max**   | **0.525** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Datasets

#### en-ar

* Dataset: [en-ar](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                       | label                                |
  |:--------|:----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 27.3 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                             | label                                                                                                                       |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
  | <code>حسناً ان ما نقوم به اليوم .. هو ان نجبر الطلاب لتعلم الرياضيات</code>                                                                                             | <code>[0.3943225145339966, 0.18910610675811768, -0.3788299858570099, 0.4386662542819977, 0.2727023661136627, ...]</code>    |
  | <code>انها المادة الاهم ..</code>                                                                                                                                       | <code>[0.6257511377334595, -0.1750679910182953, -0.5734405517578125, 0.11480475962162018, 1.1682192087173462, ...]</code>   |
  | <code>انا لا انفي لدقيقة واحدة ان الذين يهتمون بالحسابات اليدوية والذين هوايتهم القيام بذلك .. او القيام بالطرق التقليدية في اي مجال ان يقوموا بذلك كما يريدون .</code> | <code>[-0.04564047232270241, 0.4971524775028229, 0.28066301345825195, -0.726702094078064, -0.17846377193927765, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-fr

* Dataset: [en-fr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 3 tokens</li><li>mean: 30.18 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                                                                         | label                                                                                                                        |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Je ne crois pas que ce soit justifié.</code>                                                                                                                                                                  | <code>[-0.361753910779953, 0.7323777079582214, 0.6518164277076721, -0.8461216688156128, -0.007496988866478205, ...]</code>   |
  | <code>Je fais cette distinction entre ce qu'on force les gens à faire et les matières générales, et la matière que quelqu'un va apprendre parce que ça lui plait et peut-être même exceller dans ce domaine.</code> | <code>[0.3047865629196167, 0.5270194411277771, 0.26616284251213074, 0.2612147927284241, 0.1950961947441101, ...]</code>      |
  | <code>Quels sont les problèmes en relation avec ça?</code>                                                                                                                                                          | <code>[0.2123892903327942, -0.09616081416606903, -0.41965243220329285, -0.5469444394111633, -0.6056491136550903, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-de

* Dataset: [en-de](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 27.04 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                         | label                                                                                                                        |
  |:----------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Ich denke, dass es sich aus diesem Grund lohnt, den Leuten das Rechnen von Hand beizubringen.</code>                                          | <code>[0.0960279330611229, 0.7833179831504822, -0.09527698159217834, 0.8104371428489685, 0.7545774579048157, ...]</code>     |
  | <code>Außerdem gibt es ein paar bestimmte konzeptionelle Dinge, die das Rechnen per Hand rechtfertigen, aber ich glaube es sind sehr wenige.</code> | <code>[-0.5939837098121643, 0.9714100956916809, 0.6800686717033386, -0.21585524082183838, -0.7509503364562988, ...]</code>   |
  | <code>Eine Sache, die ich mich oft frage, ist Altgriechisch, und wie das zusammengehört.</code>                                                     | <code>[-0.09777048230171204, 0.07093209028244019, -0.42989012598991394, -0.1457514613866806, 1.4382753372192383, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-es

* Dataset: [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.42 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                              | label                                                                                                                        |
  |:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Y luego hay ciertas aspectos conceptuales que pueden beneficiarse del cálculo a mano pero creo que son relativamente pocos.</code> | <code>[-0.5939835906028748, 0.9714106917381287, 0.6800685524940491, -0.2158554196357727, -0.7509507536888123, ...]</code>    |
  | <code>Algo que pregunto a menudo es sobre el griego antiguo y cómo se relaciona.</code>                                                  | <code>[-0.09777048230171204, 0.07093209028244019, -0.42989012598991394, -0.1457514613866806, 1.4382753372192383, ...]</code> |
  | <code>Vean, lo que estamos haciendo ahora es forzar a la gente a aprender matemáticas.</code>                                            | <code>[0.3943225145339966, 0.18910610675811768, -0.3788299858570099, 0.4386662542819977, 0.2727023661136627, ...]</code>     |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-tr

* Dataset: [en-tr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 24.72 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                                               | label                                                                                                                        |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Eğer insanlar elle hesaba ilgililerse ya da öğrenmek için özel amaçları varsa konu ne kadar acayip olursa olsun bunu öğrenmeliler, engellemeyi bir an için bile önermiyorum.</code> | <code>[-0.04564047232270241, 0.4971524775028229, 0.28066301345825195, -0.726702094078064, -0.17846377193927765, ...]</code>  |
  | <code>İnsanların kendi ilgi alanlarını takip etmeleri, kesinlikle doğru bir şeydir.</code>                                                                                                | <code>[0.2061387449502945, 0.5284574031829834, 0.3577779233455658, 0.28818392753601074, 0.17228049039840698, ...]</code>     |
  | <code>Ben bir biçimde Antik Yunan hakkında ilgiliyimdir. ancak tüm nüfusu Antik Yunan gibi bir konu hakkında bilgi edinmeye zorlamamalıyız.</code>                                        | <code>[0.12050342559814453, 0.15652479231357574, 0.48636534810066223, -0.13693244755268097, 0.42764803767204285, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-it

* Dataset: [en-it](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 5,000 training samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 3 tokens</li><li>mean: 26.41 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                                                                                               | label                                                                                                                       |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
  | <code>Non credo che sia giustificato.</code>                                                                                                                                                                                              | <code>[-0.36175352334976196, 0.7323781251907349, 0.651816189289093, -0.8461223840713501, -0.007496151141822338, ...]</code> |
  | <code>Perciò faccio distinzione tra quello che stiamo facendo fare alle persone, le materie che si ritengono principali, e le materie che le persone potrebbero seguire per loro interesse o forse a volte anche incitate a farlo.</code> | <code>[0.3047865927219391, 0.5270194411277771, 0.26616284251213074, 0.2612147927284241, 0.1950961947441101, ...]</code>     |
  | <code>Ma che argomenti porta la gente su questi temi?</code>                                                                                                                                                                              | <code>[0.2123885154724121, -0.09616123884916306, -0.4196523427963257, -0.5469440817832947, -0.6056501865386963, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

### Evaluation Datasets

#### en-ar

* Dataset: [en-ar](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 993 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 3 tokens</li><li>mean: 28.03 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                 | label                                                                                                                        |
  |:------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>شكرا جزيلا كريس.</code>                                                                               | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>انه فعلا شرف عظيم لي ان أصعد المنصة للمرة الثانية. أنا في غاية الامتنان.</code>                       | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>لقد بهرت فعلا بهذا المؤتمر, وأريد أن أشكركم جميعا على تعليقاتكم الطيبة على ما قلته تلك الليلة.</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-fr

* Dataset: [en-fr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 992 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 30.72 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                                      | label                                                                                                                        |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Merci beaucoup, Chris.</code>                                                                                                                                              | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>C'est vraiment un honneur de pouvoir venir sur cette scène une deuxième fois. Je suis très reconnaissant.</code>                                                           | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>J'ai été très impressionné par cette conférence, et je tiens à vous remercier tous pour vos nombreux et sympathiques commentaires sur ce que j'ai dit l'autre soir.</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-de

* Dataset: [en-de](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 991 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 27.71 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                | label                                                                                                                        |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Vielen Dank, Chris.</code>                                                                                                                           | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>Es ist mir wirklich eine Ehre, zweimal auf dieser Bühne stehen zu dürfen. Tausend Dank dafür.</code>                                                 | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>Ich bin wirklich begeistert von dieser Konferenz, und ich danke Ihnen allen für die vielen netten Kommentare zu meiner Rede vorgestern Abend.</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-es

* Dataset: [en-es](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 990 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 26.47 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                                       | label                                                                                                                        |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Muchas gracias Chris.</code>                                                                                                                                | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>Y es en verdad un gran honor tener la oportunidad de venir a este escenario por segunda vez. Estoy extremadamente agradecido.</code>                        | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>He quedado conmovido por esta conferencia, y deseo agradecer a todos ustedes sus amables comentarios acerca de lo que tenía que decir la otra noche.</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-tr

* Dataset: [en-tr](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 993 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                       | label                                |
  |:--------|:----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.4 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                 | label                                                                                                                        |
  |:----------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Çok teşekkür ederim Chris.</code>                                                                                     | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>Bu sahnede ikinci kez yer alma fırsatına sahip olmak gerçekten büyük bir onur. Çok minnettarım.</code>                | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>Bu konferansta çok mutlu oldum, ve anlattıklarımla ilgili güzel yorumlarınız için sizlere çok teşekkür ederim.</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

#### en-it

* Dataset: [en-it](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [d366ddd](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/d366dddc3d1ef0421a41f9e534bad4efae6d7730)
* Size: 993 evaluation samples
* Columns: <code>non_english</code> and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 27.94 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | non_english                                                                                                                                             | label                                                                                                                        |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
  | <code>Grazie mille, Chris.</code>                                                                                                                       | <code>[-0.4331263303756714, 1.0602688789367676, -0.07791043072938919, -0.4170420169830322, 1.6768444776535034, ...]</code>   |
  | <code>E’ veramente un grande onore venire su questo palco due volte. Vi sono estremamente grato.</code>                                                 | <code>[0.27005696296691895, 0.5391750335693359, -0.2580486238002777, -0.6613674759864807, 0.6738830804824829, ...]</code>    |
  | <code>Sono impressionato da questa conferenza, e voglio ringraziare tutti voi per i tanti, lusinghieri commenti, anche perché... Ne ho bisogno!!</code> | <code>[-0.25320106744766235, 0.04791366308927536, -0.13174884021282196, -0.7357578277587891, 0.2366354614496231, ...]</code> |
* Loss: [<code>MSELoss</code>](https://sbert.net/docs/package_reference/losses.html#mseloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `learning_rate`: 2e-05
- `num_train_epochs`: 5
- `warmup_ratio`: 0.1
- `fp16`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: False
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 5
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: None
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | en-ar loss | en-it loss | en-de loss | en-fr loss | en-es loss | en-tr loss | en-ar_mean_accuracy | en-ar_negative_mse | en-de_mean_accuracy | en-de_negative_mse | en-es_mean_accuracy | en-es_negative_mse | en-fr_mean_accuracy | en-fr_negative_mse | en-it_mean_accuracy | en-it_negative_mse | en-tr_mean_accuracy | en-tr_negative_mse | sts17-en-ar-test_spearman_max | sts17-en-de-test_spearman_max | sts17-en-tr-test_spearman_max | sts17-es-en-test_spearman_max | sts17-fr-en-test_spearman_max | sts17-it-en-test_spearman_max |
|:------:|:----:|:-------------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:-------------------:|:------------------:|:-------------------:|:------------------:|:-------------------:|:------------------:|:-------------------:|:------------------:|:-------------------:|:------------------:|:-------------------:|:------------------:|:-----------------------------:|:-----------------------------:|:-----------------------------:|:-----------------------------:|:-----------------------------:|:-----------------------------:|
| 0.2110 | 100  | 0.5581        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 0.4219 | 200  | 0.3071        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 0.6329 | 300  | 0.2675        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 0.8439 | 400  | 0.2606        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 1.0549 | 500  | 0.2589        | 0.2519     | 0.2498     | 0.2511     | 0.2488     | 0.2503     | 0.2512     | 0.1254              | -25.1903           | 0.2523              | -25.1089           | 0.2591              | -25.0276           | 0.2409              | -24.8803           | 0.2180              | -24.9768           | 0.1158              | -25.1219           | 0.0308                        | 0.1281                        | 0.1610                        | 0.1465                        | 0.0552                        | 0.0518                        |
| 1.2658 | 600  | 0.2504        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 1.4768 | 700  | 0.2427        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 1.6878 | 800  | 0.2337        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 1.8987 | 900  | 0.2246        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 2.1097 | 1000 | 0.2197        | 0.2202     | 0.2157     | 0.2151     | 0.2147     | 0.2139     | 0.2218     | 0.5841              | -22.0204           | 0.8012              | -21.5087           | 0.8495              | -21.3935           | 0.7959              | -21.4660           | 0.7815              | -21.5699           | 0.6007              | -22.1778           | 0.3346                        | 0.4013                        | 0.4727                        | 0.3353                        | 0.3827                        | 0.3292                        |
| 2.3207 | 1100 | 0.2163        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 2.5316 | 1200 | 0.2123        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 2.7426 | 1300 | 0.2069        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 2.9536 | 1400 | 0.2048        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 3.1646 | 1500 | 0.2009        | 0.2086     | 0.2029     | 0.2022     | 0.2012     | 0.2002     | 0.2111     | 0.7367              | -20.8567           | 0.8739              | -20.2247           | 0.9303              | -20.0215           | 0.8755              | -20.1213           | 0.8600              | -20.2900           | 0.7165              | -21.1119           | 0.4087                        | 0.5473                        | 0.5551                        | 0.4724                        | 0.4882                        | 0.4690                        |
| 3.3755 | 1600 | 0.2019        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 3.5865 | 1700 | 0.1989        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 3.7975 | 1800 | 0.196         | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 4.0084 | 1900 | 0.1943        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 4.2194 | 2000 | 0.194         | 0.2040     | 0.1977     | 0.1973     | 0.1962     | 0.1947     | 0.2075     | 0.7714              | -20.3955           | 0.8915              | -19.7279           | 0.9449              | -19.4724           | 0.8942              | -19.6232           | 0.8807              | -19.7699           | 0.7432              | -20.7547           | 0.4425                        | 0.5618                        | 0.5819                        | 0.5021                        | 0.5334                        | 0.5250                        |
| 4.4304 | 2100 | 0.1951        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 4.6414 | 2200 | 0.1928        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |
| 4.8523 | 2300 | 0.1909        | -          | -          | -          | -          | -          | -          | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                   | -                  | -                             | -                             | -                             | -                             | -                             | -                             |


### Environmental Impact
Carbon emissions were measured using [CodeCarbon](https://github.com/mlco2/codecarbon).
- **Energy Consumed**: 0.060 kWh
- **Carbon Emitted**: 0.023 kg of CO2
- **Hours Used**: 0.179 hours

### Training Hardware
- **On Cloud**: No
- **GPU Model**: 1 x NVIDIA GeForce RTX 3090
- **CPU Model**: 13th Gen Intel(R) Core(TM) i7-13700K
- **RAM Size**: 31.78 GB

### Framework Versions
- Python: 3.11.6
- Sentence Transformers: 3.0.0.dev0
- Transformers: 4.41.0.dev0
- PyTorch: 2.3.0+cu121
- Accelerate: 0.26.1
- Datasets: 2.18.0
- Tokenizers: 0.19.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MSELoss
```bibtex
@inproceedings{reimers-2020-multilingual-sentence-bert,
    title = "Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2004.09813",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->