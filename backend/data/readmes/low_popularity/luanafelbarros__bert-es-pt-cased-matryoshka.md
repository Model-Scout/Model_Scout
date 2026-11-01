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
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:3560698
- loss:ModifiedMatryoshkaLoss
- loss:MSELoss
base_model: google-bert/bert-base-multilingual-cased
widget:
- source_sentence: We cope with this pressure by having brains, and within our brains,
    decision-making centers that I've called here the "Actor."
  sentences:
  - Nós lidamos com esta pressão porque temos cérebro, e dentro do nosso cérebro,
    centros de tomada de decisão a que eu chamei aqui o "Ator".
  - Isto significa que o Crítico deve ter falado naquele animal, e que o Crítico deve
    estar contido entre os neurónios produtores de dopamina na esquerda, mas não nos
    neurónios produtores de dopamina na direita.
  - Na ressonância magnética e na espetroscopia de MR — a atividade do tumor está
    a vermelho —
- source_sentence: Once it's a closed system, you will have legal liability if you
    do not urge your CEO to get the maximum income from reducing and trading the carbon
    emissions that can be avoided.
  sentences:
  - (Risas) Espero que las conversaciones aquí en TED me ayuden a terminarla.
  - Una vez que es un sistema cerrado, tendrán responsabilidad legal si no exhortan
    a su ejecutivo en jefe a obtener el máximo ingreso de la reducción y comercialización
    de emisiones de carbono que pueden ser evitadas.
  - Pero también son muy efectivas en desviar nuestro camino.
- source_sentence: Whenever it comes up to the midpoint, it pauses, it carefully scans
    the odor interface as if it was sniffing out its environment, and then it turns
    around.
  sentences:
  - Tiene que decidir si dar la vuelta y quedarse en el mismo olor, o si cruzar la
    línea del medio y probar algo nuevo.
  - Ésta es una oportunidad.
  - Cada vez que llega al medio, se detiene analiza con cuidado la interfaz de olor,
    como si estuviera olfateando su entorno, y luego da la vuelta.
- source_sentence: You've seen the documentaries of sweatshops making garments all
    over the world, even in developed countries.
  sentences:
  - No llegaron muy lejos, obviamente.
  - Uds ya han visto documentales de los talleres de confección de prendas en todo
    el mundo, incluso en los países desarrollados.
  - Y los maestros también están frustrados.
- source_sentence: It's hands-on, it's in-your-face, it requires an active engagement,
    and it allows kids to apply all the core subject learning in real ways.
  sentences:
  - É prático, é presencial, isso requer uma participação ativa, e permite que as
    crianças apliquem todos os tópicos importantes de aprendizagem de forma real.
  - E no mundo do áudio que é quando o microfone fica muito perto da origem do som,
    e então ele entra nessa repetição auto-destrutiva que cria um som muito desagradável.
  - Vamos encarar a realidade, o contrato de uma grande marca multinacional para um
    fornecedor na Índia ou China tem um poder persuasivo muito maior do que as leis
    locais de trabalho, do que as regras ambientais locais, do que os padrões locais
    de Direitos Humanos.
datasets:
- sentence-transformers/parallel-sentences-talks
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- negative_mse
model-index:
- name: SentenceTransformer based on google-bert/bert-base-multilingual-cased
  results:
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: MSE val en es
      type: MSE-val-en-es
    metrics:
    - type: negative_mse
      value: -31.554964184761047
      name: Negative Mse
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: MSE val en pt
      type: MSE-val-en-pt
    metrics:
    - type: negative_mse
      value: -31.72471523284912
      name: Negative Mse
  - task:
      type: knowledge-distillation
      name: Knowledge Distillation
    dataset:
      name: MSE val en pt br
      type: MSE-val-en-pt-br
    metrics:
    - type: negative_mse
      value: -30.244168639183044
      name: Negative Mse
---

