---
license: lgpl-3.0
task_categories:
- question-answering
language:
- ko
size_categories:
- n<1K
dataset_info:
  features:
  - name: question_id
    dtype: int64
  - name: category
    dtype: string
  - name: turns
    sequence: string
  - name: reference
    sequence: string
  splits:
  - name: train
    num_bytes: 52214
    num_examples: 80
  download_size: 33690
  dataset_size: 52214
tags:
- evaluation
- instruction-following
- language model
- LLM-as-a-judge
---

# KoMT-Bench

## Introduction

We present **KoMT-Bench**, a benchmark designed to evaluate the capability of language models in following instructions in Korean.
KoMT-Bench is an in-house dataset created by translating [MT-Bench](https://arxiv.org/abs/2306.05685) [1]  dataset into Korean and modifying some questions to reflect the characteristics and cultural nuances of the Korean language.
After the initial translation and modification, we requested expert linguists to conduct a thorough review of our benchmark dataset.

To conduct evaluations on KoMT-Bench, please visit the official KoMT-Bench [GitHub repository](https://github.com/LG-AI-EXAONE/KoMT-Bench) in which the evaluation scripts are provided.

<p>Here are examples from KoMT-Bench:</p>

<table>
<tr>
  <th>Category</th>
	<th>MT-Bench</th>
	<th>KoMT-Bench</th>
</tr>
<tr height=40>
	<th>Writing</th>
	<!-- <th>MT-Bench</th>
	<th>KoMT-Bench</th> -->
  <th></th>
  <th></th>

</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>Imagine you are writing a blog post comparing two popular smartphone models. Develop an outline for the blog post, including key points and subheadings to effectively compare and contrast the features, performance, and user experience of the two models. Please answer in fewer than 200 words.</td>
	<td>두 개의 인기 스마트폰 모델을 비교하는 블로그 게시물을 작성한다고 가정합니다. 두 모델의 기능, 성능, 사용자 경험을 효과적으로 비교하고 대조할 수 있도록 핵심 사항과 소제목을 포함하여 블로그 게시물의 개요를 작성하세요. 200자 이내로 답하십시오.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>Take your previous response and rephrase it as a limerick.</td>
	<td>이전 답변을 충청도 사투리로 재작성하십시오.</td>
</tr>

<tr height=40>
	<th>Math</th>
	<!-- <th>MT-Bench</th>
	<th>KoMT-Bench</th> -->
  <th></th>
  <th></th>
</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>When a number is divided by 10, the remainder is 4. What is the remainder when twice the number is divided by 4?</td>
	<td>어떤 숫자를 10으로 나눈 나머지는 4입니다. 그 숫자의 두 배를 4로 나눈 나머지를 구하세요.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>What about when twice the number is divided by 5?</td>
	<td>그 숫자의 두 배를 5로 나누면 어떨까요?</td>
</tr>

<tr height=40>
	<th>Humanities</th>
	<!-- <th>MT-Bench</th>
	<th>KoMT-Bench</th> -->
  <th></th>
  <th></th>
</tr>
<tr>
	<td align="center">1st Turn</td>
	<td>Provide insights into the correlation between economic indicators such as GDP, inflation, and unemployment rates. Explain how fiscal and monetary policies affect those indicators.</td>
	<td>GDP, 인플레이션, 실업률과 같은 경제 지표 간의 상관관계에 대한 통찰을 제시하세요. 이러한 지표들에 재정 및 통화 정책이 어떤 영향을 미치는지 설명하세요.</td>
</tr>
<tr>
	<td align="center">2nd Turn</td>
	<td>Now, explain them again like I'm five.</td>
	<td>이제 제가 5살이라 생각하고 다시 설명해 주세요.</td>
</tr>
</table>

<br>

## Models Results

Here are the evaluation results of various language models including [EXAONE 3.0 7.8B instruction-tuned model](https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct) on KoMT-Bench. Please refer to [EXAONE 3.0 technical report](https://arxiv.org/abs/2408.03541) for details.

| | EXAONE 3.0 7.8B Inst. | Llama 3.1 8B Inst. | Gemma 2 9B Inst. | QWEN 2 7B Inst. | Phi 3 7B Inst. | Mistral 7B Inst. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| KoMT-Bench | **8.92** | 6.06 | 7.92 | 7.69 | 4.87 | 5.20 |

<br>

## References

[1] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging llm-as-a-judge with mt-bench and chatbot arena. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems, volume 36, pages 46595–46623. Curran Associates, Inc., 2023.

<br>

## Citation

```
@misc{KoMT-Bench,
  author = {LG AI Research},
  title = {KoMT-Bench},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/datasets/LGAI-EXAONE/KoMT-Bench}}
}
```