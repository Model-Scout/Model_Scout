---
dataset_info:
- config_name: checker_interactor
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 994149425
    num_examples: 35718
  download_size: 274975300
  dataset_size: 994149425
- config_name: solutions
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: int64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: note
    dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: interaction_format
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 4968074271
    num_examples: 47780
  download_size: 1887049179
  dataset_size: 4968074271
- config_name: solutions_decontaminated
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: note
    dtype: string
  - name: editorial
    dtype: string
  - name: problem
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: interaction_format
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: problem_type
    dtype: string
  - name: public_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: private_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: generated_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: public_tests_ms
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: failed_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: programmingLanguage
      dtype: string
    - name: verdict
      dtype: string
  - name: accepted_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: passed_test_count
      dtype: 'null'
    - name: programmingLanguage
      dtype: string
    - name: programming_language
      dtype: string
    - name: submission_id
      dtype: string
    - name: verdict
      dtype: string
  splits:
  - name: train
    num_bytes: 6719356671
    num_examples: 40665
  download_size: 2023394671
  dataset_size: 6719356671
- config_name: solutions_py
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1000253222
    num_examples: 9556
  download_size: 411697337
  dataset_size: 1000253222
- config_name: solutions_py_decontaminated
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: accepted_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: passed_test_count
      dtype: 'null'
    - name: programmingLanguage
      dtype: string
    - name: programming_language
      dtype: string
    - name: submission_id
      dtype: string
    - name: verdict
      dtype: string
  - name: failed_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: programmingLanguage
      dtype: string
    - name: verdict
      dtype: string
  - name: generated_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: private_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: problem_type
    dtype: string
  - name: public_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: public_tests_ms
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 1349328880
    num_examples: 8133
  download_size: 500182086
  dataset_size: 1349328880
- config_name: solutions_short_and_long_decontaminated
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: note
    dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: interaction_format
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: accepted_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: passed_test_count
      dtype: 'null'
    - name: programmingLanguage
      dtype: string
    - name: programming_language
      dtype: string
    - name: submission_id
      dtype: string
    - name: verdict
      dtype: string
  - name: failed_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: programmingLanguage
      dtype: string
    - name: verdict
      dtype: string
  - name: generated_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: private_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: problem_type
    dtype: string
  - name: public_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: public_tests_ms
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 2699204607
    num_examples: 16266
  download_size: 1002365269
  dataset_size: 2699204607
- config_name: solutions_w_editorials
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: int64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 2649620432
    num_examples: 29180
  download_size: 972089090
  dataset_size: 2649620432
- config_name: solutions_w_editorials_decontaminated
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: int64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: accepted_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: passed_test_count
      dtype: 'null'
    - name: programmingLanguage
      dtype: string
    - name: programming_language
      dtype: string
    - name: submission_id
      dtype: string
    - name: verdict
      dtype: string
  - name: failed_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: programmingLanguage
      dtype: string
    - name: verdict
      dtype: string
  - name: generated_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: private_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: problem_type
    dtype: string
  - name: public_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: public_tests_ms
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 3738669884
    num_examples: 24490
  download_size: 1012247387
  dataset_size: 3738669884
- config_name: solutions_w_editorials_py
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1067124847
    num_examples: 11672
  download_size: 415023817
  dataset_size: 1067124847
- config_name: solutions_w_editorials_py_decontaminated
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: interaction_format
    dtype: string
  - name: note
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: accepted_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: passed_test_count
      dtype: 'null'
    - name: programmingLanguage
      dtype: string
    - name: programming_language
      dtype: string
    - name: submission_id
      dtype: string
    - name: verdict
      dtype: string
  - name: failed_solutions
    list:
    - name: code
      dtype: string
    - name: passedTestCount
      dtype: int64
    - name: programmingLanguage
      dtype: string
    - name: verdict
      dtype: string
  - name: generated_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: private_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: problem_type
    dtype: string
  - name: public_tests
    struct:
    - name: input
      sequence: string
    - name: output
      sequence: string
  - name: public_tests_ms
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 1499075280
    num_examples: 9796
  download_size: 466078291
  dataset_size: 1499075280
- config_name: test_input_generator
  features:
  - name: id
    dtype: string
  - name: aliases
    sequence: string
  - name: contest_id
    dtype: string
  - name: contest_name
    dtype: string
  - name: contest_type
    dtype: string
  - name: contest_start
    dtype: int64
  - name: contest_start_year
    dtype: int64
  - name: index
    dtype: string
  - name: time_limit
    dtype: float64
  - name: memory_limit
    dtype: float64
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: input_format
    dtype: string
  - name: output_format
    dtype: string
  - name: examples
    list:
    - name: input
      dtype: string
    - name: output
      dtype: string
  - name: note
    dtype: string
  - name: editorial
    dtype: string
  - name: prompt
    dtype: string
  - name: generation
    dtype: string
  - name: finish_reason
    dtype: string
  - name: api_metadata
    struct:
    - name: completion_tokens
      dtype: int64
    - name: completion_tokens_details
      dtype: 'null'
    - name: prompt_tokens
      dtype: int64
    - name: prompt_tokens_details
      dtype: 'null'
    - name: total_tokens
      dtype: int64
  - name: interaction_format
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1851104290
    num_examples: 20620
  download_size: 724157877
  dataset_size: 1851104290
