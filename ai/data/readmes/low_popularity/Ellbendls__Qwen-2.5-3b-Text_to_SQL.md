---
library_name: transformers
license: mit
datasets:
- gretelai/synthetic_text_to_sql
base_model:
- Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-generation
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---
# Fine-Tuned LLM for Text-to-SQL Conversion

This model is a fine-tuned version of [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) designed to convert natural language queries into SQL statements. It was trained on the `gretelai/synthetic_text_to_sql` dataset and can provide both SQL queries and table schema context when needed.

---

## Model Details

### Model Description

This model has been fine-tuned to help users generate SQL queries based on natural language prompts. In scenarios where table schema context is missing, the model is trained to generate schema definitions along with the SQL query, making it a robust solution for various Text-to-SQL tasks.

- **Base Model:** [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
- **Dataset:** [Gretel AI Synthetic Text-to-SQL Dataset](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql)
- **Language:** English
- **License:** MIT

### Key Features

1. **Text-to-SQL Conversion:** Converts natural language queries into accurate SQL statements.
2. **Schema Generation:** Generates table schema context when none is provided.
3. **Optimized for Analytics and Reporting:** Handles SQL queries with aggregation, grouping, and filtering.

---

## Usage

### Direct Use

To use the model for text-to-SQL conversion, you can load it using the `transformers` library as shown below:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Ellbendls/Qwen-2.5-3b-Text_to_SQL")
model = AutoModelForCausalLM.from_pretrained("Ellbendls/Qwen-2.5-3b-Text_to_SQL")

# Input prompt
query = "What is the total number of hospital beds in each state?"

# Tokenize input and generate output
inputs = tokenizer(query, return_tensors="pt")
outputs = model.generate(**inputs, max_length=512)

# Decode and print
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Example Output
Input:  
`What is the total number of hospital beds in each state?`  

Output:  
```sql
Context:
CREATE TABLE Beds (State VARCHAR(50), Beds INT);
INSERT INTO Beds (State, Beds) VALUES ('California', 100000), ('Texas', 85000), ('New York', 70000);

SQL Query:
SELECT State, SUM(Beds) FROM Beds GROUP BY State;
```

---

## Training Details

### Dataset

The model was fine-tuned on the `gretelai/synthetic_text_to_sql` dataset, which includes diverse natural language queries mapped to SQL queries, with optional schema contexts.

## Limitations

1. **Complex Queries:** May struggle with highly nested or advanced SQL tasks.
2. **Non-English Prompts:** Optimized for English only.
3. **Context Dependence:** May generate incorrect schemas without explicit instructions.
