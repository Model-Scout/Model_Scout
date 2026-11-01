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
  data_files: arenahard_en.jsonl
- config_name: zh
  data_files: arenahard_zh.jsonl
- config_name: es
  data_files: arenahard_es.jsonl
- config_name: fr
  data_files: arenahard_fr.jsonl
- config_name: de
  data_files: arenahard_de.jsonl
- config_name: ru
  data_files: arenahard_ru.jsonl
- config_name: ja
  data_files: arenahard_ja.jsonl
- config_name: th
  data_files: arenahard_th.jsonl
- config_name: bn
  data_files: arenahard_bn.jsonl
- config_name: sw
  data_files: arenahard_sw.jsonl
- config_name: te
  data_files: arenahard_te.jsonl
- config_name: ar
  data_files: arenahard_ar.jsonl
- config_name: ko
  data_files: arenahard_ko.jsonl
- config_name: vi
  data_files: arenahard_vi.jsonl
- config_name: cs
  data_files: arenahard_cs.jsonl
- config_name: hu
  data_files: arenahard_hu.jsonl
- config_name: sr
  data_files: arenahard_sr.jsonl
tags:
- multilingual
- instruction-following
---
## Dataset Sources

- **Paper**: BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models
- **Link**: https://huggingface.co/papers/2502.07346
- **Repository**: https://github.com/CONE-MT/BenchMAX

## Dataset Description
BenchMAX_Model-based is a dataset of [BenchMAX](https://arxiv.org/pdf/2502.07346), sourcing from [m-ArenaHard](https://huggingface.co/datasets/CohereForAI/m-ArenaHard), which evaluates the instruction following capability via model-based judgment.

We extend the original dataset to include languages that are not supported by m-ArenaHard through Google Translate.
Then manual post-editing is applied for all non-English languages.

## Usage

```bash
git clone https://github.com/CONE-MT/BenchMAX.git
cd BenchMAX
pip install -r requirements.txt

cd tasks/arenahard
bash prepare.sh
```

Then modify the model configs in `arena-hard-auto/config`.
Please add your model config to `api_config.yaml` and add your model name to the model list in other configs like `gen_answer_config_*.yaml`.
If you want to change the judge model, you can modify `judge_config_*.yaml`.

Finally, deploy your model and run the evaluation, where your model first generates responses to prompts and DeepSeek-V3 judge them against GPT-4o responses, as we do in the paper.

```bash
# serve your model by vllm
vllm serve meta-llama/Llama-3.1-8B-Instruct

# generate responses
cd arena-hard-auto
languages=(en ar bn cs de es fr hu ja ko ru sr sw te th vi zh)
for lang in "${languages[@]}"; do
    python gen_answer.py --setting-file config/gen_answer_config_${lang}.yaml
done

# run LLM-as-a-judge
export OPENAI_API_KEY=...
for lang in "${languages[@]}"; do
    python gen_judgment.py --setting-file config/judge_config_${lang}.yaml
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