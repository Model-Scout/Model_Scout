---
license: cc-by-nc-sa-4.0
language:
- ko
base_model: skt/kogpt2-base-v2
library_name: transformers.js
pipeline_tag: text-generation
tags:
- gpt2
- onnx
- education
---

# KoGPT2 (ONNX, int8) for Transformers.js

[skt/kogpt2-base-v2](https://huggingface.co/skt/kogpt2-base-v2)를 브라우저에서 실행할 수 있도록 ONNX로 변환하고 int8로 양자화한 버전입니다.
AI 동아리 수업용 사이트 [LLM 타임머신](https://github.com/SelectiveDeath/llm-timemachine)에서 "과거 LLM" 체험용으로 사용합니다.

## 원본 모델
- 모델: SK텔레콤 KoGPT2 (`skt/kogpt2-base-v2`)
- 라이선스: **CC BY-NC-SA 4.0** (비상업적 이용, 동일 조건 변경 허락). 이 변환본도 같은 라이선스를 따릅니다.

## 변환 내용
- Optimum 1.23.3으로 `text-generation-with-past` ONNX 내보내기 (opset 17)
- onnxruntime 1.20.1 동적 양자화 (QUInt8, per-channel 끔) → `onnx/model_quantized.onnx` (약 126MB)
- 원본 tokenizer_config에 특수 토큰 정보가 없어 `bos/eos = </s>`, `unk = <unk>`, `pad = <pad>`, `mask = <mask>`로 직접 지정
- 변환 스크립트: [tools/convert_kogpt2.py](https://github.com/SelectiveDeath/llm-timemachine/blob/main/tools/convert_kogpt2.py)

## 사용 예 (Transformers.js 3.x)
```js
import { AutoTokenizer, AutoModelForCausalLM } from '@huggingface/transformers';
const tokenizer = await AutoTokenizer.from_pretrained('Sunbyeolsa/kogpt2-ko-onnx');
const model = await AutoModelForCausalLM.from_pretrained('Sunbyeolsa/kogpt2-ko-onnx', { dtype: 'q8', device: 'wasm' });
```
