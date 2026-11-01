---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
- moe
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2-24B-A2B-Preview
---

# LFM2-24B-A2B-Preview-GGUF

LFM2-24B-A2B-Preview in GGUF format for use with [NexaSDK](https://github.com/NexaAI/nexa-sdk), with support for Qualcomm NPU, GPU, and CPU inference.

## Model

This repository contains the LFM2 24B parameter model with A2B quantization in GGUF format. It is intended for on-device inference via NexaSDK on Android, Windows, and other supported platforms.

## NPU Setup

**Hardware:** Qualcomm Snapdragon 8 Gen 4 (or other Snapdragon SoCs with NPU as documented by Nexa).

## Tutorial: Run on Android demo app

1. **Install the app**  
   Install the [NexaSDK Android demo app](https://github.com/NexaAI/nexa-sdk/tree/main/bindings/android).

   **Option A — APK:** Download the pre-built APK and install via adb:
   ```bash
   # Download: https://nexa-model-hub-bucket.s3.us-west-1.amazonaws.com/public/android-demo-release/nexaai-demo-app.apk
   adb install nexaai-demo-app.apk
   ```

   **Option B — Build from source:** Clone the repo, open `bindings/android` in Android Studio, then build and run. See the [Android demo README](https://github.com/NexaAI/nexa-sdk/tree/main/bindings/android) for full steps.

2. **Select the model**  
   Open the model selector (dropdown next to the model name) and choose **LFM2-24B-A2B-Preview-GGUF**.

3. **Download**  
   Tap **Download** to fetch the model to your device. Wait until the download finishes.

4. **Load**  
   Tap **Load**. A **load model config** dialog appears: choose **CPU**, **GPU**, or **NPU** (for Qualcomm NPU), then tap **SURE**. Once the model is loaded, the chat area becomes available.

5. **Chat**  
   Type your message in the input field at the bottom, then tap **Send** to get a response. Use **Clear** to clear the input or conversation as needed.

For NPU/GPU/CPU requirements and license, see [NPU Setup](#npu-setup) above and [Android SDK Doc](https://docs.nexa.ai/nexa-sdk-android/overview).

For the full tutorial with screenshots, see the [Tutorial: LFM2-24B-A2B-Preview-GGUF](https://github.com/NexaAI/nexa-sdk/blob/main/bindings/android/README.md#tutorial-lfm2-24b-a2b-preview-gguf) section in the Android demo README on GitHub.

## Usage

- **Android:** See [NexaSDK Android documentation](https://docs.nexa.ai/nexa-sdk-android/overview) for running this model on devices with NPU or other backends.
- **PC / other platforms:** See [NexaSDK](https://github.com/NexaAI/nexa-sdk) for CLI and bindings.
