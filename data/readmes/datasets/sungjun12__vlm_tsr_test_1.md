---
license: other
task_categories:
- image-to-text
language:
- ko
tags:
- table-structure-recognition
- TSR
- evaluation
- benchmark
pretty_name: VLM TSR Test Data (Part 1/4)
---

# vlm_tsr_test_1

`vlm_tsr_test`의 1/4 파트. scene 그룹 `50000~50004` 포함.

전체 테스트셋은 4개 레포로 나뉘어 있습니다:
- [vlm_tsr_test_1](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_1)
- [vlm_tsr_test_2](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_2)
- [vlm_tsr_test_3](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_3)
- [vlm_tsr_test_4](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_4)

코드 및 전체 파이프라인: [Lim-Sung-Jun/vlm_training_template](https://github.com/Lim-Sung-Jun/vlm_training_template)

## 구조

각 샘플은 3개 파일 세트로 구성됩니다:
```
test/source/T01_C01/{id}.jpg    # 테이블 이미지
test/source/T01_C01/{id}.json   # 정답 HTML + 메타데이터
test/label/T01_C01/{id}.html    # 렌더링용 GT HTML
```

## 평가 메트릭

| 메트릭 | 설명 |
|--------|------|
| TEDS | Tree-Edit Distance 기반 구조 유사도 (0~1) |
| TEDS-Structure | 텍스트 제외 구조만 평가 |
| Span Cell F1 | 병합 셀(colspan/rowspan) 예측 정확도 |
