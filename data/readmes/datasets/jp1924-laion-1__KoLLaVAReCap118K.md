---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: data_source
    dtype: string
  - name: caption
    dtype: string
  - name: en_caption
    dtype: string
  - name: caption_ls
    list: string
  splits:
  - name: train
    num_bytes: 6580937831.875
    num_examples: 118073
  download_size: 6342422619
  dataset_size: 6580937831.875
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
tags:
- caption
---
# Dataset Card for KoLLaVAReCap118K

## Dataset Description

- **Homepage:** [lmms-lab/LLaVA-ReCap-118K](https://huggingface.co/datasets/lmms-lab/LLaVA-ReCap-118K)
- **Paper:** [LLaVA-NeXT: What Else Influences Visual Instruction Tuning Beyond Data?](https://llava-vl.github.io/blog/2024-05-25-llava-next-ablations/)

만드는데 3만원 정도 들감     

그리고 원본 데이터, `이거 저 해상도라 답변 못하겠음` 등등의 노이즈 있으니 참고하셈