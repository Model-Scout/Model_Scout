# Nano Banana 2.0: The Omni-Subject Dataset

1067 Ways Gemini Sees the World

# 🍌 Nano Banana 2.0: The Omni-Subject Dataset

![Dataset Size](https://img.shields.io/badge/Images-1067-yellow) ![Resolution](https://img.shields.io/badge/Resolution-1K-blue) ![Sectors](https://img.shields.io/badge/Sectors-109-green) ![Generator](https://img.shields.io/badge/Generator-Google%20Gemini-red) ![Format](https://img.shields.io/badge/Format-JPEG%20%7C%20PNG-lightgrey) ![License](https://img.shields.io/badge/License-GNUv3.0-orange)

---

## 📌 Overview

**Nano Banana 2.0: The Omni-Subject Dataset** is a fully synthetic, AI-generated image collection
containing **1,067 images at 1K resolution**, purpose-built for training and benchmarking
**AI-generated image detection models**.

Every single image in this dataset was generated using **Google Gemini's image generation
capabilities**. The dataset spans **109 unique visual sectors** across 7 major domain groups,
but the actual image content goes far beyond academic categories — including pop culture,
internet memes, fictional characters, historical figures, world cuisines, global geography,
video games, comics, and much more.

This is a **pure AI image collage dataset** — meaning it can be used as:
- The **positive class** (AI = 1) in a binary detection pipeline
- A **standalone generative fingerprint** study for Gemini specifically
- A **domain coverage benchmark** for synthetic image analysis
- A **pop culture and media representation** study for generative models

---

## 🤖 Generation Source

All 1,067 images were generated using:

> **Google Gemini Image Generation**
> Prompts were engineered across 109 sectors covering everything from scientific
> phenomena to internet memes, pop culture franchises, world geography, and
> historical reconstructions.

This dataset captures **Gemini-specific generative fingerprints**, including:
- Characteristic smoothness in skin and texture rendering
- Specific color saturation and gradient tendencies
- Edge transition and boundary behaviors
- Typography and hand rendering failure patterns
- Shadow and reflection inconsistencies
- Repeating texture and pattern artifacts
- Stylistic rendering of fictional and cartoon characters
- Geographic and cultural visual interpretation patterns

---

## 📊 Dataset Statistics

| Property | Value |
|---|---|
| Total Images | 1,067 |
| Resolution | 1K (1024×1024) |
| Sectors Covered | 109 |
| Domain Groups | 7 |
| Generation Source | Google Gemini |
| Real Images | None — fully synthetic |
| Format | JPEG / PNG (mixed) |
| Directory Structure | Single flat folder |
| Label | AI Generated (all positive class) |

---

## 📁 Folder Structure
```
Nano Banana 2.0 Dataset/
│
└── dataset/               # All 1,067 AI-generated images in one flat directory
    ├── anime_202603230031.jpeg
    ├── batman_Vs_Superman_202603230038.jpeg
    ├── biriyani_202603230123.jpeg
    ├── Esports_arena_during_202603222351.jpeg
    ├── Gemini_Generated_Image_*.png
    └── ... (1,067 total)
```

> All images are stored flat in a single directory with no subfolders.
> This is a straightforward collage of AI-generated images — no metadata
> files, no annotation files, and no label CSVs are included.
>
> Files come in two naming conventions:
> - **Descriptive names** — e.g. `Batman_Vs_Superman_202603230038.jpeg`
> - **Gemini default names** — e.g. `Gemini_Generated_Image_4cxs62....png`

---

## 🎬 What's Actually In This Dataset

Beyond the formal 109-sector taxonomy, a scan of the actual filenames
reveals an extraordinarily wide range of real-world content themes:

### 🦸 Pop Culture & Fiction
- DC Comics heroes and villains (`batman_Vs_Superman`, `DC_Comics`, `dc_comic_baddies`, `spider_man`)
- Marvel universe (`Comics_for_superhero`)
- Harry Potter (`harry_potter`)
- Lord of the Rings (`lord_of_the`)
- Transformers (`transformers`, `Transformers_electrical_engineering`)
- Pokémon (`Pokemon_3d_video`)
- Power Rangers (`power_rangeas_spd`)
- Teenage Mutant Ninja Turtles (`teenage_ninja_mutant`)
- Nickelodeon (`nickalodean`)
- Austin Powers (`autin_powers`)
- Skyrim (`skyrim`)
- Anime (`anime`)
- Video game graphics (`video_games_graphics`)

### 😂 Internet Culture & Memes
- General memes (`memes`, `cat_memes`, `dog_memes`, `fat_memes`, `skinny_memes`)
- Dog content (`doggo`, `more_dog_memes`)
- Kung fu cats (`kungfu_cats`)
- Viral internet formats

### 🌍 World Geography & Countries
- Africa (`africa`)
- Albania (`albenia`)
- Argentina (`argentia`)
- Australia (`austraila`)
- Brazil (`brazil`)
- Canada (`canada`)
- China (`china`)
- Germany (`germany`)
- Ireland (`ireland`)
- Kazakhstan (`Kazakhstan`)
- Korea (`korea`)
- Mexico (`mexico`)
- USA (`usa`)
- Sweet Home Alabama (`sweet_home_alabama`)

### 🍽️ International Cuisine
- Biryani (`biriyani`)
- Burger (`burger`)
- Chinese Buddha Jumps Over the Wall Soup (`Chinese_soup_Buddha`)
- Fish and Chips (`fish_and_chips`)
- Italy's Pizza (`Italys_pizza`)
- Jamaica Ackee (`Jamaica_-_Ackee`)
- Japan Sushi (`Japans_sushi`)
- Korea BBQ (`korean_barbique`)
- Mexico Tacos (`Mexicos_tacos`)
- Middle East Kebab (`Middle_East_Kebab`)
- Ramen (`ramen`)
- Shawarma (`swarma`)
- Tortilla (`tortia`)

### 🏛️ Historical Figures & Eras
- Albert Einstein (`einstine`)
- Marie Curie (`madam_curie`)
- Nikola Tesla (`nokola_tesla`)
- Stalin (`staline`)
- Rothschild (`rothschild`)
- Vikings (`vikings`)
- Samurai (`samurai`)
- Ninja (`ninja`)
- WWI (`ww1`)
- WWII (`ww2`)
- Ice Age (`iceage`)
- Dinosaurs (`dinasours`)

### 🐍 Wildlife & Nature
- Snakes (`snakes`, `huge_snakes`, `venomous_snakes`)
- Frog in rain (`Frog_in_rainy`)
- Various biological specimens

### ✍️ Written Language & Documents
- Handwritten letters in multiple languages (`letters_written_in`, `hand_written_letters`)
- Resumes (`resume`)
- Prescriptions (`prescription`)
- Report writing (`report_writing`)
- Multiple scripts and writing systems

### 🛰️ Technology & Modern Systems
- Satellite imagery (`satelite_images`)
- Military planes (`military_planes`)
- Google Maps style (`google_maps`)
- Air traffic control (`Air_traffic_control`)

### 🎓 Academic & Professional
- CSE Graduate (`a_cse_graduate`)
- Bad men archetypes (`bad_men`)
- Successful nation imagery (`a_sucessful_nation`)

### 📚 Decades & Eras (Retro)
- 1950s imagery (`50s_images`)
- 1960s imagery (`66s_images`)
- 1970s imagery (`70s_images`)
- 1980s imagery (`80s_images`)
- 1990s imagery (`90s_images`)

---

## 🗂️ Formal Sector Coverage

This dataset spans **109 unique visual sectors** organized into **7 major domain groups**:

---

### 01. Primary Subjects & Domains

| # | Sector |
|---|---|
| 1 | Portraits & Individuals |
| 2 | Sports & Athletic Performance |
| 3 | Natural Landscapes & Wilderness |
| 4 | Architecture & Urban Design |
| 5 | Wildlife & Animal Kingdom |
| 6 | Culinary Arts & Still Life |
| 7 | Human Anatomy & Biometrics |
| 8 | Typography & Textual Imagery |
| 9 | Hybrid Media & Edge Cases |

---

### 02. Environmental & Spatial Context

| # | Sector |
|---|---|
| 10 | Spatial Settings: Indoor vs. Outdoor |
| 11 | Scenic Environments & Biomes |
| 12 | Institutional & Commercial Venues |
| 13 | Global Geographic Regions |
| 14 | Meteorological & Visibility Factors |
| 15 | Chronological & Temporal Markers |
| 16 | Population & Crowd Density |
| 17 | Compositional Complexity |
| 18 | Cinematic Angles & Perspective |
| 19 | Lighting Dynamics & Illumination |
| 20 | Surface Textures & Tactile Detail |

---

### 03. Technical Precision & Quality

| # | Sector |
|---|---|
| 21 | Generative Synthesis Methods |
| 22 | Hardware & Lens Simulation |
| 23 | Digital Integrity & Noise Profile |
| 24 | Structural & Generative Anomalies |
| 25 | Typographic Clarity & Lettering |
| 26 | Anatomical & Biometric Accuracy |
| 27 | Optical Physics & Ray Tracing |
| 28 | Geometric & Perspective Logic |
| 29 | Chromatic & Aesthetic Profiles |
| 30 | Patterning & Repetition Artifacts |
| 31 | Semantic & Narrative Logic |
| 32 | Post-Processing & Digital Edits |

---

### 04. High-Energy & Surreal Dynamics

| # | Sector |
|---|---|
| 33 | Extreme Human Stunts |
| 34 | Surreal Everyday Scenarios |
| 35 | Absurdist Public Spectacles |
| 36 | Cultural Juxtapositions |
| 37 | Extraordinary Human Feats |
| 38 | Anthropomorphic Animal Life |
| 39 | Ecological & Animal Conflicts |
| 40 | Competitive Species Behavior |
| 41 | Emotive Animal Expressions |
| 42 | Physics-Defying Animal Traits |
| 43 | Cross-Species Interactions |

---

### 05. Industrial, Scientific & Global Systems

| # | Sector |
|---|---|
| 44 | Micro-Visualizations & Science |
| 45 | Urban Decay & Ruin |
| 46 | Manufacturing & Heavy Industry |
| 47 | Extreme Weather Phenomena |
| 48 | Research & Clinical Labs |
| 49 | Historical Visual Recreations |
| 50 | Celestial & Deep Space |
| 51 | Underground Counter-Cultures |
| 52 | Emergency Medical Response |
| 53 | Performing Arts Backstage |
| 54 | Subaquatic Exploration |
| 55 | Civil Engineering & Infrastructure |
| 56 | Atmospheric & Eerie Horror |
| 57 | Biological Organic Structures |
| 58 | High-Stakes Gaming & Casinos |
| 59 | Funerary Rites & Mortuary Science |
| 60 | Digital Esports Culture |
| 61 | Engineering & Physics Trials |
| 62 | Creative Fine Art Studios |
| 63 | Active Emergency Scenarios |
| 64 | Archaeology & Lost Civilizations |
| 65 | Clinical Psychology & Therapy |
| 66 | Rare Botanical Ethnobotany |
| 67 | Acoustic & Music Production |
| 68 | High-Intensity Aquatic Sports |
| 69 | Sacred Rituals & Spirituality |
| 70 | Dentistry & Surgical Science |
| 71 | Cold War & Military History |
| 72 | Modern Agro-Technology |
| 73 | Niche Hobbies & Puzzles |
| 74 | Textiles & Fashion Industry |
| 75 | Pandemic & Public Health |
| 76 | Tactical Operations & Defense |
| 77 | Polar & Arctic Expeditions |
| 78 | Acrobatics & Circus Arts |
| 79 | Global Finance & Markets |
| 80 | Toy Engineering & Design |
| 81 | Private Aerospace Ventures |
| 82 | Precision-Based Disciplines |
| 83 | Apiculture & Beekeeping |
| 84 | Cinematic Visual Effects |
| 85 | Body Modification & Fitness |
| 86 | Olfactory & Perfumery Arts |
| 87 | Horology & Micro-Mechanics |
| 88 | Hydrology & Resource Management |
| 89 | Heritage & Endangered Crafts |

---

### 06. Specialized Identities & Subcultures

| # | Sector |
|---|---|
| 90 | Frontier Life & Western Culture |
| 91 | Combat & Martial Arts |
| 92 | Professional Culinary Science |
| 93 | Survivalism & Solo Exploration |
| 94 | Mechanical & Engine Restoration |
| 95 | Urban Street Movements |
| 96 | Orchestral Performance |
| 97 | Subterranean Mining & Labor |
| 98 | Maritime & Seafaring Life |
| 99 | Street Performance & Busking |

---

### 07. Investigation, Media & Tradition

| # | Sector |
|---|---|
| 100 | Forensic & Crime Scene Science |
| 101 | Traditional Labor Archetypes |
| 102 | Memetics & Internet Lore |
| 103 | Global Sovereignty & Diversity |
| 104 | International Gastronomy |
| 105 | Sequential Art & Graphic Novels |
| 106 | Epistolary & Handwritten Arts |
| 107 | Multilingual Linguistic Diversity |
| 108 | Contemporary Youth Vernacular |
| 109 | Bibliographic & Library Archives |

---

## 🧠 What Makes This Dataset Unique

### ✅ Pure Synthetic — No Mixed Sources
Every image is AI-generated from Google Gemini with no real photographs included.
This makes it ideal as a clean positive class for binary detection training.

### ✅ Unusually Wide Content Range
Unlike most detection datasets that stick to naturalistic photography,
this dataset includes Gemini's rendering of:
- Copyrighted fictional characters and franchises
- Internet meme formats and viral content
- Historical figures and period reconstructions
- Retro decade aesthetics (50s through 90s)
- Multi-script handwritten documents
- Cartoon and anime styles
- Video game and CGI aesthetics

### ✅ Artifact-Aware Design
Every sector was chosen to expose specific Gemini generation weaknesses:
- **Hands & anatomy** — distortion, extra fingers, impossible joints
- **Text & typography** — warped letters, nonsensical words, mixed scripts
- **Reflections & shadows** — physically inconsistent lighting
- **Fine textures** — skin, fabric, water, glass rendering failures
- **Crowds & occlusion** — object merging, floating limbs
- **Perspective & geometry** — warped buildings, broken vanishing points
- **Fictional characters** — stylistic inconsistencies vs source material
- **Handwriting** — letter formation, baseline drift, ink simulation

### ✅ Physics-Aware Design
Sectors stress-test Gemini's understanding of:
- Shadow direction consistency
- Reflection accuracy in mirrors, water, and glass
- Depth and scale relationships
- Gravity and structural logic

### ✅ Multilingual & Multi-Script Coverage
The `letters_written_in` series contains handwritten text across
multiple writing systems including Latin, Arabic, Cyrillic, CJK,
and others — a rare feature in synthetic datasets.

### ✅ Decade & Era Simulation
The 50s through 90s image series tests Gemini's ability to
simulate historical photographic aesthetics — grain, color
grading, clothing, and environmental period accuracy.

---

## 🚀 Suggested Use Cases

- **Binary AI detection** — pair with a real image dataset as the negative class
- **Gemini fingerprint analysis** — study generator-specific artifacts in isolation
- **Pop culture rendering analysis** — how well does Gemini handle IP and fictional content
- **Cross-style detection** — photorealistic vs cartoon vs meme vs historical
- **Multilingual OCR robustness** — test handwriting recognition on AI-generated scripts
- **Decade simulation analysis** — evaluate temporal aesthetic accuracy
- **Artifact localization** — segment which regions betray AI generation
- **Cross-generator generalization** — train on Gemini, test on MidJourney or DALL-E
- **Few-shot detection** — small but diverse enough for meta-learning experiments
- **Forensic feature extraction** — frequency domain, noise pattern, EXIF analysis

---

## ⚠️ Limitations

- **Single generator** — all images from Gemini only, cross-model generalization not guaranteed
- **No real images included** — must be paired with a real image dataset for binary classification
- **Nano scale** — 1,067 images is not sufficient as a standalone production training set
- **Flat directory structure** — no subfolder organization by sector or domain
- **No annotations** — no segmentation masks, bounding boxes, or metadata files included
- **Mixed naming conventions** — some files use descriptive names, others use Gemini's default hash names
- **Uneven sector distribution** — some sectors have more images than others based on generation sessions
- **Copyrighted character content** — fictional franchise images may have usage restrictions depending on jurisdiction

---

## 🔧 Recommended Pairing

To use this dataset for binary AI vs Real classification,
pair it with any of these real image datasets as the negative class:

| Dataset | Images | Notes |
|---|---|---|
| COCO | 330K | Diverse real scenes |
| ImageNet | 1.2M | Broad domain coverage |
| Unsplash-Lite | 25K | High quality photography |
| RAISE | 8K | RAW unprocessed real photos |
| Columbia Uncompressed | 933 | Unmanipulated real images |
| FFHQ | 70K | Real face portraits — pairs well with Gemini portraits |

---

## 📜 Citation

If you use this dataset in your research or project please cite:
```
@dataset{nano_banana_2_2025,
  title     = {Nano Banana 2.0: The Omni-Subject Dataset},
  year      = {2025},
  source    = {Kaggle},
  note      = {1067 fully synthetic images, 109 sectors,
               flat directory, Google Gemini generated,
               includes pop culture, geography, cuisine,
               historical figures, memes and multilingual content}
}
```

---

## 🙏 Acknowledgements

All images generated using **Google Gemini Image Generation**.
Dataset structured and curated for AI forensics and detection research.
Sector taxonomy developed through systematic prompt engineering
across 109 visual domains covering the full breadth of human visual experience —
from deep sea hydrothermal vents to internet meme culture.

---

*🍌 Fully synthetic. Truly omni-subject. Built for detection.*

출처: Kaggle (ahnuf05/nano-banana-2-0-the-omni-subject-dataset)
태그: artificial intelligence, intermediate, computer vision, image
라이선스: GNU Lesser General Public License 3.0
수정일: 2026-03-22T20:07:20.407Z
