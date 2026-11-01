---
license: apache-2.0
language:
- ja
- ko
base_model:
- trillionlabs/Tri-7B-Base
pipeline_tag: translation
tags:
- axolotl
new_version: hell0ks/ja-ko-vn-12b-v2
---

# ja-ko-vn-7b

<!-- Provide a quick summary of what the model is/does. -->

This model translates short dialogue from Japanese visual novels or other games into Korean.

이 모델은 일본어로 된 비주얼 노벨 혹은 타 게임의 짧은 대사를 한국어로 번역합니다.

## Updates

* 2025/12/06 - Model upload
* 2025/12/06 - 모델 업로드
* 2025/12/07 - Fixed chat template
* 2025/12/07 - 채팅 템플릿을 수정했습니다

## Model Details

### Model Description

TrillionLabs의 Tri-7B-Base를 베이스로 해서, 그 위에 Visual Novel의 대사 원문(일본어)과 번역(한국어)을 SFT 한 모델입니다.

- **Developed by:** hell0ks
- **Model type:** Translation
- **Language(s) (NLP):** Japanese(Input), Korean(Output)
- **License:** Apache 2.0
- **Finetuned from model :** [trillionlabs/Tri-7B-Base](https://huggingface.co/trillionlabs/Tri-7B-Base)
- **Max context length :** 4096

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [hell0ks/ja-ko-vn-7b-v1](https://huggingface.co/hell0ks/ja-ko-vn-7b-v1)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

* Temperature: 0.1, Top_k = 0.9 추천드립니다.
* 고유 명사, 이름 등은 System prompt로 힌트를 주실 수 있습니다. 예: `岡部倫太郎=오카베 린타로,阿万音鈴羽=아마네 스즈하`
* 프롬프트는 **일본어 원문만** 입력하세요. 제어 코드나 특수문자도 최대한 그대로 유지하도록 학습되었습니다.
* Chat 모드로 사용하지 마시고, **Completions 모드로 사용하세요.** 싱글 턴으로만 학습되었습니다.

### Direct Use

* vllm, Transformers로 서빙하여 타 게임 플러그인 (XUnityTranslator)등과 사용하실 수 있습니다.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
* 번역의 정확성이 크게 중요하지 않은 작업에만 사용하세요. (비즈니스 용 등에 사용 비권장)

## Bias, Risks, and Limitations

* 일본어에서 한국어 번역만 지원합니다. 반대나 다른 언어는 지원하지 않습니다. (오작동 발생)
* Safety RL이 되지 않은 모델입니다. 출력문의 내용 및 결과물에 대해선 책임지지 않습니다.
* 고유명사 기능이 불안정할 수 있습니다. 발생하는 예시를 피드백 주시면 도움이 됩니다!

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