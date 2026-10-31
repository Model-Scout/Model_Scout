---
type: "dataset"
id: "oscar-corpus/OSCAR-2301"
source: "huggingface"
url: "https://huggingface.co/datasets/oscar-corpus/OSCAR-2301"
downloads: 393
summary: "OSCAR 23.01은 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 주로 언어 모델 사전학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# oscar-corpus/OSCAR-2301

> dataset · [Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301)

OSCAR 23.01은 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 주로 언어 모델 사전학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The Open Super-large Crawled Aggregated coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The project focuses specifically in providing large quantities of unannotated raw data that is commonly used in the pre-training of large deep learning models.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The project focuses specifically in providing large quantities of unannotated raw data that is commonly used in the pre-training of large deep learning models.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[BlinkDL__rwkv-5-world|BlinkDL/rwkv-5-world]]
- [[BlinkDL__rwkv-6-world|BlinkDL/rwkv-6-world]]
- [[BlinkDL__rwkv-7-world|BlinkDL/rwkv-7-world]]
- [[BlinkDL__rwkv7-g1|BlinkDL/rwkv7-g1]]
- [[RWKV__RWKV7-1.5B-20260805|RWKV/RWKV7-1.5B-20260805]]
- [[RWKV__RWKV7-13.3B-20260805|RWKV/RWKV7-13.3B-20260805]]
- [[RWKV__RWKV7-2.9B-20260805|RWKV/RWKV7-2.9B-20260805]]
- [[RWKV__RWKV7-7.2B-20260805|RWKV/RWKV7-7.2B-20260805]]
- [[RWKV__RWKV7-G1j-1.5B-20260831|RWKV/RWKV7-G1j-1.5B-20260831]]
- [[RWKV__RWKV7-G1j-13.3B-20260831|RWKV/RWKV7-G1j-13.3B-20260831]]
- [[RWKV__RWKV7-G1j-2.9B-20260831|RWKV/RWKV7-G1j-2.9B-20260831]]
- [[RWKV__RWKV7-G1j-7.2B-20260831|RWKV/RWKV7-G1j-7.2B-20260831]]
- [[RWKV__RWKV7-Goose-World-PTH|RWKV/RWKV7-Goose-World-PTH]]
- [[RWKV__rwkv-5-world-all-pth|RWKV/rwkv-5-world-all-pth]]
- [[SmerkyG__rwkv-5-world-all-pth|SmerkyG/rwkv-5-world-all-pth]]
- [[SmerkyG__rwkv-6-world-all-pth|SmerkyG/rwkv-6-world-all-pth]]
- [[Tweeties__tweety-tatar-hydra-mt-7b-v24a|Tweeties/tweety-tatar-hydra-mt-7b-v24a]]
- [[aabbdev__RWKV7-1.5B-20260805|aabbdev/RWKV7-1.5B-20260805]]
- [[fla-hub__RWKV7-G1j-1.5B-20260831|fla-hub/RWKV7-G1j-1.5B-20260831]]
- [[fla-hub__RWKV7-G1j-13.3B-20260831|fla-hub/RWKV7-G1j-13.3B-20260831]]
- [[fla-hub__RWKV7-G1j-2.9B-20260831|fla-hub/RWKV7-G1j-2.9B-20260831]]
- [[fla-hub__RWKV7-G1j-7.2B-20260831|fla-hub/RWKV7-G1j-7.2B-20260831]]
- [[haoranxu__X-ALMA-13B-Pretrain|haoranxu/X-ALMA-13B-Pretrain]]
