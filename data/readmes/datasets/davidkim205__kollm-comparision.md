---
license: apache-2.0
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    sequence: string
  - name: src
    dtype: string
  splits:
  - name: train
    num_bytes: 123837782
    num_examples: 116166
  download_size: 66685801
  dataset_size: 123837782
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ko
---

# davidkim205/kollm-comparision

[nox-solar-10.7b-v4](https://huggingface.co/davidkim205/nox-solar-10.7b-v4)에 사용된 dpo 데이터셋으로 huggingface에 공개된 데이터와 twodigit에서 제작한 데이터로 구성되어 있습니다.

[nox github](https://github.com/davidkim205/nox)에서 사용가능하도록 comparision 형식으로 되어 있습니다.

## 공개 데이터셋
| Source | 설명 | 원본 URL |
|---|---|---|
| kobest_boolq | 한국어 벤치마크 KoBEST | https://huggingface.co/datasets/skt/kobest_v1 |
| kobest_copa | 한국어 벤치마크 KoBEST | https://huggingface.co/datasets/skt/kobest_v1 |
| kobest_hellaswag | 한국어 벤치마크 KoBEST | https://huggingface.co/datasets/skt/kobest_v1 |
| kobest_sentineg | 한국어 벤치마크 KoBEST | https://huggingface.co/datasets/skt/kobest_v1 |
| kobest_wic | 한국어 벤치마크 KoBEST | https://huggingface.co/datasets/skt/kobest_v1 |
| kollm_belebele | 다국어 MRC 벤치마크 Belebele의 한국어 subset | https://huggingface.co/datasets/facebook/belebele/blob/main/data/kor_Hang.jsonl |
| kollm_csatqa | 한국어 대학수학능력시험 질답 데이터셋 | https://huggingface.co/datasets/HAERAE-HUB/csatqa |
| kollm_paws-x | PAWS-X 데이터셋의 영어-한국어 subset | https://huggingface.co/datasets/paws-x/viewer/ko |
| Orca-DPO-Pairs-KO | Intel/orca_dpo_pairs의 한글 번역 데이터셋 | https://huggingface.co/datasets/Ja-ck/Orca-DPO-Pairs-KO |
| orca_dpo_pairs_ko | Intel/orca_dpo_pairs의 한글 번역 데이터셋 | https://huggingface.co/datasets/mncai/orca_dpo_pairs_ko |
| X-TruthfulQA_en_zh_ko_it_es | 다국어 벤치마크 X-TruthfulQA 의 한국어 subset | https://huggingface.co/datasets/zhihz0535/X-TruthfulQA_en_zh_ko_it_es |
| Yi-Ko-DPO-Orca-DPO-Pairs | Intel/orca_dpo_pairs의 한글 번역 데이터셋 | https://huggingface.co/datasets/We-Want-GPU/Yi-Ko-DPO-Orca-DPO-Pairs |

## twodigit 내부 데이터셋

| Source | 설명 | 원본 URL |
|---|---|---|
| news_common_gen | 뉴스 기반 common gen 형식 데이터셋 | https://huggingface.co/datasets/twodigit/news_common_gen |

aihub 데이터는 라이센스 문제로 제외 하였습니다. 자세한 내용은 아래를 참조하세요.

https://aihub.or.kr/partcptnmlrd/inqry/view.do?currMenu=144&topMenu=104
