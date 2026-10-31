# MyAnimeList Character Dataset

Raw anime character data from MyAnimeList.

## **📌 Context**  
This dataset was originally created for my **pet project**: [Ficbot](https://github.com/Pythonimous/ficbot).  

Anime character information is **easily accessible** and often includes high-quality illustrations in a **consistent anime art style**, making it a valuable resource for various **AI-driven generation tasks**—such as **image → name prediction** and **name → bio generation**.  

---

## **📂 Content**  

The dataset is provided in **`anime_characters.csv`**, containing openly available character data from [MyAnimeList](https://myanimelist.net/).  

### 🔹 **Dataset Overview:**  
- **106,299** characters from various manga and anime  
- **102,579** unique English names & **78,822** unique names in Japanese (or other languages such as Chinese/Korean)  
- **92,766** characters with corresponding images  

### 🔹 **Character Information Includes:**  
✔ **English Name** (if available)  
✔ **Source Language Name** (Japanese, Chinese, Korean, etc.)  
✔ **Character Bio** (if available)  
✔ **Character Link** (direct MyAnimeList page)  
✔ **Image Link** (from MyAnimeList, if available)  
✔ **Unique Image Name** (hashed using ImageHash, `hash_size=12` with average hashing)  

⚠ **Note:** Some characters may **share the same name**, such as historical figures (e.g., **Date Masamune**).  

---

## **📜 Acknowledgements**  

This dataset was collected using **Selenium** and the **[Jikan API](https://jikan.moe/)** via a **[public Python wrapper](https://github.com/abhinavk99/jikanpy)**.  

As of **February 26, 2025**, **Jikan remains the only publicly available API** that supports the **Character endpoint** for MyAnimeList. The **official MyAnimeList API does not yet support character data**, and thus, was **not used** in this dataset's creation.  

This dataset is released under the CC0 license, meaning you are free to use it without restrictions. However, if you find it useful, I’d appreciate a citation or mention in your work.

&gt; **Kirill Nikolaev**  
&gt; *MAL Character Dataset.* Kaggle, 2025.  
&gt; DOI: **10.34740/kaggle/ds/1906340**

출처: Kaggle (ophelion/mal-character-dataset)
태그: tabular, image, text, anime and manga
라이선스: CC0: Public Domain
수정일: 2025-02-26T13:23:46.537Z
