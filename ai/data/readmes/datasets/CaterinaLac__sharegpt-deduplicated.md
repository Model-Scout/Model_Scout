---
license: apache-2.0
task_categories:
- conversational
language:
- en
- zh
- ko
- fr
- ja
- es
- 'no'
- et
- de
- ca
- vi
- fi
size_categories:
- 1K<n<10K
---
# Dataset Card for Dataset Name

## Dataset Description

### Dataset Summary
This dataset is a deduplicated version of [sharegpt4](https://huggingface.co/datasets/shibing624/sharegpt_gpt4). 
<br>The deduplication process has two steps:<br>
1. The literal duplicates (both input and outputs) are removed
2. The remaining (5749) instances are embedded with the [SentenceTransformer library](https://www.sbert.net/) ("paraphrase-multilingual-mpnet-base-v2" model).
Then, we compute the cosine similarity among all the possible pairs, and consider paraphrases those pairs with a similarity > 0.95. For each paraphrase group, we only retain one element.
The resulting dataset has 5139 elements.

### Languages

The dataset includes several languages, but the vast majority of it is in English. Roughly 600 instances are in more than one language, as detected by [langdetect](https://pypi.org/project/langdetect/). 
The languages that appear across the dataset, together with the number of instances they appear in, follow: 
<details>
  <summary>Language Distribution</summary>
  en 4053<br>
zh-cn 423<br>
ko 333<br>
fr 168<br>
ja 151<br>
es 142<br>
no 110<br>
et 97<br>
de 81<br>
ca 78<br>
vi 63<br>
fi 52<br>
zh-tw 47<br>
pt 42<br>
tl 39<br>
ru 24<br>
he 24<br>
id 23<br>
it 22<br>
sv 21<br>
pl 16<br>
nl 16<br>
th 15<br>
ro 11<br>
da 9<br>
tr 8<br>
cs 8<br>
hr 6<br>
uk 5<br>
af 5<br>
ar 4<br>
bg 3<br>
cy 2<br>
sk 2<br>
hu 2<br>
so 2<br>
bn 1<br>
sl 1<br>
hi 1<br>
sw 1<br>
lv 1<br>
el 1<br>

</details>

### Data Fields
Each instance has two fields: 
- 'input': one turn of a human-bot conversation, initiated by a human. It starts with 'Human: ', and it ends with 'Assistant: '
- 'output': the bot reply