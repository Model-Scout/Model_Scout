---
dataset_info:
  features:
  - name: predict_score
    dtype: int64
  - name: response
    dtype: string
  - name: english
    dtype: string
  - name: korean
    dtype: string
  - name: from
    dtype: string
  - name: category
    dtype: string
  - name: en_token_len
    dtype: int64
  - name: ko_token_len
    dtype: int64
  splits:
  - name: train
    num_bytes: 267927608.56265026
    num_examples: 143531
  - name: valid
    num_bytes: 933344.0461038043
    num_examples: 500
  - name: test
    num_bytes: 933344.0461038043
    num_examples: 500
  download_size: 122225341
  dataset_size: 269794296.6548578
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
---


We used [nayohan/llama3-8b-it-prometheus-ko](https://huggingface.co/nayohan/llama3-8b-it-prometheus-ko) to evaluate the [nayohan/translate_corpus_uniform_313k](https://huggingface.co/datasets/nayohan/translate_corpus_uniform_313k) dataset with the criteria listed below.
We filtered out rows with a score of 4,5.

```
def create_conversation(example):
  system_prompt = """###Task Description: An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
  1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
  2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
  3. The output format should look as follows: \"Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)\"
  4. Please do not generate any other opening, closing, and explanations."""

  sample = {
    'orig_instruction': f"영어를 한국어로 번역하세요. {example['source_text']}",
    'orig_response': f"{example['target_text']}",
    'orig_criteria':'모델은 영어 문장을 자연스러운 한국어 문장으로 잘 번역하는 가?',
    'orig_score1_description':'모델은 영어를 한국어로 번역 할 수 있는 능력을 보이지 않는다.',
    'orig_score2_description':'이 모델은 영어를 한국어로 번역할 때, 일부 모순된 내용으로 번역하였다.',
    'orig_score3_description':'이 모델은 영어를 한국어로 번역할 때, 의미를 잘 번역하여 읽을 수 있다.',
    'orig_score4_description':'이 모델은 영어를 한국어로 번역할 때, 의미를 잘 번역하였고, 사람이 쓴 것과 같이 매우 자연스럽다.',
    'orig_score5_description':'이 모델은 영어를 한국어로 번역 시 마치 번역체인지 구분 못하게 사람과 같이 작성되었다.',
  }
  instruction = f"""###The instruction to evaluate: {sample['orig_instruction']}
    ###Response to evaluate: {sample['orig_response']}
    ###Score Rubrics: [{sample['orig_criteria']}]
    Score 1: {sample['orig_score1_description']}
    Score 2: {sample['orig_score2_description']}
    Score 3: {sample['orig_score3_description']}
    Score 4: {sample['orig_score4_description']}
    Score 5: {sample['orig_score5_description']}
    ###Feedback:"""

  conversation = [
              {"role": "system", "content": system_prompt},
              {"role": "user", "content": instruction},
          ]

  text = tokenizer.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors='pt'
  )#.to("cuda")
  example['input']=text
  return example

dataset = load_dataset("nayohan/translate_corpus_uniform_313k")
model_name = "nayohan/llama3-8b-it-prometheus-ko"

tokenizer = AutoTokenizer.from_pretrained(model_name)
dataset = dataset.map(lambda x: create_conversation(x), batched=False, num_proc=32)
print(dataset)
```