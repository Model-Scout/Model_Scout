---
license: apache-2.0
task_categories:
  - text-generation
language:
  - ko
tags:
  - medical
---
**1차 번역 완료**

**I found several problems during translation, so additional filtering will be needed after completion.**

**Step 1. It was confirmed that the existing data contained a lot of data that was close to duplicates. Need to remove those.**

**Step 2. There are many outputs with a risk of hallucination. Data where the last sentence of output is incomplete must be edited.**

**Step 3. If data corresponding to the output is also included in the input, those must be edited.**

# Ko-AlpaCare

This is the repo for *KoMedInstruct*, which is a Korean translated version of MedInstruct-52k dataset. MedInstruct-52k is a synthetically generated medical instruction dataset used by AlpaCare[1].

## Data Translation Process

I used DeepL Pro app (manually). (I also used DeepL free API a little bit at first)

## Warning

This is the result of simple translation **without additional filtering**. Although the medical information may be incorrect in original data, it is also possible that errors may have occurred during the translation process.

Also, I do not recommend using data that contains the instruction: “Please paraphrase the following so that a non-medical professional can understand it.” (or something similar). That's because sentences before and after conversion are almost identical in Korean.

## Example

Here's a few examples.
```
"instruction": "이 약을 진통제, 해열제, 항생제 또는 항우울제로 분류하세요.",
"input": "메트로니다졸",
"output": "메트로니다졸은 항생제로 분류됩니다.\n\n정답은 항생제입니다."
```

```
"instruction": "화이자-바이오엔텍 및 모더나 COVID-19 백신과 같은 mRNA 백신의 주요 기능 메커니즘을 요약하세요.",
"input": "<noinput>",
"output": "화이자-바이오엔텍 및 모더나 COVID-19 백신과 같은 mRNA 백신은 우리 몸의 세포에 스파이크 단백질이라는 특정 단백질을 생산하도록 지시를 내리는 방식으로 작동합니다. 이 단백질은 COVID-19를 유발하는 SARS-CoV-2 바이러스의 표면에서 발견됩니다. 백신의 mRNA가 세포에 들어가 세포의 기계를 사용하여 스파이크 단백질을 생성합니다. 스파이크 단백질이 생성되면 면역 반응을 일으켜 스파이크 단백질을 인식하고 공격할 수 있는 항체가 생성됩니다. 향후 백신을 접종한 개인이 실제 바이러스에 직면하면 면역 체계가 감염과 싸울 준비가 더 잘 되어 있습니다.\n\n따라서 mRNA 백신의 주요 기능 메커니즘은 세포가 바이러스 단백질을 생산하도록 지시하여 면역 반응을 촉발하여 바이러스에 대한 보호를 제공하는 것입니다.\n"
```

## Reference

```
@misc{zhang2023alpacareinstructiontuned,
      title={AlpaCare:Instruction-tuned Large Language Models for Medical Application}, 
      author={Xinlu Zhang and Chenxin Tian and Xianjun Yang and Lichang Chen and Zekun Li and Linda Ruth Petzold},
      year={2023},
      eprint={2310.14558},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```