---
language:
- en
- fr
- es
- de
- pt
- it
- tr
- vi
- id
- ru
- el
- he
- ar
- fa
- hi
- bn
- th
- zh
- ja
- ko
license: cc-by-sa-3.0
task_categories:
- question-answering
task_ids:
- open-domain-qa
multilinguality: multilingual
size_categories:
- 100K<n<1M
pretty_name: PPQA - Paraphrased Parallel QA
tags:
- multilingual
- paraphrase
- evaluation
- short-answer
---

# PPQA: Paraphrased Parallel Question Answering

A multilingual short-answer QA dataset for easy evaluation: every question exists in
20 languages spanning 9 writing systems (Latin, Cyrillic, Greek, Hebrew, Arabic,
Devanagari, Bengali, Thai, CJK), each with **1-8 paraphrases per language**, and
answers are single words / short entities.

## Structure

- `dataset_full.jsonl` - one row per question:
  `{id, source, answers_en, languages: {lang: {question, answer, paraphrases: [...]}}}`
  A row is included only when all 20 languages are present.
- `eval_flat.jsonl` - one row per question form (question + each paraphrase):
  `{id, source, lang, form, text, answer}` - flatten and eval directly.
- `partial_results.jsonl` - every successful (question, language) generation
  (includes questions missing some languages).
- `failures.jsonl` - tasks rejected by validation, with reasons.
- `token_stats.json` - per-language answer token-length stats (Qwen3 tokenizer).

## Sources and generation

- Questions/answers harvested from [apple/mkqa](https://huggingface.co/datasets/apple/mkqa)
  (CC BY-SA 3.0, human-translated, 13 languages), [google/xquad](https://huggingface.co/datasets/google/xquad)
  (CC BY-SA 4.0, adds Greek and Hindi) and [mandarjoshi/trivia_qa](https://huggingface.co/datasets/mandarjoshi/trivia_qa)
  (English trivia, research use) - then filtered to short entity answers.
- Missing languages and ALL paraphrases generated with Qwen/Qwen3-32B-AWQ (vLLM,
  JSON structured outputs, thinking disabled), validated for script coverage,
  answer length (<=3 words) and numeric consistency.
- Generated rows carry the same license terms as their source question.

## Evaluation notes

- Answers are short entities; `token_stats.json` reports what fraction of answers
  are exactly 1 Qwen token per language - use it to build strict single-token
  subsets if needed. Non-Latin scripts tokenize longer.
- Match answers case-insensitively and against `answers_en` aliases for English.
