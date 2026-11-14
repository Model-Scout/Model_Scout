---
base_model:
- Qwen/Qwen2.5-3B
library_name: transformers
tags:
- mergekit
- merge
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [Qwen/Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 6]
    model: Qwen/Qwen2.5-3B
- sources:
  - layer_range: [4, 12]
    model: Qwen/Qwen2.5-3B
- sources:
  - layer_range: [10, 18]
    model: Qwen/Qwen2.5-3B
- sources:
  - layer_range: [16, 24]
    model: Qwen/Qwen2.5-3B
- sources:
  - layer_range: [22, 30]
    model: Qwen/Qwen2.5-3B
- sources:
  - layer_range: [28, 36]
    model: Qwen/Qwen2.5-3B
merge_method: passthrough
dtype: bfloat16
```
