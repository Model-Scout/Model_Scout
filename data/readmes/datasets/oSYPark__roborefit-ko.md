---
language:
- ko
- en
license: unknown
task_categories:
- image-segmentation
tags:
- referring-expression-segmentation
- robotics
- korean
---

# RoboRefit Korean Translation (annotations only)

RoboRefit (robot 작업대 위 실사진 기반 referring expression segmentation
데이터셋) 어노테이션의 한국어 번역본입니다. **원본 이미지는 포함하지
않습니다** — 원 데이터셋 저작자의 명시적 재배포 라이선스가 없어, 저희가
새로 만든 결과물인 `expressions_ko` 필드만 추가한 COCO-format JSON 어노테이션
파일만 올립니다.

이 번역 데이터로 학습한 체크포인트는
[oSYPark/VATEX-korean-pnp](https://huggingface.co/oSYPark/VATEX-korean-pnp)에
있습니다 (`roborefit_finetune_ko`, `roborefit_pnp_finetune_ko` 둘 다 이
데이터로 학습).

## 사용 방법

1. 원본 RoboRefit 이미지/마스크를 원 배포처에서 받습니다.
2. 이 레포의 JSON을 원본 데이터 루트와 같은 위치에 놓습니다. 각 어노테이션의
   `images[i].file_name`이 `RoboRefit/<train|testA|testB>/image/xxxxxxx.png`
   형태의 상대 경로이므로, 이 경로 기준으로 이미지를 찾을 수 있는 루트
   디렉토리 아래에 두면 됩니다 (예: detectron2
   `register_coco_instances(name, {}, json_file, image_root)`에서
   `image_root`가 그 루트).

```python
import json
d = json.load(open("instances_roborefit_train_ko.json"))
print(d["annotations"][0]["expressions"])     # 원본 영어 표현들
print(d["annotations"][0]["expressions_ko"])  # 한국어 번역
```

## 번역 방법

- NLLB-200-distilled-1.3B로 1회 오프라인 번역 (학습 데이터용 — 실제 로봇
  명령 실시간 번역에는 사용하지 않음).
- 카테고리명 글로서리(`utils/ko_category_glossary.py`) + 플레이스홀더
  치환으로 흔한 오역(예: "cone"이 엉뚱한 단어로 번역되는 경우)을 교정.
- 조사(을/를 등)는 받침 유무에 따라 규칙 기반으로 교정.

번역 스크립트: `utils/translate_expressions_ko.py` (코드 레포:
[VATEX-korean-pnp](https://github.com/Se0ngYe0l/VATEX-korean-pnp)).

## 통계

| split | images | annotations | expressions_ko 결측 |
|---|---|---|---|
| train | 7929 | 36915 | 0 |
| testA | 1859 | 8523  | 0 |
| testB | 1083 | 5320  | 0 |
