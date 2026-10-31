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
  data_files: ifeval_en.jsonl
- config_name: zh
  data_files: ifeval_zh.jsonl
- config_name: es
  data_files: ifeval_es.jsonl
- config_name: fr
  data_files: ifeval_fr.jsonl
- config_name: de
  data_files: ifeval_de.jsonl
- config_name: ru
  data_files: ifeval_ru.jsonl
- config_name: ja
  data_files: ifeval_ja.jsonl
- config_name: th
  data_files: ifeval_th.jsonl
- config_name: bn
  data_files: ifeval_bn.jsonl
- config_name: sw
  data_files: ifeval_sw.jsonl
- config_name: te
  data_files: ifeval_te.jsonl
- config_name: ar
  data_files: ifeval_ar.jsonl
- config_name: ko
  data_files: ifeval_ko.jsonl
- config_name: vi
  data_files: ifeval_vi.jsonl
- config_name: cs
  data_files: ifeval_cs.jsonl
- config_name: hu
  data_files: ifeval_hu.jsonl
- config_name: sr
  data_files: ifeval_sr.jsonl
---
## Dataset Sources

- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Rule-based is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [IFEval](https://huggingface.co/datasets/google/IFEval), which is a rule-based benchmark for evaluating the instruction following capabilities in multilingual scenarios.

We extend the original dataset to 16 non-English languages by first translating and then manual post-editing.
All English-specific samples are filtered out, remaining 429 samples.
In addition, the number-word constraints for non-English languages are multiplied by a ratio in order to make the difficulty of the same instruction in different languages comparable.

## Usage

```bash
git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
pip install -e lm-evaluation-harness

git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

# Evaluate on all 17 languages
lm-eval -m vllm --model_args pretrained=${model} --tasks xifeval_multi --batch_size auto --apply_chat_template --include_path tasks/ifeval --log_samples -o results

# Evaluate on one specific language
lm-eval -m vllm --model_args pretrained=${model} --tasks xifeval_zh --batch_size auto --apply_chat_template --include_path tasks/ifeval --log_samples -o results
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