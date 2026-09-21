---
license: mit
datasets:
- maywell/korean_textbooks
language:
- ko
pipeline_tag: text-generation
library_name: transformers
---
tzem (**ㅌ**__ **ㅈ**_**ㅇ** **ㅁ**__!)

[korean_textbooks](https://huggingface.co/datasets/maywell/korean_textbooks) 데이터셋 정리 후 사전 학습 한 모델입니다. 비용 문제로 1 epoch만 진행하였습니다.

## 데이터셋 정리 내용:

1. 데이터에 여러 번 반복되는 문장 있을 시 제거

2. 한글이 없는 데이터 제거

3. html 태그가 포함된 데이터 제거

4. 토론 데이터 포맷 통일, 존댓말로 수정

5. 토론 데이터에서 Phi를 철수로, Epsilon을 영희로 변경

6. 기타 등등