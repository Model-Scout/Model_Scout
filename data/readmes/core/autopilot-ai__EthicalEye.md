---
license: apache-2.0
requirements:
- sentencepiece: >-
    (if not installed install using `pip install sentencepiece`, and restart
    runtime)
library_name: transformers
pipeline_tag: text-classification
language:
- en
- fr
- hi
- gu
- bn
- ml
- mr
- pa
- it
- es
- kn
- as
- af
- ru
- ro
- sq
- ar
- am
- az
- bs
- bh
- bg
- bo
- ca
- ce
- zh
- cr
- hr
- cs
- da
- de
- nl
- el
- et
- eo
- fi
- fj
- fa
- gl
- ga
- ha
- ht
- he
- hu
- hy
- id
- is
- ja
- jv
- ka
- kk
- km
- ko
- ks
- ku
- ky
- la
- lb
- lt
- lv
- mk
- mn
- ms
- mi
- mt
- ne
- 'no'
- or
- om
- ps
- pl
- pt
- qu
- sa
- sm
- gd
- sr
- sn
- sd
- si
- sk
- sl
- so
- su
- sw
- sv
- tg
- ta
---

## Details

-  Model Name: Ethical Eye
-   Description: Ethical Eye is an open-source AI model developed by AutopilotAI. It is designed to flag and analyze user-generated content for harmful or unethical behavior, providing a last layer of decision-making to assist AI systems in promoting ethical and moral actions. The model leverages advanced techniques such as text classification, toxicity analysis, and cross-lingual NLP to detect abuse, obscene language, and harmful or unethical comments in multiple languages.

## How to use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("autopilot-ai/EthicalEye")

model = AutoModelForSequenceClassification.from_pretrained("autopilot-ai/EthicalEye")
```
## Intended Use

- Primary Use Case: The Ethical Eye model is primarily intended to be used as a tool to flag or block users exhibiting harmful or unethical behavior on various platforms. It aims to assist developers, especially those with limited experience in NLP, in enforcing ethical standards and creating a safer environment for users.
- User Expertise: The model is designed to be accessible to developers with various levels of NLP expertise, including those with limited experience in the field.
- Limitations: While Ethical Eye provides valuable insights and analysis, it is essential to note that it should be used as an aid and not as the sole determinant of ethical decision-making. It may have limitations in understanding context-specific nuances and may require continuous improvement and customization for specific domains or languages.

## Model Details
- Architecture: Ethical Eye is built using PyTorch and utilizes the Transformers library. It employs the XLM-Roberta architecture, which enables cross-lingual understanding and transfer learning.
-  Developed by: [Khush Patel](https://www.linkedin.com/in/khush-patel-kp/), [Jayveersinh Raj](https://www.linkedin.com/in/jayveersinh-raj-67694222a/)
- License: The Ethical Eye model is released under the Apache 2.0 license, granting users the freedom to use, modify, and distribute the model according to the terms of the license.

## Use Cases
- Content Moderation: Ethical Eye can be integrated into content moderation systems to automatically flag and block user-generated content that contains abusive language, hate speech, or other forms of harmful or unethical behavior. It helps platforms maintain a safe and respectful environment for their users.

- Social Media Platforms: Social media platforms can utilize Ethical Eye to automatically detect and filter out toxic comments, obscenities, and offensive content in multiple languages. This helps to create a more positive and inclusive online community.

- Chatbots and Virtual Assistants: By incorporating Ethical Eye into chatbots and virtual assistants, AI systems can ensure that their responses align with ethical guidelines. It helps prevent AI agents from engaging in inappropriate or offensive conversations with users.

- Online Forums and Discussion Boards: Ethical Eye can be applied to online forums and discussion boards to monitor user interactions and identify potential instances of harassment, bullying, or unethical behavior. This allows moderators to take appropriate actions to maintain a healthy and respectful environment.

- E-commerce Platforms: E-commerce platforms can utilize Ethical Eye to automatically identify and block reviews or comments that contain false information, spam, or unethical practices. This helps maintain the integrity of the platform and ensures honest and reliable user feedback.

- Educational Platforms: Ethical Eye can be used in educational platforms to flag and address instances of cyberbullying, inappropriate language, or offensive content in student discussions and comments. It supports the creation of a safe and respectful learning environment.

- AI Reinforcement Learning: The Ethical Eye model can serve as a critic in reinforcement learning scenarios, providing feedback on the ethical implications of actions taken by AI agents. It assists in developing AI systems that not only optimize for task performance but also align with ethical guidelines and societal norms.

## Considerations for Deployment
- Hardware Requirements: The Ethical Eye model can be deployed on hardware configurations suitable for running deep learning models. Specific requirements may depend on the scale of deployment and the desired performance.
- Dependencies: The model relies on PyTorch, Transformers, and XLM-Roberta libraries. Refer to the model documentation for specific version requirements.
- Integration: Ethical Eye can be integrated into existing AI systems and platforms using the provided APIs and guidelines. Additional customization may be necessary to adapt the model to specific requirements.
- Ethical and Legal Considerations: While Ethical Eye aims to promote ethical behavior, it is important to acknowledge that it may have limitations and biases inherent in its training data. Developers should exercise caution and consider the legal and ethical implications of relying solely on the model's outputs without human oversight.