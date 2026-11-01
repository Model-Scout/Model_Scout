---
license: apache-2.0
language:
- en
- ko
pipeline_tag: text-generation
tags:
- text-generation-inference
- conversational
- motif
---

*Last update: 14th august 2025*

# New
Now you can try out Motif 2.6B on Model Hub: https://model-hub.motiftech.io/

**Select 'Motif 2.6B' from the dropdown next to the Send button.**

# Introduction

We announce **Motif 2.6B**, a 2.6 billion parameter language model trained from scratch on AMD Instinct™ MI250 GPUs. Motif 2.6B marks our very first step toward building helpful, reliable AI aligned with human values. With this initial release, our goal is for Motif 2.6B to match the performance of well-known open-source models such as Gemma, Llama, and Phi — particularly those in the sLLM regime.  
For more details, you can refer to our [technical report](https://arxiv.org/abs/2508.09148).

# Training information

- GPUs: 384 MI250
- Training time: 42 days
- Training data: 2.4T tokens

# Evaluation

When models are released, their accompanying technical reports or papers often present benchmark results based on evaluation settings chosen by the developers. While this is a common and understandable practice, it can lead to challenges when comparing models across different organizations. The same model may yield different scores depending on evaluation conditions, and details of these conditions are not always fully disclosed. This lack of standardization can make it difficult for the open-source community to interpret and trust reported results. We therefore reference performance scores based on the official numbers reported by each model’s developers in their respective publications.

To illustrate how much evaluation scores can vary across reports, we provide concrete examples of benchmark score differences for major models in the **Evaluation Appendix**.

### Comparison to Mistral 7B by Mistral AI

The benchmarks and corresponding scores listed in the table below are taken directly from the [Mistral 7B technical report](https://arxiv.org/pdf/2310.06825).

|Benchmark|Metric|Mistral 7B|Motif 2.6B|Improvement|
|---|---|---|---|---|
|MMLU|5-shot|60.1|57.93|-3.61%|
|HellaSwag|0-shot|81.3|61.35|-24.54%|
|WinoG|0-shot|75.3|59.91|-20.44%|
|PIQA|0-shot|83|75.95|-8.49%|
|Arc-e|0-shot|80|87.21|+9.01%|
|Arc-c|0-shot|55.5|74.2|+33.69%|
|NQ|5-shot|28.8|11.14|-61.32%|
|TriviaQA|5-shot|69.9|54.97|-21.36%|
|HumanEval|0-shot|30.5|68.3|+123.93%|
|MBPP|3-shot|47.5|60.3|+26.95%|
|MATH|4-shot, maj@4|13.1|40.2*|+206.87%|
|GSM8K|8-shot, maj@8|52.2|75.66**|+44.94%|
||||**Average**|**+25.47%**|

\* : We report the 4-shot, maj@1 score instead of the 4-shot, maj@4.
\** : We report the 8-shot, maj@1 score instead of the 8-shot, maj@8.

### Comparison to the Gemma series by Google

#### Gemma 1 & 2
The benchmarks and corresponding scores listed in the table below are taken directly from the [Gemma 2 technical report](https://arxiv.org/abs/2408.00118).

*Note: Although referred to as "2B", Gemma 2 2B actually has <U>2.6 billion</U> parameters.*

|Benchmark|Metric|Gemma 1 2B|Gemma 1 7B|Gemma 2 2B|Gemma 2 9B|Motif 2.6B|Improvement(over 1 1B)|Improvement(over 1 7B)|Improvement(over 2 2B)|Improvement(over 2 9B)|
|---|---|---|---|---|---|---|---|---|---|---|
|MMLU|5-shot|42.3|64.4|52.2|71.3|57.93|+36.95%|-10.05%|+10.98%|-18.75%|
|ARC-C|25-shot|48.5|61.1|55.7|68.4|75.08|+54.80%|+22.88%|+34.79%|+9.77%|
|GSM8K|5-shot|15.1|51.8|24.3|68.6|75.13|+397.55%|+45.04%|+309.18%|+9.52%|
|AGIEval|3-5-shot|24.2|44.9|31.5|52.8|-|-|-|-|-|
|DROP|3-shot, F1|48.5|56.3|51.2|69.4|29.33|-39.53%|-47.90%|-42.71%|-57.74%|
|BBH|3-shot, CoT|35.2|59|41.9|68.2|48.56|37.95%|-17.69%|+15.89%|-28.80%|
|Winogrande|5-shot|66.8|79|71.3|80.6|67.09|+0.43%|-15.08%|-5.90%|-16.76%|
|HellaSwag|10-shot|71.7|82.3|72.9|81.9|69.89|-2.52%|-15.08%|-4.13%|-14.66%|
|MATH|4-shot|11.8|24.3|16|36.6|40.2|+240.88%|+65.43%|+151.25%|+9.84%|
|ARC-e|0-shot|73.2|81.5|80.6|88|87.21|+19.14%|+7.01%|+8.20%|-0.90%|
|PIQA|0-shot|77.3|81.2|78.4|81.7|75.95|-1.75%|-6.47%|-3.13%|-7.04%|
|SIQA|0-shot|49.7|51.8|51.9|53.4|61.97|+24.69%|+19.63%|+19.40%|+16.05%|
|Boolq|0-shot|69.4|83.2|72.7|84.2|67.76|-2.36%|-18.56%|-6.80%|-19.52%|
|TriviaQA|5-shot|53.2|63.4|60.4|76.6|54.97|+3.33%|-13.30%|-8.99%|-28.24%|
|NQ|5-shot|12.5|23|17.1|29.2|10.91|-12.72%|-52.57%|-36.20%|-62.64%|
|HumanEval|pass@1|22|32.3|20.1|40.2|68.3|+210.45%|+111.46%|+239.80%|+69.90%|
|MBPP|3-shot|29.2|44.4|30.2|52.4|60.3|+106.51%|+35.81%|+99.67%|+15.08%|
|||||||**Average**|**+90.79%**|**+3.44%**|**+46.17%**|**-13.45%**|

#### Gemma 3
The benchmarks and corresponding scores listed in the table below are taken directly from the [Gemma 3 technical report](https://arxiv.org/abs/2503.19786).

|Benchmark|Metric|Gemma 3 1B|Gemma 3 4B|Motif 2.6B|Improvement(over 1B)|Improvement(over 4B)|
|---|---|---|---|---|---|---|
|HellaS|10-shot|62.3|77.2|69.89|+12.18%|-9.47%|
|BoolQ|0-shot|63.2|72.3|67.76|+7.22%|-6.28%|
|PIQA|0-shot|73.8|79.6|75.59|+2.43%|-5.04%|
|SIQA|0-shot|48.9|51.9|61.97|+26.73%|+19.40%|
|TQA|5-shot|39.8|65.8|54.97|+38.12%|-16.46%|
|NQ|5-shot|9.48|20|10.91|+15.08%|-45.45%|
|ARC-C|25-shot|38.4|56.2|75.08|+95.52%|+33.59%|
|ARC-E|0-shot|73|82.4|87.21|+19.47%|+5.84%|
|WinoG|5-shot|58.2|64.7|67.09|+15.27%|+3.69%|
|BBH|few-shot, CoT|28.4|50.9|48.56|+70.99%|-4.60%|
|Drop|1-shot, F1|42.4|60.1|29.33|-30.83%|-51.20%|
|MMLU|5-shot|-|59.6|57.93|-|-2.80%|
|MMLUpro|5-shot, CoT|-|29.2|-|-|-|
|AGIE|3-5-shot|-|42.1|-|-|-|
|MATH|4-shot, CoT|-|24.2|40.2|-|+66.12%|
|GSM8K|8-shot, CoT|-|38.4|80.21|-|+108.88%|
|GPQA Diamond|5-shot, CoT|-|15|31.81|-|+112.07%|
|MBPP|3-shot|-|46|60.3|-|+31.09%|
|HumanE|0-shot|-|36|68.3|-|+89.72%|
|IFEval|-|80.2|90.2|74.02|-7.71%|-17.94%|
|||||**Average**|**+22.04%**|**+17.29%**|

### Comparison to the Llama series by Meta

#### Llama 3
The benchmarks and corresponding scores listed in the table below are taken directly from the [Llama 3 technical report](https://arxiv.org/abs/2407.21783).

|Benchmark|Metric|Llama 3 8B|Motif 2.6B|Improvement|
|---|---|---|---|---|
|MMLU|5-shot|69.4|57.93|-16.53%|
|MMLU|0-shot, CoT|73|57.95|-20.62%|
|MMLU-Pro|5-shot, CoT|48.3|-|-|
|IFEval|-|80.4|74.02|-7.94%|
|HumanEval|0-shot|72.6|68.3|-5.92%|
|MBPP|0-shot|72.8|57.93|-20.43%|
|GSM8K|8-shot, CoT|84.5|80.21|-5.08%|
|MATH|0-shot, CoT|51.9|49.68|-4.28%|
|ARC Challenge|0-shot|83.4|74.2|-11.03%|
|GPQA|0-shot, CoT|32.8|18.53|-43.51%|
||||**Average**|**-15.04%**|

#### Llama 3.2
The benchmarks and corresponding scores listed in the table below are taken directly from the [Llama 3.2 official blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/).

|Benchmark|Metric|Llama 3.2 1B|Llama 3.2 3B|Motif 2.6B|Improvement(over 1B)|Improvement(over 3B)|
|---|---|---|---|---|---|---|
|MMLU|0-shot|49.3|63.4|57.6|+16.75%|-9.21%|
|Open-rewrite eval*|0-shot, rougeL|41.6|40.1|-|-|-|
|TLDR9+|test, 1-shot, rougeL|16.8|19|-|-|-|
|IFEval|-|59.5|77.4|74.02|+24.40%|-4.37%|
|GSM8K|8-shot, CoT|44.4|77.7|80.21|+80.65%|+3.23%|
|MATH|0-shot, CoT|30.6|48|49.68|+62.35%|+3.50%|
|ARC Challenge|0-shot|59.4|78.6|74.2|+24.92%|-5.6%|
|GPQA|0-shot|27.2|32.8|25.45|-6.43%|-22.41%|
|Hellaswag|0-shot|41.2|69.8|61.35|+48.91%|-12.11%|
|||||**Average**|**+41.82%**|**-2.49%**|

### Comparison to the Phi series by Microsoft
The benchmarks and corresponding scores listed in the table below are taken directly from the [Phi-3 technical report](https://arxiv.org/abs/2404.14219).

|Benchmark|Metric|Phi-3 3.8B|Phi-3 7B|Phi-2 2.7B|Motif 2.6B|Improvement(over 3.8B)|Improvement(over 7B)|Improvement(over 2.7B)|
|---|---|---|---|---|---|---|---|---|
|MMLU|5-shot|68.8|75.7|56.3|57.93|-15.80%|-23.47%|+2.90%|
|HellaSwag|5-shot|76.7|77|53.6|68.97|-10.08%|-10.43%|+28.68%|
|ANLI|7-shot|52.8|58.1|42.5|47.99|-9.11%|-17.40%|+12.92%|
|GSM-8K|8-shot, CoT|82.5|89.6|61.1|80.21|-2.78%|-10.48%|+31.28%|
|MATH|0-shot, CoT|41.3|34.6|-|49.68|+20.29%|+43.58%|-|
|MedQA|2-shot|53.8|65.4|40.9|42.1|-21.75%|-35.63%|+2.93%|
|AGIEval|0-shot|37.5|45.1|29.8|-|-|-|-|
|TriviaQA|5-shot|64|58.1|45.2|54.97|-14.11%|-5.39%|+21.62%|
|Arc-C|10-shot|84.9|90.7|75.9|75.17|-11.46%|-17.12%|-0.96%|
|Arc-E|10-shot|94.6|97|88.5|88.64|-6.30%|-8.62%|+0.16%|
|PIQA|5-shot|84.2|86.9|60.2|78.29|-7.02%|-9.91%|+30.05%|
|SociQA|5-shot|76.6|79.2|68.3|66.73|-12.89%|-15.74%|-2.3%|
|BigBench-Hard|3-shot, CoT|71.7|79.1|59.4|48.56|-32.27%|-38.61%|-18.25%|
|WinoGrande|5-shot|70.8|81.5|54.7|67.09|-5.24%|-17.68%|+22.65%|
|OpenBookQA|10-shot|83.2|88|73.6|87.8|+5.53%|-0.23%|+19.29%|
|BoolQ|2-shot|77.2|84.8|-|70.7|-8.42%|-16.63%|-|
|CommonSenseQA|10-shot|80.2|80|69.3|71.25|-11.16%|-10.94%|2.81%|
|TruthfulQA|10-shot|65|70.2|-|52.07|-19.89%|-25.83%|-|
|HumanEval|0-shot|58.5|61|59|68.29|+16.74%|+11.95%|+15.75%|
|MBPP|3-shot|70|71.7|60.6|60.3|-13.86%|-15.90%|-0.50%|
|GPQA|2-shot, CoT|32.8|34.3|-|27.9|-14.94%|-18.66%|-|
|MT Bench|2R. Avg.|8.38|8.7|-|6.77|-19.21%|-22.18%|-|
||||||**Average**|**-9.87%**|**-13.25%**|**+10.56%**|

## Evaluation Appendix

In the comparisons presented above, Motif 2.6B showed average performance improvements of -15.36% and -13.45% over Llama 3 8B and Gemma 2 9B, respectively, based on the benchmark scores reported in their original technical reports. However, when compared to the benchmarks and scores reported in the Qwen 2.5 technical report, Motif 2.6B shows an average improvement of +19.27% over Llama 3 8B and +1.68% over Gemma 2 9B. See the table below for details.

### Comparison to Llama 3 8B and Gemma 2 9B based on scores from the *Qwen2.5 technical report*
The benchmarks and corresponding scores listed in the table below are taken directly from the [Qwen2.5 technical report](https://arxiv.org/abs/2412.15115).

|Benchmark|Metric|Llama 3 8B|Gemma 2 9B|Motif 2.6B|Improvement(over Llama 3 8B)|Improvement(over Gemma 2 9B)|
|---|---|---|---|---|---|---|
|MMLU|5-shot|66.6|71.3|57.93|-13.02%|-18.75%|
|MMLU-pro|5-shot|35.4|44.7|28.4|-19.77%|-36.47%|
|MMLU-redux|5-shot|61.6|67.9|59.54|-3.34%|-12.31%|
|BBH|3-shot|57.7|68.2|39.28|-31.92%|-42.40%|
|ARC-C|25-shot|59.3|68.2|75.08|+26.61%|+10.09%|
|TruthfulQA|0-shot|44|45.3|41.55|-5.56%|-8.27%|
|Winogrande|5-shot|77.4|79.5|67.09|-13.32%|-15.61%|
|HellaSwag|10-shot|82.1|81.9|69.88|-14.88%|-14.68%|
|GPQA|5-shot|25.8|32.8|29.24|+13.33%|-10.85%|
|TheoremQA|5-shot|22.1|28.9|-|-|-|
|MATH|4-shot|20.5|37.7|40.2|+96.10%|+6.63%|
|MMLU-stem|5-shot|55.3|65.1|52.9|-4.34%|-18.74%|
|GSM8K|4-shot|55.3|70.7|75.2|+35.99%|+6.36%|
|HumanEval|0-shot|33.5|37.8|68.3|+103.88%|+80.69%|
|HumanEval+|0-shot|29.3|30.5|62.2|+112.29%|+103.93%|
|MBPP|0-shot|53.9|62.2|60.3|+11.87%|-3.05%|
|MBPP+|0-shot|44.4|50.6|50.8|+14.41%|+0.40%|
|MultiPL-E|0-shot|22.6|34.9|-|-|-|
|||||**Average**|**+19.27%**|**+1.68%**|


## How to use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Motif-Technologies/Motif-2.6B",
    trust_remote_code = True, 
    _attn_implementation = "eager", # also supports flash_attention_2
).cuda()

tokenizer = AutoTokenizer.from_pretrained(
    "Motif-Technologies/Motif-2.6B", 
    trust_remote_code = True, 
)

query = "What is the capital city of South Korea?"
input_ids = tokenizer.apply_chat_template(
    [
        {'role': 'system', 'content': 'you are an helpful assistant'},
        {'role': 'user', 'content': query},
    ],
    add_generation_prompt = True,
    return_tensors='pt',
).cuda()

output = model.generate(input_ids, max_new_tokens=128, pad_token_id=tokenizer.eos_token_id)
output = tokenizer.decode(output[0, input_ids.shape[-1]:], skip_special_tokens = True)
print(output)

"""
The capital city of South Korea is Seoul. Located in the southern part of the country, Seoul is not only the largest city in South Korea but also one of the largest metropolitan areas in the world.
It is a vibrant and dynamic city known for its rich history, cultural heritage, and modern amenities. Seoul is a major economic, cultural, and political center in East Asia, and it plays a crucial role in the region's politics, economy, and culture.
The city is divided into different administrative districts, each with its own unique characteristics and attractions.
"""