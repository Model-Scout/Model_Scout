---
language: ko
pipeline_tag: text-generation
license: llama3.1
---

### 1. Model Description
- KONI (KISTI Open Natural Intelligence) is a specialized large language model (LLM) developed by the Korea Institute of Science and Technology Information (KISTI). This model is specifically designed for science and technology, making it highly effective for tasks in these fields.

### 2. Key Features
- **Specialized in Science and Technology:** The model is explicitly trained on a vast and specialized corpus of scientific and technological data.
- **Enhanced Performance:** This version of KONI shows significantly improved performance compared to its initial release in December, 2023.
- **Base Model:** The base model for KONI-Llama3.1-8B-Instruct-20241024 is KONI-Llama3.1-8B-Merged-20240830, which is a merger of Meta-Llama-3-8B and KISTI-KONI/KONI-Llama3.1-8B-20240824
- **Alignment:** SFT (Supervised Fine-Tuning) and DPO (Direct Preference Optimization) are applied

### 3. Data
- Approximately 11k SFT data and 7k DPO data are used.
- **SFT Data:** The SFT data includes both internally generated data and publicly available data on Hugging Face, translated into Korean where necessary.
- **DPO Data:** The DPO data consists of translated and curated data from argilla/dpo-mix-7k.

### 4. Benchmark Results
The performances were evaluated using the [LogicKor](https://github.com/instructkr/LogicKor) benchmark dataset as follows:

| Metric         | Score |
|:--------------:|:-----:|
| Reasoning      |  8.15 |
| Math           |  8.79 |
| Writing        |  9.22 |
| Coding  |  9.21 |
| Comprehension        |  9.65 |
| Grammar      |  8.57 |
| Single-turn      |  9.05 |
| Multi-turn    |  8.81 |
| **Overall**    | **8.93** |

### 5. How to use the model
```python
import transformers
import torch

model_id = "KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

pipeline.model.eval()

instruction = "안녕? 너는 누구야?"

messages = [
   {"role": "user", "content": f"{instruction}"}
    ]

prompt = pipeline.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

print(outputs[0]["generated_text"][len(prompt):])
```
```
안녕하세요! 저는 KISTI의 KONI입니다. 과학기술 데이터를 전문으로 처리하며, 여러분의 연구와 질문에 최선을 다해 도움을 드리겠습니다. 무엇을 도와드릴까요?
```

### 6. Citation
**Language Model**
```text
@article{KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024,
  title={KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024},
  author={KISTI},
  year={2024},
  url={https://huggingface.co/KISTI-KONI/KONI-Llama3.1-8B-Instruct-20241024}
}
```
  
### 7. Contributors
- KISTI, Large-scale AI Research Group

### 8. Special Thanks
- [@beomi](https://huggingface.co/beomi)
- [@kuotient](https://huggingface.co/kuotient)
- KyungTae Lim

### 8. Acknowledgement
- This research was supported by Korea Institute of Science and Technology Information(KISTI).
- This work was supported by the National Supercomputing Center with supercomputing resources including technical support (KISTI).

### 9. References
- https://huggingface.co/meta-llama/Meta-Llama-3.1-8B
- https://huggingface.co/meta-llama/meta-llama/Meta-Llama-3.1-8B-Instruct