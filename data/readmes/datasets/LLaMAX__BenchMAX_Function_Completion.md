---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
- zh
- es
- fr
- de
- ru
- ja
- th
- sw
- te
- bn
- ar
- ko
- vi
- cs
- hu
- sr
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
configs:
- config_name: en
  data_files: humaneval_en.jsonl
- config_name: zh
  data_files: humaneval_zh.jsonl
- config_name: es
  data_files: humaneval_es.jsonl
- config_name: fr
  data_files: humaneval_fr.jsonl
- config_name: de
  data_files: humaneval_de.jsonl
- config_name: ru
  data_files: humaneval_ru.jsonl
- config_name: ja
  data_files: humaneval_ja.jsonl
- config_name: th
  data_files: humaneval_th.jsonl
- config_name: bn
  data_files: humaneval_bn.jsonl
- config_name: sw
  data_files: humaneval_sw.jsonl
- config_name: te
  data_files: humaneval_te.jsonl
- config_name: ar
  data_files: humaneval_ar.jsonl
- config_name: ko
  data_files: humaneval_ko.jsonl
- config_name: vi
  data_files: humaneval_vi.jsonl
- config_name: cs
  data_files: humaneval_cs.jsonl
- config_name: hu
  data_files: humaneval_hu.jsonl
- config_name: sr
  data_files: humaneval_sr.jsonl
tags:
- multilingual
- code-generation
---
## Dataset Sources

- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Function_Completion is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [humanevalplus](https://huggingface.co/datasets/evalplus/humanevalplus), which evaluates the code generation capability in multilingual scenarios.

We extend the original English dataset to 16 non-English languages.
The data is first translated by GPT-4o, and then post-editing by native speakers.

## Usage

```bash
git clone --recurse-submodules https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/evalplus
languages=(en ar bn cs de es fr hu ja ko ru sr sw te th vi zh)
for lang in "${languages[@]}"; do
    python -m evalplus.evaluate --model ${model} --dataset humaneval --backend vllm --greedy --lang ${lang}
done
```

## Supported Languages
Arabic, Bengali, Chinese, Czech, English, French, German, Hungarian, Japanese, Korean, Serbian, Spanish, Swahili, Telugu, Thai, Russian, Vietnamese

## Citation
If you find our dataset helpful, please cite this paper:

```
@article{huang2025benchmax,
  title={BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models},
  author={Huang, Xu and Zhu, Wenhao and Hu, Hanxu and He, Conghui and Li, Lei and Huang, Shujian and Yuan, Fei},
  journal={arXiv preprint arXiv:2502.07346},
  year={2025}
}
```
