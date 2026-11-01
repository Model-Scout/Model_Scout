---
language:
  - ko
license: gpl-3.0
datasets:
  - KSL-LEX
tags:
  - sign-language
  - korean-sign-language
  - lexical-database
  - linguistics
---

# Dataset Card for KSL-LEX

## Dataset Details

### Dataset Description

KSL-LEX is a publicly available lexical database of Korean Sign Language (KSL), inspired by the ASL-LEX project (American Sign Language Lexical Database). It is based on the Korean Sign Language Dictionary's everyday signs collection, which contains 3,669 signs, but has been expanded to include more detailed linguistic information, resulting in 6,463 entries (6,289 unique headwords).

The primary purpose of KSL-LEX is to serve as a foundational resource for effectively supporting the linguistic needs of Korean Deaf individuals and sign language users. By providing detailed linguistic information including part-of-speech data (which was not available in the original Korean Sign Language Dictionary), KSL-LEX aims to facilitate research, education, and technology development that can enhance communication accessibility for the Korean Deaf community.

*   **Curated by:** Hyun W. Ka, Inseo Chung, Jaeyun Kim; Assistive AI Lab, KAIST
*   **Shared by:** Assistive AI Lab, KAIST (http://aailab.kaist.ac.kr)
*   **Language(s):** Korean Sign Language (KSL)
*   **License:** GPL (GNU General Public License)

### Dataset Sources

*   **Repository:** Based on the Korean Sign Language Dictionary (국립국어원 한국수어사전) everyday signs collection
*   **Original Source:** https://sldict.korean.go.kr/front/sign/signList.do?top_category=CTE

## Uses

### Direct Use

KSL-LEX can be used for:
- Linguistic research on Korean Sign Language
- Development of sign language processing technologies and assistive tools
- Educational resources for KSL learners, teachers, and interpreters
- Comparative studies between different sign languages
- Sign language recognition and generation systems
- Supporting the development of AI-based communication tools for Deaf individuals
- Enhancing accessibility in digital content for Korean Sign Language users

### Out-of-Scope Use

This dataset should not be used to:
- Make generalizations about all Korean Sign Language users without considering regional and individual variations
- Develop applications that aim to replace human sign language interpreters
- Create systems that might misrepresent Korean Sign Language
- Implement technologies without consulting the Deaf community

## Dataset Structure

The KSL-LEX dataset is structured as a CSV file with the following columns:
- **Headword**: The Korean word/phrase
- **POS**: Part of speech (added through research, not present in the original dictionary)
- **Same_Sign_Words**: Related words that use the same sign
- **Additional_Info**: Additional linguistic information
- **Homonym_Info**: Information about homonyms

The dataset contains 6,463 entries, representing 6,289 unique headwords. This expansion from the original 3,669 signs in the Korean Sign Language Dictionary is due to:

1. **Part-of-speech distinctions**: Through additional research, part-of-speech information was added to each entry, which was not available in the original dictionary. This resulted in some headwords appearing multiple times with different parts of speech.
2. **Homonym differentiation**: The same sign may have multiple meanings, which are recorded as separate entries.
3. **Linguistic expansion**: Following the ASL-LEX model, entries were expanded to include more detailed linguistic information to support research and technological applications.
4. **Related word inclusion**: Words that share the same sign are explicitly documented to provide a more comprehensive understanding of sign usage.

## Dataset Creation

### Curation Rationale

KSL-LEX was created to provide a comprehensive lexical database for Korean Sign Language, similar to what ASL-LEX offers for American Sign Language. The goal was to expand upon the existing Korean Sign Language Dictionary by adding more detailed linguistic information, particularly part-of-speech data, and structuring the data in a way that facilitates computational linguistics research and sign language technology development.

The project aims to serve as a foundational resource for effectively supporting the linguistic needs of Korean Deaf individuals and sign language users, contributing to improved accessibility and communication tools.

### Source Data

#### Data Collection and Processing

The base data was collected from the Korean Sign Language Dictionary's everyday signs collection, which contains 3,669 signs. This data was then expanded and restructured to follow a format inspired by ASL-LEX, resulting in 6,463 entries that provide more detailed linguistic information.

The expansion process involved:
1. Adding part-of-speech information through research (not present in the original dictionary)
2. Separating entries by part of speech
3. Identifying and marking homonyms
4. Including related words that use the same sign
5. Adding additional linguistic information

While extensive research was conducted to ensure accuracy, there remains some possibility of errors in the part-of-speech assignments, as this information was not provided in the original dictionary and required additional linguistic analysis.

#### Who are the source data producers?

The original source data comes from the Korean Sign Language Dictionary (국립국어원 한국수어사전) created by the National Institute of Korean Language (국립국어원). The KSL-LEX adaptation, expansion, and addition of part-of-speech information was performed by Hyun W. Ka at the Assistive AI Lab, KAIST.

## Bias, Risks, and Limitations

As with any language resource, KSL-LEX may not capture the full diversity of Korean Sign Language as used across different regions and communities. The dataset is based on the standardized version of KSL as documented by the National Institute of Korean Language, and may not reflect all regional variations or evolving usage.

Additionally, since the part-of-speech information was added through research and was not present in the original dictionary, there is a possibility of some inaccuracies in these linguistic annotations.

### Recommendations

Users of this dataset should:
- Recognize that KSL, like all languages, is diverse and evolving
- Consult with native KSL users and the Deaf community when developing applications based on this dataset
- Consider regional and demographic variations in KSL usage
- Be aware of the potential for errors in part-of-speech assignments
- Use this resource as a starting point rather than a definitive representation of KSL
- Involve Deaf individuals in the development and evaluation of any technologies based on this dataset
- Contribute to the ongoing improvement of the dataset by providing feedback on any identified issues

## Citation

**BibTeX:**
```
@dataset{ka2025ksl,
  author       = {Ka, Hyun W.},
  title        = {KSL-LEX: A Lexical Database of Korean Sign Language},
  month        = {April},
  year         = {2025},
  publisher    = {Assistive AI Lab, KAIST},
  howpublished = {http://aailab.kaist.ac.kr}
}
```

**APA:**
```
Ka, H. W. (2025, April). KSL-LEX: A Lexical Database of Korean Sign Language. Assistive AI Lab, KAIST. http://aailab.kaist.ac.kr
```

## Glossary

- **KSL**: Korean Sign Language
- **ASL-LEX**: American Sign Language Lexical Database, a project that inspired KSL-LEX
- **Headword**: The main word or phrase that is being defined or described
- **POS**: Part of speech (noun, verb, adjective, etc.)
- **Homonym**: Words that share the same spelling and pronunciation but have different meanings
- **Same Sign Words**: Different words that use the same sign in Korean Sign Language

## Dataset Card Authors

Hyun W. Ka, Assistive AI Lab, KAIST

## Dataset Card Contact

Hyun W. Ka, Assistive AI Lab, KAIST (hyun.ka@kaist.ac.kr)
Website: http://aailab.kaist.ac.kr
