
---

license: llama3.2
language:
- zh
- en
- it
- de
- fr
- ja
- ko
base_model:
- meta-llama/Llama-3.2-3B
- lianghsun/Llama-3.2-Taiwan-3B
datasets:
- lianghsun/tw-emergency-medicine-bench
- lianghsun/tw-legal-nlp
- lianghsun/tw-legal-synthetic-qa
- lianghsun/tw-law-article-qa
- lianghsun/tw-judgment-qa
- lianghsun/tw-judgment-gist-chat
- lianghsun/tw-bar-examination-2020-chat
- lianghsun/tw-structured-law-article
- lianghsun/tw-judgment-gist-chat
- lianghsun/tw-contract-review-chat
- lianghsun/reasoning-base-20k-chat
- lianghsun/vulnerability-mitigation-qa-zh_tw
- lianghsun/tw-instruct
- rombodawg/Everything_Instruct_Multilingual
- xzuyn/manythings-translations-alpaca
- neural-bridge/rag-dataset-12000
- minyichen/glaive_toolcall_zh_tw
pipeline_tag: text-generation
library_name: transformers
tags:
- Taiwan
- ROC
- zh-tw
- instruct
- chat
- llama3.2
- SLM
model-index:
- name: Llama-3.2-Taiwan-3B-Instruct
  results:
  - task:
      type: text-generation
      name: Single Choice Question
    dataset:
      type: lianghsun/tw-legal-benchmark-v1
      name: tw-legal-benchmark-v1
    metrics:
    - name: single choice
      type: accuracy
      value: 31.1
  - task:
      type: text-generation
      name: Single Choice Question
    dataset:
      type: lianghsun/Formosa-bench
      name: (Society) Formosa Taiwan Knowledge Bench
      config: society
      split: test
      revision: v2024.11.27
    metrics:
    - name: single choice
      type: accuracy
      value: 60.42
  - task:
      type: text-generation
      name: Single Choice Question
    dataset:
      type: lianghsun/Formosa-bench
      name: (Governmnt) Formosa Taiwan Knowledge Bench
      config: governmnt
      split: test
      revision: v2024.11.27
    metrics:
    - name: single choice
      type: accuracy
      value: 44.25
  - task:
      type: text-generation
      name: Single Choice Question
    dataset:
      type: lianghsun/Formosa-bench
      name: (Geography) Formosa Taiwan Knowledge Bench
      config: geography
      split: test
      revision: v2024.11.27
    metrics:
    - name: single choice
      type: accuracy
      value: 47.54
  - task:
      type: text-generation
      name: Single Choice Question
    dataset:
      type: lianghsun/Formosa-bench
      name: (History) Formosa Taiwan Knowledge Bench
      config: history
      split: test
      revision: v2024.11.27
    metrics:
    - name: single choice
      type: accuracy
      value: 60
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (geography_of_taiwan) tmmlu++
      config: geography_of_taiwan
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 36.2
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (dentistry) tmmlu++
      config: dentistry
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 33.83
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (technical) tmmlu++
      config: technical
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 35.07
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (statistics_and_machine_learning) tmmlu++
      config: statistics_and_machine_learning
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 28.57
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (clinical_psychology) tmmlu++
      config: clinical_psychology
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 29.6
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (tve_design) tmmlu++
      config: tve_design
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 38.54
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (three_principles_of_people) tmmlu++
      config: three_principles_of_people
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 48.2
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (introduction_to_law) tmmlu++
      config: introduction_to_law
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 29.96
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (linear_algebra) tmmlu++
      config: linear_algebra
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 21.43
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (agriculture) tmmlu++
      config: agriculture
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 24.5
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (jce_humanities) tmmlu++
      config: jce_humanities
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 38.89
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (music) tmmlu++
      config: music
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.9
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (secondary_physics) tmmlu++
      config: secondary_physics
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 33.04
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (physics) tmmlu++
      config: physics
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.84
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (advance_chemistry) tmmlu++
      config: advance_chemistry
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.64
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (junior_science_exam) tmmlu++
      config: junior_science_exam
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.05
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (veterinary_pathology) tmmlu++
      config: veterinary_pathology
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.09
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (financial_analysis) tmmlu++
      config: financial_analysis
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.13
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (national_protection) tmmlu++
      config: national_protection
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 42.65
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (macroeconomics) tmmlu++
      config: macroeconomics
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 26.76
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (politic_science) tmmlu++
      config: politic_science
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.44
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (ttqav2) tmmlu++
      config: ttqav2
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 61.06
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (junior_chinese_exam) tmmlu++
      config: junior_chinese_exam
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.86
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (traditional_chinese_medicine_clinical_medicine) tmmlu++
      config: traditional_chinese_medicine_clinical_medicine
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.9
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (junior_math_exam) tmmlu++
      config: junior_math_exam
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 21.71
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (auditing) tmmlu++
      config: auditing
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 21.82
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (anti_money_laundering) tmmlu++
      config: anti_money_laundering
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 37.31
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (pharmacology) tmmlu++
      config: pharmacology
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.68
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (trust_practice) tmmlu++
      config: trust_practice
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 28.18
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (tve_mathematics) tmmlu++
      config: tve_mathematics
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 18.67
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (human_behavior) tmmlu++
      config: human_behavior
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 32.04
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (pharmacy) tmmlu++
      config: pharmacy
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 22.76
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (tve_chinese_language) tmmlu++
      config: tve_chinese_language
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 36.65
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (optometry) tmmlu++
      config: optometry
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.11
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (physical_education) tmmlu++
      config: physical_education
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.73
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (organic_chemistry) tmmlu++
      config: organic_chemistry
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 35.78
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (tve_natural_sciences) tmmlu++
      config: tve_natural_sciences
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 33.73
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (education) tmmlu++
      config: education
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 37.9
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (mechanical) tmmlu++
      config: mechanical
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 42.37
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (taiwanese_hokkien) tmmlu++
      config: taiwanese_hokkien
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 14.73
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (nautical_science) tmmlu++
      config: nautical_science
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.49
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (business_management) tmmlu++
      config: business_management
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 39.57
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (logic_reasoning) tmmlu++
      config: logic_reasoning
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.34
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (marketing_management) tmmlu++
      config: marketing_management
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 39.78
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (economics) tmmlu++
      config: economics
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.95
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (basic_medical_science) tmmlu++
      config: basic_medical_science
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 28.41
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (occupational_therapy_for_psychological_disorders) tmmlu++
      config: occupational_therapy_for_psychological_disorders
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 35.73
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (general_principles_of_law) tmmlu++
      config: general_principles_of_law
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 31.13
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (junior_chemistry) tmmlu++
      config: junior_chemistry
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 24.88
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (veterinary_pharmacology) tmmlu++
      config: veterinary_pharmacology
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 36.3
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (educational_psychology) tmmlu++
      config: educational_psychology
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 33.52
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (finance_banking) tmmlu++
      config: finance_banking
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 32.59
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (official_document_management) tmmlu++
      config: official_document_management
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 32.43
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (fire_science) tmmlu++
      config: fire_science
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 30.65
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (junior_social_studies) tmmlu++
      config: junior_social_studies
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 47.62
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (accounting) tmmlu++
      config: accounting
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 20.94
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (engineering_math) tmmlu++
      config: engineering_math
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.18
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (education_(profession_level)) tmmlu++
      config: education_(profession_level)
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 24.07
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (chinese_language_and_literature) tmmlu++
      config: chinese_language_and_literature
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.64
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (management_accounting) tmmlu++
      config: management_accounting
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 24.19
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (culinary_skills) tmmlu++
      config: culinary_skills
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 39.38
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (administrative_law) tmmlu++
      config: administrative_law
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 25.71
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (insurance_studies) tmmlu++
      config: insurance_studies
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 33.42
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (real_estate) tmmlu++
      config: real_estate
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 22.83
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (computer_science) tmmlu++
      config: computer_science
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 31.61
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (taxation) tmmlu++
      config: taxation
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 27.47
  - task:
      type: question-answering
      name: Single Choice Question
    dataset:
      type: ikala/tmmluplus
      name: (trade) tmmlu++
      config: trade
      split: test
      revision: c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
    metrics:
    - name: single choice
      type: accuracy
      value: 20.32
