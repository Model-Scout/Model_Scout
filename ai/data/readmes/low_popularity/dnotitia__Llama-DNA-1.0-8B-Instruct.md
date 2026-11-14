---
language:
- en
- ko
license: cc-by-nc-4.0
tags:
- dnotitia
- nlp
- llm
- slm
- conversation
- chat
base_model:
- meta-llama/Meta-Llama-3.1-8B
library_name: transformers
pipeline_tag: text-generation
---

# DNA 1.0 8B Instruct

<p align="center">
<img src="assets/dna-logo.png" width="400" style="margin: 40px auto;">
</p>

**DNA 1.0 8B Instruct** is a <u>state-of-the-art (**SOTA**)</u> bilingual language model based on Llama architecture, specifically optimized for Korean language understanding and generation, while also maintaining strong English capabilities. The model was developed through a sophisticated process involving model merging via spherical linear interpolation (**SLERP**) with Llama 3.1 8B Instruct, and underwent knowledge distillation (**KD**) using Llama 3.1 405B as the teacher model. It was extensively trained through continual pre-training (**CPT**) with a high-quality Korean dataset. The training pipeline was completed with supervised fine-tuning (**SFT**) and direct preference optimization (**DPO**) to align with human preferences and enhance instruction-following abilities.

<p align="center">
<img src="assets/training-procedure.png" width="600" style="margin: 40px auto;">
</p>

DNA 1.0 8B Instruct was fine-tuned on approximately 7B tokens of carefully curated data and has undergone extensive instruction tuning to enhance its ability to follow complex instructions and engage in natural conversations.

