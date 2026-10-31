# Color terms dataset

Literal & figurative use of color terms and the colors of objects

### Context: 

Color terms are interesting in natural language processing because it’s an area where it’s possible to link distributional semantics (models of word meanings based on which words are used together in texts) to things in the world. This dataset was created to help link semantic models to images.

### Content: 

This dataset is made up of two smaller files, but were both presented and discussed in the same paper (see Acknowledgements). All data in this dataset is in English.

**Concrete color terms**

This dataset contains a list of common items manually labeled with one of the 11 colors from the set: black, blue, brown, green, grey, orange, pink, purple, red, white, yellow.

Literal vs. nonliteral colors

This dataset is made up of color adjective-noun phrases, randomly drawn from the most frequent 8K nouns and 4K adjectives in the concatenated ukWaC, Wackypedia, and BNC corpora. These were tagged by consensus by two human judges as literal (white towel, black feather) or nonliteral (white wine, white musician, green future). Some phrases had both literal and nonliteral uses, such as blue book in “book that is blue” vs. “automobile price guide”. In these cases, only the most common sense (according to the judges) was taken into account for the present experiment. The dataset consists of 370 phrases.

### Acknowledgements: 

If you use these datasets, please cite:

Bruni, E., G. Boleda, M. Baroni, N. K. Tran. 2012. Distributional semantics in technicolor. Proceedings of ACL 2012, pages 136-145, Jeju Island, Korea.

### Inspiration: 

* Are some colors used more often in a literal sense?
* Is there a relationship between how many objects are a given color and how often that color is used in a literal sense?
* Can you use the color of concrete and an image database of those objects to create an automatic color labeller?

출처: Kaggle (rtatman/color-terms-dataset)
태그: arts and entertainment, art, earth and nature, linguistics, artificial intelligence
라이선스: CC BY-SA 4.0
수정일: 2017-07-25T21:12:51.270Z
