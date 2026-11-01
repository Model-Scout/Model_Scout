---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: text
    dtype: string
  - name: contributors
    dtype: string
  - name: type
    dtype: string
  - name: redirect
    list: string
  splits:
  - name: train
    num_bytes: 3059809576
    num_examples: 210484
  download_size: 1766273537
  dataset_size: 3059809576
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-2.0
language:
- ko
tags:
- anime
- game
- comics
size_categories:
- 100K<n<1M
---

# namuwiki-extracted-acg-filtered

ACG(Anime, Comics and Games) filtered version of [heegyu/namuwiki-extracted](https://huggingface.co/datasets/heegyu/namuwiki-extracted)

애니메이션, 만화, 게임 필터링 된 [나무위키 덤프](https://huggingface.co/datasets/heegyu/namuwiki-extracted)입니다.

## How it was made?

### English
1. Remove low effort entries: under 200 char or 3 sentences articles.
2. LLM-as-Judge categorization using [Qwen3-Next-80B-A3B](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
3. Filtered only POI categories ("Game", "Animation", "Comic/Webtoon", "Light novels", "Vocaloid/Doujin music", "Sexual", "Insult/Internet meme", "Vtuber")
4. Add redirect column for synonym

### Korean
1. 토막글 제거: 200 글자 미만 혹은 3문장 이하 문서들
2. [Qwen3-Next-80B-A3B](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)를 사용한 LLM-as-Judge 카테고리화
3. 관심 카테고리만 필터링 ("게임", "애니메이션", "만화/웹툰", "라이트노벨", "보컬로이드/동인음악", "성/섹스", "비속어/인터넷 밈", "버츄얼 유튜버")
4. 동의어를 위해 redirect 컬럼 추가

## Limitation

While I did my best to adjust system prompt for proper categorization, may not perfect.

최대한 분류를 기준에 맞게끔 시스템 프롬프트를 수정했으나, 완벽하지 않습니다.

## Acknowledgement

Thanks to Anonymous who lend me hardware for free.

하드웨어를 대가 없이 지원해주신 익명의 분께 감사 인사 드립니다.