For more details, please refer to our [Technical Report](https://arxiv.org/abs/2501.10648).

- **Developed by:** Dnotitia Inc.
- **Supported Languages:** Korean, English
- **Model Release Date:** Dec 10, 2024
- **Vocab Size:** 128,256
- **Context Length:** 131,072 tokens (128k)
- **License:** CC BY-NC 4.0

<div style="padding: 2px 8px; background-color: hsl(240, 100%, 50%, 0.1); border-radius: 5px">
  <p><strong>NOTICE (Korean):</strong></p>
  <p>본 모델은 상업적 목적으로 활용하실 수 있습니다. 상업적 이용을 원하시는 경우, <a href="https://www.dnotitia.com/contact/post-form">Contact us</a>를 통해 문의해 주시기 바랍니다. 간단한 협의 절차를 거쳐 상업적 활용을 승인해 드리도록 하겠습니다.</p>
</div>

## Evaluation

We evaluated DNA 1.0 8B Instruct against other prominent language models of similar size across various benchmarks, including Korean-specific tasks and general language understanding metrics.

| Language | Benchmark  | **dnotitia/Llama-DNA-1.0-8B-Instruct** | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct | LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct | yanolja/EEVE-Korean-Instruct-10.8B-v1.0 | Qwen/Qwen2.5-7B-Instruct | meta-llama/Llama-3.1-8B-Instruct | mistralai/Mistral-7B-Instruct-v0.3 | NCSOFT/Llama-VARCO-8B-Instruct | upstage/SOLAR-10.7B-Instruct-v1.0 |
|----------|------------|----------------------------------------|--------------------------------------|--------------------------------------|-----------------------------------------|--------------------------|----------------------------------|------------------------------------|--------------------------------|-----------------------------------|
| Korean   | KMMLU      | **53.26** (1st)                        | 45.30                                | 45.28                                | 42.17                                   | <u>45.66</u>             | 41.66                            | 31.45                              | 38.49                          | 41.50                             |
|          | KMMLU-hard | **29.46** (1st)                        | 23.17                                | 20.78                                | 19.25                                   | <u>24.78</u>             | 20.49                            | 17.86                              | 19.83                          | 20.61                             |
|          | KoBEST     | **83.40** (1st)                        | 79.05                                | 80.13                                | <u>81.67</u>                            | 78.51                    | 67.56                            | 63.77                              | 72.99                          | 73.26                             |
|          | Belebele   | **57.99** (1st)                        | 40.97                                | 45.11                                | 49.40                                   | <u>54.85</u>             | 54.70                            | 40.31                              | 53.17                          | 48.68                             |
|          | CSATQA     | <u>43.32</u> (2nd)                     | 40.11                                | 34.76                                | 39.57                                   | **45.45**                | 36.90                            | 27.27                              | 32.62                          | 34.22                             |
| English  | MMLU       | 66.64 (3rd)                            | 65.27                                | 64.32                                | 63.63                                   | **74.26**                | <u>68.26</u>                     | 62.04                              | 63.25                          | 65.30                             |
|          | MMLU-Pro   | **43.05** (1st)                        | 40.73                                | 38.90                                | 32.79                                   | <u>42.5</u>              | 40.92                            | 33.49                              | 37.11                          | 30.25                             |
|          | GSM8K      | **80.52** (1st)                        | 65.96                                | <u>80.06</u>                         | 56.18                                   | 75.74                    | 75.82                            | 49.66                              | 64.14                          | 69.22                             |
- The *highest* *scores* are in **bold** form, and the *second*\-*highest* *scores* are <u>underlined</u>.

**Evaluation Protocol**   
For easy reproduction of our evaluation results, we list the evaluation tools and settings used below:

|            | Evaluation setting | Metric                              | Evaluation tool |
|------------|--------------------|-------------------------------------|-----------------|
| KMMLU      | 5-shot             | macro\_avg / exact\_match           | lm-eval-harness |
| KMMLU Hard | 5-shot             | macro\_avg / exact\_match           | lm-eval-harness |
| KoBEST     | 5-shot             | macro\_avg / f1                     | lm-eval-harness |
| Belebele   | 0-shot             | acc                                 | lm-eval-harness |
| CSATQA     | 0-shot             | acc\_norm                           | lm-eval-harness |
| MMLU       | 5-shot             | macro\_avg / acc                    | lm-eval-harness |
| MMLU Pro   | 5-shot             | macro\_avg / exact\_match           | lm-eval-harness |
| GSM8K      | 5-shot             | acc, exact\_match & strict\_extract | lm-eval-harness |

## Quickstart

This model requires `transformers >= 4.43.0`.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

tokenizer = AutoTokenizer.from_pretrained('dnotitia/Llama-DNA-1.0-8B-Instruct')
model = AutoModelForCausalLM.from_pretrained('dnotitia/Llama-DNA-1.0-8B-Instruct', device_map='auto')
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

conversation = [
    {"role": "system", "content": "You are a helpful assistant, Dnotitia DNA."},
    {"role": "user", "content": "너의 이름은?"},
]
inputs = tokenizer.apply_chat_template(conversation,
                                       add_generation_prompt=True,
                                       return_dict=True,
                                       return_tensors="pt").to(model.device)
_ = model.generate(**inputs, streamer=streamer)
```

## Limitations

While DNA 1.0 8B Instruct demonstrates strong performance, users should be aware of the following limitations:

- The model may occasionally generate biased or inappropriate content
- Responses are based on training data and may not reflect current information
- The model may sometimes produce factually incorrect or inconsistent answers
- Performance may vary depending on the complexity and domain of the task
- Generated content should be reviewed for accuracy and appropriateness

## License

This model is released under CC BY-NC 4.0 license. For commercial usage inquiries, please [Contact us](https://www.dnotitia.com/contact/post-form).

## Appendix

- KMMLU scores comparison chart:
<img src="assets/comparison-chart.png" width="100%" style="margin: 40px auto;">

- DNA 1.0 8B Instruct model architecture <sup>[1]</sup>:
<img src="assets/model-architecture.png" width="500" style="margin: 40px auto;">

[1]: <https://www.linkedin.com/posts/sebastianraschka_the-llama-32-1b-and-3b-models-are-my-favorite-activity-7248317830943686656-yyYD/>

- The median percentage of model’s weight difference between before and after the merge (our SFT model + Llama 3.1 8B Instruct):
<img src="assets/ours-vs-merged.png" width="100%" style="margin: 40px auto;">

## Citation

If you use or discuss this model in your academic research, please cite the project to help spread awareness:

```
@misc{lee2025dna10technicalreport,
      title={DNA 1.0 Technical Report}, 
      author={Jungyup Lee and Jemin Kim and Sang Park and SeungJae Lee},
      year={2025},
      eprint={2501.10648},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.10648}, 
}
```

