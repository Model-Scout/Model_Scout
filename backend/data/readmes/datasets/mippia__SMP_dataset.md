---
license: mit
language:
- en
- ko
tags:
- music
- music-information-retrieval
- plagiarism-detection
- music-similarity
task_categories:
- audio-classification
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: smp_dataset.csv
arxiv: 2601.21260
---

# Similar Music Pair (SMP) Dataset

The SMP (Segment-based Music Plagiarism) dataset contains music plagiarism 
detection pairs with temporal segment annotations. Each row represents a pair 
of songs with identified similar segments.

This dataset accompanies the paper 
[Music Plagiarism Detection: Problem Formulation and a Segment-based Solution](https://arxiv.org/abs/2601.21260).

- Code: https://github.com/Mippia/Music-Plagiarism-Detection
- Demo: https://huggingface.co/spaces/mippia/MPD-demo
- Project page: https://mippia.github.io/icassp-mpd/

## Dataset Structure

| Column | Description |
| --- | --- |
| `ori_title` | Title of the original song |
| `comp_title` | Title of the comparison song |
| `ori_link` | YouTube link to the original song |
| `comp_link` | YouTube link to the comparison song |
| `relation` | Relationship type (e.g., `plag` for plagiarism) |
| `ori_times` | List of start times (seconds) of similar segments in the original song |
| `comp_times` | List of start times (seconds) of similar segments in the comparison song |
| `pair_number` | Unique identifier for song pairs |
| `acoustic_idx` | Unique identifier for segment pairs |

Time annotations are JSON-formatted lists; `ori_times[i]` and `comp_times[i]` 
correspond to the same matching segment between the two songs.

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("mippia/SMP-dataset")
print(dataset["train"][0])
```

## Notes

- **Audio is not included.** Only YouTube links and temporal annotations are 
  provided. Users must retrieve audio from YouTube themselves.
- The dataset includes both English and Korean songs across multiple genres.

## Citation

```bibtex
@inproceedings{go2026mpd,
  title={Music Plagiarism Detection: Problem Formulation and a Segment-based Solution},
  author={Go, Seonghyeon and Kim, Yumin},
  booktitle={ICASSP},
  year={2026}
}
```

## License

Released under MIT License.