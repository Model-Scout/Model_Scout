---
datasets:
- marcuskd/reviews_binary_not4_concat
language:
- 'no'
- nb
- nn
metrics:
- accuracy
- recall
- precision
- f1
---
# Model Card for Model ID

Sentiment analysis for Norwegian reviews.

# Model Description

This model is trained using a self-concatinated dataset consisting of Norwegian Review Corpus dataset (https://github.com/ltgoslo/norec) and a sentiment dataset from huggingface (https://huggingface.co/datasets/sepidmnorozy/Norwegian_sentiment).
Its purpose is merely for testing.


- **Developed by:** Simen Aabol and Marcus Dragsten
- **Finetuned from model:** norbert2

# Direct Use

Plug in Norwegian sentences to check its sentiment (negative to positive)

# Training Details

## Training and Testing Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

https://huggingface.co/datasets/marcuskd/reviews_binary_not4_concat

### Preprocessing

Tokenized using:

```python
tokenizer = AutoTokenizer.from_pretrained("ltgoslo/norbert2")
```
Training arguments for this model:
```python
training_args = TrainingArguments(
    output_dir='./results',          # output directory
    num_train_epochs=10,              # total number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=64,   # batch size for evaluation
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir='./logs',            # directory for storing logs
    logging_steps=10,
)
```

# Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
Evaluation by testing using test-split of dataset.
```python
{
'accuracy': 0.8357214261912695, 
 'recall': 0.886873508353222, 
 'precision': 0.8789025543992431, 
 'f1': 0.8828700403896412, 
 'total_time_in_seconds': 94.33071640000003, 
 'samples_per_second': 31.81360340013276, 
 'latency_in_seconds': 0.03143309443518828
 }
```