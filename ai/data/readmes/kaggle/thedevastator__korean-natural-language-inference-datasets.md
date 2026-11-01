# Korean Natural Language Inference 

Korean NLI Data: Premises, Hypotheses, and Labels

_____
# Korean Natural Language Inference 
### Korean NLI Data: Premises, Hypotheses, and Labels
By kor_nli (From Huggingface) [[source]](https://huggingface.co/datasets/kor_nli)
_____

### About this dataset
&gt; The Korean Natural Language Inference (NLI) datasets provided on Kaggle consist of premises, hypotheses, and corresponding labels for the purpose of natural language inference tasks. In NLI, the premise is defined as the first sentence or statement that serves as contextual information, while the hypothesis refers to the second sentence or statement that needs to be evaluated based on its relationship with the premise. The label in this dataset indicates whether there is an entailment, contradiction, or neutral relationship between the premise and hypothesis.
&gt; 
&gt; The training dataset snli_train.csv contains ample data to train a Korean NLI model, allowing for learning patterns and improving accuracy in predicting relationships between premises and hypotheses. For evaluation purposes, xnli_test.csv provides a separate test set containing premises, hypotheses, and labels. Similarly, xnli_validation.csv contains premises, hypotheses along with their respective labels for validation purposes.
&gt; 
&gt; With this comprehensive collection of datasets specifically designed for Korean NLI tasks available on Kaggle platform researchers can effectively develop models capable of classifying various relationships between natural language statements such as entailment (when hypothesis logically follows from premise), contradiction (when hypothesis negates premise), or neutrality (when there is no logical relationship between them). These datasets contribute significantly towards advancing research in natural language processing and understanding in the Korean language domain

### How to use the dataset
&gt; 
&gt; Introduction:
&gt; The Korean Natural Language Inference (NLI) datasets are a valuable resource for building and evaluating NLI models. These datasets consist of premises, hypotheses, and corresponding labels that indicate the relationship between the premise and hypothesis. This guide will provide you with an overview of how to effectively use this dataset for your NLI tasks.
&gt; 
&gt; - Understanding the Dataset Structure:
&gt;    - The dataset is available in three separate files: snli_train.csv, xnli_test.csv, and xnli_validation.csv.
&gt;    - Each file contains multiple columns, including premise, **premise**, hypothesis, **hypothesis**, label, **label**, premise, **premise**, hypothesis,**hypothesis**, label,**label**.
&gt;    - The columns marked with asterisks (*) are duplicates or repetitions of the original columns and can be ignored.
&gt; 
&gt; - Exploring Training Data (snli_train.csv):
&gt;    - The snli_train.csv file contains training data specifically designed for building an NLI model.
&gt;    - Each row represents a single instance with its corresponding premise, hypothesis, and label.
&gt;    - Use this data to train your NLI model by feeding it pairs of premises and hypotheses along with their associated labels.
&gt; 
&gt; - Evaluating Model Performance (xnli_test.csv & xnli_validation.csv):
&gt;    - The xnli_test.csv file provides premises, hypotheses, and labels specifically for evaluating your NLI model's performance on a test set.
&gt;    - Similarly,the xnli_validation.csv file offers premises,hypotheses,and labels specificfor assessingyourNLImodel on a validation set.
&gt;   *Note:* It's important to preserve these test sets throughout your experiments to avoid biased evaluation.
&gt; 
&gt; - Labels:
&gt;   The label column indicates the relationship between the given premise-hypothesis pair. There are three possible categories:
&gt; 
&gt;     i) Entailment: If the premise logically entails or implies the hypothesis.
&gt;     ii) Contradiction: If the premise contradicts or is logically incompatible with the hypothesis.
&gt;     iii) Neutral: If there is no clear logical relationship between the premise and hypothesis.
&gt; 
&gt; - Preprocessing Considerations:
&gt;   - Make sure to preprocess your text data, including tokenization, normalization, and any language-specific steps required for Korean NLI tasks.
&gt;   - It's recommended to remove any irrelevant columns or duplicate data before training your model for performance optimization.
&gt; 
&gt; Conclusion:

### Research Ideas
&gt; - Training a natural language inference model: This dataset can be used to train a Korean NLI model by using the premises and hypotheses as input, and the corresponding labels as target values.
&gt; - Evaluating model performance: The dataset can be used to evaluate the performance of a pre-trained Korean NLI model by comparing its predicted labels with the actual labels in the dataset.
&gt; - Research on cross-lingual transfer learning: Since this dataset is specifically designed for Korean NLI, it can be used in research related to cross-lingual transfer learning, where models trained on this dataset can be tested on other languages or datasets to assess their generalization ability

### Acknowledgements
&gt; If you use this dataset in your research, please credit the original authors.
&gt; [Data Source](https://huggingface.co/datasets/kor_nli)
&gt; 
&gt;


### License
&gt; 
&gt; 
&gt; **License: [CC0 1.0 Universal (CC0 1.0) - Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)**
&gt; No Copyright - You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. [See Other Information](https://creativecommons.org/publicdomain/zero/1.0/).

### Columns

**File: snli_train.csv**
| Column name    | Description                                                                                                                                                           |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **premise**    | The first sentence or statement that serves as the premise for natural language inference. (Text)                                                                     |
| **hypothesis** | The second sentence or statement referred to as the hypothesis in natural language inference. (Text)                                                                  |
| **label**      | The categorical column indicating the relationship between the premise and hypothesis, with categories including entailment, contradiction, or neutral. (Categorical) |

_____

**File: xnli_test.csv**
| Column name    | Description                                                                                                                                                           |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **premise**    | The first sentence or statement that serves as the premise for natural language inference. (Text)                                                                     |
| **hypothesis** | The second sentence or statement referred to as the hypothesis in natural language inference. (Text)                                                                  |
| **label**      | The categorical column indicating the relationship between the premise and hypothesis, with categories including entailment, contradiction, or neutral. (Categorical) |

_____

**File: xnli_validation.csv**
| Column name    | Description                                                                                                                                                           |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **premise**    | The first sentence or statement that serves as the premise for natural language inference. (Text)                                                                     |
| **hypothesis** | The second sentence or statement referred to as the hypothesis in natural language inference. (Text)                                                                  |
| **label**      | The categorical column indicating the relationship between the premise and hypothesis, with categories including entailment, contradiction, or neutral. (Categorical) |

### Acknowledgements
&gt; If you use this dataset in your research, please credit the original authors.
&gt; If you use this dataset in your research, please credit [kor_nli (From Huggingface)](https://huggingface.co/datasets/kor_nli).

출처: Kaggle (thedevastator/korean-natural-language-inference-datasets)
태그: languages, earth and nature, korea
라이선스: CC0: Public Domain
수정일: 2023-12-02T12:05:48.337Z
