---
license: apache-2.0
datasets:
- CarrotAI/ko-instruction-dataset
- CarrotAI/Amazing-Instructions
- CarrotAI/kommlu
language:
- ko
base_model:
- Qwen/Qwen2-7B-Instruct
pipeline_tag: text-generation
tags:
- Carrot
- Korea
- mergekit
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/64633ebb39359568c63b52ad/vi2T43yS-HZhsqhnHTvX7.png)

## Model Detail
The model is fine tuned using the Qwen2-7B-Instruct model.


### Score

| Benchmark | Rabbit-Ko-15B-Instruct | Llama 3.1 8B Inst. | Gemma 2 9B Inst. | QWEN 2 7B Inst. | Phi 3 7B Inst. | Mistral 7B | Shot |
|-----------|:-------------------------------:|:------------------:|:-----------------:|:----------------:|:--------------:|:----------:|:----:|
| GSM8K | 80.29 | 75.9 | 77.2 | 62.3 | 86.4 | 47.5 | 5 |
| KMMLU | 47.95 | 41.8 | 40.3 | 46.5 | 37.2 | 31.4 | 5 |
| KoBEST-BoolQ | 91.67 | 87.6 | 89.9 | 90.2 | 76.9 | 84.3 | 5 |
| KoBEST-COPA | 71.30 | 72.8 | 60.6 | 70.3 | 54.5 | 62.9 | 5 |
| KoBEST-WiC | 71.11 | 41.7 | 54.3 | 65.9 | 56.0 | 44.6 | 5 |
| KoBEST-HellaSwag | 45.40 | 44.5 | 42.6 | 46.8 | 34.8 | 42.4 | 5 |
| KoBEST-SentiNeg | 94.96 | 95.2 | 72.0 | 92.9 | 81.0 | 84.7 | 5 |
| Average | 71.81 | 65.64 | 62.41 | 67.84 | 60.97 | 56.83 | - |

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "CarrotAI/Rabbit-Ko-15B-Instruct",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("CarrotAI/Rabbit-Ko-15B-Instruct")

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

### Processing Long Texts
1. **Install vLLM**: You can install vLLM by running the following command.

```bash
pip install "vllm>=0.4.3"
```

Or you can install vLLM from [source](https://github.com/vllm-project/vllm/).

2. **Configure Model Settings**: After downloading the model weights, modify the `config.json` file by including the below snippet:
    ```json
        {
            "architectures": [
                "Qwen2ForCausalLM"
            ],
            // ...
            "vocab_size": 152064,

            // adding the following snippets
            "rope_scaling": {
                "factor": 4.0,
                "original_max_position_embeddings": 32768,
                "type": "yarn"
            }
        }
    ```
    This snippet enable YARN to support longer contexts.

3. **Model Deployment**: Utilize vLLM to deploy your model. For instance, you can set up an openAI-like server using the command:

    ```bash
    python -m vllm.entrypoints.openai.api_server --served-model-name CarrotAI/Rabbit-Ko-15B-Instruct --model path/to/weights
    ```

    Then you can access the Chat API by:

    ```bash
    curl http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
        "model": "CarrotAI/Rabbit-Ko-15B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Your Long Input Here."}
        ]
        }'
    ```

### Applications
This fine-tuned model is particularly suited for [mention applications, e.g., chatbots, question-answering systems, etc.]. Its enhanced capabilities ensure more accurate and contextually appropriate responses in these domains.

### Limitations and Considerations
While our fine-tuning process has optimized the model for specific tasks, it's important to acknowledge potential limitations. The model's performance can still vary based on the complexity of the task and the specificities of the input data. Users are encouraged to evaluate the model thoroughly in their specific context to ensure it meets their requirements.

If you liked this model, please use the card below


```
@article{RabbitKo15BInstruct,
  title={CarrotAI/Rabbit-Ko-15B-Instruct Card},
  author={CarrotAI (L, GEUN)},
  year={2024},
  url = {https://huggingface.co/CarrotAI/Rabbit-Ko-15B-Instruct}
}
```