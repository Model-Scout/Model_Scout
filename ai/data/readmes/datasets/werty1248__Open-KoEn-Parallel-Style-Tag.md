---
dataset_info:
  features:
  - name: source
    dtype: string
  - name: id
    dtype: string
  - name: source_text
    dtype: string
  - name: target_text
    dtype: string
  - name: source_length
    dtype: int64
  - name: target_length
    dtype: int64
  - name: tags
    sequence: string
  splits:
  - name: train
    num_bytes: 44515450.69131624
    num_examples: 70617
  download_size: 34775385
  dataset_size: 44515450.69131624
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
- en
---

### 설명

- gemini-1.5-flash를 이용하여, 한국어 텍스트의 스타일을 태그 형태로 제안하도록 요청하였습니다.

- 사용된 프롬프트

```
당신은 한국어 및 글쓰기 전문가입니다. 마지막에 한국어 텍스트가 주어집니다. 당신은 그 텍스트의 스타일을 주어진 기준에 따라 분류합니다. 그리고 분류 결과를 python Dict[List] 형태로 출력합니다.
dictionary 이름은 "style"입니다.

## 분류 기준 - 복수 선택이 가능합니다.

유형: [명사형(Nominal), 평서문 (Declarative), 의문문 (Interrogative), 명령문 (Imperative), 감탄문 (Exclamatory), 청유문 (Propositive)]

대상: [일반 대중 (General), 전문가 집단 (Specialist), 아동 (Children), 개인 (Individual)]

문체: [격식체 (Formal), 비격식체 (Informal), 딱딱함 (Stiff), 부드러움 (Soft), 친근함 (Friendly), 정중함 (Polite)]

분야: [학술적 (Academic), 법률적 (Legal), 업무적 (Professional), 기술적 (Technical), 문학적 (Literary), 일상적 (Casual)]

어투: [반말, 존댓말]

---

## 타겟 텍스트

```

- 분류 정확도는 따로 검수하지 않았으므로 확실하지 않습니다.
- 잘못된 출력이 파싱되어 있어, tags의 길이가 너무 길거나, 개별 tag의 길이가 너무 긴 경우, 태그에 "출력" 과 같은 단어가 포함된 경우를 필터링 해서 사용해야 합니다.

### 사용된 데이터 셋

- 아래 데이터 셋 중 일부를 발췌했습니다.
- [ChuGyouk/AI-MO-NuminaMath-TIR-korean-240918](https://huggingface.co/datasets/ChuGyouk/AI-MO-NuminaMath-TIR-korean-240918)
- [ChuGyouk/medical-o1-reasoning-SFT-Ko](https://huggingface.co/datasets/ChuGyouk/medical-o1-reasoning-SFT-Ko)
- [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
  - jinaai/jina-embeddings-v3 모델을 사용하여 medical-o1-reasoning-SFT-Ko와 medical-o1-reasoning-SFT를 임베딩한 후 유사도를 측정. 질의, CoT, 답변의 유사도 argmax가 모두 같은 레코드를 가리킬 경우만 pair로 선정
- [lemon-mint/korean_parallel_sentences_v1.1](https://huggingface.co/datasets/lemon-mint/korean_parallel_sentences_v1.1)
- [Translation-EnKo/trc_uniform_313k_eval_45_filtered](https://huggingface.co/datasets/Translation-EnKo/trc_uniform_313k_eval_45_filtered)
  - [heegyu/OIG-small-chip2-ko](https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko)
  - [jhflow/orca_ko_en_pair](https://huggingface.co/datasets/jhflow/orca_ko_en_pair)
  - [jhflow/dolly_ko_en_pair](https://huggingface.co/datasets/jhflow/dolly_ko_en_pair)
  - [jhflow/platypus_ko_en_pair](https://huggingface.co/datasets/jhflow/platypus_ko_en_pair)
  - [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)
  - [lemon-mint/en_ko_translation_purified_v0.1](https://huggingface.co/datasets/lemon-mint/en_ko_translation_purified_v0.1)
  - [squarelike/sharegpt_deepl_ko_translation](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation)

### 라이선스

- 사용된 데이터 중 [jhflow/dolly_ko_en_pair](https://huggingface.co/datasets/jhflow/dolly_ko_en_pair) 및 [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)의 라이선스에 따라, cc-by-sa-4.0으로 배포됩니다.
- [squarelike/sharegpt_deepl_ko_translation](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation) 데이터는 sharegpt 기반으로 OpenAI 약관을 따릅니다.
- 그 외에는 apache-2.0 또는 mit 라이선스를 가집니다.

### 기타

- 처음에는 해요체, 하게체, 하소서체 등으로 구분을 시도하였으나, gemini-flash의 분류 정확도가 너무 낮아서 실패했습니다. 어미 분석은 룰 베이스로 가능할 것 같습니다.
- 태그 라는 컨셉을 위해 데이터에는 분류 기준을 명시적으로 구분하지 않았습니다.
- Google Cloud API를 사용하였습니다.

### Special Thanks

- 한영 번역쌍 데이터를 공개해주신 squarelike님, junelee님, lemon-mint님, kuotient님, jhflow님, kyujinpy님, nlpai-lab 연구실, heegyu님, Translation-EnKo 그룹, ChuGyouk님, 그리고 좋은 데이터를 만들어 주신 FreedomAI, Open-Orca 그룹, databricks, garage-bAInd 그룹, Project-Numina 팀께 감사드립니다.