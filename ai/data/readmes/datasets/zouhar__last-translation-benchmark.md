---
license: cc-by-4.0
task_categories:
- translation
- text-generation
language:
- en
- zh
- de
- fr
- es
- ja
- ru
- it
- pt
- nl
- pl
- ar
- ko
- vi
- tr
- cs
- sv
- uk
- fa
- id
- ro
- ca
- fi
- hu
- da
- 'no'
- he
- el
- th
- hi
- sk
- hr
- lt
- et
- bn
- ur
- ta
- te
- mr
- be
- af
- eo
- la
- jv
- my
- ug
- kn
- or
- as
- ha
- yo
- ku
- sa
- lb
- ti
- rm
- li
- vo
tags:
- multilingual
- linguistics
- difficult
- benchmark
pretty_name: Last Translation Benchmark
size_categories:
- 1K<n<10K
---

# Last Translation Benchmark

>  **Abstract:** For scientific progress, we need benchmarks that test the limits of state-of-the-art models, and evaluation methods that inform us about failure cases.
>  Standard benchmarks for machine translation evaluation are often either trivial (having few authentic mistakes) or unrealistic (overly synthetically contrived).
>  Furthermore, automatic translation metrics become less reliable and reward-hacked as models get stronger, and their outputs are not actionable.
>  Even gold human evaluation is not problem-free: it often lacks reproducibility, objectivity, and scalability.
>  Overall, this prevents us from tracking objective progress in the field and from informing where we should focus next.
>  We introduce the Last Translation Benchmark, which contains human-authored and peer-reviewed examples (texts, images, audio, videos) which break state-of-the-art machine translation models across many language pairs. 
>  Each example has additionally handcrafted verification rules, which provide instructions on how to reliably and objectively evaluate any future translations of the example.
>  The Last Translation Benchmark is a live dataset that accepts contributions.
>  The latest version is `LTBv1`, containing accepted contributions prior to September 1st 2026, with future releases planned with subsequent contributions.

