---
license: cc-by-sa-4.0
language: [en, zh, fr, es, pt, de, it, ru, ja, ko, vi, th, ar]
tags: [wikipedia, pretraining, tokenized]
---
# wiki13_tokenized_precision

Wikipedia in 13 languages, tokenized with CMSManhattan/JiRackPrecisionTokenizer and packed into
2048-token blocks (no BOS, EOS between articles). Token shares: en 50%, the other 12 languages 4.17% each.
97 train shards (`wiki_train_shard_NNNN.pt`, 5000 blocks each, ~0.99B tokens) + `wiki_val.pt` (512 blocks).
Format: `torch.load(f)["input_ids"]` = list of LongTensor(2048).

Source: Wikipedia (https://www.wikipedia.org), licensed CC BY-SA 4.0. This dataset is a derivative
(tokenized) and is distributed under the same licence.
