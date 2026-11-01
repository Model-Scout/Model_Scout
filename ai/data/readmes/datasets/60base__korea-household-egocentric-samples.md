---
pretty_name: 60BASE Korea Household Egocentric Samples
language:
- en
- ko
license: other
license_name: 60base-sample-evaluation-1.0
license_link: LICENSE
size_categories:
- n<1K
tags:
- video
- egocentric
- human-demonstration
- household
- physical-ai
- korea
configs:
- config_name: default
  drop_labels: true
  data_files:
  - split: sample
    path: videos/**
---

# 60BASE · Korea Household Egocentric Samples

Twenty household video excerpts from 60BASE's Korea household collection, including four additions prepared on September 27, 2026.
Use this sample pack to inspect the footage and discuss a full-recording request or a custom collection brief.

**[Discuss a data project](https://60base.kr/#contact)** · **[60BASE](https://60base.kr/)** · **[Email](mailto:60base.ai@gmail.com)**

| Included in this release | Specification |
|---|---|
| Video | 20 MP4 clips × 20 seconds; 6 minutes 40 seconds total |
| Tasks | Dishwashing, clothes/towel folding, vegetable/apple preparation, vacuuming, stove cleaning, refrigerator/desk organization, pan cooking, cat litter cleanup, fruit organization, aquarium cleaning |
| Source groups | 17 from the standard source folder; 3 source-flagged recording examples |
| Viewpoint and modality | Egocentric, monocular RGB video |
| Resolution | 720 × 406 for `dishwashing.mp4`; 1280 × 720 for the other 19 clips |
| Preview frame rate | 24 fps for `dishwashing.mp4`; 30 fps for the other 19 clips. New excerpts were resampled to 30 fps. |
| Encoding | H.264; silent excerpts |
| Video download size | See the per-file `size_bytes` values in metadata; approximately 117.85 MB total |
| Metadata | English/Korean task names and summaries, environment, measured video properties, source time interval, SHA-256 |
| Access | Public sample download; full source recordings supplied separately by inquiry and agreement |
| Terms | Internal evaluation, including by commercial teams; see [LICENSE](LICENSE) |

## Watch the samples

<video controls muted playsinline preload="metadata" width="720" src="https://huggingface.co/datasets/60base/korea-household-egocentric-samples/resolve/main/videos/cutting-vegetables.mp4"></video>

| Clip | 한국어 | Duration | Video |
|---|---|---|---|
| Dishwashing | 설거지 | 20 s | [Watch / download](videos/dishwashing.mp4) |
| Folding clothes | 옷 접기 | 20 s | [Watch / download](videos/folding-clothes.mp4) |
| Cutting vegetables | 채소 썰기 | 20 s | [Watch / download](videos/cutting-vegetables.mp4) |
| Vacuuming | 바닥 청소 | 20 s | [Watch / download](videos/vacuuming.mp4) |
| Folding towels | 수건 접기 | 20 s | [Watch / download](videos/folding-towels.mp4) |
| Rinsing dishes | 식기 헹구기 | 20 s | [Watch / download](videos/dishwashing-2.mp4) |
| Wiping a stove | 가스레인지 닦기 | 20 s | [Watch / download](videos/cleaning-stove.mp4) |
| Organizing a refrigerator | 냉장고 정리 | 20 s | [Watch / download](videos/cleaning-refrigerator.mp4) |
| Organizing a desk | 책상 정리 · 상단 마스킹 | 20 s | [Watch / download](videos/cleaning-desk.mp4) |
| Pan cooking | 팬 조리 | 20 s | [Watch / download](videos/cooking-tteokgalbi.mp4) |
| Preparing an apple | 사과 손질 | 20 s | [Watch / download](videos/cutting-apple.mp4) |
| Washing dishes 5 | 식기 세척 5 | 20 s | [Watch / download](videos/dishwashing-5.mp4) |
| Washing dishes 4 | 식기 세척 4 | 20 s | [Watch / download](videos/dishwashing-4.mp4) |
| Cat litter cleanup · source-flagged | 고양이 화장실 청소 · 검수 참고 | 20 s | [Watch / download](videos/cleaning-cat-litter-review.mp4) |
| Dishwashing · source-flagged | 식기 세척 · 검수 참고 | 20 s | [Watch / download](videos/dishwashing-review.mp4) |
| Dishwashing 3 · source-flagged | 식기 세척 3 · 검수 참고 | 20 s | [Watch / download](videos/dishwashing-3-review.mp4) |
| Arranging fruit | 과일 정리 | 20 s | [Watch / download](videos/arranging-fruit.mp4) |
| Washing dishes 7 | 식기 세척 7 | 20 s | [Watch / download](videos/dishwashing-7.mp4) |
| Cleaning a fish tank | 어항 청소 | 20 s | [Watch / download](videos/cleaning-fish-tank.mp4) |
| Organizing a desk 2 | 책상 정리 2 · 상단 마스킹 | 20 s | [Watch / download](videos/cleaning-desk-2.mp4) |

The excerpts show portions of activities; they are not complete task demonstrations.
The captions summarize clip content. They are not frame-level labels, action boundaries or success/failure annotations.

**Source-flagged examples:** three source videos were stored in a folder named `Fail Data`. They are retained as clearly marked recording examples so the complete sample collection can be inspected. The original rejection reasons were not provided. These flags are not labels of whether the household task succeeded, and the other 17 clips are not certified as passed-QC data.
Use `source_quality_group` and `review_label` to distinguish them in the viewer.

## Files and loading

```text
README.md
LICENSE
videos/
  metadata.jsonl
  dishwashing.mp4
  folding-clothes.mp4
  cutting-vegetables.mp4
  vacuuming.mp4
  folding-towels.mp4
  dishwashing-2.mp4
  cleaning-stove.mp4
  cleaning-refrigerator.mp4
  cleaning-desk.mp4
  cooking-tteokgalbi.mp4
  cutting-apple.mp4
  dishwashing-5.mp4
  dishwashing-4.mp4
  cleaning-cat-litter-review.mp4
  dishwashing-review.mp4
  dishwashing-3-review.mp4
  arranging-fruit.mp4
  dishwashing-7.mp4
  cleaning-fish-tank.mp4
  cleaning-desk-2.mp4
```

The pack follows Hugging Face's [VideoFolder layout](https://huggingface.co/docs/hub/en/datasets-video).
Each `file_name` in `videos/metadata.jsonl` is relative to that metadata file.
`sample` is the only split; this release does not define training or evaluation benchmarks.

Download the files without a video-decoding dependency:

```python
from huggingface_hub import snapshot_download

folder = snapshot_download(
    repo_id="60base/korea-household-egocentric-samples",
    repo_type="dataset",
    allow_patterns=["README.md", "LICENSE", "videos/*"],
)
```

Read the metadata through Hugging Face Datasets:

```python
from datasets import Video, load_dataset

samples = load_dataset(
    "60base/korea-household-egocentric-samples", split="sample"
).cast_column("video", Video(decode=False))
print(samples[0]["task_en"], samples[0]["video"])
```

Install `huggingface_hub` for downloading and `datasets` for the second example.
`Video(decode=False)` returns a file reference without decoding frames.

## Collection and preparation

These excerpts come from the twenty owner-provided recordings in the 60BASE Korea household sample collection.
They show everyday tasks in domestic environments. The collection origin is based on the supplied project records; this release does not include GPS evidence, capture dates, participant counts or a verified camera model.

The first six clips preserve the existing website excerpts and their recorded SHA-256 values. Ten more excerpts were prepared after reviewing the source folder on September 20, 2026, and four further excerpts were approved and prepared on September 27, 2026. Every distributed clip was fully decoded before packaging.
Original recordings remain separate. Audio is omitted from the excerpts. High-resolution HDR sources were converted to 720p SDR where applicable; the fourteen later clips use 30 fps output. The provided metadata describes the **distributed clips**, not the source quality or original capture frame rate.

The upper halves of `cleaning-desk.mp4` and `cleaning-desk-2.mp4` are covered by opaque masks to hide screens, photographs or notes while keeping the lower work areas visible. This occlusion limits what can be evaluated from these clips. See `privacy_processing` for the per-clip treatment.

Selected source intervals and scene descriptions were reviewed in the collection records. The ten September 20 excerpts and four September 27 excerpts were visually checked at one frame per second, in addition to source overview frames. The new desk and aquarium excerpts received additional checks at two frames per second. These sampled visual checks do not constitute a privacy audit of the complete originals.
This pack excludes source archives, private collection manifests, participant records and consent documents.

## Intended use and limits

The samples support internal assessment of visual content and delivery compatibility.
They contain **RGB video and clip metadata**. They do not include depth, IMU, calibrated camera poses, hand/joint trajectories, robot action commands or a verified LeRobot conversion.
The small selection is not a representative benchmark of households, people or activities in Korea.

Public download permits the internal evaluation described in the [sample license](LICENSE).
Training, fine-tuning, redistribution and product use require a separate written agreement.

For full recordings or custom collection, share your target tasks, environment, required duration, camera/sensor needs, annotation requirements, intended use and delivery schedule through [60BASE](https://60base.kr/#contact) or **60base.ai@gmail.com**.
Availability, specifications and usage rights are confirmed for each project.

## 한국어 안내

60BASE의 한국 가정 영상 원본 20개에서 각각 발췌한 **20초 샘플 20개, 총 6분 40초**입니다.
설거지·옷 접기·채소 썰기·바닥 청소·수건 접기·가스레인지 닦기·냉장고 정리·팬 조리·사과 손질 등의 장면을 담았습니다. 2026년 9월 27일에 과일 정리·식기 세척 7·어항 청소·책상 정리 2 샘플을 추가했습니다.
영상 파일과 한영 설명, 길이·해상도·프레임률, 원본 내 발췌 구간을 제공합니다.

이 중 3개는 출처의 `Fail Data` 폴더에서 가져온 **검수 참고용 촬영 예시**로 표시했습니다. 분류 사유는 제공되지 않았으며 작업 실패 여부를 뜻하지 않습니다. 책상 정리 영상 2개는 화면·사진·메모를 가리기 위해 상단 절반을 마스킹했습니다.

샘플은 기업을 포함한 내부 검토용으로 내려받을 수 있습니다. 학습·재배포·제품 활용은 별도 협의 대상입니다.
전체 원본 제공과 맞춤 수집은 **[홈페이지 문의](https://60base.kr/#contact)** 또는 **60base.ai@gmail.com**으로 요청해 주세요.
이 샘플에는 로봇 제어값·깊이·IMU·손 관절 좌표가 포함되어 있지 않습니다.
