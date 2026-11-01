---
license: mit
task_categories:
- question-answering
dataset_info:
  features:
    - name: Question
      dtype: string
    - name: Answer
      dtype: string
    - name: Documents
      dtype: string
  splits:
    - name: train
      num_bytes: 3207687
      num_examples: 9547
language:
  - ko
tags:
  - Ask-for-Welfare
  - WelSSiSKo
pretty_name: AskWelfare-v1.0
---

# Dataset Card for Welfare-QA

## Description

대한민국 보건복지부에서 발간하였으며 2023년 5월 11일에 [복지로](https://www.bokjiro.go.kr/ssis-tbu/index.do)에 등록된 안내책자를 바탕으로 만들어졌습니다.
총 413페이지의 비정형 PDF에 담긴 약 460여개의 복지제도에 대한 Question-Answering-Documents 데이터셋입니다.
원본은 다음 링크에서 확인해보실 수 있습니다. [👉 '2023 나에게 힘이되는 복지서비스 PDF 책자'](https://www.bokjiro.go.kr/ssis-tbu/twatxa/wlfarePr/selectWlfareSubMain.do?dmMnuParam=column27)

## Project Repo

- Github Repo : [Ask-for-Welfare](https://github.com/ssisOneTeam/Ask-for-Welfare)

## How to Uses

```python
>>> from datasets import load_dataset
>>> dataset = load_dataset("Ash-Hun/Welfare-QA", split='train')
>>> dataset
Dataset({
    features: ['Question', 'Answer', 'Documents'],
    num_rows: 9547
})
```

```python
>>> dataset[0]
{'Question': 'LPG 사용 가정의 고무호스를 교체하려면 어떤 지원을 받을 수 있나요?',
 'Answer': 'LPG용기 사용가구 시설개선 사업을 통해 LPG 고무호스를 금속배관으로 교체하는 데 필요한 지원을 받으실 수 있습니다.',
 'Documents': 'LPG용기 사용가구 시설개선'}
```

<!---
### Contributors


<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/PangPangGod">
        <img src="https://github.com/PangPangGod.png" width="100px;" alt="송준호"/><br />
        <sub><b>송준호</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ash-hun">
        <img src="https://github.com/ash-hun.png" width="100px;" alt="최재훈"/><br />
        <sub><b>최재훈</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MoonHeesun">
        <img src="https://github.com/MoonHeesun.png" width="100px;" alt="문희선"/><br />
        <sub><b>문희선</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Noveled">
        <img src="https://github.com/Noveled.png" width="100px;" alt="김민식"/><br />
        <sub><b>김민식</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/myeongjun1007">
        <img src="https://github.com/myeongjun1007.png" width="100px;" alt="현명준"/><br />
        <sub><b>현명준</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/kha-jaejun">
        <img src="https://github.com/kha-jaejun.png" width="100px;" alt="가재준"/><br />
        <sub><b>가재준</b></sub>
      </a>
    </td>
  </tr>
</table>
--->
