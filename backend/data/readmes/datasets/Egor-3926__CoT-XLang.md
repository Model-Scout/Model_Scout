---
license: mit
task_categories:
  - text-generation
  - question-answering
language:
  - ru
  - en
  - ja
  - ko
  - id
  - vi
  - zh
  - it
  - es
  - th
tags:
  - cot
  - o1
size_categories:
  - 10M<n<100M
configs:
  - config_name: Japanese
    data_files:
      - split: train
        path: "finaly/Japanese/*"
  - config_name: Korean
    data_files:
      - split: train
        path: "finaly/Korean/*"
  - config_name: Russian
    data_files:
      - split: train
        path: "finaly/Russian/*"
  - config_name: Math_en
    data_files:
      - split: train
        path: "finaly/Math_en/*"
  - config_name: Indonesian
    data_files:
      - split: train
        path: "finaly/Indonesian/*"
  - config_name: Vietnamese_English
    data_files:
      - split: train
        path: "finaly/Vietnamese+English/*"
  - config_name: Code_en
    data_files:
      - split: train
        path: "finaly/Code_en/*"
  - config_name: Italian
    data_files:
      - split: train
        path: "finaly/Italian/*"
  - config_name: Spanish
    data_files:
      - split: train
        path: "finaly/Spanish/*"
  - config_name: Thai
    data_files:
      - split: train
        path: "finaly/Thai/*"
  - config_name: Chinese_English
    data_files:
      - split: train
        path: "finaly/Chinese+English/*"
  - config_name: English
    data_files:
      - split: train
        path: "finaly/English/*"
---

**RU:**  
**CoT-XLang** — это многоязычный датасет, состоящий из текстовых примеров с пошаговыми рассуждениями (Chain-of-Thought, CoT) на различных языках, включая английский, русский, японский и другие. Он используется для обучения и тестирования моделей в задачах, требующих пояснений решений через несколько шагов. Датасет включает около 2,419,912 примеров, что позволяет эффективно обучать модели, способные генерировать пошаговые рассуждения.

**Рекомендация:**  
Используйте датасет для обучения моделей, обеспечивая многоязычную поддержку и акцент на пошаговые объяснения, что улучшит интерпретируемость решений.

---

**EN:**  
**CoT-XLang** is a multilingual dataset consisting of text examples with chain-of-thought (CoT) reasoning in multiple languages, including English, Russian, Japanese, and others. It is used for training and evaluating models in tasks that require step-by-step explanations. The dataset includes around 2,419,912 examples, making it effective for training models capable of generating detailed reasoning.

**Recommendation:**  
Utilize the dataset for training models, ensuring multilingual support and focusing on step-by-step explanations to improve interpretability of decisions.
