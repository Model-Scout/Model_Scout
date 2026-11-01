---
license: cc-by-sa-4.0
task_categories:
- translation
language:
- en
- ko
pretty_name: aihub-flores-sparta
size_categories:
- 10K<n<100K
---
### High Quality Ko-En Translation Dataset (AIHub-FLoRes Integrated)
AI Hub의 한-영 번역 데이터셋과 FLoRes 한-영 번역 데이터셋의 합본입니다.

### High Quality AIHub Dataset
AI Hub의 경우 한-영 번역 관련 데이터셋을 8개 병합한 병렬 데이터 [traintogpb/aihub-koen-translation-integrated-tiny-100k](https://huggingface.co/datasets/traintogpb/aihub-koen-translation-integrated-tiny-100k)에서 고품질의 번역 레퍼런스를 가진 데이터만 추출하였습니다.

번역 레퍼런스 품질 평가 척도는 [Unbabel/XCOMET-XL](https://huggingface.co/Unbabel/XCOMET-XL) (3.5B)로 측정한 xCOMET metric입니다.

8개의 AIHub 데이터 소스 중 기존 실험을 통해 번역 성능(SacreBLEU)이 낮았던 4개의 소스에서 xCOMET 기준 상위 5,000개, 그 외 4개의 소스에서 xCOMET 기준 상위 2,500개를 추출해 총 약 3만 개의 데이터를 추출하였습니다.

### FLoRes Dataset
FLoRes-200 데이터셋의 경우 997개의 dev, 1,012개의 devtest 스플릿으로 구성되어 있으나, 최대한의 학습 성능을 위해 둘을 합한 2,009개의 데이터 중 200개의 임의 test셋을 제외한 나머지 1,809개의 데이터를 AIHub 데이터와 합본시켰습니다.

### Dataset Summary
|  | __[AI Hub] 일상생활 및 구어체(71265)__ | __[AI Hub] 일반(126)__ | __[AI Hub] 사회과학(125)__ | __[AI Hub] 전문분야(111)__ | __[AI Hub] 기술과학1(124)__ | __[AI Hub] 기술과학2(71266)__ | __[AI Hub] 방송콘텐츠(71382)__ | __[AI Hub] 산업정보(특허)(563)__ | __[FLoRes]__ | __총합__ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| __Tiny-100K(Train)__ | 19712 | 12780 | 10919 | 10877 | 10818 | 10733 | 4601 | 2892 | 0 | 83332 |
| __Sparta-Tiny-30K(Train)__ | 2500 | 5000 | 5000 | 5000 | 2500 | 2500 | 4601 | 2500 | 1809 | 31410 |
| __Mini-1M(Train)__ | 198471 | 128104 | 108894 | 107520 | 108014 | 106518 | 46831 | 28969 | 0 | 833321 |
| __Sparta-Mini-300K(Train)__ | 50000 | 50000 | 50000 | 50000 | 25000 | 25000 | 35000 | 10000 | 1809 | 296809 |
