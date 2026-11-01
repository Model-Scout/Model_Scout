---
license: apache-2.0
configs:
- config_name: direct
  data_files:
  - split: occupations
    path: "data/occupations_direct-00000-of-00001.csv"
  - split: adjectives
    path: "data/adjectives-00000-of-00001.csv"
- config_name: indirect
  data_files: 
  - split: occupations
    path: "data/occupations_indirect-00000-of-00001.csv"
- config_name: feminine
  data_files: 
  - split: occupations
    path: "data/occupations_direct_feminine-00000-of-00001.csv"
- config_name: gender_star
  data_files: 
  - split: occupations
    path: "data/occupations_german_gender_star-00000-of-00001.csv"
task_categories:
- text-to-image
language:
- en
- de
- it
- fr
- es
- zh
- ja
- ko
- ru
- ar
size_categories:
- 1K<n<10K
---

# MAGBIG benchmark

This is the MAGBIG benchmark proposed in https://arxiv.org/abs/2401.16092

This benchmark is intended for multilingual text-to-image models. With MAGBIG, you can generate images for a diverse set of prompts across ten different languages. These images can be evaluated for differences across languages. MAGBIG is designed to uncover and assess biases across languages such as gender, race, age, etc. This way, we can measure whether bias exists in a language, but also whether it is consistent across languages or not. Yet, this benchmark can also be used to evaluate multilingual text-to-image models for their general ability across languages, e.g., image quality, versatility, etc.

It contains four sets of prompts in four files for English, German, Arabic, French, Italian, Spanish, Russian, Korean, Japanese, and Chinese:
1) adjective prompts (`adjectives.csv`) that use standard language
2) direct occupation prompts (`occupations_direct.csv`) that use standard language
3) direct feminine occupation prompts (`occupations_direct_feminine.csv`) that use the female version of nouns in standard language (if available for a language)
4) German gender star occupation prompts (`occupations_german_gender_star.csv`) that use gender-neutral star convention in German
5) indirect occupation prompts (`occupations_indirect.csv`) that use gender-neutral descriptions

You can also find our code available at https://github.com/felifri/MAGBIG

### Citation
If you like or use our work, please consider citing us.
```bibtex
@inproceedings{friedrich2025multilingual,
      title={Multilingual Text-to-Image Generation Magnifies Gender Stereotypes and Prompt Engineering May Not Help You}, 
      author={Felix Friedrich and Katharina Hämmerl and Patrick Schramowski and Manuel Brack and Jindrich Libovicky and Kristian Kersting and Alexander Fraser},
      year={2025},
      booktitle={In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL main 2025)},
}
```