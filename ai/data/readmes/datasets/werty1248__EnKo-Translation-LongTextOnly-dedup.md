---
task_categories:
- translation
language:
- ko
- en
---

### 장문 번역 데이터만 추출

- [gemma](https://huggingface.co/google/gemma-7b) 토크나이저 기준으로 영문+한글 토큰 합이 1K 이상인 데이터만 추출
- 데이터 수
  - 1K~2K: 146,957
  - 2K~4K: 11,823
  - 4K~: 2,229
- 한/영 둘 중 한쪽만 중복인 경우는 제거하지 않았습니다.

### 데이터 출처

- [nayohan/aihub-en-ko-translation-12m](https://huggingface.co/datasets/nayohan/aihub-en-ko-translation-12m)
- [nayohan/instruction_en_ko_translation_1.4m](https://huggingface.co/datasets/nayohan/instruction_en_ko_translation_1.4m)
  - [jhflow/orca_ko_en_pair](https://huggingface.co/datasets/jhflow/orca_ko_en_pair)
  - [jhflow/platypus_ko_en_pair](https://huggingface.co/datasets/jhflow/platypus_ko_en_pair)
  - [jhflow/dolly_ko_en_pair](https://huggingface.co/datasets/jhflow/dolly_ko_en_pair)
  - [heegyu/OIG-small-chip2-ko](https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko)
  - [lemon-mint/en_ko_translation_purified_v0.1](https://huggingface.co/datasets/lemon-mint/en_ko_translation_purified_v0.1)
  - [squarelike/sharegpt_deepl_ko_translation](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation)
  - [amphora/parallel-wiki-koen](https://huggingface.co/datasets/amphora/parallel-wiki-koen)
  - [kuotient/gsm8k-ko](https://huggingface.co/datasets/kuotient/gsm8k-ko)
  - [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)

### 데이터 출처 분포

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/kqfX4nG4fMy30xUWHdvtL.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/XRkzNjMpaK8VHU3-vPzuj.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/Z513Kr5JXV49y3Dvizl9y.png)
