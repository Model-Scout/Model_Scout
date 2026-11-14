---
language:
- ko
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-8B
base_model_relation: finetune
license: other
license_name: qwen-apache-with-polyone-reference-terms
license_link: https://huggingface.co/luca0621/polyedit-qwen3-8b-property-v1/blob/main/LICENSE.md
datasets:
- luca0621/polyedit-korean-property-instructions-v6
tags:
- qwen3
- polymer
- full-finetuning
- chemistry
---
# POLYEDIT Qwen3-8B property alignment

한국어로 표현한 고분자 재료 요구를 해석하고 MMPAE에 넘길 부분 물성 목표를 출력하는 **full-parameter SFT** 모델입니다. LoRA adapter가 아닌 전체 체크포인트입니다.

The evaluated workflow is request → LLM intent → deterministic joint-reference retrieval → LLM numeric formatting → grounding check → external MMPAE. This checkpoint supplies the LLM stages; it does not itself supply MMPAE weights or independently regress physical values from vague language.

## Results

| Evaluation | Result |
|---|---:|
| Property-only100 intent exact | 87.0% |
| Property-only100 numeric exact | 90.0% |
| Property-only100 whole property pipeline exact | 87.0% |
| Full natural-wording test, 1,838 task pairs exact | 91.13% |
| Full natural-wording intent, 1,458 pairs exact | 89.03% |
| Full natural-wording numeric, 380 pairs exact | 99.21% |
| Separate PSMILES100, this LLM + MMPAE Success@20 | 58/95 = 61.05% |
| PSMILES100 clarification | 5/5 |
| PSMILES100 combined requests | 63/100 |

Property-only100 and PSMILES100 have different request IDs/reference pools. Numeric exact measures reproduction of reference-derived targets, not experimental property accuracy. PSMILES success uses a frozen separate property predictor, not laboratory measurements. Full comparative results, original-base scores, forced-JSON Frontier baselines and historical predictors are in RESULTS_KO.md and ALL_EXPERIMENT_RESULTS_KO.html.

Selected checkpoint epoch: **1** of 2 training epochs, chosen by equally weighted validation intent/numeric exact. Test was not used for checkpoint selection. Internal publication-quality gate: **false**. The 8B checkpoint missed the original intent/pipeline thresholds and is released as a research checkpoint with that limitation retained.

## Inference

Download the repository (including predict.py, polyedit/ and references/) and run from its directory:

```bash
pip install -r requirements.txt
python predict.py --model . --device cuda:0 \
  --request '산소를 잘 막는 게 가장 중요해요. 가벼운 포장재로 쓸 만한 재료를 추천해 주세요.' \
  --output result.json --properties-output properties.json
```

Alternatively use `snapshot_download("luca0621/polyedit-qwen3-8b-property-v1")` and run `predict.py` from that snapshot directory. Private repositories require Hugging Face login with read access.

The script loads FP32, SDPA, `enable_thinking=False`, `do_sample=False`, `max_new_tokens=1024`, with strict parsing and no output repair. Saved generation_config contains upstream stochastic defaults, so explicitly override them as in the script. BF16 or quantized inference may be useful but was not used for the reported checkpoint results.

Only supported requested properties appear in `properties.json`, e.g. `{"rho":{"value":1.2,"unit":"g/cm3"}}` (schema illustration, not a measured/model-produced example). Actual data and saved evaluation examples are under examples/ and evaluation/. The script refuses to export properties on schema/grounding failure, ambiguity or absent eligible reference rows.

## MMPAE interface

Use physical properties with the original MMPAE checkpoint scaler; `--scaler-json` optionally accepts mean/scale arrays of length29. `mmpae` in result.json contains only K supplied property IDs/values. With no scaler it is explicitly unnormalized and must not be used as standardized MMPAE input. No missing-property mask or dummy property slots are created. `polyedit.mmpae_compact.encode_properties_compact` supplies compact encoding for the evaluated MMTransformerAR architecture.

The evaluated external generator is e260 EMA FP32 (checkpoint SHA256 f07b54117b3c99a11fad4051315506de84509e7265227c67fba5bdeb23e92d4d), seed17, 20 candidates, temperature0.8, top-p0.95, max160, no repair. The scaler's historical training pairing has not been fully proven. This repository does not claim portability to arbitrary MMPAE checkpoints or include third-party generator weights.

## Training and reproducibility

- Base: [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), revision `b968826d9c46dd6066d109eabc6255188de91218`.
- Trainable parameters: 8,190,735,360 / 8,190,735,360; original evaluated FP32 safetensors, no conversion.
- Data: 17,036 train task pairs / 13,236 requests; 1,838 validation pairs. Two tasks: intent interpretation and numeric formatting with reference context.
- Full parameter FP32, TF32 training matmul, Adafactor factored/no first moment, lr5e-6, batch1, accumulation16, weight_decay0.01, epochs2, seed20261022.
- Assistant-only cross entropy, equal example weights; no causal/RL objective. Training maximum actual length2213, configured cap3072, no silent truncation.
- transformers4.57.6, torch2.7.1+cu126, A10080GB; peak training allocation 67.40 GiB. Reload comparison matched 8/8 saved examples.
- Exact historical training sources are under reproduction/. Raw data files are in the dataset repo. Override --base, --data, --output, and --scaler when re-running the original script. Original path defaults are historical, not portable configuration; the saved scaler is a separately required input for that script's downstream evaluation.

## Limitations and license

Instructions were assistant-authored/composed with Python, not expert or real-user labels; no GPT-5.5 API teacher was used. Targets are existing PolyOne ML estimates from one joint reference row. The q25/q75 policy is explicit software, not learned physical causality. 29 properties are supported but generalization to all29 simultaneously is limited. See per-property/condition-count metrics.

The PSMILES100 subset and forced-JSON baseline selection have prior-exposure/post-hoc limitations; no general superiority, 20% physical optimization gain, experimental feasibility, or chemical causality is established.

Weights derive from Qwen under Apache-2.0; bundled PolyOne-derived reference data retain the separate original GTRC terms (Zenodo other-nc). See LICENSE.md, LICENSE-Qwen.txt, LICENSE-PolyOne.txt and NOTICE. These terms are preserved rather than labeling the whole mixed package Apache. This is a research release provided without charge.
