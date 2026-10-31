---
language:
- ko
size_categories:
- 100K<n<1M
pretty_name: orcamathko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_en
    dtype: string
  - name: answer_en
    dtype: string
  splits:
  - name: train
    num_bytes: 458376850
    num_examples: 193789
  download_size: 171362639
  dataset_size: 458376850
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
---
원본 데이터셋: https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k

번역 모델: [Seagull-13b-translation](https://huggingface.co/kuotient/Seagull-13b-translation)

후처리
- 번역 repetition 오류 제거
- LaTeX 오류 체크(전부는 아닐 수 있음. `/(/)` -> `/(/` 같은 오류 등...)


## Citation
```
@misc{mitra2024orcamath,
      title={Orca-Math: Unlocking the potential of SLMs in Grade School Math}, 
      author={Arindam Mitra and Hamed Khanpour and Corby Rosset and Ahmed Awadallah},
      year={2024},
      eprint={2402.14830},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```