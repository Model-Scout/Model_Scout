---
dataset_info:
  features:
  - name: llm
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_en
    dtype: string
  - name: answer_en
    dtype: string
  - name: generated
    dtype: string
  - name: label
    dtype: bool
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 1051241760
    num_examples: 192426
  download_size: 386947470
  dataset_size: 1051241760
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

원본 데이터: [kuotient/orca-math-korean-preference](https://huggingface.co/datasets/kuotient/orca-math-korean-preference)

question, chosen 칼럼에 대해서 다음과 같은 필터링 수행
1. 수식에 띄어쓰기 indentation 제거
2. 특정 숫자가 반복적으로 생성되었던 데이터 제거 

문제 샘플 예시
```
죽은 닭의 수 = 400의 40%
                            = 0.40 * 400
                            = 160마리 닭

표현을 단계별로 분석해 보겠습니다: 1. 곱을 계산합니다: - \( 476 \times 100 = 47600 \) - \( 424 \times 100 = 42400 \) 2. 곱을 더합니다: - \( 47600 + 42400 = 90000 \) 3. 2^3으로 곱합니다(8입니다): - \( 90000 \times 8 = 720000 \) 4. 476 \times 100 \times 424 \times 100 \)의 곱을 계산합니다: - \( 47600 \times 42400 = 20182400000 \) 5. 4를 곱합니다: - \( 4 \times 2018240000 = 80729600000 \) 6. 첫 번째 곱에서 두 번째 곱을 뺍니다: - \( 720000 - 8072960000 = -80722400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

전처리 코드
```python
from tqdm.auto import tqdm
from datasets import load_dataset, Dataset
import re
from collections import Counter

def simplify_whitespace(text):
    # 연속된 공백을 하나의 공백으로 치환
    simplified = re.sub(r'\s+', ' ', text)
    
    # 각 줄의 시작 부분 공백 제거
    simplified = re.sub(r'^\s+', '', simplified, flags=re.MULTILINE)
    
    # 빈 줄 제거
    simplified = re.sub(r'\n\s*\n', '\n', simplified)
    
    return simplified.strip()

def has_repetition_patterns(text, char_repeat_threshold=50, ngram_repeat_threshold=4, ngram_size=3):
    # 1. 특정 character repetition 검사
    char_pattern = r'(.)\1{' + str(char_repeat_threshold) + ',}'
    if re.search(char_pattern, text):
        return True

    # 2. 특정 n-gram 반복 검사
    # words = text.split()
    # ngrams = [' '.join(words[i:i+ngram_size]) for i in range(len(words)-ngram_size+1)]
    # ngram_counts = Counter(ngrams)

    # if any(count > ngram_repeat_threshold for count in ngram_counts.values()):
    #     return True

    return False


# 사용 예시
i = 0
dataset = load_dataset("kuotient/orca-math-korean-preference", split="train")
new_items = []
for item in tqdm(dataset):
    item["question"] = simplify_whitespace(item["question"])
    item["chosen"] = simplify_whitespace(item["chosen"])

    q_repetite = has_repetition_patterns(item["question"])
    a_repetite = has_repetition_patterns(item["chosen"])

    if q_repetite:
        print("Q:", item["question"])
        i += 1
    if a_repetite:
        print("A:", item["chosen"])
        i += 1

    if not q_repetite and not a_repetite:
        new_items.append(item)

print("Total:", len(dataset))
print("Problems:", i)

new_ds = Dataset.from_list(new_items)
new_ds.push_to_hub("heegyu/orca-math-korean-preference-cleaned")

```

N-gram 처리도 하려고 했는데, 수학문제 특정상 수식을 작성하는 과정에서 반복되는 n-gram이 많아서 주석처리했음.
코드는 claude-3.5-sonnet의 도움을 받아 작성
