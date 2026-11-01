---
language:
- en
- ko
license: cc-by-nc-4.0
task_categories:
- text-generation
dataset_info:
  features:
  - name: source
    dtype: string
  - name: problem
    dtype: string
  - name: problem_ko
    dtype: string
  - name: solution
    dtype: string
  - name: solution_ko
    dtype: string
  splits:
  - name: train
    num_bytes: 2581407207
    num_examples: 859494
  download_size: 1262990465
  dataset_size: 2581407207
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Dataset Card for NuminaMath CoT Korean

🎉 **Translation finished!** If there are any errors, please open the PR. 🎉

If you use this data, please make sure to credit my source!

⚠️ There may be errors in the translation of mathematical terms. (ex: trivial-사소한X/자명한O, negative-부정?음수?)

## Dataset Description

- **Homepage:** https://projectnumina.ai
- **Repository:** https://github.com/project-numina/aimo-progress-prize
- **Paper:** https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf

### Translation

The original data [AI-MO/NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) is in English.

I used **solar-1-mini-translate-enko-240507** to translate into Korean. To see the detailed script on how I did it, please refer to the script below.

### Source breakdown

*The table in the original data shows 859,608, but in reality, there are 859,594 many :)*

| Source | Number of Samples |
| --- | --- |
| aops_forum | 30201 |
| amc_aime | 4072 |
| cn_k12 | 276591 |
| gsm8k | 7345 |
| math | 7478 |
| olympiads | 150581 |
| orca_math | 153334 |
| synthetic_amc | 62111 |
| synthetic_math | 167895 |
| **Total** | **859608** |

### Licensing Information

The dataset is available under the [Creative Commons NonCommercial (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

### Citation Information

```
@misc{numina_math_datasets,
  author = {Jia LI and Edward Beeching and Lewis Tunstall and Ben Lipkin and Roman Soletskyi and Shengyi Costa Huang and Kashif Rasul and Longhui Yu and Albert Jiang and Ziju Shen and Zihan Qin and Bin Dong and Li Zhou and Yann Fleureau and Guillaume Lample and Stanislas Polu},
  title = {NuminaMath},
  year = {2024},
  publisher = {Numina},
  journal = {Hugging Face repository},
  howpublished = {\url{[https://huggingface.co/AI-MO/NuminaMath-CoT](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)}}
}
```

### Python script for translation
Note that you need upstage API Key.
<details><summary>Python Code</summary>
  
```python
  from openai import OpenAI
  client = OpenAI(
      api_key="YOUR_UPSTAGE_API_KEY"
      base_url="https://api.upstage.ai/v1/solar"
  )
  from tqdm import tqdm
  tqdm.pandas()
  import pandas as pd
  import time
  import argparse
  
  def solar_translate_apicall(source_input, previous_translate_results):
      trial_count = 0
      while True:
          try:
              stream = client.chat.completions.create(
                  model="solar-1-mini-translate-enko",
                  messages= previous_translate_results + 
                      [
                          {
                              "role": "user",
                              "content": source_input
                          },
                      ]
                  ,
                  stream=False,
              )
          except Exception as e:
              if e.status_code == 401: # Unauthorized
                  raise Exception(e.response)
              elif e.status_code == 429: # Rate Limit
                  trial_count += 1
                  if trial_count <= 1000:
                      print("Too many requests. Take a rest and retrying...")
                      time.sleep(10)
                      continue
                  else:
                      print("Retried 100 times, but still failed. Please check the server status.")
                      raise Exception(e.response)
              elif e.status_code in [500, 502, 503, 504] : # Internal Server Error
                  trial_count += 1
                  if trial_count <= 1000:
                      print("Internal Server Error. Retrying...")
                      time.sleep(5)
                      continue
                  else:
                      print("Retried 1000 times, but still failed. Please check the server status.")
                      raise Exception(e.response)   
          else:
              break
      return stream.choices[0].message.content
  
  def translate_conversations(input_file, output_file):
      df = pd.read_json(input_file, lines=True)
      # df = df.head(2)
  
      def translate(translate_target):
          # 번역 어투 고정을 위한 예시 하나, 처음 번역에 사용
          TRANSLATE_EXAMPLE = [
              {
                  "role": "user",
                  "content": "Given the functions $f(x) = \log_a(1+x)$ and $g(x) = \log_a(1-x)$, where $a>0$ and $a \neq 1$. 1. Find the domain of the function $f(x) - g(x)$. 2. Determine the parity of the function $f(x) - g(x)$. 3. Find the range of $x$ for which $f(x) - g(x) > 0$."
              },
              {
                  "role": "assistant",
                  "content": "함수 $f(x) = \log_a(1+x)$ 와 $g(x) = \log_a(1-x)$가 주어지고, 여기서 $a>0$이고 $a \neq 1$입니다. 1. 함수 $f(x) - g(x)$의 정의역을 구하세요. 2. 함수 $f(x) - g(x)$의 패리티(parity)를 결정하세요. 3. $f(x) - g(x) > 0$인 $x$의 치역을 찾으세요."
              },
          ]
          previous_translate_results = TRANSLATE_EXAMPLE 
          translate_result = solar_translate_apicall(source_input=translate_target, previous_translate_results=previous_translate_results)
          return translate_result

  def translate_with_question(q_en, q_ko, translate_target):
      # 이전 질문 번역 결과
      TRANSLATE_EXAMPLE = [
          {
              "role": "user",
              "content": q_en
          },
          {
              "role": "assistant",
              "content": q_ko
          },
      ]
      previous_translate_results = TRANSLATE_EXAMPLE 
      translate_result = solar_translate_apicall(source_input=translate_target, previous_translate_results=previous_translate_results)
      return translate_result

  df['problem_ko'] = df['problem'].progress_apply(translate)

  df['solution_ko'] = df.progress_apply(lambda row: translate_with_question(row['problem'], row['problem_ko'], row['solution']), axis=1)

  df = df[['source', 'problem', 'problem_ko', 'solution', 'solution_ko']]
  # Save to jsonl
  df.to_json(output_file, orient='records', lines=True, force_ascii=False)
  print("*****************************")
  print(f"!!!!!!!!!번역 완료!!!!!!!!!!!")
  print("*****************************")

  return

  if __name__ == "__main__":
      parser = argparse.ArgumentParser(description="Process two filenames.")
      parser.add_argument('--filename1', type=str, required=True, help='The first filename.')
      parser.add_argument('--filename2', type=str, required=True, help='The second filename.')
      
      args = parser.parse_args()
      print(f"번역 파일: {args.filename1}")
      translate_conversations(args.filename1, args.filename2)
  
  # RUN: python translate_3.py --filename1 "$input_file" --filename2 "$output_file"
```
</details>