---
license: mit
language:
  - ko
  - en
task_categories:
  - text-generation
  - question-answering
tags:
  - fortune-telling
  - western-astrology
  - zodiac-signs
  - horoscope
  - yeji
size_categories:
  - 10K<n<100K
---

# 🌟 YEJI Horoscope Korean Dataset

서양 점성술(황도 12궁) 기반 한국어 운세 데이터셋

## 📊 Dataset Info

| 항목 | 내용 |
|------|------|
| **샘플 수** | 21,953 (train) |
| **언어** | 한국어 (번역) |
| **도메인** | 서양 점성술 |
| **형식** | Alpaca (instruction/input/output) |

## 🔮 Domain Coverage

### 황도 12궁 (Tropical Zodiac)
- ♈ 양자리 (Aries) - 3/21~4/19
- ♉ 황소자리 (Taurus) - 4/20~5/20
- ♊ 쌍둥이자리 (Gemini) - 5/21~6/20
- ♋ 게자리 (Cancer) - 6/21~7/22
- ♌ 사자자리 (Leo) - 7/23~8/22
- ♍ 처녀자리 (Virgo) - 8/23~9/22
- ♎ 천칭자리 (Libra) - 9/23~10/22
- ♏ 전갈자리 (Scorpio) - 10/23~11/21
- ♐ 사수자리 (Sagittarius) - 11/22~12/21
- ♑ 염소자리 (Capricorn) - 12/22~1/19
- ♒ 물병자리 (Aquarius) - 1/20~2/18
- ♓ 물고기자리 (Pisces) - 2/19~3/20

### 운세 유형
- 일간 운세 (Daily Horoscope)
- 주간 운세 (Weekly Horoscope)
- 월간 운세 (Monthly Horoscope)
- 연간 운세 (Yearly Horoscope)

## 💻 Usage

```python
from datasets import load_dataset

ds = load_dataset("tellang/yeji-horoscope-ko")
print(f"Total samples: {len(ds['train']):,}")  # 21,953

# 샘플 확인
sample = ds['train'][0]
print(f"Instruction: {sample['instruction']}")
print(f"Output: {sample['output'][:200]}...")
```

## 📁 Schema

```python
{
    "instruction": str,  # 질문/요청
    "input": str,        # 추가 컨텍스트 (별자리, 날짜 등)
    "output": str,       # 운세 해석
    "domain": str,       # "horoscope"
    "source": str,       # 원본 출처
    "original_output": str  # 번역 전 원문 (영어)
}
```

## 🔗 Related Datasets

- [yeji-meta](https://huggingface.co/datasets/tellang/yeji-meta) - 메타 허브
- [yeji-fortune-telling-ko-v3](https://huggingface.co/datasets/tellang/yeji-fortune-telling-ko-v3) - 통합 학습 데이터
- [yeji-tarot-v3](https://huggingface.co/datasets/tellang/yeji-tarot-v3) - 타로 데이터

## 📜 License

MIT License

---

Part of the **YEJI Project** - Fortune-Telling AI Dataset Collection
