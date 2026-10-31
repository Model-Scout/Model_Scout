---
task_categories:
- feature-extraction
language:
- ko
tags:
- audio
- homecam
- numpy
viewer: false
size_categories:
- 100M<n<1B
---

## Dataset Overview
- The dataset is a curated collection of `.npy` files containing MFCC features extracted from raw audio recordings. 
- It has been specifically designed for training and evaluating machine learning models in the context of real-world emergency sound detection and classification tasks. 
- The dataset captures diverse audio scenarios, making it a robust resource for developing safety-focused AI systems, such as the `SilverAssistant` project.

## Dataset Descriptions
- The dataset used for this audio model consists of `.npy` files containing MFCC features extracted from raw audio recordings. These recordings include various real-world scenarios, such as:
    - `violent_crime`: Violence / Criminal activities (폭력/범죄)
    - `fall`: Fall down (낙상)
    - `help_request`: Cries for help (도움 요청)
    - `daily-1`, `daily-2`: Normal indoor sounds (일상)

- Feature Extraction Process
    1.	Audio Collection:
        - Audio samples were sourced from datasets, such as AI Hub, to ensure coverage of diverse scenarios. 
        - These include emergency and non-emergency sounds to train the model for accurate classification.
    2.	MFCC Extraction:
        - The raw audio signals were processed to extract Mel-Frequency Cepstral Coefficients (MFCC).
        - The MFCC features effectively capture the frequency characteristics of the audio, making them suitable for sound classification tasks.
        ![MFCC Output](./pics/mfcc-output.png)
    3.	Output Format:
        - The extracted MFCC features are saved as `13 x n` numpy arrays, where:
        - 13: Represents the number of MFCC coefficients (features).
        - n: Corresponds to the number of frames in the audio segment.
    4.	Saved Dataset:
        - The processed `13 x n` MFCC arrays are stored as `.npy` files, which serve as the direct input to the model.

- Adaptation in `SilverAssistant` project: [HuggingFace SilverAudio Model](https://huggingface.co/SilverAvocado/Silver-Audio)

## Data Source
- Source: [AI Hub 위급상황 음성/음향](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=170)