---
license: cc-by-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- n<1K
pretty_name: KoLima(vicuna)
tags:
- KoLima
---

# Ko Lima Vicuna Dataset

GPT4 API를 사용하여 [lima_vicuna_format 데이터](https://huggingface.co/datasets/64bits/lima_vicuna_format)를 한국어로 재생성한 데이터셋입니다.  
GPT4 사용시 프롬프트는 "단순 번역이 아닌, 원문 내용을 참조하여 데이터를 재생성하라"는 내용으로 작성하였습니다.  
원본 데이터셋 1,030건 중 866건의 데이터가 재생성되었습니다.  

*데이터셋 제작은 웹 크롤링 전문 기업, **[해시스크래퍼(HASHSCRAPER)](https://www.hashscraper.com/)** 에서 진행되었습니다.*


*This is the lima_vicuna_format data regenerated into Korean using the GPT4 API.*  
*When using GPT4, the prompt was written to read "Regenerate the data by referring to the original content, not just a simple translation".*  
*Out of the 1,030 original datasets, 866 data points were regenerated.*  

*The dataset was created by [HASHSCRAPER](https://www.hashscraper.com/), a company specializing in web scraping.*

---

# How to use

```python
>>> from datasets import load_dataset

>>> data = load_dataset("changpt/ko-lima-vicuna", data_files="ko_lima_vicuna.json", split="train")


>>> data
Dataset({
    features: ['id', 'conversations'],
    num_rows: 866
})
```

```python
>>> data[0]
{'id': '7-stackexchange',
 'conversations': [{'from': 'human',
   'value': '나는 ```ffmpeg```로 비디오를 GIF 파일로 변환하고 있어:\n```ffmpeg \\\n  -i input.flv \\\n  -ss 00:00:00.000 \\\n  -pix_fmt rgb24 \\\n  -r 10 \\\n  -s 320x240 \\\n  -t 00:00:10.000 \\\n  output.gif\n```\n잘 작동하는데, 출력된 gif 파일의 품질이 너무 낮아. 변환된 gif의 품질을 어떻게 개선할 수 있을까?'},
  {'from': 'gpt',
   'value': '중간 이미지 파일을 피하고 싶다면, LordNeckBeard가 제공한 명령어를 ```ffmpeg```와 ImageMagick의 ```convert``` 사이에 파이프로 연결할 수 있습니다. 이렇게 하면 중간 파일이 필요하지 않습니다:\n```ffmpeg -i input.flv -vf scale=320:-1 -r 10 -f image2pipe -vcodec ppm - | convert -delay 10 -loop 0 - output.gif\n```\n```-f image2pipe```는 ffmpeg에게 비디오를 이미지로 분할하고 파이프 출력에 적합하게 만들라고 지시하며, ```-vcodec ppm```은 출력 형식을 ppm으로 지정합니다(png 형식인 경우, ```convert```가 파이프에서 모든 이미지를 읽지 않거나 ffmpeg가 모두 출력하지 않는 것 같습니다). 두 명령어의 ```-```는 각각 출력과 입력에 파이프를 사용하도록 지정합니다.\n파일을 저장하지 않고 결과를 최적화하려면, ```convert```의 출력을 두 번째 ```convert``` 명령어로 파이프할 수 있습니다:\n```ffmpeg -i input.flv -vf scale=320:-1 -r 10 -f image2pipe -vcodec ppm - | convert -delay 10 -loop 0 - gif:- | convert -layers Optimize - output.gif\n```\n```gif:-```는 ```convert```에게 출력을 gif 형식의 데이터로 파이프하도록 지시하고, ```-layers Optimize```는 두 번째 ```convert```에게 ```optimize-frame``` 및 ```optimize-transparancy``` 방법을 수행하도록 지시합니다(ImageMagick 애니메이션 최적화 소개 참조). ```-layers Optimize```의 출력이 항상 더 작은 파일 크기를 제공하지는 않으므로, 먼저 최적화 없이 gif로 변환해 보는 것이 좋습니다.\n이 과정에서 모든 것이 메모리에 있으므로 이미지가 매우 큰 경우 충분한 메모리가 필요할 수 있습니다.'}]}
```

---

# License

[CC BY 2.0 KR](https://creativecommons.org/licenses/by/2.0/kr/)

[Open AI](https://openai.com/policies/terms-of-use)