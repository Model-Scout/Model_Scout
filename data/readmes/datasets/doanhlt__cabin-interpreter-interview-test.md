---
license: mit
task_categories:
- automatic-speech-recognition
- translation
language:
- vi
- en
- ko
- ja
- zh
- fr
- es
- de
- it
- pt
- ru
tags:
- audio
- speech-recognition
- interpreter
- interview
- youtube
size_categories:
- n<1K
---

# Cabin AI - YouTube Interpreter & Two-Way Interview Benchmark Dataset

Tập dữ liệu kiểm thử thực tế phục vụ đánh giá năng lực dịch song song (simultaneous / consecutive interpretation), nhận dạng giọng nói đa ngôn ngữ (ASR) và xử lý ngữ cảnh đối đáp 2 chiều có phiên dịch viên.

- **Repository**: [doanhlt/cabin-interpreter-interview-test](https://huggingface.co/datasets/doanhlt/cabin-interpreter-interview-test)
- **Tổng số video hiện tại**: **218 video**
- **Đợt bổ sung ngày 29/10/2026 (100 video các ngôn ngữ khác)**: **100 video mới**
- **Chuẩn âm thanh trích xuất**: 16kHz Mono WAV phục vụ benchmark ASR / STT & MT

## 📊 Phân bổ dữ liệu theo cặp ngôn ngữ (Tổng cộng 218 video)

| Cặp ngôn ngữ | Mô tả | Đợt bổ sung mới | Tổng số video |
| :--- | :--- | :---: | :---: |
| **VI-EN** | VI-EN phỏng vấn & họp báo có phiên dịch | - | 46 |
| **VI-KO** | VI-KO phỏng vấn & họp báo có phiên dịch | - | 34 |
| **EN-KO** | EN-KO phỏng vấn & họp báo có phiên dịch | +13 | 15 |
| **EN-RU** | EN-RU phỏng vấn & họp báo có phiên dịch | +15 | 15 |
| **EN-DE** | EN-DE phỏng vấn & họp báo có phiên dịch | +14 | 14 |
| **EN-ES** | EN-ES phỏng vấn & họp báo có phiên dịch | +10 | 13 |
| **EN-JA** | EN-JA phỏng vấn & họp báo có phiên dịch | +10 | 13 |
| **VI-JA** | VI-JA phỏng vấn & họp báo có phiên dịch | - | 13 |
| **EN-ZH** | EN-ZH phỏng vấn & họp báo có phiên dịch | +10 | 12 |
| **EN-FR** | EN-FR phỏng vấn & họp báo có phiên dịch | +8 | 11 |
| **EN-IT** | EN-IT phỏng vấn & họp báo có phiên dịch | +10 | 10 |
| **EN-PT** | EN-PT phỏng vấn & họp báo có phiên dịch | +10 | 10 |
| **VI-FR** | VI-FR phỏng vấn & họp báo có phiên dịch | - | 7 |
| **VI-ZH** | VI-ZH phỏng vấn & họp báo có phiên dịch | - | 5 |

## 🗂 Cấu trúc tệp dữ liệu
- `curated_youtube_interpreter_interviews.json`: Danh mục đầy đủ toàn bộ 218 video kèm siêu dữ liệu (URL, tiêu đề, cặp ngôn ngữ, loại hình hội thoại).
- `data/cabin_interpreter_interviews_test.parquet`: Tệp dữ liệu hợp nhất chứa toàn bộ 218 dòng kiểm thử cùng dữ liệu âm thanh mẫu 16kHz chuẩn hóa.
- `data/videos.jsonl`: Bản ghi chi tiết dạng JSON Lines đồng bộ với parquet.
- `batches/new_100_videos_other_languages.json`: Danh mục riêng 100 video bổ sung ở các ngôn ngữ khác.
- `batches/today_50_videos_2026-10-29.json`: Danh mục 50 video thu thập ở đợt sáng ngày 29/10/2026.
