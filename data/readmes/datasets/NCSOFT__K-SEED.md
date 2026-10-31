---
language:
- ko
license: cc-by-nc-4.0
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: answer
    dtype: string
  - name: choice_a
    dtype: string
  - name: choice_b
    dtype: string
  - name: choice_c
    dtype: string
  - name: choice_d
    dtype: string
  - name: data_id
    dtype: string
  - name: data_type
    dtype: string
  - name: question
    dtype: string
  - name: question_id
    dtype: int64
  - name: question_type_id
    dtype: int64
  - name: image
    dtype: image
  - name: segment
    dtype: string
  splits:
  - name: test
    num_bytes: 513264892.538
    num_examples: 2971
  download_size: 505959829
  dataset_size: 513264892.538
---

# K-SEED

We introduce **K-SEED**, a Korean adaptation of the [SEED-Bench](https://arxiv.org/abs/2307.16125) [1] designed for evaluating vision-language models.
By translating the first 20 percent of the ```test``` subset of SEED-Bench into Korean, and carefully reviewing its naturalness through human inspection, we developed a novel robust evaluation benchmark specifically for Korean language.
K-SEED consists of questions across 12 evaluation dimensions, such as scene understanding, instance identity, and instance attribute, allowing a thorough evaluation of model performance in Korean.


For more details, Please refer to the VARCO-VISION technical report.

- **Technical Report:** [VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models](https://arxiv.org/pdf/2411.19103)
- **Blog(Korean):** [VARCO-VISION Technical Report Summary](https://ncsoft.github.io/ncresearch/95ad8712e60063e9ac97538504ac3eea0ac530af)
- **Huggingface Version Model:** [NCSOFT/VARCO-VISION-14B-HF](https://huggingface.co/NCSOFT/VARCO-VISION-14B-HF)
- **Evaluation Repository:** [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<table>
<tr>
  <th>Image</th>
  <th>SEED-Bench</th>
  <th>K-SEED</th>
</tr>
<tr>
  <td width=200><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/1ijfEkTCI7mPQo2OfCQCc.jpeg"></td>
  <td>
    <strong>question:</strong> How many towels are in the image?
    <br>
    <strong>choice_a:</strong> One
    <br>
    <strong>choice_b:</strong> Two
    <br>
    <strong>choice_c:</strong> Three
    <br>
    <strong>choice_d:</strong> Four
  </td>
  <td>
    <strong>question:</strong> 이미지에 수건이 몇 개 있나요?
    <br>
    <strong>choice_a:</strong> 한 개
    <br>
    <strong>choice_b:</strong> 두 개
    <br>
    <strong>choice_c:</strong> 세 개
    <br>
    <strong>choice_d:</strong> 네 개
  </td>
</tr>
</table>

<br>

## Inference Prompt
```
<image>
{question}
A. {choice_a}
B. {choice_b}
C. {choice_c}
D. {choice_d}

주어진 선택지 중 해당 옵션의 문자로 바로 답하세요.
```

<br>

## Results
Below are the evaluation results of various vision-language models, including [VARCO-VISION-14B](https://huggingface.co/NCSOFT/VARCO-VISION-14B) on K-SEED.

| | VARCO-VISION-14B | Pangea-7B | Pixtral-12B | Molmo-7B-D | Qwen2-VL-7B-Instruct | LLaVA-One-Vision-7B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| K-SEED | **75.39** | 73.34 | 46.44 | 69.53 | 74.08 | 73.21 |

<br>

## References
[1] Bohao Li, Yuying Ge, Yixiao Ge, Guangzhi Wang, Rui Wang, Ruimao Zhang, and Ying Shan. Seed-bench: Benchmarking multimodal large language models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 13299–13308, 2024.

<br>

## Citation
If you use K-SEED in your research, please cite the following:

```bibtex
@misc{ju2024varcovisionexpandingfrontierskorean,
      title={VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models}, 
      author={Jeongho Ju and Daeyoung Kim and SunYoung Park and Youngjune Kim},
      year={2024},
      eprint={2411.19103},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2411.19103}, 
}

```
