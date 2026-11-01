---
configs:
- config_name: default
  data_files:
  - split: train
    path: plain/train.jsonl
  - split: test
    path: plain/test.jsonl
- config_name: plain
  data_files:
  - split: train
    path: plain/train.jsonl
  - split: test
    path: plain/test.jsonl
- config_name: vicuna
  data_files:
  - split: train
    path: vicuna/train.jsonl
  - split: test
    path: vicuna/test.jsonl
language:
- ko
tags:
- lima
- kolima
- korean
- instruction
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
---

# Dataset Card for KoLIMA

## Dataset Description

KoLIMA는 Meta에서 공개한 [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) (Zhou et al., 2023)의 [학습 데이터](https://huggingface.co/datasets/GAIR/lima)를 한국어로 번역한 데이터셋입니다. 번역에는 [DeepL API](https://www.deepl.com/docs-api)를 활용하였고, SK(주) Tech Collaborative Lab으로부터 비용을 지원받았습니다. 전체 텍스트 중에서 code block이나 수식을 나타내는 특수문자 사이의 텍스트는 원문을 유지하는 형태로 번역을 진행하였으며, `train` 데이터셋 1,030건과 `test` 데이터셋 300건으로 구성된 총 1,330건의 데이터를 활용하실 수 있습니다. 현재 동일한 번역 문장을 `plain`, `vicuna` 두 가지 포멧으로 제공합니다.  

데이터셋 관련하여 문의가 있으신 경우 [메일](mailto:taes.hahn@gmail.com)을 통해 연락주세요! 🥰


This is Korean LIMA dataset, which is translated from the [LIMA dataset](https://huggingface.co/datasets/GAIR/lima) that Meta's [LIMA model](https://arxiv.org/abs/2305.11206) (Zhou et al., 2023) was trained on. The translation has proceeded through [DeepL API](https://www.deepl.com/docs-api) with financial support from Tech Collaborative Lab in SK Inc.

Please feel free to contact me if you have any question on the dataset.  
I'm best reached via [email](mailto:taes.hahn@gmail.com). 


#### Changelog

- [29 June 2023] New format added: `vicuna` format with the same translation is now available.
- [16 June 2023] Enhanced Translation: keep the text enclosed in special characters, e.g. `$` and `` ` ``, intact without translation.
- [14 June 2023] First upload.

### Usage

```python
>>> from datasets import load_dataset
>>> ko_lima = load_dataset('taeshahn/ko-lima', 'plain') # or load_dataset('taeshahn/ko-lima')
>>> ko_lima_vicuna = load_dataset('taeshahn/ko-lima', 'vicuna')
```

```python
>>> ko_lima['train'][1025]
{
    'conversations': [
        '저는 케냐 출신입니다. 망명을 신청하고 싶은데 비자없이 네덜란드로 망명을 신청하기 위해 여행할 수 있나요? 케냐항공에서 여권을 소지한 경우 스키폴 공항으로 가는 비자없이 비행기에 탑승할 수 있나요?',
        '항공사가 탑승을 허용할 가능성은 극히 낮습니다. 네덜란드에 입국하려는 케냐 시민은 비자, 체류 기간에 필요한 충분한 자금 증명, 다음 목적지 입국에 필요한 서류를 소지해야 합니다. 또한 항공사는 케냐에서 출발하는 승객에 대해 특별 조사를 실시해야 합니다:\n\n> 다음 공항에서 네덜란드로 운항하는 항공사:\n\n아부다비(AUH), 아크라(ACC), 바레인(BAH), 베이징 캐피탈(PEK), 보리스필(KBP), 카이로(CAI), 담만(DMM), 다르에스살람(DAR), 두바이(DXB), 엔테베(EBB), 광저우(CAN), 홍콩(HKG), 하마드(DOH), 이스탄불 아타튀르크(IST), 이스탄불 사비하곡첸(SAW), 요하네스버그(JNB), 키갈리(KGL), 킬리만자로(JRO), 쿠알라룸푸르(KUL), 쿠웨이트(KWI), 라고스(LOS), 모스크바 셰레메티예보(SVO), 무스카트(MCT), 나이로비(NB ), 뉴델리(DEL), 상파울루(GRU), 싱가포르(SIN) 및 테헤란(IKA)은 네덜란드 도착 시 적절한 여행 서류가 없어 입국할 수 없는 경우 해당 항공편의 모든 승객의 여행 서류 사본을 제출하셔야 합니다. 사본에는 여권/여행 서류의 데이터 페이지, 비자가 있는 페이지, 출국/통관 스탬프가 있는 페이지(해당되는 경우)가 포함되어야 합니다. 이러한 입국 규정을 준수하지 않을 경우 항공사에 승객 1인당 최대 11,250유로의 벌금이 부과될 수 있습니다.\n\n마지막 문장에서 볼 수 있듯이 항공사는 탑승 전에 여행 서류를 확인해야 하는 강력한 인센티브를 갖게 됩니다.',
        '인용된 자료의 출처는 무엇인가요?',
        '출처는 항공을 통해 해외로 여행하는 승객의 여권 및 비자 요건과 같은 서류 요건이 포함된 데이터베이스인 Timatic(여행 정보 매뉴얼 자동)에서 가져온 것입니다. 위의 답변은 목적지가 네덜란드이고 귀국/귀국 여행 증빙이 있으며 5일간 체류할 계획이며 케냐 여권의 유효 기간이 약 3년 남은 케냐 시민이 케냐에서 직접 여행하는 시나리오를 기반으로 한 것입니다.'
    ],
    'source': 'multi_turn'
}
```

```python
>>> ko_lima_vicuna['train'][1025]
{
    'id': '1026-multi_turn',
    'conversations': [
        {
            'from': '사람',
            'value': '저는 케냐 출신입니다. 망명을 신청하고 싶은데 비자없이 네덜란드로 망명을 신청하기 위해 여행할 수 있나요? 케냐항공에서 여권을 소지한 경우 스키폴 공항으로 가는 비자없이 비행기에 탑승할 수 있나요?'
        },
        {
            'from': '어시스턴트',
            'value': '항공사가 탑승을 허용할 가능성은 극히 낮습니다. 네덜란드에 입국하려는 케냐 시민은 비자, 체류 기간에 필요한 충분한 자금 증명, 다음 목적지 입국에 필요한 서류를 소지해야 합니다. 또한 항공사는 케냐에서 출발하는 승객에 대해 특별 조사를 실시해야 합니다:\n\n> 다음 공항에서 네덜란드로 운항하는 항공사:\n\n아부다비(AUH), 아크라(ACC), 바레인(BAH), 베이징 캐피탈(PEK), 보리스필(KBP), 카이로(CAI), 담만(DMM), 다르에스살람(DAR), 두바이(DXB), 엔테베(EBB), 광저우(CAN), 홍콩(HKG), 하마드(DOH), 이스탄불 아타튀르크(IST), 이스탄불 사비하곡첸(SAW), 요하네스버그(JNB), 키갈리(KGL), 킬리만자로(JRO), 쿠알라룸푸르(KUL), 쿠웨이트(KWI), 라고스(LOS), 모스크바 셰레메티예보(SVO), 무스카트(MCT), 나이로비(NB ), 뉴델리(DEL), 상파울루(GRU), 싱가포르(SIN) 및 테헤란(IKA)은 네덜란드 도착 시 적절한 여행 서류가 없어 입국할 수 없는 경우 해당 항공편의 모든 승객의 여행 서류 사본을 제출하셔야 합니다. 사본에는 여권/여행 서류의 데이터 페이지, 비자가 있는 페이지, 출국/통관 스탬프가 있는 페이지(해당되는 경우)가 포함되어야 합니다. 이러한 입국 규정을 준수하지 않을 경우 항공사에 승객 1인당 최대 11,250유로의 벌금이 부과될 수 있습니다.\n\n마지막 문장에서 볼 수 있듯이 항공사는 탑승 전에 여행 서류를 확인해야 하는 강력한 인센티브를 갖게 됩니다.'
        },
        {
            'from': '사람',
            'value': '인용된 자료의 출처는 무엇인가요?'
        },
        {
            'from': '어시스턴트',
            'value': '출처는 항공을 통해 해외로 여행하는 승객의 여권 및 비자 요건과 같은 서류 요건이 포함된 데이터베이스인 Timatic(여행 정보 매뉴얼 자동)에서 가져온 것입니다. 위의 답변은 목적지가 네덜란드이고 귀국/귀국 여행 증빙이 있으며 5일간 체류할 계획이며 케냐 여권의 유효 기간이 약 3년 남은 케냐 시민이 케냐에서 직접 여행하는 시나리오를 기반으로 한 것입니다.'
        }
    ]
}
```

### Citation Information
```
@InProceedings{kolimadataset,
    title = {KoLIMA: Korean LIMA Dataset for Efficient Instruction-tuning},
    author = {Hahn, Taeseung},
    year = {2023}
}
```