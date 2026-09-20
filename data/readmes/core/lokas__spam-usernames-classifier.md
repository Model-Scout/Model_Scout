---
language:
- multilingual
- af
- sq
- ar
- an
- hy
- ast
- az
- ba
- eu
- bar
- be
- bn
- inc
- bs
- br
- bg
- my
- ca
- ceb
- ce
- zh
- cv
- hr
- cs
- da
- nl
- en
- et
- fi
- fr
- gl
- ka
- de
- el
- gu
- ht
- he
- hi
- hu
- is
- io
- id
- ga
- it
- ja
- jv
- kn
- kk
- ky
- ko
- la
- lv
- lt
- roa
- nds
- lm
- mk
- mg
- ms
- ml
- mr
- mn
- min
- ne
- new
- nb
- nn
- oc
- fa
- pms
- pl
- pt
- pa
- ro
- ru
- sco
- sr
- hr
- scn
- sk
- sl
- aze
- es
- su
- sw
- sv
- tl
- tg
- th
- ta
- tt
- te
- tr
- uk
- ud
- uz
- vi
- vo
- war
- cy
- fry
- pnb
- yo
license: apache-2.0
metrics:
- accuracy
pipeline_tag: text-classification
---
## Username Classification Model 👤🔍

This is a machine learning model that can classify usernames into two categories: spam and non-spam. The model is based on the bert-base-multilingual-cased model. The input to the model is a string representing a username, and the output is a probability distribution over the two categories.

## Dataset 📊

The model was trained on a dataset of usernames that were manually labeled as spam or non-spam. The dataset contains approximately 50,000 usernames, with a roughly equal number of examples in each category.

## Performance 🏆

The model achieved an accuracy of 82% on the test set, and has been shown to generalize well to new data. However, as with any machine learning model, its performance may vary depending on the specific characteristics of the data.



## Usage 🚀
To use this model, you can load it from Hugging Face using the Transformers library. Here is an example of how to do this:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("lokas/spam-usernames-classifier")
model = AutoModelForSequenceClassification.from_pretrained("lokas/spam-usernames-classifier")

# Example usernames
usernames = ["Yousef10166", "توفيق الشارني", "Eng.salman1", "Moulay nadjem ALLOUAOUI", "Mmaarwa111", "Abdouflih99", "loka"]

# Tokenize the usernames
inputs = tokenizer(usernames, return_tensors="pt", padding=True, truncation=True)

# Get the model's predictions
outputs = model(**inputs)

# The predictions are in the form of logits, so we need to apply the softmax function to convert them to probabilities
probs = outputs.logits.softmax(dim=-1)

# Print the probabilities
print(probs)
```
This example uses the dataset provided in the comment as an example. The usernames are classified as spam or non-spam.

## License 📝

This project is licensed under the MIT License. See the LICENSE file for more details.

