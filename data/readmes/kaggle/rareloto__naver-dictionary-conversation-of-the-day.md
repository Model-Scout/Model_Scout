# Korean - English Parallel Corpus

4000+ paired conversations parallel text pairs in Korean and English

### Context

As part of my Korean language learning hobby, I write and type out daily conversations from Naver Conversation of the Day. 
After getting introduced to data science and machine learning, I wanted to use programming to facilitate my learning process by collecting data and trying out projects. So I scraped data from [Naver Dictionary](https://dict.naver.com) using a Python [script](https://github.com/rareloto/beginnerwebscraping-naverdictionary) to be used later when I train a bilingual AI study buddy chatbot or automate Anki [flashcards](https://quizlet.com/_8lh2dv?x=1jqt&i=224vll).

### Content

This is a corpus of Korean - English paired conversations parallel text extracted from [Naver Dictionary](https://dict.naver.com). This dataset consists of 4563 parallel text pairs from December 4, 2017 to August 19, 2020 of Naver's Conversation of the Day. 
The files and their headers are listed below.
* conversations.csv
    * date - 'Conversation of the Day' date
    * conversation_id - ordered numbering to indicate conversation flow
    * kor_sent - Korean sentence
    * eng_sent - English translation
    * qna_id - from sender or receiver, message or feedback
* conversation_titles.csv
    * date - 'Conversation of the Day' date
    * kor_title - 'Conversation of the Day' title in Korean
    * eng_title - English translation of the title
    * grammar - grammar of the day
    * grammar_desc - grammar description

### Acknowledgements

The data was collected from [Naver Dictionary](https://dict.naver.com) and the conversations were from the Korean Language Institute of Yonsei University.

출처: Kaggle (rareloto/naver-dictionary-conversation-of-the-day)
태그: languages, linguistics, nlp, korea
라이선스: Other (specified in description)
수정일: 2020-08-19T14:41:38.993Z
