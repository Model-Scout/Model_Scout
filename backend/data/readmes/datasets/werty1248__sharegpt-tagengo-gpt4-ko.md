---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 1K<n<10K
---

**Original Dataset**: [lightblue/tagengo-gpt4](https://huggingface.co/datasets/lightblue/tagengo-gpt4)

### ShareGPT-tagengo-GPT4-ko

- LMSYS-Chat-1M를 통해 수집된 실제 유저들과 GPT-4(`gpt-4-0125-preview`) 사이의 단발성 대화 데이터 셋입니다.
- tagengo-gpt4 데이터 셋에서 한국어 데이터 1,609개를 추출한 뒤, 사람이 직접 확인하여 일부 불필요한/중복 질문, 잘못된 답변 등을 제거했습니다.
- 자세한 언어별 분류 방법은 [lightblue/tagengo-gpt4](https://huggingface.co/datasets/lightblue/tagengo-gpt4)를 참고하세요.
- 번역이 아닌, 실제 한국어로 주고 받은 데이터 셋입니다.

### Files

- **sharegpt_tagengo_ko.json**: 불필요한/중복 질문 및 잘못된 답변을 제거한 1,540개 데이터입니다.
- **sharegpt_tagengo_ko_no_sorry.json**: sharegpt_tagengo_ko.json에서 "죄송"으로 시작되는 답변(GPT-4의 답변 거부)을 제거한 1,488개 데이터입니다.

### License

- [lightblue/tagengo-gpt4](https://huggingface.co/datasets/lightblue/tagengo-gpt4)의 라이선스 정책에 따릅니다.