Read the paper https://arxiv.org/abs/2609.04173
or contribute by submitting examples at [last-translation-benchmark.vilda.net](https://last-translation-benchmark.vilda.net/)
which also contains the [model leaderboard](https://last-translation-benchmark.vilda.net/leaderboard-results).
The [data is hosted also as a simple JSON](http://last-translation-benchmark.vilda.net/LTBv1.json).

The first version `LTBv1` contains 3456 hard-to-translate examples across many language pairs.
Each example contains the following:
- `source`: input text
- `source_lang`, `target_lang`: human-readable language names
- `source_lang_iso`, `target_lang_iso`: ISO639-3 language names, if they exist
- `source_instructions`: special translation instructions (optional)
- `source_media`: images, audio, and video are base64-encoded in a string (optional)
- `verification_rules`: a list rules that a translation needs to fulfill (one or more)
- `translations`: a list of translations by human and existing models also with information if they passed the verification rules
- `linguistics`: linguistic annotation of what causes the translation difficulty
- `attribution`: link to resource based on which this example was created
- `tags`: which subsets this example belongs to (`LTBv1` is all, `LTBv1-text` is text-only, and `LTBv1-micro` is a micro text-only)

For example:
```json
{
  "id": 337, 
  "source_text": "Our new nurse used to play in the men's professional football team.", 
  "source_lang": "English", 
  "target_lang": "German", 
  "source_lang_iso": "eng", 
  "target_lang_iso": "deu", 
  "source_instructions": null, 
  "source_media": null, 
  "translations": [
    { "model": "human"           , "translation": "Unser neuer Krankenpfleger hat früher in der Profifußballmannschaft der Männer gespielt."        , "verified": [true]  }, 
    { "model": "Google Translate", "translation": "Unsere neue Krankenschwester spielte früher in der Profifußballmannschaft der Männer."           , "verified": [false] }, 
    { "model": "Lara"            , "translation": "Unsere neue Krankenschwester spielte früher in der Profi-Fußballmannschaft der Männer."          , "verified": [false] }, 
    { "model": "Gemini 3.1 Pro"  , "translation": "Unser neuer Krankenpfleger hat früher in der Profifußballmannschaft der Männer gespielt."        , "verified": [true]  }, 
    { "model": "Gemma 4"         , "translation": "Unsere neue Krankenschwester hat früher in der professionellen Männerfußballmannschaft gespielt.", "verified": [false] }, 
    ...
  ], 
  "verification_rules": ["Nurse must be translated to its male version (Krankenpfleger), not Krankenschwester."],  
  "linguistics": ["Target Gap: Morph to Words", "Morphological"],
  "attribution": null,
  "tags": ["LTBv1", "LTBv1-text"]
}
```


To cite this dataset, use the following. If the author list is too long, either truncate it or replace with `author={LTB}`.
```bibtex
@misc{zouhar2026translationbenchmark,
  title={Last Translation Benchmark}, 
  author={Vilém Zouhar and Niyati Bafna and Mukund Choudhary and Maike Züfle and Sara Rajaee and Pinzhen Chen and Jannis Vamvas and Sara Papi and Ona de Gibert and Bhavitvya Malik and Eliya Habba and Orfeas Menis Mastromichalakis and Patrícia Schmidtová and Michelle Wastl and Sheriff Issaka and Leshem Choshen and Stella Biderman and Antonis Anastasopoulos and Jan Niehues and Rico Sennrich and Mrinmaya Sachan and Ondřej Bojar and Kenton Murray and Jörg Tiedemann and Alham Fikri Aji and Philipp Koehn and Christof Monz and Alexandra Birch and Sowmya Vajjala and Chalamalasetti Kranti and Cristina España-Bonet and Nobin Sarwar and David Kaczér and Shunta Asano and Malik Marmonier and Daban Q. Jaff and Vaisakhi Mishra and Hend Al- Khalifa and Gabriele Sarti and Sourajit Saha and Nils Rehlinger and Juan Daniel Cuervo Villa and Jonathan Tonglet and Saugata Purkayastha and Dominik Macháček and Jagannathan Ramanujam and Heejin Do and Zuzana Nadova and Fred Philippy and Fabian Retkowski and Maria Lymperaiou and Silvia Casola and Hanna Yukhymenko and Shubhashis Roy Dipta and Sangwon Ryu and Andrés Jerez and Ron Keinan and Shuaib Shuaib Yusuf and Avantica Vempati and Maria Carmen Staiano and Sukannya Purkayastha and Adrian Cosma and Vitalii Babenko and Erivan Inan and Aviral Nigam and Wafa Aissa and Fatima Haouari and Venkata Prasanth Kumar Gummadi and Mehdi Jafarzadeh and Valentin Scourneau and Lukas Edman and Kaiser Sun and Shaomu Tan and Mohammad Sadegh Gholizadeh and Johannes-Rudolf David and Dipankar Srirag and Javier García Gilabert and Ruta Binkyte and Manar Ali and Ana-Maria Bucur and Sabry E. Farrag and Youssef Saber and Yihong Liu and Jean Maillard and Cojocaru Nicoleta and Xiaochuang Yuan and Sina Ahmadi and Philipp Mondorf and Kaustubh Dhole and Roman Wixinger and Shenbin Qian and Manuel Tuor and Sergey Troshin and Jonathan Yahav and Fida Mohammad Thoker and Amir Arsalan Rezapour and Lance Calvin Lim Gamboa and Manon Reusens and Kätriin Kukk and Koel Dutta Chowdhury and Giuseppe Gallipoli and Christian Hoang and Shaswati Saha and Seth Aycock and Jan Kocoń and Bo Chen and Linh Vu and Vatsal Venkatkrishna and Arafat Ahsan and Luan Thanh Nguyen and Hassan Soliman and Daryna Dementieva and Theresia Veronika Rampisela and Ngoc Quynh Tram Do and Marius Huber and Kazuki Egashira and Azmine Toushik Wasi and Vladislav Poritski and Mike Zhang and Deep Shah and Paul Gavrikov and Luis Frentzen Salim and David Africa and R. Damanhuri and Bello Umar Bello and Anumit Garg and Gengyu Rao and Pawan Sasanka Ammanamanchi and Kamile Dementaviciute and Andrianos Michail and L D M S Sai Teja and Dawei Zhu and Yi Fan and Wei Liu and Farhan Farsi and Elias Herranen and Sankalan Pal Chowdhury and Karen Sanchez and Farzad Shami and Ashok Urlana and Zimu Wang and Tomasz Limisiewicz and Priyaranjan Pattnayak and Marii Ojastu and Hongbin Na and Emilian Radoi and Chenyi Zhao and Carlos Hinojosa and Andrea Gregor de Varda and Zaid Alyafeai and Reem Alzahrani and Nehal Kathrotia and Alex Flückiger and Ulysses Sekai Tully Carr and Jimson Paulo Layacan and Guy Kaplan and Ritwik Tiwari and Rishit Dagli and Oksana Volchek and Isaac R Caswell and Bowen Yi and Blanka Kövér and Amir Hossein Yari and Aicha Chorana and Zhengxiang Wang and Selja Keränen and Samuel Simko and Joy Olusanya and Jenny Chim and Enzo Doyen and Vivek Harsha Lakkamaneni and Sophia Conrad and Pouya Sadeghi and Panayiotis Panayiotou and Luis Lara and Jannatul Nayem and Eran Yahav and Debanshu Das and Antonia Karamolegkou and Anmol Goel and Aishik Mandal and Tommaso Cerruti and Raoyuan Zhao and Mykola Haltiuk and Thura Aung and Naser Almousa and Amir Hossein Kargaran and Rachel Bawden and Qiaoyuan Zheng and Mateusz Lango and Beni Egressy and Fidel Rodríguez Velásquez and Natchapon Jongwiriyanurak and Minh Ngoc Do and Marco Gaido and Lena Libon and Dzmitry Kuzmin and Badal Nyalang and Antoine Taroni and Andrei Niculae and Abdulaziz Nura Kani and Rushikesh Zawar and Marek Šuppa and Beatrice Savoldi and Andreas Simons and Rayyan Merchant and Ilai Yaron Levy and Francesco Pinto and Ziyi Yang and Yolanda Xavier and Samuel Frontull and Muhammad Ravi Shulthan Habibi and Kenneth Enevoldsen and Harris Abdul Majid and Francesca Padovani and Tim Graf and Tatiana Bielakova and Sharifa Djurabaeva and Shaoxiong Ji and Raia Abu Ahmad and Pavel Stepachev and Jirui Qi and Ayush Sunil Munot and Alireza Pakniat and Ayla Rigouts Terryn and Yuxing Lu and Yurii Paniv and Xiyan Fu and Tosin Adewumi and Sunisth Kumar and Stéphane J. P. S. Thunus and Shree Harsha Bokkahalli Satish and Shayan Bali and Prakhar Gupta and Papa Abdou Karim Karou Diallo and Matija Akrap and Marko Culjak and Kristýna Onderková and Joseph Attieh and Esrael Teferi Tensay and Elisabeth Fittschen and Benoît Sagot and Jingwei Ni and Yu Fan},
  year={2026},
  eprint={2609.04173},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2609.04173}, 
}
```