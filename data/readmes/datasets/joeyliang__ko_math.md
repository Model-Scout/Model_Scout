---
dataset_info:
- config_name: algebra
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 4088
    num_examples: 5
  - name: test
    num_bytes: 715481
    num_examples: 1187
  download_size: 382855
  dataset_size: 719569
- config_name: counting_and_probability
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 4747
    num_examples: 5
  - name: test
    num_bytes: 400483
    num_examples: 474
  download_size: 201859
  dataset_size: 405230
- config_name: geometry
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 11636
    num_examples: 5
  - name: test
    num_bytes: 560329
    num_examples: 479
  download_size: 290232
  dataset_size: 571965
- config_name: intermediate_algebra
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 4584
    num_examples: 5
  - name: test
    num_bytes: 881899
    num_examples: 903
  download_size: 433463
  dataset_size: 886483
- config_name: number_theory
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 2480
    num_examples: 5
  - name: test
    num_bytes: 393393
    num_examples: 540
  download_size: 199557
  dataset_size: 395873
- config_name: prealgebra
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 2781
    num_examples: 5
  - name: test
    num_bytes: 561925
    num_examples: 871
  download_size: 301541
  dataset_size: 564706
- config_name: precalculus
  features:
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 6599
    num_examples: 5
  - name: test
    num_bytes: 598982
    num_examples: 546
  download_size: 267068
  dataset_size: 605581
configs:
- config_name: algebra
  data_files:
  - split: train
    path: algebra/train-*
  - split: test
    path: algebra/test-*
- config_name: counting_and_probability
  data_files:
  - split: train
    path: counting_and_probability/train-*
  - split: test
    path: counting_and_probability/test-*
- config_name: geometry
  data_files:
  - split: train
    path: geometry/train-*
  - split: test
    path: geometry/test-*
- config_name: intermediate_algebra
  data_files:
  - split: train
    path: intermediate_algebra/train-*
  - split: test
    path: intermediate_algebra/test-*
- config_name: number_theory
  data_files:
  - split: train
    path: number_theory/train-*
  - split: test
    path: number_theory/test-*
- config_name: prealgebra
  data_files:
  - split: train
    path: prealgebra/train-*
  - split: test
    path: prealgebra/test-*
- config_name: precalculus
  data_files:
  - split: train
    path: precalculus/train-*
  - split: test
    path: precalculus/test-*
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
language:
- ko
size_categories:
- 10K<n<100K
---