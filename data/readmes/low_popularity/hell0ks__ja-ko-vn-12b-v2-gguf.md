---
license: gemma
language:
- ja
- ko
base_model:
- hell0ks/ja-ko-vn-12b-v2
pipeline_tag: translation
tags:
- axolotl
---

# ja-ko-vn-12b V2 (GGUF)

<!-- Provide a quick summary of what the model is/does. -->

<p align="center">
<picture>
  <img src="https://huggingface.co/hell0ks/ja-ko-vn-12b-v2/resolve/main/assets/jako-icon.png" alt="Main icon", style="width: 50%;">
</picture>
</p>

This model translates text from Japanese visual novels or various games into Korean.

이 모델은 일본어로 된 비주얼 노벨 혹은 다양한 게임의 텍스트를 한국어로 번역합니다.

## Updates

* 2025/12/13 - Quant upload
* 2025/12/13 - 양자화 업로드

## Model Details

### Model Description

Google의 Gemma 3 12B 모델을 기반으로 하여 비주얼 노벨 등 게임류에 적합한 번역을 하도록 다음 절차를 거쳤습니다:

1. 일본어, 한국어에 대한 문학 계열 도메인 언어 학습 (CPT)
2. 비주얼 노벨의 원문과 번역문 학습 (SFT)
3. 특정 상황 및 단어에 대한 도메인 학습 (DPO)

주로 "직역"을 선호하시는 분께 적합합니다.

- **Developed by:** hell0ks
- **Model type:** Translation
- **Language(s) (NLP):** Japanese(Input), Korean(Output)
- **License:** Gemma
- **Finetuned from model :** [google/gemma-3-12b-pt](https://huggingface.co/google/gemma-3-12b-pt)
- **Max context length :** 4096 (까지만 테스트 됨)

#### V1과의 차이점

- Base model이 Tri-7B에서 Gemma-3-12B로 변경되었습니다.
- CPT, DPO 학습을 통해 좀 더 자연스러운 어휘를 사용하도록 유도했습니다.
- 고유 명사 고정 기능이 불완전한 상태로 릴리즈 된 것을 수정했습니다.

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [hell0ks/ja-ko-vn-12b-v2](https://huggingface.co/hell0ks/ja-ko-vn-12b-v2)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

* Temperature: 0.1, Top_k = 0.95, repetition_penalty 1.05 ~ 1.1를 추천드립니다.
* 고유 명사, 이름 등은 System prompt로 힌트를 주실 수 있습니다. 예: `岡部倫太郎=오카베 린타로,阿万音鈴羽=아마네 스즈하`
* 프롬프트는 **일본어 원문만** 입력하세요. 제어 코드나 특수문자도 최대한 그대로 유지하도록 학습되었습니다.
* Chat 모드로 사용하지 마시고, **Completions 모드로 사용하세요.** 싱글 턴으로만 학습되었습니다.
* **llama.cpp에서 사용하실 때 꼭 --jinja 플래그를 사용하세요.**

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
* 번역의 정확성이 크게 중요하지 않은 작업에만 사용하세요.

## Bias, Risks, and Limitations

* 일본어에서 한국어 번역만 지원합니다. 반대나 다른 언어는 지원하지 않습니다.
* Safety RL이 되지 않았습니다. 유저가 입력한 대사에 대해 그대로 번역합니다.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

* 사용자(직접 및 하위 사용자 모두)는 모델의 위험성, 편향성 및 한계점을 인지해야 합니다.
* 긴 텍스트를 번역해야 하는 경우 문단 혹은 문장 단위로 이용하시는 것을 추천드립니다.

## Technical Specifications

#### Hardware

Nvidia DGX Spark, 2 Nodes

#### Software

Axolotl

## Acknowledgement

학습 하드웨어를 대가 없이 지원해주신 익명의 분께 감사 인사 드립니다.