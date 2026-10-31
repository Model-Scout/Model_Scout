---
license: other
license_name: cognitive-kernel-pro
license_link: LICENSE
---

Here is the SFT data for the paper [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://huggingface.co/papers/2508.00414).
We use GPT-4.1 to sample from the training queries and perform rejection sampling to acquire the successful trajectories.
We include the SFT data from the queries of URLQA (`ck-pro-web.sft.jsonl`), docbench (`docbench.sft.jsonl`), tablebench (`tablebench.sft.jsonl`), webwalkerqa (`webwalker_subset.sft.jsonl`).
SFT data from other queries such as NumiaMath, LogiCoT, BAAI/TACO, are not included due to restrictions on License.