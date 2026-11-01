---
language:
- ko
license: cc-by-nc-4.0
dataset_info:
  features:
  - name: index
    dtype: string
  - name: question
    dtype: string
  - name: choice_a
    dtype: string
  - name: choice_b
    dtype: string
  - name: choice_c
    dtype: string
  - name: choice_d
    dtype: string
  - name: answer
    dtype: string
  - name: category
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: test
    num_bytes: 9681522.0
    num_examples: 240
  download_size: 3340794
  dataset_size: 9681522.0
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---
# K-DTCBench

We introduce **K-DTCBench**, a newly developed Korean benchmark featuring both computer-generated and handwritten documents, tables, and charts.
It consists of 80 questions for each image type and two questions per image, summing up to 240 questions in total.
This benchmark is designed to evaluate whether vision-language models can process images in different formats and be applicable for diverse domains.
All images are generated with made-up values and statements for evaluation purposes only. We scanned hand-written documents/tables/charts, or created digital objects with matplotlib library to build K-DTCBench.
The proportions of digital and hand-written images are equal, each constituting 50%.


For more details, Please refer to the VARCO-VISION technical report.

- **Technical Report:** [VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models](https://arxiv.org/pdf/2411.19103)
- **Blog(Korean):** [VARCO-VISION Technical Report Summary](https://ncsoft.github.io/ncresearch/95ad8712e60063e9ac97538504ac3eea0ac530af)
- **Huggingface Version Model:** [NCSOFT/VARCO-VISION-14B-HF](https://huggingface.co/NCSOFT/VARCO-VISION-14B-HF)
- **Evaluation Repository:** [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<table>
<tr>
  <th>Category</th>
  <th>Image</th>
  <th>K-DTCBench</th>
</tr>
<tr>
  <td align="center">document</td>
  <td width=350><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/Ipi4HR73P-PDC5XcgP3WF.png"></td>
  <td>
    <strong>question:</strong> 보고서의 주요 내용이 아닌 것은 무엇인가요?
    <br>
    <strong>A:</strong> 안전 인프라 확충
    <br>
    <strong>B:</strong> 재난 및 사고 예방 체계 구축
    <br>
    <strong>C:</strong> 시민 안전 교육 강화
    <br>
    <strong>D:</strong> 긴급 대응 시스템 개선
  </td>
</tr>
<tr>
  <td align="center">table</td>
  <td width=350><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/dz_FuPnpZ5P4P3LEB5PZ0.png"></td>
  <td>
    <strong>question:</strong> 인프라 구축 항목의 점수는 몇 점인가요?
    <br>
    <strong>A:</strong> 4
    <br>
    <strong>B:</strong> 6
    <br>
    <strong>C:</strong> 8
    <br>
    <strong>D:</strong> 10
  </td>
</tr>
<tr>
  <td align="center">chart</td>
  <td width=350><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/IbNMPPgd974SbCAsz6zIS.png"></td>
  <td>
    <strong>question:</strong> 직장인들이 퇴근 후 두 번째로 선호하는 활동은 무엇인가요?
    <br>
    <strong>A:</strong> 운동
    <br>
    <strong>B:</strong> 여가활동
    <br>
    <strong>C:</strong> 자기개발
    <br>
    <strong>D:</strong> 휴식
  </td>
</tr>
</table>
<br>

## Inference Prompt
```
<image>
{question}
Options: A: {A}, B: {B}, C: {C}, D: {D}

주어진 선택지 중 해당 옵션의 문자로 바로 답하세요.
```

<br>

## Results
Below are the evaluation results of various vision-language models, including [VARCO-VISION-14B](https://huggingface.co/NCSOFT/VARCO-VISION-14B) on K-DTCBench.

| | VARCO-VISION-14B | Pangea-7B | Pixtral-12B | Molmo-7B-D | Qwen2-VL-7B-Instruct | LLaVA-One-Vision-7B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| K-DTCBench | **84.58** | 48.33 | 27.50 | 45.83 | 75.00 | 52.91 |

<br>

## Citation
If you use K-DTCBench in your research, please cite the following:
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