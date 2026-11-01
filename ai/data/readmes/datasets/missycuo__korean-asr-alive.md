---
language:
- ko
- vi
task_categories:
- automatic-speech-recognition
tags:
- speech
- audio
- korean-speech
- netflix-korean
pretty_name: Alive ASR Dataset
---

# Alive - Korean ASR Dataset

Dataset ASR trích xuất thoại tiếng Hàn và phụ đề tiếng Việt từ phim/tập: **Alive**.

## Cấu trúc dữ liệu
- `movie_name`: Đường dẫn phân cấp gốc
- `audio_id`: ID phân đoạn thoại
- `audio`: Dữ liệu âm thanh (binary bytes hoặc dictionary path/bytes)
- `korean_text`: Nội dung thoại tiếng Hàn
- `vi_text`: Bản dịch phụ đề tiếng Việt
- `start_time`, `end_time`: Mốc thời gian (giây)
- `duration`: Thời lượng audio (giây)

## Sử dụng với `datasets`
```python
from datasets import load_dataset

dataset = load_dataset("parquet", data_files="data/*.parquet")
```
