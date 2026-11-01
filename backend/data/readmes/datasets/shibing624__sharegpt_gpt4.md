---
annotations_creators:
- shibing624
language_creators:
- shibing624
language:
- zh
- en
- gl
- ko
license: cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset/tree/main
task_categories:
- text-classification
- text-generation
task_ids:
- text-scoring
paperswithcode_id: LLM
pretty_name: GPT4 sharegpt
---
# Dataset Card 

## Dataset Description
- **Repository:** [shibing624/MedicalGPT](https://github.com/shibing624/MedicalGPT)
- **Dataset:** [shibing624/sharegpt_gpt4](https://huggingface.co/datasets/shibing624/sharegpt_gpt4)
- **Size of downloaded dataset files:** 772 M
- **Total amount of disk used:** 772 M
### Dataset Summary

ShareGPT中挑选出的GPT4多轮问答数据，多语言问答。


### Languages

数据集是多语言，包括中文、英文、日文等常用语言。

## Dataset Structure

### Data Fields
The data fields are the same among all splits.

- `conversations`: a List of `string` .

```shell
head -n 1 sharegpt_gpt4.jsonl

{"conversations":[
  {'from': 'human',
   'value': '採用優雅現代中文，用中文繁體字型，回答以下問題。為所有標題或專用字詞提供對應的英語翻譯：Using scholarly style, summarize in detail James Barr\'s book "Semantics of Biblical Language". Provide examples supplied in the book and give corresponding page numbers wherever applicable.'},
  {'from': 'gpt',
   'value': '《聖經語言的語義學》（Semantics of Biblical Language）是詹姆斯·巴爾（James Barr）於1961年出版的一本研究聖經語言的專著。在這部作品中，巴爾對聖經希伯來語和希臘語的語言學特徵進行了深入的探討，他批判了當時盛行的聖經研究方法，主張應該將語言學原理應用於聖經文本的詮釋，以便更準確地理解聖經的意思。\n\n巴爾在《聖經語言的語義學》中提出了幾個重要的觀點。首先，他主張語言學和語言學家在聖經研究中的角色應該受到重視。他認為，應該避免將聖經語言學和其他古典語言學區分開來，因為聖經語言和其他古代語言一樣，都有其固有的語法、語義和詞彙特點（第18-23頁）。\n\n其次，巴爾批評了當時流行的"字根意義論"（root-meaning fallacy），即過分強調單詞的字根在詮釋聖經含義時的作用。他指出，詞義是由語境決定的，而非僅僅由字根決定。巴爾舉了希伯來語單詞 "כפר"（kāpar）為例，它在不同的語境下可以表示"遮蓋"、"贖回"或"和解"，而不是僅僅依賴其字根意義（第183-184頁）。\n\n第三，巴爾強調了詞彙意義在詮釋聖經時的重要性。他認為，了解單詞的意義和用法對於恰當理解聖經文本至關重要。巴爾引用了希伯來語單詞 "ברית"（berîṯ，英文：covenant）和希臘語單詞 "διαθήκη"（diathēkē，英文：testament）為例，解釋了這兩個詞在聖經中的不'},
  {'from': 'human', 'value': '繼續'},
  {'from': 'gpt',
   'value': '同含義和用法。巴爾認為，了解這些詞語在不同語境下的意義對於理解聖經中的盟約和遺囑概念至關重要（第50-53頁）。\n\n第四，巴爾強調語境在詮釋聖經時的重要性。他認為，要理解聖經的含義，就必須考慮到文本的歷史背景、文化環境和語言風格。此外，巴爾提倡從語言學的角度研究聖經，以便更好地理解聖經的結構和風格。他以希伯來詩篇的平行主義（Parallelism）為例，闡述了語言學原理如何有助於揭示詩篇中的意象和修辭結構（第250-252頁）。\n\n總之，《聖經語言的語義學》一書對聖經研究領域產生了深遠的影響。詹姆斯·巴爾通過對聖經語言學的深入研究，提出了許多富有洞察力的觀點，尤其是關於語言學在聖經詮釋中的重要性。這些觀點對後來的聖經研究者產生了很大的啟示，使他們在研究聖經時更加重視語言學原理，從而更加準確地理解聖經的含義。'}
  ]
}
```

### Data Splits

```shell
> wc -l *
     6206 sharegpt_gpt4.jsonl  # 清洗后的高质量gpt4日常问答数据集，大小：6K，主要是知识问答、编程题、推理计算，包括简体中文、繁体中文、英文、日文、韩文等多国语言多轮对话数据集。
    58674 sharegpt_V3_format.jsonl # 原V3版sharegpt规范格式后的数据集，大小：58K，主要是日常问答，提问偏口语化，多国语言，多轮对话。    
    38535 sharegpt_zh_38K_format.jsonl # 中文gpt4日常问答数据集，大小：38K，主要是知识问答、翻译任务、求助、编程推理任务等偏口语提问，中文，多轮对话。
   103415 total
```

#### Who are the annotators?
原作者。


### Licensing Information

same to sharegpt.



### Contributions

[shibing624](https://github.com/shibing624) add this dataset.