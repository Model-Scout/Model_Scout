---
license: mit
task_categories:
- time-series-forecasting
- text-classification
language:
- ko
size_categories:
- 10K<n<100K
---

# TIPS Multimodal Test Dataset

## Dataset Description

This dataset contains test data for multimodal stock prediction using time series and text data.

### Dataset Structure

- **labels**: Binary labels for stock price prediction (0: down/neutral, 1: up)
- **time_series**: Time series features for stock data
- **texts**: Korean news text data related to stocks

### Data Splits

This is the test split of the TIPS multimodal dataset.

### Usage

```python
from datasets import load_dataset

dataset = load_dataset("makedeltakmlee/Multimodal-test-dataset")
```

### Data Fields

- `labels`: int - Binary classification label
- `time_series`: array - Time series features
- `texts`: string - Korean news text

### Citation

If you use this dataset, please cite:

```
@dataset{tips_multimodal_test,
  title={TIPS Multimodal Test Dataset},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/makedeltakmlee/Multimodal-test-dataset}
}
```

### License

MIT License
