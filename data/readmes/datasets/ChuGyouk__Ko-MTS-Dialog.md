---
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - ko
tags:
  - medical
---

**The validation set and two test sets will also be updated soon.**

# MTS-Dialog

This is the repo for *Ko-MTS-Dialog*, which is a Korean translated version of MTS-Dialog dataset. MTS-Dialog dataset is a collection of 1.7k short doctor-patient conversations and corresponding summaries.

## Data Translation Process

I use DeepL for automatic translation and manually reviewed results.

## Warning

There are some concerns and warnings for this dataset.

1. I recommend **NOT to use this dataset for Korean medical dialogue summarization task, but to use JUST DIALOGUES for training something like Chatbot**. I did not reviewed for the section_text in detail. More specifically, I've seen cases where "noncontributory" is translated as "비기여" and "negative" is translated as "음수" instead of "부정" or "음성".

2. There are cases where the translation becomes strange due to some **fundamental differences between English and Korean**. This has not been directly modified during review (for consistency). **For example**, for the doctor's question "And no shortness of breath or wheezing that you've noticed?(숨가쁨이나 쌕쌕거림은 없었나요?)", the response in English is 'No', but it is natural to response as "네" in Korean.

3. The content may not be helpful due to **cultural differences between the US and Korea**. Simple **example** is the unit of measurements; temperature(°F vs °C), weight(lb vs kg). **Also**, cannabis/marijuana is legal in some states in the US, though it is illegal in Korea.

4. **Some medical abbreviations are not translated well**. Some have been translated well(ex:COPD - 만성폐쇄성폐질환), but others have been translated incorrectly (ex: CVA - 심근경색) or remain untranslated at all(ex: MCV).


## Example

```
"ID": 990,
"section_text": "This is a 1-year-old male who comes in with a cough and congestion for the past two to three weeks.
                  Started off as a congestion but then he started coughing about a week ago.
                  Cough has gotten worsen.  Mother was also worried.
                  He had Pop Can just three days ago and she never found the top of that and was wondering if he had swallowed that,
                  but his breathing has not gotten worse since that happened. He is not running any fevers.",
"섹션_텍스트": "지난 2~3주 동안 기침과 코막힘 증상으로 내원한 1세 남자 아이입니다.
                  처음에는 코막힘으로 시작했지만 약 일주일 전부터 기침을 시작했습니다.
                  기침이 더 심해졌습니다.  어머니도 걱정이 많으셨어요.
                  3일 전에 팝캔을 먹었는데 뚜껑을 찾지 못해 삼킨 건 아닌지 걱정했는데,
                  그 이후로 호흡이 더 심해지지는 않았어요.  열도 나지 않아요.",
"대화": "게스트_가족: 일주일째 기침 중입니다.\n
        의사: 코막힘은 어떤가요? 일주일 이상인가요?\n
        게스트_가족: 제가 그렇게 말했나요? 2~3주라고 했어요. 너무 걱정돼요. 이제 겨우 한 살이에요.  \n
        의사: 걱정하지 마세요, 처음부터 다 말씀해 주실 수 있나요? \n
        게스트_가족: 네, 처음에는 코막힘으로 시작했는데 일주일 전부터 기침을 하기 시작하더니 점점 심해지고 있습니다.\n
        의사: 좋아요, 또 어떤가요?\n
        게스트_가족: 사실 3일 전에 팝캔을 먹었는데 뚜껑을 찾지 못해서 혹시 삼킨 건 아닌지 궁금합니다.\n
        의사: 혹시 호흡에 변화를 보셨나요?\n
        게스트_가족: 그 이후로 호흡이 더 나빠지지는 않았습니다.\n
        의사: 열은 없나요? \n
        게스트_가족: 아니요, 열은 없습니다.\n
        의사: 네.",
"dialogue": "Guest_family: He is coughing for one week now.\n
              Doctor: How about any congestion? Is it one week or more?\n
              Guest_family: No did I say that? I meant two to three weeks. I am so worried. He is just one year.  \n
              Doctor: Don't worry let me see, can you tell me everything from the beginning?\n
              Guest_family: Sure. It started off as a congestion, but then he started coughing about a week ago and it is getting worse.\n
              Doctor: Okay, what else?\n
              Guest_family: Actually, he had Pop Can just three days ago and I never found the top of that and was wondering if he had swallowed that.\n
              Doctor: It is possible, have you seen any change in his breathing?\n
              Guest_family: His breathing has not gotten worse since that happened.\n
              Doctor: Any fever?\n
              Guest_family: No. No fever.\n
              Doctor: Okay."
```

## Reference

```
@inproceedings{mts-dialog,
      title     = {An Empirical Study of Clinical Note Generation from Doctor-Patient Encounters},
        author = "Ben Abacha, Asma  and
          Yim, Wen-wai  and
          Fan, Yadan  and
          Lin, Thomas",
        booktitle = "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics",
        month = may,
        year = "2023",
        address = "Dubrovnik, Croatia",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2023.eacl-main.168",
        pages = "2291--2302"
    }
```