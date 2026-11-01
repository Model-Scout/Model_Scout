---
license: mit
task_categories:
- translation
language:
- th
- en
- ko
tags:
- OCR
- translator
- FFXIV
- ENtoTH
pretty_name: MagiciteBabel (realtime translator)
---
## API Key Configuration
- Rename file `open for edit api key.env` to `.env`
- Edit `.env` file and paste your API key:
  ```env
  ANTHROPIC_API_KEY='your_claude_api_key'
  OPENAI_API_KEY='your_openai_api_key'

# MagicBabel for FFXIV
[th] โปรแกรมแปลบทสนทนาในเกมส์ FFXIV แบบ realtime สร้างโดยคนไทย

## Description
MagicBabel is a real-time translation tool specifically designed for Final Fantasy XIV (FFXIV), created by a non-native English speaker to enhance the storytelling experience. The project aims to preserve the unique voices, personalities, and cultural nuances of each character while making the rich narrative accessible to Thai players.

## Key Features
- Real-time OCR detection and context-aware translation
- Dynamic character dialogue system with personality-based translation
- Extensive character database for consistent voice and style preservation
- Advanced text correction and context mapping
- Customizable UI with multiple viewing modes
- Support for game-specific terminology and lore accuracy
- Smart caching system for improved performance
- GPU/CPU support for OCR processing
- Built-in NPC manager for character context customization

## Unique Capabilities
- Maintains individual character speech patterns and personalities
- Preserves cultural references and game-specific terms
- Handles complex dialogue scenarios and choice prompts
- Supports different dialogue formats (character speech, system messages, choices)
- Allows custom character context additions and modifications

## Technical Stack
- Python with Tkinter for UI
- EasyOCR for text detection
- LLM integration for translations
- SQLite for character database
- JSON-based configuration system
- Modular architecture for easy expansion

## License
MIT License

## Motivation
This project was born from a personal need to fully experience FFXIV's storytelling as a non-native English speaker. Standard translation tools often fail to capture the depth, nuances, and character personalities that make the game's narrative special. MagicBabel aims to provide a more immersive experience by preserving these essential elements in translation.