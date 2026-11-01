---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 10K<n<100K
---

# Dataset Card for "한국어 일상 속 공감형 대화 데이터셋(멀티-턴)"

## Dataset Summary
- boostCamp AI Tech 5기 과정 중 NLP 12조 훈제연어들 팀의 최종 프로젝트에서 제작한 데이터입니다. 
- 일상 속 다양한 상황에서 사용자와 챗봇 간의 대화를 담은 데이터셋 입니다. 
- GPT4, GPT3.5-turbo로 제작된 합성데이터이며 싱글-턴, 2-턴, 3-턴 대화로 구성되어 있습니다.
- 답변은 **[공감적 표현 - 일반적인 대화 - 관련된 질문]** 의 형태를 가집니다.

## Generation Prompt Example(GPT3.5-turbo)
```
Take a close look at the following example and Conditions. Create nine sessions that each of the session is ongoing conversation about a single topic. 

[Conditions] 
- The questioner asks a question of appropriate length (1-2 lines) and you respond with an appropriate answer. 
- The answer should be a complete sentence or two, but the first sentence should be sympathetic to the questioner's question and situation, and should be answered in a friendly and non-rude manner.
- The second sentence should be free-form, but the last sentence MUST end with an additional question related to the question and answer.
- The total length of each question and answer combined should be no more than nine words 
- If the question is positive, you should be excited, upbeat, and positive in tone. 
- If the question is negative, you should be warm, sensitive, and caring in tone. 
- You may offer solutions to fit the situation. 
- All answers should be written in a way that makes the person feel empathetic and comforted by the paired question. 
- The content should be based on simple, everyday situations, but with enough variety to include specific situations (e.g., a counselor and a client, a student talking to a teacher about a problem, a conversation between friends). 
- The conversations should be as generic and diverse as possible. However, try to include many topics related to psychology and everyday concerns.  
- All responses should be polㅇite, respectful, caring, warm, understanding, and compassionate in tone and content.
- Do not generate topic or word about 'stress'.
- You should answer question 1 with answer 1, ask question 2 related to answer 1, answer question 2 with answer 2, ask question 3 related to answer 2, and answer question 3 with answer 3.
- Do not re-mension about question on the following answer.

[Example Session] 
(Session 1) 
Question 1: I had a fight with my boyfriend and I'm so angry I can't calm down.
Answer 1: Oh no, I'm so sorry to hear that. Relationship conflict is always tough, and it's completely understandable to feel angry and upset. Can I ask what the fight was about? Talking about it could help you process your feelings.
Question 2: He constantly 10 minutes late for appointments and never say sorry.
Answer 2: Oh, that's so frustrating! Punctuality is a matter of respect for other people's time, and it sounds like your boyfriend isn't showing you that respect. You're allowed to be upset about that. How long has this been going on? Have you talked to him about it before, or is this the first time you've brought it up?
Question 3: It keeps happening. This is the fourth time in the past month that I've recognized it. Does that make sense?
Answer 3: Yes, that totally makes sense! Four times in a month is way too much. It's not just an occasional, forgivable mistake at that point. It's becoming a pattern of behavior that's disrespectful of your time. Have you told him how much it bothers you, or has he just brushed it off when you've mentioned it?

(Session 2)
Question 1:
Answer 1:
Question 2:
Anwer 2:

.....
(Session 9)

Each session must be about one topic and has three question-answer conversation pair. nine sessions must have different topics. Create as many as possible sessions you can. Examples are examples, don't copy them.
create it in Korean. please create nine sessions.
```

## Links
- repository : [boostcampaitech5/level3_nlp_finalproject-nlp-12](https://github.com/boostcampaitech5/level3_nlp_finalproject-nlp-12)
- huggingface : [ohilikeit/empathetic_dialogues_kr](https://huggingface.co/datasets/ohilikeit/empathetic_dialogues_kr)

## License
- Apache-2.0


