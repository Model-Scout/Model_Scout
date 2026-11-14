---
license: gemma
base_model: google/gemma-3-270m-it
language: [ko]
pipeline_tag: text-generation
tags: [mlx, on-device, schedule-extraction]
---
# schedule-extractor-gemma3-270m (MLX, 8-bit)

iOS 앱 「스크린샷 플래너」가 기기 안에서 MLX로 쓰는 일정 추출 모델입니다. 안드로이드용(LiteRT-LM)과 같은 가중치이며
학습 내용은 https://huggingface.co/skkw1128/schedule-extractor-gemma3-270m 를 보세요.

## 수정 사항 (Modified from Gemma)

**Google Gemma 3 270M (instruction-tuned)** 의 파생 모델(Model Derivative)입니다. 합성한 일정 데이터 약 20,000건으로
LoRA 파인튜닝 후 가중치를 병합하고 `mlx_lm.convert`로 8비트 양자화했습니다.

## 라이선스 및 사용 제한

Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms

이 모델과 그 파생물을 사용·배포하려면 [Gemma Terms of Use](https://ai.google.dev/gemma/terms)에 동의해야 하며,
[Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)의 사용 제한이 적용됩니다.
재배포 시 수신자에게도 같은 약관과 사용 제한을 알려야 합니다. 약관 전문은 이 저장소의 `LICENSE` 파일에 있습니다.

Gemma는 Google LLC의 상표이며, 이 저장소는 Google의 보증이나 제휴를 뜻하지 않습니다.
