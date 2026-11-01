---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: original_index
    dtype: int64
  - name: problem
    dtype: string
  - name: answer
    dtype: string
  - name: topic
    dtype: string
  - name: answer_type
    dtype: string
  - name: multi_step
    dtype: bool
  - name: requires_reasoning
    dtype: bool
  - name: urls
    dtype: string
  - name: method
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: test
    num_bytes: 27899884
    num_examples: 64000
  download_size: 6385075
  dataset_size: 27899884
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
license: cc-by-4.0
language:
- en
- it
- fr
- es
- zh
- id
- ja
- ko
- hi
- mr
- ur
- bn
pretty_name: CodeMixQA
---

# CodeMixQA

A benchmark with high-quality human annotations, comprising 16 diverse parallel code-switched language-pair variants that span multiple geographic regions and code-switching patterns, and include both original scripts and their transliterated forms.

We use SimpleQA Verified as our source dataset. We select the SimpleQA Verified, as it is a challenging evaluation set that has not been saturated yet by current models and has desirable properties such as verifiable answers (through source reconciliation), de-duplicated data points, topic balancing, and that it is markedly different from most standard tasks that are prevalent in code switching studies such as language identification, NER, and machine translation.

In this dataset, we employ multiple data generation strategies, including random switching, selective switching, and grammar-constrained approaches.
This dataset enables systematic evaluation of LLM performance across different code-switching patterns and text generation strategies.

## Reference
Can Large Language Models Understand, Reason About, and Generate Code-Switched Text?

If you use any datasets from this toolkit in your research, please cite the associated paper.

```
@article{winata2026can,
  title={Can Large Language Models Understand, Reason About, and Generate Code-Switched Text?},
  author={Winata, Genta Indra and Anugraha, David and Irawan, Patrick Amadeus and Das, Anirban and Yoo, Haneul and Dashore, Paresh and Kulkarni, Shreyas and Zhang, Ruochen and Sakajo, Haruki and Hudi, Frederikus and others},
  journal={arXiv preprint arXiv:2601.07153},
  year={2026}
}
```