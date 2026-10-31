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
  data_files: nexus_en.jsonl
- config_name: zh
  data_files: nexus_zh.jsonl
- config_name: es
  data_files: nexus_es.jsonl
- config_name: fr
  data_files: nexus_fr.jsonl
- config_name: de
  data_files: nexus_de.jsonl
- config_name: ru
  data_files: nexus_ru.jsonl
- config_name: ja
  data_files: nexus_ja.jsonl
- config_name: th
  data_files: nexus_th.jsonl
- config_name: bn
  data_files: nexus_bn.jsonl
- config_name: sw
  data_files: nexus_sw.jsonl
- config_name: te
  data_files: nexus_te.jsonl
- config_name: ar
  data_files: nexus_ar.jsonl
- config_name: ko
  data_files: nexus_ko.jsonl
- config_name: vi
  data_files: nexus_vi.jsonl
- config_name: cs
  data_files: nexus_cs.jsonl
- config_name: hu
  data_files: nexus_hu.jsonl
- config_name: sr
  data_files: nexus_sr.jsonl
---
## Dataset Sources
- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Multiple_Functions is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [Nexus](https://huggingface.co/datasets/Nexusflow/NexusRaven_API_evaluation).
This dataset evaluates the tool use capability in multilingual senarios, which requires a model to call the correct function given the user query and multiple functions.

We translate the standardized queries from English to 16 non-English languages by google Translate.
Some special function arguments remain English since the APIs are in English.
All samples are post-edited by native speakers.

## Usage

```bash
git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/nexus
languages=(en ar bn cs de es fr hu ja ko ru sr sw te th vi zh)
for lang in "${languages[@]}"; do
    python evaluator.py -m ${model} --infer-backend vllm -t ${lang} --output-parser-name generic
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