---
license: cc-by-nc-4.0
language:
- en
- ko
---

---
## Developed by : 
* K2S3

## Model Number:
* K2S3-Mistral-7bx2-48layers_v1.2

## Merge Method
dtype: bfloat16
merge_method: passthrough
slices:
- sources:
  - layer_range: [0, 24]
    model:
      model:
        path: Changgil/K2S3-Mistral-7b-v1.2
- sources:
  - layer_range: [8, 32]
    model:
      model:
        path: Changgil/K2S3-Mistral-7b-v1.2

