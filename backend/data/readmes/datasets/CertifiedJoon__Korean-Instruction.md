---
license: cdla-permissive-2.0
dataset_info:
  features:
  - name: Instruction
    dtype: string
  - name: Response
    dtype: string
  - name: Source
    dtype: string
  - name: MetaData
    dtype: string
  splits:
  - name: train
    num_bytes: 2099234
    num_examples: 1720
  download_size: 907301
  dataset_size: 2099234
task_categories:
- question-answering
language:
- ko
size_categories:
- n<1K
---
# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** kin.naver.com/qna
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** mjypark1212@gmail.com

### Dataset Summary

The most active korean qna site - Knowledge In Naver. Instruction + response format. Created for language model.

## Dataset Structure

[Instruction, Response, Source, Metadata]