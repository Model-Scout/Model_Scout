---
license: apache-2.0
language:
- en
- ko
pretty_name: Gantry smart-home commands (English + Korean)
size_categories:
- 1K<n<10K
task_categories:
- text-classification
tags:
- home-automation
- smart-home
- voice-assistant
- korean
- synthetic
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test_en
    path: data/test_en.jsonl
  - split: test_ko
    path: data/test_ko.jsonl
---

# Gantry smart-home commands (English + Korean)

Synthetic smart-home commands in English and Korean ("주방 불 켜줘", "현관문 잠가줘", "turn off the kitchen lights") labelled with the action, room and door a home hub should choose. Requests are Korean or English; option ids stay English (`kitchen`, `front`), and Korean room and door names map to them with a fixed table (주방/부엌 → `kitchen`, 현관문/앞문 → `front`).

Used to fine-tune [nohaah/laya-home-fine-tune-kr](https://huggingface.co/nohaah/laya-home-fine-tune-kr), the decision model in **Gantry**, a fully offline voice assistant for the home that runs on a Raspberry Pi.

## Files

| Split | File | Rows | Questions |
|---|---|---|---|
| `train` | `data/train.jsonl` | 6,700 (2,680 Korean, 4,020 English) | 10,297 |
| `test_en` | `data/test_en.jsonl` | 126 | 189 |
| `test_ko` | `data/test_ko.jsonl` | 66 | 102 |

In the training split, 1,005 rows are follow-ups whose answer depends on an earlier command, and another 1,131 carry an unrelated earlier command so a model can't treat history as a shortcut.

## Fields

Each row is one request with the questions a smart-home hub asks about it and the right answers.

| Field | What it holds |
|---|---|
| `state` | The input text: the latest request, and for follow-ups the earlier commands and the actions they produced (`Earlier requests, oldest first: ... Latest request: "..."`) |
| `questions` | One to three multiple-choice questions: `action` (always), plus `room` or `door` when the action needs one. Each has `type` (`choice`), `instructions` (`Which action?`, `Which room?`, `Which door?`) and `criteria`, the option ids for that home |
| `expected` | The correct option id for each question, e.g. `{"action": "turn_on_lights", "room": "kitchen"}` |

Room and door options vary per row (each row samples a different home layout), so a model has to pick from the options it's given rather than memorise a list. Option ids are English (`kitchen`, `front`) in every row; `all` means every room.

### Example

```json
{
  "state": "Latest request: \"아기방 불 꺼죠\"",
  "questions": {
    "action": {
      "type": "choice",
      "instructions": "Which action?",
      "criteria": [
        "turn_on_lights",
        "turn_off_lights",
        "set_temperature",
        "raise_temperature",
        "lower_temperature",
        "open_garage",
        "close_garage",
        "lock_door",
        "unlock_door",
        "none"
      ]
    },
    "room": {
      "type": "choice",
      "instructions": "Which room?",
      "criteria": [
        "all",
        "den",
        "kids room",
        "master bedroom",
        "office",
        "nursery",
        "attic"
      ]
    }
  },
  "expected": {
    "action": "turn_off_lights",
    "room": "nursery"
  }
}
```

## How it was made

Generated from templates by Gantry's `training/generate_data.py` and `training/korean.py` ([github.com/noahhps/gantry](https://github.com/noahhps/gantry)):

- **Requests** are filled from per-action phrasings ("turn on the {room} lights", "it's too dark in here", "lock the {door}") with random rooms, doors and numbers.
- **Homes** get 3–8 rooms and 2–4 doors sampled from a larger pool, shuffled per row.
- **Follow-ups** pair an earlier command with requests like "turn them off" or "make it warmer", so the answer depends on the history.
- **Non-commands** ("what's the weather", "thanks") are labelled `none`.
- **Light variation** in English: random capitalisation and openers such as "hey," and "please"; in Korean, openers such as 저기, 음 and 있잖아.
- **Korean requests** use natural phrasings (불 켜줘, 따뜻하게 해줘, 잠가줘), both Hangul numbers (칠십이) and digits, and Korean follow-ups (그거 꺼줘, 다시 열어줘).
- **Speech-to-text slips** appear in Korean requests, which usually come from a speech recogniser: 줘 heard as 죠 or 져, and dropped spaces.
- **Test sets** use phrasings that never appear in training, so they measure generalisation to new wording, not memorisation.

### Actions in the training split

| Action | Training rows |
|---|---|
| `turn_on_lights` | 1,298 |
| `turn_off_lights` | 1,288 |
| `set_temperature` | 448 |
| `raise_temperature` | 572 |
| `lower_temperature` | 527 |
| `open_garage` | 499 |
| `close_garage` | 602 |
| `lock_door` | 434 |
| `unlock_door` | 577 |
| `none` | 455 |

## Limitations

All requests are synthetic: generated from templates, not said by people. The test sets measure new phrasings of the same kinds of commands, not real speech, so expect lower accuracy on real recordings passed through a speech recogniser.

## License

Apache-2.0, the same as the models trained on it.
