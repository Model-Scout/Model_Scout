---
dataset_info:
  features:
  - name: title_embeddings
    dtype: float32
    shape: [768]
  - name: content_embeddings
    dtype: float32
    shape: [768]
  - name: labels
    dtype: int64
  - name: article_ids
    dtype: string
  splits:
  - name: train
    num_examples: 466344
  - name: validation
    num_examples: 116588
  - name: test
    num_examples: 72868
language:
- ko
task_categories:
- text-classification
tags:
- clickbait
- korean
- sbert
- news
- embeddings
license: mit
size_categories:
- 100K<n<1M
---

# Korean News Clickbait Classification Embeddings

## 데이터셋 설명

한국어 뉴스 제목의 낚시성(clickbait) 분류를 위한 SBERT 임베딩 데이터셋입니다.

이 데이터셋은 한국어 뉴스 기사의 제목과 본문을 SBERT 모델로 임베딩한 결과물로,
딥러닝 모델 학습에 바로 사용할 수 있도록 전처리되어 있습니다.

### 모델 정보

- **임베딩 모델:** [snunlp/KR-SBERT-V40K-klueNLI-augSTS](https://huggingface.co/snunlp/KR-SBERT-V40K-klueNLI-augSTS)
- **임베딩 차원:** 768
- **언어:** 한국어 (Korean)
- **정규화:** L2 normalized (코사인 유사도 계산에 최적화)

### 데이터 구조

각 `.npz` 파일은 다음 배열들을 포함합니다:

- **title_embeddings**: `(N, 768)` - 제목(title) 임베딩
- **content_embeddings**: `(N, 768)` - 본문(content) 임베딩
- **labels**: `(N,)` - 레이블 (0: 비낚시성, 1: 낚시성)
- **article_ids**: `(N,)` - 기사 고유 ID (참고용, 학습에 사용 금지)

### 데이터셋 통계

| Split | 샘플 수 | 고유 기사 수 | Class 0 (비낚시성) | Class 1 (낚시성) |
|-------|---------|-------------|-------------------|-----------------|
| Train | 466,344 | 233,172 | 50% | 50% |
| Validation | 116,588 | 58,294 | 50% | 50% |
| Test | 72,868 | 36,434 | 50% | 50% |

**총 샘플:** 655,800개
**총 기사:** 327,900개

## 사용 방법

### 1. 기본 로딩

```python
from huggingface_hub import hf_hub_download
import numpy as np

# 데이터 다운로드
train_path = hf_hub_download(
    repo_id="YOUR_USERNAME/clickbait-embeddings",
    filename="train_embeddings.npz",
    repo_type="dataset"
)

# 데이터 로드
data = np.load(train_path)
title_embeddings = data['title_embeddings']  # (466344, 768)
content_embeddings = data['content_embeddings']  # (466344, 768)
labels = data['labels']  # (466344,)
article_ids = data['article_ids']  # 참고용

print(f"Title embeddings shape: {title_embeddings.shape}")
print(f"Content embeddings shape: {content_embeddings.shape}")
print(f"Labels shape: {labels.shape}")
```

### 2. 임베딩 결합 방법

제목과 본문 임베딩을 결합하는 세 가지 방법:

#### 방법 1: 단순 Concatenate (간단함, 추천)

```python
X = np.concatenate([title_embeddings, content_embeddings], axis=1)  # (N, 1536)
y = labels
```

#### 방법 2: 각각 처리 후 결합 (유연함)

```python
import torch
import torch.nn as nn

class ClickbaitClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.title_fc = nn.Linear(768, 256)
        self.content_fc = nn.Linear(768, 256)
        self.classifier = nn.Sequential(
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 2)
        )

    def forward(self, title_emb, content_emb):
        title_out = torch.relu(self.title_fc(title_emb))
        content_out = torch.relu(self.content_fc(content_emb))
        combined = torch.cat([title_out, content_out], dim=1)
        return self.classifier(combined)
```

#### 방법 3: Attention 메커니즘 (고급)

```python
class AttentionClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = nn.MultiheadAttention(768, num_heads=8, batch_first=True)
        self.classifier = nn.Sequential(
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 2)
        )

    def forward(self, title_emb, content_emb):
        # shape: (batch_size, 2, 768)
        x = torch.stack([title_emb, content_emb], dim=1)
        attn_out, _ = self.attention(x, x, x)
        pooled = attn_out.mean(dim=1)  # (batch_size, 768)
        return self.classifier(pooled)
```

### 3. PyTorch 학습 예제

```python
import torch
from torch.utils.data import Dataset, DataLoader

class ClickbaitDataset(Dataset):
    def __init__(self, npz_path):
        data = np.load(npz_path)
        self.title_emb = torch.FloatTensor(data['title_embeddings'])
        self.content_emb = torch.FloatTensor(data['content_embeddings'])
        self.labels = torch.LongTensor(data['labels'])

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.title_emb[idx], self.content_emb[idx], self.labels[idx]

# 데이터 로더 생성
train_dataset = ClickbaitDataset("train_embeddings.npz")
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# 학습 루프
model = ClickbaitClassifier()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(10):
    for title_emb, content_emb, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(title_emb, content_emb)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

### 4. Scikit-learn 예제

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 데이터 로드
train_data = np.load("train_embeddings.npz")
val_data = np.load("val_embeddings.npz")

# Concatenate 방식
X_train = np.concatenate([
    train_data['title_embeddings'],
    train_data['content_embeddings']
], axis=1)
y_train = train_data['labels']

X_val = np.concatenate([
    val_data['title_embeddings'],
    val_data['content_embeddings']
], axis=1)
y_val = val_data['labels']

# 학습
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 평가
y_pred = clf.predict(X_val)
print(classification_report(y_val, y_pred))
```

## 중요 주의사항

### ⚠️ 데이터 리키지 방지

- **Train/Validation/Test 간 `article_id` 중복 없음**
- 각 기사는 하나의 split에만 존재합니다
- `article_ids`는 **학습에 사용하지 마세요** (참고용)

### 📊 데이터 증강 정보

각 기사는 2개의 레코드로 증강되었습니다:
- **레코드 1:** 원본 제목 (낚시성) + 본문 → Label 1
- **레코드 2:** 수정된 제목 (비낚시성) + 본문 → Label 0

따라서 같은 `article_id`를 가진 2개의 레코드가 존재하며,
이들은 항상 같은 split(train/val/test)에 속합니다.

### 💡 팁

1. **베이스라인부터 시작**: 단순 concatenate + MLP로 시작하세요
2. **배치 크기**: GPU 메모리에 따라 32~128 추천
3. **Learning Rate**: 0.001~0.0001 범위에서 시작
4. **Early Stopping**: Validation loss 모니터링 권장
5. **Class Balance**: 데이터가 50:50으로 균형 잡혀있습니다

## 파일 정보

### 임베딩 파일

- `train_embeddings.npz` (~800-1000MB)
- `val_embeddings.npz` (~200-250MB)
- `test_embeddings.npz` (~100-120MB)

### 추가 파일

- `load_example.py` - 전체 사용 예제 코드
- `README.md` - 이 문서

## 성능 벤치마크

모델 개발 시 다음 베이스라인을 목표로 하세요:

| Model | Train Acc | Val Acc | Test Acc |
|-------|-----------|---------|----------|
| Random | 50% | 50% | 50% |
| **목표 베이스라인** | **>85%** | **>80%** | **>80%** |

## 라이센스

MIT License

## Citation

이 데이터셋을 사용하신다면 다음을 인용해주세요:

```bibtex
@dataset{korean_clickbait_embeddings_2025,
  title={Korean News Clickbait Classification Embeddings},
  author={Your Name},
  year={2025},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/datasets/YOUR_USERNAME/clickbait-embeddings}}
}
```

## 문의

질문이나 이슈가 있으시면 HuggingFace Discussions를 이용해주세요.

---

**생성일:** 2025-11-20
**버전:** 1.0
**임베딩 모델:** snunlp/KR-SBERT-V40K-klueNLI-augSTS
**총 샘플:** 655,800개
