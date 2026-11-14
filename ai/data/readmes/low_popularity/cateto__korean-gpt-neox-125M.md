---
license: cc-by-3.0
language:
- ko
pipeline_tag: text-generation
---
# korean-gpt-neox-125M 

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** [cateto](http://github.com/cateto)
- **Model type:** [gpt-neox](https://github.com/EleutherAI/gpt-neox)
- **Language(s) (NLP):** Korean

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

```python
# Import the transformers library
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("cateto/korean-gpt-neox-125M")

model = AutoModelForCausalLM.from_pretrained("cateto/korean-gpt-neox-125M")

# Get user input
user_input = "우리는 앞으로 더나은 미래를"

# Encode the prompt using the tokenizer
input_ids = tokenizer.encode(user_input, return_tensors="pt")

# Generate chatbot output using the model
output_ids = model.generate(
    input_ids,
    num_beams=4,
    repetition_penalty=1.5,
    no_repeat_ngram_size=3
)

# Decode chatbot output ids as text
bot_output = tokenizer.decode(output_ids.tolist()[0], skip_special_tokens=True)

# Print chatbot output
print(f"출력 ## ", bot_output)

# 출력 ##  우리는 앞으로 더나은 미래를 향해 나아갈 수 있다.
```

