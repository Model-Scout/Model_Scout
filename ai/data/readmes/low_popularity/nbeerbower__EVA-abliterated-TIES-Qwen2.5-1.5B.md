---
base_model:
- huihui-ai/Qwen2.5-1.5B-Instruct-abliterated
- Qwen/Qwen2.5-1.5B
- EVA-UNIT-01/EVA-Qwen2.5-1.5B-v0.0
library_name: transformers
tags:
- mergekit
- merge
license: apache-2.0
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
# EVA-abliterated-TIES-Qwen2.5-1.5B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B) as a base.

### Models Merged

The following models were included in the merge:
* [huihui-ai/Qwen2.5-1.5B-Instruct-abliterated](https://huggingface.co/huihui-ai/Qwen2.5-1.5B-Instruct-abliterated)
* [EVA-UNIT-01/EVA-Qwen2.5-1.5B-v0.0](https://huggingface.co/EVA-UNIT-01/EVA-Qwen2.5-1.5B-v0.0)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: huihui-ai/Qwen2.5-1.5B-Instruct-abliterated
    parameters:
      weight: 1
      density: 1
  - model: EVA-UNIT-01/EVA-Qwen2.5-1.5B-v0.0
    parameters:
      weight: 1
      density: 1
merge_method: ties
base_model: Qwen/Qwen2.5-1.5B
parameters:
  weight: 1
  density: 1
  normalize: true
  int8_mask: true
dtype: bfloat16


```