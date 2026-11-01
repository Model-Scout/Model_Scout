# Global Cuisine Meals with Diet Labels

A comprehensive dataset of global dishes with nutritional values, allergen detai

# 🥗 Global Cuisine Dishes with Nutrition & Allergen Info

## 🌍 About the Dataset

This dataset has been **programmatically generated using AI models** and cleaned thoroughly to ensure quality and usability. It contains a curated set of global dishes—spanning **Japanese, Korean, Indian, Italian, French, Continental, and Mediterranean cuisines**—with comprehensive information across key dietary dimensions.

Each dish includes:

- 📛 **Dish Name**  
- 📝 **Description**  
- 🍽️ **Cuisine, Meal Type** (Breakfast, Lunch, Dinner), **Diet** (Veg / Non-Veg)  
- 🏷️ **Tags**  
- 🔢 **Nutritional Values**: Calories, Protein, Fat, Carbohydrates  
- ⚠️ **Common Allergens** (e.g., dairy, gluten, nuts, shellfish, soy)

---

## ⚙️ How This Was Created

I used an **AI Agent pipeline**, integrating [Ollama](https://ollama.ai/) with a local LLM (`tinyllama`) to:

- ✅ Generate realistic and culturally accurate dishes with relevant metadata  
- ✅ Parse and structure the output in a consistent tabular format  
- ✅ Add allergen and nutrition estimates  
- ✅ Clean malformed or inconsistent entries using Python and Pandas

The dataset was saved in `.csv` format and cleaned to remove:

- ❌ Garbled entries  
- ❌ Incomplete rows  
- ❌ Formatting artifacts like `"1. "` or quotes in dish names  

---

## 📊 Columns Overview

| Column             | Description                           |
|--------------------|---------------------------------------|
| Dish Name          | Name of the dish                      |
| Description        | Short description                     |
| Cuisine            | Cultural origin of the dish           |
| Meal Type          | Breakfast, Lunch, or Dinner           |
| Diet               | Veg or Non-Veg                        |
| Tags               | Keywords for classification           |
| Calories (kcal)    | Approximate calories                  |
| Protein (g)        | Protein content in grams              |
| Fat (g)            | Fat content in grams                  |
| Carbohydrates (g)  | Carbohydrate content in grams         |
| Allergens          | Known common allergens (if any)       |

---

## 💡 Potential Use Cases

- 🤖 Training ML models for nutrition/diet prediction  
- 🥗 Building health or meal planning apps  
- 🍳 Recipe recommendation engines  
- 🧠 Food classification and enrichment  
- 🧾 Educational tools for culinary learning

---

## 🛠️ Tools Used

- 🐍 Python (Pandas, CSV, Subprocess)  
- 🧠 Ollama with TinyLlama model  
- 🧑‍🍳 Local AI agent to generate and structure responses  
- 🧹 Manual + programmatic data cleaning

---

## 🙋‍♀️ Author

**Himanshi Kushwaha**  
Master’s in CS @ Indiana University  
AI Engineer & Researcher  
&gt; Feel free to connect or collaborate on cool AI x Food ideas!``

출처: Kaggle (himanshikushwaha/global-cuisine-meals-with-diet-labels)
태그: computer science, text
라이선스: CC BY-SA 4.0
수정일: 2025-04-09T16:59:27.230Z
