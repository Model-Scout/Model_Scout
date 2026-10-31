---
language:
- ko
tags:
- textapp
- documentapp
- writingapp
- android
- apk
---
자체 제작 apk, 안드로이드 app<br>


1. 안드로이드 용 글쓰기 기본 앱입니다. <br>

기존 상업, 무료 앱은 광고와 이것저것 불편해서 걍 만들었음. <br>
무료이며, 제한 없음. <br>
글자수, 선택 글자수 표기됨.<br> 
말줄임표, 굽은 따옴표 변환 가능.<br> 

*.txt파일과 폴더로 구성돼 있습니다. <br>
<br>
안드로이드 기본 파일 앱등을 통해서 해당 파일과 폴더를 공유할 수 있습니다. <br>
앱의 기본 폴더는 안드로이드 - Documents- NLibrary 입니다. <br>
파일 탐색기 앱을 통해서 자유롭게 접근, 수정, 변경, 삭제, 공유 가능합니다. <br>


상기는 과거 버전이고 <br>

![Screenshot_20260709_105706_MyStory](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/5NNXVfHIQrUJY9RMFQyBJ.jpeg)

![Screenshot_20260709_105717_MyStory](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/rbduiYP4XWbI6ziWkIeca.jpeg)

![Screenshot_20260709_102150_MyStory](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/6Q3JYnT00ta3Izt_JFStu.jpeg)

업데이트 함(26.07.09)<br>
드디어!!!!! 제가 Kotlin을 뚫었습니다. 

![260725](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/aMEgSgZrA3D8dgJoM4RLL.png)
todo의 일정관리와 날짜별 메모 추가 <br>
여러 자잘한 오류 수정(키보드, 화면 등등)<br>
본문 편집할 때 자꾸 이상하게 포커스가 맞지 않거나, 문단 첫머리 글자가 윗줄 끝으로 붙는 문제 수정<br>
검색 및 치환, 부호(말줄임표, 굽은 따옴표 변환) 등등 추가. <br>
전체 복사 버튼 추가. <br>
안드로이드 시스템에 작성 txt파일이 즉각 업데이트 되지 않았던 문제 수정<br>
글자 선택 시, 선택 글자 수가 표시되게 수정함. <br>
커서 깜빡임 오류 수정.<br>
글자 수(공백 포함)표시를 위로 고정함. <br>

기본 화면 , 원고 작성 다크모드, 원고 작성 라이트 모드 <br>
<br>
기본화면: 폴더 생성할 수 있습니다. 폴더 정보가 표시됩니다. <br>
텍스트 정보가 표시됩니다. <br>
원고 작성 화면: 글자수가 표시됩니다. 글자의 크기를 조절할 수 있습니다. 파일 이름 변경 가능. <br>
<br>
apk파일을 다운로드 해주세요 <br>
<br>
<br>
휴대폰으로 옮겨 <br>
알 수 없는 출처 앱, 1번 허용으로 설치해 주세요 <br>
무시하고 설치, 앱 검사 허용
최초 1회 모든 파일 접근 권한 허락 문구가 나옵니다. <br>
txt파일을 읽어들이기 위해 허락해주세요. <br>

화면이 안드로이드 키보드에 가리는 문제 해결 함<br>
===============================<br>

2. 운동 카운터 앱, 운동할 때 옆에서 숫자 세어주는 앱 apk
![Screenshot_20260330_070216_TempoCounter](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/RqDuYFxiF6R9fBnMim_4b.jpeg)
![Screenshot_20260330_070402_TempoCounter](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/X2rVDSm__1iAg28vLKARQ.jpeg)
![Screenshot_20260330_070242_TempoCounter](https://cdn-uploads.huggingface.co/production/uploads/69bb49a867b1bab37307832e/zg7FSzWzHbjJtaR6dqDoU.jpeg)

예전부터 운동할 때 나 대신 숫자 말해주는 앱을 갖고 싶었는데<br>

예전에는 플레이 스토어에 그런 앱이 없었어요.<br>

덤벨이나 아령이나 윗몸일으키기(안 하지만...) 할 때<br>

옆에서 간격에 맞춰서 숫자를 씨불이기만 하면 되는데<br>

그런 간단한 앱이 없더라고요?<br>

그래서 아쉬워하다가<br>

이번에 apk 만들기를 터득하면서 만들었습니다. <br>

​

템포: 숫자 읽기 간격입니다. 초 단위로 입력하면 돼요. 1.5초, 이런 식으로요<br>

​

루프+rest : 반복 세트입니다. 만약 20까지 설정하면, rest 초만큼 쉬고 다시 1부터 20까지 반복합니다. <br>

​

Tap: 템포를 잘 모르겠다! 이럴 때 tap 누르면 초시계가 작동하고 다시 누르면 멈춥니다. 템포로 지정돼요.<br>

​

TTS Mode<br>

all: 숫자로 읽어줌 <br>

interval: 밑에 5, 10, 단위로 숫자를 읽어줌 (그 외 비프 소리만 남)<br>