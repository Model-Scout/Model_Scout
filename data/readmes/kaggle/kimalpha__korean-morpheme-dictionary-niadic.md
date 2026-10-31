# Korean morpheme dictionary, NIADic (930,000 words)

한글 형태소 사전 NIADic (총 93 만 단어)

### Context

잘 아시겠지만 영어와 다르게 한국어는 NLP 처리가 엄청나게 어렵습니다. 
우선 영어의 경우 많은 전 처리 라이브러리가 있지만 한국어는 전 처리 및 임베딩이 그에 비해 매우 떨어집니다.
또한, 띄어 쓰기, 한 글자 차이 등으로 의미가 완전히 달라지기 때문에 더더욱 NLP 처리가 어렵습니다. 

이에 연구자, 일반인 등이 쉽게 NIADic을 활용하여 텍스트 분석을 수행 할 수 있도록 KoNLP의 기초 형태소 사전으로 추가하여 제공합니다. 

As you know well, unlike English, Korean is extremely difficult to process NLP.
First of all, in the case of English, there are many pre-processing libraries, but in Korean, pre-processing and embedding level are relatively low.
Also, it is even more difficult to process NLP because the meaning is completely different due to spacing and one letter difference.

Therefore, it is added as a basic morpheme dictionary of KoNLP so that researchers and the general public can easily perform text analysis using NIADic.

### Content

오픈소스 R 에서 한글 분석 패키지인 KoNLP 설치 
Installing KoNLP, a Korean analysis package, from the open source R
`&gt;Install.package('KoNLP')`

패키지 버전 확인 (0.80.0 이상)
Check the package version (0.80.0 or higher)
`&gt;packageVersion('KoNLP')`

NIADic 로딩, 시스템에서 처음 NIADic을 사용 할 때 자동으로 사전을 다운로드하고 설치
NIADic loading, automatically downloading and installing dictionaries when using NIADic for the first time in the system.
`&gt; useNIADic()`

### Acknowledgements

Source : https://kbig.kr/portal/kbig/knowledge/files/bigdata_report.page

라이센스 : 
저작자와 출처 등을 표시하면 영리 목적의 이용이나 변경 및 2차적 저작물의 작성을 포함한 자유이용을 허락합니다. 
(단, 해당 자료를 사용하여 만들어진 2차 저작물에도 동일한 라이선스를 적용해야 합니다.)

License : 
Indicating the author and source allows free use, including use or change for profit and creation of secondary works. 
(However, the same license must be applied to secondary works made using the material.)

### Inspiration

Hangul (Korean language) is a pretty hot language.
It's not bad to study. 😃

출처: Kaggle (kimalpha/korean-morpheme-dictionary-niadic)
태그: languages, beginner, nlp, text, korea
라이선스: CC BY-SA 3.0
수정일: 2021-12-15T09:37:31.780Z
