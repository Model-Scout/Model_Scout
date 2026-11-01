---
license: apache-2.0
language:
- ru
- en
- de
- 'no'
- ko
- zh
- ar
pretty_name: Chronos Thinking V1 (Mini)
task_categories:
- text-generation
tags:
- chain-of-thought
- reasoning
- unsloth
- qwen
- synthetic
- multilingual
size_categories:
- n<1K
---

# English:

# 🌌 Chronos-Thinking-v1-mini: The Genesis of Structured Reasoning

![Chronos Architecture](https://img.shields.io/badge/Architecture-ThinkFlow-blue?style=for-the-badge)
![Format](https://img.shields.io/badge/Format-JSONL-green?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-7-orange?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Chain_of_Thought-purple?style=for-the-badge)

**Chronos-Thinking-v1-mini** is a fundamental, high—density dataset designed to initialize deep reasoning processes in large language models (LLM). 

This dataset is the first step in the Chronos Super-AI project. Unlike mass datasets generated automatically, v1-mini relies on **absolute quality and density of knowledge**. He trains the model not just to answer questions, but to *think* like a system architect, using strict formal logic before generating the final answer.

---

# The Architecture of Thought

The main feature of the dataset is the implementation of a rigidly structured `<think>` block. The model is trained to deconstruct any task through 4 mandatory cognitive filters:

1. **`[DOMAIN]`**: Domain definition (for example, *Quantum Physics, System Administration, Combinatorics*). Allows the model to instantly load the required semantic context.
2. **`[ANALYSIS]`**: Deep analysis of the task. Identifying hidden patterns, dependencies, and optimal solutions.
3. **`[FORMALISM]`**: Mathematical or logical reasoning. Using formulas (LaTeX), laws of physics, or architectural code patterns.
4. **`[LIMITS]`**: Awareness of the limits of the applicability of the solution. Assessment of risks, edge cases, and physical limitations.

Only after passing through these four stages inside the `<think>` tag, the model generates a final, crystal-clear response.

---

## 🌍 Multi-Lingual Mastery

Logic is universal and does not depend on the language. The dataset is intentionally designed as multilingual in order to break the binding of complex concepts to English. The model learns to apply higher mathematics and programming in 7 languages:

* 🇷🇺 **English** (Russian)
* 🇬🇧 **English** (English)
* 🇩🇪 **German** (German)
* 🇳🇴 **Norwegian** (Norwegian)
* 🇰🇷 **Korean** (Korean)
* 🇨🇳 **Chinese** (Chinese)
* 🇸🇦 **Arabic** (Arab)

---

## 📂 Dataset Structure

The dataset is presented in the `JSONL` (JSON Lines) format, ideal for Supervised Fine-Tuning (SFT).

### Schema
``json
{
"instruction": "string", // Incoming request, task or problem
  "response": "string" // Structured thinking process + final response
}
``

### Example Entry
```json
{
  "instruction": "Find the root of the equation 8x − 6 = 16x",
  "response": "<think>\n[DOMAIN]: Algebra / Linear Equations\n[ANALYSIS]: The objective is to isolate the variable x by performing inverse operations on the linear equation 8x - 6 = 16x.\n[FORMALISM]: \n1. Start with 8x - 6 = 16x.\n2. Subtract 8x from both sides: -6 = 16x - 8x.\n3. Simplify the right side: -6 = 8x.\n4. Solve for x: x = -6/8.\n5. Reduce the fraction: x = -3/4 or -0.75.\n[LIMITATIONS]: This is a first-degree polynomial equation in one variable, which typically yields a single unique solution in the field of real numbers.\n</think>\nTo find the root of the equation 8x - 6 = 16x, we follow these logical steps:\n\n1. **Group the terms containing the variable**: We move 8x to the right side of the equation to collect all x terms together. This is done by subtracting 8x from both sides:\n-6 = 16x - 8x\n\n2. **Simplify the expression**: Perform the subtraction on the right side:\n-6 = 8x\n\n3. **Isolate the variable**: To solve for x, divide both sides of the equation by the coefficient 8:\nx = -6/8\n\n4. **Final Reduction**: Simplify the fraction by dividing both the numerator and the denominator by their greatest common divisor, which is 2:\nx = -3/4\n\nIn decimal form, the root is x = -0.75."
}
```

---

## 🚀 Intended Use & Training

This dataset is optimized for use with the **Unsloth** library and the **QLoRA** methodology. It is ideal for further training of the **Qwen (2.5 and 3.5/3.6)**, Llama 3/3.1 and Mistral family models.

### Quick Start with `datasets`
```python
from datasets import load_dataset

# Uploading a dataset
dataset = load_dataset("kweezi/Chronos-Thinking-v1-mini", split="train")

# Viewing the first example
print(dataset[0]["instruction"])
print(dataset[0]["response"])
```

### Training Prompt Template (ChatML)
For best results with SFT, wrap the data in ChatML format:
```text
<|im_start|>system
You are Chronos Prime, a self-evolving AI Architect. Always reason deeply inside <think> tags before answering.<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
{response}<|im_end|>
```

---


## 🔮 Vision: The Path to Singularity

**Chronos-Thinking-v1-mini** is a mini version of the dataset, then there will also be:
*   **v1-full:** A full-fledged dataset with 10,000+ examples with a focus on system programming (C++, Rust) and quantum physics.
*   **v1-medium:** A small dataset of about 1,000 examples, which includes many topics in different languages, from coding to philosophy

*Built for the future. Engineered by Kernel Zone Media Team.*
---

# Russian:

# 🌌 Chronos-Thinking-v1-mini: The Genesis of Structured Reasoning

![Chronos Architecture](https://img.shields.io/badge/Architecture-ThinkFlow-blue?style=for-the-badge)
![Format](https://img.shields.io/badge/Format-JSONL-green?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-7-orange?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Chain_of_Thought-purple?style=for-the-badge)

**Chronos-Thinking-v1-mini** — это фундаментальный, высокоплотный датасет, созданный для инициализации процессов глубокого рассуждения (Deep Reasoning) у больших языковых моделей (LLM). 

Этот набор данных является первым шагом в проекте **Chronos Super-AI**. В отличие от массовых датасетов, сгенерированных автоматически, `v1-mini` делает ставку на **абсолютное качество и плотность знаний**. Он обучает модель не просто отвечать на вопросы, а *мыслить* как системный архитектор, используя строгую формальную логику перед генерацией финального ответа.

---

## 🧠 The Architecture of Thought (Архитектура Мышления)

Главная особенность датасета — внедрение жестко структурированного блока `<think>`. Модель обучается деконструировать любую задачу через 4 обязательных когнитивных фильтра:

1. **`[DOMAIN]`**: Определение предметной области (например, *Quantum Physics, System Administration, Combinatorics*). Позволяет модели мгновенно подгрузить нужный семантический контекст.
2. **`[ANALYSIS]`**: Глубокий разбор задачи. Выявление скрытых паттернов, зависимостей и оптимальных путей решения.
3. **`[FORMALISM]`**: Математическое или логическое обоснование. Использование формул (LaTeX), законов физики или архитектурных паттернов кода.
4. **`[LIMITATIONS]`**: Осознание границ применимости решения. Оценка рисков, краевых случаев и физических ограничений.

Только после прохождения этих четырех этапов внутри тега `<think>`, модель генерирует финальный, кристально чистый ответ.

---

## 🌍 Multi-Lingual Mastery

Логика универсальна и не зависит от языка. Датасет намеренно спроектирован как мультиязычный, чтобы разорвать привязку сложных концепций к английскому языку. Модель учится применять высшую математику и программирование на 7 языках:

*   🇷🇺 **Russian** (Русский)
*   🇬🇧 **English** (Английский)
*   🇩🇪 **German** (Немецкий)
*   🇳🇴 **Norwegian** (Норвежский)
*   🇰🇷 **Korean** (Корейский)
*   🇨🇳 **Chinese** (Китайский)
*   🇸🇦 **Arabic** (Арабский)

---

## 📂 Dataset Structure

Датасет представлен в формате `JSONL` (JSON Lines), идеально подходящем для Supervised Fine-Tuning (SFT).

### Schema
```json
{
  "instruction": "string", // Входящий запрос, задача или проблема
  "response": "string"     // Структурированный процесс мышления + финальный ответ
}
```

### Example Entry
```json
{
  "instruction": "Find the root of the equation 8x − 6 = 16x",
  "response": "<think>\n[DOMAIN]: Algebra / Linear Equations\n[ANALYSIS]: The objective is to isolate the variable x by performing inverse operations on the linear equation 8x - 6 = 16x.\n[FORMALISM]: \n1. Start with 8x - 6 = 16x.\n2. Subtract 8x from both sides: -6 = 16x - 8x.\n3. Simplify the right side: -6 = 8x.\n4. Solve for x: x = -6/8.\n5. Reduce the fraction: x = -3/4 or -0.75.\n[LIMITATIONS]: This is a first-degree polynomial equation in one variable, which typically yields a single unique solution in the field of real numbers.\n</think>\nTo find the root of the equation 8x - 6 = 16x, we follow these logical steps:\n\n1. **Group the terms containing the variable**: We move 8x to the right side of the equation to collect all x terms together. This is done by subtracting 8x from both sides:\n-6 = 16x - 8x\n\n2. **Simplify the expression**: Perform the subtraction on the right side:\n-6 = 8x\n\n3. **Isolate the variable**: To solve for x, divide both sides of the equation by the coefficient 8:\nx = -6/8\n\n4. **Final Reduction**: Simplify the fraction by dividing both the numerator and the denominator by their greatest common divisor, which is 2:\nx = -3/4\n\nIn decimal form, the root is x = -0.75."
}
```

---

## 🚀 Intended Use & Training

Этот датасет оптимизирован для использования с библиотекой **Unsloth** и методологией **QLoRA**. Он идеально подходит для дообучения моделей семейства **Qwen (2.5 и 3.5/3.6)**, Llama 3/3.1 и Mistral.

### Quick Start with `datasets`
```python
from datasets import load_dataset

# Загрузка датасета
dataset = load_dataset("kweezi/Chronos-Thinking-v1-mini", split="train")

# Просмотр первого примера
print(dataset[0]["instruction"])
print(dataset[0]["response"])
```

### Training Prompt Template (ChatML)
Для достижения наилучших результатов при SFT, оборачивайте данные в формат ChatML:
```text
<|im_start|>system
You are Chronos Prime, a self-evolving AI Architect. Always reason deeply inside <think> tags before answering.<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
{response}<|im_end|>
```

---

## 🔮 Vision: The Path to Singularity

**Chronos-Thinking-v1-mini** — это мини версия датасета, далее так же будут:
*   **v1-full:** Полноценный датасет на 10,000+ примеров с фокусом на системное программирование (C++, Rust) и квантовую физику.
*   **v1-medium:** Небольшой датасет примерно на 1,000 примеров, включающий в себя множество тем на разных языках, от кодинга до философии

*Built for the future. Engineered by Kernel Zone Media Team.*