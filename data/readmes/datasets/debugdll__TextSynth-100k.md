---
license: apache-2.0
language:
- ru
- en
- es
- fr
- de
- it
- pt
- zh
- ja
- ko
task_categories:
- image-to-text
- text-to-image
task_ids:
- image-captioning
tags:
- synthetic
- text
- multilingual
- image-captioning
- computer-vision
- ocr
- text-recognition
- generated
size_categories:
- 100K<n<1M
pretty_name: TextSynth-100k
---

# TextSynth-100k

A synthetic dataset for training image captioning and text recognition (OCR) models. 100,000 images with text in 10 languages, in different colors, fonts, and on different backgrounds.

## What's inside

- **100,000 images** sized 224×224, JPG format.
- **200 unique texts** in 10 languages.
- **30 text colors** and **12 background colors**.
- **Various Windows fonts**: Arial, Times New Roman, Courier New, Calibri, Cambria, Georgia, and others.
- **Different font sizes** — from 28 to 90 pt.
- **Text rotations**: 0°, ±15°, ±30°.
- **Captions** in the format: `the text <text> is written in <color> on a <background> background`.

## Languages

| Language | Example |
|----------|---------|
| Russian | привет, мир, кот, собака, дом |
| English | hello, world, cat, dog, house |
| Spanish | hola, mundo, gato, perro, casa |
| French | bonjour, monde, chat, chien, maison |
| German | hallo, welt, katze, hund, haus |
| Italian | ciao, mondo, gatto, cane, casa |
| Portuguese | olá, mundo, gato, cachorro, casa |
| Chinese | 你好, 世界, 猫, 狗, 房子 |
| Japanese | こんにちは, 世界, 猫, 犬, 家 |
| Korean | 안녕, 세계, 고양이, 개, 집 |

## Structure