configs:
- config_name: checker_interactor
  data_files:
  - split: train
    path: checker_interactor/train-*
- config_name: solutions
  default: true
  data_files:
  - split: train
    path: solutions/train-*
- config_name: solutions_decontaminated
  data_files:
  - split: train
    path: solutions_decontaminated/train-*
- config_name: solutions_py
  data_files:
  - split: train
    path: solutions_py/train-*
- config_name: solutions_py_decontaminated
  data_files:
  - split: train
    path: solutions_py_decontaminated/train-*
- config_name: solutions_short_and_long_decontaminated
  data_files:
  - split: train
    path: solutions_short_and_long_decontaminated/train-*
- config_name: solutions_w_editorials
  data_files:
  - split: train
    path: solutions_w_editorials/train-*
- config_name: solutions_w_editorials_decontaminated
  data_files:
  - split: train
    path: solutions_w_editorials_decontaminated/train-*
- config_name: solutions_w_editorials_py
  data_files:
  - split: train
    path: solutions_w_editorials_py/train-*
- config_name: solutions_w_editorials_py_decontaminated
  data_files:
  - split: train
    path: solutions_w_editorials_py_decontaminated/train-*
- config_name: test_input_generator
  data_files:
  - split: train
    path: test_input_generator/train-*
license: cc-by-4.0
---

# Dataset Card for CodeForces-CoTs


## Dataset description

CodeForces-CoTs is a large-scale dataset for training reasoning models on competitive programming tasks. It consists of 10k CodeForces problems with up to five reasoning traces generated by [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1). We did not filter the traces for correctness, but found that around 84% of the Python ones pass the public tests.

The dataset consists of several subsets: 

- `solutions`: we prompt R1 to solve the problem and produce code.
- `solutions_w_editorials`: we prompt R1 to solve the problem/produce code, but also provide it with a human-written solution.
- `solutions_short_and_long`: a subset of `solutions` where we take the shortest and longest solution from R1.
- `test_input_generator`: we prompt R1 to come up with tricky edge test cases and create a test code generator in Python.
- `checker_interactor`: we prompt R1 to classify problems based on how we should verify the output (some problems are interactive, some allow multiple correct outputs, etc)

Each subset contains a `messages` column, so can be used directly for SFT. We've found that the `solutions` and `solutions_w_editorials` subsets provide best performance, with `solutions` obtaining better performance on LiveCodeBench. Training on `solutions_short_and_long` also results in comparable performance as the full `solutions` subset, but is significantly more data efficient.

By default, all subsets contains C++ generated solutions, except those with a `_py` suffix, which denote Python solutions with just one completion per problem. We also provide decontaminated subsets (indicated with a `_decontaminated` suffix), which have been decontaminated using 8-gram overlap against the AIME24, AIME25, GPQA Diamond, MATH-500, and LiveCodeBench benchmarks. Check out [this script](https://github.com/huggingface/open-r1/blob/main/scripts/decontaminate.py) for the underlying logic. 

You can load the dataset as follows:

```python
from datasets import load_dataset

ds = load_dataset("open-r1/codeforces-cots", "solutions")
```

## Dataset curation

[CodeForces](https://codeforces.com/) is one of the most popular websites among competitive programmers, hosting regular contests where participants must solve challenging algorithmic optimization problems. The challenging nature of these problems makes them an interesting dataset to improve and test models’ code reasoning capabilities.

While previous efforts such as [DeepMind’s CodeContests dataset](https://huggingface.co/datasets/deepmind/code_contests) have compiled a large amount of CodeForces problems, today we are releasing our own `open-r1/codeforces` dataset, with more than **10k problems** covering the very first contests all the way to 2025, **~3k** of which were not included in DeepMind’s dataset. Additionally, for around 60% of problems, we have **included the *editorial*,**  which is an explanation, written by the contest organizers, explaining the correct solution. You will also find 3 correct solutions per problem extracted from the official website.

Furthermore, we are releasing `open-r1/codeforces-cots`, which contains chain of thought generations produced by DeepSeek-R1 on these problems, where we asked the model to produce solutions in C++ (the main language used in competitive programming) and Python, totaling close to **100k** samples.

## License
The dataset is licensed under the Open Data Commons Attribution License (ODC-By) 4.0 license.

## Citation

If you find CodeForces-CoTs useful in your work, please consider citing it as:

```
@misc{penedo2025codeforces,
      title={CodeForces CoTs}, 
      author={Guilherme Penedo and Anton Lozhkov and Hynek Kydlíček and Loubna Ben Allal and Edward Beeching and Agustín Piqueres Lajarín and Quentin Gallouédec and Nathan Habib and Lewis Tunstall and Leandro von Werra},
      year={2025},
      publisher = {Hugging Face},
      journal = {Hugging Face repository},
      howpublished = {\url{https://huggingface.co/datasets/open-r1/codeforces-cots}}
}
```