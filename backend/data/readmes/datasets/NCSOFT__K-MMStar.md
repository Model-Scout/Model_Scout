---
language:
- ko
license: cc-by-nc-4.0
configs:
- config_name: default
  data_files:
  - split: val
    path: data/val-*
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: question
    dtype: string
  - name: image
    dtype: image
  - name: answer
    dtype: string
  - name: category
    dtype: string
  - name: l2_category
    dtype: string
  - name: meta_info
    dtype: string
  splits:
  - name: val
    num_bytes: 45120282.5
    num_examples: 1500
  download_size: 41901043
  dataset_size: 45120282.5
---

# K-MMStar

We introduce **K-MMStar**, a Korean adaptation of the [MMStar](https://arxiv.org/abs/2403.20330) [1] designed for evaluating vision-language models.
By translating the ```val``` subset of MMStar into Korean and carefully reviewing its naturalness through human inspection, we developed a novel robust evaluation benchmark specifically for Korean language.
(We observe that there are unanswerable cases *(e.g., multiple images required to answer the question but only has a single image, vague questions or options)* in the original MMStar dataset. Thus, we modify or re-create the questions to ensure they can be answered within a single image.)
K-MMStar consists of questions across 6 evaluation dimensions, such as coarse perception, fine-grained perception, and instance reasoning, allowing a thorough evaluation of model performance in Korean.


For more details, Please refer to the VARCO-VISION technical report.

- **Technical Report:** [VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models](https://arxiv.org/pdf/2411.19103)
- **Blog(Korean):** [VARCO-VISION Technical Report Summary](https://ncsoft.github.io/ncresearch/95ad8712e60063e9ac97538504ac3eea0ac530af)
- **Huggingface Version Model:** [NCSOFT/VARCO-VISION-14B-HF](https://huggingface.co/NCSOFT/VARCO-VISION-14B-HF)
- **Evaluation Repository:** [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<table>
<tr>
  <th>Image</th>
  <th>MMStar</th>
  <th>K-MMStar</th>
</tr>
<tr>
  <td width=200><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/4N3YLHmLMlxXvdRFssxPz.jpeg"></td>
  <td>
    <strong>question:</strong> Which option describe the object relationship in the image correctly? Options: A: The suitcase is on the book., B: The suitcase is beneath the cat., C: The suitcase is beneath the bed., D: The suitcase is beneath the book.
  </td>
  <td>
    <strong>question:</strong> 이미지에서 물체들의 관계를 올바르게 설명하는 옵션은 무엇인가요? Options: A: 가방이 책 위에 있다., B: 가방이 고양이 아래에 있다., C: 가방이 침대 아래에 있다., D: 가방이 책 아래에 있다.
  </td>
</tr>
</table>

<br>

## Inference Prompt
```
{question}
```

<br>

## Results
Below are the evaluation results of various vision-language models, including [VARCO-VISION-14B](https://huggingface.co/NCSOFT/VARCO-VISION-14B) on K-MMStar.

| | VARCO-VISION-14B | Pangea-7B | Pixtral-12B | Molmo-7B-D | Qwen2-VL-7B-Instruct | LLaVA-One-Vision-7B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| K-MMStar | **57.33** | 35.00 | 23.93 | 47.40 | 50.67 | 54.00 |

<br>

## References
[1] Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen, Haodong Duan, Jiaqi Wang, Yu Qiao, Dahua Lin, and Feng Zhao. Are we on the right way for evaluating large vision-language models? In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024. URL https://openreview.net/forum?id=evP9mxNNxJ.

<br>

## Citation
If you use K-MMStar in your research, please cite the following:

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