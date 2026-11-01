---
language:
- ko
task_categories:
- text-classification

---
# AutoTrain Dataset for project: intent

## Dataset Description

This dataset has been automatically processed by AutoTrain for project intent.

### Languages

The BCP-47 code for the dataset's language is ko.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "\uc878\ub824\uc11c \uc274 \uc218 \uc788\ub294 \uacf3\uc744 \ucc3e\uc544\uc918",
    "target": 1
  },
  {
    "text": "\uad50\ud1b5 \uccb4\uc99d\uc774 \uc2ec\ud55c \uc774\uc720\uac00 \ubb50\uc8e0",
    "target": 3
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['11', '12', '13', '14', '15'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 182 |
| valid        | 48 |
