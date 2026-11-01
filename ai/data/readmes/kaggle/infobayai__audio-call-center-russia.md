# call center audio dual channel russia

High-quality Russia Call-Center Audio data for training and evaluating AI model

**Dataset Description:**

This dataset is a **large-scale collection of raw Russian call center audio (dual-channel)**, designed to support the development and training of advanced speech and AI systems.

It consists of real-world customer and agent speech recordings collected from call center environments. The dataset is organized in a dual-channel format, where corresponding customer and agent audio are available as separate recordings, enabling clear role-based modeling and analysis.
The dataset captures authentic speech characteristics such as tone variation, pauses, silence patterns, and natural speaking behaviour commonly observed in customer service environments.This makes it highly valuable for building accurate, scalable, and production-ready AI systems for enterprise and customer support applications.
Additionally, this dataset can be used in data pipelines for **Supervised Fine-Tuning (SFT)** and **Reinforcement Learning with Human Feedback (RLHF)** workflows.

**Key Use Cases**

    -Training Automatic Speech Recognition (ASR) systems for call center environments
    -Call analytics and conversation intelligence
    -Sentiment analysis and emotion detection
    -Quality monitoring and compliance analysis
    -Virtual assistants for customer support
    -Speech-to-Text (STT) for structured call transcription

**Dataset Specification**

    -Language: Russian
    -Type: Raw, unprocessed call center audio
    -Speech Style: Customer and agent speech from call center environments
    -Audio Conditions: Real-world call center environments
    -Domains: customer support, service calls, query resolution, etc.
    -Channel Configuration: Dual-channel (separate customer and agent recordings)
    -Format: .wav, .mp3, .ogg, etc.
    -Sampling Rate: 8000 Hz
    -Duration: 1,025 hours

**Value of Dual Channel Dataset**

    -Clear separation of customer and agent speech for accurate modeling
    -Supports role-based speech analysis and modeling
    -Improves performance in real-world customer support scenarios
    -Ideal for call center analytics and conversation intelligence systems
    -Facilitates precise annotation and labeling workflows

**Basic JSON Schema**
```json
{
"id": "string",
"audio_filepath": "string",
"duration": "float",
"language": "string",
"sample_rate": "integer",
"format": "string",
"num_speakers": "integer",
"domain": "string",
"metadata": {
"source": "string",
"recording_condition": "string"
}
}
```
**Full Dataset Overview**
  
  Total Duration (in hours): 1,316,582
  
  This dataset is part of a large multilingual podcast audio collection covering the following languages: Arabic, Arabic(EG), Arabic(UG), Assamese, Bengali, Chinese, English (India),  English (UK), English (US), Filipino, French, Ganda, German, Gujarati, Hindi, Italian, Japanese, Kannada, Kinyarwanda, Korean, Luganda, Malay, Malayalam, Mandarin, Marathi, Mizo, Nepali, Oriya, Punjabi, Russian, Somali (SO), Somali (UG), Spanish (MX), Spanish (ES), Swahili (KE), Swahili (UG), Tamil, Telugu, Tigrinya, Urdu and Yoruba.

**Data Creation**

  Procured through formal agreements and generated in the ordinary course of business.

**Considerations**

This dataset is provided for research and educational purposes only. It contains only sample data. For access to the full dataset and enterprise licensing options, please visit our website [InfoBay AI](https://infobay.ai/) or contact us directly.

    -Ph: (+91) 8303174762
    -Email: datareq@infobay.ai

출처: Kaggle (infobayai/audio-call-center-russia)
태그: deep learning, optimization, audio, russian, benchmark
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-02-25T09:30:31.297Z
