---
license: cc0-1.0
task_categories:
- image-classification
language:
- ko
- en
pretty_name: Tomato Leaf Disease — 2,000-image teaching subset
size_categories:
- 1K<n<10K
tags:
- agriculture
- plant-disease
- tomato
- education
---

# 토마토 잎 사진 2,000장 (교육용 묶음)

토마토 잎 사진으로 병해충 진단기를 만들고 검증하는 실습에 쓰는 묶음입니다. 10개 클래스에서 클래스마다 200장씩, 모두 2,000장(약 35MB)입니다.

- 원본: [Project-AgML/tomato_leaf_disease](https://huggingface.co/datasets/Project-AgML/tomato_leaf_disease) (CC0 1.0, 11,000장). 원본 계열은 PlantVillage입니다(Kaggle kaustubhb999/tomatoleaf 경유).
- 사진: 원본의 256×256 JPEG 바이트를 그대로 옮겼고, 파일 이름도 원본 그대로입니다.
- 이용 조건: CC0 1.0. 교육과 재배포에 제약이 없습니다. 원본을 함께 밝혀 주시면 좋습니다.
- 만든 곳: 매치업(Match業) 지능형농장 X+AI 심화과정 실습 자료(2026년 10월).

## 받기

사진 2,000장을 압축 파일 하나(`tomato_leaf_small_2000.zip`, 약 34MB)로 올려 두었습니다. 사진을 한 장씩 받으면 요청 수 제한에 걸리므로, 이 파일 하나를 받아 풉니다.

```bash
hf download tmoon-atx/tomato_leaf_small_2000 tomato_leaf_small_2000.zip --repo-type dataset --local-dir data
cd data && unzip tomato_leaf_small_2000.zip      # → data/tomato_leaf_small/
```

브라우저로 받으려면: https://huggingface.co/datasets/tmoon-atx/tomato_leaf_small_2000/resolve/main/tomato_leaf_small_2000.zip

## 구성

압축을 풀면

```
tomato_leaf_small/
  images/<클래스 영문 이름>/<원본 파일 이름>   클래스마다 200장
  labels.csv                                     사진마다 한 줄
  README.md                                      이 설명
```

labels.csv 열

| 열 | 뜻 |
| --- | --- |
| file | 사진 경로(images/…) |
| class | 클래스 영문 이름(폴더 이름과 같음) |
| class_ko | 한국어 이름 |
| source | 촬영 출처 부호. 원본 파일 이름 안의 `___<출처>_<병해 약칭> <번호>` 조각에서 꺼냈습니다. 클래스와 거의 일대일로 묶여 있어, 모델이 병반 대신 배경을 배울 수 있습니다. |
| origin | 원본 사진 식별자. 같은 값이면 한 장의 사진을 돌리거나 뒤집어 만든 사본입니다. 학습과 평가에 나눠 담으면 데이터 누수가 생깁니다. |
| augmented | 1이면 돌리거나 뒤집어 만든 사본 |

| 폴더 | 한국어 이름 | 장수 |
| --- | --- | --- |
| `Bacterial_Spot` | 세균성점무늬병 | 200 |
| `Early_Blight` | 겹둥근무늬병 | 200 |
| `Healthy` | 정상 | 200 |
| `Late_Blight` | 역병 | 200 |
| `Leaf_Mold` | 잎곰팡이병 | 200 |
| `Mosaic_Virus` | 토마토모자이크바이러스 | 200 |
| `Septoria_Leaf_Spot` | 세프토리아잎마름병 | 200 |
| `Spider_Mites` | 점박이응애 피해 | 200 |
| `Target_Spot` | 표적점무늬병 | 200 |
| `Yellow_Leaf_Curl_Virus` | 토마토황화잎말림바이러스 | 200 |

한국어 이름은 실습 중 부르기 쉽도록 붙인 관용 표기입니다. 정확한 병명과 방제 기준은 농촌진흥청 등 공식 자료를 따릅니다. 이 묶음은 교육용이며, 실제 진단에 쓰는 것을 전제로 만들지 않았습니다.

## English summary

A 2,000-image teaching subset (200 per class, 10 classes, ~35 MB) of [Project-AgML/tomato_leaf_disease](https://huggingface.co/datasets/Project-AgML/tomato_leaf_disease) (CC0 1.0, PlantVillage lineage). Images are the original 256×256 JPEG bytes with original file names. The images come as one zip file (`tomato_leaf_small_2000.zip`) to avoid per-file request limits. `labels.csv` adds `source` (capture source code parsed from the original file name) and `origin` (original-photo identifier shared by rotated/flipped copies), used in class exercises on data leakage and source-held-out evaluation. For education only; not intended for real diagnosis.
