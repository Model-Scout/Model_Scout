---
license: mit

language:
  - am
  - ar
  - bn
  - ca
  - cs
  - da
  - de
  - el
  - en
  - es
  - fa
  - fi
  - fr
  - gu
  - he
  - hi
  - hr
  - hu
  - id
  - it
  - ja
  - ka
  - kn
  - ko
  - ml
  - mr
  - ms
  - nb
  - nl
  - or
  - pa
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - sr
  - sv
  - ta
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - vi
  - zh

pretty_name: "Multilingual EU-14 Food Allergen Dataset"

task_categories:
  - text-classification

size_categories:
  - 100K<n<1M

tags:
  - multilingual
  - multi-label-classification
  - food
  - food-allergens
  - eu-14-allergens
  - allergen-detection
  - restaurant-menu
  - menu-items
  - food-safety
  - natural-language-processing
---
# Adisyonist Multilingual EU-14 Allergen Dataset

A multilingual dataset for predicting the **14 EU food allergens** from restaurant menu item text.

The dataset contains approximately **294,500 examples** consisting of menu item names and, where available, short menu descriptions.

It is designed for **multi-label text classification**, where a single menu item may contain zero, one, or multiple allergens.

---

## Dataset Structure

Each record contains only three fields:

- **`id`**: Unique identifier for the example.
- **`text`**: Menu item name, optionally followed by a short description.
- **`allergens`**: List of EU-14 allergen labels associated with the item.

### Example

```json
{"id":"example_001","text":"Spaghetti Carbonara. Pasta with egg, parmesan cheese and pancetta.","allergens":["gluten","eggs","milk"]}
```

---

## Allergen Labels

The dataset uses the following 14 canonical allergen labels:

```text
gluten
crustaceans
eggs
fish
peanuts
soy
milk
tree_nuts
celery
mustard
sesame
sulphites
lupin
molluscs
```

An empty list indicates that none of the 14 allergen classes are assigned to the example:

```json
{"id":"example_002","text":"Fresh Fruit Plate.","allergens":[]}
```

---

## Intended Use

This dataset is intended for training and evaluating multilingual models that predict food allergens from restaurant menu text.

Typical applications include:

- Multi-label allergen classification
- Restaurant menu analysis
- Food information systems
- Multilingual food NLP
- Allergen detection research

---

## Important Notice

Allergen labels represent dataset annotations and should not be treated as a substitute for verified ingredient, manufacturer, or restaurant allergen information.

Real recipes and preparation methods may vary.

---
### Author

Created by **Ömer Faruk ŞAHAN**  
Hugging Face: https://huggingface.co/omerfsahan
