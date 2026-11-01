---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
- question-answering
language:
- en
- ko
---

이 데이터셋은 자체 구축한 번역기로 [WizardLM/WizardLM_evol_instruct_V2_196k](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2_196k)을 번역한 데이터셋입니다. 아래 README 페이지도 번역기를 통해 번역되었습니다. 참고 부탁드립니다.


## News

- 🔥 🔥 🔥 [08/11/2023] **WizardMath** 모델을 출시합니다.
- 🔥 **WizardMath-70B-V1.0** 모델은 **ChatGPT 3.5**, **Claude Instant 1** 및 **PaLM 2 540B** 를 포함 하 여 GSM8K에서 일부 폐쇄 소스 LLMs 보다 약간 더 우수 합니다.
- 🔥 우리의 **WizardMath-70B-V1.0** 모델은 SOTA 오픈 소스 LLM보다 **24.8** 포인트 높은 [GSM8k Benchmarks](https://github.com/openai/grade-school-math)에서  **81.6 pass@1** 을 달성합니다.
- 🔥 우리의 **WizardMath-70B-V1.0** 모델은 SOTA 오픈 소스 LLM보다 **9.2** 포인트 높은 [MATH 벤치마크](https://github.com/hendrycks/math)에서  **22.7 pass@1** 을 달성합니다.

| 모델 | 체크포인트 | 용지  | GSM8k | MATH  |온라인 데모| 라이선스
| ----- |------| ---- |------|-------| ----- | ----- |
| WizardMath-70B-V1.0 | 🤗 <a href="https://huggingface.co/WizardLM/WizardMath-70B-V1.0" target="_blank">HF Link</a> | 📃 <a href="https://arxiv.org/abs/2308.09583" target="_blank">[WizardMath]</a>| **81.6**  |  **22.7** smells|[Demo](http://47.103.63.15:50083/)| <a href="https://ai.meta.com/resources/models-and-libraries/llama-downloads/" target="_blank">Llama 2 </a> |
| WizardMath-13B-V1.0 | 🤗 <a href="https://huggingface.co/WizardLM/WizardMath-13B-V1.0" target="_blank">HF Link</a> | 📃 <a href="https://arxiv.org/abs/2308.09583" target="_blank">[WizardMath]</a>| **63.9**  |  **14.0** |[Demo](http://47.103.63.15:50082/)| <a href="https://ai.meta.com/resources/models-and-libraries/llama-downloads/" target="_blank">Llama 2</a> |
| WizardMath-7B-V1.0 | 🤗 <a href="https://huggingface.co/WizardLM/WizardMath-7B-V1.0" target="_blank">HF Link</a>  | 📃 <a href="https://arxiv.org/abs/2308.09583" target="_blank">[WizardMath]</a>| Automation **54.9**  |  **10.7** | [Demo](http://47.103.63.15:50080/)|  <a href="https://ai.meta.com/resources/models-and-libraries/llama-downloads/" target="_blank">Llama 2 </a>|


<font size=4>

| <sup>Model</sup> | <sup>Checkpoint</sup> | <sup>Paper</sup> |<sup>MT-Bench</sup> | <sup>AlpacaEval</sup> | <sup>WizardEval</sup> | <sup>HumanEval</sup>  | <sup>License</sup>|
| ----- |------| ---- |------|-------| ----- | ----- | ----- |
| <sup>WizardLM-13B-V1.2</sup> | <sup>🤗 <a href="https://huggingface.co/WizardLM/WizardLM-13B-V1.2" target="_blank">HF Link</a></sup>|  | <sup>7.06</sup> | <sup>89.17%</sup>Placement | <sup>101.4%</sup>|<sup>36.6  pass@1</sup>|<sup> <a href="https://ai.meta.com/resources/models-and-libraries/llama-downloads/" target="_blank">Llama 2 License</a></sup> |
| <sup>WizardLM-13B-V1.1</sup> |<sup> 🤗 <a href="https://huggingface.co/WizardLM/WizardLM-13B-V1.1" target="_blank">HF Link</a> </sup> |  | <sup>6.76</sup>  |<sup>86.32%</sup>Automation | <sup>99.3%</sup> |<sup>25.0  pass@1</sup>| <sup>Noncommercial</sup>|
| <sup>WizardLM-30B-V1.0</sup> | <sup>🤗 <a href="https://huggingface.co/WizardLM/WizardLM-30B-V1.0" target="_blank">HF Link</a></sup>  | | <sup>7.01</sup> |  |  <sup>97.8%</sup> | <sup>37.8  pass@1</sup>| <sup>비상업</sup> |
| <sup>WizardLM-13B-V1.0</sup> | <sup>🤗 <a href="https://huggingface.co/WizardLM/WizardLM-13B-V1.0" target="_blank">HF Link</a></sup> |  | <sup>6.35</sup> | <sup>75.31%</sup> |  <sup>89.1%</sup> | <sup>24.0 pass@1</sup> | <sup>비상업</sup>|
| <sup>WizardLM-7B-V1.0</sup>|  <sup>🤗 <a href="https://huggingface.co/WizardLM/WizardLM-7B-V1.0" target="_blank">HF Link</a></sup> |<sup> 📃 <a href="https://arxiv.org/abs/2304.12244" target="_blank">[WizardLM]</a></sup>|  |  |  <sup>78.0%</sup> |<sup>19.1 pass@1</sup>|<sup> 비상업적</sup>|
| <sup>WizardCoder-15B-V1.0</sup> | <sup> 🤗 <a href="https://huggingface.co/WizardLM/WizardCoder-15B-V1.0" target="_blank">HF Link</a></sup>  | <sup>📃 <a href="https://arxiv.org/abs/2306.08568" target="_blank">[WizardCoder]</a></sup> | || <sup> 57.3 pass@1</sup> | <sup> <a href="https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement" target="_blank">OpenRAIL-M</a></sup> |
</font>


**리포지토리**: https://github.com/nlpxucan/WizardLM

**Twitter**: https://twitter.com/WizardLM_AI/status/1669364947606982656



이 데이터 세트에는 알파카와 샤레GPT의 143K 혼합 진화 데이터가 포함되어 있다.

이것은 WizardLM 모델의 Evol-Instruct 학습 데이터의 최신 최적화 버전이다.

데이터 사용 라이선스로 인해 약 196k 데이터 행으로 구성된 **최종 전체 데이터 세트** 를 가져오려면 원본 [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered)를 **병합**하십시오.