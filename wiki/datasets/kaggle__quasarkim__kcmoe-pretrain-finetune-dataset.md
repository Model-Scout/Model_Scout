---
type: "dataset"
id: "kaggle/quasarkim/kcmoe-pretrain-finetune-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/quasarkim/kcmoe-pretrain-finetune-dataset"
downloads: 58
summary: "Kc-MoE 자연어 처리 모델 훈련용 한국어 텍스트 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/quasarkim/kcmoe-pretrain-finetune-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/quasarkim/kcmoe-pretrain-finetune-dataset)

Kc-MoE 자연어 처리 모델 훈련용 한국어 텍스트 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `네이버 영화에서 수집한 리뷰 댓글들의 긍/부정을 분류하는 데이터셋.` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `주어진 두 문장의 의미의 유사성을 측정하는 STS(Semantic Textual Similarity) 데이터셋.` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `NLI는 주어진 전제에 대해 가설이 참인지, 거짓인지, 또는 판단할 수 없는지 구분하는 task다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:question_answering = `뉴스 댓글로 이루어져 있음.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = ``label`: 리뷰의 긍정/부정을 나타내는 항목.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `자연어 처리 모델 훈련에 사용된 데이터셋들입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Datasets used for training Kc-MoE model` · 신뢰도 medium
