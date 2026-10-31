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
dataset_info:
- config_name: en
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: zh
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: es
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: fr
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: de
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: ru
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: ja
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: bn
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: th
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: sw
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: te
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: ar
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: ko
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: vi
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: cs
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: hu
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
- config_name: sr
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: answer_number
    dtype: int32
  - name: equation_solution
    dtype: string
configs:
- config_name: en
  data_dir: en
- config_name: zh
  data_dir: zh
- config_name: es
  data_dir: es
- config_name: fr
  data_dir: fr
- config_name: de
  data_dir: de
- config_name: ru
  data_dir: ru
- config_name: ja
  data_dir: ja
- config_name: th
  data_dir: th
- config_name: bn
  data_dir: bn
- config_name: sw
  data_dir: sw
- config_name: te
  data_dir: te
- config_name: ar
  data_dir: ar
- config_name: ko
  data_dir: ko
- config_name: vi
  data_dir: vi
- config_name: cs
  data_dir: cs
- config_name: hu
  data_dir: hu
- config_name: sr
  data_dir: sr
---
## Dataset Sources
- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Math is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [MGSM](https://huggingface.co/datasets/juletxara/mgsm), which evaluates the math reasoning capability in multilingual scenarios.

We extend the original MGSM dataset by six additional languages, i.e. Arabic, Czech, Hungarian, Korean, Serbian, and Vietnamese.
The data is first translated by Google Translate, and then post-editing by native speakers.

## Usage

```bash
git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
pip install -e lm-evaluation-harness

git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

lm-eval -m vllm --model_args pretrained=${model} --tasks xmgsm_native_cot_multi --batch_size auto --apply_chat_template --include_path tasks/mgsm --log_samples -o results
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