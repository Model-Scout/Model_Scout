---
language: 
  - en
  - ko

pretty_name: "KoDF"

task_categories:
  - other

# request form for accessing dataset
extra_gated_prompt: "You agree to not use the dataset to conduct experiments that cause harm to human subjects."

extra_gated_fields:
  Name: text
  Email: text
  Name of supervisor: text
  Email of supervisor: text
  Affiliation: text
  Country: country
  Specific date: date_picker
  Usage for dataset:
    type: select
    options: 
      - Research
      - label: Other
        value: other
  I agree to use this dataset for non-commercial use ONLY: checkbox
---

For the test of dataset