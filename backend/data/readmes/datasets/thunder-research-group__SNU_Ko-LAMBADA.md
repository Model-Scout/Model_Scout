---
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: text
    dtype: string
  - name: answer
    dtype: string
  - name: candidate
    dtype: string
  splits:
  - name: test
    num_bytes: 1341346
    num_examples: 2255
  download_size: 831853
  dataset_size: 1341346
configs:
- config_name: default
  data_files:
  - split: test
    path: data/validation-*
license: cc-by-nc-sa-4.0
language:
- ko
pretty_name: Ko-LAMBADA
---

> Note: Evaluation code and task configurations for this benchmark are available in the [`evaluation_code`](https://github.com/mcrl/korean_benchmarks/tree/main/evaluation_code) directory of the [Korean Benchmark Suite GitHub repository](https://github.com/mcrl/korean_benchmarks). The evaluation setup is built on the Language Model Evaluation Harness and supports standardized model assessment.

# Dataset Card for Ko-LAMBADA

## Dataset Summary

Ko-LAMBADA evaluates the ability of language models to understand long-range context in Korean texts by requiring them to predict a masked word within a passage. 
Unlike the original LAMBADA, which focused on predicting the final word of an English narrative, Ko-LAMBADA selects a contextually important **noun** from mid-sentence and asks the model to predict it using the surrounding passage.
This design reflects a key linguistic difference: while English sentences often end in a noun that is semantically tied to the discourse context, Korean sentences typically end in verbs that are less indicative of preceding content, making verb prediction a weaker signal for discourse-level understanding.

The dataset is constructed from Korean literary works that are in the public domain. 
It is designed to test whether a language model can resolve references and understand discourse at a document level, especially within the Korean language's unique linguistic and syntactic structure.

## Supported Tasks and Benchmarks

**Task**: Long-range cloze-style word prediction (masked noun prediction)

Ko-LAMBADA is a benchmark for evaluating:
- Discourse-level understanding
- Coreference resolution
- Context-sensitive language modeling

Unlike the original LAMBADA’s end-of-sentence prediction, this task targets words that are more semantically central (e.g., nouns) and contextually recoverable.

## Languages

ko (Korean)

---

## Dataset Structure
### Data Instances
```json
{
  "index": "1",
  "text": "“여보! 이번에는 당신이 꼭 병원으로 가시우.” 하고 여러 날 신음으로 쑥 들어간 내 눈을 보면서 웃었다. 싸전과 반찬 가게에서도 인제는 외상을 주지 않아서 이틀이나 좁쌀죽을 먹었고 그것도 없어서 아침을 굶었던 판이라 병원보다 급한 것은 쌀과 나무이다. 그러나 싸전과 반찬 가게에 빚을 갚고 쌀과 나무를 좀 사더라도 담배값이 오히려 부족한데 어떻게 _에 갈 수 있으랴?",
  "answer": "병원",
  "candidate": "가게"
}

```

### Data Fields
- `index`: The index of the data.
- `text`: The full passage with a blank (`_`) where the target word was removed.
- `answer`: The word that correctly fills the blank.
- `candidate`: A distractor word that also appears in context.

### Data Splits
- Single evaluation set (`test` set)

---

## Dataset Creation

The dataset construction proceeded in five stages:

1. **Data Collection**:  
   Literary works in the public domain were collected primarily from [공유마당](https://gongu.copyright.or.kr/gongu/main/main.do), a Korean government platform offering shared and expired copyright materials. All texts used are confirmed to be free of copyright restrictions.

2. **Preprocessing**:  
   Candidate passages were selected where target words (typically nouns) occurred more than once in a coherent narrative span. The final instance of the target word was masked.

3. **Initial Data Generation**:  
   For each passage, the masked word was stored as the `answer`, and another instance was marked as the `candidate`. Passages where the masking produced syntactically or semantically unnatural results were flagged for review.

4. **Manual Correction**:  
   Authors reviewed and corrected unnatural or ambiguous cases. Cases where multiple possible answers existed or where the `answer` could not be reasonably inferred from the context were either revised or removed. 

5. **Validation**:
   All dataset instances were cross-checked by independent reviewers who were not involved in the initial steps, to identify and correct errors.

The full list of source texts (including author and title) used for building this dataset is available at:  
[literature_metadata.csv](https://huggingface.co/datasets/thunder-research-group/snu_lambada/blob/main/literature_metadata.csv)

> Introduction of [공유마당](https://gongu.copyright.or.kr/gongu/main/main.do):  
> 공유마당 is a public content-sharing platform operated by the Korean government that provides copyright-cleared materials for free use.
> It offers a wide range of works, including expired copyrights, public domain texts, high-value private collections, and government-funded content.
> The platform aims to preserve and distribute cultural assets as part of an open digital heritage ecosystem.


## Additional Information

### Licensing Information

This dataset is licensed under the Creative Commons Attribution Non Commercial Share Alike 4.0 (cc-by-nc-sa-4.0).

### Citation Information

```
@inproceedings{
so2026constructing,
title={Constructing Korean Benchmark Suite for Reliable Evaluation of Foundation Models},
author={Yeonkyoung So and Jongmin Kim and Sungmok Jung and Gyuseong Lee and Sangho Kim and Jongyeon Park and Joonhak Lee and Seho Pyo and Gyeongje Cho and Seorin Kim and Jisoo Kim and Suyoung Park and Hyunji M. Park and Yelim Ahn and Yeongho Seo and Jaejin Lee},
booktitle={ICML 2026 Workshop on Combining Theory and Benchmarks: Towards A Virtuous Cycle to Understand and Guarantee Foundation Model Performance},
year={2026},
url={https://openreview.net/forum?id=oJ3rhISSqO}
}
```

### Contact Information
If you find something wrong or have question about the dataset, contact snullm@aces.snu.ac.kr.