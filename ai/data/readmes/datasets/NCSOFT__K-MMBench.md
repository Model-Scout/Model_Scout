---
language:
- ko
license: cc-by-nc-4.0
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: question
    dtype: string
  - name: hint
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: answer
    dtype: string
  - name: category
    dtype: string
  - name: image
    dtype: image
  - name: source
    dtype: string
  - name: l2-category
    dtype: string
  - name: comment
    dtype: string
  - name: split
    dtype: string
  splits:
  - name: dev
    num_bytes: 103023727.794
    num_examples: 4329
  download_size: 96835472
  dataset_size: 103023727.794
configs:
- config_name: default
  data_files:
  - split: dev
    path: data/dev-*
---

# K-MMBench

We introduce **K-MMBench**, a Korean adaptation of the [MMBench](https://arxiv.org/abs/2307.06281) [1] designed for evaluating vision-language models.
By translating the ```dev``` subset of MMBench into Korean and carefully reviewing its naturalness through human inspection, we developed a novel robust evaluation benchmark specifically for Korean language.
K-MMBench consists of questions across 20 evaluation dimensions, such as identity reasoning, image emotion, and attribute recognition, allowing a thorough evaluation of model performance in Korean.
To ensure a fair evaluation, we adopt the ***CircularEval Strategy*** as proposed by the MMBench benchmark [1]. For detailed information, please refer to Section 4.3 of the corresponding [paper](https://arxiv.org/abs/2307.06281).


For more details, Please refer to the VARCO-VISION technical report.

- **Technical Report:** [VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models](https://arxiv.org/pdf/2411.19103)
- **Blog(Korean):** [VARCO-VISION Technical Report Summary](https://ncsoft.github.io/ncresearch/95ad8712e60063e9ac97538504ac3eea0ac530af)
- **Huggingface Version Model:** [NCSOFT/VARCO-VISION-14B-HF](https://huggingface.co/NCSOFT/VARCO-VISION-14B-HF)
- **Evaluation Repository:** [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<table>
<tr>
  <th>Image</th>
  <th>MMBench</th>
  <th>K-MMBench</th>
</tr>
<tr>
  <td width=200><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/lWr_73pFC5dKbFI0xzGgB.jpeg"></td>
  <td>
    <strong>hint:</strong> The passage below describes an experiment. Read the passage and then follow the instructions below. Madelyn applied a thin layer of wax to the underside of her snowboard and rode the board straight down a hill. Then, she removed the wax and rode the snowboard straight down the hill again. She repeated the rides four more times, alternating whether she rode with a thin layer of wax on the board or not. Her friend Tucker timed each ride. Madelyn and Tucker calculated the average time it took to slide straight down the hill on the snowboard with wax compared to the average time on the snowboard without wax. Figure: snowboarding down a hill.
    <br>
    <strong>question:</strong> Identify the question that Madelyn and Tucker's experiment can best answer.
    <br>
    <strong>A:</strong> Does Madelyn's snowboard slide down a hill in less time when it has a thin layer of wax or a thick layer of wax?
    <br>
    <strong>B:</strong> Does Madelyn's snowboard slide down a hill in less time when it has a layer of wax or when it does not have a layer of wax?
  </td>
  <td>
    <strong>hint:</strong> 아래의 문단은 한 실험을 설명하고 있습니다. 문단을 읽고 아래의 지시사항을 따르세요. 매들린은 스노보드의 아랫면에 얇은 왁스층을 바르고 언덕을 직선으로 내려갔습니다. 그런 다음, 그녀는 왁스를 제거하고 다시 스노보드를 언덕을 직선으로 내려갔습니다. 그녀는 스노보드에 얇은 왁스층을 바르고 타는지 아닌지를 번갈아 가며 네 번 더 탔습니다. 그녀의 친구 터커는 각각의 타기를 시간을 재었습니다. 매들린과 터커는 왁스를 바른 스노보드로 언덕을 직선으로 내려가는데 걸리는 평균 시간을 왁스를 바르지 않은 스노보드로 언덕을 내려가는데 걸리는 평균 시간과 비교하여 계산하였습니다. 그림: 언덕을 내려가는 스노보딩.
    <br>
    <strong>question:</strong> 매들린과 터커의 실험이 가장 잘 대답할 수 있는 질문을 확인하세요.
    <br>
    <strong>A:</strong> 매들린의 스노보드는 얇은 왁스층이 있는 경우와 두꺼운 왁스층이 있는 경우 중 어느 경우에 언덕을 더 빨리 내려갈까요?
    <br>
    <strong>B:</strong> 매들린의 스노보드는 왁스층이 있는 경우와 없는 경우 중 어느 경우에 언덕을 더 빨리 내려갈까요?
  </td>
</tr>
</table>

<br>

## Inference Prompt

- As mentioned earlier, we adopt the ***CircularEval Strategy*** as proposed by the MMBench benchmark [1]. For detailed information, please refer to Section 4.3 of the corresponding [paper](https://arxiv.org/abs/2307.06281).

```
<image>
힌트: {hint} [optional]
질문: {question}
Options:
A. {A}
B. {B}
C. {C} [optional]
D. {D} [optional]

주어진 선택지 중 해당 옵션의 문자로 바로 답하세요.
```

<br>

## Results
Below are the evaluation results of various vision-language models, including [VARCO-VISION-14B](https://huggingface.co/NCSOFT/VARCO-VISION-14B) on K-MMBench.

| | VARCO-VISION-14B | Pangea-7B | Pixtral-12B | Molmo-7B-D | Qwen2-VL-7B-Instruct | LLaVA-One-Vision-7B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| K-MMBench | **82.21** | 71.64 | 57.47 | 63.83 | 78.26 | 76.28 |

<br>

## References
[1] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, et al. Mmbench: Is your multi-modal model an all-around player? In European Conference on Computer Vision, pages 216–233. Springer, 2025.

<br>

## Citation
If you use K-MMBench in your research, please cite the following:

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