widget:
- text: 中華民國憲法第一條
metrics:
- accuracy

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF
This is quantized version of [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) created using llama.cpp

# Original Model Card


# Model Card for lianghsun/Llama-3.2-Taiwan-3B-Instruct

<!-- Provide a quick summary of what the model is/does. -->
<a href="https://discord.gg/fj6WbHMvfs" target="_blank">[Discord]</a>

![image/png](https://cdn-uploads.huggingface.co/production/uploads/618dc56cbc345ca7bf95f3cd/v_cfMxTtVE6_eh0rzcy5L.png)
*圖像生成來自 [OpenArt](https://openart.ai/home)：An anime-style 🦙 standing proudly atop the summit of Taiwan’s [Yushan (Jade Mountain)](https://zh.wikipedia.org/wiki/%E7%8E%89%E5%B1%B1), gazing forward.*

採用 [lianghsun/Llama-3.2-Taiwan-3B](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B) 為[基礎模型（foundation model）](https://en.wikipedia.org/wiki/Foundation_model)，使用大量[中華民國台灣](https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3)的繁體中文對話集和多國語言對話集進行模型[指令微調（instruction fine-tuning）](https://www.ibm.com/topics/instruction-tuning)和多輪迭代[直接偏好優化（direct preference optimization, DPO）](https://arxiv.org/abs/2305.18290)，旨在訓練出具有中華民國台灣知識及風格的[小語言模型（small langugae model, SLM）](https://www.ibm.com/think/topics/small-language-models)之對話模型。

<details>
  <summary><b>Model Change Log</b></summary>
  
  | Update Date  | Model Version         | Key Changes                         |
  |--------------|-----------------------|-------------------------------------|
  | 2025/01/01   | v2025.01.01           | Fine-tuning is based on the [foundation model](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B) version v2024.12.28, and it uses self-prepared instruction datasets for this round of fine-tuning. |
  | 2024/12/13   | v2024.12.13           | Completed 1st round DPO training (10/10 epochs). Preparing for next round DPO training. |
  | 2024/11/27   | v2024.11.27           | Completed SFT training (5/5 epochs). Preparing for multi-round DPO training. |
  | 2024/11/25   | v2024.11.25           | Updated model version to v2024.11.25, training progressed to (3/5) epochs. Still in SFT stage, DPO training remains pending. |
  | 2024/11/22   | v2024.11.22           | Initial upload: Model version v2024.11.22, training completed up to (1/5) epochs. Currently trained only on SFT, DPO training not yet performed. |
  
</details>

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
- **Developed by:** [Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang)
- **Model type:** LlamaForCausalLM
- **Language(s) (NLP):** Tranditional Chinese (zh-tw), English
- **License:** [llama3.2](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/LICENSE.txt)
- **Fine-tuned from model:** [lianghsun/Llama-3.2-Taiwan-3B](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B)

### Model Sources

<!-- Provide the basic links for the model. -->
- **Repository:** [lianghsun/Llama-3.2-Taiwan-3B](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B)
- **Paper:** (WIP, show me the time)
- **Playground:** [🦉 Tawian SmolLM Chat](https://huggingface.co/spaces/lianghsun/tw-smol-chat) 👈🏼 來玩看看 😻
- **Demo:** 
```yaml
user: 請介紹台灣
assistant: 台灣，位於亞洲東部，地處太平洋與菲律賓海之間，面積約36,000平方公里，人口約2,300萬，是民主自由的國家，經濟實力強勁，擁有世界第10大經濟體。台灣以美食、文化、自然美景著稱，還有豐富的歷史與傳統，吸引全球遊客。台灣語為官方語言，但中文也廣為使用，英語也常用於國際交流。台灣政治多元，執政黨為民進黨，台灣是全球科技產業的重鎮，擁有先進的製造業與服務業。台灣氣候溫暖潮濕，四季分明，夏季炎熱，冬季涼爽，雨季則在5月至10月。台灣的美食以小吃為主，如滷肉飯、珍珠
```

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
本模型已經具備有繁體中文對話能力，使用者可以直接部署推論端點使用。

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
若需強化模型在特定領域的知識，可透過微調進一步提升其性能與專業能力。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
本模型旨在提供資訊，不參與任何政治或法律問題的評斷或立場表達。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
語言模型的生成內容可能因訓練集的多樣性而帶有偏見、特定立場，或包含與事實不符的言論，請使用者務必在使用過程中仔細確認內容的準確性與中立性。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

要使用 [vLLM Docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) 來啟動此模型，您可以按照以下操作：
```bash
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model lianghsun/Llama-3.2-Taiwan-3B-Instruct
```

請注意，如果想要使用不同版本的 checkpoint，請加上 `--revision <tag_name>` 
```bash
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=<secret>" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model lianghsun/Llama-3.2-Taiwan-3B-Instruct --revision <tag_name>
```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

<details>
  <summary><b>繁體中文對話資料集</b></summary>
  
  - [lianghsun/tw-legal-nlp](https://huggingface.co/datasets/lianghsun/tw-legal-nlp)
  - [lianghsun/tw-legal-synthetic-qa](https://huggingface.co/datasets/lianghsun/tw-legal-synthetic-qa)
  - [lianghsun/tw-law-article-qa](https://huggingface.co/datasets/lianghsun/tw-law-article-qa)
  - [lianghsun/tw-judgment-qa](https://huggingface.co/datasets/lianghsun/tw-judgment-qa)
  - [lianghsun/tw-bar-examination-2020-chat](https://huggingface.co/datasets/lianghsun/tw-bar-examination-2020-chat)
  - [lianghsun/tw-structured-law-article](https://huggingface.co/datasets/lianghsun/tw-structured-law-article)
  - [lianghsun/tw-judgment-gist-chat](https://huggingface.co/datasets/lianghsun/tw-judgment-gist-chat)
  - [lianghsun/vulnerability-mitigation-qa-zh_tw](https://huggingface.co/datasets/lianghsun/vulnerability-mitigation-qa-zh_tw)
  - [lianghsun/tw-legal-qa-chat](https://huggingface.co/datasets/lianghsun/tw-legal-qa-chat)
  - [lianghsun/reasoning-base-20k-chat](https://huggingface.co/datasets/lianghsun/reasoning-base-20k-chat)
  - [lianghsun/tw-contract-review-chat](https://huggingface.co/datasets/lianghsun/tw-contract-review-chat)
  - [lianghsun/tw-legal-methodology-chat](https://huggingface.co/datasets/lianghsun/tw-legal-methodology-chat)
  - [minyichen/glaive_toolcall_zh_tw](https://huggingface.co/datasets/minyichen/glaive_toolcall_zh_tw)
  
</details>

<details>
  <summary><b>多國語系對話資料集</b></summary>
  
  - [rombodawg/Everything_Instruct_Multilingual](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual)
  - [xzuyn/manythings-translations-alpaca](https://huggingface.co/datasets/xzuyn/manythings-translations-alpaca)
  - [neural-bridge/rag-dataset-12000](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000)

</details>

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing

(WIP)

#### Training Hyperparameters

<details>
  <summary><b>SFT stage for v2024.11.27</b></summary>

  **Note:** 以下包含 `v2024.11.22` 和 `v2025.11.25` 的超參數設定
  - **learning_rate:** 5e-05
  - **min_learning_rate:** 5e-07
  - **train_batch_size:** 105
  - **seed:** 42
  - **distributed_type:** multi-GPU
  - **num_devices:** 4
  - **gradient_accumulation_steps:** 50
  - **total_train_batch_size:** 21,000
  - **optimizer:** Adam with betas=(0.9,0.999) and epsilon=1e-08
  - **lr_scheduler_type:** cosine
  - **lr_scheduler_warmup_ratio:** 0.01
  - **num_epochs:** 5.0
  - **global_step:** 590
</details>

#### Speeds, Sizes, Times

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->
<details>
  <summary><b>SFT stage for v2024.11.27</b></summary>

  **Note:** 以下包含 `v2024.11.22` 和 `v2025.11.25` 的超參數設定
  - **Duration**: 5 days, 16:15:11.17
  - **Train runtime**: 490,511.1789
  - **Train samples per second**: 25.37
  - **Train steps per second**: 0.001
  - **Total training FLOPs**: 26,658,386,120,540,160
  - **Train loss**: 0.8533
</details>

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

<details>
  <summary><b>Formosa Taiwan Knowledge Bench</b></summary>
  
  #### Testing Data
  
  <!-- This should link to a Dataset Card if possible. -->
  
  [lianghsun/Formosa-bench](https://huggingface.co/datasets/lianghsun/Formosa-bench)
  
  #### Factors
  
  <!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->
  
  [More Information Needed]
  
  #### Metrics
  
  <!-- These are the evaluation metrics being used, ideally with a description of why. -->
  
  [More Information Needed]
  
  ### Results
  
  [More Information Needed]
  
  #### Summary

</details>

<details>
  <summary><b>lianghsun/tw-legal-benchmark-v1</b></summary>
  
  #### Testing Data
  
  <!-- This should link to a Dataset Card if possible. -->
  
  - **Dataset:** [lianghsun/tw-legal-benchmark-v1](https://huggingface.co/datasets/lianghsun/tw-legal-benchmark-v1)
  - **Revision:** 66c3a5f3ff2298f6a1cf23201070b5317bdd1893
  
  #### Factors
  
  <!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->
  
  [More Information Needed]
  
  #### Metrics
  
  <!-- These are the evaluation metrics being used, ideally with a description of why. -->
  Accuracy
  
  ### Results

  - **Model Revision:** v2024.11.27
  
  | **Subset** | **Split** | **Score** |
  |--------------|-------|-------|
  | [lianghsun/tw-legal-benchmark-v1](https://huggingface.co/datasets/lianghsun/tw-legal-benchmark-v1/blob/main/benchmark.csv) | train | 31.1 |
  
  #### Summary

</details>

<details>
  <summary><b>tmmlu++</b></summary>
  
  #### Testing Data
  
  <!-- This should link to a Dataset Card if possible. -->
  - **Dataset:** [ikala/tmmluplus](https://huggingface.co/datasets/ikala/tmmluplus)
  - **Revision:** c0e8ae955997300d5dbf0e382bf0ba5115f85e8c
  
  #### Factors
  
  <!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->
  [More Information Needed]
  
  #### Metrics
  
  <!-- These are the evaluation metrics being used, ideally with a description of why. -->
  Accuracy
  
  ### Results

  - **Model Revision:** v2024.11.27
  
  | **Subset** | **Split** | **Score** |
  |--------------|-------|-------|
  | [geography_of_taiwan](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/geography_of_taiwan_test.csv) | test | 36.2 |
  | [dentistry](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/dentistry_test.csv) | test | 33.83 |
  | [technical](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/technical_test.csv) | test | 35.07 |
  | [statistics_and_machine_learning](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/statistics_and_machine_learning_test.csv) | test | 28.57 |
  | [clinical_psychology](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/clinical_psychology_test.csv) | test | 29.6 |
  | [tve_design](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/tve_design_test.csv) | test | 38.54 |
  | [three_principles_of_people](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/three_principles_of_people_test.csv) | test | 48.2 |
  | [introduction_to_law](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/introduction_to_law_test.csv) | test | 29.96 |
  | [linear_algebra](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/linear_algebra_test.csv) | test | 21.43 |
  | [agriculture](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/agriculture_test.csv) | test | 24.5 |
  | [jce_humanities](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/jce_humanities_test.csv) | test | 38.89 |
  | [music](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/music_test.csv) | test | 25.9 |
  | [secondary_physics](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/secondary_physics_test.csv) | test | 33.04 |
  | [physics](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/physics_test.csv) | test | 27.84 |
  | [advance_chemistry](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/advance_chemistry_test.csv) | test | 27.64 |
  | [junior_science_exam](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/junior_science_exam_test.csv) | test | 30.05 |
  | [veterinary_pathology](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/veterinary_pathology_test.csv) | test | 25.09 |
  | [financial_analysis](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/financial_analysis_test.csv) | test | 25.13 |
  | [national_protection](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/national_protection_test.csv) | test | 42.65 |
  | [macroeconomics](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/macroeconomics_test.csv) | test | 26.76 |
  | [politic_science](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/politic_science_test.csv) | test | 27.44 |
  | [ttqav2](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/ttqav2_test.csv) | test | 61.06 |
  | [junior_chinese_exam](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/junior_chinese_exam_test.csv) | test | 30.86 |
  | [traditional_chinese_medicine_clinical_medicine](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/traditional_chinese_medicine_clinical_medicine_test.csv) | test | 25.9 |
  | [junior_math_exam](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/junior_math_exam_test.csv) | test | 21.71 |
  | [auditing](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/auditing_test.csv) | test | 21.82 |
  | [anti_money_laundering](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/anti_money_laundering_test.csv) | test | 37.31 |
  | [pharmacology](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/pharmacology_test.csv) | test | 30.68 |
  | [trust_practice](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/trust_practice_test.csv) | test | 28.18 |
  | [tve_mathematics](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/tve_mathematics_test.csv) | test | 18.67 |
  | [human_behavior](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/human_behavior_test.csv) | test | 32.04 |
  | [pharmacy](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/pharmacy_test.csv) | test | 22.76 |
  | [tve_chinese_language](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/tve_chinese_language_test.csv) | test | 36.65 |
  | [optometry](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/optometry_test.csv) | test | 25.11 |
  | [physical_education](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/physical_education_test.csv) | test | 30.73 |
  | [organic_chemistry](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/organic_chemistry_test.csv) | test | 35.78 |
  | [tve_natural_sciences](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/tve_natural_sciences_test.csv) | test | 33.73 |
  | [education](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/education_test.csv) | test | 37.9 |
  | [mechanical](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/mechanical_test.csv) | test | 42.37 |
  | [taiwanese_hokkien](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/taiwanese_hokkien_test.csv) | test | 14.73 |
  | [nautical_science](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/nautical_science_test.csv) | test | 30.49 |
  | [business_management](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/business_management_test.csv) | test | 39.57 |
  | [logic_reasoning](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/logic_reasoning_test.csv) | test | 27.34 |
  | [marketing_management](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/marketing_management_test.csv) | test | 39.78 |
  | [economics](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/economics_test.csv) | test | 25.95 |
  | [basic_medical_science](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/basic_medical_science_test.csv) | test | 28.41 |
  | [occupational_therapy_for_psychological_disorders](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/occupational_therapy_for_psychological_disorders_test.csv) | test | 35.73 |
  | [general_principles_of_law](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/general_principles_of_law_test.csv) | test | 31.13 |
  | [junior_chemistry](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/junior_chemistry_test.csv) | test | 24.88 |
  | [veterinary_pharmacology](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/veterinary_pharmacology_test.csv) | test | 36.3 |
  | [educational_psychology](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/educational_psychology_test.csv) | test | 33.52 |
  | [finance_banking](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/finance_banking_test.csv) | test | 32.59 |
  | [official_document_management](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/official_document_management_test.csv) | test | 32.43 |
  | [fire_science](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/fire_science_test.csv) | test | 30.65 |
  | [junior_social_studies](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/junior_social_studies_test.csv) | test | 47.62 |
  | [accounting](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/accounting_test.csv) | test | 20.94 |
  | [engineering_math](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/engineering_math_test.csv) | test | 27.18 |
  | [education_(profession_level)](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/education_(profession_level)_test.csv) | test | 24.07 |
  | [chinese_language_and_literature](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/chinese_language_and_literature_test.csv) | test | 27.64 |
  | [management_accounting](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/management_accounting_test.csv) | test | 24.19 |
  | [culinary_skills](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/culinary_skills_test.csv) | test | 39.38 |
  | [administrative_law](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/administrative_law_test.csv) | test | 25.71 |
  | [insurance_studies](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/insurance_studies_test.csv) | test | 33.42 |
  | [real_estate](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/real_estate_test.csv) | test | 22.83 |
  | [computer_science](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/computer_science_test.csv) | test | 31.61 |
  | [taxation](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/taxation_test.csv) | test | 27.47 |
  | [trade](https://huggingface.co/datasets/ikala/tmmluplus/blob/main/data/trade_test.csv) | test | 20.32 |

  
  #### Summary
  模型版號 `v2024.11.27`，無論是基礎模型（[lianghsun/Llama-3.2-Taiwan-3B](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B)）還是指令微調模型（[lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct)），均未接受過 tmmlu++ 資料集的訓練，以確保測試的公平性。經測試，目前該模型在 tmmlu++ 上表現普遍不佳，未達及格分數，可能需要加入專業領域的資料集來強化基礎模型能力。

</details>

## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->
- **Hardware Type:** 🚀
- **Hours used:** ⏳⏳⌛
- **Cloud Provider:** [鴻鵠國際股份有限公司](https://www.honghutech.com/)
- **Compute Region:** 🇹🇼
- **Carbon Emitted:** ♻️

## Technical Specifications

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

- **CPU count:** 32  
- **Logical CPU count:** 64  
- **GPU count:** 4  
- **GPU type:** NVIDIA H100 NVL  

#### Software

- **OS version:** Linux-5.15.0-124-generic-x86_64-with-glibc2.35  
- **Python version:** 3.12.7

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{lianghsun2024llama32taiwan3binstruct,
  author = {Huang, Liang Hsun},
  title = {Llama-3.2-Taiwan-3B-Instruct},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct}},
  note = {Accessed: 2024-11-25}
}
```

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->
N/A

## More Information

### Acknowledge
![image/png](https://cdn-uploads.huggingface.co/production/uploads/618dc56cbc345ca7bf95f3cd/28u7rOLoeUgn67clYEKuZ.png)
在此致謝[鴻鵠國際股份有限公司](https://www.honghutech.com/)蔡長明先生無償地贊助算力，以及曾經幫忙過：廖振翔、chweng、Ben、kevin、Maxxchu、Lam 和陳林彥…等朋友們，才能讓這個模型得以訓練完成，提供算力者乃人生父母。

### Usage
如果你基於此指令模型進行微調，希望能不吝嗇在 **模型卡片(model card)** 裡標註 **基礎模型** 為：
```yaml
base_model: lianghsun/Llama-3.2-Taiwan-3B-Instruct
```

標註和 ❤️ 是給予我們最大的鼓勵，謝謝。😀

## Model Card Authors

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang)

## Model Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang)

### Framework versions

- Transformers 4.45.2
- Pytorch 2.4.1+cu121
- Datasets 2.21.0
- Tokenizers 0.20.0

