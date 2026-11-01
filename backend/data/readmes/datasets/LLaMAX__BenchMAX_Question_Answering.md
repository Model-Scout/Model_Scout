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
---
## Dataset Sources
- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Question_Answering is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346) for evaluating the long-context capability of LLMs in multilingual scenarios.
The subtasks are similar to the subtasks in [RULER](https://github.com/NVIDIA/RULER).
The data is sourcing from [UN Parallel Corpus](https://www.un.org/dgacm/en/content/uncorpus/Download) and [xquad](https://huggingface.co/datasets/google/xquad).

The haystacks are from UN Parallel Corpus Test and Development Sets and we translate them to other languages by Google Translate.
The multilingual QA data is from xquad and we translate samples to other languages by Google Translate.

## Usage
```bash
git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/RULER/scripts
cd data/synthetic/json
bash download_haystack.sh
bash download_qa_dataset.sh
```

Then, configure your model information in `config_models.sh` and `run.sh`, referring to [RULER's guide](https://github.com/NVIDIA/RULER#3-run-evaluation-pipeline).
You can change the context length in `config_models.sh`.

Finally, run the evaluation pipeline.

```bash
cd BenchMAX/tasks/RULER/scripts

languages=(en ar bn cs de es fr hu ja ko ru sr sw te th vi zh)
for lang in "${languages[@]}"; do
    bash run.sh ${model} synthetic $lang
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
