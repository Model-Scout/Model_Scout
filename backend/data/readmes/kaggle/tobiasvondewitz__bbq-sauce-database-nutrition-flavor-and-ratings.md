# BBQ Sauce Database: Nutrition, Flavor & Ratings

Label-verified sodium, sugar & calories, 0-5 heat/smoke/sweetness scales, and we

A hand-built, label-verified database of 311 BBQ sauces from 48 brands -
the kind of structured comparison that does not exist anywhere else for
this category.

Every sauce was profiled from its physical label and from a synthesis of
public reviews, so the set combines hard nutrition facts with subjective
flavor and reception in one tidy table (one row per sauce).

### What's inside

- **Nutrition** read straight from the label: sodium, total sugars, total
  carbs, calories, and serving size (~180 sauces with full nutrition).
- **Flavor scales** scored 0-5 for heat, smoke, and sweetness (98%
  coverage) - the part you will not find in any generic food dataset.
- **Web-consensus ratings** (0-5) synthesized from public reviews, with a
  sentiment label and the number of reviews behind it.
- **Categories** ready for grouping: regional style (Kansas City,
  Carolina mustard and vinegar, Alabama white, Texas, Korean, Japanese),
  diet tags (keto, sugar-free, vegan, gluten-free, paleo, whole30 ...),
  and suggested pairings.
- A `source_url` for every row linking to the full profile.

### Ideas to explore

- Do sweeter or smokier sauces earn higher ratings?
- Which regional styles run highest in sugar or sodium?
- How do the "sugar-free" and "keto" sauces actually compare on carbs?
- Build a recommender: input a diet constraint and flavor preference,
  output matching sauces.
- Cluster sauces by flavor profile and see whether the clusters match the
  labelled regional styles.

### Source, methodology, and license

Data by **BBQ Sauce Scout** (https://bbqsaucescout.com), released under
**CC BY 4.0** - free to use, including commercially, with attribution.

- How the data is built: https://bbqsaucescout.com/methodology/
- A companion sodium reference: https://bbqsaucescout.com/data/sodium-database/

Please attribute as: *BBQ Sauce Scout, BBQ Sauce Database (CC BY 4.0),
https://bbqsaucescout.com*. If you publish a notebook with this data, a
link back is appreciated.

Notes: per-serving nutrition is not directly comparable across different
serving sizes - normalise using `serving_size`. Ratings are a synthesised
web consensus, not lab measurements. See the data dictionary for the full
column reference and caveats.

출처: Kaggle (tobiasvondewitz/bbq-sauce-database-nutrition-flavor-and-ratings)
태그: nutrition, data analytics, recommender systems, cooking and recipes, food
라이선스: CC BY-SA 4.0
수정일: 2026-07-08T05:21:18.190Z
