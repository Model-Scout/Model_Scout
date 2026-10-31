---
license: mit
task_categories:
- translation
language:
- ko
- en
pretty_name: tinystories-korean
size_categories:
- 1M<n<10M
---

# TinyStories-Korean

<!-- Provide a quick summary of the dataset. -->

This dataset is a translated version of [roneneldan](https://huggingface.co/roneneldan)'s [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories) dataset.

I first downloaded roneneldan's TinyStories, and I organized it in a db file. Then I used a local transalation model [eeve](https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0)
 to translate, and I changed it back to a txt file.

Feel free to use!

---
## Citation

```
@misc{kim2024tinystories,
      title={TinyStories Korean translations}, 
      author={Dohoon Kim(g0ster)},
      year={2024},
}
```