# SentenceTransformer based on google-bert/bert-base-multilingual-cased

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) on the en-es, en-pt and [en-pt-br](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) datasets. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) <!-- at revision 3f076fdb1ab68d5b2880cb87a0886f315b8146f8 -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Datasets:**
    - en-es
    - en-pt
    - [en-pt-br](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
- **Languages:** en, multilingual, ar, bg, ca, cs, da, de, el, es, et, fa, fi, fr, gl, gu, he, hi, hr, hu, hy, id, it, ja, ka, ko, ku, lt, lv, mk, mn, mr, ms, my, nb, nl, pl, pt, ro, ru, sk, sl, sq, sr, sv, th, tr, uk, ur, vi, zh
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: BertModel 
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
model = SentenceTransformer("luanafelbarros/bert-es-pt-cased-matryoshka")
# Run inference
sentences = [
    "It's hands-on, it's in-your-face, it requires an active engagement, and it allows kids to apply all the core subject learning in real ways.",
    'É prático, é presencial, isso requer uma participação ativa, e permite que as crianças apliquem todos os tópicos importantes de aprendizagem de forma real.',
    'Vamos encarar a realidade, o contrato de uma grande marca multinacional para um fornecedor na Índia ou China tem um poder persuasivo muito maior do que as leis locais de trabalho, do que as regras ambientais locais, do que os padrões locais de Direitos Humanos.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
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

* Datasets: `MSE-val-en-es`, `MSE-val-en-pt` and `MSE-val-en-pt-br`
* Evaluated with [<code>MSEEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator)

| Metric           | MSE-val-en-es | MSE-val-en-pt | MSE-val-en-pt-br |
|:-----------------|:--------------|:--------------|:-----------------|
| **negative_mse** | **-31.555**   | **-31.7247**  | **-30.2442**     |

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

#### en-es

* Dataset: en-es
* Size: 1,612,538 training samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.46 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 26.67 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                | non_english                                                                                                                              | label                                                                                                                                 |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
  | <code>And then there are certain conceptual things that can also benefit from hand calculating, but I think they're relatively small in number.</code> | <code>Y luego hay ciertas aspectos conceptuales que pueden beneficiarse del cálculo a mano pero creo que son relativamente pocos.</code> | <code>[-0.015244179405272007, 0.04601434990763664, -0.052873335778713226, 0.03535117208957672, -0.039562877267599106, ...]</code>     |
  | <code>One thing I often ask about is ancient Greek and how this relates.</code>                                                                        | <code>Algo que pregunto a menudo es sobre el griego antiguo y cómo se relaciona.</code>                                                  | <code>[0.0012022971641272306, -0.009590390138328075, -0.032977133989334106, 0.017047710716724396, -0.0028919472824782133, ...]</code> |
  | <code>See, the thing we're doing right now is we're forcing people to learn mathematics.</code>                                                        | <code>Vean, lo que estamos haciendo ahora es forzar a la gente a aprender matemáticas.</code>                                            | <code>[-0.019420800730586052, 0.10435999929904938, 0.009455346502363682, -0.02814250998198986, -0.017036104574799538, ...]</code>     |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

#### en-pt

* Dataset: en-pt
* Size: 1,542,353 training samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 5 tokens</li><li>mean: 24.95 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 27.08 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                                                                                                                          | non_english                                                                                                                                                                                                                                                                               | label                                                                                                                             |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
  | <code>And the country that does this first will, in my view, leapfrog others in achieving a new economy even, an improved economy, an improved outlook.</code>                                                                                                   | <code>E o país que fizer isto primeiro vai, na minha opinião, ultrapassar outros em alcançar uma nova economia até uma economia melhorada, uma visão melhorada.</code>                                                                                                                    | <code>[-0.016568265855312347, 0.10754051059484482, -0.025950804352760315, -0.045048732310533524, 0.01812679134309292, ...]</code> |
  | <code>In fact, I even talk about us moving from what we often call now the "knowledge economy" to what we might call a "computational knowledge economy," where high-level math is integral to what everyone does in the way that knowledge currently is.</code> | <code>De facto, eu até falo de mudarmos do que chamamos hoje a economia do conhecimento para o que poderemos chamar a economia do conhecimento computacional, onde a matemática de alto nível está integrada no que toda a gente faz da forma que o conhecimento actualmente está.</code> | <code>[-0.014394757337868214, 0.11997982114553452, -0.041491635143756866, -0.024539340287446976, 0.01425645500421524, ...]</code> |
  | <code>We can engage so many more students with this, and they can have a better time doing it.</code>                                                                                                                                                            | <code>Podemos cativar tantos mais estudantes com isto, e eles podem divertir-se mais a fazê-lo.</code>                                                                                                                                                                                    | <code>[-0.034232210367918015, 0.04277702793478966, -0.05683526396751404, -0.006559622474014759, -0.00639274762943387, ...]</code> |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

#### en-pt-br

* Dataset: [en-pt-br](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [0c70bc6](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/0c70bc6714efb1df12f8a16b9056e4653563d128)
* Size: 405,807 training samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.39 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 27.52 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                | non_english                                                                                                                                                | label                                                                                                                                 |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
  | <code>And then there are certain conceptual things that can also benefit from hand calculating, but I think they're relatively small in number.</code> | <code>E também existem alguns aspectos conceituais que também podem se beneficiar do cálculo manual, mas eu acho que eles são relativamente poucos.</code> | <code>[-0.015244179405272007, 0.04601434990763664, -0.052873335778713226, 0.03535117208957672, -0.039562877267599106, ...]</code>     |
  | <code>One thing I often ask about is ancient Greek and how this relates.</code>                                                                        | <code>Uma coisa sobre a qual eu pergunto com frequencia é grego antigo e como ele se relaciona a isto.</code>                                              | <code>[0.0012022971641272306, -0.009590390138328075, -0.032977133989334106, 0.017047710716724396, -0.0028919472824782133, ...]</code> |
  | <code>See, the thing we're doing right now is we're forcing people to learn mathematics.</code>                                                        | <code>Vejam, o que estamos fazendo agora, é que estamos forçando as pessoas a aprender matemática.</code>                                                  | <code>[-0.019420800730586052, 0.10435999929904938, 0.009455346502363682, -0.02814250998198986, -0.017036104574799538, ...]</code>     |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Evaluation Datasets

#### en-es

* Dataset: en-es
* Size: 2,990 evaluation samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.68 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 27.31 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                    | non_english                                                                                                                                                       | label                                                                                                                              |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
  | <code>Thank you so much, Chris.</code>                                                                                                                     | <code>Muchas gracias Chris.</code>                                                                                                                                | <code>[-0.061677999794483185, -0.04450423642992973, -0.0325058177113533, -0.06641444563865662, 0.003981702029705048, ...]</code>   |
  | <code>And it's truly a great honor to have the opportunity to come to this stage twice; I'm extremely grateful.</code>                                     | <code>Y es en verdad un gran honor tener la oportunidad de venir a este escenario por segunda vez. Estoy extremadamente agradecido.</code>                        | <code>[0.011398610658943653, -0.02500406838953495, -0.009884772822260857, 0.009336909279227257, 0.0030828709714114666, ...]</code> |
  | <code>I have been blown away by this conference, and I want to thank all of you for the many nice comments about what I had to say the other night.</code> | <code>He quedado conmovido por esta conferencia, y deseo agradecer a todos ustedes sus amables comentarios acerca de lo que tenía que decir la otra noche.</code> | <code>[-0.03842132166028023, 0.03635749593377113, -0.02491452544927597, -0.0032229204662144184, 0.0003549510147422552, ...]</code> |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

#### en-pt

* Dataset: en-pt
* Size: 2,992 evaluation samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | english                                                                            | non_english                                                                        | label                                |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                             | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.05 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 27.58 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                    | non_english                                                                                                                                                          | label                                                                                                                              |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
  | <code>Thank you so much, Chris.</code>                                                                                                                     | <code>Muito obrigado, Chris.</code>                                                                                                                                  | <code>[-0.06167794018983841, -0.04450422152876854, -0.032505810260772705, -0.06641443818807602, 0.0039817155338823795, ...]</code> |
  | <code>And it's truly a great honor to have the opportunity to come to this stage twice; I'm extremely grateful.</code>                                     | <code>É realmente uma grande honra ter a oportunidade de pisar este palco pela segunda vez. Estou muito agradecido.</code>                                           | <code>[0.011398610658943653, -0.02500406838953495, -0.009884772822260857, 0.009336909279227257, 0.0030828709714114666, ...]</code> |
  | <code>I have been blown away by this conference, and I want to thank all of you for the many nice comments about what I had to say the other night.</code> | <code>Fiquei muito impressionado com esta conferência e quero agradecer a todos os imensos comentários simpáticos sobre o que eu tinha a dizer naquela noite.</code> | <code>[-0.03842132166028023, 0.03635749593377113, -0.02491452544927597, -0.0032229204662144184, 0.0003549510147422552, ...]</code> |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

#### en-pt-br

* Dataset: [en-pt-br](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks) at [0c70bc6](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks/tree/0c70bc6714efb1df12f8a16b9056e4653563d128)
* Size: 992 evaluation samples
* Columns: <code>english</code>, <code>non_english</code>, and <code>label</code>
* Approximate statistics based on the first 992 samples:
  |         | english                                                                           | non_english                                                                        | label                                |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-------------------------------------|
  | type    | string                                                                            | string                                                                             | list                                 |
  | details | <ul><li>min: 4 tokens</li><li>mean: 25.8 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 28.92 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>size: 768 elements</li></ul> |
* Samples:
  | english                                                                                                                                                    | non_english                                                                                                                                                       | label                                                                                                                              |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
  | <code>Thank you so much, Chris.</code>                                                                                                                     | <code>Muito obrigado, Chris.</code>                                                                                                                               | <code>[-0.0616779662668705, -0.044504180550575256, -0.032505787909030914, -0.06641441583633423, 0.003981734160333872, ...]</code>  |
  | <code>And it's truly a great honor to have the opportunity to come to this stage twice; I'm extremely grateful.</code>                                     | <code>É realmente uma grande honra ter a oportunidade de estar neste palco pela segunda vez. Estou muito agradecido.</code>                                       | <code>[0.011398598551750183, -0.02500401996076107, -0.009884790517389774, 0.009336900897324085, 0.003082842566072941, ...]</code>  |
  | <code>I have been blown away by this conference, and I want to thank all of you for the many nice comments about what I had to say the other night.</code> | <code>Eu fui muito aplaudido por esta conferência e quero agradecer a todos pelos muitos comentários delicados sobre o que eu tinha a dizer naquela noite.</code> | <code>[-0.03842132166028023, 0.03635749593377113, -0.02491452544927597, -0.0032229204662144184, 0.0003549510147422552, ...]</code> |
* Loss: <code>__main__.ModifiedMatryoshkaLoss</code> with these parameters:
  ```json
  {
      "loss": "MSELoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
- `learning_rate`: 2e-05
- `num_train_epochs`: 1
- `warmup_ratio`: 0.1
- `fp16`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
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
- `restore_callback_states_from_checkpoint`: False
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
- `ddp_broadcast_buffers`: False
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
- `include_for_metrics`: []
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
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step  | Training Loss | en-es loss | en-pt loss | en-pt-br loss | MSE-val-en-es_negative_mse | MSE-val-en-pt_negative_mse | MSE-val-en-pt-br_negative_mse |
|:------:|:-----:|:-------------:|:----------:|:----------:|:-------------:|:--------------------------:|:--------------------------:|:-----------------------------:|
| 0.0719 | 1000  | 0.028         | 0.0237     | 0.0237     | 0.0231        | -24.8296                   | -24.6706                   | -25.9588                      |
| 0.1438 | 2000  | 0.0227        | 0.0213     | 0.0215     | 0.0208        | -26.2546                   | -26.2964                   | -25.9444                      |
| 0.2157 | 3000  | 0.0213        | 0.0203     | 0.0205     | 0.0199        | -27.7589                   | -27.8414                   | -27.1460                      |
| 0.2876 | 4000  | 0.0206        | 0.0197     | 0.0199     | 0.0193        | -29.1241                   | -29.2139                   | -28.3021                      |
| 0.3595 | 5000  | 0.0201        | 0.0194     | 0.0195     | 0.0190        | -30.1292                   | -30.2692                   | -29.0747                      |
| 0.4313 | 6000  | 0.0198        | 0.0190     | 0.0192     | 0.0187        | -30.3807                   | -30.4967                   | -29.3404                      |
| 0.5032 | 7000  | 0.0195        | 0.0188     | 0.0190     | 0.0185        | -31.0799                   | -31.2305                   | -29.9549                      |
| 0.5751 | 8000  | 0.0193        | 0.0186     | 0.0188     | 0.0183        | -31.1297                   | -31.2883                   | -30.0050                      |
| 0.6470 | 9000  | 0.0192        | 0.0185     | 0.0186     | 0.0182        | -31.2788                   | -31.4498                   | -30.0589                      |
| 0.7189 | 10000 | 0.019         | 0.0184     | 0.0185     | 0.0181        | -31.3215                   | -31.4903                   | -30.0056                      |
| 0.7908 | 11000 | 0.019         | 0.0183     | 0.0184     | 0.0180        | -31.4416                   | -31.6329                   | -30.1343                      |
| 0.8627 | 12000 | 0.0189        | 0.0182     | 0.0184     | 0.0180        | -31.5266                   | -31.6991                   | -30.1956                      |
| 0.9346 | 13000 | 0.0188        | 0.0182     | 0.0183     | 0.0179        | -31.5550                   | -31.7247                   | -30.2442                      |


### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.3.1
- Transformers: 4.46.3
- PyTorch: 2.5.1+cu121
- Accelerate: 1.1.1
- Datasets: 3.1.0
- Tokenizers: 0.20.3

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