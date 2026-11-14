---
license: gemma
base_model: google/gemma-3-270m-it
library_name: transformers.js
language: ko
---
# parking-gemma-270m-v2-ko-onnx

운전자 음성 질문 → 주차장 검색 조건 JSON 추출용 LoRA 튜닝 Gemma 3 270M (ONNX fp16, transformers.js).

- 어휘 축소: 262,144 → 50,874 토큰 (한국어 토큰 전부 + 학습 데이터에 나온 토큰 + 자주 쓰는 영어·숫자·기호 4만 + 바이트 256).
  모델 파일 570MB → 299MB.
- 원래 모델과 동일성: 평가 131문항에서 첫 토큰 점수 최대 차이 0, 끝까지 생성한 답과 틀린 문항까지 동일 (완전 일치 67.2%).

Gemma 이용 약관(https://ai.google.dev/gemma/terms)이 적용됩니다.
