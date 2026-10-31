---
tags:
- starcraft
- broodwar
- melee
- maps
license: unknown
language:
- en
- ko
pretty_name: Starcraft Remastered Melee Maps
size_categories: 1K<n<10K
task_categories:
- feature-extraction
- text-to-image
- image-to-image
- reinforcement-learning
task_ids:
- task-planning
splits:
- name: ashworld
  num_bytes: 12,598,840
  num_examples: 135
- name: badlands
  num_bytes: 21,067,712
  num_examples: 213
- name: desert
  num_bytes: 19,505,010
  num_examples: 185
- name: ice
  num_bytes: 19,070,217
  num_examples: 179
- name: install
  num_bytes: 28,135
  num_examples: 1
- name: jungle
  num_bytes: 62,374,211
  num_examples: 563
- name: platform
  num_bytes: 23,324,208
  num_examples: 265
- name: twilight
  num_bytes: 28,311,253
  num_examples: 274
---

## starcraft-remastered-melee-maps

This is a dataset containing 1,815 Starcraft:Remastered melee maps, categorized into tilesets.

The dataset is used to train this model: https://huggingface.co/wdcqc/starcraft-platform-terrain-32x32

The dataset is manually downloaded from Battle.net, bounding.net (scmscx.com) and broodwarmaps.com over a long period of time.

To use this dataset, extract the `staredit\\scenario.chk` files from the map files using StormLib, then refer to [Scenario.chk Format](http://www.staredit.net/wiki/index.php/Scenario.chk) to get data like text, terrain or resource placement from the map.

Alternatively download the dataset and put it in `<My Documents>\StarCraft\Maps`. You can play with your friends.