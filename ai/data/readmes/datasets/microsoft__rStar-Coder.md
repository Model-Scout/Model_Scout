---
pretty_name: rStar-Coder
configs:
- config_name: synthetic_sft
  data_files:
  - split: train
    path: synthetic_sft/*.parquet
- config_name: synthetic_rl
  data_files:
  - split: train
    path: synthetic_rl/*.parquet
- config_name: synthetic_rl_testcase
  data_files:
  - split: train
    path: synthetic_rl_testcase/*.parquet
- config_name: seed_sft
  data_files:
  - split: train
    path: seed_sft/*.parquet
- config_name: seed_testcase
  data_files:
  - split: train
    path: seed_testcase/*.parquet
license: cc-by-4.0
---
# rStar-Coder Dataset

<div align="center">

[Project GitHub](https://github.com/microsoft/rStar) | [Paper](https://arxiv.org/abs/2505.21297)

</div>

## Dataset Description
rStar-Coder is a large-scale competitive code problem dataset containing 418K programming problems, 580K long-reasoning solutions, and rich test cases of varying difficulty levels. This dataset aims to enhance code reasoning capabilities in large language models, particularly in handling competitive code problems.

Experiments on Qwen models (1.5B-14B) across various  code reasoning benchmarks demonstrate the superiority of rStar-Coder dataset, achieving leading performance comparable to frontier reasoning LLMs with much smaller model sizes. On LiveCodeBench, rStar-Coder improves Qwen2.5-7B from 17.4% to an impressive 57.3%,  and Qwen2.5-14B from 23.3% to 62.5%, surpassing o3-mini (low) by 3.1%. On the more challenging USA Computing Olympiad, our 7B model achieves an average pass@1 accuracy of 16.15%, outperforming the frontier-level QWQ-32B.  


| Model                                     |  LiveCodeBench   |    HumanEval    |    HumanEval+    |      MBPP       |      MBPP+      |
| ----------------------------------------- | :--------------: | :-------------: | :--------------: | :-------------: | :-------------: |
| GPT-4o                                    |       30.0       |      92.7       |       87.2       |      87.6       |      72.2       |
| Claude3.5-Sonnet                          |       32.0       |      92.1       |        86        |       91        |      74.6       |
| OpenAI o3-mini-2025-01-31 (low)           |       59.4       |        -        |        -         |        -        |        -        |
| QWQ-32B                                   |       63.4       |      95.6       |       89.8       |      92.2       |      76.5       |
| OpenAI o1                                 |       63.4       |        -        |        -         |        -        |        -        |
| DeepSeek-R1                               |       65.9       |      96.3       |       90.9       |      95.3       |      81.2       |
| Gemini-2.5-Pro                            |       69.2       |        -        |        -         |        -        |        -        |
| *1.5B Long-CoT coder reasoning* LLMs        |                  |                 |                  |                 |                 |
| DeepSeek-R1-Distill-Qwen-1.5B             |       16.9       |      66.3       |       61.8       |      57.1       |      48.5       |
| **rStar-Coder-1.5B**                      | **40.1 (+33.6)** | **88.4(+17.7)** | **81.7 (+16.5)** | **74.1 (+8.9)** | **60.8 (+1.5)** |
| Bespoke-Stratos-7B(Bespoke-Stratos-17k)   |       16.2       |      75.1       |       69.1       |      73.6       |      59.8       |
| OpenThinker-7B (OpenThoughts-114k)        |       25.5       |      80.5       |       75.7       |      80.9       |      68.2       |
| OpenThinker2-7B (OpenThoughts2-1M)        |       37.4       |      92.7       |       87.8       |      86.9       |      73.9       |
| DeepSeek-R1-Distill-Qwen-7B               |       37.6       |      89.6       |       83.7       |      78.4       |      66.7       |
| DeepSeek-R1-Distill-LLaMA3-8B             |       39.6       |      85.9       |       79.7       |      62.7       |      52.8       |
| OlympicCoder-7B (OpenR1-codeforces-100k)  |       40.9       |      82.1       |       76.9       |      80.0       |      66.4       |
| OCR-Qwen-7B-Instruct (OCR-736k)           |       51.3       |        -        |        -         |        -        |        -        |
| **rStar-Coder-7B**                        | **57.3 (+39.9)** | **95.9 (+7.5)** | **90.8 (+6.7)**  | **87.9 (+4.4)** | **74.0 (+2.3)** |
| *14B-70B Long-CoT reasoning* LLMs           |                  |                 |                  |                 |                 |
| DeepSeek-R1-Distill-Qwen-14B              |       53.1       |      96.1       |       89.8       |      87.4       |      74.1       |
| OCR-Qwen-14B-Instruct (OCR-736k)          |       59.4       |        -        |        -         |        -        |        -        |
| Bespoke-Stratos-32B                       |       48.9       |      95.5       |       89.8       |      93.8       |      77.5       |
| DeepSeek-R1-Distill-Qwen-32B              |       57.2       |      95.9       |       89.9       |      92.8       |      78.7       |
| OpenThinker-32B (OpenThoughts-114k)       |       54.1       |      94.8       |       89.2       |      94.1       |      78.4       |
| OlympicCoder-32B (OpenR1-codeforces-100k) |       57.4       |      90.0       |       85.2       |      86.7       |      71.3       |
| OCR-Qwen-32B-Instruct (OCR-736k)          |       61.7       |        -        |        -         |        -        |        -        |
| DeepSeek-R1-Distill-LLaMA-70B             |       57.5       |      96.5       |       90.7       |      91.9       |      77.1       |
| **rStar-Coder-14B**                       | **62.5 (+39.2)** | **95.9 (+6.3)** | **89.6 (+2.4)**  | **91.4 (+5.2)** | **77.3 (+4.5)** |


## Quick Start
The dataset comprises five distinct subsets, categorized by data origin (human-seeded or synthetic) and training paradigm (SFT or RL).
### 📁 Subset Overview
| Subset Name             | Problem Type  | Key Fields                                                                                          | Description                          |
|------------------------|---------------|-----------------------------------------------------------------------------------------------------|--------------------------------------|
| `synthetic_sft`        | Synthetic     | `question`, `seed_question`, `seed_source`, `response`, `code`                                      | Supervised fine-tuning (SFT)         |
| `synthetic_rl`         | Synthetic     | `question_id`, `question`, `seed_question`, `seed_source`                                           | RL problem set                       |
| `synthetic_rl_testcase`| Synthetic     | `question_id`, `question`, `inputs`, `outputs`                                                      | RL test cases (passed through mutual-verification) |
| `seed_sft`             | Human-seeded  | `question_id`, `question`, `starter_code`, `response`, `code`, `verified`, `is_passed`                      | Supervised fine-tuning (SFT)         |
| `seed_testcase`        | Human-seeded  | `question_id`, `question`, `starter_code`, `inputs`, `outputs`, `is_synthesized`, `test_case_type`, `func_name`, `class_name` | RL test cases (both official and solution-validated generated cases)|


---

### 1  Quick Preview of Dataset Structure
```python
from datasets import load_dataset

def truncate_text(text, max_length=100):
    """Truncate text to max_length and add ellipsis if needed"""
    text_str = str(text)
    return text_str[:max_length] + "..." if len(text_str) > max_length else text_str

def preview_subset(ds, subset_name):
    """Preview the first example from a dataset subset
    
    Args:
        ds: Dataset object to preview
        subset_name: Name of the subset being previewed
    """
    print(f"\n{'='*20} Preview of {subset_name} {'='*20}")
    example = next(iter(ds))
    for key, value in example.items():
        print(f"\n{key}:")
        print(f"  {truncate_text(value)}")

def main():
    print("\n=== Loading specific parquet shards ===")
    
    # synthetic_sft subset (using a small shard: data-00003 out of 15 shards)
    ds = load_dataset(
        "microsoft/rStar-Coder",
        data_files="synthetic_sft/data-00003-of-00015.parquet",
        split="train"
    )
    preview_subset(ds, "synthetic_sft (shard 3/15)")
    
    # synthetic_rl subset
    ds = load_dataset(
        "microsoft/rStar-Coder",
        data_files="synthetic_rl/data-00000-of-00001.parquet",
        split="train"
    )
    preview_subset(ds, "synthetic_rl (shard 0/1)")
    
    # seed_sft subset (using a small shard: data-00000 out of 20 shards)
    ds = load_dataset(
        "microsoft/rStar-Coder",
        data_files="seed_sft/data-00000-of-00020.parquet",
        split="train"
    )
    preview_subset(ds, "seed_sft (shard 0/20)")
    
    # seed_testcase subset (using a small shard: data-00009 out of 30 shards)
    ds = load_dataset(
        "microsoft/rStar-Coder",
        data_files="seed_testcase/data-00009-of-00030.parquet",
        split="train"
    )
    preview_subset(ds, "seed_testcase (shard 9/30)")
    
    # synthetic_rl_testcase subset (using a small shard: data-00008 out of 797 shards)
    ds = load_dataset(
        "microsoft/rStar-Coder",
        data_files="synthetic_rl_testcase/data-00008-of-00797.parquet",
        split="train"
    )
    preview_subset(ds, "synthetic_rl_testcase (shard 8/797)")

if __name__ == "__main__":
    main()
```

After running this script, you'll get the following output: a preview of each subset’s structure and content — including problem descriptions, test cases, solutions, and other metadata fields. This helps you get a sense of the format and content of each subset before diving into the full dataset.

```
=== Loading specific parquet shards ===

==================== Preview of synthetic_sft (shard 3/15) ====================

question:
  Problem Description:
Consider you have a sequence of integers along with a series of transformation ...

seed_question:
  Recently, Chef found a new formula for computing powers of a sequence:
- You are given two sequences...

seed_source:
  codechef

response:
  Okay, I need to solve this programming problem. Let me try to understand what the problem is asking....

code:
  def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
...

==================== Preview of synthetic_rl (shard 0/1) ====================

question_id:
  synthetic_0

question:
  **Problem Description**:
In a large playground, there are `n` children and `m` food stalls positione...

seed_question:
  Palo Alto is an unusual city because it is an endless coordinate line. It is also known for the offi...

seed_source:
  codeforces

==================== Preview of seed_sft (shard 0/20) ====================

question_id:
  seed_0

question:
  Chef has a cubic die with 6 faces kept on an infinite plane. Each face has a distinct integer in the...

starter_code:
  

response:
  Okay, so I need to solve this problem where Chef rolls a die multiple times and records the top face...

code:
  def generate_all_pairings():
    nums = [1, 2, 3, 4, 5, 6]
    all_pairings = []

    def backtrack(...

verified:
  False

is_passed:
  False

==================== Preview of seed_testcase (shard 9/30) ====================

question_id:
  seed_30092

question:
  Vasya has an array *a* consisting of positive integer numbers. Vasya wants to divide this array into...

starter_code:
  

inputs:
  ["3\n1 3 2", "5\n1 2 3 4 5", "5\n2 2 3 4 5", "5\n72 32 17 46 82", "6\n26 10 70 11 69 57", "7\n4 7 10...

outputs:
  ["YES", "NO", "YES", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO",...

is_synthesized:
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...

test_case_type:
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...

func_name:
  

class_name:
  

==================== Preview of synthetic_rl_testcase (shard 8/797) ====================

question_id:
  synthetic_54262

question:
  Problem Description:
Given an integer `n`, count all the numbers not greater than `n` that do not co...

inputs:
  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "100", "1000", "10000", "100000", "1000000"]

outputs:
  ["1", "1", "1", "1", "1", "1", "1", "1", "2", "8", "57", "456", "3652", "29169"]
```

### 2  Get the data


> ⚠️ **Dataset size alert**
>
> * All splits together exceed **480 GB**. Make sure you have enough disk space.
> * When preprocessing locally, each worker keeps one batch in RAM—tune `num_proc` and `writer_batch_size` to match your memory budget.

#### Option A  Load directly from the Hub

```python
from datasets import load_dataset
# Choose a subset from synthetic_sft/synthetic_rl/synthetic_rl_testcase/seed_sft/seed_testcase
ds = load_dataset("microsoft/rStar-Coder", "synthetic_sft", split="train")            # full download
```

#### Option B  Download first, then load locally
You can choose to download using either command-line or Python code:
```shell
huggingface-cli download microsoft/rStar-Coder \
        --repo-type dataset \
        --local-dir ./rStar-Coder \
        --local-dir-use-symlinks False \
        --resume-download \
        --max-workers 16  
```
```python
from huggingface_hub import snapshot_download
from datasets import load_dataset

snapshot_download(
    repo_id="microsoft/rStar-Coder",
    repo_type="dataset",               # Specify that this is a dataset repo
    local_dir="/data/rStar-Coder",     # Local directory to download the dataset to
    local_dir_use_symlinks=False,      # Avoid symbolic links (for better compatibility)
    resume_download=True,              # Enable resume capability for interrupted downloads
    max_workers=8,                     # Number of parallel threads for faster downloading
)

ds = load_dataset("/data/rStar-Coder", "synthetic_sft", split="train")
```

#### Option C  Stream from the Hub

```python
from datasets import load_dataset
# Choose a subset from synthetic_sft/synthetic_rl/synthetic_rl_testcase/seed_sft/seed_testcase
ds = load_dataset("microsoft/rStar-Coder", "synthetic_sft", split="train", streaming=True)  # stream as you iterate on the dataset
```

---

### 3  Parse test cases

For `synthetic_rl_testcase` subset, you need to parse the `inputs` and `outputs` columns.

```python
# pip install --upgrade "datasets>=2.19.0" "pyarrow>=15.0.0"
from datasets import load_dataset, Features, Sequence, Value
import json

# ------------- Step 1  Load raw split -------------
raw_ds = load_dataset("microsoft/rStar-Coder", "synthetic_rl_testcase", split="train")   # or local path


# ------------- Step 2  Row-level JSON parser -------------
def parse_multiple_json(example):
    example["inputs"]  = json.loads(example["inputs"])
    example["outputs"] = json.loads(example["outputs"])
    return example

# ------------- Step 3  Dynamic Arrow schema -------------
schema = Features({
    "question_id" : Value("string"),
    "question"  : Value("string"),
    "inputs"    : Sequence(Value("large_string")),   # avoids 2 GB offset overflow
    "outputs"   : Sequence(Value("large_string")),
})

# ------------- Step 4  Multiprocess map -------------
processed_ds = raw_ds.map(
    parse_multiple_json,
    num_proc=32,            # ↓ decrease if RAM is limited
    writer_batch_size=1000, # smaller batches → lower peak memory
    features=schema,
    desc="Parsing JSON columns",
)

# ------------- Step 5  (Optionally) save to disk -------------
processed_ds.save_to_disk("processed_synthetic_rl_testcase")
```

For `seed_testcase` subset, you need to parse the `inputs`, `outputs`, `is_synthesized`, and `test_case_type` columns.

```python
# pip install --upgrade "datasets>=2.19.0" "pyarrow>=15.0.0"
from datasets import load_dataset, Features, Sequence, Value
import json

# ------------- Step 1  Load raw split -------------
raw_ds = load_dataset("microsoft/rStar-Coder", "seed_testcase", split="train")   # or local path

# ------------- Step 2  Row-level JSON parser -------------
def parse_multiple_json(example):
    example["inputs"]  = json.loads(example["inputs"])
    example["outputs"] = json.loads(example["outputs"])
    example["is_synthesized"] = json.loads(example["is_synthesized"])
    example["test_case_type"] = json.loads(example["test_case_type"])
    return example

# ------------- Step 3  Dynamic Arrow schema -------------
schema = Features({
    "question_id" : Value("string"),
    "question"  : Value("string"),
    "starter_code" : Value("string"),
    "inputs"    : Sequence(Value("large_string")),
    "outputs"   : Sequence(Value("large_string")),
    "is_synthesized" : Sequence(Value("int64")),
    "test_case_type" : Sequence(Value("int64")),
    "func_name" : Value("string"),
    "class_name": Value("string"),
})

# ------------- Step 4  Multiprocess map -------------
processed_ds = raw_ds.map(
    parse_multiple_json,
    num_proc=32,            # ↓ decrease if RAM is limited
    writer_batch_size=1000, # smaller batches → lower peak memory
    features=schema,
    desc="Parsing JSON columns",
)

# ------------- Step 5  (Optionally) save to disk -------------
processed_ds.save_to_disk("processed_seed_testcase")
```

## Dataset structure

1. **Synthetic SFT Subset**
    - question: The synthesized programming problem description
    - seed_question: The original problem that was used as a seed for synthesis
    - seed_source: The source platform where the seed problem was obtained
    - response: The long cot solution
    - code: The implementation code for the solution

2. **Synthetic RL Subset**
    - question_id: Unique identifier for linking problems with their test cases
    - question: The synthesized programming problem description
    - seed_question: The original problem that was used as a seed for synthesis
    - seed_source: The source platform where the seed problem was obtained

3. **Seed SFT Subset**
    - question_id: Unique identifier for linking problems with their test cases
    - question: The original competitive programming problem description
    - starter_code: Initial code template provided with the problem
    - response: The long cot solution
    - code: The implementation code for the solution
    - verified: Boolean flag indicating whether the solution has been verified with test cases
    - is_passed: Boolean flag indicating whether the solution has passed the test cases

4. **Synthetic RL Test Case Subset**
    - question_id: Unique identifier for linking problems with their test cases
    - question: The synthesized programming problem description
    - inputs: List of input test cases (need to be parsed)
    - outputs: List of expected outputs for corresponding inputs (need to be parsed)

5. **Seed Test Case Subset**
    - question_id: Unique identifier for linking problems with their test cases
    - question: The original competitive programming problem description
    - starter_code: Initial code template provided with the problem
    - inputs: List of input test cases (need to be parsed)
    - outputs: List of expected outputs for corresponding inputs (need to be parsed)
    - is_synthesized: Boolean list indicating whether each test case was synthesized (0 is official testcase, 1 is synthesized)
    - test_case_type: List specifying the format of each test case:
        * "standard_io": Standard input/output format (0)
        * "param_dict": Parameter dictionary format (1)
        * "assert": Assertion-based test cases (2)
    - func_name: The name of the function to be tested (if applicable)
    - class_name: The name of the class containing the solution (if applicable)


## License
The rStar-Coder dataset is licensed under the CC BY 4.0.

## Citation
If you use this dataset, please cite:
```
@misc{liu2025rstarcoderscalingcompetitivecode,
      title={rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset}, 
      author={Yifei Liu and Li Lyna Zhang and Yi Zhu and Bingcheng Dong and Xudong Zhou and Ning Shang and Fan Yang and Mao Yang},
      year={2025},
      eprint={2505.21297},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.21297}, 
}
```