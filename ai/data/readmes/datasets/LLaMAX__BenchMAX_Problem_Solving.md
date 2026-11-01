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
- 10K<n<100K
configs:
- config_name: en
  data_files: en/*.parquet
- config_name: zh
  data_files: zh/*.parquet
- config_name: es
  data_files: es/*.parquet
- config_name: fr
  data_files: fr/*.parquet
- config_name: de
  data_files: de/*.parquet
- config_name: ru
  data_files: ru/*.parquet
- config_name: ja
  data_files: ja/*.parquet
- config_name: th
  data_files: th/*.parquet
- config_name: bn
  data_files: bn/*.parquet
- config_name: sw
  data_files: sw/*.parquet
- config_name: te
  data_files: te/*.parquet
- config_name: ar
  data_files: ar/*.parquet
- config_name: ko
  data_files: ko/*.parquet
- config_name: vi
  data_files: vi/*.parquet
- config_name: cs
  data_files: cs/*.parquet
- config_name: hu
  data_files: hu/*.parquet
- config_name: sr
  data_files: sr/*.parquet
---
## Dataset Sources

- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Problem_Solving is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [LiveCodeBench_v4](https://huggingface.co/datasets/livecodebench/code_generation_lite), which evaluates the code generation capability for solving multilingual competitive code problems.

We extend the original English dataset by 16 non-English languages.
The data is first translated by GPT-4o, and then post-editing by native speakers.

## Usage

```bash
git clone --recurse-submodules https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/LiveCodeBench
languages=(en ar bn cs de es fr hu ja ko ru sr sw te th vi zh)
for lang in "${languages[@]}"; do
    python -m lcb_runner.runner.main --model ${model_name} --local_model_path ${model_path} --release_version release_v4 --dataset $lang --evaluate --num_process_evaluate 16
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