---
language:
- en
- ko
license: cc-by-nc-4.0
task_categories:
- text-generation
tags:
- math
- aimo
---

# IMPORTANT NOTE
- This data is part of the progress. Current translation progress: 24.85% (2024-09-18 01:32 KST)
- I'm taking a short break due to personal reasons. I'll be back in a month.

## TODO-LIST
- Finish translation

## Translation

I used **gemini-1.5-pro-exp-0827**. The prompt used for translation will be disclosed at the end.

# Dataset Card for NuminaMath CoT

## Dataset Description

- **Homepage:** https://projectnumina.ai
- **Repository:** https://github.com/project-numina/aimo-progress-prize
- **Paper:** https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf
- **Leaderboard:** 
- **Point of Contact:** [Jia Li](jia@projectnumina.ai)


### Dataset Summary

Tool-integrated reasoning (TIR) plays a crucial role in this competition. However, collecting and annotating such data is both costly and time-consuming. To address this, we selected approximately 70k problems from the NuminaMath-CoT dataset, focusing on those with numerical outputs, most of which are integers. We then utilized a pipeline leveraging GPT-4 to generate TORA-like reasoning paths, executing the code and producing results until the solution was complete. We filtered out solutions where the final answer did not match the reference and repeated this process three times to ensure accuracy and consistency. This iterative approach allowed us to generate high-quality TORA data efficiently.

### Licensing Information

The dataset is available under the [Creative Commons NonCommercial (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

### Citation Information

```
@misc{numina_math_datasets,
  author = {Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu},
  title = {NuminaMath TIR},
  year = {2024},
  publisher = {Numina},
  journal = {Hugging Face repository},
  howpublished = {\url{[https://huggingface.co/AI-MO/NuminaMath-TIR](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)}}
}
```