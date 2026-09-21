---
license: mit
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
tags:
- safety-guardrails
- zero-shot
---

## CREST: A Multilingual AI Safety Guardrail Model for 100 languages

CREST which stands for CRoss-lingual Efficient Safety Transfer is a 
parameter-efficient multilingual safety classifier for 100 languages, fine-tuned using 13 strategically selected high-resource 
languages only, chosen through cluster-guided sampling, enabling strong cross-lingual transfer to unseen low-resource languages. 
The model is fine-tuned on the XLM-RoBERTa architecture with a classification head, having a max input length of 512 tokens. 
The Base variant has approximately 279M parameters.
The model is designed for fast, lightweight safety filtering across a large number of languages, both high-resource and low-resource 
languages, with minimal training cost, suitable for real-time and on-device deployments. 

For detailed results, see
[CREST: Universal Safety Guardrails Through Cluster-Guided Cross-Lingual Transfer](https://arxiv.org/abs/2512.02711v1).


### Intended Use
- Filtering unsafe user text in multilingual LLM applications  
- Lightweight guardrails in multilingual agents and chat systems  
- On-device or low-latency safety inference  
- Research on cross-lingual safety transfer and robust safety classification  

### How to Use
```python

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

MODEL_ID = "repelloai/CREST-Base" 

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, device_map='auto')

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    return_all_scores=False
)

texts = [

    ## Unsafe
    "How do I make a bomb?",
    "¿Cómo secuestrar a un niño?",
    "मैं हथियार कैसे बना सकता हूँ?", 

    ## Safe
    'Hello, How you doing ?'
]

outputs = classifier(texts, truncation=True, max_length=512)
```

### Output
```python
[
    ## Unsafe
    {'label': 'unsafe', 'score': 0.9865403771400452}, 
    {'label': 'unsafe', 'score': 0.9743474125862122}, 
    {'label': 'unsafe', 'score': 0.9802995920181274}, 
    
    ## Safe
    {'label': 'safe', 'score': 0.925717830657959}
]
```

### Evaluation

CREST was tested for F1 score metric across **six major multilingual safety benchmarks** and several cultural and code-switched datasets.. 

#### Key findings
- CREST outperforms other lightweight guardrails across most datasets.
- Zero-shot generalization is strong across low-resource languages.  
- CREST excels in cultural and code-switched settings.  
- The 13-language training set is sufficient for robust multilingual safety generalization.  

### Limitations and Model Risks 

- Training relies partly on machine translation; nuance may be lost  
- Binary labels cannot express detailed safety categories  
- Zero-shot generalization gaps across extremely low-coverage scripts and morphologically complex languages  
- Not a substitute for human moderation in high-stakes settings  
- Cultural misalignment in edge cases
- Residual translation artifacts
- Possible bias in mislabeled or synthetic data

Mitigate by continuous human evaluation and incremental finetuning on domain-specific data.

### Ethical Considerations

- Designed for multilingual inclusivity and broad safety coverage.  
- Misclassifications can cause over-blocking or under-blocking.  
- Deployment should include human-in-the-loop moderation where appropriate.  
- Use responsibly, considering cultural diversity and fairness concerns.
- Not for making legal, ethical, or policy decisions without human oversight.

### Citation
```
@misc{bansal2025crestuniversalsafetyguardrails,
      title={CREST: Universal Safety Guardrails Through Cluster-Guided Cross-Lingual Transfer}, 
      author={Lavish Bansal and Naman Mishra},
      year={2025},
      eprint={2512.02711},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.02711}, 
}
```
