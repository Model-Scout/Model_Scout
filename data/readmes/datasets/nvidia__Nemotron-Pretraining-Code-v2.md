---
license: other
task_categories:
- text-generation
extra_gated_prompt: >-
  By clicking “Agree” I confirm I have read and agree to NVIDIA Data Agreement
  for Model Training and agree that I intend to use this data for model training
  purposes only.
  (https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md) 
extra_gated_fields:
  Company: text
  Institutional Email: text
  I agree to use this dataset for model training purposes ONLY: checkbox
configs:
  - config_name: Nemotron-Code-Metadata
    data_files: 
    - path:
      - Nemotron-Code-Metadata/part_00000.parquet
      - Nemotron-Code-Metadata/part_00001.parquet
      - Nemotron-Code-Metadata/part_00002.parquet
      - Nemotron-Code-Metadata/part_00003.parquet
      - Nemotron-Code-Metadata/part_00004.parquet
      - Nemotron-Code-Metadata/part_00005.parquet
      - Nemotron-Code-Metadata/part_00006.parquet
      - Nemotron-Code-Metadata/part_00007.parquet
      - Nemotron-Code-Metadata/part_00008.parquet
      - Nemotron-Code-Metadata/part_00009.parquet
      - Nemotron-Code-Metadata/part_00010.parquet
      - Nemotron-Code-Metadata/part_00011.parquet
      - Nemotron-Code-Metadata/part_00012.parquet
      - Nemotron-Code-Metadata/part_00013.parquet
      - Nemotron-Code-Metadata/part_00014.parquet
      - Nemotron-Code-Metadata/part_00015.parquet
      - Nemotron-Code-Metadata/part_00016.parquet
      - Nemotron-Code-Metadata/part_00017.parquet
      - Nemotron-Code-Metadata/part_00018.parquet
      - Nemotron-Code-Metadata/part_00019.parquet
      - Nemotron-Code-Metadata/part_00020.parquet
      - Nemotron-Code-Metadata/part_00021.parquet
      - Nemotron-Code-Metadata/part_00022.parquet
      - Nemotron-Code-Metadata/part_00023.parquet
      - Nemotron-Code-Metadata/part_00024.parquet
      - Nemotron-Code-Metadata/part_00025.parquet
      - Nemotron-Code-Metadata/part_00026.parquet
      - Nemotron-Code-Metadata/part_00027.parquet
      - Nemotron-Code-Metadata/part_00028.parquet
      - Nemotron-Code-Metadata/part_00029.parquet
      - Nemotron-Code-Metadata/part_00030.parquet
      - Nemotron-Code-Metadata/part_00031.parquet
      - Nemotron-Code-Metadata/part_00032.parquet
      - Nemotron-Code-Metadata/part_00033.parquet
      - Nemotron-Code-Metadata/part_00034.parquet
      - Nemotron-Code-Metadata/part_00035.parquet
      - Nemotron-Code-Metadata/part_00036.parquet
      - Nemotron-Code-Metadata/part_00037.parquet
      - Nemotron-Code-Metadata/part_00038.parquet
      - Nemotron-Code-Metadata/part_00039.parquet
      - Nemotron-Code-Metadata/part_00040.parquet
      - Nemotron-Code-Metadata/part_00041.parquet
      - Nemotron-Code-Metadata/part_00042.parquet
      - Nemotron-Code-Metadata/part_00043.parquet
      - Nemotron-Code-Metadata/part_00044.parquet
      - Nemotron-Code-Metadata/part_00045.parquet
      - Nemotron-Code-Metadata/part_00046.parquet
      - Nemotron-Code-Metadata/part_00047.parquet
      - Nemotron-Code-Metadata/part_00048.parquet
      - Nemotron-Code-Metadata/part_00049.parquet
      - Nemotron-Code-Metadata/part_00050.parquet
      - Nemotron-Code-Metadata/part_00051.parquet
      - Nemotron-Code-Metadata/part_00052.parquet
      - Nemotron-Code-Metadata/part_00053.parquet
      - Nemotron-Code-Metadata/part_00054.parquet
      - Nemotron-Code-Metadata/part_00055.parquet
      - Nemotron-Code-Metadata/part_00056.parquet
      - Nemotron-Code-Metadata/part_00058.parquet
      - Nemotron-Code-Metadata/part_00059.parquet
      - Nemotron-Code-Metadata/part_00060.parquet
      - Nemotron-Code-Metadata/part_00061.parquet
      - Nemotron-Code-Metadata/part_00062.parquet
      - Nemotron-Code-Metadata/part_00063.parquet
      split: train
  - config_name: Synthetic-Question-Answering
    data_files:
    - path: 
      - Synthetic-Code/synthetic-question-answering/part_00000.parquet
      - Synthetic-Code/synthetic-question-answering/part_00001.parquet
      - Synthetic-Code/synthetic-question-answering/part_00002.parquet
      - Synthetic-Code/synthetic-question-answering/part_00003.parquet
      - Synthetic-Code/synthetic-question-answering/part_00004.parquet
      - Synthetic-Code/synthetic-question-answering/part_00005.parquet
      - Synthetic-Code/synthetic-question-answering/part_00006.parquet
      - Synthetic-Code/synthetic-question-answering/part_00007.parquet
      - Synthetic-Code/synthetic-question-answering/part_00008.parquet
      - Synthetic-Code/synthetic-question-answering/part_00009.parquet
      - Synthetic-Code/synthetic-question-answering/part_00010.parquet
      - Synthetic-Code/synthetic-question-answering/part_00011.parquet
      - Synthetic-Code/synthetic-question-answering/part_00012.parquet
      - Synthetic-Code/synthetic-question-answering/part_00013.parquet
      - Synthetic-Code/synthetic-question-answering/part_00014.parquet
      - Synthetic-Code/synthetic-question-answering/part_00015.parquet
      - Synthetic-Code/synthetic-question-answering/part_00016.parquet
      - Synthetic-Code/synthetic-question-answering/part_00017.parquet
      - Synthetic-Code/synthetic-question-answering/part_00018.parquet
      - Synthetic-Code/synthetic-question-answering/part_00019.parquet
      - Synthetic-Code/synthetic-question-answering/part_00020.parquet
      - Synthetic-Code/synthetic-question-answering/part_00021.parquet
      - Synthetic-Code/synthetic-question-answering/part_00022.parquet
      - Synthetic-Code/synthetic-question-answering/part_00023.parquet
      - Synthetic-Code/synthetic-question-answering/part_00024.parquet
      - Synthetic-Code/synthetic-question-answering/part_00025.parquet
      - Synthetic-Code/synthetic-question-answering/part_00026.parquet
      - Synthetic-Code/synthetic-question-answering/part_00027.parquet
      - Synthetic-Code/synthetic-question-answering/part_00028.parquet
      - Synthetic-Code/synthetic-question-answering/part_00029.parquet
      - Synthetic-Code/synthetic-question-answering/part_00030.parquet
      - Synthetic-Code/synthetic-question-answering/part_00031.parquet
      - Synthetic-Code/synthetic-question-answering/part_00032.parquet
      - Synthetic-Code/synthetic-question-answering/part_00033.parquet
      - Synthetic-Code/synthetic-question-answering/part_00034.parquet
      - Synthetic-Code/synthetic-question-answering/part_00035.parquet
      - Synthetic-Code/synthetic-question-answering/part_00036.parquet
      - Synthetic-Code/synthetic-question-answering/part_00037.parquet
      - Synthetic-Code/synthetic-question-answering/part_00038.parquet
      - Synthetic-Code/synthetic-question-answering/part_00039.parquet
      - Synthetic-Code/synthetic-question-answering/part_00040.parquet
      - Synthetic-Code/synthetic-question-answering/part_00041.parquet
      - Synthetic-Code/synthetic-question-answering/part_00042.parquet
      - Synthetic-Code/synthetic-question-answering/part_00043.parquet
      - Synthetic-Code/synthetic-question-answering/part_00044.parquet
      - Synthetic-Code/synthetic-question-answering/part_00045.parquet
      - Synthetic-Code/synthetic-question-answering/part_00046.parquet
      - Synthetic-Code/synthetic-question-answering/part_00047.parquet
      - Synthetic-Code/synthetic-question-answering/part_00048.parquet
      - Synthetic-Code/synthetic-question-answering/part_00049.parquet
      - Synthetic-Code/synthetic-question-answering/part_00050.parquet
      - Synthetic-Code/synthetic-question-answering/part_00051.parquet
      - Synthetic-Code/synthetic-question-answering/part_00052.parquet
      - Synthetic-Code/synthetic-question-answering/part_00053.parquet
      - Synthetic-Code/synthetic-question-answering/part_00054.parquet
      - Synthetic-Code/synthetic-question-answering/part_00055.parquet
      - Synthetic-Code/synthetic-question-answering/part_00056.parquet
      - Synthetic-Code/synthetic-question-answering/part_00057.parquet
      - Synthetic-Code/synthetic-question-answering/part_00058.parquet
      - Synthetic-Code/synthetic-question-answering/part_00059.parquet
      - Synthetic-Code/synthetic-question-answering/part_00060.parquet
      - Synthetic-Code/synthetic-question-answering/part_00061.parquet
      - Synthetic-Code/synthetic-question-answering/part_00062.parquet
      - Synthetic-Code/synthetic-question-answering/part_00063.parquet
      split: train
  - config_name: Synthetic-Student-Teacher
    data_files:
    - path:
      - Synthetic-Code/synthetic-student-teacher/part_00000.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00001.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00002.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00003.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00004.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00005.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00006.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00007.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00008.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00009.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00010.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00011.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00012.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00013.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00014.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00015.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00016.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00017.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00018.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00019.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00020.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00021.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00022.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00023.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00024.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00025.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00026.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00027.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00028.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00029.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00030.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00031.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00032.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00033.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00034.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00035.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00036.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00037.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00038.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00039.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00040.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00041.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00042.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00043.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00044.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00045.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00046.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00047.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00048.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00049.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00050.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00051.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00052.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00053.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00054.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00055.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00056.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00057.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00058.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00059.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00060.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00061.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00062.parquet
      - Synthetic-Code/synthetic-student-teacher/part_00063.parquet
      split: train
  - config_name: Synthetic-Code-Review
    data_files:
    - path:
      - Synthetic-Code/synthetic-code-review/part_00000.parquet
      - Synthetic-Code/synthetic-code-review/part_00001.parquet
      - Synthetic-Code/synthetic-code-review/part_00002.parquet
      - Synthetic-Code/synthetic-code-review/part_00003.parquet
      - Synthetic-Code/synthetic-code-review/part_00004.parquet
      - Synthetic-Code/synthetic-code-review/part_00005.parquet
      - Synthetic-Code/synthetic-code-review/part_00006.parquet
      - Synthetic-Code/synthetic-code-review/part_00007.parquet
      - Synthetic-Code/synthetic-code-review/part_00008.parquet
      - Synthetic-Code/synthetic-code-review/part_00009.parquet
      - Synthetic-Code/synthetic-code-review/part_00010.parquet
      - Synthetic-Code/synthetic-code-review/part_00011.parquet
      - Synthetic-Code/synthetic-code-review/part_00012.parquet
      - Synthetic-Code/synthetic-code-review/part_00013.parquet
      - Synthetic-Code/synthetic-code-review/part_00014.parquet
      - Synthetic-Code/synthetic-code-review/part_00015.parquet
      - Synthetic-Code/synthetic-code-review/part_00016.parquet
      - Synthetic-Code/synthetic-code-review/part_00017.parquet
      - Synthetic-Code/synthetic-code-review/part_00018.parquet
      - Synthetic-Code/synthetic-code-review/part_00019.parquet
      - Synthetic-Code/synthetic-code-review/part_00020.parquet
      - Synthetic-Code/synthetic-code-review/part_00021.parquet
      - Synthetic-Code/synthetic-code-review/part_00022.parquet
      - Synthetic-Code/synthetic-code-review/part_00023.parquet
      - Synthetic-Code/synthetic-code-review/part_00024.parquet
      - Synthetic-Code/synthetic-code-review/part_00025.parquet
      - Synthetic-Code/synthetic-code-review/part_00026.parquet
      - Synthetic-Code/synthetic-code-review/part_00027.parquet
      - Synthetic-Code/synthetic-code-review/part_00028.parquet
      - Synthetic-Code/synthetic-code-review/part_00029.parquet
      - Synthetic-Code/synthetic-code-review/part_00030.parquet
      - Synthetic-Code/synthetic-code-review/part_00031.parquet
      - Synthetic-Code/synthetic-code-review/part_00032.parquet
      - Synthetic-Code/synthetic-code-review/part_00033.parquet
      - Synthetic-Code/synthetic-code-review/part_00034.parquet
      - Synthetic-Code/synthetic-code-review/part_00035.parquet
      - Synthetic-Code/synthetic-code-review/part_00036.parquet
      - Synthetic-Code/synthetic-code-review/part_00037.parquet
      - Synthetic-Code/synthetic-code-review/part_00038.parquet
      - Synthetic-Code/synthetic-code-review/part_00039.parquet
      - Synthetic-Code/synthetic-code-review/part_00040.parquet
      - Synthetic-Code/synthetic-code-review/part_00041.parquet
      - Synthetic-Code/synthetic-code-review/part_00042.parquet
      - Synthetic-Code/synthetic-code-review/part_00043.parquet
      - Synthetic-Code/synthetic-code-review/part_00044.parquet
      - Synthetic-Code/synthetic-code-review/part_00045.parquet
      - Synthetic-Code/synthetic-code-review/part_00046.parquet
      - Synthetic-Code/synthetic-code-review/part_00047.parquet
      - Synthetic-Code/synthetic-code-review/part_00048.parquet
      - Synthetic-Code/synthetic-code-review/part_00049.parquet
      - Synthetic-Code/synthetic-code-review/part_00050.parquet
      - Synthetic-Code/synthetic-code-review/part_00051.parquet
      - Synthetic-Code/synthetic-code-review/part_00052.parquet
      - Synthetic-Code/synthetic-code-review/part_00053.parquet
      - Synthetic-Code/synthetic-code-review/part_00054.parquet
      - Synthetic-Code/synthetic-code-review/part_00055.parquet
      - Synthetic-Code/synthetic-code-review/part_00056.parquet
      - Synthetic-Code/synthetic-code-review/part_00057.parquet
      - Synthetic-Code/synthetic-code-review/part_00058.parquet
      - Synthetic-Code/synthetic-code-review/part_00059.parquet
      - Synthetic-Code/synthetic-code-review/part_00060.parquet
      - Synthetic-Code/synthetic-code-review/part_00061.parquet
      - Synthetic-Code/synthetic-code-review/part_00062.parquet
      - Synthetic-Code/synthetic-code-review/part_00063.parquet
      split: train
  - config_name: Synthetic-Rewriting
    data_files:
    - path: Synthetic-Code/synthetic-rewriting/*.parquet
      split: train
  - config_name: Synthetic-Transpilation
    data_files:
    - path: Synthetic-Code/synthetic-transpilation/*.parquet
      split: train
track_downloads: true
---
#  Nemotron-Pre-Training-Dataset-v2.1

  

##  Dataset  Description

  

The  Nemotron-Pre-Training-Dataset-v2.1  extends  the  previously  released  Nemotron  pretraining  datasets  with  refreshed,  higher-quality,  and  more  diverse  data  across  math,  code,  English  Common  Crawl,  and  large-scale  synthetic  corpora.  Designed  for  the  [NVIDIA  Nemotron  3](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3)  family  of  LLMs,  the  dataset  introduces  new  Common  Crawl  code  extraction,  2.5T  new  English  web  tokens,  updated  GitHub-sourced  source-code  corpora,  and  specialized  STEM  reasoning  datasets.  These  additions  are  intended  to  be  used  together  with, not  as  replacements  for, existing  [**Nemotron  Pretraining  datasets**](https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets)  (see  the  [Nemotron  Nano  2  technical  report](https://arxiv.org/abs/2508.14444)),  providing  an  expanded,  modern  foundation  for  training  leading  LLMs.

  

Our  dataset  comes  in  4  main  categories:

  

-  [nvidia/Nemotron-CC-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-CC-Code-v1)

    -  427.9B-token  high-quality  Code  pretraining  dataset  obtained  from  processing  Common  Crawl  Code  pages  using  the  [Nemotron-CC-Math](https://arxiv.org/abs/2508.15096)  Lynx  +  LLM  pipeline.  Preserves  equations  and  code  often  lost  by  other  pipelines,  standardizes  math  equations  to  LaTeX,  and  removes  noise.

-  [nvidia/Nemotron-CC-v2.1](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2.1)

    -  2.5T  English  tokens  from  Common  Crawl:  organic,  translated,  and  synthetically  rephrased.  These  are  new  tokens  that  are  intended  to  be  used  in  conjunction  with  the  previously  released  6.6T  tokens  of  [Nemotron-CC-v2](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2).

-  [nvidia/Nemotron-Pretraining-Code-v2](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v2)

    -  Comprehensive  update  to  and  expansion  of  [Nemotron-Pretraining-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1).  Adds  metadata  for  377M  more  filtered  and  deduplicated  files  from  GitHub,  or  around  340B  tokens.  It  also  includes  synthetic  data  generated  with  five  different  techniques:  Question  Answering,  Code  Review,  Student  Teacher,  Rewriting,  and  Transpilation.

-  [nvidia/Nemotron-Pretraining-Specialized-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1)

    -  Collection  of  synthetic  datasets  for  specialized  areas  like  STEM  reasoning  and  scientific  coding.  It  is  an  extension  of  the  previously  released  [Nemotron-Pretraining-SFT-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-SFT-v1)  with  updated  naming  to  better  reflect  the  nature  of  the  dataset.

  

This  dataset  is  ready  for  commercial  use.

  

##  Dataset  Owner(s)

  

NVIDIA  Corporation

  

##  Dataset  Creation  Date

  

12/15/2025

  

##  License/Terms  of  Use

  

The **Nemotron-CC-Code-v1, Nemotron-CC-v2.1, Nemotron-Pretraining-Code-v2** datasets are governed by the [NVIDIA  Data  Access  Agreement  for  Model  Training](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md)

  

NVIDIA  respects  the  rights  of  all  content  creators  and  our  NVIDIA  Data  Agreement  for  Model  Training  is  written  to  be  fully  compliant  with  the  letter  and  the  spirit  of  copyright  law.  Copyright  law  protects  particular  expressions,  but  not  facts,  ideas,  data,  or  information.  Anyone  is  free  to  learn  facts,  ideas,  data,  or  information  from  another  source  and  use  it  to  make  their  own  expressions.  Fair  use  also  protects  the  ability  to  use  a  work  for  a  transformative  purpose,  such  as  model  training.  The  Agreement  is  designed  to  limit  use  to  those  uses  protected  as  fair  uses,  such  as  model  training.

  

The  NVIDIA  Data  Access  Agreement  for  Model  Training  enables  training  of  any  AI  model,  including  models  released  under  proprietary  or  open  source  licenses.  It  does  not  prohibit  disclosure  of  evaluations,  tests  or  benchmarks  of  models  trained  with  this  dataset.

  

The  **Nemotron-Pretraining-Specialized-v1**  collection  of  datasets  is  governed  by  the   [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0),  except  for  the  Nemotron-Pretraining-Wiki-Rewrite  and  Nemotron-Pretraining-Scientific-Coding  subsets,  which are governed by the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) and the [GNU Free Documentation License Version 1.3](https://www.gnu.org/licenses/fdl-1.3.en.html) (GFDL).

  

This  dataset  contains  synthetic  data  created  using  the  following  models:

  

Qwen3-30B-A3B,  Qwen3-235B-A22B-Thinking-2507,  QwQ-32B,  Qwen3-235B-A22B,  DeepSeek-R1-0528,  DeepSeek-R1,Qwen2.5-32B-Instruct,  Phi-4,  Mixtral-8x22B-Instruct-v0.1,  gpt-oss-120b.

  

If  this  dataset  is  used  to  create,  train,  fine-tune,  or  otherwise  improve  an  AI  model,  which  is  distributed  or  made  available,  such  AI  model  may  be  subject  to  redistribution  and  use  requirements  in  the  [Qwen  License  Agreement](https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE),  the  [DeepSeek  License  Agreement](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL),  and  the  [Phi-4  license  agreement](https://huggingface.co/microsoft/phi-4/blob/main/LICENSE).

  

##  Intended  Usage

  

The  Nemotron  Pre-Training  Dataset  is  intended  to  be  used  by  the  community  to  continue  to  improve  open  models.  The  data  may  be  freely  used  to  train  and  evaluate  with  user  agreement  to  open  data  license.

  

##  Dataset  Details

  

[nvidia/Nemotron-CC-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-CC-Code-v1)

This is a 427.9B-token  high-quality  Code  pretraining  dataset  obtained  from  processing  Common  Crawl  Code  pages  using  the  [Nemotron-CC-Math](https://arxiv.org/abs/2508.15096)  Lynx  +  LLM  pipeline.  It preserves  equations  and  code  often  lost  by  other  pipelines,  standardizes  math  equations  to  LaTeX,  and  removes  noise. This process had 3 main steps: 

- Lynx Rendering – Instead of relying on brittle DOM parsing, we use lynx to convert HTML into structured text while preserving code contents, math equations and layout.

- LLM Cleaning – We use a lightweight LLM (Phi-4, 14B) to remove boilerplate, standardizes mathematical expressions into consistent LaTeX, and improves formatting.

- Quality Filtering – We use "Qwen/Qwen3-30B-A3B-Instruct-2507" to assign a quality score from 1-3 to each page and we filter out pages with quality 1, where labels are defined as below: 
    - 1 – No programming content.
    - 2 – Page is about code but with limited or incomplete code snippets, concept mentions, etc 
    - 3 – Clear, complete code with context, resembling tutorials or documentation.


The  dataset  has  the  following  columns:

  

-  **text**:

    -  The  **primary  data  field**  contains  the  processed  text  extracted  from  Common  Crawl  Code  pages.

    -  This  is  the  high-quality  content  used  for  pretraining.

-  **metadata**:  A  dictionary  detailing  the  following:

    -  **warc_id**:  Unique  identifier  from  the  original  Common  Crawl  ARChive  (WARC)  file.

    -  **warc_filename**:  The  specific  WARC  file  name  where  the  content  originated.

    -  **category**:  Specifies  the  source  type  (Fixed  value:  'cc-code').

    -  **models_used**:  Identifies  the  model  utilized  during  processing  (e.g.,  'Phi-4').

-  **uuid**:  The  unique  identifier  for  this  dataset  entry.

  

The  table  below  shows  the  number  of  tokens  and  the  model  used  to  generate  this  data:

  

|  #Tokens  |  SGD  Model  |
|  ---  |  ---  |
|  427.9  |  phi-4  |


  

[nvidia/Nemotron-CC-v2.1](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2.1)

  

This  dataset  contains  2.5T  tokens  of  general  organic,  translated,  and  synthetically  rephrased  English  web  data  from  [Common  Crawl](https://commoncrawl.org).  **It  is  meant  to  be  used  in  conjunction  with  the  6.6T  tokens  of**  [**Nemotron-CC-v2**](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2)  **and  contains  only  new  data.**  Below,  we  provide  a  high-level  overview  of  the  data  slices.  For  more  details,  please  view  the  [NVIDIA  Nemotron  3  Nano  tech  report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf).

  

Description  of  subsets:

  

-  **High-Quality,  Medium-High-Quality,  Medium-Quality:**  Organic  web  crawl  data  from  three  recent  snapshots.

-  **High-Quality-Synthetic:**  Synthetic  rephrases  of  the  High-Quality  data  of  Nemotron-CC-v2.1  using  5  prompts.

-  **Medium-High-Quality-Synthetic:**  Synthetic  rephrases  of  the  Medium-High-Quality  data  of  both  Nemotron-CC-v2.1  and  Nemotron-CC-v2  using  5  prompts  (110  snapshots  total).

-  **High-Quality-Translated-To-English,  Medium-High-Quality-Translated-To-English:**  Quality  classified  &  filtered  translations  of  non-English  web  crawl  data  from  Nemotron-CC-v2  to  English  (3  snapshots).

-  **High-Quality-Translated-To-English-Synthetic:**  Synthetic  rephrases  of  the  High-Quality-Translated-To-English  subset  using  4  prompts.

-  **High-Quality-DQA:**  A  STEM  question  &  answer  dataset  built  by  prompting  on  high-quality  STEM  web  documents  from  Essential-Web  to  produce  short-form  question-answer  pairs  using  the  Nemotron-CC  diverse  QA  (DQA)  methodology.

  

|  **Subset**  |  **Tokens  (B)**  |  **CC-MAIN  Snapshots**  |  **Model**  |
|  ---  |  ---  |  ---  |  ---  |
|  High-Quality  |  26.0  |  2025-18,  2025-21,  2025-26  |  
|  Medium-High-Quality  |  16.9  |  2025-18,  2025-21,  2025-26  |  |
|  Medium-Quality  |  53.5  |  2025-18,  2025-21,  2025-26  |
|  High-Quality-Synthetic  |  93.5  |  2025-18,  2025-21,  2025-26  |  Qwen3-30B-A3B  |
|  Medium-High-Quality-Synthetic  |  2122.8  |  2013-20  -  2025-26  |  Qwen3-30B-A3B  |
|  High-Quality-Translated-To-English  |  39.6  |  2024-51,  2025-08,  2025-18  |  Qwen3-30B-A3B  |
|  Medium-High-Quality-Translated-To-English  |  26.8  |  2024-51,  2025-08,  2025-18  |  Qwen3-30B-A3B  |
|  High-Quality-Translated-To-English-Synthetic  |  157.8  |  2024-51,  2025-08,  2025-18  |  Qwen3-30B-A3B  |
|  High-Quality-DQA  |  8.0  |  2013-20  -  2024-38  |  Qwen3-30B-A3B  |
|  _Total_  |  _2544.8_  |  |  |

  

The  dataset  has  the  following  columns:

  

-  **text**: The  **primary  data  field,**  containing  the  content  to  be  used  for  pretraining.

-  **metadata**:  A  dictionary  detailing  the  following:

    -  **category**:  Data  type  (e.g.,  'High-Quality',  'Medium-High-Quality-Synthetic',  …).

    -  **quality**:  Quality  level  of  the  sample  (e.g.,  'High-Quality',  'Medium-High-Quality,  'Medium-Quality').

    -  **language**:  Language  of  the  sample  (fixed  value:  'eng').

    -  For  organic  data:

        -  **warc_id**:  Unique  identifier  from  the  original  Common  Crawl  ARChive  (WARC)  file.

    -  For  synthetic/translated  data:

        -  **models_used**:  Models  used  to  generate  synthetic  and  translated  data  (e.g.,  'Qwen3-30B-A3B').

        -  **rephrase_prompt**:  Prompt  used  for  the  synthetic  rephrasing  (see  Appendix  H  in  the  [Nemotron-CC  paper](https://arxiv.org/abs/2412.02595)).

        -  **translated_from**:  The  source  language  for  samples  that  were  translated  to  English.

-  **uuid**:  The  unique  identifier  for  this  dataset  entry.



[nvidia/Nemotron-Pretraining-Code-v2](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v2)

  

This  dataset  contains  the  metadata  corresponding  to  the  raw  source-code  update  to  our  [Nemotron-Pretraining-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1)  source-code  corpus.  It  adds  377M  files  from  GitHub  (with  a  cut-off  date  of  April  15,  2025)  that  we  found  to  be  missing  from  our  v1  corpus.  Because  it  is  an  update  to  our  v1  corpus,  the  two  corpora  are  meant  to  be  used  jointly.

  

In  addition  to  the  update  to  our  v1  corpus,  we  re-include  the  synthetic  question-answer  data  included  in  v1  (generated  using  Mixtral  8x22B)  as  well  as  new  Python  question-answer  data  generated  using  Qwen3  32B.  To  further  augment  our  synthetic  code  tokens,  we  also  prompted  Qwen3  32B  to  generate  additional  dialogue-style  data  as  well  as  rephrased  and  transpiled  source  code.  All  generations  were  grounded  in  either  full  source  files,  or  source-code  snippets  originating  from  our  v1  and  v2  raw  source-code.  Below  we  provide  an  overview  of  the  different  splits  of  our  synthetic  code  Nemotron-Pretraining-Code-v2:

  

-  **Synthetic  Question  Answering**:  The  re-inclusion  of  our  synthetic  question-answering  (QA)  data  v1,  along  with  newly  generated  QA-style  dialogue  grounded  in  a  mixture  of  Python  source-code  file  snippets.

-  **Synthetic  Code  Review:**  Code-review-style  dialogue  grounded  in  full  source  code  files  originating  from  the  Python  and  C++  subsets  of  our  v1  and  v2  raw-source  code  corpus.  As  part  of  the  code-review,  we  also  asked  Qwen3-32B  to  provide  an  improved  version  of  the  original  source-code  (based  on  the  generated  dialogue).  At  random,  we  also  will  occasionally  include  only  the  improved  source  code.

-  **Synthetic  Student  Teacher:**  Student-teacher-style  dialogue  grounded  in  Python  raw  source-code  snippets  originating  from  our  v1  source-code  corpus.

-  **Synthetic  Rewriting:**  All  Python  samples  from  our  v1  and  v2  raw  source  code,  but  rephrased.  In  prompting  Qwen3  32B  we  used  a  combination  of  the  Style-Guided  Code  Rewriting  (SGCR)  and  Self-Contained  Optimization  Rewriting  (SCOR)  prompts  described  in  [Rewriting  Pre-Training  Data  Boosts  LLM  Performance  in  Math  and  Code](https://arxiv.org/abs/2505.02881),  as  well  as  our  own  prompt  with  similar  intent.  The  prompts  used  are  provided  in  a  "prompts"  column.

-  **Synthetic  Transpilation:**  C++  source-code  transpiled  from  Python  source-code  files  originating  from  our  v1  source-code  corpus.

  

All  subsets  within  this  dataset  use  the  **content**  field  as  the  **primary  data  field.**  The  remaining  columns  serve  as  metadata  and  change  across  the  different  splits.  Here  is  a  comprehensive  list  of  all  metadata  columns  for  each  split:

  

-  Nemotron-Code-Metadata:

    -  **commit_id:**  The  first  seven  characters  of  the  Git  commit  hash

    -  **rel_path:**  The  file  path  of  the  content  relative  to  the  repository  root  directory

    -  **language:**  The  detected  programming  language  of  the  content

-  Synthetic-Code-Review/Synthetic-Question-Answering/Synthetic-Student-Teacher:

    -  **language:**  The  detected  programming  language  of  the  seed  source-file/code-snippet  in  which  the  generation  was  grounded

    -  **seed_source:**  The  source  corpus  from  which  the  source-file/code-snippet  originated

    -  **nemotron_pretraining_id:**  The  unique  identifier  for  this  dataset  entry.

-  Synthetic-Rewriting

    -  **language:**  The  detected  programming  language  of  the  source  file

    -  **prompts:**  The  type  of  prompt  used  for  rewriting  -  Style-Guided  Code  Rewriting  (SGCR),  Self-Contained  Optimization  Rewriting  (SCOR),  or  a  custom  prompt  that  designed  with  similar  intent  (NVDA)

    -  **seed_source:**  The  source  corpus  from  which  the  source-file/code-snippet  originated

    -  **nemotron_pretraining_id:**  The  unique  identifier  for  this  dataset  entry.

-  Synthetic-Transpilation:

    -  **language:**  The  programming  language  of  the  source  file  (language  to  which  the  source  file  was  transpiled)

    -  **seed_language:**  The  language  of  the  original  source  file

    -  **seed_source:**  The  source  corpus  from  which  the  source-file/code-snippet  originated

  

[nvidia/Nemotron-Pretraining-Specialized-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1)

  

This  dataset  contains  a  number  of  synthetic  datasets  that  serve  specialized  purposes  such  as  STEM  reasoning,  scientific  coding,  or  factual  knowledge.  Below  we  provide  a  high-level  overview  of  the  data  slices.  For  more  details,  please  view  the  [NVIDIA  Nemotron  3  Nano  tech  report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf)

  

Description  of  subsets:

  

-  **Synthetic  RQA:**  A  long-form  STEM  reasoning  question-answer  dataset  generated  by  sampling  contiguous  chunks  from  high-quality  topic-stratified  STEM  documents  for  question  creation,  followed  by  context-free  reasoning  +  answer  rollouts.

-  **Synthetic  InfiniByte:**  A  cross-domain  reasoning  dataset  created  by  procedurally  "cross-breeding''  code,  math,  physics,  chemistry,  and  scientific  corpora  to  generate  novel  multi-step  composite  problems  that  require  deep  cross-discipline  reasoning.

-  **Synthetic  Wikipedia  Data:**  English  Wikipedia  articles  are  revised  using  Qwen3-30B-A3B-Instruct-2507  to  enhance  clarity  and  formatting,  dropping  disambiguation/redirect  pages  and  non‑article  sections.

-  **Synthetic  Math  Textbook  Data:**  Nemotron-CC-Math  documents  are  classified  by  educational  level,  and  undergraduate  and  higher  materials  are  used  to  generate  educational  textbook-style  sections.

-  **Synthetic  Scientific  Coding  Data:**  STEM  documents  from  Nemotron‑CC  are  used  to  produce  scientific  coding  data  that  includes  graduate-  or  research-level  code-embedded  articles  and  advanced  coding  problems  with  stepwise  Python  solutions.

-  **Synthetic  STEM  SFT:**  New  and  refreshed  SFT  datasets  that  were  included  in  Nemotron  3 Nano  pretraining.

  

The  table  below  shows  the  number  of  tokens  and  the  model  used  to  generate  this  data:

  

|  Subset  |  Tokens  (B)  |  Model  |
|  ---  |  ---  |  ---  |
|  **Nemotron-Pretraining-RQA**  |  134.6  |  Qwen3-235B-A22B-Thinking-2507,  gpt-oss-120b  |
|  **Nemotron-Pretraining-InfiniByte-Reasoning**  |  19.4  |  QwQ-32B,  Qwen3-235B-A22B-Thinking-2507  |
|  **Nemotron-Pretraining-Wiki-Rewrite**  |  7.9  |  Qwen3-30B-A3B  |
|  **Nemotron-Pretraining-Scientific-Coding**  |  1.2  |  Qwen3-235B-A22B  |
|  **Nemotron-Pretraining-Math-Textbooks**  |  25.1  |  Qwen3-30B-A3B,  Qwen3-235B-A22B  |
|  **Nemotron-Pretraining-STEM-SFT**  |  82.5  |  DeepSeek-R1-0528,  Qwen2.5-32B  |
  

The  dataset  has  the  following  columns:

  

-  **text**: The  **primary  data  field,**  containing  the  content  to  be  used  for  pretraining.

-  **license**: The license(s) governing the sample (e.g., ‘cc-by-4.0’).

-  **metadata**:  A  dictionary  detailing  the  following:

    -  **category**:  Data  type  (e.g.,  'Nemotron-Pretraining-RQA',  'Nemotron-Pretraining-Scientific-Coding',  …).

    -  **models_used**:  Models  used  to  generate  the  data  (e.g.,  'Qwen3-30B-A3B').

-  **uuid**:  The  unique  identifier  for  this  dataset  entry.

  

  

###  Downloading  the  data

  

Users  can  download  subsets  of  the  data  based  on  the  metadata  schema  described  above.  Example  script  for  downloading  code  and  math  as  follows:

  
```
ds  =  load_dataset("nvidia/Nemotron-CC-Code-v1",  "train",  streaming=True)
```
  
  
  

##  Dataset  Characterization

  

**Data  Collection  Method**

  

-  Hybrid:  Automated,  Synthetic

    -  Automated:  Large-scale  Common  Crawl  processing  (English  web  data,  code  pages,  multilingual  pages),  GitHub  source-code  ingestion,  and  curated  WARC-based  extraction  using  the  Nemotron  Lynx  +  LLM  pipeline.

  

    -  Synthetic:  Extensive  synthetic  generation  using  large  language  models  (Qwen3-30B-A3B,  Qwen3-235B-A22B-Thinking-2507,  QwQ-32B,  DeepSeek-R1-0528,  DeepSeek-R1,  Phi-4,  Qwen2.5-32B-Instruct,  Mixtral-8x22B-Instruct-v0.1,  gpt-oss-120b),  including  rephrasing,  rewriting,  translation,  code  review,  question-answer  generation,  dialogue-style  data,  style-guided  code  rewriting,  and  cross-disciplinary  STEM  reasoning  synthesis.

  

**Labeling  Method**

  

-  Hybrid:  Automated,  Synthetic

    -  Automated:  Metadata  extraction  from  Common  Crawl  WARC  files,  automatic  programming  language  detection,  and  code-quality  validation  pipelines  (e.g.,  syntax  validation,  Pylint  checks,  deduplication  filters).
    -  Synthetic:  LLM-generated  annotations,  including  reasoning  labels,  improved  code  rewrites,  synthetic  explanations,  question-answer  pairs,  textbook-style  structuring,  and  prompt-based  rephrasing/transpilation.

  

##  Dataset  Format

  

Modality:  text

  

Format:  parquet

  

##  Dataset  Quantification

  

Nemotron-CC-Code-v1

  

-  Number  of  records:  216.3M
-  Downloaded  size:  563  GB

  

Nemotron-CC-v2.1

  

-  Number  of  records:  3.8B
-  Downloaded  size:  4.59  TB

  

Nemotron-Pretraining-Code-v2

  

-  Number  of  records:  835.8M
-  Downloaded  size:  897  GB

  

Nemotron-Pretraining-Specialized-v1

  

-  Number  of  records:  60.7M
-  Downloaded  size:  351  GB

  

##  Reference(s)

  

If  you  use  our  dataset  in  your  research,  please  cite  our  [NVIDIA  Nemotron  3  Nano  tech  report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf).
  
```
@misc{nvidia_nemotron_nano_v3_2025,
  title  = {{Nemotron 3 Nano}: Open, Efficient Mixture-of-Experts Hybrid {Mamba}-{Transformer} Model for {Agentic} Reasoning},
  author = {{NVIDIA}},
  year   = {2025},
  url    = {https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf},
  note   = {Technical report}
}
```
  
  

##  Ethical  Considerations

  

NVIDIA  believes  Trustworthy  AI  is  a  shared  responsibility  and  we  have  established  policies  and  practices  to  enable  development  for  a  wide  array  of  AI  applications.  When  downloaded  or  used  in  accordance  with  our  terms  of  service,  developers  should  work  with  their  internal  developer  teams  to  ensure  this  dataset  meets  requirements  for  the  relevant  industry  and  use  case  and  addresses  unforeseen  product  misuse.

  

Please  report  quality,  risk,  security  vulnerabilities  or  NVIDIA  AI  Concerns  [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).


