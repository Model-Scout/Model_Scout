---
license: cc-by-sa-4.0
task_categories:
- summarization
- question-answering
- text-generation
- text2text-generation
language:
- af
- ar
- az
- bn
- cs
- de
- en
- es
- et
- fa
- fi
- fr
- ga
- gl
- gu
- he
- hi
- hr
- id
- it
- ja
- ka
- kk
- km
- ko
- lt
- lv
- mk
- ml
- mn
- mr
- my
- ne
- nl
- pl
- ps
- pt
- ro
- ru
- si
- sl
- sv
- ta
- th
- tr
- uk
- ur
- vi
- xh
- zh
pretty_name: MegaWika
size_categories:
- 10M<n<100M
---
# Dataset Card for MegaWika

## Dataset Description

- **Homepage:** [HuggingFace](https://huggingface.co/datasets/hltcoe/megawika)
- **Repository:** [HuggingFace](https://huggingface.co/datasets/hltcoe/megawika)
- **Paper:** [Coming soon]
- **Leaderboard:** [Coming soon]
- **Point of Contact:** [Samuel Barham](samuel.barham@jhuapl.edu)

### Dataset Summary

MegaWika is a multi- and crosslingual text dataset containing 30 million Wikipedia passages with their scraped and cleaned web citations. The passages span
50 Wikipedias in 50 languages, and the articles in which the passages were originally embedded are included for convenience. Where a Wikipedia passage is in a
non-English language, an automated English translation is provided. Furthermore, nearly 130 million English question/answer pairs were extracted from the
passages, and FrameNet events occurring in the passages are detected using the [LOME](https://aclanthology.org/2021.eacl-demos.19.pdf) FrameNet parser.


<!---
To get a feel for the dataset -- its structure, content, strengths and weaknesses -- you may visit the [dataset viewer](https://huggingface.co/spaces/hltcoe/megawika)
we have set up as a HuggingFace Space. It allows the curious visitor to explore a small set of examples spread across a number of the dataset's constituent languages.
-->

### Dataset Creation

The pipeline through which MegaWika was created is complex, and is described in more detail in the paper (linked above),
but the following diagram illustrates the basic approach.

![Illustration of MegaWikaProcess](images/MegaWikaProcess-cross-lingual.drawio.png)

### Supported Tasks and Leaderboards

MegaWika is meant to support research across a variety of tasks, including report generation, summarization, information retrieval, question answering, etc.

### Languages

MegaWika is divided by Wikipedia language. There are 50 languages, including English, each designated by their 2-character ISO language code:
- `af`: Afrikaans
- `ar`: Arabic
- `az`: Azeri (Azerbaijani)
- `bn`: Bengali
- `cs`: Czech
- `de`: German (Deutsch)
- `en`: English
- `es`: Spanish (Español)
- `et`: Estonian
- `fa`: Farsi (Persian)
- `fi`: Finnish
- `fr`: French
- `ga`: Irish (Gaelic)
- `gl`: Galician
- `gu`: Gujarati
- `he`: Hebrew
- `hi`: Hindi
- `hr`: Hungarian
- `id`: Indonesian
- `it`: Italian
- `ja`: Japanese
- `ka`: Georgian (Kartvelian/Kartlian)
- `kk`: Kazakh
- `km`: Khmer
- `ko`: Korean
- `lt`: Lithuanian
- `lv`: Latvian
- `mk`: Macedonian (Makedonski)
- `ml`: Malay (Malayalam)
- `mn`: Mongolian
- `mr`: Marathi
- `my`: Burmese (Myanmar language)
- `ne`: Nepali
- `nl`: Dutch (Nederlands)
- `pl`: Polish
- `ps`: Pashto
- `pt`: Portuguese
- `ro`: Romanian
- `ru`: Russian
- `si`: Sinhalese (Sri Lankan language)
- `sl`: Slovenian
- `sv`: Swedish (Svenska)
- `ta`: Tamil
- `th`: Thai
- `tr`: Turkish
- `uk`: Ukrainian
- `ur`: Urdu
- `vi`: Vietnamese
- `xh`: Xhosa
- `zh`: Chinese (Zhōng wén)

## Dataset Structure

The dataset is divided by language, and the data for each of the 50 languages is further chunked into discrete JSON lines files.
Each line of these files -- we'll call such a line an **instance** -- contains the data extracted from a single Wikipedia article.

### Data Instances

Each instance contains the text of the seed Wikipedia article, along with a list of **entries**. Each entry consists basically in
an extracted Wikipedia passage, the URL and scraped text of the web source it cites, a list of questions/answer pairs extracted from the passage,
and a framenet parse of the passage. Where the passage is from a non-English Wikipedia, a machine translation into English is also provided.

### Data Fields

The detailed structure of an instance is as follows:
```
{
  "article_title": <string : title of original Wikipedia article>
  "article_text": <string : text of Wikipedia article>
  "entries": [
    # Wiki Passage
    "id": <string : passage ID>
    "passage": {
      "text": <string : text of passage in English (possibly via MT)>
      "parse": <list of dict : FrameNet parse of English passage text>
      "en_tokens": <dict : tokenization of passage in English>
      "lang_tokens": <dict : tokenization of original non-English passage>
      "en_lang_token_map": <dict : alignment mapping between English and original language token indices>
    }

    # MT
    "original": <string : original language passage>
    "original_sents": <list of string : sentencized original language passage>
    "translation": <string : machine translation of passage>
    "translation_sents": <list of string : sentencized machine translation of passage>
    "translation_probs": <list of float : log prob of machine translation by sentence, where available>
    "repetitious_translation": <string \in ("true", "false") : automated judgment on whether machine translation is pathologically repetitious>
    "source_lang": <string : language ID, 2-character ISO code>

    # Source
    "source_url": <string : URL of the cited web source>
    "source_text": <string : content extracted from the scrape of the source URL>

    # Question/Answer Pairs
    "qa_pairs": [
      ...
      {
        "question": <string : generated question>
        "passage_id": <string : passage ID>
        "en_answer": <string : English answer>
        "lang_answer": <string : aligned original language answer>
        "frames": [
          ...
          {
            "frame": <string : frame triggered by the question>
            "argument": <string : detected frame arguments>
          }
          ...
        ]
        # NB: answer matches can be empty, in the case no matching span exists
        "en_matches_in_source": <list of int : start and end index of the English language-answer token(s) in the source document>
        "en_match_in_passage": <list of int : start and end index of the English language-answer token(s) in the English language translation of the passage>
        "lang_matches_in_source": <list of int : start and end index of the original language-answer token(s) in the source document>
        "lang_match_in_passage": <list of int : start and end index of the original language-answer token(s) in the original language passage>
        "passage": <list of string : sentencized view of the passage>
        "en_answer_tokens": <list of string>
        "match_disambiguated_question": <string : disambiguated version of question obtained by matching pronouns with article title (noisy but often helpful)>
      }
      ...
    ]
  ]
}
```

English language instances differ not in structure but in content; 
1. Fields in the block labeled "MT" above are naturally null (that is, they are set to falsy values in Python -- specifically `None`)
2. Since the Wiki passage only exists in English, and has no corresponding non-English "original language" version, answer spans also necessarily have only an English-language version (and no non-English "original-language" version. Therefore, fields in the `qa_pairs` block beginning with `lang_` are set to null/falsy values in Python (in this case, empty lists).


### Data Splits

MegaWika is currently split only by language, as each task will imply its own approach to filtering, sampling, downselecting, and splitting into train/test splits.

<!---
### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]
-->

## Licensing and Takedown

MegaWika 1.0 consists in part of documents scraped from across the web (based on citations linked in Wikipedia articles.)

We do not own any of the scraped text nor do we claim copyright: text drawn from Wikipedia citations are meant for research use in algorithmic design and model training.

We release this dataset and all its contents under CC-BY-SA-4.0.

### Notice and Takedown Policy:
*NB*: Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:

- Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
- Clearly identify the copyrighted work claimed to be infringed.
- Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

And contact the authors.

*Take down*: We will comply to legitimate requests by removing the affected sources from the next release of the dataset.

## Additional Information

### Dataset Curators

Released and maintained by the Johns Hopkins University Human Language Technology Center of Excellence (JHU/HLTCOE). 
You can contact one the MegaWika authors, including [Samuel Barham](mailto:samuel.barham@jhuapl.edu), [Orion Weller](mailto:oweller2@jhu.edu),
and [Ben van Durme](mailto:vandurme@jhu.edu) with questions.

### Licensing Information

Released under the [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

### Citation Information

```
@misc{barham2023megawika,
      title={MegaWika: Millions of reports and their sources across 50 diverse languages}, 
      author={Samuel Barham and and  Weller and Michelle Yuan and Kenton Murray and Mahsa Yarmohammadi and Zhengping Jiang and Siddharth Vashishtha and Alexander Martin and Anqi Liu and Aaron Steven White and Jordan Boyd-Graber and Benjamin Van Durme},
      year={2023},
      eprint={2307.07049},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<!--
### Contributions

[More Information Needed]
-->
