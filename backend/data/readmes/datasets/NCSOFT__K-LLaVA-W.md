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
  - name: question_id
    dtype: int64
  - name: question
    dtype: string
  - name: image
    dtype: image
  - name: caption
    dtype: string
  - name: gpt_answer
    dtype: string
  - name: category
    dtype: string
  - name: image_id
    dtype: string
  splits:
  - name: test
    num_bytes: 20104501.0
    num_examples: 60
  download_size: 8345267
  dataset_size: 20104501.0
---
# K-LLaVA-W

We introduce **K-LLaVA-W**, a Korean adaptation of the [LLaVA-Bench-in-the-wild](https://arxiv.org/abs/2304.08485) [1] designed for evaluating vision-language models.
By translating the LLaVA-Bench-in-the-wild into Korean and carefully reviewing its naturalness through human inspection, we developed a novel robust evaluation benchmark specifically for Korean language.
(Since our goal was to build a benchmark exclusively focused in Korean, we change the English texts in images into Korean for localization.)
K-LLaVA-W contains 24 images of various domains and 60 daily-life questions, allowing a thorough evaluation of model performance in Korean.


For more details, Please refer to the VARCO-VISION technical report.

- **Technical Report:** [VARCO-VISION: Expanding Frontiers in Korean Vision-Language Models](https://arxiv.org/pdf/2411.19103)
- **Blog(Korean):** [VARCO-VISION Technical Report Summary](https://ncsoft.github.io/ncresearch/95ad8712e60063e9ac97538504ac3eea0ac530af)
- **Huggingface Version Model:** [NCSOFT/VARCO-VISION-14B-HF](https://huggingface.co/NCSOFT/VARCO-VISION-14B-HF)
- **Evaluation Repository:** [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<table>
<tr>
  <th>Image</th>
  <th>LLaVA-Bench-in-the-wild</th>
  <th>K-LLaVA-W</th>
</tr>
<tr>
  <td width=200><img src="https://cdn-uploads.huggingface.co/production/uploads/624ceaa38746b2f5773c2d1c/SQgVUuJ831NQ0Rr9_5Bp0.jpeg"></td>
  <td>
    <strong>question:</strong> What is the name of this famous sight in the photo?
    <br>
    <strong>caption:</strong> An aerial view of Diamond Head in the Hawaiian Islands.
    <br>
    <strong>gpt_answer:</strong> The famous sight in the photo is Diamond Head.
  </td>
  <td>
    <strong>question:</strong> 사진에 나오는 이 유명한 장소의 이름은 무엇인가요?
    <br>
    <strong>caption:</strong> 하와이 제도의 다이아몬드 헤드를 공중에서 본 모습입니다.
    <br>
    <strong>gpt_answer:</strong> 이 사진은 하와이에 있는 다이아몬드 헤드입니다.
  </td>
</tr>
</table>
<br>

## Inference Prompt
```
<image>
{question}
```

<br>

## Evaluation Prompt
```
[설명]
{caption}

[질문]
{question}

[어시스턴트 1]
{gpt_answer}
[어시스턴트 1 끝]

[어시스턴트 2]
{target_model_answer}
[어시스턴트 2 끝]

[System]
두 인공지능 어시스턴트의 성능을 [질문]에 대한 응답에 기반하여 평가하세요. 해당 [질문]은 특정 이미지를 보고 생성되었습니다. `유용성`, `관련성`, `정확성`, `세부 수준`, `한국어 생성능력`을 기준으로 응답을 평가하세요. 각각의 어시스턴트에게 1에서 10까지의 전반적인 점수를 부여하며, 높은 점수일수록 더 나은 전반적인 성능을 나타냅니다.

# 단계
1. 제공된 이미지 [설명]을 검토하세요.
2. 각 어시스턴트의 응답을 다음 기준으로 분석하세요:
   - `유용성`: 응답이 사용자의 질문을 얼마나 잘 해결하는가?
   - `관련성`: 응답이 사용자의 질문에 얼마나 적절한가?
   - `정확성`: 응답에서 제공한 정보가 얼마나 정확한가?
   - `세부 수준`: 응답이 과하지 않게 충분히 자세한가?
   - `한국어 생성능력`: 생성된 한국어 문장이 자연스럽고 문법적으로 올바른가?
3. 분석에 기반하여 각 어시스턴트에게 1에서 10까지의 점수를 부여하세요.
4. 두 점수를 공백으로 구분하여 한 줄로 제공하세요.
5. 점수에 대한 이유를 강조하면서 포괄적인 평가를 제공하고, 편견을 피하며 응답의 순서가 판단에 영향을 미치지 않도록 하세요.

# 출력 형식
- 첫 번째 줄: `어시스턴트1_점수 어시스턴트2_점수` (예: `8 9`)
- 두 번째 줄: `유용성`, `관련성`, `정확성`, `세부 수준`, `한국어 생성능력` 기준으로 점수를 설명하는 자세한 문단을 제공합니다.

# 주의사항
- 평가 시 잠재적 편견을 방지하여 객관성을 확보하세요.
- 분석과 설명에서 일관성과 명확성을 유지하세요.
```

<br>

## Results
Below are the evaluation results of various vision-language models, including [VARCO-VISION-14B](https://huggingface.co/NCSOFT/VARCO-VISION-14B) on K-LLaVA-W.

| | VARCO-VISION-14B | Pangea-7B | Pixtral-12B | Molmo-7B-D-0924 | Qwen2-VL-7B-Instruct | LLaVA-One-Vision-7B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| K-LLaVA-W | **84.74** | 69.70 | 82.00 | 63.90 | 62.00 | 48.80 |

<br>

## References
[1] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Advances in neural information processing systems, 36, 2024.

<br>

## Citation
If you use K-LLaVA-W in your research, please cite the following:

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
