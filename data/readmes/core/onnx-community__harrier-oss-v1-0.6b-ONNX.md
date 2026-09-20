---
tags:
- mteb
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
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
- he
- hi
- hr
- hu
- hy
- id
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
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
license: mit
library_name: transformers.js
base_model:
- microsoft/harrier-oss-v1-0.6b
---

## harrier-oss-v1

harrier-oss-v1 is a family of multilingual text embedding models developed by Microsoft.
The models use decoder-only architectures with last-token pooling and L2 normalization to produce dense text embeddings.
They can be applied to a wide range of tasks, including but not limited to **retrieval**, **clustering**, **semantic similarity**, **classification**, **bitext mining**, and **reranking**.
The models achieve state-of-the-art results on the [Multilingual MTEB v2](https://huggingface.co/spaces/mteb/leaderboard) benchmark as of the release date.

| Model                                                                       | Parameters | Embedding Dimension | Max Tokens | MTEB v2 Score |
|-----------------------------------------------------------------------------|------------|---------------------|------------|---------------|
| [harrier-oss-v1-270m](https://huggingface.co/microsoft/harrier-oss-v1-270m) | 270M       | 640                 | 32,768     | 66.5          |
| [harrier-oss-v1-0.6b](https://huggingface.co/microsoft/harrier-oss-v1-0.6b) | 0.6B       | 1,024               | 32,768     | 69.0          |
| [harrier-oss-v1-27b](https://huggingface.co/microsoft/harrier-oss-v1-27b)   | 27B        | 5,376               | 32,768     | **74.3**      |

## Training

All models are trained with contrastive learning objectives on a large-scale mixture of multilingual datasets covering diverse tasks.
The 270m and 0.6b variants are additionally trained with knowledge distillation from larger embedding models.

## Usage

Below is an example to encode queries and passages from the MS-MARCO passage ranking dataset.

### Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```sh
npm i @huggingface/transformers
```

You can then use the model as follows:
```js
import { AutoModel, AutoTokenizer, matmul } from "@huggingface/transformers";

const model_id = "onnx-community/harrier-oss-v1-0.6b-ONNX";
const tokenizer = await AutoTokenizer.from_pretrained(model_id);
const model = await AutoModel.from_pretrained(model_id, { dtype: "q4", device: "webgpu" });

const prompts = {
  web_search_query: "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: ",
  sts_query: "Instruct: Retrieve semantically similar text\nQuery: ",
  bitext_query: "Instruct: Retrieve parallel sentences\nQuery: ",
};
const queries = ["how much protein should a female eat", "summit define"].map((x) => prompts.web_search_query + x);
const documents = [
  "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.",
  "Definition of summit for English Language Learners. : 1  the highest point of a mountain : the top of a mountain. : 2  the highest level. : 3  a meeting or series of meetings between the leaders of two or more governments.",
];

const query_inputs = tokenizer(queries, { padding: true, truncation: true });
const { sentence_embedding: query_embeddings } = await model(query_inputs);

const doc_inputs = tokenizer(documents, { padding: true, truncation: true });
const { sentence_embedding: doc_embeddings } = await model(doc_inputs);

const scores = (await matmul(query_embeddings, doc_embeddings.transpose(1, 0))).mul(100);
console.log(scores.tolist());
// [
//   [ 66.6568832397461, 28.08503532409668 ],
//   [ 29.10841178894043, 70.66002655029297 ]
// ]
```

## Supported Languages

The models are trained on multilingual data and support a wide range of languages,
including but not limited to: Arabic, Bulgarian, Catalan, Czech, Danish, German, Greek, English, Spanish,
Estonian, Persian, Finnish, French, Hebrew, Hindi, Croatian, Hungarian, Indonesian, Italian, Japanese,
Korean, Lithuanian, Latvian, Macedonian, Malay, Dutch, Norwegian, Polish, Portuguese, Romanian, Russian,
Slovak, Slovenian, Albanian, Serbian, Swedish, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Chinese.

## Evaluation

Please follow the [mteb](https://github.com/embeddings-benchmark/mteb) repository on how to reproduce our scores.
The evaluation prompts used for each task are also available at [mteb_v2_eval_prompts.json](mteb_v2_eval_prompts.json).

## FAQ

**1. Do I need to add instructions to the query?**

Yes, this is how the model is trained, otherwise you will see a performance degradation.
The task definition should be a one-sentence instruction that describes the task.
This is a way to customize text embeddings for different scenarios through natural language instructions.

On the other hand, there is no need to add instructions to the document side.

**2. Why are my reproduced results slightly different from reported in the model card?**

Different versions of `transformers` and `pytorch` could cause negligible but non-zero performance differences.

**3. What pooling strategy does this model use?**

The model uses **last-token pooling** — the embedding of the last non-padding token is used as the sentence representation.
The embedding is then L2-normalized. This is handled automatically when using Sentence Transformers.