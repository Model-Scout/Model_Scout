---
license: gemma
base_model:
- Jiunsong/supergemma4-e4b-abliterated
tags:
  - gemma4
  - gguf
  - llama.cpp
  - multimodal
  - image-text-to-text
  - abliterated
  - uncensored
  - quantized
  - 4-bit
language:
  - en
  - ko
pipeline_tag: image-text-to-text
---

# SuperGemma4-E4B-Abliterated-Multimodal GGUF 4bit

This is the llama.cpp-ready GGUF 4bit distribution of [Jiunsong/supergemma4-e4b-abliterated](https://huggingface.co/jiunsong/supergemma4-e4b-abliterated).

Contents include:
- Converted and quantized supergemma4-e4b-abliterated model from [Jiunsong/supergemma4-e4b-abliterated](https://huggingface.co/Jiunsong/supergemma4-e4b-abliterated)
- mmproj file for image functionality, sourced from [lmstudio-community/gemma-4-E4B-it-GGUF](https://huggingface.co/lmstudio-community/gemma-4-E4B-it-GGUF) (for enabling vision)
- Configuration file (Virtual model) for using Reasoning(aka 'Think') within LM Studio


# How to Install

It is a installation guide for using the model in LM Studio on Windows.
Before proceeding with these steps, you must first install and launch LM Studio."

Instructions:

1. Open Windows Terminal (PowerShell).

2. Change the directory to LM Studio's "Models Directory." (If you specified a different path for your Models Directory, change to that custom path instead.)
```
cd $env:USERPROFILE\.lmstudio\models
```

3. Clone the following repository into a folder named ```kanarena```.
```
git clone https://huggingface.co/kanarena/supergemma4-e4b-abliterated-multimodal-gguf-4bit .\kanarena\supergemma4-e4b-abliterated-multimodal-gguf-4bit\
```

4. Move the configuration files (virtual model) to the main models directory.
```
Move-Item -Path ".\kanarena\supergemma4-e4b-abliterated-multimodal-gguf-4bit\jiunsong" -Destination ".\"
```

5. You can now use this model in LM Studio. If the model does not appear, please **Refresh model list**.

---

# SuperGemma4-E4B-Abliterated-Multimodal GGUF 4bit

이 배포판은 [Jiunsong/supergemma4-e4b-abliterated](https://huggingface.co/jiunsong/supergemma4-e4b-abliterated) 모델을 **llama.cpp 또는 LM 스튜디오** 에서 사용할 수 있는 GGUF 파일입니다. 


- 변환 및 양자화 모델: Jiunsong/supergemma4-e4b-abliterated에서 변환되고 양자화된 [Jiunsong/supergemma4-e4b-abliterated](https://huggingface.co/jiunsong/supergemma4-e4b-abliterated) 모델 파일.
- 이미지 기능용 모델 (mmproj): 비전(Vision) 기능을 활성화하기 위해 [lmstudio-community/gemma-4-E4B-it-GGUF](https://huggingface.co/lmstudio-community/gemma-4-E4B-it-GGUF)에서 가져온 이미지 관련 mmproj 파일.
- 추론 설정 파일 (가상 모델): LM Studio 내에서 추론(Reasoning, Think로 알려져있음) 기능 사용을 위한 가상 모델 설정 파일.

# 설치법

이 설치법은 윈도우용 LM 스튜디오에서 모델 사용하기 위한 것입니다. 
아래 설치법을 따라하기 전에 먼저 **LM 스튜디오를 설치하고 최초 실행**을 하여야 합니다.

설치법:

1. 윈도우 터미널(Powershell)을 엽니다.

2. LM Studio의 "Models Directory" 위치로 디렉토리를 변경합니다. (만약 Models Directory를 다른 경로로 지정했다면 해당 경로로 디렉토리를 변경합니다.)
```
cd $env:USERPROFILE\.lmstudio\models
```

3. 이 레포지토리를 ```kanarena``` 이름의 폴더 안에 다운로드 합니다.
```
git clone https://huggingface.co/kanarena/supergemma4-e4b-abliterated-multimodal-gguf-4bit .\kanarena\supergemma4-e4b-abliterated-multimodal-gguf-4bit\
```

4. 설정 파일(가상 모델)을 model(상위 디렉토리)로 이동합니다.
```
Move-Item -Path ".\kanarena\supergemma4-e4b-abliterated-multimodal-gguf-4bit\jiunsong" -Destination ".\"
```

5. 이제 LM Studio 에서 이 모델을 사용할 수 있습니다. 만약 보이지 않는 경우 **모델 리스트 새로고침**을 해주세요.