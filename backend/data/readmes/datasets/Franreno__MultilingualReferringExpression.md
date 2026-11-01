---
language:
- en
- fr
- pt
- de
- nl
- ru
- ko
- it
- es
- zh
task_categories:
- object-detection
pretty_name: Multilingua Referring Expression
size_categories:
- 1M<n<10M
---

# Multilingual Referring Expression Dataset

A unified corpus of object-referent expressions in ten languages, created by consolidating twelve publicly available referring expression datasets into a consistent schema.

<img src="image_readme/example_1.png"></img>

## Composition

The dataset construction began with the collection of various referring expression corpora where English was the primary language. A total of 12 datasets were used:
- RefCOCO / RefCOCO+ / RefCOCOg
- RefClef
- RefOI
- RefDrone
- Finecops-Ref
- Toloka VQA
- Locate-Bench
- FG-OVD
- Multimodal Grounding
- WMT24 English-to-Low-Resource translation task

Each dataset was processed through a translation pipeline. English referring expressions were translated into nine target languages: German, French, Spanish, Portuguese, Italian, Russian, Chinese, Korean, and Dutch.

After translation, all datasets were standardized into a unified format to facilitate merging and ensure consistency across the corpus.



## Translation pipeline

To expand each English referring expression into nine additional languages an automated workflow was built. First, the model [Unbabel/TowerInstruct-7B-v0.2]() was used to translate each english sentence to the others.

Prompt used: 
```
Translate to \<Language>
English: \<english_text>
\<Language>:
```

Example of an translation result: 

**English:**  
Which one contains the person wearing a white shirt with his back turned?

| Language | Translation                                                                                   |
|----------|-----------------------------------------------------------------------------------------------|
| German    | Welche enthält die Person, die ein weißes Hemd trägt und sich mit dem Rücken zu uns wendet?   |
| French    | Quelle contient la personne qui porte une chemise blanche avec le dos tourné?                 |
| Chinese   | 哪张照片中的人身穿白色衬衫，且身背朝向相机？                                                         |
| Portuguese| Qual delas contém a pessoa vestida de branco com as costas viradas?                           |
| Dutch     | Welke foto bevat de persoon die een witte shirt draagt en met zijn rug naar de camera staat?  |
| Russian   | Какая из них содержит человека, одетого в белую рубашку, спину к нам обращенную?               |
| Korean    | 등을 돌린 채 흰색 셔츠를 입은 사람이 있는 사진은 어느 것인가요?                                       |
| Italian   | Quale contiene la persona che indossa una camicia bianca con la schiena rivolta?              |
| Spanish   | ¿Cuál contiene a la persona que lleva una camisa blanca con la espalda hacia atrás?            |


This automated translation pipeline was run for every dataset.
