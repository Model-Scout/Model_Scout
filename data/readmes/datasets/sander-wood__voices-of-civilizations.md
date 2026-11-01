---
license: mit
task_categories:
- question-answering
language:
- ar
- bn
- bg
- zh
- hr
- cs
- da
- nl
- en
- et
- fi
- fr
- de
- el
- iw
- hi
- hu
- id
- it
- ja
- ko
- lv
- lt
- no
- pl
- pt
- ro
- ru
- sr
- sk
- sl
- es
- sw
- sv
- th
- tr
- uk
- vi
tags:
- audio
- music
size_categories:
- n<1K
---

# Voices of Civilizations (VoC)

**Voices of Civilizations (VoC)** is the first multilingual QA benchmark designed to assess audio LLMs’ cultural comprehension using full-length music recordings. VoC spans:

- **38 languages** 🇸🇦 Arabic (ar), 🇧🇩 Bengali (bn), 🇧🇬 Bulgarian (bg), 🇨🇳 Chinese (zh), 🇭🇷 Croatian (hr), 🇨🇿 Czech (cs), 🇩🇰 Danish (da), 🇳🇱 Dutch (nl), 🇬🇧 English (en), 🇪🇪 Estonian (et), 🇫🇮 Finnish (fi), 🇫🇷 French (fr), 🇩🇪 German (de), 🇬🇷 Greek (el), 🇮🇱 Hebrew (iw), 🇮🇳 Hindi (hi), 🇭🇺 Hungarian (hu), 🇮🇩 Indonesian (id), 🇮🇹 Italian (it), 🇯🇵 Japanese (ja), 🇰🇷 Korean (ko), 🇱🇻 Latvian (lv), 🇱🇹 Lithuanian (lt), 🇳🇴 Norwegian (no), 🇵🇱 Polish (pl), 🇵🇹 Portuguese (pt), 🇷🇴 Romanian (ro), 🇷🇺 Russian (ru), 🇷🇸 Serbian (sr), 🇸🇰 Slovak (sk), 🇸🇮 Slovenian (sl), 🇪🇸 Spanish (es), 🇰🇪 Swahili (sw), 🇸🇪 Swedish (sv), 🇹🇭 Thai (th), 🇹🇷 Turkish (tr), 🇺🇦 Ukrainian (uk), 🇻🇳 Vietnamese (vi)
- **380 tracks** (10 tracks per language) drawn from traditional and regional music
- **1,190 multiple-choice questions** probing four dimensions: language, region, mood, and theme

VoC exposes models’ biases and weaknesses on under-represented musical traditions and fosters more inclusive audio understanding research.

## Record Structure

Each line in the JSONL files is a JSON object with the following fields:

- `language` (string): ISO 639-1 code of the song’s primary language
- `id` (string): YouTube video ID
- `title_native` (string): Native title of the song
- `title_transliteration` (string): Latin-script transliteration
- `title_translation` (string): English translation of the title
- `qa_language_native` / `qa_language_translation` (object): Question, answer, and distractors for language identification
- `qa_region_native` / `qa_region_translation` (object): Question, answer, and distractors for region association
- `qa_mood_native` / `qa_mood_translation` (object): Question, answer, and distractors for mood inference
- `qa_theme_native` / `qa_theme_translation` (object): Question, answer, and distractors for thematic content
- `document_native` (string): Cultural and historical context in the song’s native language
- `document_translation` (string): English translation of the context document

## Example Record

```json
{
  "language": "ko",
  "id": "5xGSngr275c",
  "title_native": "아리랑",
  "title_transliteration": "Arirang",
  "title_translation": "Arirang",
  "qa_language_native": {
    "question": "음악을 주의 깊게 듣고 노래가 주로 어떤 언어로 되어 있는지 확인하십시오.",
    "answer": "한국어",
    "distractors": ["영어", "체코어", "폴란드어"]
  },
  "qa_language_translation": {
    "question": "Please listen carefully to the music and determine which language the song is primarily in.",
    "answer": "Korean",
    "distractors": ["English", "Czech", "Polish"]
  },
  "qa_region_native": {
    "question": "음악을 주의 깊게 듣고 노래가 어느 지역 또는 문화적 전통과 가장 밀접하게 관련되어 있는지 확인하십시오.",
    "answer": "정선",
    "distractors": ["춘천", "대구", "광주"]
  },
  "qa_region_translation": {
    "question": "Please listen carefully to the music and determine which region or cultural tradition the song is most closely associated with.",
    "answer": "Jeongseon",
    "distractors": ["Chuncheon", "Daegu", "Gwangju"]
  },
  "qa_mood_native": {
    "question": "음악을 주의 깊게 듣고 노래가 암시하는 주된 분위기나 느낌을 파악하십시오.",
    "answer": "애절한",
    "distractors": ["구슬픈", "한스러운", "슬픈"]
  },
  "qa_mood_translation": {
    "question": "Please listen carefully to the music and determine the primary mood or atmosphere the song suggests.",
    "answer": "poignant",
    "distractors": ["sorrowful", "regretful", "melancholic"]
  },
  "qa_theme_native": {
    "question": "음악을 주의 깊게 듣고 노래가 암시할 가능성이 있는 주제를 파악하십시오.",
    "answer": "이별과 그리움, 사랑, 삶의 애환, 사회 비판, 통일의 염원",
    "distractors": ["사랑과 이별, 인생무상, 자연미, 사회적 불평등", "임에 대한 그리움, 인생허무, 삶의 고통, 가족애", "인생무상, 임에 대한 그리움, 이별의 아픔, 자연경관"]
  },
  "qa_theme_translation": {
    "question": "Please listen carefully to the music and determine the theme the song is likely suggesting.",
    "answer": "parting and longing, love, the joys and sorrows of life, social commentary, aspiration for reunification",
    "distractors": ["love and separation, the transience of life, natural beauty, social inequality", "longing for a loved one, the futility of life, the pain of existence, familial love", "transience of life, longing for a loved one, the pain of parting, natural scenery"]
  },
  "document_native": "아리랑은 한국의 가장 대표적인 민요로, 한민족의 정서와 역사를 대변하는 상징적인 노래이다. ...",
  "document_translation": "Arirang is the most representative folk song of Korea, a symbolic piece that embodies the emotions and history of the Korean people. ..."
}
```

## Citation
<!-- If you find this dataset useful, please consider citing us: -->
Coming Soon...