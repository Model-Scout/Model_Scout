---
license: cc-by-4.0
task_categories:
- question-answering
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
  data_files: gpqa_en.jsonl
- config_name: zh
  data_files: gpqa_zh.jsonl
- config_name: es
  data_files: gpqa_es.jsonl
- config_name: fr
  data_files: gpqa_fr.jsonl
- config_name: de
  data_files: gpqa_de.jsonl
- config_name: ru
  data_files: gpqa_ru.jsonl
- config_name: ja
  data_files: gpqa_ja.jsonl
- config_name: th
  data_files: gpqa_th.jsonl
- config_name: bn
  data_files: gpqa_bn.jsonl
- config_name: sw
  data_files: gpqa_sw.jsonl
- config_name: te
  data_files: gpqa_te.jsonl
- config_name: ar
  data_files: gpqa_ar.jsonl
- config_name: ko
  data_files: gpqa_ko.jsonl
- config_name: vi
  data_files: gpqa_vi.jsonl
- config_name: cs
  data_files: gpqa_cs.jsonl
- config_name: hu
  data_files: gpqa_hu.jsonl
- config_name: sr
  data_files: gpqa_sr.jsonl
---
## Dataset Sources
- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Science is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [GPQA](https://huggingface.co/datasets/Idavidrein/gpqa), which evaluates the natural science reasoning capability in multilingual scenarios.

We extend the original English dataset to 16 non-English languages.
The data is first translated by Google Translate, and then post-editing by native speakers.

## Usage

```bash
git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
pip install -e lm-evaluation-harness

git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

lm-eval -m vllm --model_args pretrained=${model} --tasks xgpqa_main_native_cot_zeroshot_multi --batch_size auto --apply_chat_template --include_path tasks/gpqa --log_samples -o results
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
